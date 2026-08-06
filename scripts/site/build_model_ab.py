"""Build website/data/model-ab.json — the A/B model & prompt comparator dataset.

Same underlying document image, multiple (model, prompt) responses, so the site
can show *why* different prompts or different models reach (or diverge from) the
same classification. Two axes:

- **Prompt evolution** — qwen/qwen3.7-flash v0 vs v11.8 (and v14/v16/v17 where
  present) on the same image, mined from the committed Monte Carlo corpus
  (`reports/monte_carlo/corpus.jsonl`). Zero network spend.
- **Cross-model** — gemini-2.5-flash-lite, kimi-k2.6, qwen3.5-35b-a3b and
  qwen3.7-flash all running the v11.8 prompt on the shared 160-image slice.
  Reasoning is pulled from the logged Braintrust eval spans (fetched once and
  cached in `archive/model_ab/`), because the corpus does not carry the
  non-qwen reasoning text.

Source document images are downloaded from the Braintrust dataset slices into
``website/chat_images/`` (512px grayscale PNGs, same convention as the chat page).

Usage:
  python scripts/site/build_model_ab.py [--refresh] [--max-images N]
"""
from __future__ import annotations

import argparse
import io
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from PIL import Image  # noqa: E402

from src.braintrust_config import load_braintrust_config  # noqa: E402
from src.braintrust_utils import fetch_attachment_bytes, fetch_experiment_rows, list_experiments  # noqa: E402
from src.constants import DOCUMENT_CLASSES  # noqa: E402

CACHE_DIR = ROOT / "archive" / "model_ab"
DATA_DIR = ROOT / "website" / "data"
IMG_DIR = ROOT / "website" / "chat_images"
CORPUS = ROOT / "reports" / "monte_carlo" / "corpus.jsonl"

MAX_REASONING_CHARS = 1600

# (experiment name prefix) -> (model, prompt_version); resume-loop suffixes like
# `-d558f2bc` are matched by prefix and merged.
CROSS_MODEL_EXPERIMENTS = [
    ("gemini-2.5-flash-lite_v11_8_reasoning_160", "google/gemini-2.5-flash-lite", "v11.8"),
    ("kimi-k2.6_v11_8_reasoning_160", "moonshotai/kimi-k2.6", "v11.8"),
    ("qwen3.5-35b-a3b_v11_8_reasoning_160", "qwen/qwen3.5-35b-a3b", "v11.8"),
    ("qwen3.7-flash_v11_8_reasoning_160_t0_3", "qwen/qwen3.7-flash", "v11.8"),
]


def load_corpus_rows():
    out = []
    for line in CORPUS.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        r = json.loads(line)
        if r.get("reasoning") and r.get("status") != "error":
            out.append(r)
    return out


def extract_record(row: dict) -> dict:
    """Normalize one corpus row into an A/B run record."""
    expected = row["expected"]
    predicted = row["predicted"]
    reasoning = row["reasoning"]
    no_label = predicted not in DOCUMENT_CLASSES
    if no_label:
        # The v0 prompt sometimes returned free-form text with no parseable
        # <label>; the truncated "predicted" then holds prose, not a class.
        predicted = ""
    return {
        "model": row["model"],
        "model_short": row["model"].split("/")[-1],
        "prompt": row["prompt_version"],
        "predicted": predicted,
        "no_label": no_label,
        "correct": bool(expected == predicted),
        "expected": row["expected"],
        "reasoning": reasoning[:MAX_REASONING_CHARS],
        "reasoning_len": len(reasoning),
        "runner_up": extract_runner_up(reasoning),
        "dataset": row.get("dataset") or "",
    }


def extract_runner_up(reasoning: str) -> str:
    m = re.search(r"[Rr]unner[-_ ]?up\s*:\s*([a-z_]+)", reasoning)
    return m.group(1) if m else ""


