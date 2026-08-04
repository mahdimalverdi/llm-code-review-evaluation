# P23 — Leveraging Reviewer Experience in Code Review Comment Generation

> [!NOTE]
> Compact v2 analysis. P23 is important for our data-quality and human-factor arguments because it uses reviewer authoring/reviewing ownership as a proxy for review-comment quality and evaluates outputs with semantic equivalence, applicability, informativeness, explanation, and issue-type categories.

## Status

- Paper ID: `P23`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `High`
- Reading depth: `Read once from PDF`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | Leveraging Reviewer Experience in Code Review Comment Generation |
| Authors | Hong Yi Lin, Patanamon Thongtanunam, Christoph Treude, Michael W. Godfrey, Chunhua Liu, Wachiraphan Charoenwet |
| Year | 2026 |
| Venue / Source | ACM TOSEM |
| DOI | 10.1145/3762183 |
| Artifact | Zenodo replication package `15400484` |

```bibtex
```

## One-Sentence Summary

> P23 proposes experience-aware loss functions that weight review-comment training examples by reviewer authoring/reviewing ownership, showing improvements in applicable comments, suggestions, explanations, and high-value functional issue categories.

## Main Contribution

The paper argues that not all human review comments should be treated equally. It uses reviewer experience as a data-quality signal and introduces **Experience-Aware Loss Functions (ELF)**, where comments by reviewers with higher authoring/reviewing ownership receive more influence during training.

## Dataset / Study Context

| Field | Value |
|---|---|
| Base dataset | CodeReviewer refinement dataset recovered to PR metadata |
| Final training set | 141,259 examples |
| Validation / test | 12,406 / 12,369 examples |
| Repositories | 826 GitHub repositories; 519 train, 300 validation/test |
| Languages | Nine CodeReviewer languages |
| Metadata recovered | Reviewer ID, timestamp, PR, authoring/reviewing ownership |
| Removed data | Untraceable comments, bots, and code-only suggestions |

## Method

| Component | Details |
|---|---|
| Experience metrics | Authoring Code Ownership (ACO), Review-Specific Ownership (RSO) |
| Granularities | Repository, subsystem, package |
| Training method | ELF weights negative log-likelihood by ownership values |
| Strategies | ACO, RSO, average ACO/RSO, max ACO/RSO at three granularities |
| Models | 12 ELF models + 3 oversampling models + original CodeReviewer |

## Evaluation Method

| Dimension | Metric |
|---|---|
| Text similarity | BLEU-4 over full test set |
| Accuracy | Manual semantic equivalence and applicability on 100 samples |
| Informativeness | Suggestion, concern, confused question |
| Explanation | Presence of rationale |
| Issue type | 15 comment categories grouped into functional, evolvability, discussion |
| Reliability | Cohen’s kappa reported for manual tasks, often ≥0.8 after guideline refinement |

## Key Findings

| Finding | Summary |
|---|---|
| F1 | ELF models achieve up to +5% BLEU-4 over CodeReviewer. |
| F2 | ELF models generate up to +29% applicable comments. |
| F3 | ELF generates up to +56% more suggestions. |
| F4 | ELF generates up to −71% fewer confused questions. |
| F5 | ELF generates up to +125% more comments with rationales. |
| F6 | ELF identifies up to +129% more functional issues. |
| F7 | ELF identifies up to +600% more documentation issues. |
| F8 | Package-level ACO and RSO are strong and complementary. |
| F9 | Experienced reviewers provide more suggestions/explanations and focus more on critical issues. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Applicability | High | Stronger than BLEU because it allows alternative useful comments. |
| Semantic equivalence | High | Compares intent to reference. |
| Informativeness | High | Suggestion/concern/confused question. |
| Explanation quality | High | Presence of rationale. |
| Issue-type usefulness | High | Functional/evolvability/discussion categories. |
| Reviewer experience | Very high | Central data-quality proxy. |
| Correctness | Medium | Applicability partly captures correctness. |
| Workflow impact | Low | No live deployment. |

## Problematic Comment / Review Types

- Confused question.
- Non-applicable generated comment.
- Low-informativeness comment.
- Comment without rationale.
- Trivial visual-representation issue.
- Comment from low-experience reviewer that focuses on superficial issues.
- Code-only suggestion that causes model collapse if used raw.
- Ambiguous comment requiring project-specific context.

## Context/Data-Quality Evidence

P23 shows that reference comments encode reviewer expertise. Dataset quality is not only about text clarity or relevance; it is also about **who produced the comment** and what code ownership/domain knowledge they had. This is a valuable extension to our data-quality model.

## Trade-off Extraction

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| Experience-weighted loss | Prioritizes likely higher-quality comments. | Reviewer experience is only a proxy and can be noisy. |
| Package-level ownership | Captures local expertise and high-value issues. | Depends on source-tree granularity, not true architecture. |
| Reviewer-author distinction | ACO and RSO elicit complementary comments. | Requires complete repository history. |
| Removing code-only suggestions | Prevents mode collapse. | May remove useful direct fixes. |
| Manual evaluation | Captures applicability/informativeness. | Small sample and costly. |

