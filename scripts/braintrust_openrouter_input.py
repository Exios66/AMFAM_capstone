"""
Braintrust Prompt Evaluation for Document Classification

Runs the classification prompt against the sampled dataset (16 classes) and logs
results to Braintrust for prompt iteration in their UI. Images are pulled from a
Braintrust dataset by default; a local directory of PNGs can be used instead.

Prerequisites:
    pip install braintrust openai
    Set BRAINTRUST_API_KEY and OPENROUTER_API_KEY in your .env file.

Usage:
    python scripts/braintrust_openrouter_input.py
    python scripts/braintrust_openrouter_input.py --dataset fixed_size_sampled
    python scripts/braintrust_openrouter_input.py --images-dir path/to/images
"""

import argparse
import base64
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import braintrust
from openai import OpenAI

from src.env_utils import require_env
from src.image_utils import encode_image_base64
from src.openrouter_classifier import CLASSIFICATION_PROMPT, VALID_CLASSES, clean_prediction
from src.openrouter_utils import OPENROUTER_BASE_URL, build_vision_messages

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DEFAULT_PROJECT = "DSHB_amfam_capstone_2026"
DEFAULT_DATASET = "fixed_size_sampled"
MODEL = "google/gemini-2.5-flash"  # reasoning model with visible chain-of-thought
PROJECT_NAME = "AMFAM-Doc-Classification"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def quiet_reporter() -> braintrust.Reporter:
    """Reporter that suppresses Braintrust's score summary so stdout carries only
    the classification results. Task errors are still surfaced on stderr."""
    def report_eval(evaluator, result, verbose, jsonl) -> bool:
        failures = [r for r in result.results if r.error]
        for failure in failures:
            print(f"ERROR {failure.input['filename']}: {failure.error}", file=sys.stderr)
        return not failures

    def report_run(results, verbose, jsonl) -> bool:
        return all(results)

    return braintrust.Reporter(
        "classification-only",
        report_eval=report_eval,
        report_run=report_run,
    )


def get_api_keys() -> tuple[str, str]:
    """Load required API keys from environment."""
    return require_env("OPENROUTER_API_KEY", "BRAINTRUST_API_KEY")


def extract_class_from_filename(filename: str) -> str:
    """
    Extract the ground-truth class from the fixed-size dataset filename.
    Format: processed_balanced__{class}__{original_name}.png
    """
    parts = filename.split("__")
    if len(parts) >= 2:
        return parts[1]
    return "unknown"


def load_dataset_images(dataset_dir: Path) -> list[dict]:
    """
    Load all images from a local fixed-size dataset directory.
    Returns list of records with base64 image contents and expected class.
    """
    if not dataset_dir.is_dir():
        raise FileNotFoundError(f"Dataset directory does not exist: {dataset_dir}")

    images = sorted(dataset_dir.glob("*.png"))
    dataset = []
    unlabeled = []
    for img_path in images:
        expected_class = extract_class_from_filename(img_path.name)
        if expected_class in VALID_CLASSES:
            dataset.append({
                "image_b64": encode_image_base64(img_path),
                "filename": img_path.name,
                "expected": expected_class,
            })
        else:
            unlabeled.append(img_path.name)

    if unlabeled:
        print(
            f"Warning: skipped {len(unlabeled)} image(s) whose filename carries no valid class "
            f"label (e.g. {unlabeled[0]})",
            file=sys.stderr,
        )
    if not dataset:
        raise ValueError(
            f"No labeled images found in {dataset_dir} (scanned {len(images)} PNG file(s)); "
            f"expected names like '<dataset>__<class>__<name>.png'."
        )
    return dataset


def load_braintrust_dataset(project: str, dataset_name: str) -> list[dict]:
    """
    Load images from a Braintrust dataset whose rows carry the document image as
    an attachment under ``input.image`` and the label under ``expected``.

    Rows without a stored attachment (placeholder rows) are skipped.
    """
    dataset = braintrust.init_dataset(project=project, name=dataset_name)
    records = []
    skipped = 0
    for row in dataset:
        expected = row.get("expected")
        attachment = (row.get("input") or {}).get("image")
        reference = getattr(attachment, "reference", None) or {}
        filename = reference.get("filename")
        if expected not in VALID_CLASSES or not filename:
            skipped += 1
            continue
        records.append({
            "image_b64": base64.b64encode(attachment.data).decode("utf-8"),
            "filename": filename,
            "expected": expected,
        })

    if skipped:
        print(
            f"Warning: skipped {skipped} row(s) in dataset '{dataset_name}' with no stored "
            f"attachment or no valid expected class.",
            file=sys.stderr,
        )
    if not records:
        raise ValueError(
            f"Braintrust dataset '{dataset_name}' in project '{project}' contains no usable rows "
            f"({skipped} row(s) skipped)."
        )
    return records


