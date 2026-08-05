"""Score a completed evaluation from its local manifest and save the final numbers.

Computes exact_match, per-class accuracy, and failure counts directly from the
manifest JSONL checkpoint (``reports/manifests/*.jsonl``) — no Braintrust calls.
The manifest records every row the moment the model returns, so the final result
numbers are always available and savable locally, even if Braintrust score/credit
limits cap out. Errors count as misses (matching ``braintrust_report.py``).

Writes ``<manifest-stem>_final.json`` and ``<manifest-stem>_final.md`` into
``--output-dir`` (default ``reports/experiment_reports/``).

Usage:
    python scripts/braintrust/score_manifest.py --manifest reports/manifests/<name>.jsonl
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # noqa: E402

from src.constants import DOCUMENT_CLASSES  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]


def load_manifest(path: Path) -> tuple[dict, dict[str, dict]]:
    """Return (header_metadata, {filename: last_record}) from an append-only manifest."""
    lines = path.read_text(encoding="utf-8").splitlines()
    header = json.loads(lines[0])
    final: dict[str, dict] = {}
    for line in lines[1:]:
        if line.strip():
            record = json.loads(line)
            final[record["filename"]] = record
    return header.get("metadata", {}), final


def score(metadata: dict, final: dict[str, dict]) -> dict:
    rows = sorted(final.values(), key=lambda r: (r.get("expected", ""), r.get("filename", "")))
    total = len(rows)
    completed = [r for r in rows if r.get("status") == "completed"]
    errored = [r for r in rows if r.get("status") == "error"]
    empty = [r for r in rows if r.get("status") == "empty"]
    exact = [r for r in completed if (r.get("predicted") or "").strip().lower() == (r.get("expected") or "").strip().lower()]
    misses = [r for r in completed if (r.get("predicted") or "").strip().lower() != (r.get("expected") or "").strip().lower()]

    per_class: dict[str, dict] = {}
    for cls in DOCUMENT_CLASSES:
        cls_rows = [r for r in rows if r.get("expected") == cls]
        cls_completed = [r for r in completed if r.get("expected") == cls]
        cls_exact = [r for r in exact if r.get("expected") == cls]
        cls_errors = [r for r in rows if r.get("expected") == cls and r.get("status") != "completed"]
        if cls_rows:
            per_class[cls] = {
                "total": len(cls_rows),
                "correct": len(cls_exact),
                "errors": len(cls_errors),
                "accuracy": len(cls_exact) / len(cls_rows) if cls_rows else 0.0,
            }

    return {
        "experiment": metadata.get("experiment_name"),
        "dataset": metadata.get("dataset"),
        "model": metadata.get("model"),
        "prompt_version": metadata.get("prompt_version"),
        "max_tokens": metadata.get("max_tokens"),
        "reasoning_effort": metadata.get("reasoning_effort"),
        "total_rows": total,
        "completed": len(completed),
        "error": len(errored),
        "empty": len(empty),
        "failed_rows": len(errored) + len(empty),
        "exact_match": len(exact),
        "exact_match_accuracy": len(exact) / total if total else 0.0,
        "per_class": per_class,
        "error_filenames": [r.get("filename") for r in errored],
        "miss_filenames": [r.get("filename") for r in misses],
    }


def to_markdown(result: dict) -> str:
    lines = [
        f"# Final Results: {result['experiment']}",
        "",
        f"- **Dataset**: {result['dataset']}",
        f"- **Model**: {result['model']}",
        f"- **Prompt**: {result['prompt_version']}",
        f"- **Max tokens**: {result['max_tokens']}",
        "",
        f"## Overall",
        "",
        f"- **Rows**: {result['total_rows']}",
        f"- **Completed**: {result['completed']}",
        f"- **Errors**: {result['error']}",
        f"- **Empty**: {result['empty']}",
        f"- **exact_match**: {result['exact_match']}/{result['total_rows']} ({result['exact_match_accuracy']:.1%})",
        "",
        "## Per-class accuracy",
        "",
        "| Class | Correct | Total | Errors | Accuracy |",
        "|---|---:|---:|---:|---:|",
    ]
    for cls in DOCUMENT_CLASSES:
        pc = result["per_class"].get(cls)
        if pc is None:
            continue
        lines.append(
            f"| {cls} | {pc['correct']} | {pc['total']} | {pc['errors']} | {pc['accuracy']:.1%} |"
        )
    if result["error_filenames"]:
        lines += ["", "## Failed (error) rows", ""]
        lines += [f"- `{name}`" for name in result["error_filenames"]]
    return "\n".join(lines) + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True,
                        help="Path to the manifest JSONL (reports/manifests/*.jsonl)")
    parser.add_argument("--output-dir", type=Path,
                        default=ROOT / "reports" / "experiment_reports",
                        help="Directory for the saved result files (default: reports/experiment_reports)")
    args = parser.parse_args()

    metadata, final = load_manifest(args.manifest)
    result = score(metadata, final)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    stem = args.manifest.stem
    json_path = args.output_dir / f"{stem}_final.json"
    md_path = args.output_dir / f"{stem}_final.md"
    json_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(to_markdown(result), encoding="utf-8")

    print(
        f"Saved: {json_path}\nSaved: {md_path}"
    )
    print()
    print(f"exact_match {result['exact_match']}/{result['total_rows']} ({result['exact_match_accuracy']:.1%})")
    print(f"completed={result['completed']} error={result['error']} empty={result['empty']}")


if __name__ == "__main__":
    main()
