"""Unit tests for src.openrouter_utils message construction (system-intro split)."""

from src.openrouter_utils import build_vision_messages, split_prompt

SAMPLE_PROMPT = (
    "You classify scanned documents into one of 16 categories.\n\n"
    "Labels: advertisement, budget\n\n"
    "## Output format\n\n"
    "After the scratchpad, output:\n\n"
    "<label>invoice</label>\n\n"
    "The label must be lowercase.\n\n"
    "## Calibration\n\n"
    "- Some trailing rule text.\n"
)


class TestSplitPrompt:
    def test_splits_at_output_format_marker(self):
        system_text, user_text = split_prompt(SAMPLE_PROMPT)
        assert "You classify scanned documents" in system_text
        assert "Labels: advertisement, budget" in system_text
        assert user_text.startswith("## Output format")

    def test_split_is_byte_lossless(self):
        system_text, user_text = split_prompt(SAMPLE_PROMPT)
        assert system_text + user_text == SAMPLE_PROMPT

    def test_no_marker_falls_back_to_system(self):
        system_text, user_text = split_prompt("just a short prompt without sections")
        assert system_text == "just a short prompt without sections"
        assert user_text == ""

    def test_empty_prompt(self):
        assert split_prompt("") == ("", "")


class TestBuildVisionMessagesSplit:
    def test_split_payload_has_system_and_user(self):
        messages = build_vision_messages(SAMPLE_PROMPT, "ZmFrZQ==", split_intro=True)
        assert len(messages) == 2
        assert messages[0]["role"] == "system"
        assert messages[0]["content"].startswith("You classify scanned documents")
        assert messages[1]["role"] == "user"
        content = messages[1]["content"]
        assert content[0]["type"] == "text"
        assert content[0]["text"].startswith("## Output format")
        assert content[1]["type"] == "image_url"
        assert content[1]["image_url"]["url"] == "data:image/png;base64,ZmFrZQ=="

    def test_no_split_legacy_single_user_message(self):
        messages = build_vision_messages(SAMPLE_PROMPT, "ZmFrZQ==", split_intro=False)
        assert len(messages) == 1
        assert messages[0]["role"] == "user"
        content = messages[0]["content"]
        assert content[0]["text"] == SAMPLE_PROMPT
        assert content[1]["image_url"]["url"] == "data:image/png;base64,ZmFrZQ=="

    def test_split_default_off_for_backward_compat(self):
        messages = build_vision_messages(SAMPLE_PROMPT, "ZmFrZQ==")
        assert len(messages) == 1
