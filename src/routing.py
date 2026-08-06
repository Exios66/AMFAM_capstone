"""Confidence-gated escalation (routing) helpers for the eval runner.

The Monte Carlo routing study (`reports/monte_carlo/routing_abstention.md`)
established that routing the lowest-confidence tail to a genuinely stronger
model is the best accuracy/cost lever (+4.3 pp at 1.2x for alpha=10%,
assumed escalated-model accuracy 90%). This module turns that simulation into
a per-inference decision:

- ``single_pass_confidence`` — a ``[0, 1]`` confidence for ONE classification
  run (the corpus-based confidence in ``src.monte_carlo.py`` needs many runs
  per image and is unavailable at inference time). It blends the model's
  ``<confidence>`` self-report with the two free signals from a single trace:
  uncertainty phrasing (``src.monte_carlo.uncertainty_phrases``) and a
  runner-up disagreement (the model named a different class as its second
  choice than its final label — the near-miss rescue signal, which is the
  correct answer's label in ~28% of misses).
- ``should_escalate`` — the absolute-threshold gate (production/streaming use).
- ``select_escalation_fraction`` — the rank-based alpha gate (eval use), which
  matches the simulation exactly: escalate the lowest-confidence ``alpha``
  fraction of the batch.
"""

from __future__ import annotations

from src.monte_carlo import uncertainty_phrases

# Penalty applied when the reasoning trace contains uncertainty phrasing.
UNCERTAINTY_PENALTY = 0.15
# Penalty applied when the final label differs from the stated runner-up.
RUNNER_UP_DISAGREEMENT_PENALTY = 0.20


def single_pass_confidence(
    self_report: float | None,
    predicted: str,
    runner_up: str,
    reasoning: str = "",
    source: str = "blend",
) -> float:
    """Per-inference confidence in ``[0, 1]`` from a single classification run.

    ``self_report`` is the model's ``<confidence>`` value normalized to
    ``[0, 1]`` (or ``None``). ``source`` selects the signal mix:

    - ``"self-report"`` — trust the model's stated confidence alone.
    - ``"heuristic"`` — ignore the self-report; derive confidence purely from
      uncertainty phrasing and runner-up disagreement (works with pre-v18.1
      prompts that do not emit a confidence tag).
    - ``"blend"`` (default) — self-report dominant, penalized by the two
      heuristic signals.
    """
    if source not in ("self-report", "heuristic", "blend"):
        raise ValueError(f"unknown confidence source {source!r}")

    if source == "self-report":
        confidence = self_report if self_report is not None else 0.5
    elif source == "heuristic":
        confidence = 0.5
    else:
        confidence = 0.6 * (self_report if self_report is not None else 0.5) + 0.2

    if uncertainty_phrases(reasoning or ""):
        confidence -= UNCERTAINTY_PENALTY
    runner_up = (runner_up or "").strip().lower()
    predicted = (predicted or "").strip().lower()
    if runner_up and predicted and runner_up != predicted:
        confidence -= RUNNER_UP_DISAGREEMENT_PENALTY

    return float(max(0.0, min(1.0, confidence)))


def should_escalate(confidence: float, threshold: float) -> bool:
    """True when ``confidence`` falls below the escalation threshold."""
    return confidence < threshold


def select_escalation_fraction(
    confidences: dict[str, float | None], alpha: float
) -> list[str]:
    """Rank-based alpha gate: return the filenames of the lowest-confidence tail.

    Rows with ``None`` confidence (e.g. failed base rows) sort below every
    scored row so they are escalated first. ``alpha`` is the fraction of the
    batch to escalate; ties are broken by filename for determinism.
    """
    if not confidences or alpha <= 0.0:
        return []
    ordered = sorted(
        confidences.items(),
        key=lambda kv: (kv[1] if kv[1] is not None else -1.0, kv[0]),
    )
    n = max(1, int(round(alpha * len(ordered))))
    return [filename for filename, _ in ordered[:n]]


def escalation_reason(
    confidence: float, runner_up: str, predicted: str, uncertainty: bool
) -> str:
    """Human-readable reason for the escalation decision (span metadata)."""
    if uncertainty:
        return "uncertainty phrasing in reasoning"
    runner_up = (runner_up or "").strip().lower()
    predicted = (predicted or "").strip().lower()
    if runner_up and predicted and runner_up != predicted:
        return f"runner-up conflict ({predicted} vs {runner_up})"
    return f"low confidence ({confidence:.2f})"
