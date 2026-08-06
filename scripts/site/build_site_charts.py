"""Generate the website's charts (SVG) from committed markdown tables.

Fully offline and deterministic: every chart is rendered from tables that are
already committed to the repository (confusion-matrix grids, per-class accuracy
tables, cost projections, and curated accuracy-progress data). No API keys, no
network access, no model spend.

Outputs SVG files into ``website/charts/`` so they are tracked by git (the repo
gitignores ``*.png`` but not ``*.svg``).
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[2]
CHARTS_DIR = ROOT / "website" / "charts"
MC_DIR = ROOT / "reports" / "monte_carlo"

# Import ALE estimator from the braintrust script (approach A: import via sys.path)
sys.path.insert(0, str(ROOT / "scripts" / "braintrust"))
from ale_stopword_visual import (  # noqa: E402
    accumulated_local_effects,
    build_rows as _build_rows,
)
from trace_language_viz import (  # noqa: E402
    build_trace_records,
    differential_bigrams,
    find_cycles,
    load_prompt_vocab,
    log_odds_ratio,
    scatter_frequencies,
    word_counts,
)

sys.path.insert(0, str(ROOT))
from src.constants import DOCUMENT_CLASSES  # noqa: E402
from src.monte_carlo import load_corpus  # noqa: E402

N_CLASSES = len(DOCUMENT_CLASSES)

# ---------------------------------------------------------------------------
# Styling
# ---------------------------------------------------------------------------

BG = "#ffffff"
NAVY = "#1b2a4a"
ACCENT = "#2d6cdf"
ACCENT_LIGHT = "#dbe6fb"
GOOD = "#1e9e5a"
BAD = "#d64545"
GRID = "#e8ecf3"

plt.rcParams.update(
    {
        "font.family": "DejaVu Sans",
        "font.size": 10,
        "axes.facecolor": "white",
        "figure.facecolor": "white",
        "svg.fonttype": "none",
        "axes.edgecolor": GRID,
        "axes.grid": True,
        "grid.color": GRID,
        "grid.linewidth": 0.8,
    }
)


def _save(fig, name: str) -> Path:
    fig.tight_layout()
    out = CHARTS_DIR / name
    fig.savefig(out, format="svg", bbox_inches="tight")
    plt.close(fig)
    print(f"  chart: {out.name}")
    return out


def _norm(label: str) -> str:
    label = label.strip().strip("`").strip("*").strip()
    return label


# ---------------------------------------------------------------------------
# Confusion matrices
# ---------------------------------------------------------------------------

ROW_RE = re.compile(r"^\|\s*`?([a-zA-Z_]+)`?\s*\|(.*)\|")


def parse_confusion_matrix(md_text: str) -> dict:
    """Parse a ``## Raw Counts`` grid into an 16x16 matrix + per-class accuracy."""
    in_counts = False
    rows = []
    row_labels = []
    acc = {}
    for line in md_text.splitlines():
        if line.strip().startswith("## Raw Counts"):
            in_counts = True
            continue
        if in_counts:
            if line.strip().startswith("| Expected"):
                continue
            if line.strip().startswith("|---"):
                continue
            if line.strip().startswith("## "):
                break
            m = ROW_RE.match(line)
            if not m:
                continue
            label = _norm(m.group(1))
            if not label or "invalid" in label.lower():
                continue
            cells = [c.strip() for c in m.group(2).split("|")]
            cells = [c for c in cells if c != ""]
            values = []
            for cell in cells:
                if cell in (".", "—", "-"):
                    values.append(0)
                else:
                    values.append(int(re.sub(r"[^\d]", "", cell)))
            if len(values) >= N_CLASSES:
                rows.append(values[:N_CLASSES])
                row_labels.append(label)
                acc[label] = values[-1] if values else 0
    matrix = np.array(rows, dtype=float) if rows else np.zeros((0, 0))
    return {"matrix": matrix, "labels": row_labels, "acc": acc}


def chart_confusion_matrix(md_path: Path, out_name: str) -> None:
    data = parse_confusion_matrix(md_path.read_text(encoding="utf-8"))
    matrix = data["matrix"]
    labels = data["labels"]
    if matrix.size == 0 or matrix.shape[0] != matrix.shape[1]:
        print(f"  skip (no parseable grid): {md_path.name}")
        return
    n = matrix.shape[0]
    diag = np.diag(matrix).copy()
    max_v = matrix.max() if matrix.max() > 0 else 1
    cmap = plt.matplotlib.colors.LinearSegmentedColormap.from_list(
        "amfam", ["#ffffff", "#c7d8fb", ACCENT]
    )
    fig, ax = plt.subplots(figsize=(10.5, 8.8))
    im = ax.imshow(matrix, cmap=cmap, vmin=0, vmax=max_v, aspect="equal")
    for i in range(n):
        for j in range(n):
            v = matrix[i, j]
            if v == 0:
                continue
            on_diag = i == j
            color = "white" if v > max_v * 0.62 else ("#10316b" if on_diag else "#33415c")
            ax.text(
                j, i, f"{int(v)}", ha="center", va="center",
                fontsize=8.5, color=color, fontweight="bold" if on_diag else "normal",
            )
    ax.set_xticks(range(n))
    ax.set_yticks(range(n))
    ax.set_xticklabels(labels[:n], rotation=45, ha="right", fontsize=8.5)
    ax.set_yticklabels(labels[:n], fontsize=8.5)
    ax.set_xlabel("Predicted")
    ax.set_ylabel("Expected")
    ax.set_title("Confusion matrix (correct class counts on the diagonal)", fontsize=12, pad=12)
    fig.colorbar(im, ax=ax, fraction=0.035, pad=0.02)
    _save(fig, out_name)


# ---------------------------------------------------------------------------
# Per-class accuracy
# ---------------------------------------------------------------------------

PCA_HEADER_RE = re.compile(r"^\|?\s*Class\s*\|")


