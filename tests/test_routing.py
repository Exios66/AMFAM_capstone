"""Unit tests for src.routing (confidence-gated escalation)."""

import pytest

from src.routing import (
    escalation_reason,
    select_escalation_fraction,
    should_escalate,
    single_pass_confidence,
)


class TestSinglePassConfidence:
    def test_high_self_report_high_confidence(self):
        conf = single_pass_confidence(0.9, "invoice", "", source="self-report")
        assert conf == pytest.approx(0.9)

    def test_low_self_report_low_confidence(self):
        conf = single_pass_confidence(0.1, "invoice", "", source="self-report")
        assert conf == pytest.approx(0.1)

    def test_missing_self_report_neutral(self):
        conf = single_pass_confidence(None, "invoice", "", source="self-report")
        assert conf == pytest.approx(0.5)

    def test_uncertainty_phrasing_penalizes(self):
        clean = single_pass_confidence(None, "invoice", "", "clear evidence", source="heuristic")
        unsure = single_pass_confidence(None, "invoice", "", "cannot determine the class", source="heuristic")
        assert unsure < clean

    def test_runner_up_disagreement_penalizes(self):
        agree = single_pass_confidence(0.8, "invoice", "invoice", source="blend")
        disagree = single_pass_confidence(0.8, "invoice", "budget", source="blend")
        assert disagree < agree

    def test_clamped_to_unit_interval(self):
        conf = single_pass_confidence(1.0, "a", "", "", source="self-report")
        assert 0.0 <= conf <= 1.0
        conf = single_pass_confidence(0.0, "a", "b", "hard to tell", source="blend")
        assert 0.0 <= conf <= 1.0

    def test_unknown_source_raises(self):
        with pytest.raises(ValueError, match="confidence source"):
            single_pass_confidence(None, "a", "", source="nope")


class TestShouldEscalate:
    def test_below_threshold_escalates(self):
        assert should_escalate(0.3, 0.4) is True

    def test_at_threshold_does_not_escalate(self):
        assert should_escalate(0.4, 0.4) is False

    def test_above_threshold_does_not_escalate(self):
        assert should_escalate(0.9, 0.4) is False


class TestSelectEscalationFraction:
    def test_selects_lowest_fraction(self):
        confidences = {"a": 0.9, "b": 0.1, "c": 0.5, "d": 0.2}
        tail = select_escalation_fraction(confidences, 0.5)
        assert set(tail) == {"b", "d"}

    def test_alpha_zero_selects_nothing(self):
        assert select_escalation_fraction({"a": 0.1}, 0.0) == []

    def test_none_confidence_sorts_below_all(self):
        confidences = {"a": None, "b": 0.0, "c": 0.99}
        tail = select_escalation_fraction(confidences, 0.34)
        assert "a" in tail

    def test_full_tail_when_alpha_one(self):
        confidences = {"a": 0.5, "b": 0.9}
        assert len(select_escalation_fraction(confidences, 1.0)) == 2

    def test_deterministic_ties(self):
        confidences = {"x": 0.3, "y": 0.3, "z": 0.9}
        assert select_escalation_fraction(confidences, 0.34) == ["x"]


class TestEscalationReason:
    def test_uncertainty_wins(self):
        reason = escalation_reason(0.2, "budget", "invoice", uncertainty=True)
        assert "uncertainty" in reason

    def test_runner_up_conflict(self):
        reason = escalation_reason(0.5, "budget", "invoice", uncertainty=False)
        assert "runner-up conflict" in reason

    def test_low_confidence_fallback(self):
        reason = escalation_reason(0.3, "", "invoice", uncertainty=False)
        assert "low confidence" in reason
