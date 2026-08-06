
**Research question:** In the 14-check reasoning scratchpad, are there trigger words that push the model to commit to a label prematurely — before the cascade reaches the discriminating checks — and are those premature stops more error-prone?

**Formal write-up:** [`montecarlo/ale-stopword.qmd`](Ale-Stopword) · [`reports/monte_carlo/ale_stopword_report.md`](https://github.com/Exios66/AMFAM_capstone/blob/main/reports/monte_carlo/ale_stopword_report.md)


## What questions or uncertainties remain?

The trigger list is corpus-derived (specific to v11.8-era prompts and qwen3.7-flash) — the vocabulary may shift with prompt version or model. Whether a "run all 14 checks" enforcement actually lifts accuracy is untested directly; the ALE analysis shows rising ALE curves for continued checking, which supports but does not prove it.

## What other levers may also improve accuracy?

Premature stops overlap with the near-miss ceiling in the [hardest-classes memo](Hardest-Classes) (runner-up = expected). [Few-shot exemplars](Exemplar-Mining) teach the full-cascade completion pattern; [verification](Verification) tests whether the simulated gains hold when measured.


---
*Published via [Posit Cloud](https://connect.posit.cloud/jackjburleson/content/019fd440-9bbf-1a22-cf30-a36183d9c7d4) · [GitHub repo](https://github.com/Exios66/AMFAM_capstone)*
