# P51 — A Systematic Literature Review and Taxonomy of Modern Code Review

## Metadata

- **ID:** P51
- **Title:** A Systematic Literature Review and Taxonomy of Modern Code Review
- **Authors:** Nicole Davila, Ingrid Nunes
- **Year:** 2021
- **Venue:** Journal of Systems and Software / Elsevier
- **Official URL:** https://www.sciencedirect.com/science/article/abs/pii/S0164121221000480
- **DOI:** 10.1016/j.jss.2021.110951
- **arXiv:** 2103.08777
- **Drive PDF:** https://drive.google.com/file/d/1EJcD6PRhcJWTCCFRhxbLAadffcLWVmik
- **Drive PDF filename:** P51_modern_code_review_slr_taxonomy.pdf
- **BibTeX key:** `p51_davila2021_mcr_slr_taxonomy`

## Status

- **Review status:** Deep read completed
- **Verification status:** Official publisher page verified from user-provided ScienceDirect link; Drive PDF available and read.
- **Priority:** High

## Why This Paper Matters

This paper strengthens the non-LLM foundation of our article. It defines modern code review as a flexible, asynchronous, tool-supported, socio-technical practice and gives a broad taxonomy of modern code review research.

It is especially useful for our paper because it shows that modern code review is not only about defect detection. It is also about code improvement, learning, knowledge sharing, collective ownership, reviewer interaction, and process quality. This directly supports our argument that evaluating LLM-generated review comments only with isolated correctness or exact-match metrics is too narrow.

The paper also gives a methodological precedent for our work: it derives a taxonomy from a structured evidence synthesis and explicitly separates foundational studies, support proposals, and evaluations.

## Expected Use in Our Paper

Use this paper mainly in:

- `drafts/paper/sections/02-background.md`
- `drafts/paper/sections/03-related-work.md`
- `drafts/paper/sections/04-methodology.md`
- `drafts/paper/sections/05-operational-taxonomy.md`
- `drafts/paper/sections/10-threats-to-validity.md`

Specific use:

- In **Background**, cite it for the definition and process model of modern code review.
- In **Related Work**, cite it to position LLM-based review automation inside the broader MCR support-tool literature.
- In **Methodology**, cite it as a precedent for taxonomy-oriented evidence synthesis.
- In **Taxonomy/Framework**, cite it to justify evaluating review support beyond accuracy.
- In **Threats**, cite it for the limitations of subjective coding and incomplete evidence coverage.

## Extraction Targets

When reading the paper, extract:

1. How modern code review is defined.
2. What major categories or taxonomy dimensions the SLR identifies.
3. What evaluation gaps are reported for modern code review tools.
4. Whether offline evaluation dominates over human-subject or workflow evaluation.
5. How the paper constructs or validates its taxonomy.
6. Any threat-to-validity discussion relevant to our focused evidence synthesis.

## Relevance to Our Framework

Potential links to our framework:

- socio-technical value of review;
- review goals beyond defect detection;
- taxonomy construction as a methodological precedent;
- motivation for evaluating review tools beyond isolated accuracy metrics;
- distinction between support tools, automation, and evaluation settings;
- context quality as a prerequisite for useful review feedback;
- workflow impact as a first-class evaluation dimension.

## Initial Notes

This paper should be used as a background and methodological anchor, not as a core LLM-code-review paper. It can help justify why our contribution is framed as a taxonomy plus framework rather than as another model comparison.

Deep-read summary:

- The review starts from 825 retrieved papers and selects 139 primary studies.
- The selected studies are grouped into three major categories: foundational studies, proposals, and evaluations.
- The paper defines a typical MCR process with preparation, reviewer selection, reviewer notification, code checking, reviewer interaction, and review decision.
- LLM-generated review comments mainly intervene in code checking and reviewer interaction, but their consequences can affect review decision, rework, and reviewer burden.

Important extracted claims:

- MCR is flexible, tool-supported, asynchronous, and socio-technical.
- MCR has value beyond defect detection: code quality, learning, knowledge sharing, and collective ownership matter.
- Understanding the code change, its motivation, and its rationale is a central challenge for reviewers.
- Review feedback is valuable when it gives authors an opportunity to improve code or learn.
- Review feedback is heterogeneous: it can involve code improvement, understanding, social communication, defects, design, security, architecture, and confusion.
- Missing rationale, non-functional-requirement discussions, and lack of familiarity with code are frequent sources of confusion.
- Many MCR-supporting approaches are evaluated offline with historical data; human-subject and workflow-centered evaluations are less common.

