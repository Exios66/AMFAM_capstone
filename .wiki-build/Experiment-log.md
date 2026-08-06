## Experiment: `moonshotai/kimi-k3` — 160 Images (10 per class × 16 classes)

**Experiment ID:** main-1785257772  
**Link:** <https://www.braintrust.dev/app/DSHB_amfam_capstone_2026/*p*/AMFAM-Doc-Classification/experiments/main-1785257772>  
**Dataset:** `fixed_size_sampled/images/` (1024×1024 padded PNGs)  
**Prompt:** `CLASSIFICATION_PROMPT` from `src/openrouter_classifier.py`  
**Settings:** `max_tokens=500`, `temperature=0.1`
**image size:** `1024×1024`

### Results

| Metric | Value |
| -------- | ------: |
| **Accuracy (exact_match)** | **70.00%** (112/160 correct) |
| Prompt tokens (avg) | 1,768.89 |
| Prompt cached tokens (avg) | 872.80 |
| Completion tokens (avg) | 171.51 |
| Completion reasoning tokens (avg) | 156.02 |
| Total tokens (avg) | 1,940.41 |
| Duration (avg) | 106.74s |
| LLM duration (avg) | 10.08s |
| Time to first token (avg) | 10.06s |
| Errors | 0 |

### Notes

- First run (main-1785255418) scored 0% due to `max_tokens=20` — reasoning model used all tokens on hidden reasoning, leaving nothing for output.
- Bumping to `max_tokens=500` resolved the issue.
- ~156 of ~171 completion tokens are hidden reasoning tokens (not visible in output).
- 48 misclassifications need investigation in Braintrust UI to identify confused class pairs.
- Images resized to 1024×1024 (vs original full-res) significantly reduces prompt tokens (1,769 vs 11,996 in original test).

### Cost Projections (Kimi K3, `max_tokens=500`, 1024×1024 images)

