# Context Quality

> [!NOTE]
> This file tracks how papers treat context in LLM-based code review. The main claim is that context quality should be evaluated directly, rather than assuming more context automatically improves review quality.

## Core Claim

Context in LLM-based code review is not just an input-size problem. It is an evaluation object.

A review assistant can receive more context and still perform worse if the context is noisy, irrelevant, contradictory, too broad, missing the relevant file-level detail, or hard for the model to attend to.

## Working Hypothesis

Context should not be treated as a simple quantity. More context can help, but it can also:

- add noise,
- increase inference cost,
- increase latency,
- distract the model from the actual diff,
- create unsupported assumptions,
- make judge/evaluator matching harder,
- and reduce review quality.

A useful framework should evaluate context quality, not just context size.

## Context-Related Evidence from Papers

| Paper | How Context Appears | Key Evidence | Implication |
|---|---|---|---|
| P01 — DeepCRCEval | Contextual adequacy is one of the quality dimensions. | Some comments require more file-level or surrounding context than the snippet provides. | Context adequacy affects whether a comment can be judged useful or complete. |
| P02 — HalluJudge | Context is the grounding source for hallucination detection. | A comment is hallucinated/context-misaligned when its claims are unsupported by the diff. | Context quality can be evaluated through claim-to-context grounding. |
| P03 — RovoDev Code Reviewer | Context includes PR title/description, Jira issue, code changes, guidelines, and task instructions. | Missing language/framework/version/surrounding-code context can cause incorrect or non-actionable comments. | Production systems need context selection and quality checks, not only generation prompts. |
| P04 — SWE-PRBench | Three frozen context configurations: diff-only, diff + file content, full context. | All eight evaluated models degrade as context expands from diff-only to richer context settings. | More context can hurt; context quantity and context quality must be separated. |

## Proposed Dimensions of Context Quality

| Dimension | Question | Failure Mode |
|---|---|---|
| Relevance | Is the context related to the reviewed change? | Irrelevant retrieved files distract the model. |
| Completeness | Does the context include what is needed to judge the issue? | Missing file-level or framework-level information causes wrong assumptions. |
| Specificity | Is the context narrow enough to focus the model? | Overly broad context dilutes attention. |
| Consistency | Do the commit message, PR description, comments, and diff agree? | Inconsistent metadata causes misleading review comments. |
| Groundability | Can each generated claim be traced to evidence in the context? | Unsupported claims and hallucinated concerns. |
| Locality | Is the relevant context near the changed lines or spread across files? | Wrong-location or non-traceable comments. |
| Freshness | Is the context aligned with the current version of the code? | Stale documentation or outdated examples cause false suggestions. |
| Interpretability | Can a human or judge understand why this context was selected? | Opaque retrieval makes debugging hard. |
| Cost | How expensive is it to provide and process the context? | High token cost and latency. |
| Attention load | Can the model attend to the relevant part of the context? | Performance drops even when relevant information is technically present. |

## Context Failure Types

- Missing project context.
- Missing language or framework context.
- Missing version or dependency context.
- Missing surrounding code.
- Missing cross-file dependency.
- Irrelevant retrieved context.
- Excessive context that dilutes attention.
- Contradictory PR metadata and diff.
- Unsupported inference from partial context.
- Generated claim that cannot be grounded in the diff.
- Plausible but unverified assumption.

## Evaluation Questions

- [ ] What context was provided to the generator?
- [ ] What context was provided to the evaluator or judge?
- [ ] Is the context complete enough for the comment being generated?
- [ ] Is the context narrow enough to avoid distraction?
- [ ] Can every generated claim be mapped to a context span?
- [ ] Does additional context improve or degrade performance?
- [ ] Does the paper measure context-related false positives?
- [ ] Does the paper measure context-related false negatives?
- [ ] Does the paper report token cost or latency for larger context?
- [ ] Does the paper distinguish context availability from context usability?

## Possible Context-Quality Score

A future framework could represent context quality as a vector rather than one scalar:

```text
ContextQuality = {
  relevance,
  completeness,
  specificity,
  consistency,
  groundability,
  locality,
  freshness,
  attention_load,
  cost
}
```

This avoids the simplistic assumption that more context means better context.

## Relationship to Gate Design

Context quality can be used at multiple stages:

1. **Pre-generation gate**  
   Decide whether the available context is sufficient to generate a reliable review comment.

2. **Generation-time context selection**  
   Choose the smallest context set that is likely to support the review task.

3. **Post-generation grounding check**  
   Verify whether the generated comment is supported by the selected context.

4. **Human escalation**  
   Escalate when the model detects that context is insufficient or inconsistent.

## Open Questions

- [ ] Should context quality be a precondition for generation, an evaluation dimension, or both?
- [ ] Can context quality be estimated without generating the review comment first?
- [ ] How should context quality interact with hallucination detection?
- [ ] How much useful feedback is lost if we suppress comments generated under low-quality context?
- [ ] Is there an optimal context size for code review, or does it depend on issue type?
- [ ] How can we detect attention dilution caused by excessive context?

## Draft Paragraph for Paper

A recurring limitation in current LLM-based code review evaluation is that context is often treated as an input configuration rather than as an evaluation object. Recent work suggests that this assumption is unsafe. HalluJudge frames hallucination as a failure of grounding between generated claims and the code diff. RovoDev shows that missing language, framework, or surrounding-code context can lead to incorrect or non-actionable comments. SWE-PRBench further shows that adding more context can degrade review performance across models. Together, these results suggest that future evaluation frameworks should measure context quality directly, including relevance, completeness, specificity, consistency, groundability, and cost.
