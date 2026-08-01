"""
Build a Braintrust smoke-test dataset from every misclassification across the
Qwen prompt-version experiments (v1-v11).

For each experiment listed in QWEN_EXPERIMENTS (see braintrust.env) the script:

1. Fetches the experiment's events from Braintrust and finds every row whose
   prediction does not match the expected label.
2. Pulls the source image for each misclassified filename from the source
   dataset (BRAINTRUST_DATASET, default ``fixed_size_sampled``).
3. Inserts each misclassification into BRAINTRUST_SMOKE_DATASET (default
   ``qwen_misclassification_smoke_v1_v11``) as a row whose annotation records
   the prompt version the misclassification stemmed from, the source
   experiment, the predicted label, and the reasoning trace.

The dataset is rebuilt idempotently (deleted and recreated) on every run, and
every row carries a deterministic id, so repeated runs never duplicate rows.
Run with --dry-run to preview without writing anything.

Usage:
    python scripts/braintrust/create_misclassification_smoke_dataset.py
    python scripts/braintrust/create_misclassification_smoke_dataset.py --dry-run
    python scripts/braintrust/create_misclassification_smoke_dataset.py --dataset my_smoke_set
    python scripts/braintrust/create_misclassification_smoke_dataset.py --experiments "qwen3.7-flash_v9_reasoning qwen3.7-flash_v10_reasoning"
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
    list_experiments,
    load_braintrust_dataset,
    resolve_prompt_version,
)

REASONING_LIMIT = 4000  # Cap reasoning stored per row to keep the dataset light.


def collect_misses(config, api_key: str) -> list[dict]:
    """Fetch each configured experiment and return one record per misclassification.

    Each record: ``{experiment, prompt_version, expected, predicted, filename,
    reasoning}``. Experiments with no misses contribute nothing. If
    ``config.qwen_experiments`` is empty, every qwen3.7-flash experiment in the
    project is discovered automatically.
    """
    experiments_by_name = {e.get("name"): e for e in list_experiments(api_key, config.project_id)}
    names = list(config.qwen_experiments) or [
        e["name"] for e in experiments_by_name.values() if e.get("name", "").startswith("qwen3.7-flash")
    ]

    records: list[dict] = []
    for name in names:
        meta = experiments_by_name.get(name)
        if meta is None:
            print(f"WARNING: experiment '{name}' not found in project {config.project_id}", file=sys.stderr)
            continue

        print(f"Fetching {name}...")
        rows = fetch_experiment_rows(api_key, meta["id"])
        misses = find_misses(rows)
        version = resolve_prompt_version(meta)

        for miss in misses:
            records.append({
                "experiment": name,
                "prompt_version": version,
                "expected": miss["expected"],
                "predicted": miss["predicted"],
                "filename": miss["filename"],
                "reasoning": miss["reasoning"],
            })
        print(f"  {name}: {len(misses)} misclassifications (prompt {version})")
        if misses:
            print(f"    e.g. {misses[0]['expected']} -> {misses[0]['predicted']} ({misses[0]['filename']})")

    return records


def load_images_by_filename(config, api_key: str) -> dict[str, bytes]:
    """Download the source dataset's images, keyed by attachment filename."""
    source_key = config.data_api_key or None
    records = load_braintrust_dataset(
        config.dataset_project,
        config.dataset,
        dataset_api_key=source_key,
        org_id=config.org_id,
        api_base=config.api_base,
    )
    by_filename: dict[str, bytes] = {}
    for record in records:
        by_filename[record["filename"]] = base64.b64decode(record["image_b64"])
    print(f"Loaded {len(by_filename)} source images from {config.dataset_project}/{config.dataset}")
    return by_filename


def build_rows(records: list[dict], images: dict[str, bytes]) -> list[tuple[str, dict]]:
    """Turn miss records into (row_id, row) pairs ready for dataset insertion."""
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
                    "prompt_version": record["prompt_version"],
                    "source_experiment": record["experiment"],
                },
            },
            "expected": record["expected"],
            "metadata": {
                "prompt_version": record["prompt_version"],
                "source_experiment": record["experiment"],
                "predicted": record["predicted"],
                "misclassification": f"{record['expected']} -> {record['predicted']}",
                "reasoning": reasoning or None,
            },
        }))

    if missing:
        print(f"WARNING: skipped {missing} records whose image was not in the source dataset", file=sys.stderr)
    return rows


def upload_rows(config, api_key: str, rows: list[tuple[str, dict]]) -> None:
    """Delete any existing smoke dataset and insert ``rows`` into a fresh one."""
    deleted = delete_dataset_by_name(api_key, config.project_id, config.smoke_dataset, config.api_base)
    if deleted:
        print(f"Deleted existing dataset {config.smoke_dataset} ({deleted})")

    braintrust.login(api_key=api_key, force_login=True)
    dataset = braintrust.init_dataset(project_id=config.project_id, name=config.smoke_dataset)

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
    print(f"\nDataset ready: {config.smoke_dataset} ({len(rows)} rows)")


def print_summary(records: list[dict]) -> None:
    by_version: Counter = Counter(r["prompt_version"] for r in records)
    by_class: Counter = Counter(r["expected"] for r in records)

    print("\n--- Summary ---")
    print(f"Total misclassifications: {len(records)}")
    print("By prompt version:")
    for version in sorted(by_version, key=lambda v: (len(v.split('.')), v)):
        print(f"  {version:<6} {by_version[version]}")
    print("By expected class:")
    for cls in sorted(by_class):
        print(f"  {cls:<24} {by_class[cls]}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--env-file", default="braintrust.env",
                        help="Path to the Braintrust env file (default: braintrust.env)")
    parser.add_argument("--dataset", default=None,
                        help="Override BRAINTRUST_SMOKE_DATASET (default: value from env)")
    parser.add_argument("--experiments", default=None,
                        help="Space-separated experiment names; overrides QWEN_EXPERIMENTS from env")
    parser.add_argument("--dry-run", action="store_true",
                        help="Collect and count misclassifications without creating the dataset")
    args = parser.parse_args()

    config = load_braintrust_config(args.env_file)
    api_key = config.api_key or os.environ.get("BRAINTRUST_API_KEY")
    if not api_key:
        sys.exit("Error: BRAINTRUST_API_KEY is not set (add it to braintrust.env or .env)")

    if args.dataset:
        config = replace(config, smoke_dataset=args.dataset)
    if args.experiments:
        config = replace(config, qwen_experiments=tuple(e for e in args.experiments.split() if e))

    print(f"Environment: org {config.org_id} / project {config.project_name} ({config.project_id})")
    print(f"Source dataset: {config.dataset_project}/{config.dataset}")

    records = collect_misses(config, api_key)
    print_summary(records)

    if args.dry_run:
        print("\nDry run — no dataset created.")
        return

    if not records:
        sys.exit("No misclassifications to include; nothing uploaded.")

    images = load_images_by_filename(config, api_key)
    rows = build_rows(records, images)
    if not rows:
        sys.exit("No rows could be built (all source images missing); nothing uploaded.")

    print(f"\nUploading {len(rows)} rows to {config.smoke_dataset}...")
    upload_rows(config, api_key, rows)

    per_version = Counter(r["prompt_version"] for r in records)
    print(f"Uploaded {len(rows)} annotated misclassification rows across "
          f"{len(per_version)} prompt versions to {config.smoke_dataset}.")


if __name__ == "__main__":
    main()
