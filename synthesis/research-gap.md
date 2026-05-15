# Research Gap

> [!NOTE]
> This file collects the emerging research gap from the paper notes. It should become the basis for the introduction, related-work critique, contribution statement, and methodology. Citations use keys from `references/references.bib`.

## Current Literature Movement

The analyzed papers show a clear movement in LLM-based code review evaluation.

1. **From lexical similarity to quality rubrics**  
   Early code review generation work and later evaluation papers show that BLEU/ROUGE-like metrics are weak for review comments because valid review comments are diverse, context-dependent, and often not lexically similar to a single human reference [@p14_li2022_codereviewer; @p01_lu2025_deepcrceval].

2. **From generated text to grounded claims**  
   Hallucination and context-misalignment work reframes review-comment quality as a grounding problem: a generated comment should be traceable to the diff, PR context, specification, static-analysis output, or another explicit evidence source [@p02_tantithamthavorn2026_hallujudge; @p12_wang2025_sgcr; @p22_jaoua2025_static_analyzers].

3. **From snippet-level benchmarks to PR-level and project-aware evaluation**  
   Newer benchmarks move from isolated hunks toward pull requests, issue coverage, project context, enriched semantic context, and human-flagged review issues. However, more context does not automatically improve performance and can increase noise, cost, and attention load [@p04_kumar2026_swe_prbench; @p05_zeng2025_swrbench; @p06_hu2025_contextcrbench; @p16_icoz2026_context_aware].

4. **From offline metrics to production and workflow signals**  
   Industrial and user-study papers add signals such as code resolution, acceptance, perceived value, PR cycle time, reviewer overhead, signal-to-noise, abandonment, and developer trust [@p03_tantithamthavorn2026_rovodev; @p07_olewicki2024_revmate; @p10_sun2025_bitsai_cr; @p26_zhong2026_human_ai_synergy; @p27_chowdhury2026_industry_claims].

5. **From comment quality to input and reference quality**  
   Several papers show that the data used for training or evaluation is itself noisy. Human review comments may be vague, low-value, incomplete, or shaped by reviewer experience. Reviewability of the input change and provenance of the reference comment therefore matter [@p08_liu2025_too_noisy; @p18_bensghaier2025_curated_reviews; @p23_lin2026_reviewer_experience; @p40_ram2018_reviewability].

6. **From generic evaluation to LLM-as-a-Judge validity**  
   LLM-as-a-Judge papers show that automated evaluation is itself unstable: judge decisions can depend on task type, prompt wording, response order, source model, preprocessing, verbosity, and other biases [@p29_wang2025_human_evaluators; @p30_weyssow2025_codeultrafeedback; @p31_jiang2025_codejudgebench; @p32_zhao2026_bias_loop; @p33_he2025_llmjudge_se; @p36_li2024_llms_as_judges].

7. **From general review to specialized sublayers**  
   Security review, static-analysis-guided code-quality repair, documentation-behavior consistency, and non-functional efficiency evaluation each introduce additional dimensions that should not be collapsed into a single generic quality score [@p21_peng2025_icodereviewer; @p46_zhou2025_vulnerability_repair; @p48_patcas2026_code_quality_issues; @p49_lee2025_metamon; @p50_peng2025_coffe].

## Core Gap

Recent work improves evaluation along many dimensions, but these dimensions remain fragmented. Existing studies do not yet provide a unified framework that jointly evaluates:

- **generated-comment quality**, including correctness, relevance, specificity, grounding, actionability, explanation quality, and usefulness;
- **context quality**, including relevance, completeness, specificity, consistency, groundability, freshness, reviewability, provenance, behavioral evidence, attention load, and cost;
- **reference and data quality**, including noisy human comments, reviewer expertise, reference incompleteness, multiple-valid-comment cases, and AI-generated reference/provenance risk;
- **problematic comment types**, instead of only aggregate model scores;
- **grounding and hallucination**, without reducing the whole problem to hallucination detection;
- **actionability and practical usefulness**, without collapsing them into correctness or semantic similarity;
- **acceptance and perceived value**, without treating direct acceptance as the only signal of usefulness;
- **preservation of useful feedback**, especially when filters, gates, judges, retrieval, or aggregation strategies are applied;
- **false-positive and false-negative consequences** of automated quality gates;
- **human annotation, user-study, and judge validity**, including expertise, uncertainty, disagreement, agreement reporting, prompt sensitivity, order bias, and evaluator calibration;
- **cost, latency, reviewer overhead, escalation, and workflow impact** in realistic review settings;
- **specialized layers** for secure review, static-analysis-guided review, repair validation, context consistency, and non-functional quality claims.

