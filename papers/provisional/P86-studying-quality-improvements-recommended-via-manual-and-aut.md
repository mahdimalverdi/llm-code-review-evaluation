# P86 — Studying Quality Improvements Recommended via Manual and Automated Code Review

## 1. Identification

- Project ID: `P86` (provisional)
- Citation key: `p86_crupi2026_studying_quality_improvements_recommended`
- Full reference: Giuseppe Crupi; Rosalia Tufano; Gabriele Bavota. “Studying Quality Improvements Recommended via Manual and Automated Code Review.” ICPC 2026; arXiv:2602.11925v1.
- DOI/URL: `https://doi.org/10.1145/3794763.3794809`; `https://arxiv.org/abs/2602.11925v1`
- Review date: 2026-08-04
- Source/database: arXiv/full-text screening
- Selection stage: included for reconciliation; canonical corpus integration pending
- Duplicate or companion publication: Publisher metadata available; reconcile final record.

## 2. Screening

- Decision: `Include`
- Relevance: `High`
- Decision rationale: Directly compares human and ChatGPT code-review quality improvements and manually assesses unmatched automated findings.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / annotation protocol / mitigation design / trade-off framework
- Exact inclusion criterion: Core inclusion: human-aligned issue detection, false positives, and complementary review use.

## 3. Study overview

- Purpose: Determine which code-quality improvements automated review identifies compared with human reviewers.
- Research questions: Which improvements are recommended by humans and ChatGPT, how often ChatGPT matches them, and whether unmatched comments are meaningful or noise.
- Method: Mining-based study of 739 human comments from 240 PRs; manual taxonomy and comparison with ChatGPT-4 Turbo reviews on the same PRs.
- Evaluated system/artifact: ChatGPT-4 Turbo reviewing Java/Python PR files and diffs; human review comments are the reference.
- Dataset/benchmark: 447 valid human comments from 179 PRs after excluding 292 non-improvement comments; generated ChatGPT reviews contain 1,290 extracted comments.
- Input context: Code files and PR diffs; the main prompt reviews files linked to human comments rather than full repository context.
- Main findings: ChatGPT produces about 2.4× more comments, matches only 10% of human improvements (23% including partial matches), while about 40% of unmatched sampled comments are meaningful.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Human comments are manually categorized into a taxonomy of quality improvements such as refactoring, naming, error handling, and tests. | Reported | Sections 3–4 |
| RQ2 | ChatGPT has similar low match rates across improvement families; 45/447 exact and 103/447 partial matches. | Reported | Section 4 |
| RQ3 | 40% of a sample of 292 unmatched comments recommend meaningful changes, showing output is not merely noise. | Reported | Section 3 |
| RQ4 | Automated review is complementary: it detects additional issues but cannot replace human inspection or save review time under current validation needs. | Reported | Abstract, Section 5 |
| RQ5 | Manual double-labeling, conflict meetings, taxonomy coding, and unmatched-comment inspection provide qualitative validity. | Reported | Section 3 |
| RQ6 | Output volume and partial usefulness create a coverage–validation-burden trade-off. | Inferred | Sections 3–5 |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Missed human improvement | ChatGPT does not recommend the quality improvement in a human comment. | Reported | Section 4 |
| Partial match | Same location/concern but vague or different solution. | Operational category | Section 3 |
| Generic comment | Summarizes the change or asks broad questions without actionable issue. | Reported category | Section 3 |
| Meaningful additional issue | Unmatched automated comment judged to identify a real quality improvement. | Reported | Section 3 |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Human alignment | Exact and partial match to human improvement. | 10% exact, 23% exact+partial. | Section 4 |
| Output volume | Number of generated vs. human comments. | ChatGPT about 2.4× human volume; 1,290 generated comments. | Abstract, Section 3 |
| Meaningfulness | Manual classification of sampled unmatched comments. | About 40% meaningful. | Section 3 |
| Improvement taxonomy | Categories of quality change recommended. | Similar low match across major subtrees. | Section 4 |

## 7. Mitigation and trade-offs

- Mitigation family: Use AI review as a complementary second check after human review.
- Intervention point: Additional review pass after or alongside manual review.
- What it reduces: Risk that human reviewers alone miss quality improvements.
- Useful feedback potentially lost: Filtering automated comments to reduce noise may discard meaningful additional findings.
- Coverage effect: Adds unique issues but misses approximately 77–90% of human recommendations depending on matching definition.
- Human escalation effect: Human validation remains necessary and can eliminate time-saving benefits.
- Computational/operational cost: More comments and validation work increase review burden; monetary cost is not measured.
- New failure modes: Generic/unactionable comments, false positives, and attention diversion.

## 8. Annotation and evaluator validity

- Judge/annotator: Human comments are labeled by two evaluators; ChatGPT output is inspected by authors; conflict resolution involves a third author.
- Rubric: Improvement taxonomy, matched/partially matched/missed, and meaningful/generic/unactionable categories.
- Agreement/reliability: 290/739 initial comments had label conflicts; conflicts were discussed and unresolved cases involved a third author. No formal kappa is reported.
- Validity checks: Statistically sized sample, two-language/project mining, double inspection, conflict meetings, and manual review of unmatched output.
- Possible bias: Human reviewer comments are not an objective complete oracle; manual relevance judgments may depend on project knowledge.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Human/automated comparison target is clear. |
| Q2 | 2 | PR/comment sampling and languages are reported. |
| Q3 | 2 | ChatGPT prompt and review setup are described. |
| Q4 | 2 | Match, volume, meaningfulness, and taxonomy metrics are explicit. |
| Q5 | 2 | Taxonomy and match rubric are defined. |
| Q6 | 1 | Double coding/conflict handling, but no formal kappa. |
| Q7 | 2 | Sampling, double inspection, and conflict resolution are described. |
| Q8 | 1 | Human oracle and project-knowledge limitations remain. |
| Q9 | 1 | Complementary-use recommendation, not a tested mitigation. |
| Q10 | 1 | Burden discussed, cost not measured. |
| Q11 | 2 | Scope, prompting, oracle, and manual-judgment limits are discussed. |
| Q12 | 2 | Directly studies human alignment and useful extra findings. |

- Total: `20/24` provisional
- Quality interpretation: Strong qualitative evidence for complementarity and mismatch, with subjective oracle limitations.

## 10. Review-process reliability and bias

- Missing data: Independent developer usefulness, time impact, complete recall, and cost are not measured.
- Publication-bias concern: Not assessed; one model and curated PR selection limit breadth.
- Selection uncertainty: Included by full-text screening; final ICPC metadata should be reconciled.
- Extraction uncertainty: Moderate due to manual matching and project-context dependence.
- Second-reviewer agreement: Partial double coding reported; SLR agreement not available.
- Duplicate-publication handling: Pending final-version reconciliation.

## 11. Synthesis-ready conclusion

- Contribution to the SLR: Shows that ChatGPT-generated review adds potentially meaningful findings but misses most human-identified quality improvements and increases output volume.
- What the paper does not establish: It does not establish production usefulness, causal time savings, or objective correctness of unmatched findings.
- Research gap supported: Review evaluation should separate human alignment from independent usefulness and measure validation burden.
- Candidate synthesis claims: Automated review is best treated as a complementary quality check, with coverage gains weighed against false positives and human validation cost.
- Follow-up verification needed: Inspect full taxonomy and sampled unmatched-comment labels; replicate with newer models and repository context.
