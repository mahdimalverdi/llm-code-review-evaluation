# P59 — Automated Classification of Human Code Review Comments with LLMs

## Screening and proposal alignment

- **Decision:** Include
- **Group:** Core
- **Relevance:** High
- **Evidence basis:** Full local PDF, abstract and first-pass review
- **Contribution:** Nine-label taxonomy covering six comment smells and three useful intents; 448 manually labeled comments.

## Proposal RQ mapping

- **RQ1:** Directly supports fine-grained problematic-comment taxonomy.
- **RQ2:** Uses comment–diff evidence and evidence-sensitive labels.
- **RQ3:** Evaluates zero-shot and one-shot LLM classification with macro-F1.
- **RQ4:** Supports classification/filtering trade-offs, though operational cost and preservation are not central.
- **RQ5:** Directly supports annotation difficulty and evidence-sensitive labeling.
- **RQ6:** Strong support for taxonomy and annotation protocol.

## Synthesis-ready summary

The study reports moderate zero-shot macro-F1 (0.360–0.374) and model-dependent effects of one-shot exemplars. Comment–diff evidence is sufficient for some labels but limited for evidence-sensitive smells. This supports separating taxonomy classification from correctness and measuring annotation uncertainty.

## Quality appraisal

**Provisional score: 21/24.** Strong taxonomy and annotation evidence; cross-platform robustness and inter-annotator reliability require full-text extraction.
