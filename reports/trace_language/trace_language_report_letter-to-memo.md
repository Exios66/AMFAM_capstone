# Trace-Language Analysis of Reasoning Traces

- **Corpus rows (reasoning-covered)**: 45 (45 failed, 0 correct)
- **Scope**: letter-to-memo
- **Word tokenization**: content words (stopwords removed); phrase tokenization keeps function words for loop detection
- **Dirichlet prior** a = 0.01 (symmetric pseudo-count)

## Differential Phrase Nets

![Differential phrase net](phrase_net_differential_letter-to-memo.png)

Directed bi-gram graph of the reasoning traces, restricted to edges whose prevalence in **failed** traces exceeds their prevalence in **correct** traces (log-odds difference ≥ threshold, ≥ min failed occurrences). The differential filter removes the corporate boilerplate and prompt-leaked tokens shared with correct traces, leaving the phrases characteristic of reasoning breakdowns. Diamond-outlined nodes are **prompt-leaked** tokens — words the model parrots from the prompt text itself. Red edges are structural loops.

### Top failure-biased bi-grams

| Bi-gram | Failed n | Correct n | z |
|---|---:|---:|---:|

**0 of 0 differential edges are prompt-leaked** (both words appear in the prompt text) — the model failing while reciting its own instructions.

### Structural loops

0 cycles detected (length ≤ 6). Full inventory with example traces: [phrase_net_loops_letter-to-memo.md](../../reports/trace_language/phrase_net_loops_letter-to-memo.md).

| Cycle | Length |
|---|---:|

### Stuck phrases per trace

Back-to-back phrase repetition (`A B A B` or `A B C A B C`):

| Group | Traces | Looping traces | Rate |
|---|---:|---:|---:|
| Failed | 45 | 7 | 15.6% |
| Correct | 0 | 0 | 0.0% |

## Log-Odds Ratio (Uninformative Dirichlet Prior)

![Log-odds bar chart](logodds_dirichlet_letter-to-memo.png)

Fightin' Words (Monroe, Colaresi & Quinn, 2008): `z = log((y_f + a)/(n_f - y_f + a)) - log((y_o + a)/(n_o - y_o + a))` with the symmetric prior a on every count. Positive z = word is more likely to appear in a failed trace; negative z = more likely in a correct trace. Words shared across both classes (boilerplate, prompt-leaked labels) sit near z = 0 and drop out of the extremes.

### Top 30 words most likely in FAILED traces

| word | failed n | correct n | z |
|---|---:|---:|---:|

### Top 30 words most likely in CORRECT traces

| word | failed n | correct n | z |
|---|---:|---:|---:|
| titled | 5 | 0 | -8.40 |
| sense | 5 | 0 | -8.40 |
| costs | 5 | 0 | -8.40 |
| article | 5 | 0 | -8.40 |
| paper | 5 | 0 | -8.40 |
| cigarettes | 5 | 0 | -8.40 |
| section | 5 | 0 | -8.40 |
| perfetti | 5 | 0 | -8.40 |
| taxes | 5 | 0 | -8.40 |
| change | 5 | 0 | -8.40 |
| recall | 5 | 0 | -8.40 |
| lorillard | 5 | 0 | -8.40 |
| carefully | 5 | 0 | -8.40 |
| under | 5 | 0 | -8.40 |
| evaluating | 5 | 0 | -8.40 |
| political | 5 | 0 | -8.40 |
| waste | 5 | 0 | -8.40 |
| liggett | 5 | 0 | -8.40 |
| options | 5 | 0 | -8.40 |
| capture | 5 | 0 | -8.40 |
| tub | 5 | 0 | -8.40 |
| rjrti | 5 | 0 | -8.40 |
| re-evaluating | 5 | 0 | -8.40 |
| efforts | 5 | 0 | -8.40 |
| jdb | 5 | 0 | -8.40 |
| scribble | 5 | 0 | -8.40 |
| memo's | 5 | 0 | -8.40 |
| functionally | 5 | 0 | -8.40 |
| aided | 5 | 0 | -8.40 |
| refine | 5 | 0 | -8.40 |

## Scattertext-style Frequency Scatter

![Scattertext-style scatter](scattertext_style_letter-to-memo.png)

Every word on a log-log grid of frequency-per-million-tokens in correct (x) vs failed (y) traces. The **top-left corner** isolates hallmark failure language; the **bottom-right corner** the words driving successful classification. Words near the diagonal are class-neutral (both the prompt template and document text are shared across both classes).
