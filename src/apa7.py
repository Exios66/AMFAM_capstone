"""APA 7 statistical formatting and headline-result emphasis.

Idempotent: running ``format_stats_apa`` twice produces the same output as
running it once. Already-italicized or already-bold tokens are left alone.

Formatting rules applied (in order):

1. **p-values** — ``P = 0.000`` → ``*p* < .001``; ``P = 0.94`` → ``*p* = .94``
   (strip leading zero, italicize *p*, use ``<`` when rounded to 3 dp zeros).
2. **Confidence intervals** — ``95% CI 328-402`` → ``95% *CI* [328, 402]``.
3. **Stat symbols** — italicize ``p``, ``N``, ``n``, ``M``, ``SD``, ``SE``,
   ``SEM``, ``Mdn``, ``CI``, ``K``, ``pp``, ``r``, ``t``, ``F``, ``df``, ``d``,
   ``z``, ``β``, ``χ²``, ``R²`` at word boundaries; skip already-emphasized
   text (``*…`` or ``**…``).
4. **Spacing fixes** — ``K=1`` → ``*K* = 1``; ``+4.2pp`` → ``+4.2 *pp*``.
5. **Headline bold** — bold specific result patterns (accuracy %, pp gains,
   per-image cost, failure rates) where they appear in a *headline-result*
   context (preceded by a colon, em-dash, or at the start of a bullet).

The formatter is designed for markdown/qmd source; it never rewrites inside
existing emphasis markers.
"""

from __future__ import annotations

import re

# ---------------------------------------------------------------------------
# p-value normalization
# ---------------------------------------------------------------------------

_PVAL_RE = re.compile(
    r"\b[pP]\s*=\s*(\d+\.\d{1,4})\b",
)


def _normalize_p_value(m: re.Match) -> str:
    val = m.group(1)
    fv = float(val)
    if fv == 0.0 or fv < 0.001:
        return "*p* < .001"
    # Strip leading zero per APA 7: 0.94 → .94
    if fv < 0.01:
        formatted = f"{fv:.3f}"[1:]  # "0.005" → ".005"
    else:
        formatted = f"{fv:.3f}"[1:]  # "0.940" → ".940"
    return f"*p* = {formatted}"


def normalize_p_values(text: str) -> str:
    """``P = 0.000`` → ``*p* < .001``; ``P = 0.94`` → ``*p* = .94``."""
    return _PVAL_RE.sub(_normalize_p_value, text)


# ---------------------------------------------------------------------------
# CI normalization
# ---------------------------------------------------------------------------

_CI_RE = re.compile(
    r"(\d+)%\s*CI\s+([-+]?\d+\.?\d*)\s*[-–]\s*([-+]?\d+\.?\d*)",
)


def _normalize_ci(m: re.Match) -> str:
    pct, lo, hi = m.group(1), m.group(2), m.group(3)
    return f"{pct}% *CI* [{lo}, {hi}]"


def normalize_cis(text: str) -> str:
    """``95% CI 328-402`` → ``95% *CI* [328, 402]``."""
    return _CI_RE.sub(_normalize_ci, text)


# ---------------------------------------------------------------------------
# Stat-symbol italics
# ---------------------------------------------------------------------------

# Symbols that should be italicized when they appear as standalone tokens
# (word-boundary matched). Order matters: longer symbols first to avoid
# partial matches (e.g. ``SEM`` before ``SE``).
STAT_SYMBOLS = [
    "SEM", "Mdn", "R²", "χ²", "SD", "SE", "CI", "pp",
    "df", "β",
    "p", "N", "n", "M", "K", "r", "t", "F", "d", "z",
]


