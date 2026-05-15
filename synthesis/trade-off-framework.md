# Trade-off Framework

> [!NOTE]
> This file develops the trade-off-aware evaluation argument. The central idea is that mitigation strategies should be evaluated by both what they remove and what they accidentally lose.

## Core Claim

Current evaluations often ask whether an LLM-generated review comment is good. They less often ask what is lost when we filter, suppress, rewrite, aggregate, enrich, verify, or escalate comments.

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

```text
Automation ↑
=> reviewer workload may decrease
=> knowledge transfer and shared ownership may decrease
```

## Trade-off Matrix

| Strategy / Mechanism | Main Benefit | Main Risk / Cost | Missing Metric |
|---|---|---|---|
| More context | More available evidence; better chance of resolving contextual issues | Noise, token cost, latency, attention dilution | Context-quality score; marginal value of added context |
| RAG / retrieval | Brings relevant project or historical review context | Irrelevant retrieval, stale context, hidden assumptions | Retrieval relevance and freshness; context usability |
| Full project context | More realistic review setting | Large context, harder attention, higher cost | Useful-context ratio; attention-load metric |
| Semantic context enrichment | Adds issue/PR intent and surrounding code | Extraction errors; dependency on linkage quality | Context completeness and correctness |
| Reviewability gate | Avoids unreliable review on huge/scattered/poorly described changes | May skip useful automation opportunities | Useful-feedback preserved under reviewability gating |
| Documentation/spec consistency check | Prevents stale or contradictory context from misleading review | Extra cost; false inconsistency reports | Consistency precision/recall; false block rate |
| Hallucination gate | Removes unsupported or ungrounded claims | Removes useful but weakly grounded comments | Useful-comment preservation rate |
| Factuality gate | Removes technically incorrect comments | May miss subtle errors or remove correct edge-case comments | False-positive/false-negative gate error |
| Actionability gate | Removes comments that developers cannot act on | May remove high-level design or architectural concerns | Actionability vs strategic-value metric |
| Relevance gate | Removes off-topic or irrelevant comments | May remove unexpected but useful comments | Novel-useful comment retention |
| LLM-as-a-Judge | Scales evaluation/filtering | Judge bias, cost, latency, inconsistent judgments | Judge calibration and agreement |
| Human escalation | Improves reliability for uncertain cases | Human cost, delay, reviewer burden | Escalation cost and escalation precision |
| Multi-review aggregation | Improves coverage and filters invalid points | More model calls, latency, possible over-aggregation | Marginal F1 gain per cost |
| Live reviewer inspection | Preserves human control | Reviewer time overhead and interruption | Value-to-time ratio |
| Strict suppression policy | Reduces exposure to bad comments | Lower recall and lower review coverage | Suppressed-useful-comment count |
| Rewrite instead of suppress | Preserves potentially useful feedback | Rewrite may introduce new errors or change intent | Rewrite quality and grounding preservation |
| Static-analysis + LLM hybrid | Provides focused tool evidence and measurable issue resolution | Tool warnings may be false or misinterpreted | Warning-resolution validity; behavior preservation |
| Security-focused review | Can surface high-impact vulnerabilities | False alarms, missed vulnerabilities, severity miscalibration | Security precision/recall and severity calibration |
| Efficiency/performance review | Adds non-functional quality evidence | Premature optimization, benchmark overfitting | Workload validity and maintainability impact |
| Human-centered support, not automation | Preserves learning, awareness, and ownership | Slower than full automation | Knowledge-transfer preservation metric |
| Sharing AI conversations in PRs/issues | Transparency and collaboration support | Unverified authority and provenance ambiguity | Provenance and verification outcome |

## Required Metrics for Trade-off-Aware Evaluation

A trade-off-aware evaluation should report more than model quality.

### Error reduction metrics

- hallucinated comments removed;
- unsupported claims removed;
- irrelevant comments removed;
- non-actionable comments removed;
- false positives reduced;
- low-value comments reduced;
- stale-context comments blocked;
- invalid repair suggestions blocked;
- unsupported security/performance claims blocked.

### Useful-feedback preservation metrics

- useful comments retained;
- useful comments wrongly removed;
- accepted comments retained;
- valuable-but-not-accepted comments retained;
- human-flagged issues still covered after filtering;
- rare but high-value categories retained;
- review coverage before and after filtering;
- coverage retained after reviewability/context-consistency gating.

