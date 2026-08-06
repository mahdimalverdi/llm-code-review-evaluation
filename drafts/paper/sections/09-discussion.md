# Discussion

## Interpretation of the Evidence

The expanded corpus supports a shift from evaluating generated text in isolation to evaluating review decisions within a workflow. A review comment depends on a change, selected context, a model or agent trajectory, and an evaluation instrument. Failure can occur at any of these points. Training references may be ambiguous, retrieval may supply misleading context, a plausible comment may identify the wrong cause, and a judge may prefer a fluent explanation without reliable evidence [@p08_liu2025_too_noisy; @p31_jiang2025_codejudgebench; @p72_centellas_claros2026_rethinking_training_data_for_g; @p93_meng2025_when_more_retrieval_hurts_retr; @p101_jin2025_uncovering_systematic_failures]. The evaluation problem is therefore wider than hallucination detection or comment-reference similarity.

The corpus also reveals a difference between evidence coverage and comparability. Many studies discuss correctness, usefulness, coverage, cost, or human involvement, but define them with different artifacts, denominators, and evaluators. The study-level counts therefore describe reporting practice rather than a common effect size. The proposed framework makes these differences visible; this review does not test whether it improves review outcomes.

## Denominators and Missing Outcomes

The framework changes which observations belong in an evaluation. Precision over displayed comments cannot reveal useful comments removed by a filter. Coverage over known reference issues cannot reveal valid issues absent from the reference. An escalation rate is difficult to interpret without escalation precision, reviewer effort, and the consequences of non-escalation. Evaluation records should preserve the relationship between generated candidates, displayed comments, suppressed comments, escalated cases, and developer action.

## Implications for Tool Builders

Tool builders need records of candidate generation and subsequent filtering. Context expansion should be evaluated for marginal utility, freshness, integrity, latency, and model capacity. More retrieval or a larger model does not consistently improve review performance [@p83_kumar2026_bigger_isn_t_always_better_a_c; @p93_meng2025_when_more_retrieval_hurts_retr]. Verification and filtering should retain suppressed outputs during evaluation so that wrong removals can be measured. Human escalation should be treated as a cost and coverage outcome, not as a free fallback.

Agentic systems also require trajectory-level observability. Reporting only the final comment hides which context was selected, which tools were used, which candidate issues were discarded, and where unsupported claims entered the trajectory [@p74_charoenwet2026_agentic_code_review_in_the_ter; @p76_wang2026_swe_review_closing_the_loop_on; @p85_zhang2026_reporeviewer_a_local_first_mul]. Deployments should record the provenance of context retrieval, tool evidence, suppression, rewriting, and escalation decisions.

## Implications for Benchmarks

Benchmarks should distinguish reference incompleteness from model failure, record input reviewability, and support multiple valid comments. Acceptance, adoption, and lexical similarity are partial measures of usefulness. Specialized security, static-analysis, repair, and performance claims require task-specific evidence rather than a generic quality score.

Benchmark reporting should also identify the unit of analysis. Comment-level, issue-level, change-level, pull-request-level, and trajectory-level evaluations answer different questions. A model may localize issues well but produce poor explanations, or generate plausible comments without improving review outcomes. Multi-task and multidimensional benchmarks expose these differences only when their aggregate scores remain decomposable [@p91_zhang2026_sphinx_benchmarking_and_modeli; @p98_yu2025_fine_tuning_llms_to_analyze_mu].

## Implications for LLM-as-a-Judge Evaluation

LLM-as-a-Judge methods can support evaluation at scale. Judge studies should report the rubric, answer rate, order swaps, repeated-run consistency, prompt perturbation, judge and source-model sensitivity, preprocessing, human comparison, adversarial robustness, and cost [@p29_wang2025_human_evaluators; @p31_jiang2025_codejudgebench; @p32_zhao2026_bias_loop; @p33_he2025_llmjudge_se; @p36_li2024_llms_as_judges].

Consistency alone is insufficient because a judge can be consistently biased or sensitive to source cues. Human evaluation is also affected by expertise, task context, rubric interpretation, and disagreement procedures. Evaluator validation should combine repeated measurements, human calibration, disagreement analysis, and claims limited to the constructs the instrument can measure.

## Scope of the Framework

The reviewed studies supply the constructs, failure evidence, and intervention families used by the framework. This review contributes their six-layer organization, the core/modifier taxonomy, and the show, suppress, rewrite, and escalate policy. Projects must still set thresholds according to risk and review capacity. Independent annotation and controlled strategy comparisons are needed to validate these elements.

## Research Agenda

Future work should measure useful-feedback preservation under filters and gates, validate the taxonomy with independent annotators, compare context quantity with context quality, test defenses against adversarial review context, and report workflow and cost effects alongside quality. Longitudinal field studies are needed to determine whether apparently useful comments change developer behavior, reviewer workload, defect outcomes, or trust over time [@p77_lin2026_is_agentic_code_review_helpful; @p100_sun2025_does_ai_code_review_lead_to_co; @p110_a_alsteinsson2025_rethinking_code_review_workflo]. A controlled mitigation study can use the annotation protocol and framework derived here, but its findings should be reported separately from this literature review.
