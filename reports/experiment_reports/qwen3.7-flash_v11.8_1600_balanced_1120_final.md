# Final Results: qwen3.7-flash_v11.8_reasoning_1600_balanced_1120

- **Dataset**: rvl_cdip_1600
- **Model**: qwen/qwen3.7-flash
- **Prompt**: v11.8
- **Max tokens**: 8192

## Overall

- **Rows**: 725
- **Completed**: 721
- **Errors**: 4
- **Empty**: 0
- **exact_match**: 602/725 (83.0%)
- **near_miss** (correct answer was the model's runner-up): 0/725 (0.0% of rows; 0.0% of all misses)
- **runner_up coverage**: 0/721 completed rows had a parsable runner-up

## Per-class accuracy

| Class | Correct | Total | Errors | Accuracy |
|---|---:|---:|---:|---:|
| advertisement | 40 | 47 | 0 | 85.1% |
| budget | 25 | 38 | 0 | 65.8% |
| email | 48 | 53 | 0 | 90.6% |
| file_folder | 40 | 47 | 0 | 85.1% |
| form | 38 | 43 | 0 | 88.4% |
| handwritten | 40 | 44 | 0 | 90.9% |
| invoice | 35 | 44 | 0 | 79.5% |
| letter | 34 | 47 | 0 | 72.3% |
| memo | 33 | 39 | 2 | 84.6% |
| news_article | 38 | 43 | 2 | 88.4% |
| presentation | 30 | 45 | 0 | 66.7% |
| questionnaire | 43 | 50 | 0 | 86.0% |
| resume | 40 | 41 | 0 | 97.6% |
| scientific_publication | 43 | 48 | 0 | 89.6% |
| scientific_report | 35 | 50 | 0 | 70.0% |
| specification | 40 | 46 | 0 | 87.0% |

## Failed (error) rows

- `rvl_cdip__memo__0014.png`
- `rvl_cdip__memo__0043.png`
- `rvl_cdip__news_article__0048.png`
- `rvl_cdip__news_article__0084.png`
