"""
Summarize a Braintrust experiment run: per-image OK/MISS lines, per-class
accuracy, and overall exact_match, computed from the experiment records in
Braintrust. Useful when a run's local summary was lost (e.g. the process hung
after tasks completed).

Usage:
    python scripts/braintrust/summarize_braintrust_experiment.py --experiment gemini-2.5-flash_v4_reasoning
"""

import argparse
import os
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import braintrust

from src.braintrust_config import load_braintrust_config
from src.env_utils import require_env
from src.openrouter_classifier import VALID_CLASSES

_CONFIG = load_braintrust_config()
PROJECT_ID = _CONFIG.project_id


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--experiment", required=True, help="Experiment name to summarize")
    parser.add_argument("--project-id", default=PROJECT_ID)
    args = parser.parse_args()

    require_env("BRAINTRUST_API_KEY")
    braintrust.login(api_key=os.environ["BRAINTRUST_API_KEY"])

    from braintrust.logger import init

    exp = init(
        project_id=args.project_id,
        experiment=args.experiment,
        open=True,
    )

    rows = []
    for r in exp:
        expected = r.get("expected")
        if isinstance(expected, str) and expected in VALID_CLASSES:
            rows.append(r)

    print(f"task records found: {len(rows)}")
    if not rows:
        return

    results = []
    for r in rows:
        filename = r.get("input", {}).get("filename", "?")
        expected = r["expected"]
        output = r.get("output")
        output = output if isinstance(output, str) else ""
        results.append((filename, expected, output, expected == output))

    results.sort(key=lambda row: (row[1], row[0]))
    for filename, expected, predicted, correct in results:
        print(f"{'OK ' if correct else 'MISS'}  {expected:<24} {predicted:<24} {filename}")

    per_class = Counter()
    per_class_correct = Counter()
    for _, expected, _, correct in results:
        per_class[expected] += 1
        if correct:
            per_class_correct[expected] += 1

    print()
    for cls in sorted(per_class):
        total = per_class[cls]
        correct = per_class_correct[cls]
        print(f"{cls:<24} {correct}/{total} ({100.0 * correct / total:.0f}%)")

    total = len(results)
    correct = sum(1 for _, _, _, ok in results if ok)
    print(f"\nexact_match {correct}/{total} ({100.0 * correct / total:.1f}%)")


if __name__ == "__main__":
    main()
