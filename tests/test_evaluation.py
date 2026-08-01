import json
import tempfile
import unittest
from pathlib import Path

from src.evaluation import ManifestStore, validate_dataset


class EvaluationTests(unittest.TestCase):
    def record(self, filename="one.png"):
        return {
            "filename": filename,
            "expected": "invoice",
            "image_b64": "aGVsbG8=",
        }

    def test_dataset_validation_rejects_duplicates(self):
        with self.assertRaisesRegex(ValueError, "duplicate filename"):
            validate_dataset([self.record(), self.record()])

    def test_dataset_validation_rejects_missing_images(self):
        row = self.record()
        row["image_b64"] = ""
        with self.assertRaisesRegex(ValueError, "no image data"):
            validate_dataset([row])

    def test_manifest_reuses_only_completed_rows(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "run.jsonl"
            metadata = {"model": "test", "prompt_version": "v14"}
            store = ManifestStore(path, metadata)
            store.append({
                "filename": "one.png",
                "status": "completed",
                "predicted": "invoice",
            })
            store.append({
                "filename": "two.png",
                "status": "error",
                "predicted": "",
            })

            resumed = ManifestStore(path, metadata)
            self.assertEqual(resumed.get_completed("one.png")["predicted"], "invoice")
            self.assertIsNone(resumed.get_completed("two.png"))
            lines = path.read_text(encoding="utf-8").splitlines()
            self.assertEqual(json.loads(lines[0])["type"], "header")

    def test_manifest_rejects_mismatched_run(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "run.jsonl"
            ManifestStore(path, {"prompt_version": "v14"}).initialize()
            with self.assertRaisesRegex(ValueError, "metadata"):
                ManifestStore(path, {"prompt_version": "v13"})


if __name__ == "__main__":
    unittest.main()
