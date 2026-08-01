# Discussion

## Evaluation as a Decision Problem

The synthesis suggests that evaluation should connect measurement to action. Correctness or groundedness alone does not determine whether a comment should be shown. A weakly grounded but potentially important concern may require escalation; a valid but vague concern may require rewriting; and a correct but low-value nitpick may justify suppression. The show, suppress, rewrite, and escalate decisions expose trade-offs hidden by binary quality labels.

## Implications for Tool Builders

Tool builders should report both harmful-comment reduction and useful-feedback preservation. Context expansion should be evaluated for marginal utility, freshness, integrity, latency, and model capacity. Verification and filtering should expose suppressed outputs to audit so that wrong removals can be measured. Human escalation should be treated as a cost and coverage outcome, not as a free fallback.

## Implications for Benchmarks

Benchmarks should distinguish reference incompleteness from model failure, record input reviewability, and support multiple valid comments. Acceptance, adoption, or lexical similarity should not be treated as complete proxies for usefulness. Specialized security, static-analysis, repair, and performance claims require task-specific evidence rather than a generic quality score.

## Implications for Evaluators

LLM-based judges can support scale but should be treated as measurement instruments. At minimum, judge studies should report the rubric, answer rate, order swaps, repeated-run consistency, prompt perturbation, judge and source-model sensitivity, preprocessing, human comparison, adversarial robustness, and cost [@p29_wang2025_human_evaluators; @p31_jiang2025_codejudgebench; @p32_zhao2026_bias_loop; @p33_he2025_llmjudge_se; @p36_li2024_llms_as_judges].

## Research Agenda

The most useful next step is not another single-score leaderboard. Future work should measure preservation under filters and gates, validate the proposed taxonomy with independent annotators, compare context quantity with context quality, test defensive mechanisms against adversarial review context, and report workflow and cost effects alongside quality. A controlled mitigation study can use the annotation protocol and framework derived here, but its findings should be presented separately from this literature review.
