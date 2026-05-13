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
% TODO: Add checked arXiv BibTeX.
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
