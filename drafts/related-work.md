# Related Work Draft

> [!NOTE]
> This is a working draft. It is organized by argument, not by paper order. The goal is to support a framework-oriented paper on trade-off-aware evaluation of LLM-generated code review comments. Citations use Pandoc/Quarto-style citation keys from `references/references.bib`.

## 1. Evaluation of LLM-Generated Code Review Comments

Early and recent work on automated code review shows that evaluating generated review comments is difficult because valid comments are diverse, context-dependent, and often not lexically similar to a single human reference. Foundational systems such as CodeReviewer helped establish code review comment generation as a model task, but also exposed the weakness of relying on lexical overlap metrics. Later evaluation-focused work, such as DeepCRCEval, further argues that review-comment quality needs domain-specific criteria rather than generic text-similarity metrics [@p14_li2022_codereviewer; @p01_lu2025_deepcrceval].

More recent benchmarks extend the evaluation setting from isolated hunks toward PR-level and project-aware review. SWE-PRBench, SWRBench, and ContextCRBench represent this movement: they emphasize human-flagged review issues, project context, enriched semantic information, and benchmark data quality. However, these works also show that realism alone does not solve evaluation. In particular, adding more context can degrade model performance, and enriched context still needs to be selected, filtered, and evaluated for quality [@p04_kumar2026_swe_prbench; @p05_zeng2025_swrbench; @p06_hu2025_contextcrbench].

## 2. Context, Grounding, and Hallucination

A major thread in the literature reframes poor review comments as failures of grounding. HalluJudge treats hallucination as context misalignment: a generated comment is problematic when its claims cannot be supported by the code diff or available review context. Industrial systems such as RovoDev also show that missing context about language, framework, version, surrounding code, or task intent can lead to incorrect or non-actionable comments [@p02_tantithamthavorn2026_hallujudge; @p03_tantithamthavorn2026_rovodev].

At the same time, context is not simply a matter of adding more files. RAG-based and context-aware review systems show that retrieval can help when relevant, but can also introduce irrelevant, stale, or distracting information. Specification-grounded, static-analysis-guided, and reviewer-experience-aware approaches further expand what counts as useful context: specifications, tool warnings, historical reviewer behavior, and project conventions may all matter. The central gap is that most papers treat context as an input configuration, while our framework treats context quality as an evaluation object with dimensions such as relevance, completeness, specificity, consistency, freshness, groundability, reviewability, provenance, attention load, and cost [@p11_zhang2025_laura; @p12_wang2025_sgcr; @p16_icoz2026_context_aware; @p20_hong2025_rag_reviewer; @p22_jaoua2025_static_analyzers; @p23_lin2026_reviewer_experience; @p40_ram2018_reviewability; @p49_lee2025_metamon].

## 3. Data Quality, Reference Quality, and Provenance

Several studies show that code review datasets and references are not clean ground truth. Human review comments can be vague, unclear, non-actionable, uncivil, irrelevant, or low-value. Data-curation work such as Too Noisy To Learn and Harnessing Large Language Models for Curated Code Reviews highlights that cleaning and reformulating review comments can improve downstream model behavior, but this also introduces a trade-off: cleaning may remove or alter useful signals [@p08_liu2025_too_noisy; @p18_bensghaier2025_curated_reviews].

Reference quality also depends on provenance. Reviewer-experience-aware work suggests that who wrote the reference comment matters. LLM-as-a-judge and preference-data papers show that AI-generated labels or preferences can scale annotation, but they also introduce judge-dependence. Public developer-practice studies, such as work on shared ChatGPT conversations in GitHub PRs and issues, add another provenance concern: AI-generated explanations may become part of collaboration artifacts and influence review discussions without clear verification [@p23_lin2026_reviewer_experience; @p30_weyssow2025_codeultrafeedback; @p42_wasserbaech2024_chatgpt_github].

## 4. Human-Centered Code Review and Usefulness

Human code review is not only defect detection. Foundational studies of modern code review at Google, expectations and outcomes of modern code review, and characteristics of useful code reviews show that review also supports maintainability, knowledge transfer, team awareness, shared ownership, alternative solution discovery, and developer learning. This matters because an LLM review assistant can be technically correct while still reducing the socio-technical value of review [@p37_sadowski2018_google_mcr; @p38_bacchelli2013_expectations_mcr; @p39_bosu2015_useful_reviews].

User-study and industrial papers reinforce this point. Acceptance is not the same as usefulness: a generated comment may be rejected or edited but still provide useful development insight. Conversely, an accepted or adopted suggestion may increase complexity or fail to support team understanding. Therefore, evaluation should include developer-perceived value, reviewer overhead, downstream revision, PR cycle time, signal-to-noise ratio, abandonment, trust, knowledge transfer, and team awareness [@p07_olewicki2024_revmate; @p10_sun2025_bitsai_cr; @p26_zhong2026_human_ai_synergy; @p27_chowdhury2026_industry_claims; @p28_heander2025_support_not_automation].

## 5. Problematic Comment Types and Taxonomies

The literature identifies many failure modes, but they are rarely unified into a single taxonomy. Existing papers discuss hallucinated comments, unsupported claims, irrelevant comments, vague comments, non-actionable comments, low-value nitpicks, wrong locations, wrong API or type assumptions, missed issues, noisy references, and low-signal automated feedback. Fine-grained classification work adds category-level distinctions and shows that some rare categories can be highly useful but hard to classify [@p01_lu2025_deepcrceval; @p02_tantithamthavorn2026_hallujudge; @p08_liu2025_too_noisy; @p19_nguyen2025_fine_grained_classification; @p27_chowdhury2026_industry_claims].

