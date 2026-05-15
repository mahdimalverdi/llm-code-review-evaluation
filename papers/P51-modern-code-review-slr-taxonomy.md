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

## One-Sentence Takeaway

This paper is a strong foundation for our Background and Methodology because it frames modern code review as a flexible, tool-supported, asynchronous, socio-technical practice and shows that most evaluations of MCR-supporting approaches are offline rather than workflow- or human-centered.

## What the Paper Does

Davila and Nunes conduct a systematic literature review of modern code review (MCR). Their goal is to structure the MCR literature and identify what is known about the practice, what kinds of support tools have been proposed, and how those tools have been evaluated.

The review starts from 825 retrieved papers and selects 139 primary studies. The selected studies are organized into three major categories:

1. **Foundational studies**: studies that analyze existing or collected MCR data to understand the practice.
2. **Proposals**: techniques, tools, or methods proposed to support MCR.
3. **Evaluations**: studies that assess or compare MCR-supporting approaches.

This three-way distinction is useful for our own paper because we also need to separate background evidence, proposed mitigation/evaluation artifacts, and evaluation practice.

## Definition and Characterization of Modern Code Review

The paper characterizes MCR as a flexible, tool-supported, asynchronous process. A typical MCR process includes:

1. **Preparation**: the author prepares the changed code and a description of the change.
2. **Reviewer selection**: candidate reviewers are selected.
3. **Reviewer notification**: selected reviewers are invited.
4. **Code checking**: reviewers inspect the changed code.
5. **Reviewer interaction**: reviewers and authors discuss feedback.
6. **Review decision**: the change is accepted, rejected, or sent back for rework.

This process view is useful for our framework because LLM-generated review comments intervene mainly in the **Code Checking** and **Reviewer Interaction** stages, but their impact also affects **Review Decision**, reviewer burden, and possible rework.

## Foundational Findings Relevant to Our Paper

### Code review has value beyond defect detection

The review finds that MCR is expected to improve code quality and defect detection, but it also supports knowledge sharing, learning, collective ownership, and discussion of alternative solutions. This supports our claim that generated review comments should not be evaluated only by defect-oriented metrics.

### Understanding the change is a central challenge

The paper identifies understanding the code change, its motivation, and its purpose as a major challenge faced by reviewers. This is directly relevant to our context-quality dimension: if reviewers struggle with missing rationale and unfamiliar code, an LLM reviewer will also struggle when its context is incomplete.

### Review feedback is valuable when it improves code or learning

The paper reports that review feedback is perceived as valuable when it gives authors an opportunity to improve code or learn. This helps justify why our framework distinguishes **correctness**, **usefulness**, **actionability**, and **workflow impact** rather than treating all correct comments as equally valuable.

### Review feedback has multiple roles

Review comments can discuss code improvement, understanding, social communication, defects, design, questions, confusion, security, and architecture. This supports the need for a fine-grained taxonomy of problematic comments because review comments are not a single homogeneous artifact.

### Confusion often comes from missing rationale or unfamiliar code

The SLR reports that missing rationale, non-functional-requirement discussions, and lack of familiarity with code are frequent sources of confusion in review. This is especially important for our framework's context-quality dimension.

## Findings About MCR Proposals

The paper classifies MCR support proposals into three broad groups:

1. **Review Planning and Setup**
   - patch documentation;
   - reviewer recommendation;
   - review prioritization.

2. **Code Review**
   - code checking support;
   - feedback provision;
   - review decision support.

3. **Process Management and Support**
   - methodology and guidelines;
   - review retrospective;
   - tool support.

The most common proposal type is reviewer recommendation. Code checking support is also common and often aims to improve reviewer understanding through visualization or decomposition of changes.

This matters for our paper because LLM-based code review comment generation is a newer form of code checking/feedback provision support. It should be positioned as part of a longer MCR-support trajectory, not as an isolated LLM-only phenomenon.

