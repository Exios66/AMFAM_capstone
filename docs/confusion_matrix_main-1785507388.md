# Confusion Matrix — main-1785507388

**Overall Accuracy:** 93.1% (149/160)  
**Dataset:** 10 per class  
**Model:** `google/gemini-3.6-flash`

![Confusion Matrix](confusion_matrix_main-1785507388.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **10** | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `budget` | . | **10** | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `email` | . | . | **9** | . | . | . | . | . | . | . | . | . | . | . | . | 1 | 10 | 90% |
| `file_folder` | . | . | . | **10** | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `form` | . | . | . | . | **10** | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `handwritten` | . | . | . | . | . | **9** | . | . | . | . | . | 1 | . | . | . | . | 10 | 90% |
| `invoice` | . | . | . | . | . | . | **10** | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `letter` | . | . | 1 | . | . | . | 1 | **7** | . | . | . | 1 | . | . | . | . | 10 | 70% |
| `memo` | . | . | . | . | . | . | 1 | . | **9** | . | . | . | . | . | . | . | 10 | 90% |
| `news_article` | . | . | . | . | . | . | . | . | . | **9** | . | . | . | 1 | . | . | 10 | 90% |
| `presentation` | . | . | . | . | . | . | . | . | . | . | **10** | . | . | . | . | . | 10 | 100% |
| `questionnaire` | . | . | . | . | 1 | . | . | . | . | . | . | **9** | . | . | . | . | 10 | 90% |
| `resume` | . | . | . | . | . | . | . | . | . | . | . | . | **10** | . | . | . | 10 | 100% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | 1 | . | . | . | **9** | . | . | 10 | 90% |
| `scientific_report` | . | . | . | . | . | . | . | . | . | . | 1 | . | . | . | **9** | . | 10 | 90% |
| `specification` | . | . | . | . | . | 1 | . | . | . | . | . | . | . | . | . | **9** | 10 | 90% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `email` | `specification` | 1 |
| `handwritten` | `questionnaire` | 1 |
| `letter` | `email` | 1 |
| `letter` | `invoice` | 1 |
| `letter` | `questionnaire` | 1 |
| `memo` | `invoice` | 1 |
| `news_article` | `scientific_publication` | 1 |
| `questionnaire` | `form` | 1 |
| `scientific_publication` | `news_article` | 1 |
| `scientific_report` | `presentation` | 1 |
| `specification` | `handwritten` | 1 |
