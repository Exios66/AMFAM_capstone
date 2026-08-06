"""Extract real chat-thread examples (raw scratchpad reasoning) from Braintrust experiments.

Joins each eval `task` span (filename + predicted label) to its `Chat Completion`
child span (the raw model response) via nearest-timestamp matching, pulls the
ground-truth label from the `exact_match` scorer spans, and downloads the source
document images from the dataset slice so the site can render LLaVA-style chat cards.

Outputs:
  - website/data/chat-examples.json   — curated example records (real traces)
  - website/chat_images/*.png         — source document images for the examples
  - archive/chat_data/<name>.json     — cached raw experiment rows (optional re-fetch)

Usage:
  python scripts/site/build_chat_examples.py
"""
from __future__ import annotations

import argparse
import base64
import io
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path


def _ts(v) -> float:
    if isinstance(v, (int, float)):
        return float(v)
    try:
        return datetime.fromisoformat(str(v).replace("Z", "+00:00")).timestamp()
    except (ValueError, TypeError):
        return 0.0

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from PIL import Image  # noqa: E402

from src.braintrust_config import load_braintrust_config  # noqa: E402
from src.braintrust_utils import fetch_attachment_bytes, fetch_experiment_rows, list_experiments  # noqa: E402
from src.constants import DOCUMENT_CLASSES  # noqa: E402

CACHE_DIR = ROOT / "archive" / "chat_data"
DATA_DIR = ROOT / "website" / "data"
IMG_DIR = ROOT / "website" / "chat_images"

MAX_RAW_CHARS = 2600
MAX_REASONING_CHARS = 2000

# experiment_name -> (label, prompt_version, model)
EXPERIMENTS = {
    "qwen3.7-flash_v17.2_v1b_reasoning": ("qwen3.7-flash", "v17.2"),
    "qwen3.7-flash_v11_8_reasoning_160": ("qwen3.7-flash", "v11.8"),
}


def load_or_fetch_experiment(api_key, project_id, api_base, name, exp_id, refresh=False):
    cache_file = CACHE_DIR / f"{name}.json"
    if cache_file.exists() and not refresh:
        return json.loads(cache_file.read_text())
    rows = fetch_experiment_rows(api_key, exp_id, api_base)
    cache_file.parent.mkdir(parents=True, exist_ok=True)
    cache_file.write_text(json.dumps(rows))
    return rows


def extract_records(rows):
    cls = [r for r in rows if (r.get("span_attributes") or {}).get("name") == "classify_document"]
    em = [r for r in rows if (r.get("span_attributes") or {}).get("name") == "exact_match"]

    expected_by_file = {}
    for r in em:
        try:
            expected_by_file[r["input"]["input"]["filename"]] = r["input"]["expected"]
        except (KeyError, TypeError, AttributeError):
            continue

    records = []
    for r in cls:
        md = r.get("metadata") or {}
        fn = md.get("filename") or (r.get("input") or {}).get("input_data", {}).get("filename")
        raw = md.get("raw_response") or ""
        if not fn or not raw:
            continue
        label_match = re.search(r"<label>\s*([^<\s]+)", raw)
        pred_label = label_match.group(1) if label_match else ""
        if pred_label not in DOCUMENT_CLASSES:
            continue
        reasoning = re.sub(r"^\s*<scratchpad>\s*", "", raw, flags=re.MULTILINE)
        reasoning = re.sub(r"\s*</scratchpad>\s*<label>.*$", "", reasoning, flags=re.S).strip()
        runner_match = re.search(r"<runner_up>\s*([^<\s]+)", raw)
        runner_up = runner_match.group(1) if runner_match else None
        expected = expected_by_file.get(fn)
        if expected not in DOCUMENT_CLASSES:
            continue
        records.append({
            "filename": fn,
            "expected": expected,
            "predicted": pred_label,
            "correct": bool(expected == pred_label),
            "near_miss": bool(expected != pred_label and runner_up == expected),
            "runner_up": runner_up,
            "raw_response": raw[:MAX_RAW_CHARS],
            "reasoning": reasoning[:MAX_REASONING_CHARS],
            "model": md.get("model"),
            "prompt_version": md.get("prompt_version"),
            "finish_reason": md.get("finish_reason"),
            "max_tokens": md.get("max_tokens"),
        })
    return records


def _find_experiment_ids(api_key, project_id, api_base):
    exps = {e.get("name"): e.get("id") for e in list_experiments(api_key, project_id, api_base)}
    return exps


