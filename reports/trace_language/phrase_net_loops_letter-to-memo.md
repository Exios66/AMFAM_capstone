# Structural Loops in Failed Reasoning Traces

- **Corpus rows (reasoning-covered)**: 45
- **Differential bigram edges**: 0
- **Cycles found (length ≤ 6)**: 0

## Per-trace stuck-phrase rates

A trace is marked as looping when its token stream repeats a bi-gram back-to-back (`A B A B`) or a tri-gram back-to-back (`A B C A B C`) — the model re-running the same phrase instead of progressing. Plain `A -> B -> A` trigrams saturate (every v11.8 trace re-quotes evidence across the check cascade), so only consecutive duplication is counted.

| Group | Traces | Looping traces | Rate |
|---|---:|---:|---:|
| Failed | 45 | 7 | 15.6% |
| Correct | 0 | 0 | 0.0% |

## Cycles

No cycles found in the differential graph.
