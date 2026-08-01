import unittest

from scripts.braintrust.braintrust_report import build_results


class ReportAccountingTests(unittest.TestCase):
    def test_failures_are_not_silently_removed(self):
        tasks, failures = build_results([
            {"expected": "invoice", "output": "invoice", "input": {"filename": "ok.png"}},
            {"expected": "invoice", "output": "", "error": "provider failure", "input": {"filename": "bad.png"}},
            {"expected": "invoice", "output": "budget", "input": {"filename": "wrong.png"}},
        ])
        self.assertEqual(len(tasks), 2)
        self.assertEqual(len(failures), 1)
        self.assertEqual(failures[0]["status"], "error")
        self.assertEqual(failures[0]["filename"], "bad.png")


if __name__ == "__main__":
    unittest.main()
