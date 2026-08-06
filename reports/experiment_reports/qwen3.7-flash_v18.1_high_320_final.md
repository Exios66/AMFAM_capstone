# Final Results: qwen3.7-flash_v18.1_high_320

- **Dataset**: fixed_size_sampled_320
- **Model**: qwen/qwen3.7-flash
- **Prompt**: v18.1
- **Max tokens**: 4096

## Overall

- **Rows**: 319
- **Completed**: 317
- **Errors**: 2
- **Empty**: 0
- **exact_match**: 269/319 (84.3%)
- **failure rate**: 2/319 (0.6%)
- **near_miss** (correct answer was the model's runner-up): 33/319 (10.3% of rows; 68.8% of all misses)
- **runner_up coverage**: 295/317 completed rows had a parsable runner-up
- **Total cost**: $0.1221 across 317 rows with billed cost (avg $0.000385/image)

## Per-class accuracy

| Class | Correct | Total | Errors | Accuracy |
|---|---:|---:|---:|---:|
| advertisement | 18 | 20 | 0 | 90.0% |
| budget | 17 | 20 | 0 | 85.0% |
| email | 20 | 20 | 0 | 100.0% |
| file_folder | 16 | 20 | 0 | 80.0% |
| form | 15 | 19 | 1 | 78.9% |
| handwritten | 18 | 20 | 0 | 90.0% |
| invoice | 14 | 20 | 0 | 70.0% |
| letter | 15 | 20 | 0 | 75.0% |
| memo | 20 | 20 | 0 | 100.0% |
| news_article | 16 | 20 | 0 | 80.0% |
| presentation | 17 | 20 | 0 | 85.0% |
| questionnaire | 16 | 20 | 1 | 80.0% |
| resume | 20 | 20 | 0 | 100.0% |
| scientific_publication | 18 | 20 | 0 | 90.0% |
| scientific_report | 14 | 20 | 0 | 70.0% |
| specification | 15 | 20 | 0 | 75.0% |

## Failed (error) rows

- `rvl_cdip__form__0006.png`
- `rvl_cdip__questionnaire__0003.png`

## Near-miss rows (correct answer was the model's runner-up)

These rows were misclassified but the model named the correct class as its
second choice in the reasoning trace — the closest possible misses.

- `rvl_cdip__budget__0007.png`
- `rvl_cdip__budget__0014.png`
- `rvl_cdip__file_folder__0004.png`
- `rvl_cdip__file_folder__0008.png`
- `rvl_cdip__file_folder__0011.png`
- `rvl_cdip__form__0001.png`
- `rvl_cdip__form__0018.png`
- `rvl_cdip__invoice__0003.png`
- `rvl_cdip__invoice__0006.png`
- `rvl_cdip__invoice__0008.png`
- `rvl_cdip__invoice__0014.png`
- `rvl_cdip__invoice__0015.png`
- `rvl_cdip__invoice__0017.png`
- `rvl_cdip__letter__0007.png`
- `rvl_cdip__letter__0008.png`
- `rvl_cdip__letter__0010.png`
- `rvl_cdip__news_article__0008.png`
- `rvl_cdip__news_article__0014.png`
- `rvl_cdip__news_article__0018.png`
- `rvl_cdip__news_article__0020.png`
- `rvl_cdip__presentation__0017.png`
- `rvl_cdip__presentation__0018.png`
- `rvl_cdip__scientific_publication__0006.png`
- `rvl_cdip__scientific_publication__0016.png`
- `rvl_cdip__scientific_report__0002.png`
- `rvl_cdip__scientific_report__0003.png`
- `rvl_cdip__scientific_report__0008.png`
- `rvl_cdip__scientific_report__0009.png`
- `rvl_cdip__scientific_report__0016.png`
- `rvl_cdip__specification__0004.png`
- `rvl_cdip__specification__0006.png`
- `rvl_cdip__specification__0013.png`
- `rvl_cdip__specification__0019.png`
