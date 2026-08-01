# P22 — Combining Large Language Models with Static Analyzers for Code Review Generation

> [!NOTE]
> Compact v2 analysis. P22 is important for our trade-off framework because it compares three integration points for combining rule-based static analyzers with LLM-based review generation: data-augmented training, retrieval-augmented generation, and naive output concatenation.

## Status

- Paper ID: `P22`
- Analysis status: `First pass completed from PDF; needs citation/BibTeX cleanup`
- Priority: `High`
- Reading depth: `Read once from PDF`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | Combining Large Language Models with Static Analyzers for Code Review Generation |
| Authors | Imen Jaoua, Oussama Ben Sghaier, Houari Sahraoui |
| Year | 2025 |
| Venue / Source | arXiv |
| DOI / arXiv | arXiv:2502.06633 |
| Artifact | GitHub: `ImenJaoua/Hybrid-Code-Review`; Zenodo: `14061110` |

```bibtex
```

## One-Sentence Summary

> P22 evaluates hybrid code review generation strategies that combine static-analyzer precision with LLM coverage, finding that RAG improves accuracy and coverage most reliably, while DAT improves coverage and NCO can suffer from conflicting outputs.

## Main Contribution

The paper studies how to combine knowledge-based systems (KBS), represented by static analyzers, and learning-based systems (LBS), represented by a fine-tuned CodeLlama model. It contributes three hybrid strategies:

- **Data-Augmented Training (DAT):** generate and filter mixed KBS/LBS reviews, then fine-tune a model.
- **Retrieval-Augmented Generation (RAG):** inject PMD/Checkstyle output into the LLM prompt at inference time.
- **Naive Concatenation of Outputs (NCO):** concatenate KBS and LBS outputs after inference.

## Dataset / Study Context

| Field | Value |
|---|---|
| Base model | CodeLlama-7B fine-tuned with QLoRA |
| Static analyzers | PMD and Checkstyle |
| Language | Java |
| Java subset | 27,267 entries |
| Augmented dataset | 78,776 samples, balanced between KBS and LBS reviews |
| Main test subset | 1,245 common code differences with both KBS and LBS reviews |
| Data availability | Replication package and Zenodo dataset released |

## Evaluation Method

| RQ | Method |
|---|---|
| RQ1 | Manual accuracy evaluation on 10% of 1,245 samples by two reviewers: accurate, partially accurate, not accurate. |
| RQ2 | Llama3-70B sanity check against human evaluation; Cohen’s kappa = 0.72. |
| RQ3 | LLM-as-a-judge accuracy evaluation over full 1,245 samples. |
| RQ4 | LLM-as-a-judge coverage ranking with rank 1–5 and win/tie/loss analysis. |

## Key Findings

| Finding | Summary |
|---|---|
| F1 | Static analyzers are accurate on rule-based issues but limited in coverage. |
| F2 | The LBS model covers more nuanced/context-dependent issues but is less accurate. |
| F3 | RAG significantly improves accuracy over using the LLM alone, though still below static-analyzer precision. |
| F4 | DAT and RAG improve issue coverage; DAT often reaches Rank 1 but has polarized performance. |
| F5 | NCO gives only moderate coverage improvement and can inherit LBS inaccuracies. |
| F6 | LBS output can contradict KBS output, reducing NCO usefulness. |
| F7 | Llama3-70B aligns substantially with human accuracy judgments, with kappa 0.72. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Accuracy | High | Manual + LLM evaluation. |
| Coverage | High | Rank-based comparison. |
| Relevance | Medium / High | Used in filtering and judging. |
| Static-rule precision | High | KBS baseline. |
| LLM contextuality | High | LBS baseline and hybrid methods. |
| LLM-as-judge calibration | High | Cohen’s kappa against humans. |
| Useful-feedback preservation | Medium | DAT/RAG/NCO are compared, but lost useful comments are not directly measured. |
| Workflow impact | Low | No live deployment. |

## Problematic Comment / Review Types

- Static-analyzer false positive.
- Outdated or context-insensitive rule-based comment.
- LLM inaccurate review comment.
- Partially accurate review comment.
- Irrelevant generated feedback.
- Conflicting hybrid output, especially when LBS contradicts KBS.
- Low-coverage rule-based review.
- Overbroad LLM review that lacks static grounding.

## Context-Quality Evidence

P22 shows that static-analysis output can act as structured external context. The strongest result is that injecting KBS knowledge at inference time through RAG improves accuracy and coverage more reliably than simply concatenating outputs. This supports our claim that context must be integrated in a usable form, not merely appended.

## Trade-off Extraction

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| DAT | Broader coverage and exposure to KBS/LBS patterns. | May learn noise from synthetic reviews; accuracy not consistently improved. |
| RAG | Best practical accuracy/coverage balance; grounded in static analyzer findings. | Depends on static analyzer quality and prompt integration. |
| NCO | Simple and comprehensive. | Can produce contradictions and inherits LBS inaccuracies. |
| Static analyzers | High precision for rule-based issues. | Limited coverage and outdated/context-insensitive rules. |
| LLM generation | Broader contextual feedback. | Lower precision and hallucination risk. |
| LLM-as-judge | Scales evaluation. | Requires calibration and can miss subtle human judgments. |

## Relevance to Our Paper

P22 is a strong example of mitigation as a trade-off. It shows that the integration point matters: using static analysis during inference is more effective than post-hoc concatenation, and training-time augmentation can improve coverage but not necessarily accuracy.

