"""Generate the manuscript figure set (F1-F10) from committed data.

Deterministic and offline: every figure is drawn from markdown tables and JSON
already committed to the repository (no API access). Outputs both SVG and
300-dpi PNG into ``website/figures/`` so the manuscript renders identically
locally and when published.

Figures:
  F1  accuracy arc            — qwen3.7-flash prompt-version accuracy on the
                               160-image slice (v1 -> v11.8)
  F2  generalization falloff  — v11.8 accuracy vs slice size (160-1120)
  F3  model comparison        — 160-slice accuracy with 95% Wilson CIs
  F4  confusion heatmap       — best-run 16x16 confusion counts (row %)
  F5  per-class accuracy      — 1120-image run, threshold colored
  F6  cost projections        — OpenRouter-derived cost per image and at
                               800 / 25k / 320k images
  F7  ensemble vs committee K — majority-vote Monte Carlo
  F8  confidence-gated routing— escalation alpha vs accuracy and cost factor
  F9  hasty-stop triggers     — top trigger words by hasty_score
  F10 failure pipeline        — P(attempt success) by config + exemplar
                               measured-vs-simulated delta

Usage:
    python scripts/site/build_manuscript_figures.py
"""

from __future__ import annotations

import json
import math
import re
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "website" / "figures"
MC = ROOT / "reports" / "monte_carlo"

PALETTE = ["#264653", "#2a9d8f", "#e9c46a", "#e76f51", "#8ab17d", "#6d597a"]
sns.set_theme(style="whitegrid", context="notebook", font_scale=1.05)
plt.rcParams["figure.dpi"] = 100
plt.rcParams["svg.fonttype"] = "none"


def _wilson(k: int, n: int, z: float = 1.96) -> tuple[float, float]:
    """Wilson score interval for a binomial proportion."""
    if n == 0:
        return 0.0, 0.0
    p = k / n
    denom = 1 + z * z / n
    centre = p + z * z / (2 * n)
    half = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (centre - half) / denom, (centre + half) / denom