## Why the Gap Matters

A code review assistant can fail in several different ways that are easy to collapse under a single “quality” score:

- It can produce a hallucinated comment.
- It can produce a technically grounded but useless comment.
- It can produce a correct but non-actionable comment.
- It can provide a plausible explanation with unsupported rationale.
- It can miss the actual issue human reviewers would flag.
- It can be filtered too aggressively and suppress useful comments.
- It can use more context while performing worse because the added context increases noise or attention load.
- It can rely on stale documentation or inconsistent specifications.
- It can interpret a static-analysis warning incorrectly.
- It can make a security or performance claim without enough evidence.
- It can improve benchmark scores while failing to improve developer workflow.
- It can be rejected by a reviewer but still provide useful development insight.
- It can reduce visible noise while hiding the cost of wrong removals.
- It can be judged by an LLM evaluator whose score is biased, unstable, or under-calibrated.

These failures imply that evaluation should not only ask whether a generated comment is good. It should also ask what kind of failure occurred, what caused it, what evidence supports the judgment, and what trade-off a mitigation strategy introduces.

## Candidate Research Problem

Current LLM-based code review evaluation lacks a trade-off-aware framework for assessing generated review comments under varying context quality, reference quality, problematic comment types, evaluator validity, and filtering/gating decisions.

More specifically, current work lacks a systematic way to answer:

- Which problematic comment types occur in LLM-generated code review?
- Which failures are caused or amplified by poor context quality or low reviewability?
- How should we evaluate comments that are grounded but low-value?
- How should we evaluate comments that are useful but not directly accepted?
- How much useful feedback is lost when stricter hallucination, relevance, actionability, reviewability, or consistency filters are applied?
- When should a generated comment be shown, suppressed, rewritten, aggregated, or escalated to a human?
- How should controlled annotation, benchmark issue coverage, live reviewer feedback, and LLM-as-a-Judge results be combined?
- How should evaluator validity be reported when LLM judges are used as measurement instruments?

## Research Questions

| RQ | Question | Expected Output |
|---|---|---|
| RQ1 | What types of problematic comments appear in LLM-generated code review? | Problematic-comment taxonomy |
| RQ2 | How is context quality defined, used, or ignored in current LLM-based code review evaluation? | Context-quality model |
| RQ3 | Which evaluation dimensions are covered or missing in current studies? | Evaluation-dimension matrix |
| RQ4 | What trade-offs arise when generated review comments are filtered, gated, judged, aggregated, or enriched with context? | Trade-off matrix |
| RQ5 | What should a trade-off-aware evaluation framework for LLM-generated code review comments include? | Final evaluation framework |

## Possible Contribution

A strong contribution direction is:

> A taxonomy and trade-off-aware evaluation framework for LLM-generated code review comments, with special attention to context quality, reference/provenance quality, evaluator validity, and the consequences of filtering, judging, aggregating, suppressing, rewriting, or escalating generated comments.

This contribution can include:

- a taxonomy of problematic generated review comments;
- a context-quality model for code review automation;
- an evaluation matrix separating correctness, grounding, usefulness, actionability, explanation quality, acceptance, coverage, workflow impact, and cost;
- a trade-off matrix for filtering/gating/judging/aggregation decisions;
- a judge-validity checklist for LLM-as-a-Judge use in code review evaluation;
- optional specialized sublayers for security, static-analysis/code-quality, context-consistency, and non-functional quality evaluation;
- guidelines for human annotation, user-study design, agreement reporting, and useful-feedback preservation;
- a mapping from current papers to missing evaluation dimensions.

## What This Is Not

To avoid weak positioning, the contribution should **not** be framed as:

- just another comparison of LLMs for code review;
- just another benchmark leaderboard;
- just another hallucination detector;
- just another rubric like DeepCRCEval;
- just another RAG/context expansion method;
- just a generic survey of LLMs for software engineering.

The stronger framing is that existing methods each cover one part of the evaluation problem, but the field still lacks a framework for reasoning about the trade-offs between quality, context, reference provenance, filtering, evaluator validity, cost, and developer value.

## Evidence from Current Papers

