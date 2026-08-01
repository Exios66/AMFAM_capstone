"""
Braintrust Prompt Evaluation for Document Classification

Runs the classification prompt against the sampled dataset (16 classes) and logs
results to Braintrust for prompt iteration in their UI. Images are pulled from a
Braintrust dataset by default; a local directory of PNGs can be used instead.

Prerequisites:
    pip install braintrust openai
    Set BRAINTRUST_API_KEY and OPENROUTER_API_KEY in your .env file.

Usage:
    python scripts/braintrust/braintrust_openrouter_input.py
    python scripts/braintrust/braintrust_openrouter_input.py --dataset fixed_size_sampled
    python scripts/braintrust/braintrust_openrouter_input.py --images-dir path/to/images
    python scripts/braintrust/braintrust_openrouter_input.py --prompt-version v4 --model qwen/qwen3.7-flash
    python scripts/braintrust/braintrust_openrouter_input.py --experiment-name qwen3.7-flash_v4_reasoning
"""

import argparse
import base64
import os
import re
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import braintrust
import requests
from openai import OpenAI

from src.env_utils import require_env
from src.image_utils import encode_image_base64
from src.openrouter_classifier import VALID_CLASSES, clean_prediction
from src.openrouter_utils import OPENROUTER_BASE_URL, build_vision_messages
from src.prompts import get_prompt, DEFAULT_PROMPT_VERSION

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

PROJECT_NAME = "AMFAM v2"
PROJECT_ID = "ba0346b3-cad8-463d-b758-afddafd9f0d0"
ORG_ID = "cc595192-8420-461d-8111-1d3ca1b42948"
BRAINTRUST_API_BASE = "https://api.braintrust.dev"
DEFAULT_DATASET_PROJECT = "AMFAM v2"  # Project holding the dataset
DEFAULT_DATASET = "fixed_size_sampled"
DEFAULT_MODEL = "qwen/qwen3.7-flash"  # cost-efficient vision reasoning model
DEFAULT_MAX_TOKENS = 4096  # Enough for reasoning trace + scratchpad + final label
DEFAULT_ATTACHMENT_WORKERS = 8
MAX_TRIES = 3  # Retry transient provider failures (502s, token caps, empty responses)
MAX_TOKENS_CAP = 16384  # Upper bound when growing max_tokens on "length" finish reasons


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


def fetch_attachment_bytes(
    api_key: str,
    reference: dict,
    org_id: str = ORG_ID,
    api_base: str = BRAINTRUST_API_BASE,
) -> bytes:
    """Download an already-uploaded Braintrust attachment's bytes directly.

    The SDK downloads attachments one at a time (metadata request + object-store
    GET, ~1s per row); fetching in parallel avoids that bottleneck for datasets
    of hundreds of images.
    """
    params = {
        "filename": reference["filename"],
        "content_type": reference["content_type"],
        "org_id": org_id,
    }
    if reference["type"] == "braintrust_attachment":
        params["key"] = reference["key"]
    elif reference["type"] == "external_attachment":
        params["url"] = reference["url"]
    else:
        raise RuntimeError(f"Unknown attachment type: {reference['type']}")

    resp = requests.get(
        f"{api_base}/attachment",
        params=params,
        headers={"Authorization": f"Bearer {api_key}"},
        timeout=60,
    )
    resp.raise_for_status()
    download_url = resp.json()["downloadUrl"]

    data = requests.get(download_url, timeout=120)
    data.raise_for_status()
    return data.content


def load_braintrust_dataset(project: str, dataset_name: str, dataset_api_key: str = None, org_id: str = ORG_ID) -> list[dict]:
    """
    Load images from a Braintrust dataset whose rows carry the document image as
    an attachment under ``input.image`` and the label under ``expected``.

    Rows without a stored attachment (placeholder rows) are skipped. Attachments
    are downloaded in parallel.
    """
    # Initialize braintrust with proper login using dataset-specific API key
    api_key = dataset_api_key or os.environ.get("BRAINTRUST_API_KEY")
    if api_key:
        # Only force login if using a different API key
        force = dataset_api_key is not None
        braintrust.login(api_key=api_key, force_login=force)

    dataset = braintrust.init_dataset(project=project, name=dataset_name)
    pending = []
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

        pending.append((expected, attachment, filename))

    records = []
    failures = []

    def grab(item):
        _, attachment, _ = item
        try:
            return fetch_attachment_bytes(api_key, attachment.reference, org_id), None
        except Exception as e:  # noqa: BLE001 - one bad row shouldn't abort the eval
            return None, str(e)

    with ThreadPoolExecutor(max_workers=DEFAULT_ATTACHMENT_WORKERS) as pool:
        for (expected, _, filename), (image_bytes, error) in zip(pending, pool.map(grab, pending)):
            if error is not None:
                failures.append((expected, filename, error))
                continue
            records.append({
                "image_b64": base64.b64encode(image_bytes).decode("utf-8"),
                "filename": filename,
                "expected": expected,
            })

    for expected, filename, error in failures:
        print(f"SKIP {expected:<24} {filename}: {error}", file=sys.stderr)
    if failures:
        print(f"WARNING: skipped {len(failures)} rows with unreadable attachments", file=sys.stderr)

    return records