def parse_per_class_accuracy(md_text: str) -> dict[str, tuple[int, int]]:
    out = {}
    for line in md_text.splitlines():
        if not line.strip().startswith("|"):
            continue
        if "Per-Class Accuracy" in line:
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        cells = [_norm(c) for c in cells]
        if len(cells) >= 2 and cells[0] and PCA_HEADER_RE.match(cells[0]):
            continue
        if len(cells) >= 4 and cells[0] in DOCUMENT_CLASSES:
            try:
                correct = int(cells[1])
                total = int(cells[2])
            except ValueError:
                continue
            out[cells[0]] = (correct, total)
        elif len(cells) >= 2 and cells[0] in DOCUMENT_CLASSES:
            m = re.search(r"(\d+)%", cells[1])
            if m:
                out[cells[0]] = (int(m.group(1)), 100)
    return out


def chart_per_class(md_path: Path, out_name: str, title: str) -> None:
    pca = parse_per_class_accuracy(md_path.read_text(encoding="utf-8"))
    if not pca:
        print(f"  skip (no per-class table): {md_path.name}")
        return
    classes = DOCUMENT_CLASSES
    accs = []
    for c in classes:
        if c in pca:
            correct, total = pca[c]
            accs.append((c, correct, total, correct / total if total else 0))
    if not accs:
        return
    accs.sort(key=lambda t: t[3])
    names = [t[0] for t in accs]
    vals = [t[3] * 100 for t in accs]
    details = [f"{t[1]}/{t[2]}" for t in accs]
    colors = [GOOD if v >= 80 else ("#e8a13c" if v >= 60 else BAD) for v in vals]
    fig, ax = plt.subplots(figsize=(9.5, 6.6))
    y = np.arange(len(names))
    ax.barh(y, vals, color=colors, height=0.72, edgecolor="none")
    for yi, v, d in zip(y, vals, details):
        ax.text(v + 1, yi, f"{v:.0f}% ({d})", va="center", fontsize=8.5, color="#33415c")
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=9)
    ax.set_xlim(0, 108)
    ax.set_xlabel("Exact-match accuracy (%)")
    ax.axvline(80, color=GRID, lw=1, ls="--", zorder=0)
    ax.set_title(title, fontsize=12, pad=10)
    ax.grid(axis="y", visible=False)
    _save(fig, out_name)


# ---------------------------------------------------------------------------
# Cost projections
# ---------------------------------------------------------------------------

def parse_cost_projections(md_text: str) -> list[dict]:
    """Parse model sections with a 3-row cost table (800 / 25K / 320K)."""
    models = []
    cur = None
    for line in md_text.splitlines():
        m = re.match(r"^## Model\s+\d+:\s*`([^`]+)`", line.strip())
        if m:
            cur = {"model": m.group(1), "costs": {}}
            models.append(cur)
            continue
        if cur is None or not line.strip().startswith("|"):
            continue
        cells = [_norm(c) for c in line.strip().strip("|").split("|")]
        scale = {"800": 800, "25,000": 25000, "320,000": 320000}
        key = cells[0] if cells else ""
        cost_m = re.search(r"\$([\d,]+\.?\d*)", cells[-1]) if cells else None
        if key in scale and cost_m:
            cur["costs"][scale[key]] = float(cost_m.group(1).replace(",", ""))
    return [m for m in models if len(m["costs"]) == 3]


def chart_cost_projection(paths: list[Path], out_name: str) -> None:
    models = []
    for p in paths:
        models.extend(parse_cost_projections(p.read_text(encoding="utf-8")))
    if not models:
        print("  skip (no cost tables)")
        return
    scales = [800, 25000, 320000]
    fig, ax = plt.subplots(figsize=(10, 6))
    x = np.arange(len(models))
    width = 0.26
    for si, scale in enumerate(scales):
        vals = [m["costs"][scale] for m in models]
        bars = ax.bar(
            x + (si - 1) * width, vals, width,
            color=[ACCENT, "#5b8def", "#a6c2f7"][si],
            label=f"{scale:,} images",
        )
        for b, v in zip(bars, vals):
            ax.text(
                b.get_x() + b.get_width() / 2, b.get_height() * 1.04,
                f"${v:,.0f}", ha="center", va="bottom", fontsize=9,
            )
    ax.set_xticks(x)
    ax.set_xticklabels([m["model"] for m in models], rotation=25, ha="right", fontsize=9)
    ax.set_yscale("log")
    ax.set_ylim(5, max(vals) * 2.5)
    ax.set_ylabel("Projected cost (USD, log scale)")
    ax.set_title("Extrapolated OpenRouter cost per model (800 / 25K / 320K images)")
    ax.legend(frameon=False)
    _save(fig, out_name)


# ---------------------------------------------------------------------------
# Hasty-stop trigger words
# ---------------------------------------------------------------------------

def chart_hasty_stop_words(md_path: Path, out_name: str) -> None:
    rows = []
    for line in md_path.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [_norm(c) for c in line.strip().strip("|").split("|")]
        if len(cells) >= 7 and cells[0] and cells[0] != "word":
            try:
                rows.append((cells[0], float(cells[-1]), int(cells[1])))
            except ValueError:
                continue
    if not rows:
        print("  skip (no hasty-stop table)")
        return
    rows.sort(key=lambda t: t[1])
    words = [r[0] for r in rows]
    scores = [r[1] for r in rows]
    ns = [r[2] for r in rows]
    fig, ax = plt.subplots(figsize=(9, 6.5))
    y = np.arange(len(words))
    ax.barh(y, scores, color=BAD if max(scores) > 1 else ACCENT, height=0.7)
    for yi, s, n in zip(y, scores, ns):
        ax.text(s + 0.01, yi, f"{s:.2f}  (n={n})", va="center", fontsize=8)
    ax.set_yticks(y)
    ax.set_yticklabels(words, fontsize=9)
    ax.set_xlim(0, max(scores) * 1.28)
    ax.set_xlabel("hasty score (early stop × error lift × frequency)")
    ax.set_title("Hasty-stop trigger words — words that push early, wrong commits")
    ax.grid(axis="y", visible=False)
    _save(fig, out_name)


# ---------------------------------------------------------------------------
# Accuracy progress (curated)
# ---------------------------------------------------------------------------

