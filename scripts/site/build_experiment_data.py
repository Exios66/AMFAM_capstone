"""Build the website's interactive data layer from committed markdown reports.

Deterministic, offline, no API access: every record is parsed from markdown
tables that are already committed to the repository. Outputs four JSON files
into ``website/data/`` that feed the Observable-JS interactive pages and the
ipywidgets notebook:

- ``experiments.json``         — per-run records (model, prompt version, slice,
  accuracy, tokens, cost, settings) from ``docs/experiments/experiment_log.md``
  and ``reports/experiment_reports/*.md``
- ``cost-models.json``         — per-model single-image token usage + billed
  cost from OpenRouter (``docs/experiments/1pic_cost_estimation.md``); input/
  output prices are derived from the OpenRouter-reported metrics
- ``per-class-accuracy.json``  — per-class correct/total per report file
- ``confusion-matrices.json``  — 16x16 count grids per confusion-matrix file

Usage:
    python scripts/site/build_experiment_data.py
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "website" / "data"

sys.path.insert(0, str(ROOT))
from src.constants import DOCUMENT_CLASSES  # noqa: E402

CLASSES = list(DOCUMENT_CLASSES)


def _norm(s: str) -> str:
    return s.strip().strip("`").strip("*").strip()


def _num(s: str):
    s = s.replace(",", "").replace("$", "").strip()
    if s.endswith("%"):
        s = s[:-1]
    try:
        return float(s)
    except ValueError:
        return None


def _parse_accuracy_cell(value: str):
    """Turn '87.11% (277/318)' or '925/1120 (82.6%)' into (acc, correct, total)."""
    m = re.search(r"(\d+)\s*/\s*(\d+)", value)
    correct = total = None
    if m:
        correct, total = int(m.group(1)), int(m.group(2))
    pct = re.search(r"([\d.]+)\s*%", value)
    acc = float(pct.group(1)) / 100 if pct else (correct / total if total else None)
    return acc, correct, total


# ---------------------------------------------------------------------------
# 1. Experiment records
# ---------------------------------------------------------------------------

HEADING_RE = re.compile(
    r"^## Experiment:\s*`?([^`]+?)`?\s*—\s*(\d+)\s*[Ii]mages?"
)
EXP_ID_RE = re.compile(r"Experiment ID[:\s]*`?([\w-]+)`?")


def _model_short(model: str) -> str:
    return model.split("/")[-1]


def parse_experiment_log(md_text: str) -> list[dict]:
    """Parse the ``## Experiment:`` sections of the experiment log."""
    records = []
    cur: dict | None = None
    metric_table = False
    in_cost_table = False
    for line in md_text.splitlines():
        h = HEADING_RE.search(line)
        if h:
            if cur is not None and cur.get("accuracy") is not None:
                records.append(cur)
            cur = {
                "model": _norm(h.group(1)),
                "images": int(h.group(2)),
                "accuracy": None,
            }
            metric_table = False
            in_cost_table = False
            continue
        if cur is None:
            continue
        stripped = line.strip()
        if stripped.startswith("**Dataset:**"):
            cur["dataset"] = _norm(stripped.removeprefix("**Dataset:**"))
        elif stripped.startswith("**Prompt:**"):
            prompt = stripped.removeprefix("**Prompt:**")
            vm = re.search(r"`?(v\d+(?:\.\d+)?)`?", prompt)
            cur["prompt_version"] = vm.group(1) if vm else "unknown"
        elif stripped.startswith("**Model:**"):
            cur["model"] = _norm(stripped.removeprefix("**Model:**"))
        elif stripped.startswith("**Settings:**"):
            settings = stripped.removeprefix("**Settings:**")
            mt = re.search(r"max_tokens=(\d+)", settings)
            tt = re.search(r"temperature=([\d.]+)", settings)
            rt = re.search(r"reasoning\.effort=([\w]+)", settings)
            if mt:
                cur["max_tokens"] = int(mt.group(1))
            if tt:
                cur["temperature"] = float(tt.group(1))
            if rt:
                cur["reasoning"] = rt.group(1)
        elif EXP_ID_RE.search(stripped):
            cur["id"] = EXP_ID_RE.search(stripped).group(1)
        elif "Experiment:" in stripped and "—" not in stripped and "images" in stripped.lower():
            m = re.match(r".*`?([\w/-]+)`?.*(\d+)\s*[Ii]mages", stripped)
            if m and cur.get("model") is None:
                cur["model"] = _norm(m.group(1))
                cur["images"] = int(m.group(2))

        if stripped.startswith("| Metric |"):
            metric_table = True
            continue
        if stripped.startswith("### Cost Projections"):
            in_cost_table = True
            metric_table = False
            cur.setdefault("cost_scale", {})
            continue
        if stripped.startswith("| Images |"):
            if in_cost_table:
                continue
            metric_table = False
        if in_cost_table and stripped.startswith("|"):
            cells = [_norm(c) for c in stripped.strip("|").split("|")]
            scale_map = {"800": 800, "25,000": 25000, "320,000": 320000}
            if len(cells) >= 2 and cells[0] in scale_map:
                cost = _num(cells[-1])
                if cost is not None:
                    cur["cost_scale"][scale_map[cells[0]]] = cost
            continue
        if metric_table and stripped.startswith("|"):
            cells = [_norm(c) for c in stripped.strip("|").split("|")]
            if len(cells) >= 2:
                key, value = cells[0], cells[1]
                if "Accuracy" in key or "exact_match" in key:
                    acc, correct, total = _parse_accuracy_cell(value)
                    cur["accuracy"] = acc
                    cur["correct"] = correct
                    cur["total"] = total
                elif key.lower().startswith("errors"):
                    cur["errors"] = int(_num(value) or 0)
                elif key == "Prompt tokens (avg)":
                    cur["prompt_tokens_avg"] = _num(value)
                elif key == "Prompt cached tokens (avg)":
                    cur["prompt_cached_tokens_avg"] = _num(value)
                elif key == "Completion tokens (avg)":
                    cur["completion_tokens_avg"] = _num(value)
                elif key == "Completion reasoning tokens (avg)":
                    cur["completion_reasoning_tokens_avg"] = _num(value)
                elif key == "Total tokens (avg)":
                    cur["total_tokens_avg"] = _num(value)
                elif key == "Expected cost":
                    cur["expected_cost"] = _num(value)
                elif key == "Actual cost":
                    cur["actual_cost"] = _num(value)
        if stripped.startswith("## "):
            metric_table = False
            in_cost_table = False
    if cur is not None and cur.get("accuracy") is not None:
        records.append(cur)
    return records