## Findings About Evaluation Practice

This is the most important part for our paper.

The paper finds that MCR-supporting approaches are evaluated mostly through **offline evaluations** using historical data. Offline evaluation is especially common for reviewer recommenders and code checking support. The frequent metrics include precision, recall, accuracy, and mean reciprocal rank.

The paper also reports that evaluations involving human subjects are much less common. This is a strong background justification for our own argument: code review is human-centered and workflow-dependent, but the evaluation of support tools often remains offline and metric-centered.

## Research Gaps Relevant to Our Paper

The paper identifies several gaps that connect directly to our work:

1. **Need for more user studies**
   MCR is human-based and tool-supported, yet many evaluations do not involve practitioners.

2. **Need to evaluate non-technical benefits**
   Knowledge transfer, learning, and collective ownership are underexplored in MCR support tools.

3. **Need for richer evaluation of support approaches**
   Many evaluations only show that a new approach outperforms a baseline on offline metrics.

4. **Need to consider context and process variation**
   MCR is flexible and context-dependent, so support tools and their evaluation must account for different workflows and settings.

These gaps align with our paper's main claim that current evaluation practice is fragmented and should connect error reduction, usefulness, context quality, cost, workflow impact, and evaluator validity.

## How We Should Use This Paper

### In `02-background.md`

Use it to support:

- MCR is flexible, tool-supported, asynchronous, and socio-technical.
- MCR value includes code quality, defect detection, learning, knowledge sharing, and collective ownership.
- Understanding code changes and their rationale is a key challenge.
- Review comments have multiple roles, not only bug reporting.

### In `03-related-work.md`

Use it to position our paper relative to the broader MCR literature:

- Foundational studies vs proposals vs evaluations.
- Existing support approaches before LLM-based review generation.
- Offline evaluation dominance in MCR support tools.

### In `04-methodology.md`

Use it as a methodological precedent for:

- focused evidence synthesis;
- coding/categorization of literature;
- deriving taxonomy from primary studies.

### In `05-operational-taxonomy.md`

Use it to justify why our taxonomy should capture comment function and workflow role, not only technical correctness.

### In `10-threats-to-validity.md`

Use it to discuss:

- incompleteness of evidence synthesis;
- selection bias;
- subjectivity in coding/classification;
- limited generalizability from OSS-heavy or offline-heavy evaluations.

## Concrete Claims We Can Reuse

- MCR is not only defect detection; it also supports code improvement, knowledge sharing, learning, and collective ownership.
- Review feedback is valuable when it helps authors improve code or learn.
- Missing rationale and lack of familiarity with code are important sources of review confusion.
- Most evaluations of MCR-supporting approaches are offline and rely on historical data.
- Human-subject and workflow-centered evaluations remain relatively limited.
- MCR support tools should be evaluated against the broader goals of review, not only output accuracy.

## Connection to Our Core Argument

P51 strengthens the paper's background and evaluation-gap argument. It shows that even before LLM-based review generation, MCR research had already identified a gap between the socio-technical nature of review and the offline, metric-centered evaluation of support tools. Our paper extends this gap to LLM-generated review comments and argues for a decision-oriented, trade-off-aware evaluation framework.

## Limitations of Using This Paper

- The paper covers MCR literature up to 2019, before the recent wave of LLM-based code review systems.
- It is excellent for background and methodology, but it does not address LLM hallucination, LLM-as-a-Judge, or modern RAG/context-aware code review directly.
- Its taxonomy is about MCR research as a field, not about problematic generated comments. We should use it as a methodological and conceptual foundation, not as a replacement for our own taxonomy.

## Reading Outcome

- **Use in Introduction:** already useful as a background citation.
- **Use in Background:** high priority.
- **Use in Related Work:** high priority.
- **Use in Methodology:** medium/high priority.
- **Use in Taxonomy:** medium priority.
- **Use in Framework:** medium priority.