PROGRESS = [
    # (label, slice, accuracy_pct) -- curated from docs/CHANGELOG.md + experiment_log.md
    ("gemini v0 (base)", "800", 72.9),
    ("qwen v0 (ctrl)", "480", 69.2),
    ("gemini disambig", "160", 83.75),
    ("qwen v10", "160", 97.5),
    ("qwen v11", "160", 98.7),
    ("qwen v11.7", "160", 98.1),
    ("qwen v11.8", "160", 99.4),
    ("qwen v11.8", "320", 87.2),
    ("qwen v11.8", "480", 89.1),
    ("qwen v11.8", "800", 83.1),
    ("qwen v11.8", "1,120", 82.6),
    ("qwen v13", "160 (v2)", 86.2),
    ("qwen v14", "160 (v2)", 85.0),
    ("qwen v16", "160 (v1)", 96.2),
    ("qwen v16", "160 (v3)", 79.4),
    ("qwen v17", "160 (v1)", 95.0),
    ("qwen v17.2", "exemplar 48", 68.8),
    ("qwen v18 (exp.)", "exemplar 48", 64.6),
]

SLICE_COLORS = {
    "160": "#1b2a4a",
    "320": ACCENT,
    "480": "#5b8def",
    "800": "#a6c2f7",
    "1,120": "#8e44ad",
    "160 (v1)": "#d4a017",
    "160 (v2)": "#d4a017",
    "160 (v3)": "#d4a017",
    "exemplar 48": "#e8a13c",
}


def chart_progress(out_name: str) -> None:
    fig, ax = plt.subplots(figsize=(14, 7.6))
    x = np.arange(len(PROGRESS))
    colors = [SLICE_COLORS.get(s, GRID) for _, s, _ in PROGRESS]
    vals = [v for _, _, v in PROGRESS]
    ax.bar(x, vals, color=colors, width=0.68)
    for xi, v in zip(x, vals):
        ax.text(xi, v - 2.4, f"{v:.1f}", ha="center", va="center",
                fontsize=9, fontweight="bold", color="white")
    ax.set_xticks(x)
    ax.set_xticklabels([f"{l}\n({s})" for l, s, _ in PROGRESS], rotation=45, ha="right", fontsize=8.5)
    ax.set_ylim(0, 108)
    ax.set_ylabel("Exact-match accuracy (%)")
    ax.set_title("Accuracy progress: baseline → prompt iterations → production slices", pad=14)
    ax.grid(axis="x", visible=False)
    handles = [plt.Rectangle((0, 0), 1, 1, color=c) for c in dict.fromkeys(SLICE_COLORS.values())]
    labels = ["160 dev-set", "320", "480", "800", "1,120", "HF-mirror v2/v3", "exemplar slice"]
    ax.legend(handles, labels, ncol=7, frameon=False, loc="upper center",
              bbox_to_anchor=(0.5, -0.36), fontsize=9, columnspacing=1.2)
    _save(fig, out_name)


# ---------------------------------------------------------------------------
# ALE (Accumulated Local Effects) curves
# ---------------------------------------------------------------------------

ALE_FEATURES = [
    ("reasoning_len", "Reasoning length (chars)"),
    ("checks_walked", "Checks walked before stop"),
    ("stop_position", "Stop position (check #)"),
    ("max_tokens", "Token budget"),
    ("cost", "Cost (USD)"),
    ("attempts", "Attempts"),
]


def chart_ale_correctness(out_name: str, prompt_version: str = "v11.8") -> None:
    """Multi-panel ALE of reasoning features on P(correct).

    Reads the committed corpus (reports/monte_carlo/corpus.jsonl), filters to
    reasoning-covered rows, and computes ALE per feature with 20 quantile bins
    and 200-draw bootstrap CI. Matches the methodology in ale_stopword_visual.py.
    """
    corpus_path = MC_DIR / "corpus.jsonl"
    if not corpus_path.exists():
        print(f"  skip ALE (corpus missing: {corpus_path})")
        return
    records = load_corpus(corpus_path)
    rows = _build_rows(records)
    rows = [r for r in rows if (r.get("reasoning_len") or 0) > 0]
    if prompt_version:
        rows = [r for r in rows if r.get("prompt_version") == prompt_version]
    if not rows:
        print("  skip ALE (no rows after filtering)")
        return

    panels = []
    for key, label in ALE_FEATURES:
        pts = [(r[key], 1.0 if r["correct"] else 0.0)
               for r in rows if r.get(key) is not None and np.isfinite(r[key])]
        if len(pts) < 20:
            continue
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]
        res = accumulated_local_effects(xs, ys, n_bins=20)
        if res is None:
            continue
        panels.append((key, label, res))

    if not panels:
        print("  skip ALE (no panels computable)")
        return

    ncols = 2
    nrows = int(np.ceil(len(panels) / ncols))
    fig, axes = plt.subplots(nrows, ncols, figsize=(14, 3.6 * nrows))
    axes = np.atleast_1d(axes).ravel()
    for ax, (key, label, res) in zip(axes, panels):
        ax.fill_between(res["centers"], res["ci_lo"], res["ci_hi"],
                        color=ACCENT, alpha=0.15)
        ax.plot(res["centers"], res["ale"], color=NAVY, lw=2)
        ax.axhline(0.0, color="gray", lw=0.8, ls="--")
        ax.set_title(f"ALE of {label}", fontsize=10, pad=6)
        ax.set_xlabel(label, fontsize=9)
        ax.set_ylabel("Effect on P(correct)", fontsize=9)
        ax.tick_params(labelsize=8)
        ax.grid(alpha=0.3)
    for ax in axes[len(panels):]:
        ax.set_visible(False)
    fig.suptitle(
        f"Accumulated Local Effects on Classification Accuracy — {prompt_version}\n"
        f"({len(rows)} reasoning-covered rows, 20 bins, 200-draw bootstrap)",
        fontsize=12, fontweight="bold", y=0.995,
    )
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    _save(fig, out_name)


# ---------------------------------------------------------------------------
# Stop-word scatter (trigger geography)
# ---------------------------------------------------------------------------

