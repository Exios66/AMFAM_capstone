"""Unit tests for the pure helpers in scripts.braintrust_openrouter_input."""

from scripts.braintrust import braintrust_openrouter_input as bi


class TestNearMissScore:
    def test_zero_when_prediction_correct(self):
        assert bi.near_miss_score("invoice", "invoice", "budget") == 0.0

    def test_one_when_runner_up_is_correct(self):
        assert bi.near_miss_score("budget", "invoice", "invoice") == 1.0

    def test_zero_when_runner_up_does_not_match(self):
        assert bi.near_miss_score("budget", "letter", "invoice") == 0.0

    def test_zero_when_no_runner_up_recorded(self):
        assert bi.near_miss_score("budget", "invoice", "") == 0.0


class TestManifestRecords:
    """Manifest records must carry the reasoning trace (and raw response) so the
    full metric set is derivable locally — reduced-spec/routed runs may log
    their spans to another Braintrust account (--agent / AMFAMv4)."""

    def _completed(self, **overrides):
        kwargs = dict(
            filename="ds__invoice__0001.png", expected="invoice", predicted="invoice",
            attempts=1, used_fallback=False, runner_up="budget", row_cost=0.001,
            routed=False, confidence=0.9, self_report=0.8, escalation_reason="",
            escalation_model=None, escalated_cost=0.0, escalation_error="",
            reasoning_text="**Check 1:** header. **Runner-up:** budget", raw="invoice",
        )
        kwargs.update(overrides)
        return bi._manifest_completed_record(**kwargs)

    def test_completed_record_carries_reasoning_and_raw(self):
        rec = self._completed()
        assert rec["reasoning"] == "**Check 1:** header. **Runner-up:** budget"
        assert rec["raw_response"] == "invoice"
        assert rec["status"] == "completed"
        assert rec["tag"] == "OK"
        assert rec["cost"] == 0.001

    def test_completed_record_tag_miss_on_wrong_prediction(self):
        rec = self._completed(predicted="letter", expected="invoice")
        assert rec["tag"] == "MISS!"

    def test_routed_record_keeps_reasoning_and_escalation_fields(self):
        rec = self._completed(
            routed=True, escalation_model="google/gemini-2.5-flash",
            escalated_cost=0.02, escalation_reason="low confidence",
            reasoning_text="**Runner-up:** invoice", raw="budget", predicted="budget",
        )
        assert rec["reasoning"] == "**Runner-up:** invoice"
        assert rec["routed"] is True
        assert rec["escalated_model"] == "google/gemini-2.5-flash"
        assert rec["escalated_cost"] == 0.02

    def test_error_record_keeps_reasoning(self):
        rec = bi._manifest_error_record(
            filename="ds__letter__0002.png", expected="letter", status="error",
            attempts=3, error="provider 502", reasoning_text="partial trace",
        )
        assert rec["reasoning"] == "partial trace"
        assert rec["tag"] == "ERROR!"
        assert rec["status"] == "error"


class TestExtractClassFromFilename:
    def test_extracts_middle_segment(self):
        name = "processed_balanced__invoice__0001.png"
        assert bi.extract_class_from_filename(name) == "invoice"

    def test_returns_unknown_without_delimiter(self):
        assert bi.extract_class_from_filename("nofields.png") == "unknown"

    def test_handles_extra_segments(self):
        name = "ds__letter__foo__bar.png"
        assert bi.extract_class_from_filename(name) == "letter"


class TestEncodeImageBase64:
    def test_round_trips(self, tmp_path):
        import base64

        raw = b"image-bytes"
        p = tmp_path / "x.png"
        p.write_bytes(raw)
        assert base64.b64decode(bi.encode_image_base64(p)) == raw


