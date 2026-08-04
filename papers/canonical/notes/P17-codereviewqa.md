# P17 — CodeReviewQA: The Code Review Comprehension Assessment for Large Language Models

> [!NOTE]
> Compact v2 analysis. P17 is central for our evaluation-framework argument because it decomposes automated code refinement into intermediate code-review comprehension probes, manually curates a clean benchmark, and directly addresses data contamination and memorization without comprehension.

## Status

- Paper ID: `P17`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `High`
- Reading depth: `Read once from PDF`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | CodeReviewQA: The Code Review Comprehension Assessment for Large Language Models |
| Authors | Hong Yi Lin, Chunhua Liu, Haoyu Gao, Patanamon Thongtanunam, Christoph Treude |
| Year | 2025 |
| Venue / Source | Findings of ACL 2025 / arXiv |
| DOI / arXiv | DOI: 10.18653/v1/2025.findings-acl.476; arXiv:2503.16167 |
| Artifact | Hugging Face dataset: TomoMelb/CodeReviewQA |

```bibtex
```

## One-Sentence Summary

> CodeReviewQA evaluates whether LLMs truly understand code review comments by decomposing automated code refinement into Change Type Recognition, Change Localisation, and Solution Identification MCQA probes, rather than relying only on final exact-match code generation.

## Main Contribution

P17 turns automated code refinement evaluation from a one-step text/code matching problem into a multi-step comprehension assessment. This directly supports our claim that LLM code review evaluation should diagnose *why* a model succeeds or fails, not only whether the final output matches a reference.

## Dataset / Study Context

| Field | Value |
|---|---|
| Source dataset | CodeReview-New / recent ACR data |
| Initial pool | 9,367 examples from 259 repositories |
| Final benchmark | 900 manually verified clean examples |
| Repository coverage | 199 repositories |
| Languages | C, C++, C#, Go, Java, JavaScript, PHP, Python, Ruby |
| Retention rate | 13% clean retention after filtering/curation |
| Tasks | ACR plus CTR, CL, SI probes |

## Benchmark Design

| Probe | What it evaluates | Why it matters |
|---|---|---|
| CTR — Change Type Recognition | Whether the review asks to add, delete, or modify code. | Captures high-level intent. |
| CL — Change Localisation | Which exact code lines the review targets. | Captures code-review coreference/localization. |
| SI — Solution Identification | Which revision implements the review intent. | Captures intent-to-solution mapping. |

The probes are multiple-choice questions with easy/hard distractors. Correctness is measured through invariant accuracy across all answer-order permutations, reducing random guessing and option-order sensitivity.

## Data-Quality Filters

P17 explicitly removes examples that are:

- unclear,
- not asking for a code change,
- ignored by developers,
- wrongly linked to code hunks,
- directly containing the intended implementation,
- simple formatting/lint issues,
- not self-contained.

Two annotators independently reviewed 3,000 examples and resolved conflicts across 46 rounds. Reported Cohen’s kappa mean was 0.89, with standard deviation 0.11.

## Evaluation Method

| Dimension | Evidence |
|---|---|
| Models | 72 open-source LLMs across ≤3B to ≤72B scales |
| Final generation metric | Exact Match for ACR |
| Intermediate metrics | Invariant accuracy for CTR, CL, SI |
| Contamination checks | Perplexity and 5-gram accuracy |
| Prompting analysis | Zero-shot, few-shot, chain-of-thought variants |

## Key Findings

| Finding | Summary |
|---|---|
| F1 | Llama-3.1-70B-Instruct achieved the highest ACR EM among reported top models: 50.3%. |
| F2 | ACR performance is not always aligned with comprehension-probe performance. |
| F3 | Change Localisation is the hardest probe and often explains ACR failure. |
| F4 | In non-exact-match cases, top models failed at least one probe in 76.5%–99.8% of failures. |
| F5 | Exact-match success can still occur without full probe success, suggesting memorization or shallow pattern matching. |
| F6 | MCQA reformulation yields higher perplexity and lower 5-gram accuracy, mitigating surface-level contamination. |
| F7 | Chain-of-thought degraded probe performance for the top model; few-shot helped some probes but hurt SI. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Comprehension | Very high | CTR/CL/SI decomposition. |
| Localization | Very high | CL is line-level. |
| Solution correctness | High | SI and ACR. |
| Data contamination | High | PPL and n-gram tests. |
| Data quality | Very high | Fully manual verification. |
| Ground-truth validity | High | Filters noisy/unfaithful examples. |
| Human annotation reliability | High | Kappa reported. |
| Production usefulness | Low | Not a live study. |

## Problematic Comment / Data Types

- Unclear comments.
- Non-actionable comments.
- Ignored comments.
- Wrongly linked comments.
- Comments that reveal the solution verbatim.
- Formatting-only comments.
- Non-self-contained comments.
- Under-specified conversational comments.
- Memorized exact-match success without comprehension.