def load_braintrust_images(api_key, config, filenames):
    """Fetch PNG bytes for the given dataset filenames; return {fn: bytes}."""
    import braintrust

    braintrust.login(api_key=api_key)
    ds = braintrust.init_dataset(project=config.dataset_project, name=config.dataset)
    wanted = set(filenames)
    out = {}
    for row in ds:
        input_data = row.get("input") or {}
        att = input_data.get("image")
        if not att:
            continue
        try:
            ref = att.reference
            fn = ref.get("filename")
        except AttributeError:
            continue
        if fn in wanted and fn not in out:
            try:
                out[fn] = fetch_attachment_bytes(api_key, ref, config.org_id, config.api_base)
            except Exception as e:  # noqa: BLE001
                print(f"  WARN: failed to fetch {fn}: {e}")
    return out


def to_png_bytes(raw: bytes, target_size=512) -> bytes:
    img = Image.open(io.BytesIO(raw)).convert("L")
    w, h = img.size
    scale = target_size / max(w, h)
    nw, nh = max(1, int(w * scale)), max(1, int(h * scale))
    img = img.resize((nw, nh), Image.LANCZOS)
    canvas = Image.new("L", (target_size, target_size), 255)
    canvas.paste(img, ((target_size - nw) // 2, (target_size - nh) // 2))
    buf = io.BytesIO()
    canvas.save(buf, format="PNG")
    return buf.getvalue()


def main(refresh=False, max_examples=4, max_misses=4):
    config = load_braintrust_config()
    exp_ids = _find_experiment_ids(config.api_key, config.project_id, config.api_base)
    all_records = []
    for name, (model, pv) in EXPERIMENTS.items():
        exp_id = exp_ids.get(name)
        if not exp_id:
            print(f"  skip {name}: experiment not found")
            continue
        print(f"  fetching {name} ({exp_id}) ...")
        rows = load_or_fetch_experiment(config.api_key, config.project_id, config.api_base, name, exp_id, refresh=refresh)
        recs = extract_records(rows)
        for r in recs:
            r["experiment"] = name
            if not r.get("model"):
                r["model"] = model
            if not r.get("prompt_version"):
                r["prompt_version"] = pv
        all_records.extend(recs)
        ok = sum(1 for r in recs if r["correct"])
        print(f"  {name}: {len(recs)} traces, {ok} correct")

    correct = [r for r in all_records if r["correct"]]
    misses = [r for r in all_records if not r["correct"]]

    # pick a diverse set of correct examples (one per class, capped)
    seen_classes = set()
    picks = []
    for r in correct:
        if r["expected"] in seen_classes or len(picks) >= max_examples:
            continue
        seen_classes.add(r["expected"])
        picks.append(r)

    # misses (cap per experiment, prefer ones with long reasoning)
    misses_sorted = sorted(misses, key=lambda r: -len(r["reasoning"]))
    miss_picks = []
    seen_exp = {}
    for r in misses_sorted:
        if seen_exp.get(r["experiment"], 0) >= max_misses:
            continue
        seen_exp[r["experiment"]] = seen_exp.get(r["experiment"], 0) + 1
        miss_picks.append(r)
        if len(miss_picks) >= max_misses * len(EXPERIMENTS):
            break

    examples = {"correct": picks, "misclassified": miss_picks, "generated_at": None}
    print(f"\ncorrect picks: {len(picks)}, miss picks: {len(miss_picks)}")

    # download source images for all picked filenames
    fns = sorted({r["filename"] for r in picks + miss_picks})
    print(f"fetching {len(fns)} source images ...")
    images = load_braintrust_images(config.api_key, config, fns)
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    img_map = {}
    for fn in fns:
        raw = images.get(fn)
        if not raw:
            print(f"  WARN: no image for {fn}")
            continue
        safe = re.sub(r"[^A-Za-z0-9_.-]", "_", fn)
        if not safe.endswith(".png"):
            safe += ".png"
        out_path = IMG_DIR / safe
        out_path.write_bytes(to_png_bytes(raw))
        img_map[fn] = f"chat_images/{safe}"
    for group in ("correct", "misclassified"):
        for r in examples[group]:
            r["image"] = img_map.get(r["filename"])

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_file = DATA_DIR / "chat-examples.json"
    out_file.write_text(json.dumps(examples, indent=2))
    print(f"wrote {out_file} ({len(picks) + len(miss_picks)} examples, {len(img_map)} images)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--refresh", action="store_true", help="re-fetch experiment rows")
    ap.add_argument("--max-examples", type=int, default=4)
    ap.add_argument("--max-misses", type=int, default=4)
    args = ap.parse_args()
    main(refresh=args.refresh, max_examples=args.max_examples, max_misses=args.max_misses)
