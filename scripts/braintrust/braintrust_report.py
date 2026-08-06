"""
Generate a full experiment report from Braintrust for a given experiment:
accuracy + per-class, confusion matrix (PNG + markdown), misclassification
analysis with reasoning traces, and expected-vs-actual cost breakdown.

Usage:
    python scripts/braintrust/braintrust_report.py --experiment qwen3.7-flash_v8.5_reasoning
      --model qwen/qwen3.7-flash --prompt-version v8.5 --dataset fixed_size_sampled
      --images-per-class 10 --image-size 1024x1024 --input-price 0.03 --output-price 0.13
"""

import argparse
import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from src.braintrust_config import load_braintrust_config
from src.braintrust_utils import fetch_experiment_rows, list_experiments
from src.constants import DOCUMENT_CLASSES
from src.env_utils import require_env

VALID_CLASSES = DOCUMENT_CLASSES
_CONFIG = load_braintrust_config()
API_BASE = _CONFIG.api_base.rstrip("/") + "/v1"
PROJECT_ID = _CONFIG.project_id


def fetch_experiment(api_key: str, experiment_name: str, project_id: str) -> tuple[list[dict], dict]:
    experiments = list_experiments(api_key, project_id, API_BASE)
    meta = next((e for e in experiments if e["name"] == experiment_name), None)
    if not meta:
        print(f"Error: experiment '{experiment_name}' not found in project {project_id}.")
        sys.exit(1)

    rows = fetch_experiment_rows(api_key, meta["id"], API_BASE)
    print(f"  Fetched {len(rows)} rows")
    return rows, meta


def build_results(rows: list[dict]) -> tuple[list[dict], list[dict]]:
    # Index span-level metadata (reasoning, filename) and metrics by root_span_id.
    span_meta = {}
    span_metrics = {}
    for row in rows:
        root_span_id = row.get("root_span_id", "") or row.get("span_id", "")
        metadata = row.get("metadata") or {}
        metrics = row.get("metrics") or {}
        if metadata.get("reasoning") or metadata.get("filename"):
            span_meta.setdefault(root_span_id, {}).update(metadata)
        if metrics.get("cost") is not None or metrics.get("prompt_tokens") is not None:
            span_metrics.setdefault(root_span_id, {}).update(metrics)

    tasks = []
    failures = []
    for row in rows:
        expected = row.get("expected")
        output = row.get("output")
        error = row.get("error")
        input_data = row.get("input") or {}
        if not isinstance(input_data, dict):
            input_data = {}
        row_filename = str(
            (row.get("metadata") or {}).get("filename")
            or input_data.get("filename")
            or ""
        )
        if expected not in VALID_CLASSES:
            continue
        if error is not None:
            failures.append({
                "expected": expected,
                "output": str(output or ""),
                "filename": row_filename,
                "status": "error",
                "error": str(error),
            })
            continue
        if not output:
            failures.append({
                "expected": expected,
                "output": "",
                "filename": row_filename,
                "status": "empty",
                "error": "missing output",
            })
            continue
        root_span_id = row.get("root_span_id", "")
        meta = dict(row.get("metadata") or {})
        meta.update(span_meta.get(root_span_id, {}))
        metrics = dict(row.get("metrics") or {})
        metrics.update(span_metrics.get(root_span_id, {}))
        tasks.append({
            "expected": expected,
            "output": str(output).strip().lower(),
            "correct": str(output).strip().lower() == expected,
            "reasoning": str(meta.get("reasoning", "") or ""),
            "filename": str(meta.get("filename", "") or ""),
            "metrics": metrics,
        })
    return tasks, failures


def avg(xs):
    return sum(xs) / len(xs) if xs else 0.0


def compute_cost(tasks: list[dict], input_price: float, output_price: float) -> dict:
    """Expected = list-price x measured tokens; actual = OpenRouter billed cost."""
    exp_prompt = sum((t["metrics"].get("prompt_tokens") or 0) for t in tasks)
    exp_completion = sum((t["metrics"].get("completion_tokens") or 0) for t in tasks)
    expected = exp_prompt * input_price / 1e6 + exp_completion * output_price / 1e6
    actual = sum((t["metrics"].get("cost") or 0) for t in tasks)
    return {
        "prompt_tokens": exp_prompt,
        "completion_tokens": exp_completion,
        "total_tokens": exp_prompt + exp_completion,
        "expected_usd": expected,
        "actual_usd": actual,
        "difference_usd": expected - actual,
        "pct_diff": (expected - actual) / expected * 100 if expected else 0.0,
    }


