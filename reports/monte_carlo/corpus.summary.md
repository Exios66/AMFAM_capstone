# Monte Carlo Corpus Summary

- **Records**: 5599
- **Images**: 1512
- **Experiments**: 18
- **Reasoning coverage**: 4580/5599 rows

## Status

| status | count |
|---|---:|
| completed | 5470 |
| error | 129 |

## Models

| model | rows |
|---|---:|
| google/gemini-2.5-flash-lite | 320 |
| google/gemini-3.5-flash-lite | 479 |
| moonshotai/kimi-k2.6 | 109 |
| qwen/qwen3.5-35b-a3b | 212 |
| qwen/qwen3.7-flash | 4479 |

## Prompt versions

| prompt | rows |
|---|---:|
| v0 | 1759 |
| v11.8 | 2561 |
| v14 | 160 |
| v16 | 480 |
| v17 | 160 |
| v18 | 160 |
| v18.1 | 319 |

## Top confusion pairs

| expected->predicted | count |
|---|---:|
| `budget->invoice` | 63 |
| `letter->memo` | 63 |
| `specification->form` | 52 |
| `invoice->form` | 51 |
| `budget->form` | 40 |
| `handwritten->letter` | 34 |
| `scientific_report->form` | 34 |
| `resume->form` | 33 |
| `invoice->budget` | 28 |
| `file_folder->presentation` | 22 |
| `presentation->news_article` | 19 |
| `presentation->file_folder` | 19 |
| `scientific_report->scientific_publication` | 19 |
| `scientific_publication->news_article` | 18 |
| `questionnaire->form` | 17 |
| `news_article->advertisement` | 16 |
| `presentation->scientific_report` | 16 |
| `presentation->memo` | 14 |
| `questionnaire->scientific_report` | 14 |
| `scientific_publication->scientific_report` | 13 |
