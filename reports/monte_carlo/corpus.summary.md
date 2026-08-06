# Monte Carlo Corpus Summary

- **Records**: 4641
- **Images**: 1512
- **Experiments**: 14
- **Reasoning coverage**: 3113/4641 rows

## Status

| status | count |
|---|---:|
| completed | 4520 |
| error | 121 |

## Models

| model | rows |
|---|---:|
| google/gemini-2.5-flash-lite | 160 |
| moonshotai/kimi-k2.6 | 109 |
| qwen/qwen3.5-35b-a3b | 212 |
| qwen/qwen3.7-flash | 4160 |

## Prompt versions

| prompt | rows |
|---|---:|
| v0 | 1280 |
| v11.8 | 2561 |
| v14 | 160 |
| v16 | 480 |
| v17 | 160 |

## Top confusion pairs

| expected->predicted | count |
|---|---:|
| `letter->memo` | 53 |
| `budget->invoice` | 52 |
| `invoice->form` | 41 |
| `specification->form` | 41 |
| `budget->form` | 33 |
| `scientific_report->form` | 23 |
| `invoice->budget` | 22 |
| `resume->form` | 21 |
| `handwritten->letter` | 19 |
| `questionnaire->form` | 16 |
| `presentation->file_folder` | 16 |
| `presentation->scientific_report` | 15 |
| `file_folder->presentation` | 15 |
| `scientific_report->scientific_publication` | 15 |
| `presentation->news_article` | 14 |
| `scientific_publication->news_article` | 14 |
| `scientific_publication->scientific_report` | 13 |
| `file_folder->form` | 12 |
| `news_article->advertisement` | 11 |
| `scientific_report->specification` | 11 |
