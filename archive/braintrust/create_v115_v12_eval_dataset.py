"""
Build a Braintrust evaluation dataset from the union of failed classifications
across prompt versions v11.5, v11.6, v11.7, and v12.

Each failed image appears exactly once (deduplicated by filename). The source
experiments are the ``*_eval`` runs on the ``qwen_v115_eval`` 56-image set plus
the 160-image ``fixed_size_sampled`` runs (``*_reasoning_160``), so both the
persistent failures and the 160-set-only failures are captured:

1. ``qwen3.7-flash_v11_5_eval``
2. ``qwen3.7-flash_v11_6_eval``
3. ``qwen3.7-flash_v11_7_eval-424b5da8`` (complete 56-row v11.7 eval)
4. ``qwen3.7-flash_v11_7_reasoning_160``
5. ``qwen3.7-flash_v12_eval``
6. ``qwen3.7-flash_v12_reasoning_160``

Rows carry the expected label plus metadata recording which versions failed on
that image, each version's predicted label, and the (capped) reasoning trace.
Images are sourced from ``fixed_size_sampled`` and ``fixed_size_sampled_320``.
The dataset is rebuilt idempotently (deleted and recreated). Run with --dry-run
to preview without writing.

Usage:
    python scripts/braintrust/create_v115_v12_eval_dataset.py
    python scripts/braintrust/create_v115_v12_eval_dataset.py --dry-run
    python scripts/braintrust/create_v115_v12_eval_dataset.py --dataset my_eval_set
"""

import argparse
import base64
import hashlib
import os
import sys
from collections import Counter
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
)

REASONING_LIMIT = 4000  # Cap reasoning stored per row to keep the dataset light.

SOURCE_EXPERIMENTS = {
    "v11.5": "qwen3.7-flash_v11_5_eval",
    "v11.6": "qwen3.7-flash_v11_6_eval",
    "v11.7": "qwen3.7-flash_v11_7_eval-424b5da8",
    "v11.7-160": "qwen3.7-flash_v11_7_reasoning_160",
    "v12": "qwen3.7-flash_v12_eval",
    "v12-160": "qwen3.7-flash_v12_reasoning_160",
}


def collect_misses(config, api_key: str, experiment_name: str) -> list[dict]:
    """Fetch one experiment and return one record per misclassification."""
    experiments_by_name = {
        e.get("name"): e for e in list_experiments(api_key, config.project_id)
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

        row_id = hashlib.md5(f"eval-union::{filename}".encode("utf-8")).hexdigest()
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
                    "versions": sorted(record["versions"]),
                },
            },
            "expected": record["expected"],
            "metadata": {
                "versions": sorted(record["versions"]),
                "predictions": record["predictions"],
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
    parser.add_argument("--dataset", default="qwen_v115_v12_eval",
                        help="Name of the dataset to create (default: qwen_v115_v12_eval)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Collect and count misclassifications without creating the dataset")
    args = parser.parse_args()

    config = load_braintrust_config(args.env_file)
    api_key = config.api_key or os.environ.get("BRAINTRUST_API_KEY")
    if not api_key:
        sys.exit("Error: BRAINTRUST_API_KEY is not set (add it to braintrust.env or .env)")

    print(f"Environment: org {config.org_id} / project {config.project_name} ({config.project_id})")

    # Collect per-experiment miss records, keyed by version label.
    by_version: dict[str, list[dict]] = {}
    for version, experiment in SOURCE_EXPERIMENTS.items():
        by_version[version] = collect_misses(config, api_key, experiment)

    # Union across versions, deduplicated by filename.
    union: dict[str, dict] = {}
    for version, records in by_version.items():
        for r in records:
            filename = r["filename"]
            entry = union.setdefault(filename, {
                "expected": r["expected"],
                "versions": set(),
                "predictions": {},
                "predicted": r["predicted"],
                "reasoning": r["reasoning"],
            })
            entry["versions"].add(version)
            entry["predictions"][version] = r["predicted"]
            if len(r["reasoning"]) > len(entry["reasoning"]):
                entry["reasoning"] = r["reasoning"]

    records = []
    for filename, entry in sorted(union.items()):
        records.append({
            "filename": filename,
            "expected": entry["expected"],
            "predicted": entry["predicted"],
            "versions": entry["versions"],
            "predictions": entry["predictions"],
            "reasoning": entry["reasoning"],
        })

    print("\n--- Summary ---")
    for version, recs in by_version.items():
        print(f"  {version:12s} {len(recs)} misclassifications")
    print(f"\nTotal misclassifications: {sum(len(r) for r in by_version.values())}")
    print(f"Unique by filename: {len(records)}")
    by_class: Counter = Counter(r["expected"] for r in records)
    print("By expected class:")
    for cls in sorted(by_class):
        print(f"  {cls:<24} {by_class[cls]}")

    if args.dry_run:
        print("\nDry run — no dataset created.")
        return

    if not records:
        sys.exit("No misclassifications to include; nothing uploaded.")

    smoke_images = load_images_by_filename(config, api_key, config.dataset_project, config.dataset)
    img320 = load_images_by_filename(config, api_key, config.dataset_project, "fixed_size_sampled_320")
    all_images = {**img320, **smoke_images}

    rows = build_rows(records, all_images)
    if not rows:
        sys.exit("No rows could be built (all source images missing); nothing uploaded.")

    print(f"\nUploading {len(rows)} rows to {args.dataset}...")
    upload_rows(config, api_key, args.dataset, rows)
    print(f"Uploaded {len(rows)} annotated misclassification rows to {args.dataset}.")


if __name__ == "__main__":
    main()
