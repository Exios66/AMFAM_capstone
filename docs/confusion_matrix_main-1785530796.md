# Confusion Matrix — main-1785530796

**Overall Accuracy:** 54.0% (61/113)  
**Dataset:** 7 per class  
**Model:** `google/gemini-3.6-flash`

![Confusion Matrix](confusion_matrix_main-1785530796.png)

## Raw Counts

| Expected \ Predicted | `advert` | `budget` | `email` | `file_f` | `form` | `handwr` | `invoic` | `letter` | `memo` | `news_a` | `presen` | `questi` | `resume` | `scient` | `scient` | `specif` | **Total** | **Acc** |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| `advertisement` | **4** | . | 1 | 2 | . | . | . | . | . | . | . | . | . | . | . | . | 7 | 57% |
| `budget` | . | **4** | 2 | 2 | . | . | . | . | . | . | . | . | . | . | . | . | 8 | 50% |
| `email` | . | . | **9** | 1 | . | . | . | . | . | . | . | . | . | . | . | . | 10 | 90% |
| `file_folder` | . | . | . | **8** | . | . | . | . | . | . | . | . | . | . | . | . | 8 | 100% |
| `form` | 1 | . | . | 2 | **6** | . | . | . | . | . | . | . | . | . | . | . | 9 | 67% |
| `handwritten` | . | . | . | . | . | **9** | . | . | . | . | . | . | . | . | . | . | 9 | 100% |
| `invoice` | . | . | 1 | 2 | . | . | **6** | . | . | . | . | . | . | . | . | . | 9 | 67% |
| `letter` | . | 3 | 2 | 2 | . | . | . | **1** | . | . | . | . | . | . | . | . | 8 | 12% |
| `memo` | . | 1 | 1 | 4 | . | . | 1 | . | **3** | . | . | . | . | . | . | . | 10 | 30% |
| `news_article` | 1 | 3 | . | . | . | . | . | . | . | **5** | . | . | . | 1 | . | . | 10 | 50% |
| `presentation` | . | 1 | 1 | 4 | . | . | . | . | . | . | **4** | . | . | . | . | . | 10 | 40% |
| `questionnaire` | . | . | . | 1 | . | . | . | . | . | . | . | **2** | . | . | . | . | 3 | 67% |
| `resume` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 0 | 0% |
| `scientific_publication` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 0 | 0% |
| `scientific_report` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 0 | 0% |
| `specification` | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | . | 0 | 0% |

## Top Confused Pairs

| Expected | Predicted As | Count |
|----------|-------------|------:|
| `memo` | `file_folder` | 4 |
| `presentation` | `file_folder` | 4 |
| `letter` | `budget` | 3 |
| `news_article` | `budget` | 3 |
| `advertisement` | `file_folder` | 2 |
| `budget` | `email` | 2 |
| `budget` | `file_folder` | 2 |
| `form` | `file_folder` | 2 |
| `invoice` | `file_folder` | 2 |
| `letter` | `email` | 2 |
| `letter` | `file_folder` | 2 |
| `advertisement` | `email` | 1 |
| `email` | `file_folder` | 1 |
| `form` | `advertisement` | 1 |
| `invoice` | `email` | 1 |
| `memo` | `budget` | 1 |
| `memo` | `email` | 1 |
| `memo` | `invoice` | 1 |
| `news_article` | `advertisement` | 1 |
| `news_article` | `scientific_publication` | 1 |
