"""
Build a Braintrust evaluation dataset for PROMPT_V11_5 from the failed
classification samples of two v10 runs:

1. ``qwen3.7-flash_v10_smoke_full`` — 37 misclassifications on the
   ``qwen_misclassification_smoke_v1_v11`` smoke set (images from
   ``fixed_size_sampled``).
2. ``qwen3.7-flash_v10_reasoning_320`` — 47 misclassifications on the
   ``fixed_size_sampled_320`` 320-image set.

The union is deduplicated by filename; each row carries the expected label, the
source experiment, the v10 predicted label, and the v10 reasoning trace. The
dataset is rebuilt idempotently (deleted and recreated). Run with --dry-run to
preview without writing.

Usage:
    python scripts/braintrust/create_v115_eval_dataset.py
    python scripts/braintrust/create_v115_eval_dataset.py --dry-run
    python scripts/braintrust/create_v115_eval_dataset.py --dataset my_v115_set
"""

import argparse
import base64
import hashlib
import os
import sys
from collections import Counter
from dataclasses import replace
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

import braintrust

from src.braintrust_config import load_braintrust_config
from src.braintrust_utils import (
    delete_dataset_by_name,
    fetch_experiment_rows,
    find_misses,
    load_braintrust_dataset,
)

REASONING_LIMIT = 4000  # Cap reasoning stored per row to keep the dataset light.

V10_SMOKE_FULL_EXP = "qwen3.7-flash_v10_smoke_full"
V10_REASONING_320_EXP = "qwen3.7-flash_v10_reasoning_320"


def collect_misses(config, api_key: str, experiment_name: str) -> list[dict]:
    """Fetch one experiment and return one record per misclassification."""
    experiments_by_name = {
        e.get("name"): e for e in __import__("src.braintrust_utils", fromlist=["list_experiments"]).list_experiments(api_key, config.project_id)
    }
    meta = experiments_by_name.get(experiment_name)
    if meta is None:
        sys.exit(f"Experiment '{experiment_name}' not found in project {config.project_id}")

    print(f"Fetching {experiment_name}...")
    rows = fetch_experiment_rows(api_key, meta["id"])
    misses = find_misses(rows)

    records = []
    for miss in misses:
        records.append({
            "experiment": experiment_name,
            "expected": miss["expected"],
            "predicted": miss["predicted"],
            "filename": miss["filename"],
            "reasoning": miss["reasoning"],
        })
    print(f"  {experiment_name}: {len(misses)} misclassifications")
    return records


def load_images_by_filename(config, api_key: str, dataset_project: str, dataset: str) -> dict[str, bytes]:
    """Download a source dataset's images, keyed by attachment filename."""
    source_key = config.data_api_key or None
    records = load_braintrust_dataset(
        dataset_project,
        dataset,
        dataset_api_key=source_key,
        org_id=config.org_id,
        api_base=config.api_base,
    )
    by_filename: dict[str, bytes] = {}
    for record in records:
        by_filename[record["filename"]] = base64.b64decode(record["image_b64"])
    print(f"Loaded {len(by_filename)} source images from {dataset_project}/{dataset}")
    return by_filename


def build_rows(records: list[dict], images: dict[str, bytes]) -> list[tuple[str, dict]]:
    rows: list[tuple[str, dict]] = []
    missing = 0
    for record in records:
        filename = record["filename"]
        image_bytes = images.get(filename)
        if image_bytes is None:
            missing += 1
            print(f"SKIP {record['expected']:<24} {filename}: image not found in source dataset", file=sys.stderr)
            continue

        row_id = hashlib.md5(f"{record['experiment']}::{filename}".encode("utf-8")).hexdigest()
        reasoning = record["reasoning"][:REASONING_LIMIT]
        rows.append((row_id, {
            "input": {
                "image": braintrust.Attachment(
                    data=image_bytes,
                    filename=filename,
                    content_type="image/png",
                ),
                "filename": filename,
                "metadata": {
                    "source_experiment": record["experiment"],
                },
            },
            "expected": record["expected"],
            "metadata": {
                "source_experiment": record["experiment"],
                "predicted": record["predicted"],
                "misclassification": f"{record['expected']} -> {record['predicted']}",
                "reasoning": reasoning or None,
            },
        }))

    if missing:
        print(f"WARNING: skipped {missing} records whose image was not in the source dataset", file=sys.stderr)
    return rows


def upload_rows(config, api_key: str, dataset_name: str, rows: list[tuple[str, dict]]) -> None:
    deleted = delete_dataset_by_name(api_key, config.project_id, dataset_name, config.api_base)
    if deleted:
        print(f"Deleted existing dataset {dataset_name} ({deleted})")

    braintrust.login(api_key=api_key, force_login=True)
    dataset = braintrust.init_dataset(project_id=config.project_id, name=dataset_name)

    for i, (row_id, row) in enumerate(rows):
        dataset.insert(
            input=row["input"],
            expected=row["expected"],
            metadata=row["metadata"],
            id=row_id,
        )
        if (i + 1) % 25 == 0 or (i + 1) == len(rows):
            print(f"  Inserted {i + 1}/{len(rows)} rows...")

    dataset.flush()
    print(f"\nDataset ready: {dataset_name} ({len(rows)} rows)")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--env-file", default="braintrust.env",
                        help="Path to the Braintrust env file (default: braintrust.env)")
    parser.add_argument("--dataset", default="qwen_v115_eval",
                        help="Name of the dataset to create (default: qwen_v115_eval)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Collect and count misclassifications without creating the dataset")
    args = parser.parse_args()

    config = load_braintrust_config(args.env_file)
    api_key = config.api_key or os.environ.get("BRAINTRUST_API_KEY")
    if not api_key:
        sys.exit("Error: BRAINTRUST_API_KEY is not set (add it to braintrust.env or .env)")

    print(f"Environment: org {config.org_id} / project {config.project_name} ({config.project_id})")

    records = collect_misses(config, api_key, V10_SMOKE_FULL_EXP)
    records += collect_misses(config, api_key, V10_REASONING_320_EXP)

    # Deduplicate by filename (prefer the smoke copy, but keep both sets' totals).
    by_filename: dict[str, dict] = {}
    for r in records:
        by_filename.setdefault(r["filename"], r)
    unique = list(by_filename.values())

    per_src = Counter(r["experiment"] for r in records)
    print("\n--- Summary ---")
    print(f"Total misclassifications: {len(records)} ({dict(per_src)})")
    print(f"Unique by filename: {len(unique)}")
    by_class: Counter = Counter(r["expected"] for r in unique)
    print("By expected class:")
    for cls in sorted(by_class):
        print(f"  {cls:<24} {by_class[cls]}")

    if args.dry_run:
        print("\nDry run — no dataset created.")
        return

    if not unique:
        sys.exit("No misclassifications to include; nothing uploaded.")

    # Smoke images live in fixed_size_sampled; 320 images in fixed_size_sampled_320.
    smoke_images = load_images_by_filename(config, api_key, config.dataset_project, config.dataset)
    img320 = load_images_by_filename(config, api_key, config.dataset_project, "fixed_size_sampled_320")
    all_images = {**img320, **smoke_images}

    rows = build_rows(unique, all_images)
    if not rows:
        sys.exit("No rows could be built (all source images missing); nothing uploaded.")

    print(f"\nUploading {len(rows)} rows to {args.dataset}...")
    upload_rows(config, api_key, args.dataset, rows)
    print(f"Uploaded {len(rows)} annotated misclassification rows to {args.dataset}.")


if __name__ == "__main__":
    main()