## Context-Quality Evidence

P17 shows that even when code hunk and review comment are available, the model may fail to understand the intended change type, target location, or solution. Context quality therefore includes whether the provided context is sufficient for each reasoning step.

## Trade-offs

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| MCQA probes | Fine-grained diagnosis and contamination resistance. | Less natural than full generation. |
| Manual curation | High benchmark reliability. | Small benchmark size: 900 examples. |
| Easy/hard distractors | Measures robustness at different difficulty levels. | Needs surrogate model and manual verification. |
| Invariant answer-order testing | Reduces guessing/order bias. | Expensive: N! runs per question. |

## Relevance to Our RQs

| Our RQ | Relevance |
|---|---|
| RQ1 | Adds noisy/unfaithful review-comment/data types. |
| RQ2 | Strong evidence for reasoning-step context sufficiency. |
| RQ3 | Adds CTR/CL/SI as evaluation dimensions beyond final text/code match. |
| RQ4 | Shows exact match can hide memorization; MCQA reduces contamination but adds cost. |
| RQ5 | Strong support for decomposed, contamination-aware evaluation. |

## Follow-up TODOs

- [ ] Verify ACL BibTeX.
- [ ] Add CTR/CL/SI to `synthesis/evaluation-dimensions.md`.
- [ ] Add noisy/unfaithful example categories to taxonomy.
- [ ] Add contamination-resistance and invariant testing to trade-off matrix.
## Legacy proposal-aligned quality appraisal (superseded by the canonical record)

P17 is **Core / Medium–High relevance**. It supports RQ1 through noisy and unfaithful review-comment/data types; RQ2–RQ3 through question-answering and context use; and RQ5–RQ6 through dataset validity and annotation considerations.

**Quality score: 19/24.** Q1–Q5=2, Q6=2, Q7=1, Q8=1, Q9=1, Q10=1, Q11=1, Q12=2. It is less direct evidence for mitigation trade-offs and deployment workflow effects.
## Canonical citation record

Use citation key `p17_lin2025_codereviewqa` from `references/references.bib`; do not duplicate its BibTeX entry in this note.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p17_lin2025_codereviewqa`; Core; Include; Medium–High relevance.
- Study overview: Code-review comprehension assessment using question-answering and review context.
- RQ1: Noisy, unfaithful, and context-insufficient review-comment/data types (Reported).
- RQ2: Review comprehension and context use are central (Reported).
- RQ3: QA/comprehension dimensions and benchmark evaluation (Reported).
- RQ4: Context and benchmark quality versus model performance; mitigation cost is limited.
- RQ5: Dataset validity and annotation protocol are relevant.
- RQ6: Supports benchmark and evaluator design.
- Failure taxonomy: noisy; unfaithful; context-insufficient; misunderstanding.
- Metrics: QA/comprehension and benchmark performance.
- Mitigation/trade-off: context-aware comprehension evaluation; no deployment gate or escalation.
- Validity: annotation/reliability and transfer to generated comments require verification.
- Quality: 19/24; supporting/core benchmark evidence.
- Synthesis conclusion: supports comprehension and context dimensions, not direct preservation analysis.

### 1. Identification
- P17; `p17_lin2025_codereviewqa`; local full PDF; included; authoritative record.
### 2. Screening and proposal alignment
- Include as Core. `p17_lin2025_codereviewqa`; Core; Include; Medium–High relevance.
### 3. Study overview
Code-review comprehension assessment using question-answering and review context.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | Noisy, unfaithful, and context-insufficient review-comment/data types (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Review comprehension and context use are central (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | QA/comprehension dimensions and benchmark evaluation (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Context and benchmark quality versus model performance; mitigation cost is limited. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Dataset validity and annotation protocol are relevant. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Supports benchmark and evaluator design. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| noisy | Reported/Inferred | Full PDF |
| unfaithful | Reported/Inferred | Full PDF |
| context-insufficient | Reported/Inferred | Full PDF |
| misunderstanding. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| QA/comprehension and benchmark performance. | Not an end-to-end outcome | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: context-aware comprehension evaluation; no deployment gate or escalation.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: partial; useful-issue retention after mitigation is incomplete.
- Human escalation: no formal rate/policy reported.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- annotation/reliability and transfer to generated comments require verification.
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
| Q7 | 1 | judging at scored depth. |
| Q8 | 1 | reliability at scored depth. |
| Q9 | 1 | intervention at scored depth. |
| Q10 | 1 | trade-offs at scored depth. |
| Q11 | 1 | threats at scored depth. |
| Q12 | 2 | SLR support at scored depth. |
- Total: 19/24; reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence and selection/publication bias remain explicit; second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Code-review comprehension assessment using question-answering and review context.
- Boundary: supports comprehension and context dimensions, not direct preservation analysis.