def chart_stop_scatter(md_path: Path, out_name: str) -> None:
    """Bubble chart: stop position vs error rate per trigger word."""
    rows = []
    for line in md_path.read_text(encoding="utf-8").splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [_norm(c) for c in line.strip().strip("|").split("|")]
        if len(cells) >= 7 and cells[0] and cells[0] != "word":
            try:
                rows.append({
                    "word": cells[0],
                    "freq": int(cells[1]),
                    "avg_stop_position": float(cells[2]),
                    "error_rate": float(cells[3].rstrip("%")) / 100,
                    "early_lift": float(cells[4]),
                    "err_lift": float(cells[5]),
                    "hasty_score": float(cells[6]),
                })
            except ValueError:
                continue
    if not rows:
        print("  skip stop-scatter (no word table)")
        return
    rows.sort(key=lambda w: w["hasty_score"], reverse=True)
    top = rows[:40]
    fig, ax = plt.subplots(figsize=(11, 7))
    xs = [w["avg_stop_position"] for w in top]
    ys = [w["error_rate"] * 100 for w in top]
    sizes = [20 + 55 * np.log1p(w["freq"]) for w in top]
    sc = ax.scatter(xs, ys, s=sizes, alpha=0.65, c=[w["hasty_score"] for w in top],
                    cmap="RdYlBu_r", edgecolor="gray", linewidth=0.5)
    placed = []
    for wi, w in enumerate(top[:12]):
        px, py = w["avg_stop_position"], w["error_rate"] * 100
        if any(abs(px - ox) < 1.2 and abs(py - oy) < 6 for ox, oy in placed):
            continue
        placed.append((px, py))
        offset = (4, 3) if wi % 2 == 0 else (4, -12)
        ax.annotate(w["word"], (px, py), fontsize=8.5, xytext=offset,
                    textcoords="offset points")
    ax.axvspan(1, 6, color="#e74c3c", alpha=0.06, label="early-stop zone")
    ax.axhline(50, color="gray", ls="--", lw=0.8, alpha=0.6)
    ax.set_xlabel("Mean stop position (check #) when word triggers", fontsize=11)
    ax.set_ylabel("Error rate when word triggers (%)", fontsize=11)
    ax.set_title("Stop-Word Trigger Geography: early + wrong = hasty",
                 fontsize=12, fontweight="bold")
    ax.legend(loc="lower right", fontsize=9)
    cbar = fig.colorbar(sc, ax=ax, shrink=0.7)
    cbar.set_label("hasty score", fontsize=10)
    ax.grid(alpha=0.3)
    _save(fig, out_name)


# ---------------------------------------------------------------------------
# Monte Carlo visualizations (for site montecarlo pages)
# ---------------------------------------------------------------------------

def chart_ensemble_vs_k(md_path: Path, out_name: str) -> None:
    """Ensemble majority-vote accuracy by committee size K with 95% CI band."""
    text = md_path.read_text(encoding="utf-8")
    rows = []
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [_norm(c) for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[0] and cells[0] != "K":
            try:
                k = int(cells[0])
                acc = float(cells[1])
                lo_s, hi_s = cells[2].split("-")
                lo, hi = float(lo_s), float(hi_s)
                rows.append((k, acc, lo, hi))
            except ValueError:
                continue
    if not rows:
        print("  skip ensemble (no table)")
        return
    ks = [r[0] for r in rows]
    accs = [r[1] for r in rows]
    lo = [r[2] for r in rows]
    hi = [r[3] for r in rows]
    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.plot(ks, [a * 100 for a in accs], marker="o", color=NAVY, linewidth=2.2, zorder=3)
    ax.fill_between(ks, [l * 100 for l in lo], [h * 100 for h in hi],
                    color=ACCENT, alpha=0.15)
    for k, a in zip(ks, accs):
        if k % 2 == 1:
            ax.annotate(f"{a:.3f}", (k, a * 100), textcoords="offset points",
                        xytext=(0, 8), ha="center", fontsize=8.5)
    ax.set_xticks(ks)
    ax.set_xlabel("Committee size K (majority vote)", fontsize=10)
    ax.set_ylabel("Simulated accuracy (%)", fontsize=10)
    ax.yaxis.set_label_coords(-0.09, 0.5)
    ax.set_title("Ensemble majority vote: monotone gains, diminishing returns",
                 fontsize=11, fontweight="bold")
    ax.set_ylim(80, 88)
    ax.grid(alpha=0.3)
    _save(fig, out_name)


def chart_routing(md_path: Path, out_name: str) -> None:
    """Confidence-gated escalation: accuracy vs alpha with cost twin axis."""
    text = md_path.read_text(encoding="utf-8")
    rows = []
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [_norm(c) for c in line.strip().strip("|").split("|")]
        if len(cells) >= 5 and cells[0] and cells[0] != "alpha":
            try:
                alpha = float(cells[0].rstrip("%")) / 100
                acc = float(cells[3])
                cost = float(cells[5].rstrip("x"))
                rows.append((alpha, acc, cost))
            except ValueError:
                continue
    if not rows:
        print("  skip routing (no table)")
        return
    alpha = [r[0] for r in rows]
    accs = [r[1] * 100 for r in rows]
    cost = [r[2] for r in rows]
    fig, ax1 = plt.subplots(figsize=(9, 5.2))
    ax1.plot(alpha, accs, marker="o", color=NAVY, linewidth=2.2, zorder=3, label="Accuracy")
    ax1.axhline(82.1, color="#999", linestyle="--", linewidth=1.3)
    ax1.text(0.68, 82.6, "baseline 82.1%", fontsize=9, color="#666")
    ax1.set_xlabel("Escalation fraction α (lowest-confidence tail)", fontsize=10)
    ax1.set_ylabel("Accuracy (%)", fontsize=10)
    ax1.set_ylim(80, 93)
    ax1.grid(alpha=0.3)
    ax2 = ax1.twinx()
    ax2.plot(alpha, cost, marker="s", color=BAD, linewidth=1.8, linestyle="--", zorder=2, label="Cost (×)")
    ax2.set_ylabel("Cost factor (×)", color=BAD, fontsize=10)
    ax2.tick_params(axis="y", labelcolor=BAD)
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=9,
               framealpha=0.9, frameon=True)
    ax1.set_title("Confidence-gated escalation: peak 91.9% at 1.8× cost (simulated)",
                  fontsize=11, fontweight="bold")
    _save(fig, out_name)


