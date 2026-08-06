
**Research question:** Which of the 16 RVL-CDIP classes drive the remaining misclassification budget, and which confusion pairs account for it?

**Formal write-up:** [`results/confusion-matrices.qmd`](Confusion-Matrices) · [`appendix/misclassifications.qmd`](Misclassifications) · [`reports/monte_carlo/corpus.summary.md`](https://github.com/Exios66/AMFAM_capstone/blob/main/reports/monte_carlo/corpus.summary.md)


## What questions or uncertainties remain?

Per-class difficulty is slice-dependent — the 160 curated slice shows near-perfect per-class scores while 1,120 shows the collapse above. Whether the difficulty ordering (form, budget/invoice, letter/memo) is stable across production-noise samples is untested; the v3/v4 disjoint slices (96.2% / 79.4% at v16) hint it is only roughly stable.

## What other levers may also fix these classes?

The [few-shot exemplar memo](Exemplar-Mining) mines correct traces for exactly these pairs as in-context examples; the [hasty-stop memo](Hasty-Stop-Words) shows trigger words that cause premature commit before the cascade reaches the discriminating checks.


---
*Published via [Posit Cloud](https://connect.posit.cloud/jackjburleson/content/019fd440-9bbf-1a22-cf30-a36183d9c7d4) · [GitHub repo](https://github.com/Exios66/AMFAM_capstone)*
