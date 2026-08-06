import unittest

from src.prompts import DEFAULT_PROMPT_VERSION, get_prompt, list_prompt_versions
from src.openrouter_classifier import clean_prediction


class PromptTests(unittest.TestCase):
    def test_v14_is_registered_and_default(self):
        self.assertEqual(DEFAULT_PROMPT_VERSION, "v17.2")
        self.assertIn("v14", list_prompt_versions())
        prompt = get_prompt("v14")
        self.assertIn("v14 production precedence", prompt)
        self.assertIn("specialist science", prompt)

    def test_unknown_version_fails_loudly(self):
        with self.assertRaisesRegex(ValueError, "Unknown prompt version"):
            get_prompt("v999")

    def test_prediction_parser_prefers_final_label(self):
        response = "Reasoning mentions budget and form.\n<label>invoice</label>"
        self.assertEqual(clean_prediction(response), "invoice")

    def test_v18_1_is_registered_with_routing_improvements(self):
        prompt = get_prompt("v18.1")
        self.assertIn("v18.1", list_prompt_versions())
        self.assertIn("RUNNER-UP RESCUE", prompt)
        self.assertIn("FORM IS NEVER A DEFAULT", prompt)
        self.assertIn("<confidence>87</confidence>", prompt)

    def test_v18_1_keeps_v18_exemplar_base(self):
        prompt = get_prompt("v18.1")
        self.assertIn("PHS 398", prompt)  # v18 exemplar appendix retained
        self.assertIn("MSDS", prompt)

    def test_v19_is_vote_fork_of_v18_1(self):
        v18_1 = get_prompt("v18.1")
        v19 = get_prompt("v19")
        self.assertIn("v19", list_prompt_versions())
        self.assertIn("ONE INDEPENDENT VOTE", v19)
        self.assertTrue(v19.endswith(v18_1), "v19 must be v18.1 with the vote preamble prepended")


if __name__ == "__main__":
    unittest.main()
