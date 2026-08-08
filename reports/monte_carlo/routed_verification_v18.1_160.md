# Routed Verification: Base vs Confidence-Gated Escalation

- **Base run**: `qwen3.7-flash_v18.1_high_160.jsonl` — 159 rows, accuracy 0.962, cost $0.0617
- **Escalation run**: `qwen3.7-flash_gemini-2.5-pro_v18.1_routed10_160.jsonl` — 15 rows (3 predictions changed), accuracy 0.800, cost $0.4018

## Merged pipeline

| metric | value |
|---|---:|
| rows | 159 |
| merged accuracy | 0.943 |
| base accuracy | 0.962 |
| **delta vs base** | **-0.019** |
| merged cost | $0.4635 |
| cost factor vs base | 7.51x |
| escalation tail accuracy | 0.800 (12/15) |

**Memo reference** (`reports/monte_carlo/routing_abstention.md`): simulated +4.3pp at alpha=10% assumes the escalated model is genuinely stronger.

## Escalated flips (base label -> escalated label)

0 of 3 escalated rows flipped to the CORRECT label.

| filename | expected | base | escalated | fixed? |
|---|---|---|---|---|
| `test_imagesj_j_p_s_jps20f00_0000954900.tif.png` | `memo` | memo | specification | no |
| `test_imagest_t_q_y_tqy07d00_tnwl0000798.tif.png` | `budget` | budget | handwritten | no |
| `test_imagesw_w_z_j_wzj74c00_81190731_0743.tif.png` | `scientific_report` | scientific_report | presentation | no |

## Per-class merged accuracy

| class | correct | total | accuracy |
|---|---:|---:|---:|
| advertisement | 9 | 9 | 1.000 |
| budget | 9 | 10 | 0.900 |
| email | 10 | 10 | 1.000 |
| file_folder | 10 | 10 | 1.000 |
| form | 8 | 10 | 0.800 |
| handwritten | 10 | 10 | 1.000 |
| invoice | 6 | 10 | 0.600 |
| letter | 10 | 10 | 1.000 |
| memo | 9 | 10 | 0.900 |
| news_article | 9 | 9 | 1.000 |
| presentation | 10 | 10 | 1.000 |
| questionnaire | 10 | 10 | 1.000 |
| resume | 10 | 10 | 1.000 |
| scientific_publication | 11 | 11 | 1.000 |
| scientific_report | 9 | 10 | 0.900 |
| specification | 10 | 10 | 1.000 |
