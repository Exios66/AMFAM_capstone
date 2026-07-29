"""
OpenRouter Cost Estimator

Run a single image through a vision model and extrapolate token usage/cost
for the full dataset. This is kept separate from the main classifier to avoid
accidentally processing the entire dataset.
"""

import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from src.openrouter_classifier import OpenRouterError, classify_image

# Optional: load from .env file if python-dotenv is installed
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("Note: python-dotenv is not installed; relying on existing environment variables.")


def get_api_key() -> str:
    """Load OpenRouter API key from environment variable."""
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: OPENROUTER_API_KEY environment variable is not set.")
        print("Set it in your terminal with:")
        print('    $env:OPENROUTER_API_KEY="sk-or-v1-..."')
        print("Or create a .env file with:")
        print("    OPENROUTER_API_KEY=sk-or-v1-...")
        sys.exit(1)
    return api_key


def build_markdown_section(
    model: str,
    usage: dict,
    image_counts: list[int],
    input_price_per_million: float,
    output_price_per_million: float
) -> str:
    """Build a markdown section for a single model's token/cost projections."""
    prompt_tokens = usage.get("prompt_tokens", 0)
    completion_tokens = usage.get("completion_tokens", 0)
    total_tokens = usage.get("total_tokens", prompt_tokens + completion_tokens)

    actual_cost = usage.get("cost", 0.0)
    cost_details = usage.get("cost_details", {}) or {}
    actual_prompt_cost = cost_details.get("upstream_inference_prompt_cost", 0.0)
    actual_completion_cost = cost_details.get("upstream_inference_completions_cost", 0.0)

    lines = [
        f"## Model: `{model}`",
        "",
        "### Single-Image Usage (Actual API Response)",
        "",
        f"- **Prompt tokens:** {prompt_tokens:,}",
        f"- **Completion tokens:** {completion_tokens:,}",
        f"- **Total tokens:** {total_tokens:,}",
    ]

    if actual_cost:
        lines.extend([
            f"- **Actual upstream cost:** ${actual_cost:.7f}",
            f"  - Prompt cost: ${actual_prompt_cost:.7f}",
            f"  - Completion cost: ${actual_completion_cost:.7f}",
        ])

    lines.extend([
        "",
        "### Actual Cost Projections",
        "",
        "| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Total Cost** |",
        "|--------|--------------:|------------------:|-------------:|---------------:|",
    ])

    for count in image_counts:
        p = prompt_tokens * count
        c = completion_tokens * count
        t = total_tokens * count
        if actual_cost:
            cost = actual_cost * count
            lines.append(f"| {count:,} | {p:,} | {c:,} | {t:,} | **${cost:,.2f}** |")
        else:
            input_cost = p * (input_price_per_million / 1_000_000)
            output_cost = c * (output_price_per_million / 1_000_000)
            cost = input_cost + output_cost
            lines.append(f"| {count:,} | {p:,} | {c:,} | {t:,} | **${cost:,.4f}** |")

    lines.append("")
    return "\n".join(lines)


def update_markdown(md_path: Path, section: str, model: str) -> None:
    """Insert or replace the model section in openrouter_token_calculation.md."""
    if md_path.exists():
        content = md_path.read_text(encoding="utf-8")
    else:
        content = (
            "# OpenRouter Token and Cost Calculation\n\n"
            "Based on actual single-image runs on OpenRouter.\n\n"
            "## Notes\n\n"
            "- Token counts and costs are extrapolated linearly from one representative image per model.\n"
            "- Actual total cost may vary slightly depending on image dimensions, content, and any OpenRouter/provider price changes.\n"
        )

    escaped_model = re.escape(model)
    pattern = rf"## Model: `{escaped_model}`.*?\n(?=## |\Z)"
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, section, content, flags=re.DOTALL)
    else:
        notes_match = re.search(r"\n## Notes\n", content)
        if notes_match:
            insert_pos = notes_match.start()
            content = content[:insert_pos] + "\n" + section + content[insert_pos:]
        else:
            content = content.rstrip() + "\n\n" + section

    try:
        md_path.write_text(content, encoding="utf-8")
    except OSError as e:
        raise RuntimeError(f"Could not write markdown to {md_path}: {e}") from e


