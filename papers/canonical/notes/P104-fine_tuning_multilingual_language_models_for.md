# P104 — Fine-Tuning Multilingual Language Models for Code Review: An Empirical Study on Industrial C# Projects

> **Provisional intake record.** This is not a canonical paper note.

| Field | Value |
|---|---|
| Project ID | `P104` (provisional) |
| Citation key | `p104_begolli2025_fine_tuning_multilingual_langu` |
| Authors | Igli Begolli; Meltem Aksoy; Daniel Neider |
| Year | 2025 |
| Source | arXiv |
| arXiv | `2507.19271v2` |
| Screening tier | `core` |
| Reconciliation status | New candidate after initial local matching |
| Metadata status | local_arxiv_metadata |
| Evidence status | Full-text eligibility recorded; extraction not yet completed |

## 1. Identification

- Duplicate or companion publication: No publisher venue or DOI is reported; verify before final integration.

## 2. Screening
- Decision: `Include`; Relevance: `High`
- Decision rationale: Directly evaluates language-specific fine-tuning for C# code-review tasks against multilingual baselines, SonarQube, and human reviewers.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: language/context quality / human comparison / efficiency trade-off

## 3. Study overview
- Purpose: Assess whether monolingual C# adaptation improves automated review performance in industrial repositories.
- Research questions: Effects on change-quality estimation (RQ1), review-comment generation across PL/NL configurations (RQ2), code refinement (RQ3), and comparison with ASAT/humans (RQ4).
- Method: Fine-tune CodeReviewer, CodeLlama-7B, and DeepSeek-R1-Distill-Llama-8B using C# industrial/public data and compare automated, human-centered, and time metrics.
- Evaluated system/artifact: C#-adapted CodeReviewer plus CodeLlama and DeepSeek models; SonarQube and six human reviewers as comparison points.
- Dataset/benchmark: Five Lovion industrial C# repositories combined with C# CodeReviewer data; approximately 44,962 quality-estimation samples and task-specific comment/refinement datasets. Translation variants include English-only, English+German, and multilingual data.
- Input context: C# PR diffs, review comments, code changes, reviewer feedback, and refinement targets; QLoRA used for larger instruction models.
- Main findings: Monolingual fine-tuning generally improves C# classification/comment relevance, but refinement benefits do not consistently transfer. Humans remain strongest for semantically complex review; LMs often complete reviews in under one minute versus 3–5 minutes SonarQube and 5–7 minutes humans.

## 4. Evidence mapped to review questions
| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | C# monolingual CodeReviewer improves change-quality estimation relative to multilingual variants, though industrial domain shift reduces performance. | Reported | Sections 4–5.1 |
| RQ2 | Monolingual fine-tuning improves comment generation, but BLEU and human Information/Relevance do not always agree. | Reported | Section 5.2, Table 3 |
| RQ3 | C# fine-tuning can reduce code-refinement BLEU/exact match, likely due to small, narrow training data and translation noise. | Reported | Section 5.3 |
| RQ4 | Humans outperform LMs and SonarQube on comprehensive context-sensitive feedback; ASAT remains useful for rule-based issues. | Reported | Section 5.4, Figures 4–5 |
| RQ5 | Language alignment improves routine/discriminative tasks but may reduce reasoning diversity in reasoning-oriented models. | Inferred | Sections 5.2–5.3 |
| RQ6 | Evaluation should combine BLEU/EM with human information/relevance, correctness, ASAT comparison, and time-to-review. | Inferred | Sections 3.7, 5.4 |

## 5. Failure and problematic-comment categories
| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Context-sensitive miss | Model fails on nuanced logic, architecture, or project-specific conventions. | Reported limitation | Sections 5.4, 7 |
| Rule-only blind spot | SonarQube misses deeper semantic/architectural concerns. | Reported limitation | Section 5.4 |
| Lexical-quality mismatch | High BLEU does not imply informative or relevant feedback. | Reported limitation | Section 5.2 |
| Reasoning degradation | Fine-tuning improves lexical precision but reduces reasoning-rich comments in DeepSeek. | Reported finding | Section 5.2 |
| Translation/language noise | Mixed English/German or translated comments reduce fluency and coherence. | Reported threat | Sections 3.2, 5.2, 7 |

