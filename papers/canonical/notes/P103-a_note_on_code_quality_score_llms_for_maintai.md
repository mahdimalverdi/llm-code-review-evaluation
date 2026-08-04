# P103 — A Note on Code Quality Score: LLMs for Maintainable Large Codebases

> **Provisional intake record.** This is not a canonical paper note.

| Field | Value |
|---|---|
| Project ID | `P103` (provisional) |
| Citation key | `p103_wong2025_a_note_on_code_quality_score_l` |
| Authors | Sherman Wong; Jalaj Bhandari; Leo Zhou Fan Yang; Xylan Xu; Yi Zhuang; Cem Cayiroglu; Payal Bhuptani; Sheela Yadawad; Hung Duong |
| Year | 2025 |
| Source | arXiv |
| arXiv | `2508.02732v1` |
| Screening tier | `core` |
| Reconciliation status | New candidate after initial local matching |
| Metadata status | local_arxiv_metadata |
| Evidence status | Full-text eligibility recorded; extraction not yet completed |

## 1. Identification

- Duplicate or companion publication: No publisher venue or DOI is reported; verify before final integration.

## 2. Screening
- Decision: `Include`; Relevance: `High`
- Decision rationale: Describes an industrial LLM code-quality/review system with issue collection, validation, filtering, fine-tuning, developer feedback, and online helpfulness.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: mitigation design / precision–recall trade-off / workflow impact

## 3. Study overview
- Purpose: Automate code-quality issue detection and actionable critique for large, continuously changing industrial codebases.
- Research questions: Implicitly evaluate issue collection/validation, precision–recall trade-offs, LLM-judge quality, and online developer helpfulness.
- Method: Multi-stage CQS pipeline with Llama 3.1-70B issue collector, LLM-judge validator, rule filters, SFT and DPO, and developer-feedback flywheel.
- Evaluated system/artifact: Code Quality Score (CQS) with issue collection, issue validation, and action generation components.
- Dataset/benchmark: About 6,000 curated internal diffs for training, reduced to 5,000 high-quality diff/review examples; 8,400 DPO preference pairs; evaluation uses about 80 diff/review pairs and a 200-example thumbs-up/down judge set.
- Input context: Multi-language diffs (mainly Python, C++, PHP), issue tags, review text, function/file/line locations, rationales, and code-quality dimensions such as readability, modularity, robustness, and testability.
- Main findings: Collector SFT+DPO reaches precision 13.48% and recall 9.25% in Table 1; validator/filtering raises average precision to 78.20% but reduces recall to 1.20%. Online week-over-week helpfulness is approximately 60% with ±10% confidence interval.

## 4. Evidence mapped to review questions
| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | CQS decomposes review into collection, validation, and action generation, with rules and an LLM judge before display. | Reported | Sections 2–3 |
| RQ2 | SFT+DPO improves the collector over base/SFT in precision and recall, while post-generation validation strongly prioritizes precision over coverage. | Reported | Section 5.1–5.2, Tables 1–2 |
| RQ3 | LLM-judge quality is central: the trained judge reaches 62% accuracy vs 56% for base Llama on thumbs-up/down data. | Reported | Section 5.3 |
| RQ4 | Industrial feedback reports ≈60% helpfulness, but the small, biased evaluation set limits transfer from offline metrics to deployment. | Reported / limitation | Section 5.4 |
| RQ5 | Human/model-generated evaluation data is biased toward frontier models used to create the benchmark and can expose annotators to model identity. | Reported limitation | Section 4 |
| RQ6 | High-precision review systems should report the coverage lost by filtering and calibrate judge/rule thresholds against developer value. | Inferred | Sections 4–6 |

## 5. Failure and problematic-comment categories
| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Incorrect issue | Collector identifies a code-quality problem that is invalid or empty. | Target failure | Sections 3.1, 5 |
| Low-actionability comment | Human review lacks clear guidance or useful rationale. | Dataset filtering | Section 3.2 |
| Hallucinated/unsupported issue | Generated issue fails rule and LLM-judge validation. | Target failure | Section 3.1 |
| Filtered valid issue | Validator/rules reject an issue to preserve precision, potentially lowering recall. | Trade-off | Section 5.2 |
| Tag/language-specific error | Accuracy varies by issue tag and programming language, requiring hard-coded filters. | Reported failure | Section 3.1 |

