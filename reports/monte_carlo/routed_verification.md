# Routed Verification: Base vs Confidence-Gated Escalation

- **Base run**: `qwen3.7-flash_v19_high_160.jsonl` — 159 rows, accuracy 0.975, cost $0.0599
- **Escalation run**: `qwen3.7-flash_gemini-2.5-pro_v19_routed10_160.jsonl` — 15 rows (1 predictions changed), accuracy 0.933, cost $0.4077

## Merged pipeline

| metric | value |
|---|---:|
| rows | 159 |
| merged accuracy | 0.969 |
| base accuracy | 0.975 |
| **delta vs base** | **-0.006** |
| merged cost | $0.4675 |
| cost factor vs base | 7.81x |
| escalation tail accuracy | 0.933 (14/15) |

**Memo reference** (`reports/monte_carlo/routing_abstention.md`): simulated +4.3pp at alpha=10% assumes the escalated model is genuinely stronger.

## Escalated flips (base label -> escalated label)

0 of 1 escalated rows flipped to the CORRECT label.

| filename | expected | base | escalated | fixed? |
|---|---|---|---|---|
| `test_imagesw_w_z_j_wzj74c00_81190731_0743.tif.png` | `scientific_report` | scientific_report | presentation | no |

## Per-class merged accuracy

| class | correct | total | accuracy |
|---|---:|---:|---:|
| advertisement | 9 | 9 | 1.000 |
| budget | 10 | 10 | 1.000 |
| email | 10 | 10 | 1.000 |
| file_folder | 10 | 10 | 1.000 |
| form | 9 | 10 | 0.900 |
| handwritten | 10 | 10 | 1.000 |
| invoice | 7 | 10 | 0.700 |
| letter | 10 | 10 | 1.000 |
| memo | 10 | 10 | 1.000 |
| news_article | 9 | 9 | 1.000 |
| presentation | 10 | 10 | 1.000 |
| questionnaire | 10 | 10 | 1.000 |
| resume | 10 | 10 | 1.000 |
| scientific_publication | 11 | 11 | 1.000 |
| scientific_report | 9 | 10 | 0.900 |
| specification | 10 | 10 | 1.000 |
