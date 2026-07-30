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
    python scripts/braintrust_openrouter_input.py --prompt-version v4 --model qwen/qwen-3.7-flash
    python scripts/braintrust_openrouter_input.py --project AMFAM_v2 --dataset-project DSHB_amfam_capstone_2026
"""

import argparse
import base64
import os
import re
import sys
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import braintrust
from openai import OpenAI

from src.env_utils import require_env
from src.image_utils import encode_image_base64
from src.openrouter_classifier import VALID_CLASSES, clean_prediction
from src.openrouter_utils import OPENROUTER_BASE_URL, build_vision_messages
from src.prompts import get_prompt, DEFAULT_PROMPT_VERSION

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DEFAULT_PROJECT = "AMFAM v2"  # Project name for evaluation
DEFAULT_DATASET_PROJECT = "DSHB_amfam_capstone_2026"  # Project with dataset (source account)
DEFAULT_DATASET = "fixed_size_sampled"
DEFAULT_MODEL = "qwen/qwen-3.7-flash"  # cost-efficient model
DEFAULT_MAX_TOKENS = 2048  # Increased for reasoning models to accommodate both reasoning and output
PROJECT_NAME = "AMFAM v2"


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
    dataset = []
    for img_path in sorted(dataset_dir.glob("*.png")):
        expected_class = extract_class_from_filename(img_path.name)
        if expected_class in VALID_CLASSES:
            dataset.append({
                "image_b64": encode_image_base64(img_path),
                "filename": img_path.name,
                "expected": expected_class,
            })
    return dataset


def load_braintrust_dataset(project: str, dataset_name: str, dataset_api_key: str = None) -> list[dict]:
    """
    Load images from a Braintrust dataset whose rows carry the document image as
    an attachment under ``input.image`` and the label under ``expected``.

    Rows without a stored attachment (placeholder rows) are skipped.
    """
    # Initialize braintrust with proper login using dataset-specific API key
    api_key = dataset_api_key or os.environ.get("BRAINTRUST_API_KEY")
    if api_key:
        # Only force login if using a different API key
        force = dataset_api_key is not None
        braintrust.login(api_key=api_key, force_login=force)
    
    dataset = braintrust.init_dataset(project=project, name=dataset_name)
    records = []
    for i, row in enumerate(dataset):
        expected = row.get("expected")
        input_data = row.get("input") or {}
        attachment = input_data.get("image")
        metadata = input_data.get("metadata", {})
        
        # Skip placeholder rows
        if metadata.get("placeholder", False):
            continue
            
        if expected not in VALID_CLASSES or not attachment:
            continue
        
        # Try to get filename from reference
        filename = None
        try:
            reference = getattr(attachment, "reference", None) or {}
            filename = reference.get("filename")
        except (KeyError, AttributeError):
            pass
        
        # If no filename, use document_id or fallback
        if not filename:
            doc_id = input_data.get("document_id")
            if doc_id and doc_id != "generated":
                filename = f"{doc_id}.png"
            else:
                filename = f"document_{i+1}.png"
            
        records.append({
            "image_b64": base64.b64encode(attachment.data).decode("utf-8"),
            "filename": filename,
            "expected": expected,
        })
    return records


# ---------------------------------------------------------------------------
# Braintrust Eval
# ---------------------------------------------------------------------------

def run_eval(dataset: list[dict], model: str = DEFAULT_MODEL, prompt_version: str = DEFAULT_PROMPT_VERSION, max_tokens: int = DEFAULT_MAX_TOKENS, project_id: str = DEFAULT_PROJECT) -> None:
    """Run the classification prompt against the dataset and log to Braintrust."""
    openrouter_key = os.environ.get("OPENROUTER_API_KEY")
    braintrust_key = os.environ.get("BRAINTRUST_API_KEY")
    
    # Initialize braintrust with proper login and project using eval API key
    braintrust.login(api_key=braintrust_key)
    
    # Get the appropriate prompt version
    classification_prompt = get_prompt(prompt_version)

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

        # Build extra body based on model capabilities
        extra_body = {}
        if "gemini" in model.lower():
            extra_body = {"reasoning": {"effort": "medium"}}
        
        response = client.chat.completions.create(
            model=model,
            messages=build_vision_messages(classification_prompt, image_b64),
            max_tokens=max_tokens,
            temperature=0.1,
            extra_body=extra_body,
        )

        raw = response.choices[0].message.content or ""

        # Extract reasoning from response if available
        reasoning_text = ""
        msg = response.choices[0].message
        if hasattr(msg, "reasoning_content") and msg.reasoning_content:
            reasoning_text = msg.reasoning_content
        elif hasattr(msg, "reasoning") and msg.reasoning:
            reasoning_text = msg.reasoning

        # Strip any ``` blocks from visible output to get clean prediction
        clean_output = re.sub(r"```.*?```", "", raw, flags=re.DOTALL).strip()
        predicted = clean_prediction(clean_output)

        # Log metadata for Braintrust UI — includes reasoning trace
        braintrust.current_span().log(
            metadata={
                "raw_response": raw,
                "reasoning": reasoning_text or "(reasoning not exposed by model)",
                "model": model,
                "prompt_version": prompt_version,
                "max_tokens": max_tokens,
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


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=DEFAULT_PROJECT,
                        help="Braintrust project for evaluation (where results are logged)")
    parser.add_argument("--dataset-project", default=DEFAULT_DATASET_PROJECT,
                        help="Braintrust project holding the dataset")
    parser.add_argument("--dataset", default=DEFAULT_DATASET,
                        help="Braintrust dataset name to classify")
    parser.add_argument("--images-dir", type=Path, default=None,
                        help="Classify local PNGs instead of a Braintrust dataset")
    parser.add_argument("--limit", type=int, default=None,
                        help="Classify only the first N images")
    parser.add_argument("--model", default=DEFAULT_MODEL,
                        help=f"Model to use for classification (default: {DEFAULT_MODEL})")
    parser.add_argument("--prompt-version", default=DEFAULT_PROMPT_VERSION,
                        help=f"Prompt version to use (v1, v2, v3, v4) (default: {DEFAULT_PROMPT_VERSION})")
    parser.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS,
                        help=f"Maximum tokens for model response (default: {DEFAULT_MAX_TOKENS})")
    args = parser.parse_args()

    if args.images_dir:
        dataset = load_dataset_images(args.images_dir)
    else:
        # Use source API key for loading dataset from DSHB account
        dataset = load_braintrust_dataset(args.dataset_project, args.dataset, "DATA_BRAINTRUST_KEY")

    if args.limit:
        dataset = dataset[:args.limit]

    if not dataset:
        sys.exit("No labeled images found to classify.")

    print(f"Running evaluation with {args.model} using prompt {args.prompt_version} on {len(dataset)} images")
    print(f"Evaluation project: {args.project}, Dataset from: {args.dataset_project}")
    run_eval(dataset, model=args.model, prompt_version=args.prompt_version, max_tokens=args.max_tokens, project_id=args.project)


if __name__ == "__main__":
    main()