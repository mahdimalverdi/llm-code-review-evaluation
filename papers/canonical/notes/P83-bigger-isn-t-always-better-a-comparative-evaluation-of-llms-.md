# P83 — Bigger Isn’t Always Better: A Comparative Evaluation of LLMs for Automated Code Review

## 1. Identification

- Project ID: `P83` (provisional)
- Citation key: `p83_kumar2026_bigger_isn_t_always_better_a_c`
- Full reference: Shivam Pankaj Kumar; Swati Bararia; Kislay Raj. “Bigger Isn’t Always Better: A Comparative Evaluation of LLMs for Automated Code Review.” arXiv:2606.15689v1, 2026.
- DOI/URL: `https://arxiv.org/abs/2606.15689v1`
- Review date: 2026-08-04
- Source/database: arXiv full-text screening
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: Not reported; verify final metadata.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Compares five LLMs on synthetic and real PR review, quantifies quality/cost trade-offs, and diagnoses synthetic-to-real evaluation failure.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: Core inclusion: model evaluation, real-world validity, and review quality trade-offs.

## 3. Study overview

- Purpose: Evaluate model choice and benchmark realism for automated code review.
- Research questions: Compare five models, synthetic vs. real PR performance, bug-category/diff-size effects, ensemble behavior, cost, and qualitative review quality.
- Method: Two-pass deterministic matching plus Claude Opus adjudication; 150 samples: 100 mutation-injected synthetic bugs and 50 real bug-fix PRs.
- Evaluated system/artifact: Claude Sonnet 4.6, Claude Haiku 4.5, GPT-5.4 mini, Minimax M2.7, and GLM-5 Turbo with a common production prompt.
- Dataset/benchmark: TypeScript, Python, and Go samples from eight open-source repositories; independent Martian validation uses 50 real PRs with 136 human-curated comments.
- Input context: PR diffs and structured finding output; synthetic diffs are small (median 5 lines), while real PRs span larger/multi-file changes.
- Main findings: Haiku F1 0.365 vs. Sonnet 0.343 at 3.2× lower cost; synthetic best F1 0.847 vs. real-only best 0.066 (92% drop). F1 drops from 0.657 under 10 lines to 0.043 over 150 lines; performance-bug recall is near zero.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Smaller Haiku outperforms Sonnet on F1, recall, and qualitative dimensions while costing less. | Reported | Abstract, Sections 4–5 |
| RQ2 | Synthetic-only scores overestimate real-world review ability by an order of magnitude. | Reported | Section 4.4 |
| RQ3 | Diff size is dominant; context complexity and multi-file interactions cause sharp degradation. | Reported | Sections 4.3–4.4 |
| RQ4 | Performance bugs/N+1 and unbounded queries receive near-zero recall; security is easier than logic/performance. | Reported | Section 4.2 |
| RQ5 | Two-pass matching and LLM adjudication combine deterministic precision with semantic matching, but judge/ground-truth limits remain. | Reported limitation | Sections 3.2, 5 |
| RQ6 | Model scale, benchmark realism, output volume, recall, and cost form a clear quality–cost trade-off. | Inferred | Sections 4–5 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Performance bug miss | N+1 or unbounded query not detected. | Reported failure | Section 4.2 |
| Large-diff miss | Review quality collapses as changed-line count grows. | Reported failure | Section 4.3 |
| Synthetic overestimate | Mutation-injected, small, familiar bugs inflate measured performance. | Reported benchmark failure | Section 4.4 |
| Verbose/non-actionable output | More findings/tokens do not yield proportional true positives. | Reported behavior | Section 4.7 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Finding quality | Precision, recall, F1, severity-weighted F1. | Haiku F1 0.365; Sonnet 0.343. | Sections 3–4 |
| Qualitative quality | Claude Opus judge scores depth, context awareness, specificity, actionability. | Haiku highest across four dimensions. | Section 4.7 |
| Realism/generalization | Synthetic-only vs. real-only F1. | 0.847 vs. 0.066 best model. | Section 4.4 |
| Complexity sensitivity | F1 by diff-size bucket. | 0.657 under 10 lines vs. 0.043 over 150. | Section 4.3 |
| Efficiency | Cost per review. | Haiku costs $0.003 vs. Sonnet $0.010. | Table 5 |

