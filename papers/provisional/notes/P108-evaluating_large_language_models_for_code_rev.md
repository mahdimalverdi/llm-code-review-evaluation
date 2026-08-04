# P108 — Evaluating Large Language Models for Code Review

## 1. Identification

| Field | Value |
|---|---|
| Project ID | `P108` |
| Citation key | `p108_cihan2025_evaluating_large_language_mode` |
| Authors | Umut Cihan; Arda İçöz; Vahid Haratian; Eray Tüzün |
| Year | 2025 |
| Source | arXiv preprint, `2505.20206v1` |
| Study type | Controlled benchmark of correctness assessment and code correction |
| Reconciliation | Queue marks this as an external duplicate/companion candidate mapped to `EXT-0028`; resolve identity before synthesis counting. |

## 2. Screening

- **Scope decision:** Include as evidence only after duplicate resolution; do not count as a separate study if `EXT-0028` is the same work.
- **Task:** LLMs decide whether Python code should be approved and provide a corrected code block when needed.
- **Evidence boundary:** The study tests functional correctness against unit tests, not natural-language comment quality or developer acceptance.
- **Metadata caveat:** Publisher/duplicate status and the provisional BibTeX record require verification.

## 3. Study overview

The study evaluates GPT-4o (`gpt-4o-2024-11-20`) and Gemini 2.0 Flash on 492 AI-generated Python code blocks and 164 canonical HumanEval solutions. Prompts either include or omit the HumanEval problem description. Models classify code as Correct or Incorrect and return a replacement code block. Unit tests provide an objective correctness oracle for classification and suggested corrections. The mixed set contains 234 correct and 258 incorrect generated blocks; experiments are repeated three times and report means and standard deviations.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | GPT-4o and Gemini assess code correctness for approval/rejection; with problem descriptions, classification accuracy is 68.50% and 63.89%, respectively. | Reported | Abstract; Sections 3–4 |
| RQ2 | GPT-4o corrects 67.83% of incorrect mixed-set blocks versus 54.26% for Gemini; unit tests determine whether a suggestion is correct. | Reported | Abstract; Figure 6 |
| RQ3 | False positives, false negatives, regressions, and faulty corrections are the central failure modes; fully automated review is judged unreliable. | Reported | Section 3; Figures 4–9 |
| RQ4 | Problem descriptions/comments and unit-test context are varied as prompt inputs; performance declines without the description. | Reported | Sections 3–4 |
| RQ5 | The authors propose human-in-the-loop review, with a responsible human deciding when further review is needed. | Proposed | Introduction; Conclusion |
| RQ6 | Unit tests provide functional validation and repeated runs assess stability, but no human evaluation of comments or workflow outcomes is performed. | Reported/limitation | Sections 3–6 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| False-positive approval | Incorrect code is classified as Correct. | Measured | Figure 4/metrics |
| False-negative rejection | Correct code is classified as Incorrect. | Measured | Figure 5/metrics |
| Failed correction | Suggested replacement does not pass all unit tests. | Measured by correction ratio | Section 3; Figure 6 |
| Regression | A suggestion changes a correct block into an incorrect one. | Measured by regression ratio | Section 3; Figure 7/9 |
| Context omission | Missing problem descriptions reduce correctness and correction performance. | Reported comparison | Sections 3–5 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Correctness assessment | Accuracy against unit-test labels | With descriptions: GPT-4o 68.50%, Gemini 63.89% on mixed data. | Abstract; Figure 3 |
| False-positive rate | Incorrect samples accepted as Correct | GPT-4o is lower than Gemini; both worsen without descriptions. | Figure 4 |
| False-negative rate | Correct samples rejected as Incorrect | Model ranking differs from false-positive performance. | Figure 5 |
| Correction effectiveness | Correct suggestions divided by incorrect input blocks | GPT-4o 67.83%, Gemini 54.26% in the mixed experiment. | Figure 6 |
| Regression safety | Incorrect suggestions divided by correct input blocks | GPT-4o 10.43%, Gemini 13.53% in the mixed experiment. | Figure 7 |
| Stability | Standard deviations across three runs | Accuracy SD 0.35–1.61%; other metrics also show nonzero variability. | Section 4 |
| External validity | Ground-truth HumanEval versus mixed AI-generated blocks | Results differ substantially by dataset, limiting universal model ranking. | Section 4 |