# ---------------------------------------------------------------------------
# Braintrust Eval
# ---------------------------------------------------------------------------

def run_eval(dataset: list[dict]) -> int:
    """Run the classification prompt against the dataset and log to Braintrust."""
    openrouter_key, _ = get_api_keys()

    # Wrap OpenAI client pointed at OpenRouter with Braintrust logging
    client = braintrust.wrap_openai(
        OpenAI(
            base_url=OPENROUTER_BASE_URL,
            api_key=openrouter_key,
        )
    )

    images_by_index = {i: d["image_b64"] for i, d in enumerate(dataset)}

    @braintrust.traced
    def classify_document(input_data: dict) -> str:
        """Classify a single document image via the vision model."""
        image_b64 = images_by_index[input_data["index"]]

        response = client.chat.completions.create(
            model=MODEL,
            messages=build_vision_messages(CLASSIFICATION_PROMPT, image_b64),
            max_tokens=1024,
            temperature=0.1,
            extra_body={
                "reasoning": {"effort": "medium"},
            },
        )

        if not response.choices:
            raise RuntimeError(
                f"Model returned no choices for {input_data['filename']}: {response}"
            )

        msg = response.choices[0].message
        raw = msg.content or ""

        # Extract reasoning from response if available
        reasoning_text = ""
        if hasattr(msg, "reasoning_content") and msg.reasoning_content:
            reasoning_text = msg.reasoning_content
        elif hasattr(msg, "reasoning") and msg.reasoning:
            reasoning_text = msg.reasoning

        # Strip any <think> blocks from visible output to get clean prediction
        clean_output = re.sub(r"<think>.*?</think>", "", raw, flags=re.DOTALL).strip()
        predicted = clean_prediction(clean_output)

        # Log metadata for Braintrust UI — includes reasoning trace
        braintrust.current_span().log(
            metadata={
                "raw_response": raw,
                "reasoning": reasoning_text or "(reasoning not exposed by model)",
                "model": MODEL,
                "filename": input_data["filename"],
            }
        )

        return predicted

    def exact_match(output: str, expected: str) -> float:
        """Score 1.0 if prediction matches expected class, else 0.0."""
        return 1.0 if output == expected else 0.0

    result = braintrust.Eval(
        PROJECT_NAME,
        data=lambda: [
            {
                "input": {"index": i, "filename": d["filename"]},
                "expected": d["expected"],
            }
            for i, d in enumerate(dataset)
        ],
        task=classify_document,
        scores=[exact_match],
        max_concurrency=8,
        reporter=quiet_reporter(),
    )

    print_classifications(result)

    failed = [r for r in result.results if r.error is not None]
    if failed:
        print(f"{len(failed)} of {len(dataset)} image(s) failed to classify.", file=sys.stderr)
        return 1
    return 0


def print_classifications(result) -> None:
    """Print only the classification outcome: per-image labels and accuracy."""
    rows = [
        (r.input["filename"], r.expected, r.output, r.expected == r.output)
        for r in result.results
        if r.error is None
    ]
    rows.sort(key=lambda row: (row[1], row[0]))

    for filename, expected, predicted, correct in rows:
        print(f"{'OK ' if correct else 'MISS'}  {expected:<24} {predicted:<24} {filename}")

    per_class = Counter()
    per_class_correct = Counter()
    for _, expected, _, correct in rows:
        per_class[expected] += 1
        per_class_correct[expected] += int(correct)

    print()
    for cls in sorted(per_class):
        total = per_class[cls]
        correct = per_class_correct[cls]
        print(f"{cls:<24} {correct}/{total} ({correct / total:.0%})")

    total = len(rows)
    correct = sum(1 for row in rows if row[3])
    print()
    print(f"exact_match {correct}/{total} ({correct / total:.1%})" if total else "no results")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=DEFAULT_PROJECT,
                        help="Braintrust project holding the dataset")
    parser.add_argument("--dataset", default=DEFAULT_DATASET,
                        help="Braintrust dataset name to classify")
    parser.add_argument("--images-dir", type=Path, default=None,
                        help="Classify local PNGs instead of a Braintrust dataset")
    parser.add_argument("--limit", type=int, default=None,
                        help="Classify only the first N images")
    args = parser.parse_args()

    try:
        if args.images_dir:
            dataset = load_dataset_images(args.images_dir)
        else:
            dataset = load_braintrust_dataset(args.project, args.dataset)
    except (FileNotFoundError, ValueError, OSError) as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1

    if args.limit:
        dataset = dataset[:args.limit]

    if not dataset:
        print("Error: no labeled images found to classify.", file=sys.stderr)
        return 1

    return run_eval(dataset)


if __name__ == "__main__":
    sys.exit(main())