## 6. Evaluation dimensions and metrics
| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Issue precision/recall | Matching issue tags/rationales against consensus evaluation set. | Collector SFT+DPO 13.48%/9.25%; CQS filtering 78.20%/1.20%. | Tables 1–2 |
| Baseline comparison | Base/SFT/DPO Llama and closed models. | Claude 30.43% precision/30.58% recall; Gemini 32.77%/22.53%; benchmark biased toward these models. | Table 1 |
| Judge quality | Accuracy on 100 positive and 100 negative developer-feedback examples. | Trained judge 62% vs base Llama 56%. | Section 5.3 |
| Human usefulness | Week-over-week positive UI feedback. | Approx. 60%, ±10% confidence interval; not equivalent to correctness or acceptance. | Section 5.4 |
| Data quality | Consensus issue agreement from at least two engineers. | ≈80 evaluation pairs, 2–4 consensus issues each. | Section 4 |
| Operational cost | Open-weight models, post-training, filtering, and internal deployment. | Compute/API cost and latency not reported. | Sections 3–5 |

## 7. Mitigation and trade-offs
- Mitigation family: SFT+DPO, LLM-judge validation, hard-coded filters, and developer-feedback data flywheel.
- Intervention point: Training data, preference optimization, post-generation filtering, and display threshold.
- What it reduces: Incorrect, hallucinated, irrelevant, and low-actionability issues reaching developers.
- Useful feedback potentially lost: The 78.20% precision/1.20% recall configuration demonstrates severe coverage loss from aggressive filtering.
- Coverage effect: Tag/language filters improve trust but can suppress novel or underrepresented issues.
- Human escalation effect: Only filtered comments are shown; online thumbs feedback provides a coarse post-display signal.
- Computational/operational cost: Multiple Llama agents, DPO preference generation, judge scoring, and rule maintenance add complexity; cost absent.
- New failure modes: Judge bias, threshold sensitivity, filter brittleness, model identity bias, and data-flywheel reinforcement of existing preferences.

## 8. Annotation and evaluator validity
- Judge/annotator: Developers provide critiques/thumbs signals; Llama judge rewrites/scores feedback; multiple engineers validate evaluation issues.
- Rubric: Issue tags, correctness, rationale, location, language/tag rules, and 0–10 judge scores.
- Agreement/reliability: At least two engineers must agree on evaluation issues; exact inter-rater statistic is not reported.
- Validity checks: Consensus filtering, separate evaluation diffs, semantic/rule matching, eyeball sanity checks, and judge benchmark.
- Possible bias: Evaluation candidates generated by GPT-4o/Claude/Gemini, annotators saw model names, internal Meta data, and incomplete ground truth.

## 9. Quality appraisal
| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | CQS stages and industrial objective explicit. |
| Q2 | 2 | Training, preference, evaluation, and judge datasets reported. |
| Q3 | 2 | Collector, validator, SFT, DPO, and filters described. |
| Q4 | 2 | Precision, recall, judge accuracy, and helpfulness reported. |
| Q5 | 2 | Issue/tag/rationale/line rubric described. |
| Q6 | 1 | Multi-engineer validation but no formal agreement statistic. |
| Q7 | 2 | Ablations and closed/open model comparisons included. |
| Q8 | 1 | Strong benchmark/model and internal-data bias. |
| Q9 | 2 | Filtering and post-training interventions evaluated. |
| Q10 | 1 | Industrial deployment reported but cost/latency absent. |
| Q11 | 2 | Evaluation bias and coverage trade-off explicitly discussed. |
| Q12 | 2 | Direct industrial generated-review evidence. |
- Total: `21/24` provisional
- Quality interpretation: Valuable industrial evidence for precision filtering and deployment feedback, with severe recall and benchmark-bias limitations.

## 10. Review-process reliability and bias
- Missing data: Exact system scale, latency, cost, developer sample size, acceptance rationale, and independent evaluation.
- Publication-bias concern: Internal author-developed system and positive deployment signal; evaluation benchmark favors source models.
- Selection uncertainty: Full text available; publisher metadata unverified.
- Extraction uncertainty: Moderate; some online and table details are incompletely specified.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Check for later venue/version before final bibliography integration.

## 11. Synthesis-ready conclusion
- Contribution to the SLR: Shows how multi-stage validation can substantially improve precision in industrial code-review assistance, while making the lost recall explicit.
- What the paper does not establish: It does not establish high recall, unbiased correctness, causal developer productivity gains, or generalization outside Meta.
- Research gap supported: Evaluation must report precision–coverage trade-offs, judge calibration, benchmark construction bias, and user helpfulness separately.
- Candidate synthesis claims: Filtering and learned validation can improve trust, but precision gains may conceal severe coverage loss and reinforce evaluator/data biases.
- Follow-up verification needed: Obtain exact evaluation-set counts, threshold/filter details, deployment volume, and independent human validation.
