# Evaluation Dimensions

> [!NOTE]
> This file defines the evaluation dimensions for our framework. These dimensions should stay separate from problematic comment types. For example, `actionability` is an evaluation dimension, while `non-actionable comment` is a problematic comment type.

## Purpose

Current papers often collapse several concepts into a single quality, acceptance, or similarity score. Our framework separates them so that LLM-generated code review comments can be evaluated more precisely.

## Core Distinction

```text
Evaluation dimension = what we measure
Problematic comment type = what kind of failure occurred
Mitigation strategy = what we do about the failure
Trade-off = what we gain and what we risk losing
```

## Primary Evaluation Dimensions

| Dimension | Core Question | Typical Evidence | Related Papers |
|---|---|---|---|
| Technical correctness | Is the comment technically true? | Human labels, issue coverage, code resolution, factuality judge | P01, P02, P03, P04, P05, P06 |
| Relevance to code change | Is the comment about the actual reviewed change? | PR/diff alignment, reviewer acceptance, judge matching | P01, P02, P03, P04, P05 |
| Grounding / context alignment | Can the comment’s claims be traced to provided context? | Claim-to-diff grounding, hallucination labels | P02, P03 |
| Usefulness | Does the comment provide practical value to the developer/reviewer? | Reviewer value marking, code resolution, survey feedback | P01, P03, P07 |
| Actionability | Can the developer act on the comment? | Actionability gate, human labels, accepted comments | P01, P03, P07 |
| Specificity | Is the comment precise enough to identify the issue/location? | Line-level localization, specificity rubric | P01, P06 |
| Issue/review coverage | How many relevant issues are found? | Recall-like issue coverage, missed human-flagged issues | P04, P05, P06 |
| Hallucination / unsupported claim | Does the comment make unsupported claims? | Hallucination labels, judge scores, unsupported-claim examples | P02, P03 |
| False positive risk | Does the system show a bad/unnecessary comment? | Rejected comments, fabricated issues, unmatched comments | P02, P04, P07 |
| False negative risk | Does the system miss a useful/needed comment? | Missed human issues, recall gaps, issue coverage | P04, P05, P06 |
| Preservation of useful feedback | Does a filter keep useful comments? | Useful comments retained after filtering; value preservation | P02, P03, P07 |
| Wrong removal of useful comments | Does a gate/filter suppress good feedback? | False-positive filtering, hidden rejected-by-gate comments | P02, P03, P07 |
| Acceptance | Does the reviewer accept/use the generated comment directly? | Accepted generated comments | P07 |
| Perceived value | Does the reviewer find the comment useful even if not accepted? | Value-marking, survey feedback | P07 |
| Downstream revision | Does the comment lead to patch/code changes? | Code resolution, chunk-level revision after comments | P03, P07 |
| Reviewer time overhead | How much extra human time does the comment require? | Inspection/editing time, median overhead | P07 |
| Computational cost | What is the inference/judging cost? | Token cost, API cost, model-call count | P01, P02 |
| Latency | How much delay does the method introduce? | Inference time, reviewer wait time, pipeline delay | P01, P02, P07 |
| Operational complexity | How hard is it to deploy and maintain? | Workflow integration, quality gates, monitoring | P03, P07 |
| Developer trust | Does the system increase or erode trust? | Survey, adoption, feedback, acceptance patterns | P03, P07 |
| Workflow impact | Does it improve review workflow? | PR cycle time, human-comment reduction, live study outcomes | P03, P07 |

## Dimensions Often Collapsed Together

### Correctness vs usefulness

A comment can be technically correct but not useful. For example, a style-only nitpick may be true but low-value.

### Usefulness vs acceptance

A comment can be useful but not accepted directly. P07 is important here: some generated comments were not accepted but were still marked valuable as review or development tips.

### Actionability vs relevance

A comment can be relevant to the changed code but still not tell the developer what to do.

### Grounding vs correctness

A comment can be plausible and even correct in the real project, but unsupported by the context given to the model. For evaluation, this matters because the model should not make claims it cannot ground.

### Coverage vs precision

A system can cover more potential issues while also producing more false positives. This is a key trade-off for code review assistants.

## Suggested Evaluation Matrix

| Evaluation Layer | Dimensions | Why It Matters |
|---|---|---|
| Comment-level quality | correctness, relevance, grounding, actionability, specificity | Determines whether a generated comment is individually acceptable. |
| Review-level coverage | issue coverage, false negatives, missed human-flagged issues | Determines whether the review is complete enough. |
| Filtering/gating effect | false positives, false negatives, useful-feedback preservation, wrong removals | Determines whether mitigation helps or harms. |
| Human-centered value | acceptance, perceived value, downstream revision, reviewer overhead, trust | Determines whether developers benefit in practice. |
| System-level cost | computational cost, latency, operational complexity, escalation | Determines whether the approach is deployable. |
| Workflow impact | PR cycle time, human-comment reduction, code resolution | Determines whether the tool improves software engineering workflow. |

## Metrics to Look For in Future Papers

- Precision/recall/F1 against human labels.
- Hallucination precision/recall.
- Issue coverage / human-flagged issue recall.
- Code resolution rate.
- Direct acceptance rate.
- Valuable-but-not-accepted rate.
- Downstream revision rate.
- Reviewer inspection/editing time.
- False-positive filtering rate.
- Useful-comment preservation rate.
- Token cost and model-call count.
- Latency per review.
- Human escalation rate.
- Inter-rater agreement.

## Missing Metrics We Should Emphasize

The papers we have read often lack explicit metrics for:

- useful-comment preservation under filtering;
- wrong removal of useful comments;
- cost of reviewer interruption;
- human escalation rate;
- context-quality score;
- value-to-time ratio;
- attention-load effect of larger context;
- combined evaluation of correctness, usefulness, and actionability.

## Working Claim

A trade-off-aware evaluation framework should not report a single “comment quality” score. It should report a vector of dimensions that separates:

```text
correctness
+ grounding
+ usefulness
+ actionability
+ coverage
+ filtering effects
+ human value
+ cost/workflow impact
```

This separation is necessary because improving one dimension can harm another.