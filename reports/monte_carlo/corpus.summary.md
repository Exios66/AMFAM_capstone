# Monte Carlo Corpus Summary

- **Records**: 5280
- **Images**: 1512
- **Experiments**: 17
- **Reasoning coverage**: 3889/5280 rows

## Status

| status | count |
|---|---:|
| completed | 5151 |
| error | 129 |

## Models

| model | rows |
|---|---:|
| google/gemini-2.5-flash-lite | 320 |
| google/gemini-3.5-flash-lite | 160 |
| moonshotai/kimi-k2.6 | 109 |
| qwen/qwen3.5-35b-a3b | 212 |
| qwen/qwen3.7-flash | 4479 |

## Prompt versions

| prompt | rows |
|---|---:|
| v0 | 1440 |
| v11.8 | 2561 |
| v14 | 160 |
| v16 | 480 |
| v17 | 160 |
| v18 | 160 |
| v18.1 | 319 |

## Top confusion pairs

| expected->predicted | count |
|---|---:|
| `budget->invoice` | 60 |
| `letter->memo` | 58 |
| `specification->form` | 49 |
| `invoice->form` | 47 |
| `budget->form` | 36 |
| `scientific_report->form` | 30 |
| `invoice->budget` | 28 |
| `resume->form` | 25 |
| `handwritten->letter` | 24 |
| `file_folder->presentation` | 18 |
| `presentation->file_folder` | 18 |
| `presentation->news_article` | 17 |
| `scientific_publication->news_article` | 16 |
| `questionnaire->form` | 16 |
| `scientific_report->scientific_publication` | 16 |
| `presentation->scientific_report` | 15 |
| `news_article->advertisement` | 14 |
| `scientific_publication->scientific_report` | 13 |
| `file_folder->form` | 13 |
| `questionnaire->scientific_report` | 13 |
