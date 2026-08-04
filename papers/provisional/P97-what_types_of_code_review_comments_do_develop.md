# P97 — What Types of Code Review Comments Do Developers Most Frequently Resolve?

> **Provisional intake record.** This is not a canonical paper note.

| Field | Value |
|---|---|
| Project ID | `P97` (provisional) |
| Citation key | `p97_goldman2025_what_types_of_code_review_comm` |
| Authors | Saul Goldman; Hong Yi Lin; Jirat Pasuksmit; Patanamon Thongtanunam; Kla Tantithamthavorn; Zhe Wang; Ray Zhang; Ali Behnaz; Fan Jiang; Michael Siers; Ryan Jiang; Mike Buller; Minwoo Jeong; Ming Wu |
| Year | 2025 |
| Source | arXiv |
| arXiv | `2510.05450v1` |
| Screening tier | `core` |
| Reconciliation status | New candidate after initial local matching |
| Metadata status | local_arxiv_metadata |
| Evidence status | Full-text eligibility recorded; extraction not yet completed |

## 1. Identification

- Duplicate or companion publication: No publisher venue or DOI is reported; verify before final integration.

## 2. Screening
- Decision: `Include`; Relevance: `High`
- Decision rationale: Directly studies LLM-generated review-comment types and developer resolution in OSS and enterprise projects.
- Protocol deviation or amendment: None reported.
- Inclusion group: `Core`
- Proposal deliverable supported: taxonomy / actionability / human-outcome evaluation

## 3. Study overview
- Purpose: Identify which types of LLM-generated comments are produced and which are acted on by developers.
- Research questions: Compare human and LLM comment-type distributions (RQ1) and measure resolution rates by generated-comment type (RQ2).
- Method: Construct a six-category taxonomy, use GPT-4.1 as an LLM judge, compare human/LLM comments, and analyze subsequent code changes for 4,000 generated comments.
- Evaluated system/artifact: RovoDev Agent via Claude 3.5 Sonnet, evaluated on Atlassian internal repositories and OSS projects.
- Dataset/benchmark: 300 internal merged PRs with 465 human comments; 1,000 human comments from CuRev; generated sets of 702 internal and 1,256 OSS comments; online evaluation samples 4,000 generated comments across 3,746 PRs and 1,007 repositories.
- Input/context: Review comments anchored to exact code lines; resolution means a subsequent commit modified the commented line.
- Main findings: Resolution was 43.3% for readability, 41.9% for bugs, 36.2% for maintainability, and 28.6% for design. LLM comments were more bug/maintainability-oriented internally but less readability-oriented than human comments.

## 4. Evidence mapped to review questions
| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | LLM and human reviewers emphasize different categories, with context-dependent differences across Atlassian and OSS. | Reported | Section IV, Figures 3–4 |
| RQ2 | Readability, bug, and maintainability comments are resolved more often than design comments; 60–70% remain unresolved. | Reported | Section IV, Figure 5 |
| RQ3 | Category coverage and actionability provide outcome-oriented evaluation beyond lexical similarity metrics. | Inferred | Section V |
| RQ4 | Human and LLM reviewers appear complementary rather than interchangeable. | Inferred | Section V |
| RQ5 | Resolution is an observable behavioral proxy, but line modification can conflate agreement, incidental edits, and developer workflow. | Limitation | Section IV, Threats |
| RQ6 | Evaluation should report category distribution, resolution/actionability, context, and judge reliability. | Inferred | Sections III–VI |

## 5. Failure and problematic-comment categories
| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Unresolved comment | Developer does not modify the exact commented line in a later commit. | Reported outcome | Section IV |
| Low-clarity/low-relevance feedback | Authors suggest unresolved comments may lack clarity, relevance, or simplicity. | Interpretation | Section IV |
| Design-actionability gap | Architectural/design suggestions require broader context and larger changes, lowering resolution. | Reported interpretation | Section IV |
| Category imbalance | Bug comments are underrepresented in LLM output despite being actionable. | Reported finding | Abstract, Section V |
| Judge misclassification | GPT-4.1 taxonomy assignment may differ from human labeling or another judge. | Threat | Section VI |

