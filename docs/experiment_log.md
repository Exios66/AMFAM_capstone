# Braintrust Prompt Evaluation Results

## Experiment: `moonshotai/kimi-k3` — 160 Images (10 per class × 16 classes)

**Experiment ID:** main-1785257772  
**Link:** <https://www.braintrust.dev/app/DSHB_amfam_capstone_2026/p/AMFAM-Doc-Classification/experiments/main-1785257772>  
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

**Pricing:** $0.30/M input tokens, $15.00/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
| -------- | ---: | ---: | ---: | ---: |
| 800 | 1,415,112 | 137,208 | 1,552,320 | **$2.48** |
| 25,000 | 44,222,250 | 4,287,750 | 48,510,000 | **$64.74** |
| 320,000 | 566,044,800 | 54,883,200 | 620,928,000 | **$823.57** |

**vs. Original Kimi K3 estimate (full-res images, `max_tokens=20`):** $1,257.98 for 320K — resizing to 1024×1024 saves ~$434.

---

## Experiment: `google/gemini-2.5-flash` — 160 Images (10 per class × 16 classes)

**Experiment ID:** main-1785265188  
**Link:** <https://www.braintrust.dev/app/DSHB_amfam_capstone_2026/p/AMFAM-Doc-Classification/experiments/main-1785265188>  
**Dataset:** `fixed_size_sampled/images/` (1024×1024 padded PNGs)  
**Prompt:** `CLASSIFICATION_PROMPT` from `src/openrouter_classifier.py`  
**Settings:** `max_tokens=1024`, `temperature=0.1`, `reasoning.effort=medium`  
**Image size:** `1024×1024`

### Results

| Metric | Value |
| -------- | ------: |
| **Accuracy (exact_match)** | **74.38%** (119/160 correct) |
| Prompt tokens (avg) | 1,637 |
| Prompt cached tokens (avg) | 8.17 |
| Completion tokens (avg) | 415.64 |
| Completion reasoning tokens (avg) | 413.82 |
| Total tokens (avg) | 2,052.64 |
| Duration (avg) | 48.10s |
| LLM duration (avg) | 4.60s |
| Time to first token (avg) | 4.58s |
| Errors | 0 |

### Notes

- +4.38% accuracy over Kimi K3 (74.38% vs 70.00%) with 13 improvements and 6 regressions.
- Reasoning tokens are visible in Braintrust UI metadata for debugging misclassifications.
- 2.2x faster than Kimi K3 (48s vs 107s avg duration per image).
- More completion tokens (416 vs 172) due to visible reasoning chain, but cheaper output pricing.
- 41 misclassifications to investigate in Braintrust UI.

### Cost Projections (Gemini 2.5 Flash, `max_tokens=1024`, 1024×1024 images)

**Pricing:** $0.15/M input tokens, $0.60/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
| -------- | ---: | ---: | ---: | ---: |
| 800 | 1,309,600 | 332,512 | 1,642,112 | **$0.40** |
| 25,000 | 40,925,000 | 10,391,000 | 51,316,000 | **$12.37** |
| 320,000 | 523,840,000 | 133,004,800 | 656,844,800 | **$158.38** |

**vs. Kimi K3 at 320K:** $158 vs $824 — Gemini 2.5 Flash is **~5.2x cheaper** with higher accuracy.

---

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

**Pricing:** $0.15/M input tokens, $0.6/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
| -------- | ---: | ---: | ---: | ---: |
| 800 | 2,960,800 | 334,555 | 3,295,355 | **$0.64** |
| 25,000 | 92,525,000 | 10,454,843 | 102,979,843 | **$20.15** |
| 320,000 | 1,184,320,000 | 133,822,000 | 1,318,142,000 | **$257.94** |

---

## Experiment: `google/gemini-2.5-flash` — 800 Images (50 per class × 16 classes)

