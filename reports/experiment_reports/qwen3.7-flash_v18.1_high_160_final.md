# Final Results: qwen3.7-flash_v18.1_high_160

- **Dataset**: fixed_size_sampled
- **Model**: qwen/qwen3.7-flash
- **Prompt**: v18.1
- **Max tokens**: 4096

## Overall

- **Rows**: 160
- **Completed**: 159
- **Errors**: 1
- **Empty**: 0
- **exact_match**: 153/160 (95.6%)
- **failure rate**: 1/160 (0.6%)
- **near_miss** (correct answer was the model's runner-up): 2/160 (1.2% of rows; 33.3% of all misses)
- **runner_up coverage**: 141/159 completed rows had a parsable runner-up
- **Total cost**: $0.0617 across 159 rows with billed cost (avg $0.000388/image)

## Per-class accuracy

| Class | Correct | Total | Errors | Accuracy |
|---|---:|---:|---:|---:|
| advertisement | 9 | 10 | 1 | 90.0% |
| budget | 10 | 10 | 0 | 100.0% |
| email | 10 | 10 | 0 | 100.0% |
| file_folder | 10 | 10 | 0 | 100.0% |
| form | 8 | 10 | 0 | 80.0% |
| handwritten | 10 | 10 | 0 | 100.0% |
| invoice | 6 | 10 | 0 | 60.0% |
| letter | 10 | 10 | 0 | 100.0% |
| memo | 10 | 10 | 0 | 100.0% |
| news_article | 9 | 9 | 0 | 100.0% |
| presentation | 10 | 10 | 0 | 100.0% |
| questionnaire | 10 | 10 | 0 | 100.0% |
| resume | 10 | 10 | 0 | 100.0% |
| scientific_publication | 11 | 11 | 0 | 100.0% |
| scientific_report | 10 | 10 | 0 | 100.0% |
| specification | 10 | 10 | 0 | 100.0% |

## Failed (error) rows

- `test_imagesw_w_a_t_wat19d00_502218643.tif.png`

## Near-miss rows (correct answer was the model's runner-up)

These rows were misclassified but the model named the correct class as its
second choice in the reasoning trace — the closest possible misses.

- `test_imagesp_p_d_q_pdq99d00_94346851.tif.png`
- `test_imagesd_d_a_v_dav40c00_ti16801308.tif.png`
