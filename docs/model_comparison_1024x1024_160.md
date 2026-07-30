# Model Comparison — 1024×1024, 160 Images (10 per class × 16 classes)

**Prompt:** `CLASSIFICATION_PROMPT` v2 (expanded disambiguation rules)
**Settings:** `max_tokens=1024`, `temperature=0.1`, `reasoning.effort=medium`

| Model | Cost | Total Tokens | Accuracy | Macro F1 | Pricing (per M tokens) |
|-------|-----:|-------------:|---------:|---------:|------------------------|
| `google/gemini-2.5-flash` | $0.28 | 434,843 | 85.00% | 85.29% | $0.15 in / $0.60 out |
| `moonshotai/kimi-k3` | $1.07 | 407,330 | 85.00% | 84.83% | $0.30 in / $15.00 out |
| `openai/gpt-5.6-terra` | $0.72 | 395,819 | 91.25% | 91.26% | $2.50 in / $10.00 out |
| `x-ai/grok-4.5` | $0.60 | 437,337 | 89.31% | 89.30% | $2.00 in / $6.00 out |
| `anthropic/claude-sonnet-5` | $1.17 | 580,000 | 90.62% | 90.69% | $3.00 in / $15.00 out |
| `google/gemini-3.6-flash` | $0.97 | 445,579 | **91.88%** | 91.89% | $0.15 in / $0.60 out |
| `anthropic/claude-opus-5` | $2.94 | 580,904 | **91.88%** | **91.85%** | $15.00 in / $75.00 out |