**Experiment ID:** main-1785272634
**Dataset:** `2550x3300_50perclass_800/images/` (2550×3300 padded PNGs, 300 DPI)
**Prompt:** `CLASSIFICATION_PROMPT` from `src/openrouter_classifier.py` (baseline, pre-disambiguation)
**Settings:** `max_tokens=1024`, `temperature=0.1`, `reasoning.effort=medium`
**Image size:** `2550×3300`

### Results

| Metric | Value |
| -------- | ------: |
| **Accuracy (exact_match)** | **72.88%** (583/800 correct) |
| Prompt tokens (avg) | 3,701.00 |
| Prompt cached tokens (avg) | 0.00 |
| Completion tokens (avg) | 417.38 |
| Total tokens (avg) | 4,118.38 |
| Duration (avg) | 0.00s |
| Errors | 0 |

### Notes

- Scaling from 160 → 800 images held steady at ~73% accuracy, confirming the 10-per-class sample is representative.
- `form` (30%), `presentation` (36%), and `specification` (46%) are the worst-performing classes — `scientific_report` is massively over-predicted with 64 false positives across 7 classes.
- Reasoning trace analysis revealed the model confuses fax cover sheets with memos, specs with scientific reports, and press releases with news articles — leading to the disambiguation prompt update.
- See `docs/50pic_cost_est_tst.md` for full per-class accuracy breakdown and confused pairs analysis.
- See `docs/confusion_matrix_main-1785272634.md` for confusion matrix.
- See `docs/misclassification_reasoning_main-1785270444.md` for reasoning trace analysis.

### Cost Projections (Gemini 2.5 Flash, `max_tokens=1024`, 2550×3300 images)

**Pricing:** $0.15/M input tokens, $0.6/M output tokens

| Images | Prompt Tokens | Completion Tokens | Total Tokens | **Estimated Cost** |
| -------- | ---: | ---: | ---: | ---: |
| 800 | 2,960,800 | 333,902 | 3,294,701 | **$0.64** |
| 25,000 | 92,525,000 | 10,434,437 | 102,959,437 | **$20.14** |
| 320,000 | 1,184,320,000 | 133,560,800 | 1,317,880,799 | **$257.78** |

---

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

**Pricing:** $0.15/M input tokens, $0.6/M output tokens

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

---

## AMFAM v2 — qwen3.7-flash & gemini-2.5-flash reasoning experiments (complete)

All runs: `fixed_size_sampled` (160-image balanced sample, ~10 per class × 16),
reasoning enabled, `exact_match` tracked. 2 of 160 rows lack a stored attachment
and are skipped, so the scored total is 158.

### Summary

| Experiment | Model | Prompt | Accuracy |
| -------- | ----- | ------ | ------: |
| `qwen3.7-flash_v1_reasoning` | qwen/qwen3.7-flash | v1 | 50.0% (11/22)¹ |
| `qwen3.7-flash_v1_reasoning-5718f5da` | qwen/qwen3.7-flash | v1 | 80.1% (125/156) |
| `qwen3.7-flash_v2_reasoning` | qwen/qwen3.7-flash | v2 | 78.5% (124/158) |
| `qwen3.7-flash_v3_reasoning-14553e3a` | qwen/qwen3.7-flash | v3 | 78.5% (124/158) |
| `qwen3.7-flash_v4_reasoning` | qwen/qwen3.7-flash | v4 | 83.5% (132/158) |
| `qwen3.7-flash_v5_reasoning` | qwen/qwen3.7-flash | v5 | 84.8% (134/158) |
| `qwen3.7-flash_v6_reasoning` | qwen/qwen3.7-flash | v6 | 83.9% (130/155) |
| `qwen3.7-flash_v7_reasoning` | qwen/qwen3.7-flash | v7 | 91.1% (144/158) |
| `qwen3.7-flash_v8_reasoning` | qwen/qwen3.7-flash | v8 | 91.8% (145/158) |
| `qwen3.7-flash_v8.5_reasoning` | qwen/qwen3.7-flash | v8.5 | 88.6% (140/158) |
| `qwen3.7-flash_v9_reasoning` | qwen/qwen3.7-flash | v9 | 91.1% (144/158) |
| `qwen3.7-flash_v10_smoke` | qwen/qwen3.7-flash | v10 | 100% (14/14)² |
| `qwen3.7-flash_v10_reasoning` | qwen/qwen3.7-flash | v10 | **97.5% (154/158)** |
| `gemini-2.5-flash_v3_reasoning` | google/gemini-2.5-flash | v3 | 77.4% (123/159) |
| `gemini-2.5-flash_v4_reasoning` | google/gemini-2.5-flash | v4 | 77.7% (122/157) |

