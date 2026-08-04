# P112 — Measuring Determinism in Large Language Models for Software Code Review

## 1. Identification

| Field | Value |
|---|---|
| Project ID | `P112` |
| Citation key | `p112_klishevich2025_measuring_determinism_in_large` |
| Authors | Eugene Klishevich; Yegor Denisov-Blanch; Simon Obstbaum; Igor Ciobanu; Michal Kosinski |
| Year | 2025 |
| Source | arXiv preprint, `2502.20747v1` |
| Study type | Repeated-run reliability and determinism experiment |

## 2. Screening

- **Scope decision:** Include as core methodological evidence for reliability, reproducibility, and evaluation of LLM-generated review assessments.
- **Task:** Repeatedly assess identical Java commits under temperature-zero conditions.
- **Evidence boundary:** The paper measures test–retest consistency, not whether assessments are correct or useful to developers.
- **Metadata caveat:** Publisher/duplicate status and the provisional BibTeX record require verification.

## 3. Study overview

The study tests GPT-4o mini, GPT-4o, Claude 3.5 Sonnet, and Llama 3.2 90B Vision on 70 Java commits drawn from private and public repositories. Each model receives three prompt lengths and five review questions, with five independent runs per identical input, temperature set to zero, and context cleared. The resulting 21,000 structured responses are compared using Pearson correlations across runs, with bootstrap 95% confidence intervals and permutation testing. Questions cover effort estimates, author experience, difficulty, and maintainability. The study also compares model consistency with prior human-rater ICC values.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | The study evaluates repeatability of LLM code-commit assessments across four models and three prompt lengths. | Reported | Sections 2–3 |
| RQ2 | Llama 3.2 shows the highest consistency, Claude is intermediate, and GPT-4o/mini are less consistent; human ICC values provide context. | Reported | Tables 3–4 |
| RQ3 | Output variation occurs even at temperature zero, creating risk of inconsistent review decisions and maintainability judgments. | Reported | Abstract; Section 4 |
| RQ4 | Prompt length is varied from approximately 100 to 750 words while code patches and questions remain fixed. | Reported | Section 2.4 |
| RQ5 | Repeated runs, ensembles/majority selection, fine-tuning, and inference-time methods are proposed to reduce variability. | Proposed | Section 4.2 |
| RQ6 | Structured JSON outputs, repeated trials, confidence intervals, and statistical testing support reliability measurement; correctness is explicitly left for future work. | Reported/limitation | Sections 2.6–2.7; 4.3 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Inconsistent assessment | Identical commit receives different categorical or scalar answers across runs. | Measured | Sections 2–3 |
| Maintainability instability | Model changes its maintainability judgment for the same code. | Measured | Q5; Table 4 |
| Effort-estimate instability | Hours-to-implement estimates vary across repeated outputs. | Measured | Q1–Q2 |
| Difficulty/experience instability | Model changes perceived difficulty or author-experience category. | Measured | Q3–Q4 |
| Unreliable automation | Variability undermines reproducibility of review decisions even when temperature is zero. | Interpretation | Discussion |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Test–retest consistency | Pearson correlation across five runs for each model/prompt/question | Model-specific consistency gradients are observed. | Section 2.6; Table 3 |
| Prompt sensitivity | Compare simple, balanced, and explanatory prompts | Prompt length is treated as a factor, though validity impact is not fully established. | Sections 2.4, 3 |
| Question-domain reliability | Five topics: effort, implementation effort, experience, difficulty, maintainability | Reliability varies by topic; maintainability is intrinsically subjective. | Table 2/4 |
| Human comparability | Compare LLM correlations with human ICC2,k values | LLM consistency can be comparable to human consistency, but constructs are not identical. | Table 4 |
| Statistical uncertainty | Bootstrap 95% CIs and permutation test | Supports comparison of consistency estimates. | Sections 2.6–2.7 |
| Validity | Accuracy against an external correctness oracle | Not measured; authors identify validity as future work. | Section 4.3 |

## 7. Mitigation and trade-offs

- **Mitigation family:** Repeat model calls, aggregate/majority-vote outputs, ensemble models, fine-tuning, and inference-time stabilization.
- **Intervention point:** Inference and training reliability rather than review content alone.
- **What it reduces:** Unstable recommendations and irreproducible review decisions.
- **Useful feedback potentially lost:** Majority aggregation can suppress minority findings that are correct or unusually insightful.
- **Coverage:** Repetition improves confidence in repeated outputs but does not improve the model’s defect coverage or truthfulness.
- **Human escalation:** Inconsistent or high-impact assessments should be reviewed by humans; the paper does not define an operational escalation policy.
- **Cost:** Multiple runs and ensembles multiply inference cost and latency.
- **New failure modes:** Correlated repeated errors can appear stable, and aggregation can create false confidence without validity testing.

## 8. Annotation and evaluator validity

- **Output control:** Standardized JSON makes categorical/scalar responses machine-comparable.
- **Sample:** 70 Java commits from public/private repositories and 21,000 responses provide repeated-measures depth.
- **Human comparison:** Prior human ICC values are used as a reference, not newly collected in this study.
- **Agreement:** The main reliability target is cross-run correlation; no new human inter-rater study is conducted.
- **Validity limitation:** Consistency is precision-like reliability, not correctness; the paper explicitly postpones validity measurement.
- **Scope threats:** Java-only commits, selected questions, prompt construction, and model/API versions constrain generalization.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Determinism objective and experimental factors are explicit. |
| Q2 | 2 | 70 commits and source composition are described. |
| Q3 | 2 | Models, prompts, repeats, temperature, and structured outputs are specified. |
| Q4 | 2 | Correlations, confidence intervals, and permutation tests are reported. |
| Q5 | 2 | Repeated identical inputs provide a clear reliability protocol. |
| Q6 | 1 | Human comparison uses prior ICC rather than a new agreement sample. |
| Q7 | 2 | Four models, three prompt lengths, and five questions are compared. |
| Q8 | 1 | Public/private commits improve realism, but language and sample scope are narrow. |
| Q9 | 1 | Mitigations are proposed rather than empirically tested. |
| Q10 | 1 | Cost implications are discussed qualitatively. |
| Q11 | 2 | Reliability, prompt sensitivity, and human comparability are directly analyzed. |
| Q12 | 2 | Consistency is directly relevant to dependable review assistance. |

**Total: 20/24 — high confidence for determinism/reliability evidence; not evidence of assessment correctness.**

## 10. Review-process reliability and bias

- **Construct validity:** High consistency can coexist with consistently wrong judgments; validity is not measured.
- **Dataset bias:** Seventy Java commits may not represent other languages, repositories, or review tasks.
- **Prompt bias:** The three prompt templates and five questions constrain the conclusions about general code review.
- **Model/API drift:** Closed-model implementations can change, making future replication difficult.
- **Human-comparison caveat:** Prior ICC values and LLM Pearson correlations are related but not directly interchangeable.
- **Operational omission:** No workflow study measures whether repeated-run stabilization improves developer trust, decisions, or productivity.

## 11. Synthesis-ready conclusion

- P112 establishes that temperature zero does not guarantee deterministic LLM code-review assessments.
- Repeatability is a necessary reliability dimension, but it must be paired with correctness, usefulness, and calibration measures.
- Repeated inference or ensembles may reduce visible variation while increasing cost and potentially masking correlated errors.
- The study supports reporting test–retest reliability in LLM review evaluations, especially for high-impact decisions.
- Use as core evidence for reproducibility and reliability risk, not as evidence that any model’s review judgments are accurate.