def span_to_record(span: dict, model: str, prompt_version: str) -> dict | None:
    """Turn one Braintrust eval span (with raw_response metadata) into an A/B run."""
    md = span.get("metadata") or {}
    raw = md.get("raw_response") or ""
    fn = md.get("filename") or (span.get("input") or {}).get("input_data", {}).get("filename")
    if not fn or not raw:
        return None
    label_match = re.search(r"<label>\s*([^<\s]+)", raw)
    if not label_match:
        return None
    predicted = label_match.group(1)
    if predicted not in DOCUMENT_CLASSES:
        return None
    reasoning = re.sub(r"^\s*<scratchpad>\s*", "", raw, flags=re.MULTILINE)
    reasoning = re.sub(r"\s*</scratchpad>\s*<label>.*$", "", reasoning, flags=re.S).strip()
    # expected comes from the exact_match scorer span, resolved by the caller
    return {
        "filename": fn,
        "expected": None,  # filled in by caller
        "model": model,
        "model_short": model.split("/")[-1],
        "prompt": prompt_version,
        "predicted": predicted,
        "no_label": False,
        "correct": None,  # filled in by caller
        "reasoning": reasoning[:MAX_REASONING_CHARS],
        "reasoning_len": len(reasoning),
        "runner_up": extract_runner_up(reasoning),
        "dataset": "",
    }


def fetch_experiment(name: str, exp_id: str, api_key: str, api_base: str, refresh: bool = False):
    cache_file = CACHE_DIR / f"{name}.json"
    if cache_file.exists() and not refresh:
        return json.loads(cache_file.read_text(encoding="utf-8"))
    rows = fetch_experiment_rows(api_key, exp_id, api_base)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_file.write_text(json.dumps(rows), encoding="utf-8")
    return rows


def build_prompt_evolution(rows: list[dict]) -> list[dict]:
    """qwen3.7-flash runs grouped by image; images with >=2 distinct prompts."""
    by_file: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        if r["model"] != "qwen/qwen3.7-flash":
            continue
        by_file[r["filename"]].append(extract_record(r))
    images = []
    for fn, runs in by_file.items():
        prompts = {r["prompt"] for r in runs}
        if len(prompts) < 2:
            continue
        images.append({
            "filename": fn,
            "expected": _expected_of(runs),
            "axis": "prompt_evolution",
            "runs": sorted(runs, key=lambda r: _pv_sort(r["prompt"])),
        })
    return images


def _expected_of(runs: list[dict]) -> str:
    return runs[0].get("expected") or ""


def _pv_sort(pv: str):
    m = re.match(r"v(\d+(?:\.\d+)?)", pv or "")
    return (m.group(1).split(".")[0].zfill(3), m.group(1)) if m else (pv or "")


def build_cross_model(rows: list[dict], span_records: dict[str, list[dict]]) -> list[dict]:
    """All v11.8 runs per image across the four models."""
    # corpus qwen3.7 v11.8 runs (the t0_3 160-slice experiment)
    all_runs: dict[str, list[dict]] = defaultdict(list)
    for r in rows:
        if r["model"] == "qwen/qwen3.7-flash" and r["prompt_version"] == "v11.8":
            rec = extract_record(r)
            all_runs[r["filename"]].append(rec)
    # merge with fetched spans
    for fn, recs in span_records.items():
        all_runs[fn].extend(recs)
    images = []
    for fn, runs in all_runs.items():
        models = {r["model"] for r in runs}
        if len(models) < 2:
            continue
        runs = [r for r in runs if r["expected"]]
        if not runs:
            continue
        expected = runs[0]["expected"]
        for r in runs:
            r["correct"] = bool(r["predicted"] == expected)
        images.append({
            "filename": fn,
            "expected": expected,
            "axis": "cross_model",
            "runs": sorted(runs, key=lambda r: r["model"]),
        })
    return images


def _class_key(fn: str) -> str:
    m = re.search(r"rvl_cdip__([a-z_]+)__", fn)
    return m.group(1) if m else ""


def dedupe_runs(runs: list[dict]) -> list[dict]:
    """One run per (model, prompt), keeping the most complete reasoning."""
    best: dict[tuple, dict] = {}
    for r in runs:
        key = (r["model"], r["prompt"])
        prev = best.get(key)
        if prev is None or len(r["reasoning"]) > len(prev["reasoning"]):
            best[key] = r
    return list(best.values())


