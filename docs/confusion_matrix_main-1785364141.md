# Confusion Matrix — main-1785364141

**Overall Accuracy:** 85.0% (136/160)  
**Dataset:** 10 per class  
**Model:** `google/gemini-2.5-flash`

![Confusion Matrix](confusion_matrix_main-1785364141.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **9** | . | . | . | . | . | . | . | . | . | 1 | . | . | . | . | . | 10 | 90% |
| `budget` | . | **10** | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 100% |
| `email` | . | . | **9** | . | . | . | . | . | . | . | . | . | . | . | 1 | . | 10 | 90% |
| `file_folder` | . | 1 | . | **8** | 1 | . | . | . | . | . | . | . | . | . | . | . | 10 | 80% |
| `form` | . | . | . | 1 | **7** | . | . | . | . | . | . | . | . | . | 2 | . | 10 | 70% |
| `handwritten` | . | . | . | . | 1 | **9** | . | . | . | . | . | . | . | . | . | . | 10 | 90% |
| `invoice` | . | 1 | . | . | . | . | **8** | . | . | . | . | . | . | . | . | 1 | 10 | 80% |
| `letter` | . | 1 | . | . | . | . | . | **8** | 1 | . | . | . | . | . | . | . | 10 | 80% |
| `memo` | . | . | . | . | . | . | 1 | . | **9** | . | . | . | . | . | . | . | 10 | 90% |
| `news_article` | . | . | . | . | . | . | . | . | . | **9** | . | . | . | 1 | . | . | 10 | 90% |
| `presentation` | . | . | . | 1 | . | . | . | . | . | . | **8** | . | . | . | 1 | . | 10 | 80% |
| `questionnaire` | . | . | . | . | 3 | . | . | 1 | . | . | . | **6** | . | . | . | . | 10 | 60% |
| `resume` | . | . | . | . | . | . | . | . | . | . | . | . | **10** | . | . | . | 10 | 100% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | 1 | . | . | . | **7** | 2 | . | 10 | 70% |
| `scientific_report` | . | . | . | . | . | . | . | . | . | . | 1 | . | . | . | **9** | . | 10 | 90% |
| `specification` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | **10** | 10 | 100% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `questionnaire` | `form` | 3 |
| `form` | `scientific_report` | 2 |
| `scientific_publication` | `scientific_report` | 2 |
| `advertisement` | `presentation` | 1 |
| `email` | `scientific_report` | 1 |
| `file_folder` | `budget` | 1 |
| `file_folder` | `form` | 1 |
| `form` | `file_folder` | 1 |
| `handwritten` | `form` | 1 |
| `invoice` | `budget` | 1 |
| `invoice` | `specification` | 1 |
| `letter` | `budget` | 1 |
| `letter` | `memo` | 1 |
| `memo` | `invoice` | 1 |
| `news_article` | `scientific_publication` | 1 |
| `presentation` | `file_folder` | 1 |
| `presentation` | `scientific_report` | 1 |
| `questionnaire` | `letter` | 1 |
| `scientific_publication` | `news_article` | 1 |
| `scientific_report` | `presentation` | 1 |
