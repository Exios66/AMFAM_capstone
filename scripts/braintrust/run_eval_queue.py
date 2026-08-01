"""Run production evaluations sequentially with preflight and checkpoints."""

from __future__ import annotations

import argparse
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
RUNNER = ROOT / "scripts" / "braintrust" / "braintrust_openrouter_input.py"
PREFLIGHT = ROOT / "scripts" / "braintrust" / "preflight_eval.py"


@dataclass(frozen=True)
class Job:
    name: str
    dataset: str
    manifest: str
    expected_rows: int


DEFAULT_JOBS = (
    Job("qwen3.7-flash_v14_reasoning_160_v2", "fixed_size_sampled_v2", "eval_160_v14_v2.jsonl", 160),
    # The repository's canonical dataset name is fixed_size_sampled (the
    # requested fixed_siz_sample name does not exist).
    Job("qwen3.7-flash_v14_fixed_size_sample", "fixed_size_sampled", "eval_fixed_size_sample_v14.jsonl", 160),
    Job("qwen3.7-flash_v14_hard_eval", "qwen_v115_v12_eval", "eval_hard_v14.jsonl", 52),
)


def run(command: list[str], dry_run: bool) -> None:
    print("$ " + " ".join(str(part) for part in command))
    if not dry_run:
        subprocess.run(command, cwd=ROOT, check=True)


def verify_manifest(path: Path, expected_rows: int) -> None:
    if not path.exists():
        raise RuntimeError(f"evaluation produced no manifest: {path}")
    records = {}
    for line in path.read_text(encoding="utf-8").splitlines()[1:]:
        import json
        record = json.loads(line)
        records[record["filename"]] = record
    if len(records) != expected_rows:
        raise RuntimeError(
            f"manifest {path} has {len(records)} rows; expected {expected_rows}"
        )
    incomplete = [name for name, record in records.items() if record.get("status") != "completed"]
    if incomplete:
        raise RuntimeError(f"evaluation has incomplete rows: {', '.join(incomplete[:5])}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--prompt-version", default="v14")
    parser.add_argument("--model", default="qwen/qwen3.7-flash")
    parser.add_argument("--max-tokens", type=int, default=4096)
    args = parser.parse_args()

    for job in DEFAULT_JOBS:
        manifest = ROOT / "reports" / "manifests" / job.manifest
        common = [
            sys.executable,
            str(RUNNER),
            "--dataset",
            job.dataset,
            "--prompt-version",
            args.prompt_version,
            "--model",
            args.model,
            "--max-tokens",
            str(args.max_tokens),
            "--experiment-name",
            job.name,
            "--manifest",
            str(manifest),
        ]
        run(
            [
                sys.executable,
                str(PREFLIGHT),
                "--dataset",
                job.dataset,
                "--prompt-version",
                args.prompt_version,
            ],
            args.dry_run,
        )
        run(common, args.dry_run)
        if not args.dry_run:
            verify_manifest(manifest, job.expected_rows)

    print("QUEUE COMPLETE: all jobs passed preflight and evaluation commands")


if __name__ == "__main__":
    main()