def write_confusion_matrix(tasks: list[dict], experiment: str, out_dir: Path,
                           dataset: str, model: str, per_class: int):
    labels = sorted(VALID_CLASSES) + ["__invalid__"]
    matrix = {e: {p: 0 for p in labels} for e in labels}
    for t in tasks:
        predicted = t["output"] if t["output"] in matrix[t["expected"]] else "__invalid__"
        matrix[t["expected"]][predicted] += 1

    n = len(labels)
    data = np.zeros((n, n))
    for i, e in enumerate(labels):
        for j, p in enumerate(labels):
            data[i][j] = matrix[e][p]

    fig, ax = plt.subplots(figsize=(15, 13))
    im = ax.imshow(data, cmap="YlOrRd", aspect="auto")
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(labels, rotation=45, ha="right", fontsize=9, fontfamily="monospace")
    ax.set_yticklabels(labels, fontsize=9, fontfamily="monospace")
    ax.set_xlabel("Predicted", fontsize=12)
    ax.set_ylabel("Expected (True)", fontsize=12)
    total_correct = sum(1 for t in tasks if t["correct"])
    ax.set_title(f"Confusion Matrix — {experiment}\n"
                 f"{len(tasks)} images | {total_correct} correct "
                 f"({total_correct / len(tasks) * 100:.1f}%)", fontsize=13, fontweight="bold")
    for i in range(n):
        for j in range(n):
            val = int(data[i][j])
            if val == 0:
                continue
            color = "white" if val > data.max() * 0.6 else "black"
            ax.text(j, i, str(val), ha="center", va="center", fontsize=8, fontweight="bold", color=color)
    plt.colorbar(im, ax=ax, shrink=0.8, label="Count")
    plt.tight_layout()
    png_path = out_dir / f"confusion_matrix_{experiment}.png"
    plt.savefig(png_path, dpi=150, bbox_inches="tight")
    plt.close()

    total_correct = sum(1 for t in tasks if t["correct"])
    md = []
    md.append(f"# Confusion Matrix — {experiment}")
    md.append("")
    md.append(f"**Overall Accuracy:** {total_correct / len(tasks) * 100:.1f}% ({total_correct}/{len(tasks)})  ")
    md.append(f"**Dataset:** {dataset}  ")
    md.append(f"**Model:** `{model}`")
    md.append("")
    md.append(f"![Confusion Matrix](confusion_matrix_{experiment}.png)")
    md.append("")
    md.append("## Raw Counts")
    md.append("")
    short = {c: c[:6] for c in labels}
    for src, dst in (
        ("advertisement", "advert"),
        ("file_folder", "file_f"),
        ("handwritten", "handwr"),
        ("invoice", "invoic"),
        ("news_article", "news_a"),
        ("presentation", "presen"),
        ("questionnaire", "questi"),
        ("scientific_publication", "sci_pub"),
        ("scientific_report", "sci_rep"),
        ("specification", "specif"),
        ("__invalid__", "__inv"),
    ):
        short[src] = dst
    md.append("| Expected \\ Predicted | " + " | ".join(f"`{short[c]}`" for c in labels) + " | **Total** | **Acc** |")
    md.append("|" + "---:|" * (n + 3))
    for i, exp in enumerate(labels):
        row_total = sum(int(data[i][j]) for j in range(n))
        row_correct = int(data[i][i])
        row_acc = (row_correct / row_total * 100) if row_total > 0 else 0
        cells = []
        for j in range(n):
            val = int(data[i][j])
            cells.append(f"**{val}**" if i == j and val > 0 else (f"{val}" if val > 0 else "."))
        md.append(f"| `{exp}` | " + " | ".join(cells) + f" | {row_total} | {row_acc:.0f}% |")
    md.append("")
    md.append("## Top Confused Pairs")
    md.append("")
    md.append("| Expected | Predicted As | Count |")
    md.append("|----------|-------------|------:|")
    confused = [(e, p, matrix[e][p]) for e in labels for p in labels if e != p and matrix[e][p] > 0]
    confused.sort(key=lambda x: -x[2])
    for e, p, c in confused[:20]:
        md.append(f"| `{e}` | `{p}` | {c} |")
    md.append("")
    md_path = out_dir / f"confusion_matrix_{experiment}.md"
    md_path.write_text("\n".join(md), encoding="utf-8")
    return png_path, md_path, confused


