# Confusion Matrix — main-1785277280

**Overall Accuracy:** 83.8% (134/160)  
**Dataset:** 2550×3300 padded PNGs, 50 per class  
**Model:** `google/gemini-2.5-flash`

![Confusion Matrix](confusion_matrix_main-1785277280.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **10** | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `budget` | . | **10** | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `email` | . | . | **9** | . | . | . | . | . | . | . | . | . | . | . | 1 | . | 10 | 90% |
| `file_folder` | . | . | . | **8** | 1 | 1 | . | . | . | . | . | . | . | . | . | . | 10 | 80% |
| `form` | . | . | . | 1 | **7** | . | . | . | . | . | . | . | . | . | 2 | . | 10 | 70% |
| `handwritten` | . | . | . | . | 1 | **9** | . | . | . | . | . | . | . | . | . | . | 10 | 90% |
| `invoice` | . | 2 | . | . | . | . | **8** | . | . | . | . | . | . | . | . | . | 10 | 80% |
| `letter` | . | 1 | . | . | . | . | . | **8** | 1 | . | . | . | . | . | . | . | 10 | 80% |
| `memo` | . | . | . | . | . | . | 1 | . | **9** | . | . | . | . | . | . | . | 10 | 90% |
| `news_article` | . | . | . | . | . | . | . | . | . | **9** | . | . | . | 1 | . | . | 10 | 90% |
| `presentation` | . | . | . | 4 | . | . | . | . | . | . | **5** | . | . | . | 1 | . | 10 | 50% |
| `questionnaire` | . | . | . | . | 2 | . | . | 1 | . | . | . | **7** | . | . | . | . | 10 | 70% |
| `resume` | . | . | . | . | 1 | . | . | . | . | . | . | . | **9** | . | . | . | 10 | 90% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | 1 | . | . | . | **7** | 2 | . | 10 | 70% |
| `scientific_report` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | **10** | . | 10 | 100% |
| `specification` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 1 | **9** | 10 | 90% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `presentation` | `file_folder` | 4 |
| `form` | `scientific_report` | 2 |
| `invoice` | `budget` | 2 |
| `questionnaire` | `form` | 2 |
| `scientific_publication` | `scientific_report` | 2 |
| `email` | `scientific_report` | 1 |
| `file_folder` | `form` | 1 |
| `file_folder` | `handwritten` | 1 |
| `form` | `file_folder` | 1 |
| `handwritten` | `form` | 1 |
| `letter` | `budget` | 1 |
| `letter` | `memo` | 1 |
| `memo` | `invoice` | 1 |
| `news_article` | `scientific_publication` | 1 |
| `presentation` | `scientific_report` | 1 |
| `questionnaire` | `letter` | 1 |
| `resume` | `form` | 1 |
| `scientific_publication` | `news_article` | 1 |
| `specification` | `scientific_report` | 1 |
