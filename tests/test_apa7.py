"""Tests for src/apa7.py — APA 7 statistical formatting.

Covers: p-value normalization, CI bracketing, stat-symbol italics
(word-boundary-safe, idempotent), spacing fixes, and headline bold.
"""

import pytest

from src.apa7 import (
    bold_headline_results,
    fix_spacing,
    format_stats_apa,
    italicize_stat_symbols,
    normalize_cis,
    normalize_p_values,
)


# ---------------------------------------------------------------------------
# p-value normalization
# ---------------------------------------------------------------------------

class TestNormalizePValues:
    def test_zero_becomes_less_than(self):
        assert normalize_p_values("P = 0.000") == "*p* < .001"

    def test_small_p_strips_leading_zero(self):
        # p = 0.001 is reported as exact value per APA 7 (not "< .001")
        assert normalize_p_values("P = 0.001") == "*p* = .001"

    def test_moderate_p_strips_leading_zero(self):
        assert normalize_p_values("P = 0.94") == "*p* = .940"

    def test_lowercase_p_also_matches(self):
        assert normalize_p_values("p = 0.05") == "*p* = .050"

    def test_does_not_touch_already_italicized(self):
        # "*p* = .05" already has the right form; normalize should leave it
        # alone because it's wrapped in emphasis (handled at the segment level)
        text = "result (*p* = .05)"
        assert "*p* = .05" in normalize_p_values(text)

    def test_preserves_surrounding_text(self):
        out = normalize_p_values("the test showed P = 0.000 overall")
        assert out == "the test showed *p* < .001 overall"


# ---------------------------------------------------------------------------
# CI normalization
# ---------------------------------------------------------------------------

class TestNormalizeCIs:
    def test_basic_ci(self):
        assert normalize_cis("95% CI 328-402") == "95% *CI* [328, 402]"

    def test_dash_vs_hyphen(self):
        assert normalize_cis("95% CI 328–402") == "95% *CI* [328, 402]"

    def test_negative_bounds(self):
        assert normalize_cis("95% CI -0.5-0.3") == "95% *CI* [-0.5, 0.3]"

    def test_does_not_reformat_already_bracketed(self):
        text = "95% *CI* [328, 402]"
        # The regex only matches "N% CI X-Y" form, not "[X, Y]"
        assert normalize_cis(text) == text


# ---------------------------------------------------------------------------
# Stat-symbol italics
# ---------------------------------------------------------------------------

class TestItalicizeStatSymbols:
    def test_italicizes_ci(self):
        assert italicize_stat_symbols("the CI is wide") == "the *CI* is wide"

    def test_italicizes_pp(self):
        assert italicize_stat_symbols("+4.2pp gain") == "+4.2*pp* gain"

    def test_italicizes_k(self):
        assert italicize_stat_symbols("K = 5") == "*K* = 5"

    def test_does_not_rewrap_already_italicized(self):
        assert italicize_stat_symbols("*CI*") == "*CI*"

    def test_does_not_rewrap_already_bold(self):
        assert italicize_stat_symbols("**CI**") == "**CI**"

    def test_ignores_symbol_inside_backticks(self):
        text = "use the `CI` column"
        assert italicize_stat_symbols(text) == text

    def test_ignores_symbol_inside_link(self):
        text = "see [CI](../charts/ci.svg)"
        assert italicize_stat_symbols(text) == text

    def test_word_boundary_no_false_hit_in_prose(self):
        # "report" should not become "re*port*"
        text = "the report shows"
        assert italicize_stat_symbols(text) == text

    def test_multiple_symbols(self):
        out = italicize_stat_symbols("N=100, M=50, SD=10")
        assert "*N*" in out
        assert "*M*" in out
        assert "*SD*" in out


# ---------------------------------------------------------------------------
# Spacing fixes
# ---------------------------------------------------------------------------

class TestFixSpacing:
    def test_k_equals(self):
        assert fix_spacing("K=1") == "*K* = 1"

    def test_k_equals_with_space(self):
        assert fix_spacing("K = 5") == "*K* = 5"

    def test_pp_no_space(self):
        assert fix_spacing("+4.2pp") == "+4.2 *pp*"

    def test_pp_with_space_unchanged(self):
        assert fix_spacing("+4.2 pp") == "+4.2 *pp*"


# ---------------------------------------------------------------------------
# Combined formatter
# ---------------------------------------------------------------------------

class TestFormatStatsApa:
    def test_p_value_and_ci(self):
        text = "P = 0.000, 95% CI 328-402"
        out = format_stats_apa(text)
        assert "*p* < .001" in out
        assert "*CI*" in out
        assert "[328, 402]" in out

    def test_idempotent(self):
        text = "P = 0.94, K=5, 95% CI -0.5-0.3"
        first = format_stats_apa(text)
        second = format_stats_apa(first)
        assert first == second

    def test_preserves_prose(self):
        text = "The report shows a big improvement."
        assert format_stats_apa(text) == text

    def test_complex_sentence(self):
        text = "v0→v17 +28.4pp (P=0.000), 95% CI 328-402, K=1 baseline."
        out = format_stats_apa(text)
        assert "*p*" in out
        assert "*CI*" in out
        assert "*K*" in out
        assert "[328, 402]" in out
