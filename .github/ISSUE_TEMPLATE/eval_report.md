---
name: Prompt / experiment report
about: Share results of an eval run or prompt iteration (prompt changes, accuracy, cost)
title: "[EVAL] "
labels: ''
assignees: ''
---

## Summary

<!-- What was tested and why (rationale, link to prior issue/experiment). -->

- Prompt version: `vXX` (from `src/prompts.py`)
- Model: 
- Dataset / slice: 
- Experiment name: 
- Images per class / total rows: 

## Results

| Metric | Value |
| --- | --- |
| exact_match (accuracy) |  |
| Failed / ERROR rows |  |
| Near-misses (runner-up == expected) |  |
| Expected cost |  |
| Actual (billed) cost |  |

<!-- Attach or link: report_<experiment>.md, confusion matrix, per-class chart,
     misclassification_reasoning, experiment log section. -->

## Observations

<!-- Strong/weak classes, top confusion pairs, notable failures, reasoning patterns. -->

## Proposed next step

<!-- Promote prompt version / new experiment / revert, etc. -->