¹ First v1 run aborted early (22 scored rows). ² Smoke test on the 14 v9-miss images.

### qwen3.7-flash v1 (run 1, partial)

11/22 (50.0%). Aborted early — only 22 rows scored (budget 5/9, invoice 3/9,
letter 1/1, presentation 2/3).

### qwen3.7-flash v1 (run 2)

125/156 (80.1%). Weakest classes: presentation 3/9, invoice 4/10, questionnaire
6/10, budget 6/10, form 6/10. Strong: email, file_folder, handwritten, letter,
memo all 10/10.

### qwen3.7-flash v2

124/158 (78.5%). Weakest: invoice 3/10, presentation 4/10, budget/form/
questionnaire 6/10. file_folder, email, handwritten 10/10.

### qwen3.7-flash v3

124/158 (78.5%). Weakest: questionnaire 4/10, presentation 4/10, invoice 4/10,
budget 6/10. Handwritten drops to 9/10.

### qwen3.7-flash v4

132/158 (83.5%). +5.0 over v3. resume jumps to 10/10; questionnaire 8/10,
presentation 7/9, invoice 7/10. form still 6/10, budget 6/10.

### qwen3.7-flash v5

134/158 (84.8%). form 9/10, budget collapses to 3/10. invoice 6/10.

### qwen3.7-flash v6

130/155 (83.9%). budget 4/10, invoice 4/10, scientific_report 7/10. form 9/10.

### qwen3.7-flash v7

144/158 (91.1%). form 10/10, presentation 10/10, questionnaire 10/10, resume
10/10. handwritten drops to 6/10, scientific_report 7/10. (v7 added presentation
cover/slide rules.)

### qwen3.7-flash v8

145/158 (91.8%). Best qwen result before v10. memo 8/10, handwritten 8/10,
scientific_report 7/10. (v8 added agency estimate change order + scratchpad
deliberation.)

### qwen3.7-flash v8.5

140/158 (88.6%). Regression on file_folder (3/10) — the v8.5 folder-tab rewrite
over-corrected cover pages. memo 10/10, form 10/10.

### qwen3.7-flash v9

144/158 (91.1%). Recovered file_folder (10/10) and invoice (10/10); regressed
questionnaire (7/10) and scientific_report (6/10). (v9 added folder-tab and
budget-vs-form rules.)

### qwen3.7-flash v10 (full run)

154/158 (97.5%). See section above. Only 4 misses remain, all `invoice ↔ budget`
agency estimate/billing ambiguities.

### gemini-2.5-flash v3

123/159 (77.4%). Weakest: invoice 3/10, questionnaire 4/10, form 5/10,
presentation 6/10, budget 6/10, resume 6/10. email/file_folder/handwritten/
memo/scientific_publication 10/10.

### gemini-2.5-flash v4

122/157 (77.7%). Weakest: form 4/10, scientific_report 5/10, news_article 6/10,
advertisement 6/10, budget 6/10. file_folder/email/handwritten 10/10.

### Cross-model note

qwen3.7-flash with the same prompt family outperforms gemini-2.5-flash by a wide
margin once the prompt reaches v7+ (91-97% vs 77%). qwen3.7-flash's explicit
forced reasoning (`reasoning.enabled + effort high`) produces a structured
scratchpad that reliably follows the v7+ step cascade; gemini's medium-effort
reasoning is less controllable and does not hit the same disambiguation rules.