## 7. Mitigation and trade-offs

- Mitigation family: Real-PR evaluation, diff preprocessing, model selection, and targeted deterministic checks.
- Intervention point: Benchmark/model selection and review pipeline design.
- What it reduces: Optimistic benchmark conclusions and high-cost model use without quality benefit.
- Useful feedback potentially lost: Smaller/cheaper models may be more conservative or miss rare high-severity findings; cost-only selection is unsafe.
- Coverage effect: Ensembles increase output volume but hurt F1 by adding false positives without meaningful true-positive gain.
- Human escalation effect: Human-curated external validation is used, but escalation workflow is not measured.
- Computational/operational cost: Explicit per-review cost and output-token analysis; Sonnet is dominated by Haiku in the reported setting.
- New failure modes: Synthetic benchmark overfitting, large-diff overload, verbose findings, and judge/ground-truth artifacts.

## 8. Annotation and evaluator validity

- Judge/annotator: Deterministic file/line matching plus Claude Opus adjudication; real benchmark includes human-curated golden comments for external validation.
- Rubric: Finding match as true/false/partial, precision/recall/F1, severity weighting, and four qualitative dimensions.
- Agreement/reliability: No inter-rater statistic for golden comments or Claude judge is reported.
- Validity checks: Three sample-size conditions, independent Martian benchmark, common prompt/temperature, synthetic-real stratification, and bug-category analysis.
- Possible bias: Auto-extracted real annotations, one Claude judge for all models, 150-sample benchmark, and model versions fixed to a time point.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Models, task, and evaluation framework are explicit. |
| Q2 | 2 | Synthetic/real composition and repositories are reported. |
| Q3 | 2 | Five models, prompts, and independent benchmark are specified. |
| Q4 | 2 | Quality, realism, complexity, and cost metrics are explicit. |
| Q5 | 2 | Matching/adjudication and qualitative rubric are defined. |
| Q6 | 0 | Inter-rater/judge reliability is absent. |
| Q7 | 2 | Replication conditions, external validation, and ablations are included. |
| Q8 | 2 | Real PR validation and synthetic-real comparison strongly support validity. |
| Q9 | 2 | Benchmark/model/pipeline mitigations are evaluated. |
| Q10 | 2 | Cost per review and output behavior are measured. |
| Q11 | 2 | Ground truth, judge, synthetic gap, and temporal limits are discussed. |
| Q12 | 2 | Directly evaluates automated review quality and deployment trade-offs. |

- Total: `22/24` provisional
- Quality interpretation: Strong comparative evidence, especially for benchmark realism and cost, with judge/annotation reliability limitations.

## 10. Review-process reliability and bias

- Missing data: Human developer usefulness, long-term workflow impact, and exhaustive defect recall are not measured.
- Publication-bias concern: Not assessed; benchmark is small and partly synthetic.
- Selection uncertainty: Included by full-text screening; released artifacts should be reconciled.
- Extraction uncertainty: Moderate due to auto-extracted real ground truth and single judge.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Pending version reconciliation.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Demonstrates that model size is not a reliable proxy for review quality and that synthetic-only evaluation can be severely misleading.
- What the paper does not establish: It does not establish universal superiority of Haiku or complete real-world review quality from F1 alone.
- Research gap supported: Evaluation should use realistic PRs, complexity strata, independent human/agent judges, and cost-normalized quality metrics.
- Candidate synthesis claims: Smaller models may offer a better quality–cost frontier, but benchmark realism and diff complexity dominate apparent capability.
- Follow-up verification needed: Inspect benchmark annotations, prompt, judge protocol, and Martian validation mapping.
