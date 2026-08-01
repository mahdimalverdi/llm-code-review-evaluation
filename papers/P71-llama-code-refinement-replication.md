# P71 — Exploring the Potential of Llama Models in Automated Code Refinement

## Screening and proposal alignment

- **Decision:** Include as supporting
- **Group:** Supporting
- **Relevance:** Medium
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