def _build_italic_re() -> re.Pattern:
    """Build a pattern that matches any stat symbol at word boundaries.

    ``pp`` is special-cased: it may appear directly after a digit (e.g.
    ``+4.2pp``), so the left boundary uses a lookbehind for non-letter
    rather than ``\b``.
    """
    # pp: left boundary is "not a letter" (allows digit+pp), right is \b
    pp_pat = r"(?<![a-zA-Z])(pp)\b"
    # Other symbols: standard \b on both sides
    other_syms = [s for s in STAT_SYMBOLS if s != "pp"]
    other_pat = "|".join(re.escape(s) for s in other_syms)
    combined = rf"(?:(\*{{1,3}})?\b({other_pat})\b(\*{{1,3}})?)|(?:(\*{{1,3}})?{pp_pat}(\*{{1,3}})?)"
    return re.compile(combined)


_ITALIC_RE = _build_italic_re()


def _italicize_match(m: re.Match) -> str:
    lead, sym, trail = m.group(1), m.group(2), m.group(3)
    # Branch 2 (pp): groups 4, 5, 6
    if sym is None:
        lead, sym, trail = m.group(4), m.group(5), m.group(6)
    # If already wrapped in emphasis markers, leave alone
    if lead and trail and lead == trail:
        return m.group(0)
    return f"*{sym}*"


def italicize_stat_symbols(text: str) -> str:
    """Italicize standalone statistical symbols, respecting existing emphasis."""
    # Process text in segments split on existing markdown emphasis, so we don't
    # re-wrap ``*CI*`` → ``**CI**`` or mess up links.
    segments = re.split(r"(\*\*[^*]+\*\*|\*[^*]+\*|\[[^\]]+\]\([^)]+\)|`[^`]+`)", text)
    out = []
    for seg in segments:
        if re.match(r"^\*\*|^`|^\[", seg):
            out.append(seg)
        else:
            out.append(_ITALIC_RE.sub(_italicize_match, seg))
    return "".join(out)


# ---------------------------------------------------------------------------
# Spacing fixes
# ---------------------------------------------------------------------------

# K=1 → *K* = 1
_K_EQUALS_RE = re.compile(r"\bK\s*=\s*(\d+)")


def fix_spacing(text: str) -> str:
    """``K=1`` → ``*K* = 1``; ``+4.2pp`` → ``+4.2 *pp*``; ``+4.2 pp`` → ``+4.2 *pp*``."""
    text = _K_EQUALS_RE.sub(r"*K* = \1", text)
    # +N.N pp or +N.Npp → +N.N *pp*
    text = re.sub(r"([-+]?\d+\.?\d*)\s*pp\b", r"\1 *pp*", text)
    return text


# ---------------------------------------------------------------------------
# Headline bold (conservative: only in clear headline-result contexts)
# ---------------------------------------------------------------------------

# Patterns that indicate a headline result:
# - after a colon: ": 99.4%" or ": 0.114%"
# - after em-dash: "— +19.3 pp"
# - at start of a bullet line: "- 82.6%" or "- $0.0004"
# - standalone percentage/gain in a short context

_HEADLINE_PAT_RE = re.compile(
    r"(:\s*|\s*[—–]\s*|^\-\s*)"  # context prefix
    r"([-+]?\d+\.?\d*\s*(?:pp|%)|\$\d+\.?\d*)"  # value
    r"(\s|$)",  # trailing context
    flags=re.MULTILINE,
)


def _bold_headline(m: re.Match) -> str:
    prefix, value, suffix = m.group(1), m.group(2), m.group(3)
    # Don't double-bold
    if "**" in value:
        return m.group(0)
    return f"{prefix}**{value}**{suffix}"


def bold_headline_results(text: str) -> str:
    """Bold specific result values in headline-result contexts."""
    return _HEADLINE_PAT_RE.sub(_bold_headline, text)


# ---------------------------------------------------------------------------
# Combined entry point
# ---------------------------------------------------------------------------

def format_stats_apa(text: str) -> str:
    """Apply all APA 7 formatting passes to ``text``. Idempotent."""
    # Order matters: spacing fixes must run before italics so that
    # ``+4.2pp`` → ``+4.2 *pp*`` before ``pp`` gets wrapped to ``*pp*``.
    text = normalize_p_values(text)
    text = normalize_cis(text)
    text = fix_spacing(text)
    text = italicize_stat_symbols(text)
    return text
