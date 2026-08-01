# P52 — Towards Automating Code Review Activities

## Metadata

- **ID:** P52
- **Title:** Towards Automating Code Review Activities
- **Authors:** Rosalia Tufano, Luca Pascarella, Michele Tufano, Denys Poshyvanyk, Gabriele Bavota
- **Year:** 2021
- **Venue:** IEEE Xplore / ICSE 2021
- **Official URL:** https://ieeexplore.ieee.org/abstract/document/9402025/
- **DOI:** TODO: extract from IEEE metadata
- **arXiv:** 2101.02518
- **Drive PDF:** https://drive.google.com/file/d/1X6BiupUKfz7raX9xn1Rkg_skyirno5fF
- **Drive PDF filename:** P52_towards_automating_code_review_activities.pdf
- **BibTeX key:** `p52_tufano2021_automating_code_review_activities`

## Status

- **Review status:** Deep read completed
- **Verification status:** Official IEEE Xplore page verified from user-provided link; Drive PDF available and read; DOI still needs extraction.
- **Priority:** High

## Why This Paper Matters

This paper provides an important pre-LLM automated-code-review baseline. It helps position our work as part of a longer automation trajectory rather than as a response only to recent LLM-based review generation.

It is also important because the authors frame automation as assistance, not replacement. They explicitly note that fully replacing developers would remove one of the benefits of code review: knowledge sharing. This supports our own framing that LLM-generated review comments should be evaluated as review-support artifacts inside a human workflow, not merely as standalone model outputs.

## Expected Use in Our Paper

Use this paper mainly in:

- `drafts/paper/sections/02-background.md`
- `drafts/paper/sections/03-related-work.md`
- `drafts/paper/sections/05-operational-taxonomy.md`
- `drafts/paper/sections/06-framework.md`
- `drafts/paper/sections/10-threats-to-validity.md`

Specific use:

- In **Background**, cite it for the historical motivation of automating parts of code review.
- In **Related Work**, cite it as an early transformer-based code review automation baseline.
- In **Taxonomy**, cite it for the distinction between actionable comments and noisy/non-actionable review comments.
- In **Framework**, cite it for cost reduction, data-quality limitations, and the limits of exact-match evaluation.
- In **Threats**, cite it for noisy mined review data and Java-only generalizability limits.

## Extraction Targets

When reading the paper, extract:

1. Which code review activities are automated.
2. What costs or human-effort reductions the paper motivates.
3. What evaluation criteria are used.
4. What limitations are reported for automation.
5. Whether generated artifacts are evaluated as directly actionable review outputs.
6. Any evidence that automation success depends on context or task type.

## Relevance to Our Framework

Potential links to our framework:

- cost and human effort;
- automation as review support rather than replacement;
- pre-LLM evaluation baselines;
- limits of direct automation metrics;
- connection between generated review output and developer action;
- noisy review comments as a dataset-construction problem;
- exact-match and BLEU limitations;
- semantic usefulness vs reference equality.

## Initial Notes

This paper should be used to show that code review automation had evaluation and cost trade-offs before LLMs. It can help avoid presenting the trade-off problem as unique to LLMs, while still showing that LLMs make the problem more acute because generated comments can be plausible, ungrounded, and context-sensitive.

Deep-read summary:

- The paper studies two transformer-based automation tasks.
- **Contributor-side task:** given code submitted for review, generate revised code that implements changes a reviewer might request.
- **Reviewer-side task:** given submitted code and a natural-language reviewer comment, generate revised code that implements that comment.
- The authors mine code review data from GitHub and Gerrit and focus on Java methods.
- Their final dataset contains 17,194 triplets and corresponding code pairs.
- The reviewer-side model performs better than the contributor-side model, showing that review comments provide useful context.

Important extracted claims:

- Code review improves code quality and lowers the likelihood of introducing bugs, but it costs developer time and causes context switching.
- The authors' goal is not to replace developers; automation should work with developers and preserve knowledge sharing.
- Review comments mined from repositories are noisy: approval, thanks, clarification requests, requests for tests, and references to previous comments may not directly trigger code changes.
- The authors use filtering heuristics to remove comments unlikely to trigger code changes; their heuristic reaches around 93% precision for relevant comments.
- The contributor-side model produces exact revised code in roughly 3% to 16% of cases depending on beam size.
- The reviewer-side model produces exact revised code in roughly 12% to 31% of cases depending on beam size.
- Some non-perfect predictions are still meaningful and semantically acceptable.
- BLEU and Levenshtein can be misleading because generated code is often close to the input code.

