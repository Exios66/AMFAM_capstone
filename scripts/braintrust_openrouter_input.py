"""
Braintrust Prompt Evaluation for Document Classification

Runs the classification prompt against the fixed-size sampled dataset (16 classes)
and logs results to Braintrust for prompt iteration in their UI.

Prerequisites:
    pip install braintrust openai
    Set BRAINTRUST_API_KEY and OPENROUTER_API_KEY in your .env file.

Usage:
    python scripts/braintrust_prompt_eval.py
"""

import base64
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

# Optional: load from .env file
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

import braintrust
from openai import OpenAI

from src.openrouter_classifier import CLASSIFICATION_PROMPT, VALID_CLASSES, clean_prediction

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DATASET_DIR = Path(r"c:\Users\grant\AMFAM\1024x1024_10perclass_160\images")
MODEL = "anthropic/claude-opus-5"  # Anthropic flagship reasoning model
PROJECT_NAME = "AMFAM-Doc-Classification"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_api_keys() -> tuple[str, str]:
    """Load required API keys from environment."""
    openrouter_key = os.environ.get("OPENROUTER_API_KEY")
    braintrust_key = os.environ.get("BRAINTRUST_API_KEY")

    missing = []
    if not openrouter_key:
        missing.append("OPENROUTER_API_KEY")
    if not braintrust_key:
        missing.append("BRAINTRUST_API_KEY")

    if missing:
        print(f"Error: Missing environment variables: {', '.join(missing)}")
        print("Set them in your .env file or terminal.")
        sys.exit(1)

    return openrouter_key, braintrust_key


def extract_class_from_filename(filename: str) -> str:
    """
    Extract the ground-truth class from the fixed-size dataset filename.
    Format: processed_balanced__{class}__{original_name}.png
    """
    parts = filename.split("__")
    if len(parts) >= 2:
        return parts[1]
    return "unknown"


def encode_image_base64(image_path: Path) -> str:
    """Encode image file to base64 string."""
    with open(image_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def load_dataset_images(dataset_dir: Path) -> list[dict]:
    """
    Load all images from the fixed-size dataset directory.
    Returns list of dicts with image_path and expected_class.
    """
    images = sorted(dataset_dir.glob("*.png"))
    dataset = []
    for img_path in images:
        expected_class = extract_class_from_filename(img_path.name)
        if expected_class in VALID_CLASSES:
            dataset.append({
                "image_path": str(img_path),
                "filename": img_path.name,
                "expected": expected_class,
            })
    return dataset


# ---------------------------------------------------------------------------
# Braintrust Eval
# ---------------------------------------------------------------------------

def run_eval():
    """Run the classification prompt against all dataset images and log to Braintrust."""
    openrouter_key, _ = get_api_keys()

    # Wrap OpenAI client pointed at OpenRouter with Braintrust logging
    client = braintrust.wrap_openai(
        OpenAI(
            base_url="https://openrouter.ai/api/v1",
            api_key=openrouter_key,
        )
    )

    # Load dataset
    dataset = load_dataset_images(DATASET_DIR)
    print(f"Loaded {len(dataset)} images from {DATASET_DIR}")
    print(f"Classes represented: {sorted(set(d['expected'] for d in dataset))}")
    print()

    # Run eval
    @braintrust.traced
    def classify_document(input_data: dict) -> str:
        """Classify a single document image via the vision model."""
        image_path = Path(input_data["image_path"])
        image_b64 = encode_image_base64(image_path)

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": CLASSIFICATION_PROMPT},
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/png;base64,{image_b64}"
                            },
                        },
                    ],
                }
            ],
            max_tokens=1024,
            temperature=0.1,
            extra_body={
                "reasoning": {"effort": "medium"},
            },
        )

        raw = response.choices[0].message.content or ""

        # Extract reasoning from response if available
        reasoning_text = ""
        msg = response.choices[0].message
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

    # Run the Braintrust evaluation
    eval_result = braintrust.Eval(
        PROJECT_NAME,
        data=lambda: [
            {
                "input": {"image_path": d["image_path"], "filename": d["filename"]},
                "expected": d["expected"],
            }
            for d in dataset
        ],
        task=classify_document,
        scores=[exact_match],
    )

    # Print local summary
    print()
    print("=" * 60)
    print("EVALUATION COMPLETE")
    print("=" * 60)
    print(f"Results logged to Braintrust project: {PROJECT_NAME}")
    print("Open https://www.braintrust.dev to view results and iterate on the prompt.")


if __name__ == "__main__":
    run_eval()