def write_misclassification_reasoning(tasks: list[dict], experiment: str, out_dir: Path):
    errors = [t for t in tasks if not t["correct"]]
    pairs: dict[tuple[str, str], list[dict]] = defaultdict(list)
    for t in errors:
        pairs[(t["expected"], t["output"])].append(t)
    sorted_pairs = sorted(pairs.items(), key=lambda x: -len(x[1]))

    md = []
    md.append(f"# Misclassification Reasoning — {experiment}")
    md.append("")
    md.append(f"**Overall Accuracy:** {sum(1 for t in tasks if t['correct']) / len(tasks) * 100:.1f}% "
              f"({sum(1 for t in tasks if t['correct'])}/{len(tasks)})  ")
    md.append(f"**Total Errors:** {len(errors)}  ")
    md.append(f"**Unique Confused Pairs:** {len(sorted_pairs)}")
    md.append("")
    md.append("---")
    for (expected, predicted), items in sorted_pairs:
        md.append("")
        md.append(f"## {expected} → {predicted} ({len(items)} errors)")
        md.append("")
        for item in items:
            filename = item.get("filename") or "unknown"
            reasoning = item.get("reasoning", "").strip()
            md.append(f"### `{filename}`")
            md.append(f"**Expected:** `{expected}` | **Predicted:** `{predicted}`")
            md.append("")
            if reasoning:
                md.append("**Reasoning:**")
                for para in reasoning.split("\n\n"):
                    md.append(f"> {para}")
            else:
                md.append("*No reasoning text captured.*")
            md.append("")
            md.append("---")
    md_path = out_dir / f"misclassification_reasoning_{experiment}.md"
    md_path.write_text("\n".join(md), encoding="utf-8")
    return md_path


def write_per_class_chart(tasks: list[dict], experiment: str, out_dir: Path):
    per_class = Counter(t["expected"] for t in tasks)
    per_class_correct = Counter(t["expected"] for t in tasks if t["correct"])
    classes = sorted(VALID_CLASSES)
    rows = [(per_class_correct[c] / per_class[c] * 100 if per_class[c] else 0, c) for c in classes]
    rows.sort()
    accs = [r[0] for r in rows]
    names = [r[1] for r in rows]
    colors = ["#2ecc71" if a >= 90 else ("#f39c12" if a >= 70 else ("#e67e22" if a >= 50 else "#e74c3c")) for a in accs]
    overall = sum(1 for t in tasks if t["correct"]) / len(tasks) * 100

    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.barh(range(len(names)), accs, color=colors, edgecolor="gray", linewidth=0.5)
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names, fontsize=11, fontfamily="monospace")
    ax.set_xlabel("Accuracy (%)", fontsize=12)
    ax.set_title(f"Per-Class Classification Accuracy — {experiment}\nOverall: {overall:.1f}% "
                 f"({sum(1 for t in tasks if t['correct'])}/{len(tasks)})", fontsize=13, fontweight="bold")
    ax.set_xlim(0, 110)
    ax.axvline(x=overall, color="blue", linestyle="--", linewidth=1.2, alpha=0.7,
               label=f"Overall avg ({overall:.1f}%)")
    ax.legend(loc="lower right", fontsize=10)
    for i, (bar, acc, name) in enumerate(zip(bars, accs, names)):
        wrong = per_class[name] - per_class_correct[name]
        label = f"{acc:.0f}%" + (f"  ({wrong} wrong)" if wrong > 0 else "")
        ax.text(acc + 1.5, i, label, va="center", fontsize=9, fontweight="bold")
    plt.tight_layout()
    png_path = out_dir / f"per_class_accuracy_{experiment}.png"
    plt.savefig(png_path, dpi=150, bbox_inches="tight")
    plt.close()
    return png_path


