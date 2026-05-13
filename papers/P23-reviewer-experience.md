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
% TODO: Add checked ACM BibTeX.
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