## 6. Evaluation dimensions and metrics
| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Comment taxonomy | Code Readability, Code Bugs, Maintainability, Code Design, No Issue, Other. | Six categories developed by six engineers; no inter-rater agreement during card sorting. | Section III-B, Table I |
| Distribution | Category proportions for human vs LLM comments. | Internal LLM: bugs 18.2% vs human 6.5%; maintainability 26.8% vs 19.1%; readability 33.2% vs 46.0%. OSS LLM maintainability 37.9% vs human 23.6%. | Section IV, Figures 3–4 |
| Actionability | Exact-line resolution rate after a subsequent commit. | Readability 43.3%, bugs 41.9%, maintainability 36.2%, design 28.6%. | Section IV, Figure 5 |
| Judge reliability | Cohen’s kappa against human annotations. | Human annotators κ=.80/.86 by round; judge agreement κ=.42. | Section III-C |
| Context/generalization | Internal Atlassian plus OSS projects. | Findings limited to 13 OSS and 1,007 internal projects and one proprietary reviewer. | Section VI |

## 7. Mitigation and trade-offs
- Mitigation family: Taxonomy-aware monitoring and balancing of generated comment types; outcome-based evaluation.
- Intervention point: Generation policy, category coverage, comment clarity, and product evaluation.
- What it reduces: Overreliance on lexical similarity and under-detection of actionable bug comments.
- Useful feedback potentially lost: Optimizing for line-level resolution may favor local edits and undervalue design or discussion comments that are useful without immediate code change.
- Coverage effect: Taxonomy exposes category imbalance, but six categories may omit domain-specific or cross-category concerns.
- Human escalation effect: Design comments may need discussion or broader architectural review rather than immediate line edits; resolution metric does not capture this.
- Computational/operational cost: LLM judging and large-scale comment classification are required; costs are not reported.
- New failure modes: Judge category errors, line-anchoring bias, and optimization toward easily resolved comments.

## 8. Annotation and evaluator validity
- Judge/annotator: Six engineers develop the taxonomy; two annotators label 100 comments over two rounds, with a third arbiter; GPT-4.1 classifies the large corpus.
- Rubric: Six mutually exclusive categories with definitions and justification/confidence in JSON output.
- Agreement/reliability: Human rounds κ=.80 and .86; LLM judge agreement κ=.42, described as moderate.
- Validity checks: Prompt refinement, human sanity check, arbiter resolution, and experiments with another LLM reportedly yielded consistent results.
- Possible bias: Proprietary RovoDev/Claude setup, internal Atlassian norms, line-change resolution proxy, and LLM-as-judge classification.

## 9. Quality appraisal
| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Questions, taxonomy, and outcome are explicit. |
| Q2 | 2 | Internal, OSS, generated, and resolution samples are reported. |
| Q3 | 2 | Reviewer, judge, sampling, and line-resolution procedure described. |
| Q4 | 2 | Distribution, resolution, and agreement metrics reported. |
| Q5 | 2 | Six-category taxonomy is defined. |
| Q6 | 2 | Human agreement and judge agreement are reported. |
| Q7 | 2 | Two contexts and triangulated datasets are used. |
| Q8 | 1 | Proprietary reviewer and resolution proxy constrain validity. |
| Q9 | 1 | Taxonomy is an evaluation framework, not a tested intervention. |
| Q10 | 1 | Operational classification cost is not reported. |
| Q11 | 2 | Judge, context, and generalization threats are discussed. |
| Q12 | 2 | Direct behavioral evidence concerns generated review comments. |
- Total: `21/24` provisional
- Quality interpretation: Strong outcome-oriented evidence for comment type and resolution, with moderate judge agreement and limited causal inference.

## 10. Review-process reliability and bias
- Missing data: Comment acceptance rationale, dismissal reasons, reviewer effort, time-to-resolution, and costs.
- Publication-bias concern: Author-affiliated Atlassian data and proprietary reviewer may favor the studied workflow.
- Selection uncertainty: Full text available; final publication metadata unverified.
- Extraction uncertainty: Moderate because exact category counts for some plots are not fully tabulated.
- Second-reviewer agreement: Not available for this note.
- Duplicate-publication handling: Check for a later venue/version before bibliography integration.

## 11. Synthesis-ready conclusion
- Contribution to the SLR: Demonstrates that comment type and subsequent developer resolution are useful complements to lexical similarity for evaluating LLM review feedback.
- What the paper does not establish: It does not establish that resolution proves comment correctness, nor that findings generalize across reviewers, models, or organizations.
- Research gap supported: Evaluation should distinguish comment category, immediate actionability, architectural usefulness, and unresolved-comment causes.
- Candidate synthesis claims: Readability, bug, and maintainability feedback is more likely to trigger local code changes than design feedback, but this may reflect the resolution proxy rather than intrinsic usefulness.
- Follow-up verification needed: Inspect category distributions, exact Figure 5 denominators, and released annotation/prompt artifacts if available.
