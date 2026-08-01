# P70 — ChatGPT in Automated Code Refinement

## Screening and proposal alignment

- **Decision:** Include as supporting
- **Group:** Supporting
- **Relevance:** Medium
- **Citation key:** `p70_guo2023_chatgpt_code_refinement`

## Proposal RQ mapping

- **RQ1:** Supports incorrect, incomplete, or low-quality generated suggestions.
- **RQ2–RQ3:** Evaluates refinement quality and code-quality dimensions.
- **RQ4:** Supports refinement benefit versus correctness and maintainability risk.
- **RQ5–RQ6:** Provides methodological context for LLM-generated code changes.

## Synthesis-ready summary

P70 studies ChatGPT for automated code refinement. It is relevant to the boundary between review suggestions and generated fixes, but should not be treated as direct evidence about review-comment usefulness or reviewer workflow without explicit review data.

**Provisional quality score: 14/24.** Verify task design, human evaluation, and connection to code-review comments.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p70_guo2023_chatgpt_code_refinement`; Supporting; Include; Medium relevance.
- Study overview: Empirical study of ChatGPT for automated code refinement, adjacent to review-comment generation.
- RQ1: Incorrect, incomplete, or low-quality refinement suggestions (Reported/Our perspective).
- RQ2: Code/comment context and refinement task type (Reported).
- RQ3: Exact-match, BLEU, refinement success, and task-profile evaluation (Reported).
- RQ4: Refinement benefit versus correctness, maintainability, and model/API cost (Reported).
- RQ5: Dataset/task validity and manual profile annotation (Reported/Our perspective).
- RQ6: Supporting evidence for generated-fix and non-functional sublayers.
- Failure taxonomy: incorrect fix; incomplete fix; new-code difficulty; refactoring asymmetry.
- Metrics: exact match, BLEU, refinement success, task-type performance.
- Mitigation/trade-off: ChatGPT refinement; quality versus proprietary cost and privacy risk.
- Validity: code refinement is adjacent, not equivalent to review-comment usefulness.
- Quality: 14/24 provisional; low-to-medium supporting evidence.
- Synthesis conclusion: use only for the boundary between review suggestions and generated fixes.

### 1. Identification
- P70; `p70_guo2023_chatgpt_code_refinement`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p70_guo2023_chatgpt_code_refinement`; Supporting; Include; Medium relevance.
### 3. Study overview
Empirical study of ChatGPT for automated code refinement, adjacent to review-comment generation.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Incorrect, incomplete, or low-quality refinement suggestions (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Code/comment context and refinement task type (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Exact-match, BLEU, refinement success, and task-profile evaluation (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Refinement benefit versus correctness, maintainability, and model/API cost (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Dataset/task validity and manual profile annotation (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Supporting evidence for generated-fix and non-functional sublayers. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| incorrect fix | Reported/Inferred | Full PDF |
| incomplete fix | Reported/Inferred | Full PDF |
| new-code difficulty | Reported/Inferred | Full PDF |
| refactoring asymmetry. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| exact match | Transfer/deployment limits remain | Full PDF |
| BLEU | Transfer/deployment limits remain | Full PDF |
| refinement success | Transfer/deployment limits remain | Full PDF |
| task-type performance. | Transfer/deployment limits remain | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: ChatGPT refinement; quality versus proprietary cost and privacy risk.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- code refinement is adjacent, not equivalent to review-comment usefulness.
- Q7–Q8 encode judging and reliability depth.
### 9. Quality appraisal
| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 | 2 | goal at scored depth. |
| Q2 | 2 | artifact at scored depth. |
| Q3 | 2 | dataset/context at scored depth. |
| Q4 | 1 | procedure at scored depth. |
| Q5 | 1 | metrics at scored depth. |
| Q6 | 1 | failures at scored depth. |
| Q7 | 1 | judging at scored depth. |
| Q8 | 1 | reliability at scored depth. |
| Q9 | 1 | intervention at scored depth. |
| Q10 | 0 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 1 | SLR support at scored depth. |
- Total: 14/24; calibrated reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence, transfer limits, and selection/publication bias remain explicit; independent second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Empirical study of ChatGPT for automated code refinement, adjacent to review-comment generation.
- Boundary: use only for the boundary between review suggestions and generated fixes.