def chart_failure_pipeline(md_path: Path, out_name: str) -> None:
    """Failure-pipeline sensitivity sweep: grouped bars by max_tries × fallback."""
    text = md_path.read_text(encoding="utf-8")
    rows = []
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [_norm(c) for c in line.strip().strip("|").split("|")]
        if len(cells) >= 3 and cells[0] and cells[0] != "max_tries":
            try:
                tries = int(cells[0])
                fb = cells[1]
                rate = float(cells[2].rstrip("%"))
                rows.append((tries, fb, rate))
            except ValueError:
                continue
    if not rows:
        print("  skip failure-pipeline (no table)")
        return
    tries_unique = sorted(set(r[0] for r in rows))
    x = np.arange(len(tries_unique))
    width = 0.32
    off_rates = [r[2] for r in rows if r[1] == "off"]
    on_rates = [r[2] for r in rows if r[1] == "on"]
    fig, ax = plt.subplots(figsize=(9, 5.2))
    ax.bar(x - width / 2, off_rates, width, label="fallback off",
           color=BAD, zorder=3, edgecolor="#444", linewidth=0.4)
    ax.bar(x + width / 2, on_rates, width, label="fallback on",
           color=GOOD, zorder=3, edgecolor="#444", linewidth=0.4)
    for xi, v in zip(x - width / 2, off_rates):
        ax.text(xi, v + 0.15, f"{v:.3f}%", ha="center", va="bottom", fontsize=8)
    for xi, v in zip(x + width / 2, on_rates):
        ax.text(xi, v + 0.08, f"{v:.3f}%", ha="center", va="bottom", fontsize=8)
    ax.set_xticks(x)
    ax.set_xticklabels([f"max_tries={t}" for t in tries_unique], fontsize=9)
    ax.set_ylabel("Simulated failure rate (%)", fontsize=10)
    ax.set_title("Failure pipeline: fallback collapses 2.86% → 0.114%",
                 fontsize=11, fontweight="bold")
    ax.set_ylim(0, 3.6)
    ax.legend(fontsize=9, framealpha=0.9)
    ax.grid(alpha=0.3)
    _save(fig, out_name)


def chart_prompt_ablation(md_path: Path, out_name: str) -> None:
    """Forest plot of paired-bootstrap prompt deltas with 95% CI."""
    text = md_path.read_text(encoding="utf-8")
    rows = []
    for line in text.splitlines():
        if not line.strip().startswith("|"):
            continue
        cells = [_norm(c) for c in line.strip().strip("|").split("|")]
        if len(cells) >= 10 and cells[0] and cells[0] != "model":
            try:
                delta = float(cells[6])
                ci_s = cells[7]
                m = re.search(r"([-+]?\d+\.\d+)\s*\.\.\s*([-+]?\d+\.\d+)", ci_s)
                if not m:
                    continue
                lo, hi = float(m.group(1)), float(m.group(2))
                label = f"{cells[1]} vs {cells[2]}"
                rows.append((label, delta, lo, hi, cells[9]))
            except (ValueError, IndexError):
                continue
    if not rows:
        print("  skip prompt-ablation (no table)")
        return
    rows.reverse()
    labels = [r[0] for r in rows]
    deltas = [r[1] for r in rows]
    ci_lo = [r[2] for r in rows]  # absolute lower bound
    ci_hi = [r[3] for r in rows]  # absolute upper bound
    verdicts = [r[4] for r in rows]
    colors = [GOOD if v == "B wins**" else (BAD if v == "A wins**" else "#888")
              for v in verdicts]
    # barh xerr expects non-negative [[left_extent], [right_extent]]
    left_extent = [max(0, d - lo) for d, lo in zip(deltas, ci_lo)]
    right_extent = [max(0, hi - d) for d, hi in zip(deltas, ci_hi)]
    fig, ax = plt.subplots(figsize=(9, 5.5))
    y = np.arange(len(labels))
    ax.barh(y, deltas, xerr=[left_extent, right_extent], capsize=3,
            color=colors, zorder=3, error_kw=dict(elinewidth=1, ecolor="#444"))
    for yi, d, lbl in zip(y, deltas, labels):
        ax.text(d + 0.004, yi, f"{d:+.3f}", va="center", fontsize=8.5)
    ax.axvline(0, color="#444", linewidth=1)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=8.5)
    ax.margins(x=0.22)
    ax.set_xlabel("Mean delta (A − B), positive favors A", fontsize=10)
    ax.set_title("Paired-bootstrap prompt ablation (95% CI, 10 000 reps)",
                 fontsize=11, fontweight="bold")
    _save(fig, out_name)


def chart_verification(md_path: Path, out_name: str) -> None:
    """Measured vs simulated accuracy: escalation + exemplar slices."""
    text = md_path.read_text(encoding="utf-8")
    # Parse the two slices
    groups = {"Escalation": [], "Exemplar": []}
    cur = None
    for line in text.splitlines():
        if "Escalation slice" in line:
            cur = "Escalation"
        elif "Exemplar slice" in line:
            cur = "Exemplar"
        elif not line.strip().startswith("|") or "run" in line.lower():
            continue
        if cur:
            cells = [_norm(c) for c in line.strip().strip("|").split("|")]
            if len(cells) >= 4:
                try:
                    run = cells[0]
                    acc = float(cells[3])
                    groups[cur].append((run, acc))
                except ValueError:
                    continue
    cats, vals, colors = [], [], []
    RUN_SHORT = {
        "base (v11.8)": "base v11.8",
        "escalated (max effort)": "escalated (max effort)",
        "base (v17.2)": "base v17.2",
        "exemplar (v18)": "exemplar v18",
    }
    for g, grp in groups.items():
        for run, acc in grp:
            cats.append(f"{g}\n{RUN_SHORT.get(run, run)}")
            vals.append(acc * 100)
            colors.append(NAVY if "base" in run else ACCENT)
    if not cats:
        print("  skip verification (no data)")
        return
    fig, ax = plt.subplots(figsize=(8.5, 5.2))
    bars = ax.bar(cats, vals, color=colors, zorder=3, width=0.55, edgecolor="#444", linewidth=0.4)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.6, f"{v:.1f}%",
                ha="center", va="bottom", fontsize=9.5, fontweight="bold")
    ax.set_ylabel("Accuracy (%)", fontsize=10)
    ax.set_title("Verification: measured vs simulated",
                 fontsize=11, fontweight="bold")
    ax.set_ylim(0, 100)
    ax.tick_params(axis="x", labelsize=9.5)
    ax.grid(axis="y", alpha=0.3)
    _save(fig, out_name)