def parse_report_files(files: list[Path]) -> list[dict]:
    records = []
    for path in sorted(files):
        text = path.read_text(encoding="utf-8")
        rec: dict = {
            "name": path.stem,
            "id": path.stem,
            "source": f"reports/experiment_reports/{path.name}",
            "accuracy": None,
        }
        for line in text.splitlines():
            s = line.strip()
            if s.startswith("**Model:**"):
                rec["model"] = _norm(s.removeprefix("**Model:**"))
            elif s.startswith("**Prompt version:**"):
                rec["prompt_version"] = _norm(s.removeprefix("**Prompt version:**"))
            elif s.startswith("**Dataset:**"):
                ds = s.removeprefix("**Dataset:**")
                m = re.search(r"(\d+)\s*per class", ds)
                rec["dataset"] = _norm(ds)
                if m:
                    rec["images"] = int(m.group(1)) * len(CLASSES)
            elif "**Accuracy (exact_match)**" in s:
                value = _norm(s.split("|")[2] if s.count("|") else s.split("**", 2)[-1])
                acc, correct, total = _parse_accuracy_cell(value)
                rec["accuracy"] = acc
                rec["correct"] = correct
                rec["total"] = total
            elif s.startswith("| Scored rows |"):
                rec["scored_rows"] = int(_num(s.split("|")[2]) or 0)
            elif s.startswith("| Failed/empty rows |"):
                rec["failed_rows"] = int(_num(s.split("|")[2]) or 0)
            elif s.startswith("| Prompt tokens (avg) |"):
                rec["prompt_tokens_avg"] = _num(s.split("|")[2])
            elif s.startswith("| Prompt cached tokens (avg) |"):
                rec["prompt_cached_tokens_avg"] = _num(s.split("|")[2])
            elif s.startswith("| Completion tokens (avg) |"):
                rec["completion_tokens_avg"] = _num(s.split("|")[2])
            elif s.startswith("| Completion reasoning tokens (avg) |"):
                rec["completion_reasoning_tokens_avg"] = _num(s.split("|")[2])
            elif s.startswith("| Total tokens (avg) |"):
                rec["total_tokens_avg"] = _num(s.split("|")[2])
            elif s.startswith("| **Expected cost**"):
                rec["expected_cost"] = _num(s.split("|")[2])
            elif s.startswith("| **Actual cost**"):
                rec["actual_cost"] = _num(s.split("|")[2])
            elif s.startswith("| 800 |"):
                cells = [_norm(c) for c in s.strip("|").split("|")]
                if len(cells) >= 3 and cells[1].startswith("$"):
                    rec.setdefault("cost_scale", {})[800] = _num(cells[-1])
            elif s.startswith("| 25,000 |"):
                cells = [_norm(c) for c in s.strip("|").split("|")]
                if len(cells) >= 3 and cells[1].startswith("$"):
                    rec.setdefault("cost_scale", {})[25000] = _num(cells[-1])
            elif s.startswith("| 320,000 |"):
                cells = [_norm(c) for c in s.strip("|").split("|")]
                if len(cells) >= 3 and cells[1].startswith("$"):
                    rec.setdefault("cost_scale", {})[320000] = _num(cells[-1])
        rec["images"] = rec.get("images") or rec.get("total") or 0
        if rec.get("accuracy") is not None:
            records.append(rec)
    return records


