# Discussion

The empirical study is designed to show that reducing problematic LLM-generated code review comments is a trade-off problem rather than a simple quality-improvement problem. This section discusses the implications of that framing for evaluation design, tool builders, benchmark designers, and future research.

## Implications for Evaluation Design

The main implication is that single-score evaluation is insufficient. A strategy that removes more comments may appear better under an error-rate metric, but it may be worse if it suppresses useful feedback, reduces review coverage, or increases human escalation. Evaluation should therefore report both reduction and preservation metrics.

This is especially important for generated review comments because usefulness is not identical to correctness. Some comments may be technically correct but low-value. Others may be weakly grounded but still useful as signals for a human reviewer. A binary correct/incorrect or accepted/rejected label cannot capture these cases. The show/suppress/rewrite/escalate decision model gives a more realistic view of how generated comments should enter a review workflow.

## Implications for Tool Builders

Tool builders should avoid treating mitigation as only a filter. Suppression is only one possible action. When a generated comment contains a useful signal but is too uncertain, too vague, or too strongly phrased, rewriting or escalation may preserve value that would otherwise be lost. This matters for developer trust: an assistant that is too noisy can be ignored, but an assistant that is too conservative may fail to provide useful feedback.

The study also suggests that mitigation strategies should be selected according to failure type. Robust prompting may help with vagueness or actionability. Post-generation verification may help with unsupported claims. Context-quality gates may help when the available context is insufficient or inconsistent. Hybrid strategies may be useful, but they should be justified by improved trade-offs, not by the assumption that more safeguards are always better.

## Implications for Benchmark and Dataset Designers

Benchmark designers should treat context and reference quality as part of the evaluation object. If a benchmark instance does not provide enough context to judge a comment, then disagreement between a model and a reference may not indicate model failure. It may indicate an invalid or under-specified evaluation instance.

Datasets for LLM-based code review should therefore record what context is available, whether the reference comment is judgeable, and whether a generated comment requires additional evidence. This would make it easier to evaluate context-quality gates, retrieval strategies, and post-generation verification systems fairly.

## Implications for Human and LLM-Based Evaluation

Human annotation remains important because usefulness, actionability, and value are partly judgment-based. However, human annotation also introduces disagreement. Reporting inter-annotator agreement and disagreement patterns is therefore part of the evidence, not merely a quality-control step.

LLM-as-a-Judge may be useful for scaling evaluation or supporting screening, but it should not be treated as ground truth without validation. If LLM judges are used in future versions of this work, their judgments should be compared against human labels, tested for prompt sensitivity where feasible, and reported as measurement instruments with known limitations.

## Scope of Generalization

The study should be interpreted according to its scope. If it uses one dataset, one main generation model, and a few hundred comments, it can provide strong design evidence and exploratory empirical findings, but not universal claims about all LLM-based review systems. The goal is to identify trade-off patterns and evaluation requirements that can guide larger studies.

The strongest general contribution is therefore methodological and empirical: mitigation should be evaluated by the failure types it reduces, the useful comments it preserves or loses, the coverage it retains, and the cost it introduces. This framing can be reused even when future work uses different models, datasets, programming languages, or review workflows.
