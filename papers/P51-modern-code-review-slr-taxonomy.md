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