| Evidence | Supporting Papers | Citation keys | Interpretation |
|---|---|---|---|
| Text-similarity metrics are insufficient | P01, P14, P18, P29, P30, P31 | [@p01_lu2025_deepcrceval; @p14_li2022_codereviewer; @p18_bensghaier2025_curated_reviews; @p29_wang2025_human_evaluators; @p30_weyssow2025_codeultrafeedback; @p31_jiang2025_codejudgebench] | Evaluation needs task-specific and developer-facing criteria. |
| Hallucination can be framed as context misalignment | P02 | [@p02_tantithamthavorn2026_hallujudge] | Generated comments should be checked against available review context. |
| Production metrics matter | P03, P10, P26, P27 | [@p03_tantithamthavorn2026_rovodev; @p10_sun2025_bitsai_cr; @p26_zhong2026_human_ai_synergy; @p27_chowdhury2026_industry_claims] | Offline quality does not fully capture workflow impact. |
| More context can hurt | P04, P13, P16 | [@p04_kumar2026_swe_prbench; @p13_haider2024_prompting_finetuning; @p16_icoz2026_context_aware] | Context quality must be evaluated, not assumed. |
| Full project and PR context improve realism | P05, P06 | [@p05_zeng2025_swrbench; @p06_hu2025_contextcrbench] | Realistic evaluation needs project-level information, but still needs context-quality controls. |
| Human feedback is useful but noisy | P03, P04, P05, P07, P08, P18, P23 | [@p03_tantithamthavorn2026_rovodev; @p04_kumar2026_swe_prbench; @p05_zeng2025_swrbench; @p07_olewicki2024_revmate; @p08_liu2025_too_noisy; @p18_bensghaier2025_curated_reviews; @p23_lin2026_reviewer_experience] | Human review comments, acceptance, value signals, and references are realistic but imperfect. |
| Gates and filters exist but trade-offs are under-modeled | P02, P03, P07, P10, P21, P22, P35 | [@p02_tantithamthavorn2026_hallujudge; @p03_tantithamthavorn2026_rovodev; @p07_olewicki2024_revmate; @p10_sun2025_bitsai_cr; @p21_peng2025_icodereviewer; @p22_jaoua2025_static_analyzers; @p35_mcaleese2024_llm_critics] | We need to evaluate both caught errors and lost useful comments. |
| Acceptance is not usefulness | P07, P39 | [@p07_olewicki2024_revmate; @p39_bosu2015_useful_reviews] | A comment can be valuable even if not directly accepted. |
| Review has socio-technical value | P28, P37, P38, P39 | [@p28_heander2025_support_not_automation; @p37_sadowski2018_google_mcr; @p38_bacchelli2013_expectations_mcr; @p39_bosu2015_useful_reviews] | Evaluation should preserve knowledge transfer, team awareness, and shared ownership. |
| Input reviewability matters | P40 | [@p40_ram2018_reviewability] | Low-reviewability changes can make both human and automated review harder. |
| Explanation quality is distinct from issue detection | P25, P41 | [@p25_yu2024_finetuning_acr; @p41_widyasari2025_explaining_explanations] | A generated comment can identify a concern but fail to explain it usefully. |
| LLM-as-a-Judge needs validation | P29, P30, P31, P32, P33, P36 | [@p29_wang2025_human_evaluators; @p30_weyssow2025_codeultrafeedback; @p31_jiang2025_codejudgebench; @p32_zhao2026_bias_loop; @p33_he2025_llmjudge_se; @p36_li2024_llms_as_judges] | Automated evaluators are measurement instruments, not ground truth. |
| Specialized security/code-quality/performance layers matter | P21, P22, P46, P48, P50 | [@p21_peng2025_icodereviewer; @p22_jaoua2025_static_analyzers; @p46_zhou2025_vulnerability_repair; @p48_patcas2026_code_quality_issues; @p50_peng2025_coffe] | Some review tasks need structured validation beyond generic comment quality. |
| Context consistency and provenance matter | P12, P42, P49 | [@p12_wang2025_sgcr; @p42_wasserbaech2024_chatgpt_github; @p49_lee2025_metamon] | Specs, docs, AI conversations, and behavior can diverge or need verification. |

## Methodological Implication

The method should be described as a **focused evidence synthesis**, not as a simple literature summary. The analysis pipeline is:

```text
Paper selection
  → structured coding using the template
  → extraction of evaluation dimensions
  → extraction of problematic comment types
  → extraction of context-quality dimensions
  → extraction of trade-offs
  → cross-paper synthesis
  → taxonomy + framework + trade-off matrix
```

## Next Steps

- [ ] Convert this gap into a concise introduction section.
- [ ] Convert this gap into a related-work critique section.
- [ ] Decide whether to include a small illustrative mini-validation.
- [ ] Replace `TODO_PUBLISHER_BIBTEX` entries with official publisher-exported BibTeX.
- [ ] Deep-read P39, P40, and P49 for stronger usefulness/context-quality framing.
