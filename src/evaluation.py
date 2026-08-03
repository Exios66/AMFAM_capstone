"""Shared evaluation validation, accounting, and resumable-run helpers."""

from __future__ import annotations

import json
import hashlib
import threading
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from src.constants import DOCUMENT_CLASSES


def validate_dataset(dataset: list[dict]) -> None:
    """Fail before an evaluation if its input cannot produce a valid score."""
    if not dataset:
        raise ValueError("evaluation dataset is empty")

    seen: set[str] = set()
    for index, row in enumerate(dataset):
        filename = str(row.get("filename") or "")
        expected = row.get("expected")
        if not filename:
            raise ValueError(f"dataset row {index} has no filename")
        if filename in seen:
            raise ValueError(f"dataset contains duplicate filename: {filename}")
        seen.add(filename)
        if expected not in DOCUMENT_CLASSES:
            raise ValueError(f"dataset row {filename} has invalid expected class: {expected!r}")
        if not row.get("image_b64"):
            raise ValueError(f"dataset row {filename} has no image data")


def dataset_fingerprint(dataset: list[dict]) -> str:
    """Return a stable identity for labels and filenames in an evaluation."""
    payload = "\n".join(
        f"{row['filename']}\0{row['expected']}" for row in dataset
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


class ManifestStore:
    """Thread-safe JSONL manifest used to resume interrupted evaluations.

    The first line is a run header. Subsequent lines are append-only row states;
    the last state for a filename is authoritative. A manifest is reusable only
    when its run metadata matches the current evaluation exactly.
    """

    def __init__(self, path: str | Path, metadata: dict[str, Any]):
        self.path = Path(path)
        self.metadata = metadata
        self._lock = threading.Lock()
        self.records: dict[str, dict[str, Any]] = {}
        self.reused = False
        self._load()

    def _load(self) -> None:
        if not self.path.exists():
            return
        try:
            lines = self.path.read_text(encoding="utf-8").splitlines()
            if not lines:
                return
            header = json.loads(lines[0])
            if header.get("type") != "header" or header.get("metadata") != self.metadata:
                raise ValueError("manifest metadata does not match this evaluation")
            for line in lines[1:]:
                record = json.loads(line)
                if record.get("filename"):
                    self.records[record["filename"]] = record
            self.reused = True
        except (OSError, json.JSONDecodeError, ValueError) as exc:
            raise ValueError(f"cannot reuse manifest {self.path}: {exc}") from exc

    def initialize(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        if self.path.exists() and self.path.stat().st_size > 0:
            return
        self.path.write_text(
            json.dumps({"type": "header", "metadata": self.metadata}, sort_keys=True) + "\n",
            encoding="utf-8",
        )

    def get_completed(self, filename: str) -> dict[str, Any] | None:
        record = self.records.get(filename)
        if record and record.get("status") == "completed":
            return record
        return None

    def append(self, record: dict[str, Any]) -> None:
        record = {**record, "updated_at": utc_now()}
        line = json.dumps(record, sort_keys=True) + "\n"
        with self._lock:
            self.initialize()
            with self.path.open("a", encoding="utf-8") as stream:
                stream.write(line)
                stream.flush()
            self.records[str(record["filename"])] = record


def classify_row_status(output: Any, error: Any) -> str:
    """Return the accounting status for one evaluator row."""
    if error is not None:
        return "error"
    if output is None or str(output).strip() == "":
        return "empty"
    return "scored"