## 6. Evaluation dimensions and metrics
| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Change-quality estimation | Accuracy, precision, recall, F1 for review-needed classification. | Monolingual C# adaptation improves CodeReviewer, but industrial domain shift matters. | Sections 3.7, 5.1 |
| Comment generation | BLEU-4 plus human Information and Relevance ratings. | CodeLlama C# has stronger human alignment; CodeReviewer often has higher BLEU. | Table 3, Section 5.2 |
| Code refinement | BLEU and exact match. | Monolingual fine-tuning can underperform multilingual baseline. | Section 5.3 |
| Human comparison | Issue correctness and six-reviewer ratings. | Humans outperform automated systems on nuanced feedback. | Sections 3.7.2, 5.4 |
| ASAT comparison | SonarQube issue detection and correctness. | Strong on rule-based defects, weak on context-dependent flaws. | Section 5.4 |
| Efficiency | Average time-to-review per PR. | LMs <1 min (except DeepSeek base 1–3); SonarQube 3–5; humans 5–7 min. | Table 4 |

## 7. Mitigation and trade-offs
- Mitigation family: Language/task-specific fine-tuning, QLoRA, and hybrid LM–ASAT–human workflows.
- Intervention point: Training data composition, model adaptation, and workflow routing.
- What it reduces: Language mismatch and routine-review workload.
- Useful feedback potentially lost: Monolingual adaptation may reduce multilingual robustness, reasoning diversity, or refinement generalization.
- Coverage effect: C# specialization improves target-language performance but does not establish cross-language transfer.
- Human escalation effect: Fast LMs and ASATs support triage; humans remain necessary for complex/context-sensitive issues.
- Computational/operational cost: Open models and QLoRA reduce licensing/training cost, but data curation and translation effort are nontrivial.
- New failure modes: Domain shift, translation artifacts, BLEU optimization, and ASAT false positives/semantic blind spots.

## 8. Annotation and evaluator validity
- Judge/annotator: Human review comments from Lovion/CodeReviewer; six bilingual/professional reviewers rate outputs; SonarQube supplies static-analysis baseline.
- Rubric: Review-needed classification, BLEU/EM, Information/Relevance Likert ratings, issue correctness, and functional equivalence.
- Agreement/reliability: Translation validation κ=.82; human evaluation uses consensus/averaging, with no single overall kappa reported in the extracted section.
- Validity checks: Five industrial repositories, public C# data, language variants, 40-PR human-aligned subset, and separate evaluation splits.
- Possible bias: Small proprietary C# corpus, translated German comments, final-hunk negative sampling, model/task asymmetry, and BLEU reliance.

## 9. Quality appraisal
| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Four RQs and industrial setting explicit. |
| Q2 | 2 | Industrial/public datasets and task statistics reported. |
| Q3 | 2 | Models, language configurations, QLoRA, and baselines described. |
| Q4 | 2 | Classification, generation, refinement, human, ASAT, and time metrics reported. |
| Q5 | 2 | Human information/relevance and correctness rubrics defined. |
| Q6 | 1 | Translation agreement clear; human-output agreement less explicit. |
| Q7 | 2 | Multilingual/monolingual variants, ASAT, humans, and task comparisons. |
| Q8 | 1 | C# scope, translation, and industrial-domain limits. |
| Q9 | 2 | Monolingual fine-tuning is directly compared. |
| Q10 | 2 | Time-to-review and open-model efficiency reported. |
| Q11 | 2 | Domain shift, BLEU, translation, and human-bias threats discussed. |
| Q12 | 2 | Direct multi-task industrial code-review evidence. |
- Total: `22/24` provisional
- Quality interpretation: Strong practical comparison evidence, with language/domain and metric-validity constraints.

## 10. Review-process reliability and bias
- Missing data: Exact per-task human scores, monetary cost, longitudinal adoption, and cross-language replication.
- Publication-bias concern: Proprietary industrial corpus and author-reported model comparisons.
- Selection uncertainty: Full text available; final publisher metadata unverified.
- Extraction uncertainty: Moderate because several results are figure-based and detailed table values are difficult to parse.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Check for later venue/version before final bibliography integration.

## 11. Synthesis-ready conclusion
- Contribution to the SLR: Shows that monolingual fine-tuning can improve language-aligned review tasks while speed remains substantially better than humans.
- What the paper does not establish: It does not establish broad language generalization, production acceptance, or replacement of expert review.
- Research gap supported: Evaluation should report language alignment, domain shift, human-centered quality, ASAT complementarity, reasoning preservation, and time trade-offs.
- Candidate synthesis claims: Specialization improves routine/discriminative performance, but may trade away reasoning richness and generalization; hybrid human/LM/ASAT workflows are better supported than full automation.
- Follow-up verification needed: Inspect exact Table 3/Figure 4 values, dataset release/access, and independent C# or multilingual replication.