Newer evidence suggests that the taxonomy should also include explanation failures, workflow failures, context failures, and evaluator failures. Explanation-focused work shows that a comment may identify a plausible issue but fail to explain why it matters or how to act on it. Reviewability work suggests that some poor comments are caused by low-quality input changes: large, scattered, poorly described changes are harder to review. Documentation-behavior consistency work suggests stale or contradictory context can produce misleading comments. LLM-as-a-Judge studies add another layer: evaluation itself can fail because the judge is biased, unstable, or prompt-sensitive [@p41_widyasari2025_explaining_explanations; @p40_ram2018_reviewability; @p49_lee2025_metamon; @p29_wang2025_human_evaluators; @p31_jiang2025_codejudgebench; @p32_zhao2026_bias_loop].

## 6. LLM-as-a-Judge and Evaluator Validity

LLM-as-a-Judge is increasingly used to evaluate code and review artifacts, but recent work warns that it should be treated as a measurement instrument rather than ground truth. Studies such as Can LLMs Replace Human Evaluators?, CodeJudgeBench, Bias in the Loop, and LLM-as-a-Judge for Software Engineering show that judge behavior can depend on task type, response order, source model, preprocessing, prompt perturbations, verbosity, and other biases [@p29_wang2025_human_evaluators; @p31_jiang2025_codejudgebench; @p32_zhao2026_bias_loop; @p33_he2025_llmjudge_se; @p36_li2024_llms_as_judges].

This has direct consequences for code review evaluation. If an LLM judge is used to filter generated comments, score usefulness, or compare systems, the evaluation should report judge calibration, answer rate, parseability, repeated-run consistency, A/B order sensitivity, judge-choice sensitivity, source-model sensitivity, preprocessing sensitivity, and human agreement or uncertainty. Without these checks, a benchmark may simply replace one weak proxy metric with another [@p29_wang2025_human_evaluators; @p30_weyssow2025_codeultrafeedback; @p31_jiang2025_codejudgebench; @p32_zhao2026_bias_loop; @p33_he2025_llmjudge_se].

## 7. Mitigation Strategies and Trade-offs

Many mitigation strategies have been proposed: hallucination gates, relevance/actionability filters, RAG, specification grounding, static-analysis hybrids, prompt routing, multi-agent generation, reviewer-experience weighting, reward models, structured reasoning chains, LLM critics, and human-in-the-loop workflows. These strategies can reduce some failures, but they are not free improvements [@p02_tantithamthavorn2026_hallujudge; @p09_ren2025_hydra_reviewer; @p10_sun2025_bitsai_cr; @p11_zhang2025_laura; @p12_wang2025_sgcr; @p21_peng2025_icodereviewer; @p22_jaoua2025_static_analyzers; @p24_bensghaier2025_reward_models; @p25_yu2024_finetuning_acr; @p35_mcaleese2024_llm_critics].

A stricter filter may remove hallucinated comments but also suppress rare useful comments. More context may improve grounding but increase cost and attention dilution. Static-analysis context may provide focused evidence but can be misinterpreted. Security-focused review can find high-impact issues but risks false alarms and severity miscalibration. Performance or efficiency suggestions need workload evidence and can become premature optimization. Human escalation improves reliability but adds delay and reviewer overhead. Therefore, mitigation should be evaluated by both error reduction and useful-feedback preservation [@p04_kumar2026_swe_prbench; @p21_peng2025_icodereviewer; @p22_jaoua2025_static_analyzers; @p35_mcaleese2024_llm_critics; @p39_bosu2015_useful_reviews; @p46_zhou2025_vulnerability_repair; @p48_patcas2026_code_quality_issues; @p50_peng2025_coffe].

## 8. Specialized Evaluation Sublayers

The literature also suggests that a single generic review-comment quality score is insufficient for specialized cases. Secure code review needs vulnerability type, location, exploitability, severity, repair correctness, false-positive cost, and missed-vulnerability risk. Static-analysis-guided review needs warning interpretation, issue resolution, and behavior preservation. Non-functional quality review needs evidence about performance, efficiency, workload assumptions, and maintainability trade-offs. Context-consistency work needs checks for stale or contradictory documentation, specifications, and behavior [@p21_peng2025_icodereviewer; @p22_jaoua2025_static_analyzers; @p46_zhou2025_vulnerability_repair; @p48_patcas2026_code_quality_issues; @p49_lee2025_metamon; @p50_peng2025_coffe].

These sublayers should be optional components of the final framework rather than being collapsed into generic usefulness or correctness.

## 9. Summary of the Gap

Overall, prior work has made strong progress in evaluating LLM-based code review systems, but the evidence remains fragmented. Existing studies cover quality rubrics, hallucination detection, PR-level benchmarks, production telemetry, data curation, RAG, specification grounding, static-analysis hybrids, reward models, human-AI workflow, and LLM-as-a-Judge validity. What is still missing is a unified framework that jointly evaluates generated-comment quality, context quality, reference/provenance quality, problematic comment types, workflow value, useful-feedback preservation, evaluator validity, cost, and specialized security/static-analysis/non-functional sublayers.

This motivates our contribution: a taxonomy and trade-off-aware evaluation framework for LLM-generated code review comments.

## TODOs

- [ ] Replace `TODO_PUBLISHER_BIBTEX` entries in `references/references.bib` with official publisher-exported BibTeX before final submission.
- [ ] Decide whether related work should be organized by topic, chronology, or framework components.
- [ ] Convert this into polished academic prose after the final framework is stable.
- [ ] Add a concise table mapping related-work clusters to framework gaps.
