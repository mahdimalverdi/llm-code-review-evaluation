# P54 — CR-Bench: Evaluating the Real-World Utility of AI Code Review Agents

## Screening and proposal alignment

- **Decision:** Include
- **Group:** Core
- **Relevance:** High
- **Evidence basis:** Full local PDF, first-pass abstract and introduction review
- **Contribution:** CR-Bench dataset and CR-Evaluator pipeline for granular evaluation of issue resolution versus spurious findings.

## Proposal RQ mapping

- **RQ1:** Spurious findings and low signal-to-noise outputs are reported.
- **RQ2:** Evaluates issue correctness and utility beyond coarse resolution metrics.
- **RQ3:** Introduces benchmark and fine-grained evaluator for code-review agents.
- **RQ4:** Directly studies issue resolution versus false/spurious findings.
- **RQ5:** Supports benchmark validity and granular annotation concerns.
- **RQ6:** Strong support for benchmark, evaluator, and trade-off framework design.

## Synthesis-ready summary

CR-Bench is directly relevant because it frames code-review-agent evaluation as a frontier between resolving real issues and generating spurious findings. Resolution rate alone can obscure signal-to-noise and developer productivity. The paper should be used for RQ4, while preserving the distinction between benchmark utility and production adoption.

## Quality appraisal

**Provisional score: 19/24.** Core evidence is strong for artifact, benchmark, issue coverage, and trade-offs; detailed annotation reliability, cost, and limitations require full-text extraction.