def _save(fig, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    for ext in (".png", ".svg"):
        fig.savefig(OUT / f"{name}{ext}", bbox_inches="tight", dpi=300 if ext == ".png" else None)
    plt.close(fig)
    print(f"  wrote {name}.png/.svg")


def _parse_md_table(text: str, header: str) -> list[list[str]]:
    """Return data rows of the first markdown table whose header line starts with ``header``."""
    lines = text.splitlines()
    rows = []
    in_table = False
    for line in lines:
        s = line.strip()
        if not s.startswith("|"):
            if in_table:
                break
            continue
        if header in s:
            in_table = True
            continue
        if in_table and s.startswith("|---"):
            continue
        if in_table:
            rows.append([c.strip().strip("`") for c in s.strip("|").split("|")])
    return rows


# ---------------------------------------------------------------------------
# F1 / F2  - accuracy arc and generalization falloff
# ---------------------------------------------------------------------------

def f1_accuracy_arc() -> None:
    arc = [(1.0, 80.1), (4.0, 83.5), (7.0, 91.1), (10.0, 97.5), (11.0, 98.7), (11.8, 99.4)]
    x = [v for v, _ in arc]
    y = [a for _, a in arc]
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.plot(x, y, marker="o", linewidth=2.4, color=PALETTE[0], markersize=7, zorder=3)
    for xi, yi in zip(x, y):
        ax.annotate(f"{yi:.1f}%", (xi, yi), textcoords="offset points", xytext=(0, 9),
                    ha="center", fontsize=9, color="#333")
    ax.set_xticks(x)
    ax.set_xticklabels([f"v{int(v) if v == int(v) else v}" for v in x])
    ax.set_ylim(75, 102)
    ax.set_xlabel("Prompt version (qwen3.7-flash, 160-image slice)")
    ax.set_ylabel("Exact-match accuracy (%)")
    ax.set_title("Prompt engineering dominates: +19.3 pp with no model or data change")
    ax.grid(axis="x", alpha=0.35)
    _save(fig, "f1_accuracy_arc")


def f2_generalization_falloff() -> None:
    pts = [(160, 99.4), (320, 87.2), (480, 89.1), (800, 83.1), (1120, 82.6)]
    x = [n for n, _ in pts]
    y = [a for _, a in pts]
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.semilogx(x, y, marker="o", linewidth=2.2, color=PALETTE[1], markersize=7, zorder=3)
    for xi, yi in zip(x, y):
        ax.annotate(f"{yi:.1f}%", (xi, yi), textcoords="offset points", xytext=(0, 9),
                    ha="center", fontsize=9, color="#333")
    ax.set_xticks(x)
    ax.set_xticklabels([str(n) for n in x])
    ax.set_xlabel("Slice size (images per-class x 16)")
    ax.set_ylabel("Exact-match accuracy (%)")
    ax.set_title("v11.8 transfer to larger, noisier slices")
    ax.set_ylim(78, 102)
    ax.grid(axis="x", which="major", alpha=0.35)
    _save(fig, "f2_generalization_falloff")


# ---------------------------------------------------------------------------
# F3 - model comparison with Wilson CIs
# ---------------------------------------------------------------------------

def f3_model_comparison() -> None:
    data = json.loads((ROOT / "website/data/experiments.json").read_text())
    rows = [r for r in data["experiments"] if r.get("images") == 160 and r.get("total")]
    keep = {}
    for r in rows:
        key = (r["model_short"], r.get("prompt_version"))
        if key in keep and (r.get("accuracy") or 0) <= (keep[key][0] or 0):
            continue
        keep[key] = (r.get("accuracy"), r.get("correct"), r.get("total"), r.get("model"))
    items = sorted(keep.items(), key=lambda kv: -(kv[1][0] or 0))
    labels = [f"{k[0]} {k[1]}" for k, _ in items]
    accs = [v[0] * 100 for v in [kv[1] for kv in items]]
    lo, hi = [], []
    for _, (_, correct, total, _) in items:
        l, h = _wilson(correct, total)
        lo.append((accs[len(lo)] - l * 100))
        hi.append(h * 100 - accs[len(hi)])
    fig, ax = plt.subplots(figsize=(9, 5.2))
    bars = ax.bar(labels, accs, yerr=[lo, hi], capsize=4, color=PALETTE[2], edgecolor="#7a6a2f",
                  error_kw=dict(elinewidth=1.2, ecolor="#444"), zorder=3)
    for b, a in zip(bars, accs):
        ax.text(b.get_x() + b.get_width() / 2, a + 1.8, f"{a:.1f}%", ha="center", fontsize=9)
    ax.axhline(80.1, color=PALETTE[4], linestyle="--", linewidth=1.4)
    ax.text(7.4, 81.0, "v1 baseline 80.1%", fontsize=9, color=PALETTE[4])
    ax.set_ylim(0, 105)
    ax.set_ylabel("Exact-match accuracy (%) on the 160-image slice")
    ax.set_title("Model comparison (best prompt version per model)")
    _save(fig, "f3_model_comparison")


# ---------------------------------------------------------------------------
# F4 - confusion heatmap
# ---------------------------------------------------------------------------

def f4_confusion_heatmap() -> None:
    data = json.loads((ROOT / "website/data/confusion-matrices.json").read_text())
    key = "qwen3.7-flash_v11_8_reasoning_160_t0_3"
    cm = data[key]
    labels, matrix = cm["labels"], np.array(cm["matrix"], dtype=float)
    row_pct = np.where(matrix.sum(axis=1, keepdims=True) > 0,
                       matrix / matrix.sum(axis=1, keepdims=True) * 100, 0.0)
    fig, ax = plt.subplots(figsize=(11, 9.5))
    annot = np.array([[f"{v:.0f}" if v >= 1 else (f"{v:.1f}" if v > 0 else "") for v in row] for row in row_pct])
    sns.heatmap(row_pct, annot=annot, fmt="", cmap="YlOrRd", vmin=0, vmax=100,
                xticklabels=labels, yticklabels=labels, cbar_kws={"label": "Row % (expected)"},
                linewidths=0.4, linecolor="#ffffff", ax=ax)
    ax.set_xlabel("Predicted class")
    ax.set_ylabel("Expected class")
    ax.set_title("Confusion matrix — qwen3.7-flash v11.8, 160-image slice (98.7%)")
    ax.tick_params(axis="x", rotation=40, labelsize=8)
    ax.tick_params(axis="y", rotation=0, labelsize=8)
    _save(fig, "f4_confusion_heatmap")


# ---------------------------------------------------------------------------
# F5 - per-class accuracy (1120-image run)
# ---------------------------------------------------------------------------

def f5_per_class_accuracy() -> None:
    data = json.loads((ROOT / "website/data/per-class-accuracy.json").read_text())
    pca = data["qwen3.7-flash_v11.8_1600_balanced_1120_final"]
    rows = sorted(pca.items(), key=lambda kv: kv[1]["accuracy"])
    classes = [k for k, _ in rows]
    accs = [v["accuracy"] * 100 for _, v in rows]
    colors = [PALETTE[1] if a >= 90 else (PALETTE[2] if a >= 70 else PALETTE[3]) for a in accs]
    fig, ax = plt.subplots(figsize=(9, 5.4))
    ax.barh(classes, accs, color=colors, zorder=3)
    for y, (a, (_, v)) in zip(range(len(accs)), zip(accs, rows)):
        ax.text(a + 0.6, y, f"{a:.1f}% ({v['correct']}/{v['total']})", va="center", fontsize=8.5)
    ax.axvline(82.6, color="#444", linestyle="--", linewidth=1.2)
    ax.set_xlim(0, 105)
    ax.set_xlabel("Accuracy (%)")
    ax.set_title("Per-class accuracy — 1120-image run (overall 82.6%)")
    _save(fig, "f5_per_class_accuracy")


# ---------------------------------------------------------------------------
# F6 - cost projections
# ---------------------------------------------------------------------------

def f6_cost_projections() -> None:
    data = json.loads((ROOT / "website/data/cost-models.json").read_text())
    models = sorted(data["models"], key=lambda m: m["actual_cost_per_image"])
    names = [m["model"] for m in models]
    per_img = [m["actual_cost_per_image"] for m in models]
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8))
    ax = axes[0]
    bars = ax.bar(names, per_img, color=PALETTE[0], zorder=3)
    for b, v in zip(bars, per_img):
        ax.text(b.get_x() + b.get_width() / 2, v * 1.03, f"${v:.4f}", ha="center", fontsize=8.5)
    ax.set_yscale("log")
    ax.set_ylabel("Billed cost per image (USD, log scale)")
    ax.set_title("OpenRouter-reported per-image cost")
    ax.tick_params(axis="x", rotation=18, labelsize=8.5)
    scales = [800, 25000, 320000]
    x = np.arange(len(models))
    width = 0.26
    ax = axes[1]
    for i, n in enumerate(scales):
        vals = [m["actual_cost_per_image"] * n for m in models]
        ax.bar(x + (i - 1) * width, vals, width, label=f"{n:,}", color=PALETTE[i], zorder=3)
    ax.set_yscale("log")
    ax.set_xticks(x)
    ax.set_xticklabels(names, rotation=18, fontsize=8.5)
    ax.set_ylabel("Projected total cost (USD, log scale)")
    ax.set_title("Linear scale-up at 800 / 25k / 320k images")
    ax.legend(title="Images", fontsize=9)
    fig.suptitle("Cost per image and scale-up projections (derived from OpenRouter metrics)", y=1.02)
    _save(fig, "f6_cost_projections")


