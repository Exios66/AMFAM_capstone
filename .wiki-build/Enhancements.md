Compiled from the Monte Carlo analysis suite (`reports/monte_carlo/`), the joint
corpus (4,641 rows / 1,512 images across 14 experiments, 4 models, prompt
versions v0–v17.2), and the existing per-experiment reports. Every claim below
carries its source table/chart.


## 2. Ensemble & variance simulation

**Source:** `reports/monte_carlo/ensemble_accuracy_vs_k.md`

| *K* | accuracy | 95% *CI* | cost |
|---:|---:|---:|---:|
| 1 | 0.821 | 0.805–0.836 | 1x |
| 5 | 0.844 | 0.828–0.859 | 5x |
| 10 | 0.853 | 0.837–0.869 | 10x |
| 25 | 0.863 | 0.846–0.879 | 25x |

**Interpretation.** Cross-run variance is small. Majority voting buys at most
+4.2 *pp* at 25× cost; the marginal gain per extra vote collapses after *K* = 5. The
variance budget lives in the *prompt* (v0→v17 is +28.4 *pp*), not in repeated
sampling.

**Action:** Do NOT run *K*-vote ensembles in production. If a second pass is ever
justified, it should be a **single** second opinion on low-confidence images
(§4), not a full committee.


## 4. Confidence-gated escalation

**Source:** `reports/monte_carlo/routing_abstention.md`

| alpha | escalated | accuracy | cost factor |
|---:|---:|---:|---:|
| 5% | 76 | 0.845 | 1.10x |
| 10% | 151 | 0.864 | 1.20x |
| 15% | 227 | 0.879 | 1.30x |
| 20% | 302 | 0.891 | 1.40x |
| 30% | 454 | 0.895 | 1.60x |

Sensitivity band ±5 *pp* on the escalated-model accuracy moves the 15–20% points
by ≤±1 *pp* — the recommendation is robust to the stronger-model assumption.

**Interpretation.** The lowest-confidence images (high label entropy, a
near-miss signal, or uncertainty phrasing in the reasoning) are exactly where a
stronger model / higher reasoning effort pays. The curve is steepest through
10–20%.

**Action:** For production-scale runs, escalate the bottom ~10–15% by
confidence to a stronger model or `--reasoning-effort max`. Expected +4–6 *pp* at
+20–30% cost. Candidate list: `reports/monte_carlo/escalation_candidates.txt`.


## 6. Prompt ablation: what the versions actually changed

**Source:** `reports/monte_carlo/prompt_ablation.md`

| A | B | shared | delta | P(A wins) | verdict |
|---|---|---:|---:|---:|---|
| v0 | v17 | 155 | −0.284 | 0.000 | v17 wins** |
| v0 | v16 | 314 | −0.217 | 0.000 | v16 wins** |
| v0 | v11.8 | 898 | −0.130 | 0.000 | v11.8 wins** |
| v11.8 | v14 | 160 | −0.056 | 0.077 | v14 likely |
| v11.8 | v17 | 159 | +0.025 | 0.936 | v11.8 likely |
| v16 | v17 | 159 | +0.006 | 0.565 | inconclusive |
| v11.8 | v16 | 319 | −0.009 | 0.305 | inconclusive |

**Interpretation.**
- The big win was **v0 → the v11.x scratchpad line (+13–28 *pp*)**. Function-based
  scratchpad reasoning is the largest single contributor.
- **v16 vs v17 is a statistical tie** (+0.6 ***pp***, ***p*** = .565). The "v17 is better"
  narrative is NOT supported on shared images.
- **v11.8 still edges v17** (+2.5 ***pp***, ***p*** = .936) on shared images.

**Action:** Before the next prompt version, run the candidate against **v11.8**
AND **v17.2** on a shared slice, and require P(win) ≥ 0.90 (or a **CI** excluding
zero). Do not promote on a single-slice headline number. The v18 exemplar
candidate (§7) is the first test of this gate.


## 8. Class-level priorities (aggregate corpus accuracy)

| Class | Accuracy | Status |
|---|---:|---|
| budget | 62.0% | **critical** — weakest |
| presentation | 71.2% | critical |
| invoice | 74.2% | high |
| scientific_report | 74.6% | high |
| letter | 78.6% | high |
| handwritten | 80.4% | medium |
| specification | 81.5% | medium |
| form | 81.8% | medium |
| ... email | 95.5% | strong |

Top confusion pairs (corpus-wide): `letter→memo` (53), `budget→invoice` (52),
`invoice→form` (41), `specification→form` (41), `budget→form` (33),
`scientific_report→form` (23), `invoice→budget` (22).

**Interpretation.** The `form` attractor is systemic: 5 of the top 8 pairs end
in `form`. The financial cluster (`budget↔invoice`, 74 errors) is the second
system. `letter→memo` is the third (53 errors, plus 19 handwritten→letter).


## 10. Verification results (measured vs simulated)

`monte_carlo_verify.py --run-eval` (spend-minimal: 2 datasets, 4 targeted evals,
48 images each) completed. Source: `reports/monte_carlo/verification_results.md`.

### Escalation slice (lowest-confidence 3% tail)

| run | rows | accuracy |
|---|---:|---:|
| base (v11.8) | 48 | 66.7% |
| escalated (v11.8, `--reasoning-effort max`) | 48 | 62.5% |

**Measured tail accuracy (66.7%) is well below the corpus average (82%) —
confirms the confidence ordering flags genuinely hard images.** The simulator's
`p_correct` mean for these images (0.425) is lower still, i.e. the heuristic is
conservative but directionally correct.

**Critical caveat:** escalating to a *stronger model* was the assumption that
gave +4–6 **pp**; escalating to the SAME model at higher reasoning effort did NOT
help (62.5% < 66.7%). Higher effort does not fix hard images on this model
line. Escalation requires a genuinely stronger model (e.g. kimi/gemini-class),
which should be validated before production adoption.

### Exemplar slice (top confusion pairs)

| run | rows | accuracy |
|---|---:|---:|
| base (v17.2) | 48 | 68.8% |
| exemplar (v18) | 48 | 64.6% |

**Delta (v18 − v17.2): −4.2 **pp** — the exemplar appendix did NOT improve accuracy
on the targeted slice; it slightly hurt.** v18 should NOT be promoted to default
on this evidence. The four appended worked examples (11,383 chars) added
verbosity without correcting the runner-up-vs-final decision.

**Action revision:** instead of adding more exemplar text, the highest-value
next experiment is the **runner-up rescue rule** (§3) — a short calibration
sentence forbidding the model to override its own stated runner-up without new
evidence — evaluated on the same exemplar slice, plus a measured check on
whether a stronger-model escalation beats the 66.7% base on the escalation tail.

---
*Published via [Posit Cloud](https://connect.posit.cloud/jackjburleson/content/019fd440-9bbf-1a22-cf30-a36183d9c7d4) · [GitHub repo](https://github.com/Exios66/AMFAM_capstone)*
