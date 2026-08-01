# P60 — Hold On! Is My Feedback Useful?

## Screening and proposal alignment

- **Decision:** Include
- **Group:** Core
- **Relevance:** High
- **Evidence basis:** Full local PDF, abstract and first-pass review
- **Contribution:** Predictive evaluation of code-review-comment usefulness across open-source and commercial datasets.

## Proposal RQ mapping

- **RQ1:** Directly addresses useful versus non-useful comments.
- **RQ2:** Tests textual, jargon, voice, code, and domain features as context/quality signals.
- **RQ3:** Compares feature-based, bag-of-words, transfer-learning, and GPT-4o approaches.
- **RQ4:** Supports usefulness-prediction versus model/resource trade-offs.
- **RQ5:** Compares domains, projects, datasets, and feature validity.
- **RQ6:** Supports usefulness annotation and evaluation-schema design.

## Synthesis-ready summary

The study predicts code-review-comment usefulness using multiple datasets and feature/model families, reporting improved performance over baselines and strong results for GPT-4o and TF-IDF bag-of-words in the tested setting. Usefulness prediction is valuable for the SLR, but predicted usefulness is not identical to correctness, actionability, or acceptance.

## Quality appraisal

**Provisional score: 20/24.** Strong relevance to usefulness and dataset comparison; full-text extraction is needed for label construction, agreement, and cross-project validity.