def curate(images: list[dict], max_total: int) -> list[dict]:
    """Pick the most illustrative images per axis. Roughly 60/40
    prompt-evolution / cross-model, favouring correctness flips."""
    prompt_evo = [i for i in images if i["axis"] == "prompt_evolution"]
    cross = [i for i in images if i["axis"] == "cross_model"]

    def flips(im):
        return sum(1 for a in im["runs"] for b in im["runs"] if a["correct"] != b["correct"]) // 2

    def disagreements(im):
        return len({r["predicted"] for r in im["runs"]}) - 1

    def score(im):
        return flips(im) * 10 + disagreements(im) + max(len(r["reasoning"]) for r in im["runs"]) / 5000.0

    picks: list[dict] = []
    seen: set[str] = set()

    evo_budget = max(1, int(max_total * 0.6))
    evo_sorted = sorted(prompt_evo, key=score, reverse=True)
    cross_sorted = sorted(cross, key=score, reverse=True)

    for im in evo_sorted + cross_sorted:
        if im["filename"] in seen:
            continue
        want_cross = im["axis"] == "cross_model"
        if want_cross and sum(1 for p in picks if p["axis"] == "cross_model") >= (max_total - evo_budget):
            continue
        if not want_cross and sum(1 for p in picks if p["axis"] == "prompt_evolution") >= evo_budget:
            continue
        picks.append(im)
        seen.add(im["filename"])
        if len(picks) >= max_total:
            break
    return picks[:max_total]


# ---------------------------------------------------------------------------
# Images
# ---------------------------------------------------------------------------

def fetch_images(api_key, config, images: list[dict], datasets: list[str]) -> dict[str, str]:
    """Download 512px grayscale PNGs for every curated filename -> image path."""
    import braintrust

    wanted = sorted({im["filename"] for im in images})
    raw_map: dict[str, bytes] = {}
    for ds in datasets:
        try:
            dataset = braintrust.init_dataset(project=config.dataset_project, name=ds)
        except Exception as e:  # noqa: BLE001
            print(f"  WARN: cannot open dataset {ds}: {e}")
            continue
        for row in dataset:
            input_data = row.get("input") or {}
            att = input_data.get("image")
            if not att:
                continue
            try:
                fn = att.reference.get("filename")
            except AttributeError:
                continue
            if fn in wanted and fn not in raw_map:
                try:
                    raw_map[fn] = fetch_attachment_bytes(api_key, att.reference, config.org_id, config.api_base)
                except Exception as e:  # noqa: BLE001
                    print(f"  WARN: failed to fetch {fn}: {e}")
        if len(raw_map) >= len(wanted):
            break
    IMG_DIR.mkdir(parents=True, exist_ok=True)
    out = {}
    for fn in wanted:
        raw = raw_map.get(fn)
        if not raw:
            print(f"  WARN: no image for {fn}")
            continue
        safe = re.sub(r"[^A-Za-z0-9_.-]", "_", fn)
        if not safe.endswith(".png"):
            safe += ".png"
        out_path = IMG_DIR / safe
        if not out_path.exists():
            out_path.write_bytes(to_png_bytes(raw))
        out[fn] = f"chat_images/{safe}"
    return out