def _merge_records(log_recs: list[dict], report_recs: list[dict]) -> list[dict]:
    merged: dict[str, dict] = {}
    for rec in log_recs:
        key = rec.get("id") or f"{rec.get('model')}_{rec.get('images')}"
        rec.setdefault("name", key)
        rec["source"] = rec.get("source", "docs/experiments/experiment_log.md")
        merged.setdefault(key, rec)
    for rec in report_recs:
        key = rec["id"]
        existing = merged.get(key)
        if existing and existing.get("accuracy") is not None:
            merged[key] = {**rec, **{k: v for k, v in existing.items() if v is not None}}
        else:
            merged[key] = rec
    out = []
    for rec in merged.values():
        rec.setdefault("model_short", _model_short(rec.get("model", "")))
        rec.setdefault("prompt_version", "unknown")
        rec.setdefault("dataset", "unknown")
        rec["images"] = rec.get("images") or 0
        if rec.get("accuracy") is None:
            continue
        out.append(rec)
    seen: dict[tuple, dict] = {}
    for rec in out:
        sig = (
            rec.get("model_short"),
            rec.get("prompt_version"),
            rec.get("images"),
            round(rec.get("accuracy") or 0, 4),
        )
        prev = seen.get(sig)
        if prev is None:
            seen[sig] = rec
        elif rec.get("id") and not prev.get("id"):
            seen[sig] = rec
        elif rec.get("id") and prev.get("id"):
            seen[sig] = {**rec, **{k: v for k, v in prev.items() if v is not None}}
    out = list(seen.values())
    out.sort(key=lambda r: (r.get("prompt_version", ""), r.get("model_short", ""), r.get("images", 0)))
    return out


# ---------------------------------------------------------------------------
# 2. Cost models (OpenRouter-reported metrics)
# ---------------------------------------------------------------------------

MODEL_SECTION_RE = re.compile(r"^## Model\s+\d+:\s*`([^`]+)`")


def parse_cost_models(md_text: str) -> list[dict]:
    models = []
    cur: dict | None = None
    in_usage = False
    in_proj = False
    for line in md_text.splitlines():
        s = line.strip()
        m = MODEL_SECTION_RE.match(s)
        if m:
            if cur is not None and cur.get("prompt_tokens"):
                models.append(cur)
            cur = {"model": _norm(m.group(1))}
            in_usage = in_proj = False
            continue
        if cur is None:
            continue
        if "Single-Image Usage" in s:
            in_usage = True
            continue
        if "Cost Projections" in s:
            in_usage = False
            in_proj = True
            cur.setdefault("projections", {})
            continue
        if in_usage:
            m = re.match(r"[-*]\s+\*\*([^*]+)\*\*\s*\$?([\d,]+\.?\d*)", s)
            if not m:
                m = re.match(r"[-*]\s+([^*:]+?):\s*\$?([\d,]+\.?\d*)", s)
            if m:
                key = m.group(1).strip().rstrip(":")
                val = float(m.group(2).replace(",", ""))
                if key == "Prompt tokens":
                    cur["prompt_tokens"] = int(val)
                elif key == "Completion tokens":
                    cur["completion_tokens"] = int(val)
                elif key == "Total tokens":
                    cur["total_tokens"] = int(val)
                elif key == "Actual upstream cost":
                    cur["actual_cost_per_image"] = val
                elif key == "Prompt cost":
                    cur["prompt_cost_per_image"] = val
                elif key == "Completion cost":
                    cur["completion_cost_per_image"] = val
        if in_proj and s.startswith("|"):
            cells = [_norm(c) for c in s.strip("|").split("|")]
            scale_map = {"800": 800, "25,000": 25000, "320,000": 320000}
            if len(cells) >= 2 and cells[0] in scale_map:
                cost = _num(cells[-1])
                if cost is not None:
                    cur["projections"][scale_map[cells[0]]] = cost
    if cur is not None and cur.get("prompt_tokens"):
        models.append(cur)
    for m in models:
        p = m.get("prompt_cost_per_image")
        pc = m.get("prompt_tokens")
        cc = m.get("completion_cost_per_image")
        ct = m.get("completion_tokens")
        m["input_price_per_m"] = round(p * 1e6 / pc, 6) if p is not None and pc else None
        m["output_price_per_m"] = round(cc * 1e6 / ct, 6) if cc is not None and ct else None
        m["model_short"] = _model_short(m["model"])
    return models