Concrete connection to our argument:

- The paper shows that even before LLM-based review generation, MCR research had a gap between the socio-technical nature of review and the offline, metric-centered evaluation of support tools.
- Our paper extends this gap to LLM-generated review comments and argues for a decision-oriented, trade-off-aware evaluation framework.

Limitations when using this source:

- It covers MCR literature up to 2019 and does not address the recent LLM wave directly.
- Its taxonomy is about MCR research as a field, not about problematic generated comments.
- It is best used as conceptual and methodological grounding, not as evidence about LLM hallucination.

## TODO

- [x] Read the PDF.
- [x] Extract taxonomy dimensions.
- [x] Extract methodology details.
- [x] Extract evaluation gaps.
- [x] Map findings to Background and Related Work.
- [x] Map findings to taxonomy/framework motivation.
- [x] Confirm final BibTeX from publisher export.
- [ ] Add precise claims and citations to Background.
- [ ] Add precise claims and citations to Methodology if useful.
## Legacy quality appraisal (superseded by the canonical record)

P51 is **Supporting / High relevance**. It supports RQ1–RQ3 through a modern-code-review taxonomy, RQ4 through workflow and review-cost dimensions, RQ5 through review-study methodology, and RQ6 through taxonomy construction. It is not LLM-specific.

**Quality score: 20/24.** Q1–Q5=2, Q6=2, Q7=1, Q8=1, Q9=0, Q10=1, Q11=2, Q12=2.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p51_davila2021_mcr_slr_taxonomy`; Supporting; Include; High relevance.
- Study overview: Systematic literature review and taxonomy of modern code review.
- RQ1: Review-process, comment, and outcome categories from pre-LLM research (Reported).
- RQ2: Review context, usefulness, quality, and workflow dimensions (Reported).
- RQ3: Taxonomy and activity classification for review research (Reported).
- RQ4: Review benefit versus effort, delay, and process cost (Reported).
- RQ5: Direct methodological and taxonomy support.
- RQ6: Strong support for taxonomy construction and SLR positioning.
- Failure taxonomy: process friction, low-value feedback, review delay, and activity-specific failures.
- Metrics: review outcomes, process measures, usefulness, and taxonomy frequencies.
- Mitigation/trade-off: review practices and automation boundaries; no LLM gate.
- Validity: secondary-study search/selection and coding reliability must be checked.
- Quality: 20/24; high-value supporting SLR.
- Synthesis conclusion: foundational vocabulary and justification for separating comment, context, workflow, and evaluator failures.

### 1. Identification
- P51; `p51_davila2021_mcr_slr_taxonomy`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p51_davila2021_mcr_slr_taxonomy`; Supporting; Include; High relevance.
### 3. Study overview
Systematic literature review and taxonomy of modern code review.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Review-process, comment, and outcome categories from pre-LLM research (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Review context, usefulness, quality, and workflow dimensions (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Taxonomy and activity classification for review research (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Review benefit versus effort, delay, and process cost (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Direct methodological and taxonomy support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong support for taxonomy construction and SLR positioning. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| process friction, low-value feedback, review delay, and activity-specific failures. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| review outcomes | Does not alone establish deployment value | Full PDF |
| process measures | Does not alone establish deployment value | Full PDF |
| usefulness | Does not alone establish deployment value | Full PDF |
| and taxonomy frequencies. | Does not alone establish deployment value | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: review practices and automation boundaries; no LLM gate.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- secondary-study search/selection and coding reliability must be checked.
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
| Q7 | 1 | judging at scored depth. |
| Q8 | 1 | reliability at scored depth. |
| Q9 | 0 | intervention at scored depth. |
| Q10 | 1 | trade-offs at scored depth. |
| Q11 | 2 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 19/24; calibrated reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence and selection/publication bias remain explicit; independent second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Systematic literature review and taxonomy of modern code review.
- Boundary: foundational vocabulary and justification for separating comment, context, workflow, and evaluator failures.
