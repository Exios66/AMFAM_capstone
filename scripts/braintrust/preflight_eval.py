"""Validate a prompt and evaluation dataset without sending model requests."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from src.braintrust_config import load_braintrust_config
from src.braintrust_utils import load_braintrust_dataset
from src.evaluation import validate_dataset
from src.env_utils import require_env
from src.prompts import get_prompt
from scripts.braintrust.braintrust_openrouter_input import load_dataset_images


def main() -> None:
    config = load_braintrust_config()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", default=config.dataset)
    parser.add_argument("--dataset-project", default=config.dataset_project)
    parser.add_argument("--images-dir", type=Path)
    parser.add_argument("--prompt-version", default="v14")
    args = parser.parse_args()

    get_prompt(args.prompt_version)
    require_env("BRAINTRUST_API_KEY", "OPENROUTER_API_KEY")
    if args.images_dir:
        dataset = load_dataset_images(args.images_dir)
    else:
        dataset = load_braintrust_dataset(
            args.dataset_project,
            args.dataset,
            config.data_api_key or None,
            org_id=config.org_id,
            api_base=config.api_base,
        )
    validate_dataset(dataset)
    print(
        f"PREFLIGHT OK: prompt={args.prompt_version} "
        f"dataset={args.dataset_project}/{args.dataset} rows={len(dataset)}"
    )


if __name__ == "__main__":
    main()