def chart_corpus_summary(md_path: Path, out_name: str) -> None:
    """Corpus composition: model rows and prompt version rows side by side."""
    text = md_path.read_text(encoding="utf-8")
    models, prompts = [], []
    cur = None
    for line in text.splitlines():
        if "## Models" in line:
            cur = "models"
        elif "## Prompt versions" in line:
            cur = "prompts"
        elif line.strip().startswith("## "):
            cur = None
        elif cur and line.strip().startswith("|") and "model" not in line.lower() and "prompt" not in line.lower():
            cells = [_norm(c) for c in line.strip().strip("|").split("|")]
            if len(cells) >= 2:
                try:
                    count = int(cells[-1])
                    label = cells[0]
                    if cur == "models":
                        models.append((label, count))
                    elif cur == "prompts":
                        prompts.append((label, count))
                except ValueError:
                    continue
    if not models and not prompts:
        print("  skip corpus-summary (no tables)")
        return
    fig, axes = plt.subplots(1, 2, figsize=(12, 5.5))
    if models:
        models.sort(key=lambda t: t[1])
        y = np.arange(len(models))
        axes[0].barh(y, [t[1] for t in models], color=NAVY, zorder=3)
        for i, (lbl, v) in enumerate(models):
            axes[0].text(v + 10, i, f"{v:,}", va="center", fontsize=8.5)
        axes[0].set_yticks(y)
        axes[0].set_yticklabels([t[0] for t in models], fontsize=8.5)
        axes[0].set_xlabel("Rows", fontsize=10)
        axes[0].set_title("Corpus by model", fontsize=11, fontweight="bold")
    if prompts:
        prompts.sort(key=lambda t: t[1])
        y = np.arange(len(prompts))
        axes[1].barh(y, [t[1] for t in prompts], color=ACCENT, zorder=3)
        for i, (lbl, v) in enumerate(prompts):
            axes[1].text(v + 10, i, f"{v:,}", va="center", fontsize=8.5)
        axes[1].set_yticks(y)
        axes[1].set_yticklabels([t[0] for t in prompts], fontsize=8.5)
        axes[1].set_xlabel("Rows", fontsize=10)
        axes[1].set_title("Corpus by prompt version", fontsize=11, fontweight="bold")
    fig.suptitle("Monte Carlo corpus composition (4,641 rows / 1,512 images)",
                 fontsize=12, fontweight="bold", y=1.01)
    fig.tight_layout()
    _save(fig, out_name)


# ---------------------------------------------------------------------------
# Trace-language visualizations (differential phrase net, log-odds, scatter)
# ---------------------------------------------------------------------------

def _trace_rows() -> list[dict]:
    """Reasoning-covered corpus rows for the trace-language charts."""
    corpus_path = MC_DIR / "corpus.jsonl"
    if not corpus_path.exists():
        print(f"  skip trace-language (corpus missing: {corpus_path})")
        return []
    return build_trace_records(load_corpus(corpus_path))


def _trace_graph() -> tuple[list[dict], list[dict]]:
    """Shared phrase-net analysis: (nodes, edges) for both SVG and JSON output."""
    rows = _trace_rows()
    if not rows:
        return [], []
    edges = differential_bigrams(rows, alpha=0.01, min_fail=3, min_z=0.5,
                                 max_edges=400)
    prompt_vocab = load_prompt_vocab()
    cycles = find_cycles(edges, max_len=6)
    cycle_edges = set()
    for c in cycles:
        for i in range(len(c)):
            cycle_edges.add((c[i], c[(i + 1) % len(c)]))
    stats: dict[str, dict] = {}
    for e in edges:
        for key in ("a", "b"):
            node = e[key]
            s = stats.setdefault(node, {"fail": 0, "ok": 0})
            s["fail"] += e["fail"]
            s["ok"] += e["ok"]
    nodes = [
        {
            "id": w,
            "fail": s["fail"],
            "ok": s["ok"],
            "share": s["fail"] / max(s["fail"] + s["ok"], 1),
            "leak": w in prompt_vocab,
        }
        for w, s in sorted(stats.items())
    ]
    node_by_id = {n["id"]: n for n in nodes}
    out_edges = [
        {
            "from": e["a"],
            "to": e["b"],
            "z": e["z"],
            "fail": e["fail"],
            "ok": e["ok"],
            "in_cycle": (e["a"], e["b"]) in cycle_edges,
        }
        for e in edges
    ]
    return nodes, out_edges


def _blend(lo, hi, t):
    return lo * (1 - float(t)) + hi * float(t)


def _trace_node_rgb(share: float) -> str:
    lo = np.array([0.12, 0.62, 0.35])
    hi = np.array([0.84, 0.27, 0.27])
    rgb = _blend(lo, hi, max(0.0, min(1.0, share)))
    return "#" + "".join(f"{int(round(c * 255)):02x}" for c in rgb)


