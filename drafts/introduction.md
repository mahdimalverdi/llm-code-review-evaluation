# Introduction Draft

> [!NOTE]
> This draft intentionally uses a gradual opening. It does not start directly from problematic LLM-generated comments. Instead, it moves from human code review, to LLM-based review assistance, to the evaluation gap, and then to the proposed taxonomy and trade-off-aware framework.

## Draft

Modern code review is a central practice in software engineering. Beyond detecting defects, it supports maintainability, knowledge sharing, team awareness, and shared ownership of code. Empirical studies of modern code review show that developers value review not only because it can identify faults, but also because it improves understanding, encourages discussion, and helps teams align on design and implementation decisions [@p37_sadowski2018_google_mcr; @p38_bacchelli2013_expectations_mcr; @p39_bosu2015_useful_reviews]. These broader functions make code review a socio-technical activity rather than a purely mechanical quality-control step.

Recent advances in large language models have renewed interest in automating or supporting code review. LLM-based systems can generate review comments, summarize changes, suggest fixes, classify review feedback, and assist with secure or static-analysis-guided review. Research has therefore moved from early code review generation models toward richer settings, including pull-request-level benchmarks, retrieval-augmented review, specification-grounded review, production deployments, and human-centered user studies [@p14_li2022_codereviewer; @p04_kumar2026_swe_prbench; @p05_zeng2025_swrbench; @p11_zhang2025_laura; @p12_wang2025_sgcr; @p03_tantithamthavorn2026_rovodev; @p07_olewicki2024_revmate]. This progress suggests that LLMs may become useful assistants in code review workflows, but it also raises a difficult evaluation problem: how should generated review comments be assessed?

Early evaluations often relied on lexical or reference-based metrics, but generated review comments are difficult to evaluate with a single reference. A comment can be useful even when it does not match a human reference in wording, and a comment can be lexically plausible while being unsupported, irrelevant, or non-actionable. Recent work has therefore introduced richer evaluation criteria, including usefulness, grounding, actionability, hallucination, context alignment, and workflow impact [@p01_lu2025_deepcrceval; @p02_tantithamthavorn2026_hallujudge; @p10_sun2025_bitsai_cr; @p18_bensghaier2025_curated_reviews]. However, these criteria are often studied in isolation. A benchmark may emphasize issue coverage, a hallucination detector may focus on unsupported claims, a production system may track acceptance or resolution, and an LLM-as-a-Judge study may focus on evaluator agreement. Each view is useful, but none is sufficient on its own.

The central challenge is that evaluation decisions involve trade-offs. A stricter post-generation verifier may reduce unsupported comments, but it may also suppress comments that are potentially useful but weakly grounded. Adding more context may improve grounding, but it can also increase cost, latency, noise, and attention dilution. A relevance or actionability filter may reduce reviewer burden, but it may remove early design concerns or comments that are useful after rewriting. LLM-based evaluators can scale assessment, but they can also introduce prompt sensitivity, order effects, judge-choice dependence, and other measurement risks [@p29_wang2025_human_evaluators; @p30_weyssow2025_codeultrafeedback; @p31_jiang2025_codejudgebench; @p32_zhao2026_bias_loop; @p33_he2025_llmjudge_se]. Therefore, evaluating LLM-generated review comments requires more than asking whether a comment is correct or whether a filter removes bad comments. It also requires asking what useful feedback is preserved, what review coverage is lost, what cost is introduced, and how reliable the evaluator is.

This paper argues that current evaluations of LLM-generated code review comments remain fragmented. Existing work has studied quality metrics, hallucination, context enrichment, data curation, production signals, human usefulness, and evaluator validity, but these strands are rarely connected through a unified trade-off-aware framework. In particular, current evaluations often do not jointly model problematic comment types, context quality, generated-comment quality, useful-feedback preservation, review coverage, human effort, computational cost, and evaluator validity. This fragmentation makes it difficult to compare evaluation results across studies and to reason about when a generated comment should be shown, suppressed, rewritten, or escalated.

To address this gap, we develop a framework-oriented synthesis of LLM-based code review evaluation. We first synthesize evidence from recent and foundational work on automated code review, human code review, LLM-generated review comments, context-aware review, production deployments, and LLM-as-a-Judge evaluation. From this evidence, we derive an operational taxonomy of problematic LLM-generated review comments. The taxonomy distinguishes, for example, unsupported or hallucinated comments, irrelevant comments, incorrect technical claims, wrong-location comments, non-actionable comments, low-value nitpicks, invalid fix suggestions, and context-dependent cases. The goal is not only to name these failures, but to make them annotatable through definitions, decision rules, and examples.

We then propose a multi-dimensional evaluation framework that connects comment quality to context quality, usefulness, actionability, mitigation decisions, cost, workflow impact, and evaluator validity. The framework treats context quality as an evaluation object rather than only an input configuration, and it treats LLM-based judging as a measurement instrument that requires calibration rather than as ground truth. To make the taxonomy and framework more concrete, we also define an annotation protocol and evaluation schema for a small annotated evidence layer. This layer is intended to support the framework by showing how problematic comment types, usefulness, groundedness, actionability, and show/suppress/rewrite/escalate decisions can be labeled and analyzed.

This paper makes four contributions. First, it synthesizes evaluation concerns across LLM-based code review studies and identifies fragmentation in current evaluation practice. Second, it proposes an operational taxonomy of problematic LLM-generated code review comments. Third, it introduces a trade-off-aware evaluation framework that jointly considers error reduction, useful-feedback preservation, review coverage, cost, context quality, and evaluator validity. Fourth, it defines an annotation protocol and evaluation schema for a small evidence layer that can support the taxonomy and expose concrete trade-offs in generated review comments.

## Intended Introduction Flow

1. Start with human code review as a socio-technical practice.
2. Introduce LLM-based code review assistance as a recent development.
3. Explain why generated review comments are hard to evaluate.
4. Show that existing evaluations study useful dimensions but remain fragmented.
5. Introduce trade-offs: error reduction vs useful-feedback preservation vs cost.
6. State the gap.
7. Present the taxonomy, framework, and annotation layer.
8. List contributions.

## TODOs

- [ ] Add a concise motivating example after the opening paragraphs, if needed.
- [ ] Decide whether to use “LLM-generated code review comments” or “LLM-based code review comments” consistently.
- [ ] Add final paper title after the framework is stable.
- [ ] Tighten citations after official publisher BibTeX verification.
- [ ] Align contribution wording with `synthesis/final-framework.md` after that file is created.
