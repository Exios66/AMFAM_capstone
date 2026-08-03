# Confusion Matrix — main-1785529923

**Overall Accuracy:** 13.1% (21/160)  
**Dataset:** 10 per class  
**Model:** `google/gemini-3.6-flash`

![Confusion Matrix](confusion_matrix_main-1785529923.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **3** | . | . | 5 | . | . | . | . | . | . | . | . | . | . | . | . | 8 | 38% |
| `budget` | . | **5** | . | 3 | . | . | . | 1 | . | . | . | . | . | . | . | . | 9 | 56% |
| `email` | . | 7 | **2** | 1 | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 20% |
| `file_folder` | . | . | . | **9** | . | . | . | . | . | . | 1 | . | . | . | . | . | 10 | 90% |
| `form` | . | 1 | 1 | 6 | . | . | . | . | . | . | . | . | . | . | . | . | 8 | 0% |
| `handwritten` | . | . | . | 8 | 1 | . | . | . | . | . | . | . | . | . | . | . | 9 | 0% |
| `invoice` | . | 6 | 1 | 1 | . | . | . | . | . | . | . | . | . | . | . | . | 8 | 0% |
| `letter` | . | 4 | 1 | 2 | . | . | . | **1** | . | . | . | . | . | . | . | . | 8 | 12% |
| `memo` | . | 5 | 2 | 3 | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 0% |
| `news_article` | 2 | 5 | 1 | 2 | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 0% |
| `presentation` | . | 7 | . | 2 | . | . | . | . | . | . | . | . | . | . | . | . | 9 | 0% |
| `questionnaire` | . | 1 | . | 8 | 1 | . | . | . | . | . | . | . | . | . | . | . | 10 | 0% |
| `resume` | . | . | 1 | 9 | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 0% |
| `scientific_publication` | . | . | 1 | 9 | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 0% |
| `scientific_report` | . | 1 | 2 | 3 | . | . | . | 1 | . | . | . | . | . | . | . | . | 7 | 0% |
| `specification` | . | 7 | . | 2 | . | . | . | . | . | . | . | . | . | . | . | **1** | 10 | 10% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `resume` | `file_folder` | 9 |
| `scientific_publication` | `file_folder` | 9 |
| `handwritten` | `file_folder` | 8 |
| `questionnaire` | `file_folder` | 8 |
| `email` | `budget` | 7 |
| `presentation` | `budget` | 7 |
| `specification` | `budget` | 7 |
| `form` | `file_folder` | 6 |
| `invoice` | `budget` | 6 |
| `advertisement` | `file_folder` | 5 |
| `memo` | `budget` | 5 |
| `news_article` | `budget` | 5 |
| `letter` | `budget` | 4 |
| `budget` | `file_folder` | 3 |
| `memo` | `file_folder` | 3 |
| `scientific_report` | `file_folder` | 3 |
| `letter` | `file_folder` | 2 |
| `memo` | `email` | 2 |
| `news_article` | `advertisement` | 2 |
| `news_article` | `file_folder` | 2 |