def chart_trace_logodds(out_name: str) -> None:
    """Fightin' Words log-odds bars: top fail-biased and success-biased words."""
    rows = _trace_rows()
    if not rows:
        return
    fail_counts, ok_counts = word_counts(rows)
    words = log_odds_ratio(fail_counts, ok_counts, alpha=0.01, min_count=5)
    fail_biased = [w for w in words if w["z"] > 0][-30:][::-1]
    ok_biased = [w for w in words if w["z"] <= 0][:30][::-1]
    fig, (ax_f, ax_o) = plt.subplots(1, 2, figsize=(15, 10.5))
    for ax, items, color, title in (
        (ax_f, fail_biased, BAD, "Most likely in FAILED traces"),
        (ax_o, ok_biased, GOOD, "Most likely in CORRECT traces"),
    ):
        y = np.arange(len(items))
        ax.barh(y, [w["z"] for w in items], color=color, height=0.68, zorder=3)
        for yi, w in zip(y, items):
            ax.text(w["z"] + max(0.06 * abs(w["z"]), 0.04), yi, f"{w['fail']} · {w['ok']}",
                    va="center", ha="left", fontsize=8.5, color="#333333")
        ax.set_yticks(y)
        ax.set_yticklabels([w["word"] for w in items], fontsize=9.5)
        ax.set_ylim(-0.6, len(items) - 0.4)
        ax.set_xlim(0, max(w["z"] for w in items) * 1.22)
        ax.axvline(0.0, color="gray", lw=0.8)
        ax.set_title(title, fontsize=12.5, fontweight="bold", pad=10)
        ax.set_xlabel("Log-odds ratio z (fail vs correct)", fontsize=11)
        ax.grid(axis="x", alpha=0.35)
        ax.tick_params(axis="y", length=0)
    fig.suptitle(
        "Log-odds ratio with uninformative Dirichlet prior (a = 0.01)\n"
        "z = log((f+a)/(F-f+a)) − log((o+a)/(O-o+a)) — Fightin' Words (Monroe et al., 2008)\n"
        "bar labels show fail · correct raw counts",
        fontsize=12.5, fontweight="bold",
    )
    _save(fig, out_name)


def chart_trace_scatter(out_name: str) -> None:
    """Scattertext-style log-log grid of word frequency in correct vs failed traces."""
    rows = _trace_rows()
    if not rows:
        return
    points, _, _ = scatter_frequencies(rows)
    points = sorted(points, key=lambda p: p["fail"] + p["ok"], reverse=True)[:2500]
    fail_counts, ok_counts = word_counts(rows)
    words = log_odds_ratio(fail_counts, ok_counts, alpha=0.01, min_count=5)
    z_by_word = {w["word"]: w["z"] for w in words}
    fig, ax = plt.subplots(figsize=(12, 10.5))
    xs = [max(p["freq_ok"], 0.5) for p in points]
    ys = [max(p["freq_fail"], 0.5) for p in points]
    sizes = [16 + 7 * np.log1p(p["fail"] + p["ok"]) for p in points]
    zs = [z_by_word.get(p["word"], 0.0) for p in points]
    colors = [BAD if z > 0.5 else GOOD if z < -0.5 else "#b9c4d6" for z in zs]
    ax.scatter(xs, ys, s=sizes, c=colors, alpha=0.55, edgecolors="none",
               rasterized=True, zorder=2)
    lim = [0.3, 10 ** 4]
    ax.plot(lim, lim, color="gray", lw=1, ls="--", alpha=0.7, zorder=1)
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlim(*lim)
    ax.set_ylim(*lim)
    ax.set_xlabel("Frequency per million tokens — CORRECT traces", fontsize=12)
    ax.set_ylabel("Frequency per million tokens — FAILED traces", fontsize=12)
    ax.set_title(
        "Scattertext-style word geography\n"
        "top-left = failure hallmarks · bottom-right = success drivers",
        fontsize=13, fontweight="bold",
    )
    ranked = sorted(points, key=lambda p: abs(z_by_word.get(p["word"], 0.0)),
                    reverse=True)
    placed: list[tuple[float, float]] = []
    chosen = []
    min_sep = 0.45
    for p in ranked:
        z = z_by_word.get(p["word"], 0.0)
        if abs(z) < 0.8:
            break
        cx, cy = np.log10(max(p["freq_ok"], 0.5)), np.log10(max(p["freq_fail"], 0.5))
        if placed and min(np.hypot(cx - qx, cy - qy) for qx, qy in placed) < min_sep:
            continue
        placed.append((cx, cy))
        chosen.append(p)
        if len(chosen) >= 18:
            break
    for p in chosen:
        z = z_by_word.get(p["word"], 0.0)
        x, y = max(p["freq_ok"], 0.5), max(p["freq_fail"], 0.5)
        dx = -3 if p["freq_fail"] > p["freq_ok"] else 4
        ax.annotate(
            p["word"], (x, y),
            fontsize=9, fontweight="bold", color=NAVY,
            xytext=(dx, 5), textcoords="offset points",
            arrowprops=dict(arrowstyle="-", color="#8a94a6", lw=0.8,
                            shrinkA=0, shrinkB=3),
            bbox=dict(boxstyle="round,pad=0.18", fc="white", ec="#d0d6e0",
                      lw=0.7, alpha=0.9),
            zorder=5,
        )
    handles = [
        plt.Line2D([0], [0], marker="o", ls="", markersize=9, mfc=BAD, mec="none", alpha=0.7,
                   label="Failure-biased (z > 0.5)"),
        plt.Line2D([0], [0], marker="o", ls="", markersize=9, mfc="#b9c4d6", mec="none", alpha=0.7,
                   label="Neutral (−0.5 ≤ z ≤ 0.5)"),
        plt.Line2D([0], [0], marker="o", ls="", markersize=9, mfc=GOOD, mec="none", alpha=0.7,
                   label="Success-biased (z < −0.5)"),
    ]
    ax.legend(handles=handles, loc="upper right", fontsize=10, framealpha=0.95,
              title="Word bias", title_fontsize=10.5)
    _save(fig, out_name)