# ---------------------------------------------------------------------------
# 3. Per-class accuracy
# ---------------------------------------------------------------------------

def parse_per_class(md_text: str) -> dict:
    out = {}
    for line in md_text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [_norm(c) for c in line.strip().strip("|").split("|")]
        if len(cells) >= 4 and cells[0] in CLASSES:
            try:
                correct = int(cells[1])
                total = int(cells[2])
            except ValueError:
                continue
            out[cells[0]] = {
                "correct": correct,
                "total": total,
                "accuracy": round(correct / total, 4) if total else 0.0,
            }
    return out


# ---------------------------------------------------------------------------
# 4. Confusion matrices
# ---------------------------------------------------------------------------

CM_ROW_RE = re.compile(r"^\|\s*`?([a-zA-Z_]+)`?\s*\|(.*)\|")


def parse_confusion_matrix(md_text: str) -> dict:
    in_counts = False
    rows: list[list[int]] = []
    labels: list[str] = []
    for line in md_text.splitlines():
        if line.strip().startswith("## Raw Counts"):
            in_counts = True
            continue
        if in_counts:
            if line.strip().startswith("| Expected"):
                continue
            if line.strip().startswith("|---"):
                continue
            if line.strip().startswith("## "):
                break
            m = CM_ROW_RE.match(line)
            if not m:
                continue
            label = _norm(m.group(1))
            if label in ("__invalid__", "invalid") or not label:
                continue
            cells = [c.strip() for c in m.group(2).split("|")]
            cells = [c for c in cells if c != ""]
            values = []
            for cell in cells:
                if cell in (".", "—", "-", "**.**"):
                    values.append(0)
                else:
                    digits = re.sub(r"[^\d]", "", cell)
                    values.append(int(digits) if digits else 0)
            rows.append(values[: len(CLASSES)])
            labels.append(label)
    matrix = []
    for r in rows[: len(CLASSES)]:
        matrix.append(r[: len(CLASSES)] + [0] * max(0, len(CLASSES) - len(r)))
    return {"labels": labels[: len(CLASSES)], "matrix": matrix}


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    log_path = ROOT / "docs" / "experiments" / "experiment_log.md"
    report_files = sorted((ROOT / "reports" / "experiment_reports").glob("report_*.md"))
    cost_path = ROOT / "docs" / "experiments" / "1pic_cost_estimation.md"

    log_recs = parse_experiment_log(log_path.read_text(encoding="utf-8"))
    report_recs = parse_report_files(report_files)
    experiments = _merge_records(log_recs, report_recs)

    experiments_json = {
        "experiments": experiments,
        "meta": {
            "generated_from": [
                "docs/experiments/experiment_log.md",
                "reports/experiment_reports/*.md",
            ],
            "count": len(experiments),
            "classes": CLASSES,
        },
    }

    cost_models = parse_cost_models(cost_path.read_text(encoding="utf-8"))
    cost_json = {
        "models": cost_models,
        "meta": {
            "generated_from": "docs/experiments/1pic_cost_estimation.md",
            "note": "token counts and billed cost are OpenRouter-reported metrics; "
                    "input/output prices are derived from those metrics.",
            "count": len(cost_models),
        },
    }

    per_class: dict[str, dict] = {}
    pca_files = report_files + [
        ROOT / "reports" / "experiment_reports" / "qwen3.7-flash_v11.8_1600_balanced_1120_final.md"
    ]
    for path in pca_files:
        pca = parse_per_class(path.read_text(encoding="utf-8"))
        if pca:
            per_class[path.stem] = pca

    confusion: dict[str, dict] = {}
    for path in sorted((ROOT / "reports" / "confusion_matrices").glob("confusion_matrix_*.md")):
        cm = parse_confusion_matrix(path.read_text(encoding="utf-8"))
        if cm["matrix"]:
            key = path.name.removeprefix("confusion_matrix_").removesuffix(".md")
            confusion[key] = cm

    def _write(name: str, payload: dict) -> None:
        out = DATA_DIR / name
        out.write_text(json.dumps(payload, indent=2) + "\n", encoding="utf-8")
        print(f"  wrote {out.name}")

    _write("experiments.json", experiments_json)
    _write("cost-models.json", cost_json)
    _write("per-class-accuracy.json", per_class)
    _write("confusion-matrices.json", confusion)
    print(
        f"Done: {len(experiments)} experiments, {len(cost_models)} cost models, "
        f"{len(per_class)} per-class tables, {len(confusion)} confusion matrices."
    )


if __name__ == "__main__":
    main()