Concrete connection to our argument:

- This paper shows that automated code review evaluation already suffered from data-quality and metric-validity problems before general-purpose LLMs.
- It supports our argument that review automation should be judged by usefulness, actionability, data quality, context sufficiency, and human-workflow value, not only by exact output matching.

Limitations when using this source:

- It focuses on generating revised code, not directly on showing generated review comments to reviewers.
- It uses Java method-level data, limiting generalizability.
- It predates the current wave of general-purpose LLMs and retrieval/context-aware review systems.
- It does not provide a full workflow evaluation with developers.

## TODO

- [x] Read the PDF.
- [x] Extract the automated activities and evaluation setup.
- [x] Extract explicit cost/human-effort claims.
- [x] Extract data-quality and filtering details.
- [x] Extract metric limitations.
- [x] Map findings to Related Work and Framework.
- [ ] Verify official DOI from IEEE metadata.
- [ ] Decide whether this paper should be cited in Introduction or only Background/Related Work.
## Legacy quality appraisal (superseded by the canonical record)

P52 is **Supporting / Medium–High relevance**. It supports RQ2–RQ4 through code-review activity decomposition, automation boundaries, human involvement, and workflow cost; RQ5 through methodology; and RQ6 through mitigation and workflow design. Direct LLM evidence is limited.

**Quality score: 18/24.** Q1–Q5=2, Q6=1, Q7=1, Q8=1, Q9=1, Q10=2, Q11=1, Q12=2.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p52_tufano2021_automating_code_review_activities`; Supporting; Include; Medium–High relevance.
- Study overview: Decomposition and automation of code-review activities.
- RQ1: Activity-specific omissions, incorrectness, and automation limitations (Reported/Our perspective).
- RQ2: Code-change, review-task, and process context (Reported).
- RQ3: Review-activity taxonomy and automation dimensions (Reported).
- RQ4: Automation coverage versus human effort, quality, and accountability (Reported).
- RQ5: Empirical-SE and workflow validity (Reported).
- RQ6: Supports activity and mitigation-family design.
- Failure taxonomy: missed activity; incorrect automation; context-insensitive automation; accountability gap.
- Metrics: task performance, activity coverage, and process outcomes.
- Mitigation/trade-off: activity automation; reduces effort but may lose human review value.
- Validity: pre/current LLM boundary must be stated.
- Quality: 18/24; supporting evidence.
- Synthesis conclusion: supports mapping intervention points across the review workflow.

### 1. Identification
- P52; `p52_tufano2021_automating_code_review_activities`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p52_tufano2021_automating_code_review_activities`; Supporting; Include; Medium–High relevance.
### 3. Study overview
Decomposition and automation of code-review activities.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Activity-specific omissions, incorrectness, and automation limitations (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Code-change, review-task, and process context (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Review-activity taxonomy and automation dimensions (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Automation coverage versus human effort, quality, and accountability (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Empirical-SE and workflow validity (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Supports activity and mitigation-family design. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| missed activity | Reported/Inferred | Full PDF |
| incorrect automation | Reported/Inferred | Full PDF |
| context-insensitive automation | Reported/Inferred | Full PDF |
| accountability gap. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| task performance | Does not alone establish deployment value | Full PDF |
| activity coverage | Does not alone establish deployment value | Full PDF |
| and process outcomes. | Does not alone establish deployment value | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: activity automation; reduces effort but may lose human review value.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- pre/current LLM boundary must be stated.
- Q7–Q8 encode judging and reliability depth.
### 9. Quality appraisal
| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 | 2 | goal at scored depth. |
| Q2 | 2 | artifact at scored depth. |
| Q3 | 2 | dataset/context at scored depth. |
| Q4 | 2 | procedure at scored depth. |
| Q5 | 2 | metrics at scored depth. |
| Q6 | 1 | failures at scored depth. |
| Q7 | 1 | judging at scored depth. |
| Q8 | 1 | reliability at scored depth. |
| Q9 | 1 | intervention at scored depth. |
| Q10 | 2 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 19/24; calibrated reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence and selection/publication bias remain explicit; independent second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Decomposition and automation of code-review activities.
- Boundary: supports mapping intervention points across the review workflow.