## Limitations from Our Perspective

- Java-only evaluation.
- PMD/Checkstyle represent only a subset of static-analysis capabilities.
- LLM-as-judge is calibrated but still used heavily.
- Coverage ranking assumes Llama3-70B can identify a comprehensive set of issues.
- No live reviewer acceptance or downstream code-change evaluation.

## Follow-up TODOs

- [ ] Verify arXiv BibTeX.
- [ ] Add DAT/RAG/NCO to `synthesis/trade-off-framework.md`.
- [ ] Add static-analysis context to `synthesis/context-quality.md`.
- [ ] Add hybrid-conflict failure mode to taxonomy.
- [ ] Update `matrices/cross-paper-synthesis.md` with P22 evidence.
## Legacy proposal-aligned quality appraisal (superseded by the canonical record)

P22 is **Core / High relevance**. It supports RQ1 through false positives, rule misinterpretation, and unsupported findings; RQ2–RQ3 through static-analysis context and calibrated evaluation; RQ4 through hybrid precision/coverage and cost trade-offs; and RQ6 through mitigation-family design.

**Quality score: 20/24.** Q1–Q7=2, Q8=1, Q9=2, Q10=1, Q11=1, Q12=2. Hybrid gains do not establish useful-feedback preservation or workflow benefit.
## Canonical citation record

Use citation key `p22_jaoua2025_static_analyzers` from `references/references.bib`; do not duplicate its BibTeX entry in this note.
## Canonical SLR record

> [!NOTE]
> The numbered eleven-section record below is authoritative; the compact block is provenance only.

- Identification/screening: `p22_jaoua2025_static_analyzers`; Core; Include; High relevance.
- Study overview: Hybrid static-analyzer and LLM code-review generation/evaluation.
- RQ1: False positives, rule misinterpretation, unsupported findings, and analyzer-induced noise (Reported).
- RQ2: Static-analysis findings provide structured context and evidence (Reported).
- RQ3: Hybrid quality, calibrated judging, and comparison of analyzer/LLM configurations (Reported).
- RQ4: Precision/coverage and hybrid complexity/cost trade-offs (Reported/Our perspective).
- RQ5: Rule/dataset validity and judge calibration (Reported).
- RQ6: Strong hybrid mitigation support.
- Failure taxonomy: false positive; rule misinterpretation; unsupported finding; analyzer-context mismatch.
- Metrics: precision/recall/F1 or calibrated quality measures, cost, and comparison baselines.
- Mitigation/trade-off: static-analysis grounding; can reduce hallucination but inherit analyzer blind spots and cost.
- Validity: language/tool-specific setting limits generalization.
- Quality: 20/24; strong core evidence with partial workflow validity.
- Synthesis conclusion: supports hybrid grounding, not automatic useful-feedback preservation.

### 1. Identification
- P22; `p22_jaoua2025_static_analyzers`; local full PDF; included; authoritative record.
### 2. Screening and proposal alignment
- Include as Core. `p22_jaoua2025_static_analyzers`; Core; Include; High relevance.
### 3. Study overview
Hybrid static-analyzer and LLM code-review generation/evaluation.
### 4. Evidence mapped to proposal RQ1–RQ6
| RQ | Evidence | Type | Location |
|---|---|---|---|
| RQ1 | False positives, rule misinterpretation, unsupported findings, and analyzer-induced noise (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ2 | Static-analysis findings provide structured context and evidence (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ3 | Hybrid quality, calibrated judging, and comparison of analyzer/LLM configurations (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ4 | Precision/coverage and hybrid complexity/cost trade-offs (Reported/Our perspective). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ5 | Rule/dataset validity and judge calibration (Reported). | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
| RQ6 | Strong hybrid mitigation support. | Reported/Inferred/Our perspective | Full PDF; detailed extraction above |
### 5. Failure and problematic-comment categories
| Category | Type | Location |
|---|---|---|
| false positive | Reported/Inferred | Full PDF |
| rule misinterpretation | Reported/Inferred | Full PDF |
| unsupported finding | Reported/Inferred | Full PDF |
| analyzer-context mismatch. | Reported/Inferred | Full PDF |
### 6. Evaluation dimensions and metrics
| Dimension/metric | Limitation | Location |
|---|---|---|
| precision/recall/F1 or calibrated quality measures | Not an end-to-end outcome | Full PDF |
| cost | Not an end-to-end outcome | Full PDF |
| and comparison baselines. | Not an end-to-end outcome | Full PDF |
### 7. Mitigation and trade-offs
- Mitigation/intervention: static-analysis grounding; can reduce hallucination but inherit analyzer blind spots and cost.
- Useful feedback potentially lost: not directly measured unless stated above.
- Coverage: partial; useful-issue retention after intervention is incomplete.
- Human escalation: no formal rate/policy reported unless stated above.
- Cost: paper-specific evidence above; otherwise Not reported.
### 8. Annotation and evaluator validity
- language/tool-specific setting limits generalization.
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
- Total: 21/24; reporting-quality score.
### 10. Review-process reliability and bias
- Missing preservation/escalation evidence and selection/publication bias remain explicit; second-reviewer calibration is unavailable.
### 11. Synthesis-ready conclusion
- Contribution: Hybrid static-analyzer and LLM code-review generation/evaluation.
- Boundary: supports hybrid grounding, not automatic useful-feedback preservation.