def build_full_report(experiment: str, model: str, prompt_version: str, dataset: str,
                      per_class: int, image_size: str, input_price: float, output_price: float,
                      reasoning: str, tasks: list[dict], errors: list[dict],
                      cost: dict, metrics: dict) -> str:
    total = len(tasks)
    correct = sum(1 for t in tasks if t["correct"])
    accuracy = correct / total * 100 if total else 0
    per_class_acc = Counter(t["expected"] for t in tasks)
    per_class_ok = Counter(t["expected"] for t in tasks if t["correct"])

    md = []
    md.append(f"# Braintrust Experiment Report — {experiment}")
    md.append("")
    md.append(f"**Model:** `{model}`  ")
    md.append(f"**Prompt version:** `{prompt_version}`  ")
    md.append(f"**Dataset:** `{dataset}` ({per_class} per class × 16 classes = {total} images)  ")
    md.append(f"**Image size:** {image_size}  ")
    md.append(f"**Reasoning:** {reasoning}  ")
    md.append(f"**Max concurrency:** 8  ")
    md.append("")
    md.append("## Results")
    md.append("")
    md.append("| Metric | Value |")
    md.append("|--------|------:|")
    md.append(f"| **Accuracy (exact_match)** | **{accuracy:.2f}%** ({correct}/{total}) |")
    md.append(f"| Scored rows | {total} |")
    md.append(f"| Failed/empty rows | {len(errors)} |")
    md.append(f"| Total expected rows | {total + len(errors)} |")
    md.append(f"| Prompt tokens (avg) | {metrics['prompt_tokens_avg']:,.1f} |")
    md.append(f"| Prompt cached tokens (avg) | {metrics['cached_tokens_avg']:,.1f} |")
    md.append(f"| Completion tokens (avg) | {metrics['completion_tokens_avg']:,.1f} |")
    md.append(f"| Completion reasoning tokens (avg) | {metrics['reasoning_tokens_avg']:,.1f} |")
    md.append(f"| Total tokens (avg) | {metrics['prompt_tokens_avg'] + metrics['completion_tokens_avg']:,.1f} |")
    md.append(f"| Time to first token (avg) | {metrics['ttft_avg']:.2f}s |")
    md.append(f"| Duration (avg) | {metrics['duration_avg']:.2f}s |")
    md.append(f"| Evaluation failures | {len(errors)} |")
    md.append("")
    md.append("## Cost — Expected vs Actual")
    md.append("")
    md.append(f"**List pricing:** ${input_price}/M input tokens, ${output_price}/M output tokens "
              f"(`{model}`, per OpenRouter model listing). Cached input priced at 10% of input "
              f"(not applicable here — `cached_tokens` is 0 across the run).")
    md.append("")
    md.append("| Metric | Value |")
    md.append("|--------|------:|")
    md.append(f"| Total prompt tokens (measured) | {cost['prompt_tokens']:,} |")
    md.append(f"| Total completion tokens (measured) | {cost['completion_tokens']:,} |")
    md.append(f"| Total tokens (measured) | {cost['total_tokens']:,} |")
    md.append(f"| **Expected cost** (list price × measured tokens) | **${cost['expected_usd']:.4f}** |")
    md.append(f"| **Actual cost** (OpenRouter billed, from Braintrust `cost` metric) | **${cost['actual_usd']:.4f}** |")
    md.append(f"| Difference (expected − actual) | ${cost['difference_usd']:+.4f} "
              f"({cost['pct_diff']:+.1f}%) |")
    md.append("")
    md.append("### Scale-up projections (list-price expected vs extrapolated actual)")
    md.append("")
    md.append("| Images | Expected Cost | Estimated Actual |")
    md.append("|--------|--------------:|-----------------:|")
    actual_per_image = cost['actual_usd'] / total if total else 0
    expected_per_image = cost['expected_usd'] / total if total else 0
    for n in (800, 25000, 320000):
        md.append(f"| {n:,} | ${expected_per_image * n:.2f} | ${actual_per_image * n:.2f} |")
    md.append("")
    md.append("## Per-Class Accuracy")
    md.append("")
    md.append("![Per-Class Accuracy](per_class_accuracy_{0}.png)".format(experiment))
    md.append("")
    md.append("| Class | Correct | Total | Accuracy |")
    md.append("|-------|--------:|------:|---------:|")
    for cls in sorted(VALID_CLASSES):
        if per_class_acc[cls] == 0:
            md.append(f"| `{cls}` | 0 | 0 | — |")
            continue
        md.append(f"| `{cls}` | {per_class_ok[cls]} | {per_class_acc[cls]} | "
                  f"{per_class_ok[cls] / per_class_acc[cls] * 100:.0f}% |")
    md.append("")
    md.append("## Confusion Matrix & Misclassification Analysis")
    md.append("")
    md.append(f"- [Confusion matrix markdown](confusion_matrix_{experiment}.md)")
    md.append(f"  - [Confusion matrix heatmap](confusion_matrix_{experiment}.png)")
    md.append(f"- [Misclassification reasoning traces](misclassification_reasoning_{experiment}.md)")
    md.append("")
    return "\n".join(md)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment", required=True)
    parser.add_argument("--model", default=_CONFIG.model)
    parser.add_argument("--prompt-version", required=True)
    parser.add_argument("--dataset", required=True)
    parser.add_argument("--images-per-class", type=int, required=True)
    parser.add_argument("--image-size", default="1024x1024")
    parser.add_argument("--input-price", type=float, default=0.03)
    parser.add_argument("--output-price", type=float, default=0.13)
    parser.add_argument("--reasoning", default="enabled (effort=high), trace logged")
    parser.add_argument("--project-id", default=PROJECT_ID)
    parser.add_argument("--project", default=_CONFIG.project_name)
    parser.add_argument("--output-dir", default="reports")
    args = parser.parse_args()

    (api_key,) = require_env("BRAINTRUST_API_KEY")
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"Fetching experiment {args.experiment}...")
    rows, meta = fetch_experiment(api_key, args.experiment, args.project_id)
    tasks, failures = build_results(rows)
    print(f"Scored rows: {len(tasks)} (failures: {len(failures)}, total expected rows: {len(tasks) + len(failures)})")

    if not tasks:
        sys.exit("No scored task rows found — experiment may still be running or all rows failed")

    # Metrics
    metrics = {
        "prompt_tokens_avg": avg([t["metrics"].get("prompt_tokens") or 0 for t in tasks]),
        "completion_tokens_avg": avg([t["metrics"].get("completion_tokens") or 0 for t in tasks]),
        "reasoning_tokens_avg": avg([t["metrics"].get("completion_reasoning_tokens") or 0 for t in tasks]),
        "cached_tokens_avg": avg([t["metrics"].get("prompt_cached_tokens") or 0 for t in tasks]),
        "duration_avg": avg([t["metrics"].get("duration") or 0 for t in tasks]),
        "ttft_avg": avg([t["metrics"].get("time_to_first_token") or 0 for t in tasks]),
    }
    cost = compute_cost(tasks, args.input_price, args.output_price)

    # Generate artifacts
    write_per_class_chart(tasks, args.experiment, out_dir)
    write_confusion_matrix(tasks, args.experiment, out_dir, args.dataset, args.model, args.images_per_class)
    write_misclassification_reasoning(tasks, args.experiment, out_dir)

    report = build_full_report(
        args.experiment, args.model, args.prompt_version, args.dataset,
        args.images_per_class, args.image_size, args.input_price, args.output_price,
        args.reasoning, tasks, failures, cost, metrics,
    )
    report_path = out_dir / f"report_{args.experiment}.md"
    report_path.write_text(report, encoding="utf-8")
    print(f"Report written: {report_path}")
    print(f"Accuracy: {sum(1 for t in tasks if t['correct'])}/{len(tasks)} "
          f"({sum(1 for t in tasks if t['correct']) / len(tasks) * 100:.1f}%)")
    print(f"Expected cost: ${cost['expected_usd']:.4f} | Actual cost: ${cost['actual_usd']:.4f} "
          f"| diff {cost['pct_diff']:+.1f}%")
    print(f"Per-class rows: {dict(sorted(Counter(t['expected'] for t in tasks).items()))}")


if __name__ == "__main__":
    main()