**Pricing:** $0.30/*M* input tokens, $15.00/*M* output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
| -------- | ---: | ---: | ---: | ---: |
| 800 | 1,415,112 | 137,208 | 1,552,320 | **$2.48** |
| 25,000 | 44,222,250 | 4,287,750 | 48,510,000 | **$64.74** |
| 320,000 | 566,044,800 | 54,883,200 | 620,928,000 | **$823.57** |

**vs. Original Kimi K3 estimate (full-res images, `max_tokens=20`):** $1,257.98 for 320K — resizing to 1024×1024 saves ~$434.


## Experiment: `google/gemini-2.5-flash` — 160 Images (10 per class × 16 classes)

**Experiment ID:** main-1785270444
**Dataset:** `2550x3300_10perclass_160/images/` (2550×3300 padded PNGs, 300 DPI)
**Prompt:** `CLASSIFICATION_PROMPT` from `src/openrouter_classifier.py`
**Settings:** `max_tokens=1024`, `temperature=0.1`, `reasoning.effort=medium`
**Image size:** `2550×3300`

### Results

| Metric | Value |
| -------- | ------: |
| **Accuracy (exact_match)** | **73.75%** (118/160 correct) |
| Prompt tokens (avg) | 3,701.00 |
| Prompt cached tokens (avg) | 0.00 |
| Completion tokens (avg) | 418.19 |
| Total tokens (avg) | 4,119.19 |
| Duration (avg) | 0.00s |
| Errors | 0 |

### Notes

- Switching from 1024×1024 to full-res 2550×3300 doubled prompt tokens (1,637 → 3,701) but accuracy dropped slightly (74.38% → 73.75%), suggesting higher resolution does not help and may add noise.
- Cost per image roughly doubled vs 1024×1024 ($0.64 vs $0.40 for 800 images) with no accuracy gain — 1024×1024 is the better cost/performance tradeoff.

### Cost Projections (Gemini 2.5 Flash, `max_tokens=1024`, 2550×3300 images)

**Pricing:** $0.15/*M* input tokens, $0.6/*M* output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
| -------- | ---: | ---: | ---: | ---: |
| 800 | 2,960,800 | 334,555 | 3,295,355 | **$0.64** |
| 25,000 | 92,525,000 | 10,454,843 | 102,979,843 | **$20.15** |
| 320,000 | 1,184,320,000 | 133,822,000 | 1,318,142,000 | **$257.94** |


## Experiment: `google/gemini-2.5-flash` — 160 Images (10 per class × 16 classes)

**Experiment ID:** main-1785277280
**Dataset:** 2550×3300 padded PNGs, 300 DPI
**Prompt:** `CLASSIFICATION_PROMPT` from `src/openrouter_classifier.py`
**Settings:** `max_tokens=1024`, `temperature=0.1`, `reasoning.effort=medium`
**Image size:** `2550×3300`

### Results

| Metric | Value |
| -------- | ------: |
| **Accuracy (exact_match)** | **83.75%** (134/160 correct) |
| Prompt tokens (avg) | 4,368.00 |
| Prompt cached tokens (avg) | 0.00 |
| Completion tokens (avg) | 412.39 |
| Total tokens (avg) | 4,780.39 |
| Duration (avg) | 0.00s |
| Errors | 0 |

### Cost Projections (Gemini 2.5 Flash, `max_tokens=1024`, 2550×3300 images)

**Pricing:** $0.15/*M* input tokens, $0.6/*M* output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
| -------- | ---: | ---: | ---: | ---: |
| 800 | 3,494,400 | 329,915 | 3,824,315 | **$0.72** |
| 25,000 | 109,200,000 | 10,309,843 | 119,509,843 | **$22.57** |
| 320,000 | 1,397,760,000 | 131,966,000 | 1,529,726,000 | **$288.84** |

### Notes

- **+10% accuracy jump** (73.75% → 83.75%) from adding disambiguation rules to the prompt — largest single improvement across all experiments.
- Prompt tokens increased from 3,701 → 4,368 due to longer prompt with disambiguation rules, but the accuracy gain far outweighs the ~$0.08 cost increase per 800 images.
- Only 26 errors remain (down from 42). Top confusion is now `presentation → file_folder` (4 errors) where cover/divider pages get misclassified.
- See `docs/confusion_matrix_main-1785277280.md` and `docs/misclassification_reasoning_main-1785277280.md` for detailed breakdown.

## v10 (qwen3.7-flash, reasoning enabled)

Prompt v10 is the full v9 ruleset plus new disambiguation rules covering every v9
miss AND every v8.5→v9 regression:
- questionnaire vs presentation (v9 misses: 2), questionnaire vs handwritten,
  resume vs scientific_report, scientific_report vs budget/email/form/presentation,
  memo vs letter, budget vs invoice, handwritten vs form, advertisement vs
  news_article.

### v10 smoke (14 v9-miss images)

| Metric | Value |
| -------- | ------: |
| **Accuracy (exact_match)** | **100%** (14/14 correct) |

All 13 prompt-related v9 misses now correct. The 14th case
(news_article→scientific_publication, `test_imagesr_r_c_s_rcs96d00_...`) was a
dataset mislabel — an American Journal of Epidemiology reprint (Vol. 119, No. 4,
1984) — ground truth flipped to `scientific_publication`; v10 predicts it
correctly.

### v10 full run (160-image `fixed_size_sampled`)

| Metric | Value |
| -------- | ------: |
| **Accuracy (exact_match)** | **97.5%** (154/158 correct) |

Per-class (of ~10 per class; 2 rows without a stored attachment are skipped):

| Class | Correct/Total | | Class | Correct/Total |
| ------ | --: | -- | ------ | --: |
| advertisement | 9/9 | | news_article | 9/9 |
| budget | 9/10 | | presentation | 10/10 |
| email | 9/9 | | questionnaire | 10/10 |
| file_folder | 10/10 | | resume | 10/10 |
| form | 10/10 | | scientific_publication | 11/11 |
| handwritten | 10/10 | | scientific_report | 10/10 |
| invoice | 7/10 | | specification | 10/10 |
| letter | 10/10 | | memo | 10/10 |

Remaining 4 misses (all `invoice ↔ budget`):
- `qia17d00` — Tobacco Institute check + detachable "INVOICE" stub (state campaign
  contribution): predicted invoice, expected budget.
- `dav40c00`, `wce83f00`, `ynj47c00` — "ESTIMATE CHANGE ORDER" / "PRODUCTION
  ESTIMATE REPORT" / "NEWSPAPER ESTIMATE RECAP": predicted budget, expected
  invoice.

No memo↔invoice confusion in the final run (memo 10/10, letter 10/10). The
residual error class is agency/vendor estimate-vs-bill (budget vs invoice).

### Notes

- Experiments `qwen3.7-flash_v10_smoke` and `qwen3.7-flash_v10_reasoning` on Braintrust.


## v11.7 (qwen3.7-flash) — minimal edit set D + A + B

v11.7 = v11.6 + a deliberately minimal 3-edit set (D, A, B — C and E skipped
to reduce regression risk):

- **Edit D** — check 7 structural split between voucher/check-stub (budget) and
  vendor billing with amounts/totals (invoice).
- **Edit A** — check 8 adds: a labeled product/parameter rate-data chart
  (rates/units per product or parameter) is a specification.
- **Edit B** — check 10 adds a standalone-chart carve-out: a financial/money
  chart with no other document signals is budget; an unlabeled standalone
  chart/table is a presentation slide.

### v11.7 full-run results

| Run | Accuracy |
| -------- | ------: |
| 160-image `qwen3.7-flash_v11_7_reasoning_160` | **98.1%** (156/159) |
| 56-row eval `qwen3.7-flash_v11_7_eval` | **35.7%** (20/56) |

v11.7 is the first 16-class prompt to exceed 35% on the eval set
(v11.5 = 16/56, v11.6 = 17/56). Its 3 misses on the 160 set:

- **`yvp54d00` — form → budget:** a "MILWAUKEE ADVERTISING CLUB" document
  requesting authorization of $690,000; the budget money-only rule catches the
  bare figure.
- **`cpt85d00` — letter → memo:** correspondence to "Mr. T. E. Sandefur"; the
  by-name + no-TO:/FROM: pattern routes it to memo.
- **`tqi16e00` — budget → invoice:** the OUTDOOR ESTIMATE RECAP bus-shelter
  planning recap (also a v11 miss).


## v11.9 (qwen3.7-flash) — narrow Edit B's financial-chart→budget carve-out

v11.9 = v11.8 + three edits that narrow Edit B so titled/designed deck charts
no longer fall into budget:

- **Edit 1** — check 10 carve-out narrowed: a product/parameter rate-data
  chart → specification; a research/measurement chart → scientific_report; a
  financial/money chart → budget **only when it is a standalone data table
  used for money planning or tracking**; a titled, designed deck chart stays
  presentation (check 9).
- **Edit 2** — check 9 hardened: a titled/designed deck chart IS a
  presentation slide; don'*t* route it to budget.
- **Edit 3** — calibration line: deck charts → presentation, product/parameter
  charts → specification.

### v11.9 full-run results

| Run | Accuracy |
| -------- | ------: |
| 56-row eval `qwen3.7-flash_v11_9_eval` | **35.7%** (20/56) |

Ties v11.7's best eval score and is +2 over v11.8's 18/56. The two
presentation→budget regressions introduced by Edit B in v11.8 are recovered,
plus two bonus fixes:

- ✓ `rvl_cdip__presentation__0001.png` — presentation → budget → **presentation**
- ✓ `rvl_cdip__presentation__0011.png` — presentation → budget → **presentation**
- ✓ `test_imagesj_j_e_d_jed71e00...` — form → presentation → **form** (this is
  also the one remaining 160-set miss in v11.8)
- ✓ `rvl_cdip__questionnaire__0016.png` — questionnaire → handwritten → **questionnaire**

Two rows regressed against v11.8:

- ✗ `rvl_cdip__form__0005.png` — form → invoice (a Fix-1 success in v11.8,
  lost in v11.9)
- ✗ `rvl_cdip__news_article__0008.png` — news_article → memo (new miss; was
  correct in v11.7 and v11.8)

Three rows remain misses but shifted prediction: `advertisement__0015`
(form→handwritten), `presentation__0013` (memo→letter),
`scientific_report__0016` (specification→form). The 5 `letter → memo` eval
misses are unchanged. **v11.9 recovers the Edit B presentation regression while
holding v11.8's 160-set fix, so the next eval benchmark is the 480-image run
(queued) to confirm the generalization holds.**

### v11.8 on the 320-image set — `qwen3.7-flash_v11_8_reasoning_320`

| Metric | Value |
| -------- | ------: |
| **Accuracy (exact_match)** | **87.2%** (279/320) |

Per-class (20/class):

| Class | Correct/Total | | Class | Correct/Total |
| ------ | --: | -- | ------ | --: |
| advertisement | 18/20 | | news_article | 18/20 |
| budget | 16/20 | | presentation | 16/20 |
| email | 20/20 | | questionnaire | 17/20 |
| file_folder | 17/20 | | resume | 20/20 |
| form | 17/20 | | scientific_publication | 17/20 |
| handwritten | 18/20 | | scientific_report | 16/20 |
| invoice | 16/20 | | specification | 18/20 |
| letter | 15/20 | | memo | 20/20 |

v11.8 on the noisy 320 set is 87.2% vs v11's 83.9% (+3.3 *pp*) — strong
generalization of the 160-set improvement. Biggest per-class gains:

- **budget** 13/20 → 16/20 (+3)
- **form** 14/20 → 17/20 (+3)
- **specification** 15/20 → 18/20 (+3)
- **presentation** 14/20 → 16/20 (+2)
- **invoice** 15/20 → 16/20 (+1), **memo** 19/20 → 20/20 (+1)

Small losses: **file_folder** 18/20 → 17/20 (−1), **handwritten** 19/20 → 18/20
(−1), **scientific_publication** 18/20 → 17/20 (−1).

### v11.8 on the 480-image set — `qwen3.7-flash_v11_8_reasoning_480`

| Metric | Value |
| -------- | ------: |
| **Accuracy (exact_match)** | **89.1%** (424/476) |

Per-class (30/class; 4 rows unscored):

| Class | Correct/Total | | Class | Correct/Total |
| ------ | --: | -- | ------ | --: |
| advertisement | 26/29 | | news_article | 27/29 |
| budget | 27/30 | | presentation | 25/30 |
| email | 28/29 | | questionnaire | 28/30 |
| file_folder | 26/30 | | resume | 29/32 |
| form | 27/30 | | scientific_publication | 27/30 |
| handwritten | 27/30 | | scientific_report | 24/30 |
| invoice | 24/30 | | specification | 27/30 |
| letter | 23/30 | | memo | 29/30 |

This is the first run on the 480 set (no v11 baseline). The 89.1% score holds
up well given the larger, noisier sample. Biggest miss buckets:

- **letter → memo (7):** the persistent v11.5+ TO:/FROM: memo-header issue
- **invoice → form (4), scientific_report → form (3):** form-layout pull
- **budget → invoice (3), invoice → budget (2):** residual estimate/billing
- **advertisement → presentation (3):** labeled chart routing
- **presentation → scientific_report (2), presentation → file_folder (2):**
  deck-chart misrouting


## Cross-model v11.8 runs — temperature/reasoning sweep on `fixed_size_sampled` (v1)

Three additional v11.8 runs on the original 160-image `fixed_size_sampled` slice plus one
retroactive run on the 52-row `qwen_v12_retroactive_eval` slice. All runs use the v11.8 prompt;
reasoning is set to each model family's maximum effort (qwen `high`, kimi `xhigh`, gemini `max`).

| Run | Dataset | Temp | Model | Accuracy |
|-----|---------|-----:|-------|---------:|
| `qwen3.7-flash_v11_8_reasoning_160_t0_3` | fixed_size_sampled | 0.3 | qwen3.7-flash | **98.7%** (157/159) |
| `qwen3.5-35b-a3b_v11_8_reasoning_160` | fixed_size_sampled | 0.1 | qwen3.5-35b-a3b | **98.7%** (155/157) |
| `qwen3.5-35b-a3b_v11_8_reasoning_v12retro` | qwen_v12_retroactive_eval | 0.1 | qwen3.5-35b-a3b | 30.8% (16/52) |
| `kimi-k2.6_v11_8_reasoning_160` | fixed_size_sampled | 0.1 | kimi-k2.6 | aborted (network outage) |
| `gemini-2.5-flash-lite_v11_8_reasoning_160` | fixed_size_sampled | 0.2 | gemini-2.5-flash-lite | **86.9%** (139/160) |

### qwen3.7-flash at temperature 0.3 — `qwen3.7-flash_v11_8_reasoning_160_t0_3`

Baseline comparison: v11.8 at temp 0.1 scored 157/158 (99.4%) on this slice. At temp 0.3 the
run scores **157/159 (98.7%)** with one row failing to produce content (`wat19d00`, no usable
output after retries). Both remaining misses are pre-existing v11.7-era rows:

- ✗ `jed71e00` — form → presentation (the long-standing deck-chart miss; also v11.8's only
  160-set miss at temp 0.1)
- ✗ `tqi16e00` — budget → invoice (OUTDOOR ESTIMATE RECAP; was fixed by v11.7/v11.8 at temp
  0.1, regressed back at 0.3)

So temperature 0.3 costs one regression on the budget/invoice boundary without recovering
`jed71e00`; net −0.7 *pp* vs temp 0.1 on scored rows.

### qwen3.5-35b-a3b (max reasoning) — `qwen3.5-35b-a3b_v11_8_reasoning_160`

First run of the hybrid-reasoning Qwen3.5-35B-A3B on this slice: **155/157 (98.7%)**, three rows
failed to produce usable content (`mvr50f00`, `iby31c00`, `umv76d00` — Qwen3.5 burns long
reasoning traces; retries grew max_tokens to 16k but still capped). Misses:

- ✗ `jed71e00` — form → presentation (same recurring miss)
- ✗ `noz90d00` — form → advertisement (new single error for this model)

### qwen3.5-35b-a3b on the v12 retroactive slice — `qwen3.5-35b-a3b_v11_8_reasoning_v12retro`

On the 52-row `qwen_v12_retroactive_eval` slice (all rows previously misclassified by v12),
qwen3.5-35b-a3b with v11.8 scores **16/52 (30.8%)**. Five rows errored with
`finish_reason=length` (`rvl_cdip__form__0005.png`, `rvl_cdip__invoice__0006.png`,
`rvl_cdip__presentation__0011.png`, `rvl_cdip__questionnaire__0005.png`,
`rvl_cdip__scientific_report__0016.png`). Notable: this slice is hard by construction (every
row is a known v12 miss), so the low absolute score is expected; the top confusion buckets are
letter → memo (5), scientific_report → form (4), budget/invoice and file_folder/presentation
pairs (2 each).

Full per-run artifacts: `reports/report_*_v11_8_*.md`, `reports/confusion_matrix_*_v11_8_*.{md,png}`,
`reports/misclassification_reasoning_*_v11_8_*.md`, `reports/per_class_accuracy_*_v11_8_*.png`.

### gemini-2.5-flash-lite (max reasoning) — `gemini-2.5-flash-lite_v11_8_reasoning_160`

Completed at **139/160 (86.9%)**, temperature 0.2, `reasoning.effort=max`. Notable: it is the
only one of the v11.8 runs with zero failed/empty rows. The miss profile is different from the
qwen family — heavy `→ specification` pull (memo 3, form 2, handwritten/letter/scientific_report
1 each) plus `scientific_publication → scientific_report` (2) and `budget → invoice` (2). The
`jed71e00` (form → presentation) miss that every qwen run made was NOT missed by gemini.

### kimi-k2.6 (xhigh reasoning) — `kimi-k2.6_v11_8_reasoning_160` (aborted)

Run was aborted mid-flight (~109/160 completed) due to a transient DNS/network outage against
`api.braintrust.dev` that crashed the Braintrust logging thread (no usable result row). The
manifest (`reports/manifests/eval_v11_8_kimi.jsonl`) preserves the completed rows if a rerun is
wanted; the experiment in Braintrust is partial and should not be used for comparisons.


## Experiment: `qwen/qwen3.7-flash` — 800 Images (50 per class × 16 classes)

**Experiment ID:** qwen3.7-flash_v0_reasoning_800-f0b6b2e4
**Dataset:** rvl_cdip_800, 1024×1024 grayscale padded PNGs
**Prompt:** `v0` from `src/prompts.py`
**Settings:** `max_tokens=8192`, `temperature=0.1`, `reasoning.effort=high`

### Results

| Metric | Value |
|--------|------:|
| **Accuracy (exact_match)** | **66.12%** (529/800 correct) |
| Prompt tokens (avg) | 741.1 |
| Prompt cached tokens (avg) | 0.0 |
| Completion tokens (avg) | 1,552.1 |
| Total tokens (avg) | 2,293.1 |
| Errors | 0 |

### Cost — Expected vs Actual

**Pricing:** $0.03/*M* input, $0.13/*M* output. Expected $0.1792 (list price × measured tokens); actual billed $0.1773 (+1.1%).

| Images | Expected Cost | Estimated Actual |
|--------|--------------:|-----------------:|
| 800 | $0.18 | $0.18 |
| 25,000 | $5.60 | $5.54 |
| 320,000 | $71.68 | $70.92 |

## Experiment: `qwen3.7-flash_v11.8_reasoning_1600_balanced_1120` — 1120 images (70 per class × 16 classes)

**Model:** `qwen/qwen3.7-flash`  
**Prompt:** `v11.8`  
**Dataset:** `rvl_cdip_1600`  

| Metric | Value |
|---|---:|
| **exact_match** | **925/1120 (82.6%)** |
| Failure rate | 0.0% |
| Near-miss | 72 (36.9% of misses) |
| Expected cost | $0.6815 |
| Actual cost | $0.4937 |


---
*Published via [Posit Cloud](https://connect.posit.cloud/jackjburleson/content/019fd440-9bbf-1a22-cf30-a36183d9c7d4) · [GitHub repo](https://github.com/Exios66/AMFAM_capstone)*