## Relevance to Our Paper

P23 should be cited in the data-quality and human-ground-truth validity sections. It supports the argument that human comments vary in quality and that evaluator frameworks should consider reviewer expertise, applicability, issue type, explanation, and informativeness.

## Limitations from Our Perspective

- Experience is a proxy, not direct quality ground truth.
- Open-source GitHub only; may not generalize to closed-source review culture.
- Manual evaluation uses only 100 samples.
- Applicability still depends on available project context.
- Ownership approximates architecture imperfectly.

## Follow-up TODOs

- [ ] Add reviewer-experience quality signal to `synthesis/context-quality.md` or data-quality layer.
- [ ] Add applicability/informativeness/explanation to `synthesis/evaluation-dimensions.md`.
- [ ] Add confused-question and low-expertise/superficial-review types to taxonomy.
- [ ] Update `matrices/cross-paper-synthesis.md` with P23 evidence.
## Legacy proposal-aligned quality appraisal (superseded by the canonical record)

P23 is **Supporting/Core / High relevance**. It supports RQ1 through low-value and reviewer-burden-related feedback types; RQ2–RQ3 through developer-centered usefulness and attention; RQ4 through value versus reviewer time; and RQ5–RQ6 through human-centered annotation and framework design.

**Quality score: 21/24.** Q1–Q7=2, Q8=1, Q9=1, Q10=2, Q11=1, Q12=2. It is not an LLM mitigation study, so its direct evidence for RQ3 is limited.
## Canonical citation record

Use citation key `p23_lin2026_reviewer_experience` from `references/references.bib`; do not duplicate its BibTeX entry in this note.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p23_lin2026_reviewer_experience`; Supporting; Include; High relevance.
- Study overview: Reviewer experience is used to weight or interpret review-comment usefulness and reviewer value.
- RQ1: Low-value, confusing, or experience-dependent feedback (Reported/Our perspective).
- RQ2: Reviewer expertise and project context affect usefulness (Reported).
- RQ3: Usefulness, reviewer attention, actionability, and experience-sensitive evaluation (Reported).
- RQ4: Value-to-attention and reviewer-burden trade-offs (Reported).
- RQ5: Human-centered annotation and construct validity (Reported).
- RQ6: Strong usefulness and workflow framework support.
- Failure taxonomy: low-value; confusing; expertise-mismatched; attention-inefficient feedback.
- Metrics: usefulness, reviewer experience, attention/time, and experience-conditioned quality.
- Mitigation/trade-off: reviewer-experience weighting; may personalize value but reduce comparability and add burden.
- Validity: human preference is not identical to correctness or actionability.
- Quality: 21/24; strong supporting evidence.
- Synthesis conclusion: supports separating usefulness from correctness and measuring reviewer burden.

### 1. Identification
- P23; `p23_lin2026_reviewer_experience`; local full PDF; included; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p23_lin2026_reviewer_experience`; Supporting; Include; High relevance.
### 3. Study overview
Reviewer experience is used to weight or interpret review-comment usefulness and reviewer value.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Low-value, confusing, or experience-dependent feedback (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Reviewer expertise and project context affect usefulness (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Usefulness, reviewer attention, actionability, and experience-sensitive evaluation (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Value-to-attention and reviewer-burden trade-offs (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Human-centered annotation and construct validity (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong usefulness and workflow framework support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| low-value | Reported/Inferred | Full PDF |
| confusing | Reported/Inferred | Full PDF |
| expertise-mismatched | Reported/Inferred | Full PDF |
| attention-inefficient feedback. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| usefulness | Not an end-to-end outcome | Full PDF |
| reviewer experience | Not an end-to-end outcome | Full PDF |
| attention/time | Not an end-to-end outcome | Full PDF |
| and experience-conditioned quality. | Not an end-to-end outcome | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: reviewer-experience weighting; may personalize value but reduce comparability and add burden.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: partial; useful-issue retention after intervention is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- human preference is not identical to correctness or actionability.
- Q7–Q8 encode judging and reliability depth.
### 9. Quality appraisal
| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 | 2 | goal at scored depth. |
| Q2 | 2 | artifact at scored depth. |
| Q3 | 2 | dataset/context at scored depth. |
| Q4 | 2 | procedure at scored depth. |
| Q5 | 2 | metrics at scored depth. |
| Q6 | 2 | failures at scored depth. |
| Q7 | 2 | judging at scored depth. |
| Q8 | 1 | reliability at scored depth. |
| Q9 | 1 | intervention at scored depth. |
| Q10 | 2 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 21/24; reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence and selection/publication bias remain explicit; second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Reviewer experience is used to weight or interpret review-comment usefulness and reviewer value.
- Boundary: supports separating usefulness from correctness and measuring reviewer burden.