# ---------------------------------------------------------------------------
# F7 - ensemble voting vs committee size K
# ---------------------------------------------------------------------------

def f7_ensemble_vs_k() -> None:
    rows = _parse_md_table((MC / "ensemble_accuracy_vs_k.md").read_text(), "| K |")
    ks = [int(r[0]) for r in rows]
    accs = [float(r[1]) for r in rows]
    lo = [float(r[2].split("-")[0]) for r in rows]
    hi = [float(r[2].split("-")[1]) for r in rows]
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.plot(ks, [a * 100 for a in accs], marker="o", color=PALETTE[0], linewidth=2.2, zorder=3)
    ax.fill_between(ks, [l * 100 for l in lo], [h * 100 for h in hi], color=PALETTE[0], alpha=0.15)
    for k, a in zip(ks, accs):
        ax.annotate(f"{a:.3f}", (k, a * 100), textcoords="offset points", xytext=(0, 8),
                    ha="center", fontsize=8.5)
    ax.set_xticks(ks)
    ax.set_xlabel("Committee size K (majority vote)")
    ax.set_ylabel("Simulated accuracy (%)")
    ax.set_title("Ensemble majority vote: monotone gains, diminishing returns")
    ax.set_ylim(80, 88)
    _save(fig, "f7_ensemble_vs_k")


# ---------------------------------------------------------------------------
# F8 - confidence-gated routing
# ---------------------------------------------------------------------------

def f8_routing() -> None:
    rows = _parse_md_table((MC / "routing_abstention.md").read_text(), "| alpha |")
    alpha = [float(r[0].rstrip("%")) / 100 for r in rows]
    accs = [float(r[3]) * 100 for r in rows]
    cost = [float(r[5].rstrip("x")) for r in rows]
    fig, ax1 = plt.subplots(figsize=(8.5, 4.8))
    ax1.plot(alpha, accs, marker="o", color=PALETTE[0], linewidth=2.2, zorder=3)
    ax1.axhline(82.1, color="#999", linestyle="--", linewidth=1.3)
    ax1.text(0.01, 82.6, "baseline 82.1%", fontsize=9, color="#666")
    ax1.set_xlabel("Escalation fraction $\\alpha$ (lowest-confidence tail)")
    ax1.set_ylabel("Accuracy (%)")
    ax1.set_ylim(80, 93)
    ax2 = ax1.twinx()
    ax2.plot(alpha, cost, marker="s", color=PALETTE[3], linewidth=1.8, linestyle="--", zorder=2)
    ax2.set_ylabel("Cost factor (×)", color=PALETTE[3])
    ax2.tick_params(axis="y", labelcolor=PALETTE[3])
    ax1.set_title("Confidence-gated escalation: peak 91.9% at 1.8× cost (simulated)")
    _save(fig, "f8_routing")