def chart_phrase_net(out_name: str) -> None:
    """Differential directed bigram graph of failed traces with loops highlighted."""
    nodes, edges = _trace_graph()
    if not edges:
        print("  skip phrase net (no differential edges)")
        return
    import networkx as nx

    G = nx.DiGraph()
    for e in edges:
        G.add_edge(e["from"], e["to"], weight=e["z"])
    cycle_edges = {(e["from"], e["to"]) for e in edges if e["in_cycle"]}
    stats = {n["id"]: n for n in nodes}
    pos = nx.spring_layout(G, seed=42, k=0.5)
    zs = [e["z"] for e in edges]
    zmin, zmax = min(zs), max(zs)
    fig, ax = plt.subplots(figsize=(15, 11))
    sizes = [200 + 70 * np.log1p(stats[n]["fail"]) for n in G.nodes()]
    rgb = np.array([_hex_to_rgb(_trace_node_rgb(stats[n]["share"])) for n in G.nodes()])
    nx.draw_networkx_nodes(G, pos, ax=ax, node_size=sizes, node_color=rgb,
                           edgecolors="#333333", linewidths=0.8)
    plain = [(a, b) for a, b in G.edges() if (a, b) not in cycle_edges]
    looped = [(a, b) for a, b in G.edges() if (a, b) in cycle_edges]
    for edge_list, color, alpha in ((plain, "#888888", 0.45), (looped, BAD, 1.0)):
        if not edge_list:
            continue
        widths = [0.8 + 4.5 * (G[a][b]["weight"] - zmin) / (zmax - zmin)
                  for a, b in edge_list]
        nx.draw_networkx_edges(G, pos, ax=ax, edgelist=edge_list, width=widths,
                               edge_color=color, alpha=alpha, arrowstyle="-|>",
                               arrowsize=13, connectionstyle="arc3,rad=0.12")
    leak_nodes = [n for n in G.nodes() if stats[n]["leak"]]
    if leak_nodes:
        nx.draw_networkx_nodes(G, pos, ax=ax, nodelist=leak_nodes,
                               node_size=[sizes[list(G.nodes()).index(n)]
                                          for n in leak_nodes],
                               node_color="none", edgecolors="#d4a017",
                               linewidths=2.0, node_shape="D")
    nx.draw_networkx_labels(G, pos, labels={n: n for n in G.nodes()}, ax=ax,
                            font_size=8.5, font_color=NAVY)
    ax.set_title(
        f"Differential phrase net — bi-grams over-represented in failed traces\n"
        f"({G.number_of_nodes()} words, {G.number_of_edges()} edges, "
        f"{len(cycle_edges)} cycle edges in red)",
        fontsize=13, fontweight="bold",
    )
    ax.axis("off")
    _save(fig, out_name)


def chart_phrase_net_data(out_json: str) -> None:
    """Emit the phrase-net graph as JSON for the interactive vis-network widget."""
    nodes, edges = _trace_graph()
    if not edges:
        print(f"  skip phrase net JSON (no differential edges): {out_json}")
        return
    payload = {
        "generated": "build_site_charts.py chart_phrase_net_data",
        "nodes": nodes,
        "edges": edges,
    }
    out = CHARTS_DIR / out_json
    out.write_text(json.dumps(payload), encoding="utf-8")
    print(f"  chart data: {out.name} ({len(nodes)} nodes, {len(edges)} edges)")


def _hex_to_rgb(hex_color: str) -> np.ndarray:
    hex_color = hex_color.lstrip("#")
    return np.array([int(hex_color[i:i + 2], 16) for i in (0, 2, 4)]) / 255.0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    CHARTS_DIR.mkdir(parents=True, exist_ok=True)

    print("Confusion matrices (reports/confusion_matrices + docs/experiments):")
    sources = sorted((ROOT / "reports" / "confusion_matrices").glob("confusion_matrix_*.md"))
    sources += sorted((ROOT / "docs" / "experiments").glob("confusion_matrix_main-*.md"))
    for md in sources:
        exp = md.name.removeprefix("confusion_matrix_").removesuffix(".md")
        chart_confusion_matrix(md, f"confusion_matrix_{exp}.svg")

    print("Per-class accuracy (report files + 800pic notes):")
    report_sources = sorted((ROOT / "reports" / "experiment_reports").glob("report_*.md"))
    for md in report_sources:
        exp = md.name.removeprefix("report_").removesuffix(".md")
        chart_per_class(md, f"per_class_accuracy_{exp}.svg", f"Per-class accuracy — {exp}")
    final_1120 = ROOT / "reports" / "experiment_reports" / "qwen3.7-flash_v11.8_1600_balanced_1120_final.md"
    if final_1120.exists():
        chart_per_class(
            final_1120,
            "per_class_accuracy_qwen3.7-flash_v11.8_reasoning_1600_balanced_1120.svg",
            "Per-class accuracy — qwen3.7-flash v11.8 · 1,120-image slice",
        )
    chart_per_class(
        ROOT / "docs" / "experiments" / "800pic_tst_notes.md",
        "per_class_accuracy_gemini-2.5-flash_800_notes.svg",
        "Per-class accuracy — gemini-2.5-flash 800 (from notes)",
    )

    print("Cost projections:")
    chart_cost_projection(
        [ROOT / "docs" / "experiments" / "1pic_cost_estimation.md"],
        "cost_projection_models.svg",
    )

    print("Hasty-stop words:")
    chart_hasty_stop_words(ROOT / "reports" / "monte_carlo" / "ale_stopword_report.md", "hasty_stop_words.svg")

    print("Stop-word scatter:")
    chart_stop_scatter(ROOT / "reports" / "monte_carlo" / "ale_stopword_report.md", "stop_word_scatter.svg")

    print("ALE correctness curves:")
    chart_ale_correctness("ale_correctness.svg", prompt_version="v11.8")

    print("Ensemble voting:")
    chart_ensemble_vs_k(
        ROOT / "reports" / "monte_carlo" / "ensemble_accuracy_vs_k.md",
        "ensemble_vs_k.svg",
    )

    print("Routing escalation:")
    chart_routing(
        ROOT / "reports" / "monte_carlo" / "routing_abstention.md",
        "routing_escalation.svg",
    )

    print("Failure pipeline:")
    chart_failure_pipeline(
        ROOT / "reports" / "monte_carlo" / "failure_pipeline.md",
        "failure_pipeline.svg",
    )

    print("Prompt ablation:")
    chart_prompt_ablation(
        ROOT / "reports" / "monte_carlo" / "prompt_ablation.md",
        "prompt_ablation.svg",
    )

    print("Verification measured vs simulated:")
    chart_verification(
        ROOT / "reports" / "monte_carlo" / "verification_results.md",
        "verification.svg",
    )

    print("Corpus summary:")
    chart_corpus_summary(
        ROOT / "reports" / "monte_carlo" / "corpus.summary.md",
        "corpus_summary.svg",
    )

    print("Trace-language (log-odds, scatter, phrase net):")
    chart_trace_logodds("logodds_dirichlet.svg")
    chart_trace_scatter("scattertext_style.svg")
    chart_phrase_net("phrase_net_differential.svg")
    chart_phrase_net_data("phrase_net_differential.json")

    print("Accuracy progress:")
    chart_progress("accuracy_progress.svg")

    print("Done.")


if __name__ == "__main__":
    main()
