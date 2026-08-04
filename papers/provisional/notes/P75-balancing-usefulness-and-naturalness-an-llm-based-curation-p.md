# P75 — Balancing Usefulness and Naturalness: An LLM-based Curation Pipeline for Code Review Comments

## 1. Identification

- Project ID: `P75` (provisional)
- Citation key: `p75_sghaier2026_balancing_usefulness_and_natur`
- Full reference: Oussama Ben Sghaier; Martin Weyssow; Houari Sahraoui. “Balancing Usefulness and Naturalness: An LLM-based Curation Pipeline for Code Review Comments.” Empirical Software Engineering, accepted 6 July 2026; arXiv:2607.09524v1.
- DOI/URL: `https://arxiv.org/abs/2607.09524v1`
- Review date: 2026-08-04
- Source/database: arXiv full-text screening
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: Accepted manuscript and arXiv version require final metadata reconciliation.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Directly evaluates LLM-based curation of review-comment datasets across quality dimensions, downstream generation/refinement, and the standardization–diversity trade-off.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: Core inclusion: generated review comments, dataset validity, and mitigation trade-offs.

## 3. Study overview

- Purpose: Improve review-comment quality and downstream utility while preserving natural stylistic variation.
- Research questions: RQ1 characterizes the original dataset; RQ2 evaluates curation quality; RQ3 compares diversity; RQ4 tests comment generation; RQ5 tests code refinement.
- Method: LLM-as-a-Judge assessment, two LLM curation pipelines, diversity analysis, and fine-tuning experiments on comment generation and code refinement.
- Evaluated system/artifact: CuREV reformulates relevant comments for clarity, conciseness, and civility; CuREV+ preserves high-quality comments and reformulates poorer comments using high-quality in-context exemplars.
- Dataset/benchmark: 176,613 multilingual samples across nine languages from the Li et al. code-review dataset; filtering removes 5,895 low-relevance comments, leaving 170,718.
- Input context: Old/new code pairs and associated review comments. CuREV+ preserves 92,894 good comments and reformulates 77,824 poorer comments.
- Main findings: CuREV+ reaches clarity 8.95, conciseness 8.53, civility 8.53, Self-BLEU 0.1431, CodeBLEU 0.49, and Exact Match 463.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Comments are assessed for relevance, clarity, conciseness, civility, nature, and type. | Reported | Sections 2.1, 3.1–3.2 |
| RQ2 | CuREV and CuREV+ improve clarity and conciseness; CuREV+ is selective rather than fully reformulating. | Reported | Section 4, Table 10 |
| RQ3 | CuREV+ has richer lexical/style diversity and lower repetition: Self-BLEU 0.1431 vs. 0.2466 for CuREV. | Reported | Section 5, Table 14 |
| RQ4 | Fine-tuned DeepSeek-Coder-6.7B BLEU: original 7.71, CuREV 11.26, CuREV+ 11.05. | Reported | Section 6.1, Table 17 |
| RQ5 | Code refinement improves from CodeBLEU 0.36/EM 408 to 0.49/463 with CuREV+. | Reported | Section 6.2, Table 18 |
| RQ6 | Selective exemplar-guided reformulation balances quality and natural stylistic diversity. | Inferred | Sections 4–6 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Low relevance/no actionable review | Comments below the relevance threshold are removed before reformulation. | Reported pipeline category | Section 4 |
| Poor clarity/conciseness/civility | Low-scoring comments are reformulated while intended meaning is to be preserved. | Reported pipeline category | Sections 3–4 |
| Over-standardization | Reformulating every comment can homogenize style and reduce natural variability. | Reported limitation | Sections 1, 4 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Quality | Llama-3.1-70B-Instruct scores relevance, clarity, conciseness, civility, nature, and type. | CuREV+ clarity 8.95, conciseness 8.53, civility 8.53. | Sections 3–4, Table 10 |
| Diversity | Type–token ratio, n-gram diversity, entropy, and Self-BLEU. | Self-BLEU 0.1431 vs. 0.2466 for CuREV. | Section 5, Table 14 |
| Comment generation | BLEU after fine-tuning DeepSeek-Coder-6.7B-Instruct. | 7.71 → 11.26 / 11.05 for CuREV / CuREV+. | Section 6.1, Table 17 |
| Code refinement | CodeBLEU and Exact Match on generated code diffs. | 0.36/408 → 0.49/463 with CuREV+. | Section 6.2, Table 18 |

