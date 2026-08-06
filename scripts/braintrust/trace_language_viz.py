"""Trace-language visualization suite for classification reasoning traces.

Reads the joint Monte Carlo corpus (``reports/monte_carlo/corpus.jsonl``) and
produces three zero-spend diagnostics of the language of reasoning traces:

1. **Differential phrase nets** — a directed bigram graph of *failed* traces.
   Edges (bi-grams) are kept only when their prevalence in failed traces
   exceeds their prevalence in correct traces (a log-odds difference), so the
   graph shows the phrases that are *unique* to reasoning breakdowns, not the
   boilerplate shared with correct traces. Structural loops (``A -> B -> A``
   stuck phrases, repeated bi-grams) are detected and inventoried, and words
   that also appear in the prompt text (``src/prompts.py``) are tagged as
   prompt-leaked tokens — the model parroting its own instructions.

2. **Log-odds ratio with an uninformative Dirichlet prior** — Fightin' Words
   (Monroe, Colaresi & Quinn, 2008): each word is scored by
   ``log((y_fail + a)/(n_fail - y_fail + a)) - log((y_ok + a)/(n_ok - y_ok + a))``
   with a symmetric prior ``a`` on all counts. The top-30 words with the
   highest probability of appearing in a failed trace (and, mirrored, in a
   correct trace) are plotted as horizontal bars.

3. **Scattertext-style frequency scatter** — every word is mapped onto a
   log-log grid of frequency-per-million in correct (x-axis) vs failed
   (y-axis) traces. The top-left corner isolates the hallmark words of agent
   failures (hedge words, stuck phrases); the bottom-right corner the words
   driving successful classification.

Outputs (into ``--out-dir``, default ``reports/trace_language/``):

- ``phrase_net_differential.png`` — differential bigram graph of failed traces
- ``phrase_net_loops.md`` — structural-loop inventory + stuck-phrase stats
- ``logodds_dirichlet.png`` — top-30 fail-biased and top-30 success-biased words
- ``scattertext_style.png`` — log-log frequency scatter with corner labeling
- ``trace_language_report.md`` — methodology + full word tables

Usage:
    python scripts/braintrust/trace_language_viz.py
    python scripts/braintrust/trace_language_viz.py --confusion-pair letter->memo
    python scripts/braintrust/trace_language_viz.py --exclude-prompt-leaks --max-edges 250
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter, defaultdict
from math import log
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # noqa: E402
sys.path.insert(0, str(Path(__file__).resolve().parent))  # noqa: E402

import numpy as np
from matplotlib import pyplot as plt

from ale_stopword_visual import STOPWORDS, TOKEN_RE  # noqa: E402
from src.constants import DOCUMENT_CLASSES  # noqa: E402
from src.monte_carlo import load_corpus, save_figure, style_axis  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CORPUS = ROOT / "reports" / "monte_carlo" / "corpus.jsonl"
DEFAULT_OUT = ROOT / "reports" / "trace_language"

CLASSES = DOCUMENT_CLASSES
FAIL_COLOR = "#d64545"
OK_COLOR = "#1e9e5a"
LEAK_COLOR = "#d4a017"
GRID_COLOR = "#e8ecf3"

# Unfiltered phrase tokenization keeps short function words ("to", "as", "so")
# because they carry the structure of reasoning loops ("let's re-examine ->
# however -> let's re-examine"); the differential filter removes boilerplate.
PHRASE_TOKEN_RE = re.compile(r"[a-z][a-z0-9'_\-]{1,}")


# ---------------------------------------------------------------------------
# Data preparation
# ---------------------------------------------------------------------------

def build_trace_records(records: list[dict]) -> list[dict]:
    """Project corpus records into analysis rows (text, correctness, metadata)."""
    rows = []
    for r in records:
        reasoning = r.get("reasoning") or ""
        if not reasoning.strip():
            continue
        if r.get("status") not in ("completed", ""):
            continue
        expected = (r.get("expected") or "").strip().lower()
        predicted = (r.get("predicted") or "").strip().lower()
        rows.append({
            "text": reasoning,
            "correct": predicted == expected,
            "expected": expected,
            "predicted": predicted,
            "confusion_pair": f"{expected}->{predicted}",
            "prompt_version": r.get("prompt_version"),
            "model": r.get("model"),
            "dataset": r.get("dataset"),
            "attempts": r.get("attempts"),
            "filename": r.get("filename"),
        })
    return rows


def tokenize_phrases(text: str) -> list[str]:
    """Lowercased word tokens for phrase nets; keeps short function words."""
    if not text:
        return []
    return PHRASE_TOKEN_RE.findall(text.lower())


def tokenize_words(text: str) -> list[str]:
    """Content-word tokens for log-odds/scatter; drops generic stopwords."""
    if not text:
        return []
    return [t for t in TOKEN_RE.findall(text.lower()) if t not in STOPWORDS]


def load_prompt_vocab() -> frozenset[str]:
    """All phrase tokens appearing anywhere in the prompt texts."""
    from src.prompts import PROMPTS
    toks: set[str] = set()
    for text in PROMPTS.values():
        toks.update(tokenize_phrases(text))
    return frozenset(toks)


# ---------------------------------------------------------------------------
# Word-level statistics (log-odds + scatter)
# ---------------------------------------------------------------------------

def word_counts(records: list[dict]) -> tuple[Counter, Counter]:
    """Per-word token counts split by correctness of the trace."""
    fail_counts: Counter = Counter()
    ok_counts: Counter = Counter()
    for r in records:
        target = ok_counts if r["correct"] else fail_counts
        for tok in tokenize_words(r["text"]):
            target[tok] += 1
    return fail_counts, ok_counts


def log_odds_ratio(fail_counts: Counter, ok_counts: Counter,
                   alpha: float = 0.01, min_count: int = 5) -> list[dict]:
    """Fightin' Words log-odds with a symmetric Dirichlet prior.

    Returns words sorted ascending by ``z`` (most correct-biased first, most
    fail-biased last). ``alpha`` is the pseudo-count added to every cell; with
    an uninformative prior (``alpha -> 0``) words absent from one class get
    strong (negative or positive) scores without a division-by-zero.
    """
    n_fail = sum(fail_counts.values())
    n_ok = sum(ok_counts.values())
    words = set(fail_counts) | set(ok_counts)
    out = []
    for w in words:
        yf = fail_counts.get(w, 0)
        yo = ok_counts.get(w, 0)
        if max(yf, yo) < min_count:
            continue
        z = (log(yf + alpha) - log(n_fail - yf + alpha)
             - (log(yo + alpha) - log(n_ok - yo + alpha)))
        out.append({"word": w, "fail": yf, "ok": yo, "z": z})
    out.sort(key=lambda d: d["z"])
    return out


def scatter_frequencies(records: list[dict]) -> tuple[list[dict], int, int]:
    """Per-word frequency-per-million tokens in failed vs correct traces.

    Uses the unfiltered phrase tokenizer so the grid covers function words
    too (scattertext-style); class-size imbalance is normalized by
    per-million scaling.
    """
    fail_counts: Counter = Counter()
    ok_counts: Counter = Counter()
    for r in records:
        target = ok_counts if r["correct"] else fail_counts
        for tok in tokenize_phrases(r["text"]):
            target[tok] += 1
    n_fail = sum(fail_counts.values())
    n_ok = sum(ok_counts.values())
    words = set(fail_counts) | set(ok_counts)
    points = []
    for w in words:
        yf = fail_counts.get(w, 0)
        yo = ok_counts.get(w, 0)
        if max(yf, yo) < 2:
            continue
        points.append({
            "word": w,
            "fail": yf,
            "ok": yo,
            "freq_fail": yf / n_fail * 1e6 if n_fail else 0.0,
            "freq_ok": yo / n_ok * 1e6 if n_ok else 0.0,
        })
    return points, n_fail, n_ok


# ---------------------------------------------------------------------------
# Differential phrase nets
# ---------------------------------------------------------------------------

def differential_bigrams(records: list[dict], alpha: float = 0.01,
                         min_fail: int = 3, min_z: float = 0.5,
                         max_edges: int = 400,
                         exclude_prompt_leaks: bool = False) -> list[dict]:
    """Bi-grams whose prevalence in failed traces exceeds correct traces.

    Every bigram (word_i -> word_{i+1}) across all traces is counted per
    class; edges are kept when the fail-vs-ok log-odds difference clears
    ``min_z`` and the bigram appears in at least ``min_fail`` failed traces.
    The differential filter is what removes corporate boilerplate and
    prompt-leaked tokens that appear everywhere — only failure-biased edges
    survive. Returns up to ``max_edges`` edges sorted by z descending.
    """
    fail_edges: Counter = Counter()
    ok_edges: Counter = Counter()
    for r in records:
        toks = tokenize_phrases(r["text"])
        target = ok_edges if r["correct"] else fail_edges
        for a, b in zip(toks, toks[1:]):
            target[(a, b)] += 1
    n_fail = sum(fail_edges.values())
    n_ok = sum(ok_edges.values())
    prompt_vocab = load_prompt_vocab() if exclude_prompt_leaks else frozenset()
    scored = []
    for (a, b), yf in fail_edges.items():
        if yf < min_fail:
            continue
        if prompt_vocab and a in prompt_vocab and b in prompt_vocab:
            continue
        yo = ok_edges.get((a, b), 0)
        z = (log(yf + alpha) - log(n_fail - yf + alpha)
             - (log(yo + alpha) - log(n_ok - yo + alpha)))
        if z < min_z:
            continue
        scored.append({"a": a, "b": b, "fail": yf, "ok": yo, "z": z})
    scored.sort(key=lambda d: d["z"], reverse=True)
    return scored[:max_edges]


def differential_bigrams_two_sided(records: list[dict], alpha: float = 0.01,
                                   min_count: int = 3, min_z: float = 0.5,
                                   max_edges: int = 300,
                                   exclude_prompt_leaks: bool = False) -> list[dict]:
    """Differential bi-grams in BOTH directions — failure- AND correct-biased.

    Every bigram is scored by its fail-vs-correct log-odds difference with the
    symmetric Dirichlet prior (Fightin' Words). Edges clearing ``+min_z`` are
    kept as **failure-biased** (characteristic of reasoning breakdowns); edges
    clearing ``-min_z`` are kept as **correct-biased** (characteristic of
    successful classification). Each returned edge carries a ``bias`` field
    (``"fail"`` or ``"ok"``) and appears in at least ``min_count`` traces of
    its dominant class. Both sides are capped at ``max_edges`` each so the
    interactive widget shows the two sides in balance; the list is sorted by
    absolute log-odds descending.
    """
    fail_edges: Counter = Counter()
    ok_edges: Counter = Counter()
    for r in records:
        toks = tokenize_phrases(r["text"])
        target = ok_edges if r["correct"] else fail_edges
        for a, b in zip(toks, toks[1:]):
            target[(a, b)] += 1
    n_fail = sum(fail_edges.values())
    n_ok = sum(ok_edges.values())
    prompt_vocab = load_prompt_vocab() if exclude_prompt_leaks else frozenset()
    scored = []
    for (a, b) in set(fail_edges) | set(ok_edges):
        if prompt_vocab and a in prompt_vocab and b in prompt_vocab:
            continue
        yf = fail_edges.get((a, b), 0)
        yo = ok_edges.get((a, b), 0)
        if max(yf, yo) < min_count:
            continue
        z = (log(yf + alpha) - log(n_fail - yf + alpha)
             - (log(yo + alpha) - log(n_ok - yo + alpha)))
        if z >= min_z:
            scored.append({"a": a, "b": b, "fail": yf, "ok": yo, "z": z, "bias": "fail"})
        elif z <= -min_z:
            scored.append({"a": a, "b": b, "fail": yf, "ok": yo, "z": z, "bias": "ok"})
    scored.sort(key=lambda d: abs(d["z"]), reverse=True)
    fail_side = [e for e in scored if e["bias"] == "fail"][:max_edges]
    ok_side = [e for e in scored if e["bias"] == "ok"][:max_edges]
    return fail_side + ok_side


def find_cycles(edges: list[dict], max_len: int = 6) -> list[list[str]]:
    """Bounded directed-cycle search over the edge list.

    Returns simple cycles of length 2..``max_len``, deduplicated across
    rotations and reversals are NOT merged (direction matters). A 2-cycle
    ``A -> B -> A`` is a classic stuck-phrase loop in reasoning breakdowns.
    """
    adj: dict[str, list[str]] = defaultdict(list)
    for e in edges:
        adj[e["a"]].append(e["b"])
    raw: set[tuple[str, ...]] = set()

    def dfs(node: str, path: list[str], visited: set[str]) -> None:
        if len(path) > max_len:
            return
        for nxt in adj.get(node, ()):
            if nxt == path[0] and len(path) >= 1:
                raw.add(tuple(path))
            elif nxt not in visited and len(path) < max_len:
                dfs(nxt, path + [nxt], visited | {nxt})

    for start in adj:
        dfs(start, [start], {start})

    def canon(cycle: tuple[str, ...]) -> tuple[str, ...]:
        return min(cycle[i:] + cycle[:i] for i in range(len(cycle)))

    return [list(c) for c in sorted({canon(c) for c in raw},
                                    key=lambda c: (len(c), c))]


def stuck_phrase_stats(records: list[dict]) -> dict:
    """Per-trace stuck-phrase rates: back-to-back repetition of a phrase.

    A trace is marked as looping when its token stream repeats a bi-gram
    back-to-back (``A B A B``) or a tri-gram back-to-back (``A B C A B C``) —
    the model re-running the same phrase instead of progressing. Plain
    ``A -> B -> A`` trigrams and repeated bi-grams anywhere in the trace
    saturate (~all v11.8 traces re-quote evidence across the check cascade),
    so only *consecutive* duplication is counted; it runs ~2x higher in
    failed traces.
    """
    def has_loop(toks: list[str]) -> bool:
        if any(toks[i:i + 2] == toks[i + 2:i + 4] for i in range(len(toks) - 3)):
            return True
        if any(toks[i:i + 3] == toks[i + 3:i + 6] for i in range(len(toks) - 5)):
            return True
        return False

    failed = [r for r in records if not r["correct"]]
    ok = [r for r in records if r["correct"]]
    f_loops = sum(1 for r in failed if has_loop(tokenize_phrases(r["text"])))
    o_loops = sum(1 for r in ok if has_loop(tokenize_phrases(r["text"])))
    return {
        "failed_n": len(failed),
        "ok_n": len(ok),
        "failed_loops": f_loops,
        "ok_loops": o_loops,
        "failed_rate": f_loops / len(failed) if failed else 0.0,
        "ok_rate": o_loops / len(ok) if ok else 0.0,
    }


def _example_trace(records: list[dict], cycle: list[str]) -> str:
    """First failed-trace excerpt whose token stream runs the cycle consecutively."""
    seq = [t.lower() for t in cycle]
    for r in records:
        if r["correct"]:
            continue
        toks = tokenize_phrases(r["text"])
        for i in range(len(toks) - len(seq) + 1):
            if toks[i:i + len(seq)] == seq:
                return r["text"][:400].replace("\n", " ")
    return ""


def _node_stats(edges: list[dict]) -> dict[str, dict]:
    """Aggregate per-node frequency and fail share from the edge list."""
    stats: dict[str, dict] = defaultdict(lambda: {"fail": 0, "ok": 0, "z": 0.0})
    for e in edges:
        for key in ("a", "b"):
            node = e[key]
            stats[node]["fail"] += e["fail"]
            stats[node]["ok"] += e["ok"]
            stats[node]["z"] += e["z"]
    return stats


# ---------------------------------------------------------------------------
# Plotting
# ---------------------------------------------------------------------------

def plot_phrase_net(edges: list[dict], prompt_vocab: frozenset[str],
                    out_path: Path, scope: str, records: list[dict]) -> None:
    """Directed differential bigram graph with cycle edges highlighted."""
    import networkx as nx

    G = nx.DiGraph()
    for e in edges:
        G.add_edge(e["a"], e["b"], weight=e["z"])
    if G.number_of_nodes() == 0:
        print("  no differential edges to plot")
        return

    stats = _node_stats(edges)
    pos = nx.spring_layout(G, seed=42, k=0.5)
    zs = [e["z"] for e in edges]
    zmin, zmax = min(zs), max(zs)

    fig, ax = plt.subplots(figsize=(16, 12))
    cycles = find_cycles(edges)
    cycle_edges = set()
    for c in cycles:
        for i in range(len(c)):
            cycle_edges.add((c[i], c[(i + 1) % len(c)]))

    node_colors = []
    node_sizes = []
    for node in G.nodes():
        s = stats[node]
        share = s["fail"] / (s["fail"] + s["ok"]) if s["fail"] + s["ok"] else 0.5
        node_colors.append(_interp_color(share))
        node_sizes.append(240 + 90 * np.log1p(s["fail"]))

    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=node_sizes,
                           node_color=node_colors, edgecolors="#333333",
                           linewidths=0.8)
    plain = [(a, b) for a, b in G.edges() if (a, b) not in cycle_edges]
    looped = [(a, b) for a, b in G.edges() if (a, b) in cycle_edges]
    for edge_list, color, alpha in ((plain, "#888888", 0.45), (looped, FAIL_COLOR, 1.0)):
        if not edge_list:
            continue
        widths = [0.8 + 4.5 * (G[a][b]["weight"] - zmin) / (zmax - zmin)
                  for a, b in edge_list]
        nx.draw_networkx_edges(G, pos, ax=ax, edgelist=edge_list,
                               width=widths, edge_color=color, alpha=alpha,
                               arrowstyle="-|>", arrowsize=14,
                               connectionstyle="arc3,rad=0.12")

    leak_nodes = [n for n in G.nodes() if n in prompt_vocab]
    if leak_nodes:
        nx.draw_networkx_nodes(G, pos, ax=ax, nodelist=leak_nodes,
                               node_size=[node_sizes[list(G.nodes()).index(n)]
                                          for n in leak_nodes],
                               node_color="none", edgecolors=LEAK_COLOR,
                               linewidths=2.0, node_shape="D")

    labels = {n: n for n in G.nodes()}
    nx.draw_networkx_labels(G, pos, labels=labels, ax=ax, font_size=8,
                            font_color="#1b2a4a")
    ax.set_title(
        f"Differential Phrase Net — {scope}\n"
        f"bi-grams over-represented in failed traces ({G.number_of_nodes()} words, "
        f"{G.number_of_edges()} edges, red = structural loops)",
        fontsize=14, fontweight="bold",
    )
    ax.axis("off")
    fig.tight_layout()
    save_figure(fig, out_path)


def _interp_color(share: float) -> str:
    """Red-heavy for fail-dominated nodes, green-heavy for ok-dominated."""
    t = float(np.clip(share, 0.0, 1.0))
    lo = np.array([0.12, 0.62, 0.35])
    hi = np.array([0.84, 0.27, 0.27])
    rgb = lo * (1 - t) + hi * t
    return tuple(rgb)


def plot_logodds(words: list[dict], out_path: Path, scope: str,
                 top_n: int = 30, alpha: float = 0.01) -> None:
    """Two horizontal bar panels: top fail-biased and top success-biased words."""
    fail_biased = [w for w in words if w["z"] > 0][-top_n:][::-1]
    ok_biased = [w for w in words if w["z"] <= 0][:top_n][::-1]
    fig, (ax_f, ax_o) = plt.subplots(1, 2, figsize=(15, 0.5 * top_n + 3))

    def _panel(ax, items, color, title):
        labels = [w["word"] for w in items]
        vals = [w["z"] for w in items]
        y = np.arange(len(items))
        ax.barh(y, vals, color=color, height=0.72)
        for yi, w in zip(y, items):
            ax.text(w["z"], yi + 0.25, f"fail {w['fail']} · ok {w['ok']}",
                    va="center", fontsize=7.5, color="#444444")
        ax.set_yticks(y)
        ax.set_yticklabels(labels, fontsize=9)
        ax.set_xlabel("log-odds z", fontsize=11)
        ax.set_title(title, fontsize=12, fontweight="bold")
        ax.grid(alpha=0.3, axis="x")
        ax.axvline(0.0, color="gray", lw=0.8)

    _panel(ax_f, fail_biased, FAIL_COLOR,
           f"Most failed-trace words (n = {len(fail_biased)})")
    _panel(ax_o, ok_biased, OK_COLOR,
           f"Most correct-trace words (n = {len(ok_biased)})")
    fig.suptitle(
        f"Log-Odds Ratio with Uninformative Dirichlet Prior — {scope}\n"
        f"z = log((f+a)/(F-f+a)) - log((o+a)/(O-o+a)), a = {alpha}",
        fontsize=13, fontweight="bold",
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    save_figure(fig, out_path)


def plot_scattertext(points: list[dict], words: list[dict], out_path: Path,
                     scope: str) -> None:
    """Log-log scatter of per-million word frequency in correct vs failed traces."""
    z_by_word = {w["word"]: w["z"] for w in words}
    fig, ax = plt.subplots(figsize=(11, 10))
    xs = [max(p["freq_ok"], 0.5) for p in points]
    ys = [max(p["freq_fail"], 0.5) for p in points]
    sizes = [18 + 8 * np.log1p(p["fail"] + p["ok"]) for p in points]
    zs = [z_by_word.get(p["word"], 0.0) for p in points]
    colors = [FAIL_COLOR if z > 0.5 else OK_COLOR if z < -0.5 else "#b9c4d6"
              for z in zs]

    ax.scatter(xs, ys, s=sizes, c=colors, alpha=0.55, edgecolors="none")
    lim = [0.3, 10 ** 4]
    ax.plot(lim, lim, color="gray", lw=1, ls="--", alpha=0.7)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(*lim)
    ax.set_ylim(*lim)
    ax.set_xlabel("Frequency per million tokens — CORRECT traces", fontsize=12)
    ax.set_ylabel("Frequency per million tokens — FAILED traces", fontsize=12)
    ax.set_title(
        f"Scattertext-style Word Geography — {scope}\n"
        "top-left = failure hallmarks · bottom-right = success drivers",
        fontsize=13, fontweight="bold",
    )
    ax.grid(alpha=0.3)

    ranked = sorted(points, key=lambda p: abs(z_by_word.get(p["word"], 0.0)),
                    reverse=True)[:24]
    for p in ranked:
        z = z_by_word.get(p["word"], 0.0)
        dx, dy = 4, 4
        if p["freq_fail"] > p["freq_ok"]:
            dx, dy = -2, 4
        ax.annotate(p["word"], (max(p["freq_ok"], 0.5), max(p["freq_fail"], 0.5)),
                    fontsize=8.5, xytext=(dx, dy), textcoords="offset points",
                    color="#1b2a4a", alpha=0.85,
                    bbox=dict(boxstyle="round,pad=0.15", fc="white", ec="none", alpha=0.55))
    fig.tight_layout()
    save_figure(fig, out_path)


# ---------------------------------------------------------------------------
# Reports
# ---------------------------------------------------------------------------

def write_loop_report(cycles: list[list[str]], records: list[dict],
                      edges: list[dict], stats: dict, out_path: Path,
                      suffix: str = "") -> None:
    """Structural-loop inventory: every detected cycle with an example trace."""
    edge_by_pair = {(e["a"], e["b"]): e for e in edges}
    md = [
        "# Structural Loops in Failed Reasoning Traces",
        "",
        f"- **Corpus rows (reasoning-covered)**: {len(records)}",
        f"- **Differential bigram edges**: {len(edges)}",
        f"- **Cycles found (length ≤ 6)**: {len(cycles)}",
        "",
        "## Per-trace stuck-phrase rates",
        "",
        "A trace is marked as looping when its token stream repeats a bi-gram "
        "back-to-back (`A B A B`) or a tri-gram back-to-back (`A B C A B C`) — "
        "the model re-running the same phrase instead of progressing. Plain "
        "`A -> B -> A` trigrams saturate (every v11.8 trace re-quotes evidence "
        "across the check cascade), so only consecutive duplication is counted.",
        "",
        "| Group | Traces | Looping traces | Rate |",
        "|---|---:|---:|---:|",
        f"| Failed | {stats['failed_n']} | {stats['failed_loops']} | {stats['failed_rate']:.1%} |",
        f"| Correct | {stats['ok_n']} | {stats['ok_loops']} | {stats['ok_rate']:.1%} |",
        "",
    ]
    if not cycles:
        md += ["## Cycles", "", "No cycles found in the differential graph.", ""]
        out_path.write_text("\n".join(md), encoding="utf-8")
        print(f"Loop report saved: {out_path}")
        return

    md += ["## Cycles in the differential bigram graph", "",
           "| # | Cycle | Length | Edge weight (fail n / ok n) | Example trace excerpt |",
           "|---|---:|---:|---|---|"]
    for i, c in enumerate(cycles, start=1):
        weights = " → ".join(
            f"{a}→{b} ({edge_by_pair[(a, b)]['fail']}/{edge_by_pair[(a, b)]['ok']})"
            for a, b in zip(c, c[1:] + c[:1])
        )
        excerpt = _example_trace(records, c)
        snippet = excerpt[:220] + ("..." if len(excerpt) > 220 else "")
        md.append(f"| {i} | `{' → '.join(c)}` | {len(c)} | {weights} | `{snippet}` |")
    md += [
        "",
        "Cycle edges are highlighted in red on "
        f"`phrase_net_differential{suffix}.png`. Rotational duplicates are "
        "merged; direction is preserved (a reversed cycle is a different loop).",
        "",
    ]
    out_path.write_text("\n".join(md), encoding="utf-8")
    print(f"Loop report saved: {out_path}")


def write_report(records: list[dict], words: list[dict], edges: list[dict],
                 cycles: list[list[str]], stats: dict, prompt_vocab: frozenset[str],
                 alpha: float, scope: str, out_dir: Path, top_n: int,
                 suffix: str = "") -> None:
    failed = [r for r in records if not r["correct"]]
    ok = [r for r in records if r["correct"]]
    leaked_edges = [e for e in edges if e["a"] in prompt_vocab and e["b"] in prompt_vocab]
    md = [
        "# Trace-Language Analysis of Reasoning Traces",
        "",
        f"- **Corpus rows (reasoning-covered)**: {len(records)} "
        f"({len(failed)} failed, {len(ok)} correct)",
        f"- **Scope**: {scope}",
        f"- **Word tokenization**: content words (stopwords removed); "
        f"phrase tokenization keeps function words for loop detection",
        f"- **Dirichlet prior** a = {alpha} (symmetric pseudo-count)",
        "",
        "## Differential Phrase Nets",
        "",
        f"![Differential phrase net](phrase_net_differential{suffix}.png)",
        "",
        "Directed bi-gram graph of the reasoning traces, restricted to edges "
        "whose prevalence in **failed** traces exceeds their prevalence in "
        "**correct** traces (log-odds difference ≥ threshold, ≥ min failed "
        "occurrences). The differential filter removes the corporate "
        "boilerplate and prompt-leaked tokens shared with correct traces, "
        "leaving the phrases characteristic of reasoning breakdowns. "
        "Diamond-outlined nodes are **prompt-leaked** tokens — words the model "
        "parrots from the prompt text itself. Red edges are structural loops.",
        "",
        "### Top failure-biased bi-grams",
        "",
        "| Bi-gram | Failed n | Correct n | z |",
        "|---|---:|---:|---:|",
    ]
    for e in edges[:25]:
        md.append(f"| `{e['a']} → {e['b']}` | {e['fail']} | {e['ok']} | {e['z']:.2f} |")
    md += [
        "",
        f"**{len(leaked_edges)} of {len(edges)} differential edges are "
        "prompt-leaked** (both words appear in the prompt text) — the model "
        "failing while reciting its own instructions.",
        "",
        "### Structural loops",
        "",
        f"{len(cycles)} cycles detected (length ≤ 6). Full inventory with "
        "example traces: "
        f"[phrase_net_loops{suffix}.md](../../reports/trace_language/"
        f"phrase_net_loops{suffix}.md).",
        "",
        "| Cycle | Length |",
        "|---|---:|",
    ]
    for c in cycles[:15]:
        md.append(f"| `{' → '.join(c)}` | {len(c)} |")
    md += [
        "",
        "### Stuck phrases per trace",
        "",
        "Back-to-back phrase repetition (`A B A B` or `A B C A B C`):",
        "",
        "| Group | Traces | Looping traces | Rate |",
        "|---|---:|---:|---:|",
        f"| Failed | {stats['failed_n']} | {stats['failed_loops']} | {stats['failed_rate']:.1%} |",
        f"| Correct | {stats['ok_n']} | {stats['ok_loops']} | {stats['ok_rate']:.1%} |",
        "",
        "## Log-Odds Ratio (Uninformative Dirichlet Prior)",
        "",
        f"![Log-odds bar chart](logodds_dirichlet{suffix}.png)",
        "",
        "Fightin' Words (Monroe, Colaresi & Quinn, 2008): "
        "`z = log((y_f + a)/(n_f - y_f + a)) - log((y_o + a)/(n_o - y_o + a))` "
        "with the symmetric prior a on every count. Positive z = word is more "
        "likely to appear in a failed trace; negative z = more likely in a "
        "correct trace. Words shared across both classes (boilerplate, "
        "prompt-leaked labels) sit near z = 0 and drop out of the extremes.",
        "",
        "### Top 30 words most likely in FAILED traces",
        "",
        "| word | failed n | correct n | z |",
        "|---|---:|---:|---:|",
    ]
    fail_biased = [w for w in words if w["z"] > 0][-top_n:][::-1]
    for w in fail_biased:
        md.append(f"| {w['word']} | {w['fail']} | {w['ok']} | {w['z']:.2f} |")
    md += [
        "",
        "### Top 30 words most likely in CORRECT traces",
        "",
        "| word | failed n | correct n | z |",
        "|---|---:|---:|---:|",
    ]
    ok_biased = [w for w in words if w["z"] <= 0][:top_n][::-1]
    for w in ok_biased:
        md.append(f"| {w['word']} | {w['fail']} | {w['ok']} | {w['z']:.2f} |")
    md += [
        "",
        "## Scattertext-style Frequency Scatter",
        "",
        f"![Scattertext-style scatter](scattertext_style{suffix}.png)",
        "",
        "Every word on a log-log grid of frequency-per-million-tokens in "
        "correct (x) vs failed (y) traces. The **top-left corner** isolates "
        "hallmark failure language; the **bottom-right corner** the words "
        "driving successful classification. Words near the diagonal are "
        "class-neutral (both the prompt template and document text are shared "
        "across both classes).",
        "",
    ]
    path = out_dir / f"trace_language_report{suffix}.md"
    path.write_text("\n".join(md), encoding="utf-8")
    print(f"Report saved: {path}")


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS,
                        help=f"Corpus JSONL (default: {DEFAULT_CORPUS})")
    parser.add_argument("--out-dir", type=Path, default=DEFAULT_OUT,
                        help=f"Output dir (default: {DEFAULT_OUT})")
    parser.add_argument("--alpha", type=float, default=0.01,
                        help="Symmetric Dirichlet prior pseudo-count")
    parser.add_argument("--top-n", type=int, default=30,
                        help="Words per tail of the log-odds chart")
    parser.add_argument("--min-count", type=int, default=5,
                        help="Min occurrences in one class for log-odds words")
    parser.add_argument("--min-fail", type=int, default=3,
                        help="Min failed-trace occurrences for a bigram edge")
    parser.add_argument("--min-z", type=float, default=0.5,
                        help="Min fail-vs-ok log-odds for a bigram edge")
    parser.add_argument("--max-edges", type=int, default=400,
                        help="Max differential edges in the phrase net")
    parser.add_argument("--max-cycle-len", type=int, default=6,
                        help="Max cycle length to detect")
    parser.add_argument("--exclude-prompt-leaks", action="store_true",
                        help="Drop bigrams whose words all appear in the prompt text")
    parser.add_argument("--confusion-pair", default=None,
                        help="Restrict to one confusion pair, e.g. letter->memo")
    parser.add_argument("--prompt-version", default=None,
                        help="Restrict to one prompt version, e.g. v11.8")
    parser.add_argument("--class", dest="expected_class", default=None,
                        help="Restrict to one expected (ground-truth) class")
    parser.add_argument("--scope", default="all",
                        help="Label for output filenames (default: all)")
    args = parser.parse_args()

    records = load_corpus(args.corpus)
    rows = build_trace_records(records)
    if args.confusion_pair:
        rows = [r for r in rows if r["confusion_pair"] == args.confusion_pair]
    if args.prompt_version:
        rows = [r for r in rows if r["prompt_version"] == args.prompt_version]
    if args.expected_class:
        rows = [r for r in rows if r["expected"] == args.expected_class]
    if not rows:
        print("No rows after filtering — nothing to visualize.")
        return
    print(f"Loaded {len(records)} corpus records; {len(rows)} traces with reasoning"
          + (f" (scope: {args.scope})" if args.scope != "all" else ""))

    args.out_dir.mkdir(parents=True, exist_ok=True)
    scope = args.scope
    suffix = "" if scope == "all" else f"_{scope}"
    fail_counts, ok_counts = word_counts(rows)
    words = log_odds_ratio(fail_counts, ok_counts, alpha=args.alpha,
                           min_count=args.min_count)
    print(f"Log-odds ranked {len(words)} words "
          f"(prior a={args.alpha}, min {args.min_count} occurrences)")
    plot_logodds(words, args.out_dir / f"logodds_dirichlet{suffix}.png", scope,
                 top_n=args.top_n, alpha=args.alpha)

    points, n_fail, n_ok = scatter_frequencies(rows)
    print(f"Scattertext grid: {len(points)} words "
          f"({n_fail} failed tokens, {n_ok} correct tokens)")
    plot_scattertext(points, words,
                     args.out_dir / f"scattertext_style{suffix}.png", scope)

    prompt_vocab = load_prompt_vocab()
    edges = differential_bigrams(
        rows, alpha=args.alpha, min_fail=args.min_fail, min_z=args.min_z,
        max_edges=args.max_edges, exclude_prompt_leaks=args.exclude_prompt_leaks,
    )
    print(f"Differential phrase net: {len(edges)} failure-biased bi-grams")
    if edges:
        plot_phrase_net(edges, prompt_vocab,
                        args.out_dir / f"phrase_net_differential{suffix}.png",
                        scope, rows)
    else:
        print("  no differential edges (loosen --min-z/--min-fail)")

    cycles = find_cycles(edges, max_len=args.max_cycle_len)
    stats = stuck_phrase_stats(rows)
    print(f"Detected {len(cycles)} structural loops; "
          f"stuck-phrase rate: failed {stats['failed_rate']:.1%} vs "
          f"correct {stats['ok_rate']:.1%}")
    write_loop_report(cycles, rows, edges, stats,
                      args.out_dir / f"phrase_net_loops{suffix}.md", suffix)
    write_report(rows, words, edges, cycles, stats, prompt_vocab, args.alpha,
                 scope, args.out_dir, args.top_n, suffix)
    print("Done.")


if __name__ == "__main__":
    main()