### Cost and workflow metrics

- token cost;
- model-call count;
- inference latency;
- reviewer inspection time;
- human escalation rate;
- PR cycle time;
- developer trust/adoption;
- downstream code revision rate;
- signal-to-noise ratio;
- abandonment/merge outcomes;
- knowledge transfer and team-awareness preservation.

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
| Data cleaning improves training/evaluation | P08/P18 | Cleaning and reformulation can also remove or change intent. |
| Industrial filtering improves precision | P10 | Precision-first systems may suppress useful comments. |
| RAG/context enrichment helps selectively | P11/P16/P20 | Retrieval quality, model capacity, and token budget shape value. |
| Specification grounding improves trust | P12 | Specs must remain fresh and consistent with code. |
| Static-analysis context is useful but partial | P22/P48 | Tool output still needs interpretation and behavior validation. |
| Reviewer experience affects reference quality | P23 | Provenance of human labels/comments matters. |
| Reward optimization changes what is valued | P24/P30 | Reward/preference data may optimize proxies rather than human usefulness. |
| Structured output increases comprehensibility | P25/P46 | Issue/location/explanation/repair structure helps but requires validation. |
| AI review affects workflow differently from human review | P26/P27/P28 | Adoption, signal-to-noise, abandonment, and knowledge transfer matter. |
| Human review has socio-technical value | P37/P38/P39 | Automation must preserve usefulness, learning, awareness, and ownership. |
| Reviewability affects reliability | P40 | Low-reviewability changes should be treated as high-risk inputs. |
| Explanation quality is separate from issue detection | P41 | More rationale can help, but unsupported or verbose rationale can hurt. |
| AI conversations have provenance risks | P42 | Shared AI output should be verified and labeled. |
| Broad benchmarks may miss workflow validity | P43/P44/P45/P50 | Benchmark success is not equivalent to review usefulness. |
| Security review has asymmetric costs | P46 | False alarms erode trust; missed vulnerabilities can be high-impact. |
| Misalignment and safety filtering have coverage costs | P47 | Safer outputs may become less useful or too conservative. |
| Documentation-code consistency can be checked | P49 | Consistency checks help but add false-block and cost risks. |

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
| Low-reviewability input | Defer, ask for better description, or escalate | Bad input context can make both generation and evaluation unreliable. |
| Security claim without evidence | Escalate or require structured validation | False alarms and missed vulnerabilities have asymmetric costs. |
| Efficiency claim without benchmark/workload | Require evidence or lower priority | Avoid unsupported optimization advice. |
| Stale or contradictory documentation context | Run consistency check or escalate | Prevent stale-context-based comments. |

## Proposed Evaluation Formula Sketch

This is not a final mathematical model, but a conceptual scoring structure:

```text
NetReviewValue = UsefulFeedbackRetained
               - HarmfulCommentsShown
               - UsefulCommentsSuppressed
               - ReviewerOverhead
               - ComputationalCost
               - WorkflowDelay
               - LostKnowledgeTransfer
               - UnverifiedContextRisk
```

A practical framework should not optimize only one term.

## Open Questions

- [ ] How should useful-comment preservation be measured when usefulness itself is subjective?
- [ ] Should filters optimize for precision, recall, or reviewer value?
- [ ] How should a system decide between suppressing, rewriting, and escalating a comment?
- [ ] How can we measure wrong removal when reviewers never see suppressed comments?
- [ ] How can context-quality scores be combined with hallucination gates?
- [ ] What is the acceptable reviewer overhead for low-acceptance but high-value suggestions?
- [ ] How should reviewability gates report useful automation opportunities they skipped?
- [ ] How should security/performance specialized layers interact with general comment-quality filters?

## Working Claim for Paper

A trade-off-aware evaluation framework should evaluate the full decision pipeline, not only the generated comment. The key question is not only “Is this comment good?” but also:

- Should it be shown?
- Should it be filtered?
- Should it be rewritten?
- Should it be escalated?
- What useful feedback might be lost?
- What context quality or consistency risk remains?
- What cost or reviewer overhead is introduced?
- What socio-technical review value might automation remove?

This is the gap our framework should address.