def to_png_bytes(raw: bytes, target_size: int = 512) -> bytes:
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


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main(refresh: bool = False, max_images: int = 20) -> None:
    config = load_braintrust_config()
    corpus_rows = load_corpus_rows()
    print(f"corpus rows (reasoning): {len(corpus_rows)}")

    # 1. Prompt evolution (corpus only)
    prompt_evo = build_prompt_evolution(corpus_rows)
    print(f"prompt-evolution images: {len(prompt_evo)}")

    # 2. Cross-model (fetch spans for gemini/kimi/qwen3.5, cache in archive/)
    exps = {e.get("name"): e.get("id") for e in list_experiments(config.api_key, config.project_id, config.api_base)}
    span_records: dict[str, list[dict]] = defaultdict(list)
    for prefix, model, pv in CROSS_MODEL_EXPERIMENTS:
        for name, exp_id in exps.items():
            if not name.startswith(prefix):
                continue
            print(f"  fetch {name} ...")
            rows = fetch_experiment(name, exp_id, config.api_key, config.api_base, refresh=refresh)
            em_expected = {}
            for r in rows:
                if (r.get("span_attributes") or {}).get("name") == "exact_match":
                    try:
                        em_expected[r["input"]["input"]["filename"]] = r["input"]["expected"]
                    except (KeyError, TypeError):
                        continue
            for r in rows:
                if (r.get("span_attributes") or {}).get("name") != "classify_document":
                    continue
                rec = span_to_record(r, model, pv)
                if not rec:
                    continue
                rec["expected"] = em_expected.get(rec["filename"])
                if rec["expected"] and rec["expected"] in DOCUMENT_CLASSES:
                    rec["correct"] = bool(rec["predicted"] == rec["expected"])
                    span_records[rec["filename"]].append(rec)
    print(f"cross-model span records: {sum(len(v) for v in span_records.values())} "
          f"across {len(span_records)} files")

    cross = build_cross_model(corpus_rows, span_records)
    print(f"cross-model images (>=2 models): {len(cross)}")

    # 3. Curate + dedupe (an image might be both axes; keep the richer one)
    images = curate(prompt_evo + cross, max_images)
    seen = set()
    unique = []
    for im in images:
        if im["filename"] in seen:
            continue
        seen.add(im["filename"])
        unique.append(im)
    images = unique
    print(f"curated: {len(images)} images "
          f"({sum(1 for i in images if i['axis'] == 'prompt_evolution')} prompt-evolution, "
          f"{sum(1 for i in images if i['axis'] == 'cross_model')} cross-model)")

    # 4. Fetch images
    datasets = sorted({r.get("dataset") for im in images for r in im["runs"] if r.get("dataset")})
    if any(i["axis"] == "cross_model" for i in images):
        datasets.append(config.dataset)
    print(f"fetching images from datasets: {datasets}")
    img_map = fetch_images(config.api_key, config, images, sorted(set(datasets)))

    # 5. Emit
    for im in images:
        im["image"] = img_map.get(im["filename"])
        runs = dedupe_runs(im["runs"])
        im["runs"] = [
            {
                "model_short": r["model_short"],
                "model": r["model"],
                "prompt": r["prompt"],
                "predicted": r["predicted"],
                "no_label": r.get("no_label", False),
                "correct": r["correct"],
                "reasoning_len": r["reasoning_len"],
                "runner_up": r.get("runner_up", ""),
                "reasoning": r["reasoning"],
            }
            for r in runs
        ]
        im["runs"].sort(key=lambda r: (r["prompt"] if im["axis"] == "prompt_evolution" else r["model_short"]))
    payload = {
        "generated": "build_model_ab.py",
        "meta": {
            "count": len(images),
            "prompt_evolution": sum(1 for i in images if i["axis"] == "prompt_evolution"),
            "cross_model": sum(1 for i in images if i["axis"] == "cross_model"),
            "note": "Real logged traces: same image, different prompts/models. "
                    "Prompt evolution = qwen3.7-flash v0 vs v11.8+ from the Monte Carlo corpus; "
                    "cross-model = the four models on the shared 160-image slice at v11.8.",
        },
        "images": images,
    }
    out = DATA_DIR / "model-ab.json"
    out.write_text(json.dumps(payload, indent=1), encoding="utf-8")
    n_runs = sum(len(im["runs"]) for im in images)
    print(f"wrote {out} ({len(images)} images, {n_runs} runs, {len(img_map)} images fetched)")


if __name__ == "__main__":
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--refresh", action="store_true", help="re-fetch cached experiment spans")
    ap.add_argument("--max-images", type=int, default=20)
    args = ap.parse_args()
    main(refresh=args.refresh, max_images=args.max_images)