# ---------------------------------------------------------------------------
# F9 - hasty-stop trigger words
# ---------------------------------------------------------------------------

def f9_hasty_stop() -> None:
    rows = _parse_md_table((MC / "ale_stopword_report.md").read_text(), "| word |")
    top = rows[:10]
    words = [r[0] for r in top][::-1]
    scores = [float(r[6]) for r in top][::-1]
    fig, ax = plt.subplots(figsize=(8, 4.6))
    ax.barh(words, scores, color=PALETTE[3], zorder=3)
    for y, (w, sc) in zip(range(len(words)), zip(words, scores)):
        ax.text(sc + 0.02, y, f"{sc:.2f}", va="center", fontsize=9)
    ax.set_xlabel("Hasty-score (early stop + elevated error, frequency-weighted)")
    ax.set_title("Trigger words that push the model to commit too early (17.1% baseline error)")
    ax.set_xlim(0, 2.1)
    _save(fig, "f9_hasty_stop")


# ---------------------------------------------------------------------------
# F10 - failure pipeline + exemplar verification
# ---------------------------------------------------------------------------

def f10_failure_and_exemplar() -> None:
    fp = (MC / "failure_pipeline.md").read_text()
    sens = _parse_md_table(fp, "| max_tries |")
    fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

    # Left panel: grouped bars by max_tries, colored by fallback
    ax = axes[0]
    tries_unique = sorted(set(int(r[0]) for r in sens))
    x = np.arange(len(tries_unique))
    width = 0.32
    off_rates = [float(r[2].rstrip("%")) for r in sens if r[1] == "off"]
    on_rates = [float(r[2].rstrip("%")) for r in sens if r[1] == "on"]
    bars_off = ax.bar(x - width / 2, off_rates, width, label="fallback off",
                      color=PALETTE[3], zorder=3, edgecolor="#444", linewidth=0.4)
    bars_on = ax.bar(x + width / 2, on_rates, width, label="fallback on",
                     color=PALETTE[1], zorder=3, edgecolor="#444", linewidth=0.4)
    for bar, v in zip(bars_off, off_rates):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 0.15, f"{v:.3f}%",
                ha="center", va="bottom", fontsize=7.5, color="#444")
    for bar, v in zip(bars_on, on_rates):
        ax.text(bar.get_x() + bar.get_width() / 2, v + 0.08, f"{v:.3f}%",
                ha="center", va="bottom", fontsize=7.5, color="#1a5c3a")
    ax.set_xticks(x)
    ax.set_xticklabels([f"max_tries={t}" for t in tries_unique], fontsize=9)
    ax.set_ylabel("Simulated failure rate (%)", fontsize=10)
    ax.set_title("Failure pipeline: fallback collapses 2.86% → 0.114%",
                 fontsize=11, pad=10)
    ax.set_ylim(0, 3.6)
    ax.legend(loc="upper right", fontsize=9, framealpha=0.9)
    ax.grid(axis="y", alpha=0.3)

    # Right panel: measured vs simulated exemplar delta
    ax = axes[1]
    cats = ["Measured Δ\n(v18 vs v17.2)", "Simulated gain\n(exemplar model)"]
    vals = [-4.2, 4.27]
    bars = ax.bar(cats, vals, color=[PALETTE[3], PALETTE[1]], zorder=3,
                  width=0.55, edgecolor="#444", linewidth=0.4)
    for b, v in zip(bars, vals):
        offset = 0.5 if v > 0 else -0.5
        ax.text(b.get_x() + b.get_width() / 2, v + offset,
                f"{v:+.2f} pp", ha="center",
                va="bottom" if v > 0 else "top", fontsize=10,
                fontweight="bold", color="#1a3a5c" if v > 0 else "#7a1a1a")
    ax.axhline(0, color="#444", linewidth=1)
    ax.set_ylabel("Accuracy delta (percentage points)", fontsize=10)
    ax.set_title("Exemplar appendix: simulation over-optimistic vs measured",
                 fontsize=11, pad=10)
    ax.set_ylim(-6.5, 6.5)
    ax.grid(axis="y", alpha=0.3)

    fig.tight_layout(w_pad=2.5)
    _save(fig, "f10_failure_and_exemplar")


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    f1_accuracy_arc()
    f2_generalization_falloff()
    f3_model_comparison()
    f4_confusion_heatmap()
    f5_per_class_accuracy()
    f6_cost_projections()
    f7_ensemble_vs_k()
    f8_routing()
    f9_hasty_stop()
    f10_failure_and_exemplar()
    print(f"Done: 10 figures in {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