class TestLoadDatasetImages:
    def test_only_includes_valid_classes(self, tmp_path):
        # Valid class filenames.
        (tmp_path / "ds__invoice__001.png").write_bytes(b"x")
        (tmp_path / "ds__letter__002.png").write_bytes(b"x")
        # Invalid class -> excluded.
        (tmp_path / "ds__notaclass__003.png").write_bytes(b"x")
        # Non-png -> ignored by glob.
        (tmp_path / "ds__invoice__004.txt").write_bytes(b"x")

        dataset = bi.load_dataset_images(tmp_path)
        classes = sorted(d["expected"] for d in dataset)
        assert classes == ["invoice", "letter"]
        for d in dataset:
            assert set(d.keys()) == {"image_b64", "filename", "expected"}

    def test_empty_dir_returns_empty_list(self, tmp_path):
        assert bi.load_dataset_images(tmp_path) == []


class TestGetApiKeys:
    def test_returns_both_keys(self, monkeypatch):
        monkeypatch.setenv("OPENROUTER_API_KEY", "or-key")
        monkeypatch.setenv("BRAINTRUST_API_KEY", "bt-key")
        assert bi.get_api_keys() == ("or-key", "bt-key")

    def test_exits_when_any_missing(self, monkeypatch):
        import pytest
        from unittest import mock

        monkeypatch.setenv("OPENROUTER_API_KEY", "or-key")
        monkeypatch.delenv("BRAINTRUST_API_KEY", raising=False)
        with mock.patch("src.env_utils.load_dotenv_if_available"):
            with pytest.raises(SystemExit):
                bi.get_api_keys()

    def test_agent_uses_agent_key(self, monkeypatch):
        import pytest
        from unittest import mock

        monkeypatch.setenv("OPENROUTER_API_KEY", "or-key")
        monkeypatch.setenv("AGENT_BRAINTRUST_API_KEY", "agent-key")
        monkeypatch.delenv("BRAINTRUST_API_KEY", raising=False)
        with mock.patch("src.env_utils.load_dotenv_if_available"):
            assert bi.get_api_keys(agent=True) == ("or-key", "agent-key")

    def test_agent_exits_without_agent_key(self, monkeypatch):
        import pytest
        from unittest import mock

        monkeypatch.setenv("OPENROUTER_API_KEY", "or-key")
        monkeypatch.delenv("AGENT_BRAINTRUST_API_KEY", raising=False)
        monkeypatch.setenv("BRAINTRUST_API_KEY", "bt-key")
        with mock.patch("src.env_utils.load_dotenv_if_available"):
            with pytest.raises(SystemExit):
                bi.get_api_keys(agent=True)


class TestParseScorers:
    def test_none_defaults_to_caller_choice(self):
        assert bi.parse_scorers(None) is None

    def test_parses_csv(self):
        assert bi.parse_scorers("exact_match,failure") == ["exact_match", "failure"]

    def test_single(self):
        assert bi.parse_scorers("exact_match") == ["exact_match"]

    def test_none_keyword_means_no_scorers(self):
        assert bi.parse_scorers("none") == []
        assert bi.parse_scorers("none") is not None

    def test_empty_means_no_scorers(self):
        assert bi.parse_scorers("") == []

    def test_whitespace_tolerated(self):
        assert bi.parse_scorers(" exact_match , cost ") == ["exact_match", "cost"]

    def test_unknown_scorer_rejected(self):
        import pytest

        with pytest.raises(SystemExit):
            bi.parse_scorers("exact_match,bogus")


class TestBuildExtraBody:
    def test_qwen_high_without_budget(self):
        body = bi._build_extra_body("qwen/qwen3.7-flash", "high")
        assert body == {"reasoning": {"enabled": True, "effort": "high"},
                        "include_reasoning": True}

    def test_qwen_budget_tokens_added(self):
        body = bi._build_extra_body("qwen/qwen3.7-flash", "high", 32768)
        assert body["reasoning"]["budget_tokens"] == 32768
        assert body["reasoning"]["effort"] == "high"
        assert body["reasoning"]["enabled"] is True

    def test_gemini_budget_tokens_added(self):
        body = bi._build_extra_body("google/gemini-2.5-flash", "max", 8192)
        assert body["reasoning"]["budget_tokens"] == 8192
        assert body["reasoning"]["effort"] == "max"

    def test_no_budget_keeps_existing_shape(self):
        body = bi._build_extra_body("qwen/qwen3.7-flash", None)
        assert "budget_tokens" not in body["reasoning"]