def estimate_cost_for_dataset(
    api_key: str,
    image_path: Path,
    model: str = "moonshotai/kimi-k3",
    num_images: int = 800,
    input_price_per_million: float = None,
    output_price_per_million: float = None
) -> dict:
    """
    Run one image through the vision model and extrapolate token usage/cost
    for the full dataset.

    Args:
        api_key: OpenRouter API key
        image_path: Path to a single representative image
        model: Vision model identifier
        num_images: Number of images to project cost for
        input_price_per_million: Optional USD price per 1M input tokens
        output_price_per_million: Optional USD price per 1M output tokens

    Returns:
        Dictionary with single-image usage and full dataset projection
    """
    result = classify_image(api_key, image_path, model)
    usage = result.get("usage", {})
    if not usage:
        raise OpenRouterError(
            f"OpenRouter response for {image_path} contained no usage data; "
            f"cannot project cost."
        )

    prompt_tokens = usage.get("prompt_tokens", 0)
    completion_tokens = usage.get("completion_tokens", 0)
    total_tokens = usage.get("total_tokens", prompt_tokens + completion_tokens)

    projection = {
        "status": "success",
        "model": model,
        "num_images": num_images,
        "single_image_usage": usage,
        "single_image_prompt_tokens": prompt_tokens,
        "single_image_completion_tokens": completion_tokens,
        "single_image_total_tokens": total_tokens,
        "estimated_total_prompt_tokens": prompt_tokens * num_images,
        "estimated_total_completion_tokens": completion_tokens * num_images,
        "estimated_total_tokens": total_tokens * num_images,
    }

    if input_price_per_million and output_price_per_million:
        input_cost = projection["estimated_total_prompt_tokens"] * (input_price_per_million / 1_000_000)
        output_cost = projection["estimated_total_completion_tokens"] * (output_price_per_million / 1_000_000)
        projection["input_price_per_million"] = input_price_per_million
        projection["output_price_per_million"] = output_price_per_million
        projection["estimated_input_cost_usd"] = round(input_cost, 4)
        projection["estimated_output_cost_usd"] = round(output_cost, 4)
        projection["estimated_total_cost_usd"] = round(input_cost + output_cost, 4)
    else:
        projection["cost_note"] = (
            "Provide input_price_per_million and output_price_per_million "
            "to calculate USD cost, or multiply token counts by OpenRouter pricing for your model."
        )

    return projection


def main() -> int:
    API_KEY = get_api_key()

    IMAGE_PATH = Path(r"c:\Users\grant\AMFAM\processed_balanced_dataset\images\advertisement_0000139610_page_0001.png")

    MODEL = "nex-agi/nex-n2-pro"
    INPUT_PRICE = 3.00
    OUTPUT_PRICE = 15.00
    IMAGE_COUNTS = [800, 25000, 320000]

    if not IMAGE_PATH.is_file():
        print(f"Error: sample image does not exist: {IMAGE_PATH}")
        return 1

    # Run single image and project cost for full 800-image dataset
    try:
        estimate = estimate_cost_for_dataset(
            API_KEY,
            IMAGE_PATH,
            model=MODEL,
            num_images=800,
            input_price_per_million=INPUT_PRICE,
            output_price_per_million=OUTPUT_PRICE
        )
    except OpenRouterError as e:
        print(f"Error: {e}")
        return 1

    section = build_markdown_section(
        MODEL,
        estimate["single_image_usage"],
        IMAGE_COUNTS,
        INPUT_PRICE,
        OUTPUT_PRICE
    )
    md_path = Path(__file__).parent / "openrouter_token_calculation.md"
    try:
        update_markdown(md_path, section, MODEL)
    except RuntimeError as e:
        print(f"Error: {e}")
        return 1

    print(json.dumps(estimate, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