## 7. Mitigation and trade-offs

- **Mitigation family:** Include problem descriptions/comments, test prompts on the target codebase, and retain a human approval layer.
- **Intervention point:** Input context, evaluation protocol, and review workflow.
- **What it reduces:** Context-related misclassification and unsafe reliance on unverified corrections.
- **Useful feedback potentially lost:** A strict correctness/correction task does not capture explanatory comments, design concerns, or knowledge-sharing value.
- **Coverage:** Unit tests provide an objective oracle but only cover tested behavior and may miss broader review concerns.
- **Human escalation:** A designated review responsible decides whether an LLM result requires human review.
- **Cost:** Repeated model calls and test execution add operational cost; the paper does not quantify production latency or API cost.
- **New failure modes:** A plausible but test-passing patch may still be undesirable, and a model may reject correct code or introduce regressions.

## 8. Annotation and evaluator validity

- **Oracle:** Unit-test outcomes label correctness and validate suggested code.
- **Dataset:** HumanEval canonical solutions provide a control set; AI-generated blocks create a mixed set with known correctness labels.
- **Repeatability:** Each configuration is run three times; standard deviations are reported.
- **Statistical checks:** A chi-square variance check is reported, with statistics below the stated threshold.
- **Human validity:** No expert review, inter-rater agreement, or developer acceptance study is reported.
- **Threats:** Python-only scope, test-suite incompleteness, stochastic model behavior, dataset-specific distributions, and prompt-design effects.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Research questions and approval/correction task are explicit. |
| Q2 | 2 | HumanEval and mixed datasets are described with counts. |
| Q3 | 2 | Models, prompt variants, labels, and test setup are specified. |
| Q4 | 2 | Accuracy, error rates, correction, regression, and variability are reported. |
| Q5 | 2 | Unit tests provide a clear functional correctness oracle. |
| Q6 | 0 | No human annotation agreement or comment-quality validation. |
| Q7 | 2 | Two models, two context conditions, and two datasets are compared. |
| Q8 | 1 | Repeated runs support stability, but evaluation is Python-only. |
| Q9 | 2 | Context inclusion and human-in-the-loop mitigation are explicit. |
| Q10 | 1 | Operational implications are discussed, but runtime/cost is not quantified. |
| Q11 | 2 | False positives, false negatives, regressions, and corrections are separated. |
| Q12 | 1 | Strong functional test evidence, but weak alignment with natural-language review outcomes. |

**Total: 19/24 — moderate-high confidence for functional correctness and safety trade-offs; limited for human review quality.**

## 10. Review-process reliability and bias

- **Selection uncertainty:** The queue explicitly indicates a possible duplicate/companion relationship with `EXT-0028`; synthesis must deduplicate.
- **Construct validity:** Passing unit tests is treated as correctness, although tests may not cover style, maintainability, security, or architectural concerns.
- **Dataset bias:** AI-generated HumanEval solutions and canonical solutions do not represent repository-scale pull requests.
- **Model/prompt uncertainty:** Results depend on fixed model versions, prompt wording, and the presence of problem descriptions.
- **Missing outcomes:** No accepted-fix rate, reviewer workload, comment usefulness, or longitudinal adoption is measured.
- **Reproducibility:** Data and code are reported as available through Zenodo, but external metadata and duplicate identity require checking.

## 11. Synthesis-ready conclusion

- P108 shows that LLM code-review decisions and corrections remain error-prone even when evaluated against unit tests.
- Problem descriptions or review-context comments materially improve performance, supporting context-quality claims.
- Correction quality must be separated from approval accuracy because unsafe regressions can be introduced into already-correct code.
- The proposed human-in-the-loop process is an appropriate mitigation, but its real workflow benefit is not empirically evaluated.
- Deduplicate against `EXT-0028` before counting or citing this study as an independent record.

