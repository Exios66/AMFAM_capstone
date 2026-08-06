"""Compare a base single-pass run against its confidence-gated escalation run.

Reads two manifests produced by ``braintrust_openrouter_input.py`` on the
SAME dataset:

- ``--base``: the base single-pass run (all rows, qwen-class model).
- ``--routed``: the escalation tail run (only the low-confidence tail rows,
  re-scored by the escalation/stronger model; every row carries ``routed``).

Merges them into one final prediction per image (escalated where present,
base elsewhere) and reports:

1. Accuracy of the base run, the routed tail run, and the merged routed
   pipeline (with the delta vs the base run).
2. Measured cost of both runs and the merged cost factor vs the base run.
3. Per-image flips on the escalated tail (base label -> escalated label).
4. Per-class merged accuracy.

This is the direct test of the routing memo's claim
(``reports/monte_carlo/routing_abstention.md``): the merged accuracy gain at
alpha=10% should approach the simulated +4.3pp IF the escalation model is
genuinely stronger on the tail.

Usage:
    python scripts/braintrust/routed_compare.py \
      --base reports/manifests/qwen3.7-flash_v18.1_high.jsonl \
      --routed reports/manifests/qwen3.7-flash_gemini-2.5-pro_v18.1_routed10.jsonl
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # noqa: E402

from src.monte_carlo import safe_div  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_OUT = ROOT / "reports" / "monte_carlo" / "routed_verification.md"


def load_manifest_rows(path: Path) -> dict[str, dict]:
    """Return {filename: record} for a manifest (last state per filename)."""
    final: dict[str, dict] = {}
    for line in path.read_text(encoding="utf-8").splitlines()[1:]:
        if not line.strip():
            continue
        record = json.loads(line)
        final[record["filename"]] = record
    return final


def row_correct(record: dict) -> bool:
    if record.get("status") != "completed":
        return False
    return (record.get("predicted") or "").strip().lower() == (record.get("expected") or "").lower()


def summarize(rows: dict[str, dict]) -> dict:
    completed = [r for r in rows.values() if r.get("status") == "completed"]
    correct = sum(1 for r in completed if row_correct(r))
    cost = sum(float(r.get("cost") or 0.0) for r in completed)
    return {
        "rows": len(completed),
        "correct": correct,
        "accuracy": safe_div(correct, len(completed)),
        "cost": cost,
    }


def run() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", type=Path, required=True,
                        help="Manifest of the base single-pass run")
    parser.add_argument("--routed", type=Path, required=True,
                        help="Manifest of the escalation tail run")
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT,
                        help=f"Report path (default: {DEFAULT_OUT})")
    args = parser.parse_args()

    base = load_manifest_rows(args.base)
    routed = load_manifest_rows(args.routed)
    if not base or not routed:
        sys.exit("Error: one or both manifests are empty")

    base_sum = summarize(base)
    routed_sum = summarize(routed)

    # Merge: escalated prediction wins on tail rows, base elsewhere.
    merged_correct = 0
    merged_total = 0
    merged_cost = base_sum["cost"] + routed_sum["cost"]
    per_class = Counter()
    per_class_correct = Counter()
    flips: list[tuple[str, str, str, bool, bool]] = []
    for filename, rec in base.items():
        if rec.get("status") != "completed":
            continue
        merged_total += 1
        expected = rec["expected"]
        base_pred = (rec.get("predicted") or "").strip().lower()
        final_pred = base_pred
        tail_rec = routed.get(filename)
        if tail_rec and tail_rec.get("status") == "completed":
            esc_pred = (tail_rec.get("predicted") or "").strip().lower()
            if esc_pred:
                final_pred = esc_pred
            if esc_pred and esc_pred != base_pred:
                flips.append((filename, expected, base_pred, esc_pred,
                              esc_pred == expected))
        correct = final_pred == expected
        merged_correct += int(correct)
        per_class[expected] += 1
        per_class_correct[expected] += int(correct)

    merged_acc = safe_div(merged_correct, merged_total)
    delta = merged_acc - base_sum["accuracy"]
    cost_factor = safe_div(merged_cost, base_sum["cost"]) if base_sum["cost"] else float("nan")
    tail_correct = routed_sum["correct"]

    lines = [
        "# Routed Verification: Base vs Confidence-Gated Escalation",
        "",
        f"- **Base run**: `{args.base.name}` — {base_sum['rows']} rows, "
        f"accuracy {base_sum['accuracy']:.3f}, cost ${base_sum['cost']:.4f}",
        f"- **Escalation run**: `{args.routed.name}` — {routed_sum['rows']} rows "
        f"({len(flips)} predictions changed), accuracy {routed_sum['accuracy']:.3f}, "
        f"cost ${routed_sum['cost']:.4f}",
        "",
        "## Merged pipeline",
        "",
        "| metric | value |",
        "|---|---:|",
        f"| rows | {merged_total} |",
        f"| merged accuracy | {merged_acc:.3f} |",
        f"| base accuracy | {base_sum['accuracy']:.3f} |",
        f"| **delta vs base** | **{delta:+.3f}** |",
        f"| merged cost | ${merged_cost:.4f} |",
        f"| cost factor vs base | {cost_factor:.2f}x |",
        f"| escalation tail accuracy | {routed_sum['accuracy']:.3f} "
        f"({tail_correct}/{routed_sum['rows']}) |",
        "",
        "**Memo reference** (`reports/monte_carlo/routing_abstention.md`): simulated "
        f"+4.3pp at alpha=10% assumes the escalated model is genuinely stronger.",
        "",
    ]

    if flips:
        fixed = sum(1 for *_, flipped_ok in flips if flipped_ok)
        lines += [
            "## Escalated flips (base label -> escalated label)",
            "",
            f"{fixed} of {len(flips)} escalated rows flipped to the CORRECT label.",
            "",
            "| filename | expected | base | escalated | fixed? |",
            "|---|---|---|---|---|",
        ]
        for filename, expected, base_pred, esc_pred, fixed_ok in sorted(flips):
            lines.append(f"| `{filename}` | `{expected}` | {base_pred} | {esc_pred} | "
                         f"{'yes' if fixed_ok else 'no'} |")
        lines.append("")

    lines += [
        "## Per-class merged accuracy",
        "",
        "| class | correct | total | accuracy |",
        "|---|---:|---:|---:|",
    ]
    for cls in sorted(per_class):
        total = per_class[cls]
        correct = per_class_correct[cls]
        lines.append(f"| {cls} | {correct} | {total} | {safe_div(correct, total):.3f} |")

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"Report saved: {args.out}")
    print("\n" + "\n".join(lines[:22]))


if __name__ == "__main__":
    run()
