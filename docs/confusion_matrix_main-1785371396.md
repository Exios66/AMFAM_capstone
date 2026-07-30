# Confusion Matrix — main-1785371396

**Overall Accuracy:** 91.9% (147/160)  
**Dataset:** 10 per class  
**Model:** `anthropic/claude-opus-5`

![Confusion Matrix](confusion_matrix_main-1785371396.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **10** | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `budget` | . | **10** | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `email` | . | . | **9** | . | . | . | . | . | . | . | . | . | . | . | . | 1 | 10 | 90% |
| `file_folder` | . | . | . | **10** | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `form` | . | . | . | 1 | **9** | . | . | . | . | . | . | . | . | . | . | . | 10 | 90% |
| `handwritten` | 1 | . | . | . | . | **9** | . | . | . | . | . | . | . | . | . | . | 10 | 90% |
| `invoice` | . | 1 | . | . | . | . | **8** | . | . | . | . | . | . | . | . | 1 | 10 | 80% |
| `letter` | . | 1 | 1 | . | . | . | . | **8** | . | . | . | . | . | . | . | . | 10 | 80% |
| `memo` | . | . | . | . | . | . | 1 | . | **9** | . | . | . | . | . | . | . | 10 | 90% |
| `news_article` | . | . | . | . | . | . | . | . | . | **9** | . | . | . | 1 | . | . | 10 | 90% |
| `presentation` | . | . | . | . | . | . | . | . | . | . | **10** | . | . | . | . | . | 10 | 100% |
| `questionnaire` | . | . | . | . | 1 | . | . | 1 | . | . | . | **8** | . | . | . | . | 10 | 80% |
| `resume` | . | . | . | . | . | . | . | . | . | . | . | . | **10** | . | . | . | 10 | 100% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | 1 | . | . | . | **9** | . | . | 10 | 90% |
| `scientific_report` | . | . | . | . | . | . | . | . | . | . | . | . | . | 1 | **9** | . | 10 | 90% |
| `specification` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | **10** | 10 | 100% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `email` | `specification` | 1 |
| `form` | `file_folder` | 1 |
| `handwritten` | `advertisement` | 1 |
| `invoice` | `budget` | 1 |
| `invoice` | `specification` | 1 |
| `letter` | `budget` | 1 |
| `letter` | `email` | 1 |
| `memo` | `invoice` | 1 |
| `news_article` | `scientific_publication` | 1 |
| `questionnaire` | `form` | 1 |
| `questionnaire` | `letter` | 1 |
| `scientific_publication` | `news_article` | 1 |
| `scientific_report` | `scientific_publication` | 1 |
