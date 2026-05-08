# Trade-off Framework

> [!NOTE]
> This file develops the trade-off-aware evaluation argument. The central idea is that mitigation strategies should be evaluated by both what they remove and what they accidentally lose.

## Core Claim

Current evaluations often ask whether an LLM-generated review comment is good. They less often ask what is lost when we filter, suppress, rewrite, aggregate, or escalate comments.

A trade-off-aware framework should measure both:

```text
error reduction
and
useful-feedback preservation
```

## Why Trade-offs Matter

LLM-generated review comments are not simply good or bad. A mitigation strategy can improve one dimension while harming another.

Examples:

```text
Filtering strictness ↑
=> hallucinated comments ↓
=> useful comments wrongly removed ↑
=> review coverage ↓
```

```text
Context size ↑
=> available evidence ↑
=> token cost ↑
=> attention dilution ↑
=> possible review quality ↓
```

```text
LLM-as-a-Judge gate ↑
=> bad comments filtered ↑
=> latency/cost ↑
=> false-positive filtering risk ↑
```

## Trade-off Matrix

| Strategy / Mechanism | Main Benefit | Main Risk / Cost | Missing Metric |
|---|---|---|---|
| More context | More available evidence; better chance of resolving contextual issues | Noise, token cost, latency, attention dilution | Context-quality score; marginal value of added context |
| RAG / retrieval | Brings relevant project or historical review context | Irrelevant retrieval, stale context, hidden assumptions | Retrieval relevance and freshness; context usability |
| Full project context | More realistic review setting | Large context, harder attention, higher cost | Useful-context ratio; attention-load metric |
| Semantic context enrichment | Adds issue/PR intent and surrounding code | Extraction errors; dependency on linkage quality | Context completeness and correctness |
| Hallucination gate | Removes unsupported or ungrounded claims | Removes useful but weakly grounded comments | Useful-comment preservation rate |
| Factuality gate | Removes technically incorrect comments | May miss subtle errors or remove correct edge-case comments | False-positive/false-negative gate error |
| Actionability gate | Removes comments that developers cannot act on | May remove high-level design or architectural concerns | Actionability vs strategic-value metric |
| Relevance gate | Removes off-topic or irrelevant comments | May remove unexpected but useful comments | Novel-useful comment retention |
| LLM-as-a-Judge | Scales evaluation/filtering | Judge bias, cost, latency, inconsistent judgments | Judge calibration and agreement |
| Human escalation | Improves reliability for uncertain cases | Human cost, delay, reviewer burden | Escalation cost and escalation precision |
| Multi-review aggregation | Improves coverage and filters invalid points | More model calls, latency, possible over-aggregation | Marginal F1 gain per cost |
| Live reviewer inspection | Preserves human control | Reviewer time overhead and interruption | Value-to-time ratio |
| Strict suppression policy | Reduces exposure to bad comments | Lower recall and lower review coverage | Suppressed-useful-comment count |
| Rewrite instead of suppress | Preserves potentially useful feedback | Rewrite may introduce new errors | Rewrite quality and grounding preservation |

## Required Metrics for Trade-off-Aware Evaluation

A trade-off-aware evaluation should report more than model quality.

### Error reduction metrics

- hallucinated comments removed;
- unsupported claims removed;
- irrelevant comments removed;
- non-actionable comments removed;
- false positives reduced;
- low-value comments reduced.

### Useful-feedback preservation metrics

- useful comments retained;
- useful comments wrongly removed;
- accepted comments retained;
- valuable-but-not-accepted comments retained;
- human-flagged issues still covered after filtering;
- review coverage before and after filtering.

### Cost and workflow metrics

- token cost;
- model-call count;
- inference latency;
- reviewer inspection time;
- human escalation rate;
- PR cycle time;
- developer trust/adoption;
- downstream code revision rate.

## Trade-off Patterns from Papers

| Pattern | Evidence Source | Interpretation |
|---|---|---|
| LLM evaluation reduces human evaluation cost | P01 | LLM-as-evaluator can scale evaluation, but evaluator bias must be controlled. |
| Hallucination judging can catch unsupported comments | P02 | Useful for safeguards, but wrong removals are under-measured. |
| Actionability gates matter in production | P03 | Actionability may be more practically important than factuality alone. |
| More context can degrade performance | P04 | Context size must be separated from context quality. |
| Full project context improves benchmark realism | P05 | Realism needs context, but context quality/cost must still be evaluated. |
| Enriched semantic/code context can help | P06 | Context helps when extracted and filtered carefully. |
| Acceptance is lower than perceived value | P07 | Direct acceptance underestimates usefulness. |

## Decision Matrix for Generated Comments

| Comment State | Suggested Decision | Reason |
|---|---|---|
| Grounded + correct + actionable + useful | Show to reviewer | High value and low risk. |
| Grounded + correct but low-value | Suppress or lower priority | Avoid reviewer noise. |
| Grounded + correct but non-actionable | Rewrite or escalate | Potential value but weak actionability. |
| Ungrounded but potentially important | Escalate or request more context | Avoid unsupported claim while preserving possible value. |
| Clearly hallucinated | Suppress | High risk. |
| Irrelevant or out-of-scope | Suppress | Low value, high noise. |
| Vague but relevant | Rewrite | Preserve signal while improving usefulness. |
| Duplicate/redundant | Merge or suppress | Reduce reviewer overhead. |
| Uncertain due to missing context | Ask for context or escalate | Avoid overconfident automation. |

## Proposed Evaluation Formula Sketch

This is not a final mathematical model, but a conceptual scoring structure:

```text
NetReviewValue = UsefulFeedbackRetained
               - HarmfulCommentsShown
               - UsefulCommentsSuppressed
               - ReviewerOverhead
               - ComputationalCost
               - WorkflowDelay
```

A practical framework should not optimize only one term.

## Open Questions

- [ ] How should useful-comment preservation be measured when usefulness itself is subjective?
- [ ] Should filters optimize for precision, recall, or reviewer value?
- [ ] How should a system decide between suppressing, rewriting, and escalating a comment?
- [ ] How can we measure wrong removal when reviewers never see suppressed comments?
- [ ] How can context-quality scores be combined with hallucination gates?
- [ ] What is the acceptable reviewer overhead for low-acceptance but high-value suggestions?

## Working Claim for Paper

A trade-off-aware evaluation framework should evaluate the full decision pipeline, not only the generated comment. The key question is not only “Is this comment good?” but also:

- Should it be shown?
- Should it be filtered?
- Should it be rewritten?
- Should it be escalated?
- What useful feedback might be lost?
- What cost or reviewer overhead is introduced?

This is the gap our framework should address.