def extract_prediction(text: str) -> str:
    """Prefer the ``<label>...</label>`` output tag (V4 format), then fall back
    to scanning the raw output for any valid class name."""
    if not text:
        return ""
    match = re.search(r"<label>\s*([^<\s][^<]*?)\s*</label>", text, flags=re.IGNORECASE | re.DOTALL)
    if match:
        candidate = match.group(1).strip().lower()
        if candidate in VALID_CLASSES:
            return candidate
    return clean_prediction(text)


# ---------------------------------------------------------------------------
# Braintrust Eval
# ---------------------------------------------------------------------------

def run_eval(dataset: list[dict], model: str = DEFAULT_MODEL, prompt_version: str = DEFAULT_PROMPT_VERSION, max_tokens: int = DEFAULT_MAX_TOKENS, project_id: str = PROJECT_ID, experiment_name: str = None) -> None:
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
        elif "qwen" in model.lower():
            # Qwen3.x are hybrid reasoning models; force thinking on and ask
            # OpenRouter to include the reasoning trace so we can log it.
            extra_body = {
                "reasoning": {"enabled": True, "effort": "high"},
                "include_reasoning": True,
            }
        
        # Transient provider failures (Alibaba 502 "inappropriate content", token
        # caps, empty responses) return no usable content. Retry with backoff;
        # grow max_tokens when the model capped out mid-reasoning.
        tokens = max_tokens
        last_error = None
        for attempt in range(MAX_TRIES):
            try:
                response = client.chat.completions.create(
                    model=model,
                    messages=build_vision_messages(classification_prompt, image_b64),
                    max_tokens=tokens,
                    temperature=0.1,
                    extra_body=extra_body,
                )
                raw = response.choices[0].message.content or ""
                finish_reason = response.choices[0].finish_reason
                if raw.strip() == "" or finish_reason == "error":
                    raise RuntimeError(
                        f"model returned no usable content (finish_reason={finish_reason})"
                    )
                if finish_reason == "length":
                    tokens = min(tokens * 2, MAX_TOKENS_CAP)
                    raise RuntimeError(
                        f"model hit max_tokens={tokens // 2} (finish_reason=length)"
                    )
                break
            except Exception as e:  # noqa: BLE001 - retry transient provider errors
                last_error = e
                if attempt < MAX_TRIES - 1:
                    time.sleep(2 * (attempt + 1))
        else:
            raise last_error

        msg = response.choices[0].message
        reasoning_text = ""
        if hasattr(msg, "reasoning_content") and msg.reasoning_content:
            reasoning_text = msg.reasoning_content
        elif hasattr(msg, "reasoning") and msg.reasoning:
            reasoning_text = msg.reasoning

        # V4 wraps the final label in <label>...</label>; parse it first so the
        # scratchpad prose never leaks a wrong class into the prediction.
        predicted = extract_prediction(raw)

        # Log metadata for Braintrust UI — includes reasoning trace and prompt
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

    if experiment_name is None:
        experiment_name = f"{model.split('/')[-1]}_p{prompt_version}"

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
        project_id=project_id,
        experiment_name=experiment_name,
        metadata={
            "prompt": classification_prompt,
            "prompt_version": prompt_version,
            "model": model,
            "max_tokens": max_tokens,
            "reasoning": "enabled",
            "dataset": f"{DEFAULT_DATASET_PROJECT}/{DEFAULT_DATASET}",
        },
        description=f"{model} | prompt {prompt_version} | reasoning enabled | exact_match tracked",
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
    # Loads .env and validates both keys are present before anything else.
    get_api_keys()

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", default=PROJECT_NAME,
                        help="Braintrust project for evaluation (where results are logged)")
    parser.add_argument("--project-id", default=PROJECT_ID,
                        help=f"Braintrust project id for evaluation (default: {PROJECT_ID})")
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
                        help=f"Prompt version to use (v1-v11) (default: {DEFAULT_PROMPT_VERSION})")
    parser.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS,
                        help=f"Maximum tokens for model response (default: {DEFAULT_MAX_TOKENS})")
    parser.add_argument("--experiment-name", default=None,
                        help="Braintrust experiment name (default: {model-slug}_p{prompt-version})")
    args = parser.parse_args()

    if args.images_dir:
        dataset = load_dataset_images(args.images_dir)
    else:
        # Load the dataset with the default BRAINTRUST_API_KEY; if a separate
        # source-account key (DATA_BRAINTRUST_KEY) is configured, use it instead.
        source_key = os.environ.get("DATA_BRAINTRUST_KEY")
        dataset = load_braintrust_dataset(args.dataset_project, args.dataset, source_key)

    if args.limit:
        dataset = dataset[:args.limit]

    if not dataset:
        sys.exit("No labeled images found to classify.")

    print(f"Running evaluation with {args.model} using prompt {args.prompt_version} on {len(dataset)} images")
    print(f"Evaluation project: {args.project} ({args.project_id}), Dataset from: {args.dataset_project}/{args.dataset}")
    run_eval(dataset, model=args.model, prompt_version=args.prompt_version, max_tokens=args.max_tokens, project_id=args.project_id, experiment_name=args.experiment_name)


if __name__ == "__main__":
    main()