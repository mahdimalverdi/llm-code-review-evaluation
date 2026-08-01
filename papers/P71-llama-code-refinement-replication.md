# P71 — Exploring the Potential of Llama Models in Automated Code Refinement

## Screening and proposal alignment

- **Decision:** Include as supporting
- **Group:** Supporting
- **Relevance:** Medium
- **Citation key:** `p71_caumartin2024_llama_code_refinement`
- **Method:** Replication study comparing Llama 2, CodeLlama, ChatGPT, and CodeReviewer on code-refinement tasks.
- **Data:** CodeReview and CodeReview-New datasets; 2,106 refinement tasks and 400 manually annotated instances for task profiles.

## Proposal RQ mapping

- **RQ1:** Highlights irrelevant responses and task-type-dependent failures, especially new-code tasks.
- **RQ2:** Shows clarity and relevance of review comments affect refinement quality.
- **RQ3:** Evaluates prompting, temperature, model family, and refinement outcomes.
- **RQ4:** Supports open-source privacy/cost benefits versus performance and task-coverage trade-offs.
- **RQ5:** Uses filtered datasets and manual task annotation, relevant to dataset validity.
- **RQ6:** Supports replication methodology and model/mitigation comparison, but not a full comment taxonomy.

## Synthesis-ready summary

The replication study reports that properly tuned Llama models, particularly CodeLlama, can approach ChatGPT on some code-refinement tasks. Existing-code modifications such as refactoring are easier than tasks requiring new code, and clarity/relevance of comments affect outcomes. The paper is useful for model/resource trade-offs but should not be treated as direct evidence of review-comment usefulness or production workflow impact.

## Quality appraisal

| Criterion | Score | Evidence note |
|---|---:|---|
| Q1–Q5 | 2 each | RQs, models, datasets, replication procedure, and metrics are described. |
| Q6 | 1 | Task failures are discussed, but no full problematic-comment taxonomy. |
| Q7 | 1 | Manual task annotation is reported; full protocol needs verification. |
| Q8 | 1 | Replication controls are present; agreement/validity details need verification. |
| Q9 | 1 | Prompt/model configuration is compared rather than a deployment mitigation. |
| Q10 | 1 | Privacy/cost versus performance is discussed, not comprehensively measured. |
| Q11 | 1 | Dataset and model limitations remain. |
| Q12 | 2 | Direct support for proposal RQ2–RQ6 as supporting evidence. |
| **Total** | **17/24** | **Relevant supporting evidence.** |

## Evidence boundary

Code refinement is adjacent to code review but not equivalent to review-comment generation. Transfer claims should therefore be explicit and limited.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p71_caumartin2024_llama_code_refinement`; Supporting; Include; Medium relevance.
- Study overview: Replication comparing Llama 2, CodeLlama, ChatGPT, and CodeReviewer on 2,106 code-refinement tasks plus 400 manually annotated instances.
- RQ1: Prompt/temperature effects and irrelevant or low-quality outputs (Reported).
- RQ2: Open-source Llama models versus ChatGPT/CodeReviewer (Reported).
- RQ3: Existing-code/refactoring tasks outperform new-code tasks; clarity and relevance matter (Reported).
- RQ4: Open-source privacy/cost benefits versus performance and task coverage (Reported).
- RQ5: Replication datasets and manual task profiling (Reported/Our perspective).
- RQ6: Supports replication and model/resource comparison.
- Failure taxonomy: irrelevant; low-quality; new-code failure; unclear/relevance-deficient refinement.
- Metrics: exact match, BLEU, refinement performance, prompt/temperature comparisons.
- Mitigation/trade-off: prompt/model tuning; privacy and cost benefits may trade off with quality.
- Validity: code refinement is adjacent to review comments; manual agreement requires verification.
- Quality: 17/24; supporting evidence.
- Synthesis conclusion: transfer claims must remain limited to generated-fix/refinement contexts.

### 1. Identification
- P71; `p71_caumartin2024_llama_code_refinement`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as supporting. `p71_caumartin2024_llama_code_refinement`; Supporting; Include; Medium relevance.
### 3. Study overview
Replication comparing Llama 2, CodeLlama, ChatGPT, and CodeReviewer on 2,106 code-refinement tasks plus 400 manually annotated instances.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Prompt/temperature effects and irrelevant or low-quality outputs (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Open-source Llama models versus ChatGPT/CodeReviewer (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Existing-code/refactoring tasks outperform new-code tasks; clarity and relevance matter (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Open-source privacy/cost benefits versus performance and task coverage (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Replication datasets and manual task profiling (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Supports replication and model/resource comparison. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| irrelevant | Reported/Inferred | Full PDF |
| low-quality | Reported/Inferred | Full PDF |
| new-code failure | Reported/Inferred | Full PDF |
| unclear/relevance-deficient refinement. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| exact match | Transfer/deployment limits remain | Full PDF |
| BLEU | Transfer/deployment limits remain | Full PDF |
| refinement performance | Transfer/deployment limits remain | Full PDF |
| prompt/temperature comparisons. | Transfer/deployment limits remain | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: prompt/model tuning; privacy and cost benefits may trade off with quality.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- code refinement is adjacent to review comments; manual agreement requires verification.
- Q7–Q8 encode judging and reliability depth.
### 9. Quality appraisal
| Criterion | Score | Evidence note |
|---|---:|---|
| Q1 | 2 | goal at scored depth. |
| Q2 | 2 | artifact at scored depth. |
| Q3 | 2 | dataset/context at scored depth. |
| Q4 | 1 | procedure at scored depth. |
| Q5 | 2 | metrics at scored depth. |
| Q6 | 1 | failures at scored depth. |
| Q7 | 2 | judging at scored depth. |
| Q8 | 1 | reliability at scored depth. |
| Q9 | 0 | intervention at scored depth. |
| Q10 | 1 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 17/24; calibrated reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence, transfer limits, and selection/publication bias remain explicit; independent second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Replication comparing Llama 2, CodeLlama, ChatGPT, and CodeReviewer on 2,106 code-refinement tasks plus 400 manually annotated instances.
- Boundary: transfer claims must remain limited to generated-fix/refinement contexts.