## 7. Mitigation and trade-offs

- Mitigation family: Training-data curation and exemplar-guided reformulation.
- Intervention point: Offline dataset preparation before model fine-tuning.
- What it reduces: Irrelevant, unclear, verbose, uncivil, and poorly structured training comments.
- Useful feedback potentially lost: 5,895 low-relevance comments are removed; valid uncommon feedback is not separately checked.
- Coverage effect: Dataset size falls from 176,613 to 170,718; issue-type coverage is not evaluated separately.
- Human escalation effect: Not measured.
- Computational/operational cost: Dataset-scale LLM judging/reformulation is used, but monetary or latency cost is not reported.
- New failure modes: Reformulation may alter semantic intent; uniform CuREV phrasing can reduce stylistic diversity; LLM judging can introduce evaluator bias.

## 8. Annotation and evaluator validity

- Judge/annotator: Llama-3.1-70B-Instruct evaluates the full dataset; two human annotators independently assess a random sample of 100 comments.
- Rubric: Relevance, clarity, conciseness, civility, nature, and type; prompts require semantic-intent preservation plus improved form.
- Agreement/reliability: Human–LLM Cohen’s kappa includes civility 1.00, type 0.88, nature 0.82, and relevance 0.85; independent-LLM cross-architecture correlation is about 0.60 on N=1,668.
- Validity checks: Prompt iteration, human baseline comparison, weighted agreement analysis, independent-model cross-check, and released datasets/replication packages.
- Possible bias: Limited human sample, LLM-as-a-Judge self-evaluation risk, and rubric-defined quality may not represent all developer preferences.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Dataset, quality dimensions, and curation objectives are explicit. |
| Q2 | 2 | 176,613 multilingual samples and filtering are reported. |
| Q3 | 2 | Judge, human sample, and downstream model setups are described. |
| Q4 | 2 | Quality, diversity, BLEU, CodeBLEU, and EM are operationalized. |
| Q5 | 2 | Rubric and reformulation constraints are specified. |
| Q6 | 2 | Human–LLM kappa and independent-LLM correlation are reported. |
| Q7 | 2 | Prompt iteration, human baseline, and cross-model checks are described. |
| Q8 | 1 | Checks exist, but independent-LLM correlation is only moderate. |
| Q9 | 2 | Two explicit data-curation interventions are compared. |
| Q10 | 1 | Downstream effectiveness is measured, but curation cost is not. |
| Q11 | 2 | Homogenization, semantic drift, and evaluator-bias concerns are discussed. |
| Q12 | 2 | Directly evaluates quality, diversity, usefulness, and preservation trade-offs. |

- Total: `22/24` provisional
- Quality interpretation: Strong curation and downstream-evaluation evidence, with residual concerns about LLM judging and unreported operational cost.

## 10. Review-process reliability and bias

- Missing data: Human evaluation of downstream usefulness, semantic drift at scale, and curation cost is not reported.
- Publication-bias concern: Positive results may be influenced by BLEU/CodeBLEU sensitivity to reformulated references; not independently assessed.
- Selection uncertainty: Included by full-text screening; accepted manuscript and arXiv metadata should be reconciled.
- Extraction uncertainty: Moderate due to LLM annotation and limited manual sample.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Pending publisher/version reconciliation.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Selective exemplar-guided curation improves review-comment quality and code-refinement utility while preserving more stylistic diversity than uniform reformulation.
- What the paper does not establish: It does not establish greater usefulness to human reviewers, guaranteed semantic preservation, or improved real-world review outcomes.
- Research gap supported: Curation should jointly evaluate quality, semantic fidelity, stylistic diversity, and downstream usefulness rather than optimize surface clarity alone.
- Candidate synthesis claims: CuREV+ offers a quality–naturalness trade-off by retaining good human comments and reformulating poorer ones, but automated metrics and LLM judging remain incomplete proxies.
- Follow-up verification needed: Reconcile publication metadata and inspect released CuREV/CuREV+ artifacts for exact filtering and training splits.
