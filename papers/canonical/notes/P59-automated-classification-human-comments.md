# P59 — Automated Classification of Human Code Review Comments with LLMs

## Screening and proposal alignment

- **Decision:** Include
- **Group:** Core
- **Relevance:** High
- **Evidence basis:** Full local PDF, abstract and first-pass review
- **Citation key:** `p59_caglar2026_human_cr_classification`
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

## Legacy quality appraisal (superseded by the canonical record)

**Provisional score: 21/24.** Strong taxonomy and annotation evidence; cross-platform robustness and inter-annotator reliability require full-text extraction.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p59_caglar2026_human_cr_classification`; Core; Include; High relevance.
- Study overview: Nine-label taxonomy for six comment smells and three useful intents; 448 manually labeled comments with diff hunks.
- RQ1: Directly supports fine-grained problematic-comment and useful-intent taxonomy (Reported).
- RQ2: Comment–diff evidence and evidence-sensitive labels (Reported).
- RQ3: Zero-shot/one-shot GPT-5-mini, LLaMA-3.3, and DeepSeek-R1 classification with macro-F1 (Reported).
- RQ4: Classification/filtering versus misclassification and useful-comment loss (Reported/Our perspective).
- RQ5: Annotation difficulty and evidence-sensitive labeling (Reported).
- RQ6: Strong taxonomy and annotation-protocol support.
- Failure taxonomy: six comment smells plus three useful intents; evidence-sensitive ambiguity.
- Metrics: macro-F1, class-level performance, zero-shot/one-shot changes.
- Mitigation/trade-off: classification and intent-preserving rewrite; filtering cost and preservation not fully measured.
- Validity: class imbalance, platform transfer, and inter-annotator agreement require verification.
- Quality: 21/24 provisional; strong taxonomy evidence.
- Synthesis conclusion: comment–diff evidence suffices for some labels but not evidence-sensitive smells.

### 1. Identification
- P59; `p59_caglar2026_human_cr_classification`; local full PDF extracted and reviewed; authoritative record.
### 2. Screening and proposal alignment
- Include as Core. `p59_caglar2026_human_cr_classification`; Core; Include; High relevance.
### 3. Study overview
Nine-label taxonomy for six comment smells and three useful intents; 448 manually labeled comments with diff hunks.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Directly supports fine-grained problematic-comment and useful-intent taxonomy (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Comment–diff evidence and evidence-sensitive labels (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Zero-shot/one-shot GPT-5-mini, LLaMA-3.3, and DeepSeek-R1 classification with macro-F1 (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Classification/filtering versus misclassification and useful-comment loss (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Annotation difficulty and evidence-sensitive labeling (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong taxonomy and annotation-protocol support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| six comment smells plus three useful intents | Reported/Inferred | Full PDF |
| evidence-sensitive ambiguity. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| macro-F1 | Does not alone establish deployment value | Full PDF |
| class-level performance | Does not alone establish deployment value | Full PDF |
| zero-shot/one-shot changes. | Does not alone establish deployment value | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: classification and intent-preserving rewrite; filtering cost and preservation not fully measured.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: task-specific; retained useful-issue coverage is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- class imbalance, platform transfer, and inter-annotator agreement require verification.
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
| Q7 | 2 | judging at scored depth. |
| Q8 | 1 | reliability at scored depth. |
| Q9 | 2 | intervention at scored depth. |
| Q10 | 1 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 21/24; calibrated reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence and selection/publication bias remain explicit; independent second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Nine-label taxonomy for six comment smells and three useful intents; 448 manually labeled comments with diff hunks.
- Boundary: comment–diff evidence suffices for some labels but not evidence-sensitive smells.
