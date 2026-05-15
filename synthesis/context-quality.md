# Context Quality

> [!NOTE]
> This file tracks how papers treat context in LLM-based code review. The main claim is that context quality should be evaluated directly, rather than assuming more context automatically improves review quality.

## Core Claim

Context in LLM-based code review is not just an input-size problem. It is an evaluation object.

A review assistant can receive more context and still perform worse if the context is noisy, irrelevant, contradictory, stale, too broad, missing the relevant file-level detail, hard to review, or hard for the model to attend to.

## Working Hypothesis

Context should not be treated as a simple quantity. More context can help, but it can also:

- add noise;
- increase inference cost;
- increase latency;
- distract the model from the actual diff;
- create unsupported assumptions;
- make judge/evaluator matching harder;
- hide contradictions between documentation and behavior;
- and reduce review quality.

A useful framework should evaluate context quality, not just context size.

## Context-Related Evidence from Papers

| Paper | How Context Appears | Key Evidence | Implication |
|---|---|---|---|
| P01 — DeepCRCEval | Contextual adequacy is one of the quality dimensions. | Some comments require more file-level or surrounding context than the snippet provides. | Context adequacy affects whether a comment can be judged useful or complete. |
| P02 — HalluJudge | Context is the grounding source for hallucination detection. | A comment is hallucinated/context-misaligned when its claims are unsupported by the diff. | Context quality can be evaluated through claim-to-context grounding. |
| P03 — RovoDev | Context includes PR title/description, Jira issue, code changes, guidelines, and task instructions. | Missing language/framework/version/surrounding-code context can cause incorrect or non-actionable comments. | Production systems need context selection and quality checks, not only generation prompts. |
| P04 — SWE-PRBench | Context configurations include diff-only, diff + file content, and full context. | Models can degrade as context expands. | More context can hurt; context quantity and quality must be separated. |
| P05 — SWRBench | PR-centric context and full-project setting. | Benchmark realism improves with PR context, but full context does not guarantee useful review. | Realistic context still needs quality, focus, and cost evaluation. |
| P06 — ContextCRBench | Enriched semantic/code context. | Highlights missing semantic context, noisy data, and coarse granularity. | Context enrichment must be evaluated as context quality, not assumed beneficial. |
| P10 — BitsAI-CR | Production context, rules, and review filters. | Rules and filters shape what context is considered actionable. | Context quality interacts with deployment policy. |
| P11/P20 — RAG review papers | Retrieved exemplars and review history. | Retrieval can help but can also distract or add stale/irrelevant examples. | Retrieval relevance and freshness are context-quality dimensions. |
| P12 — SGCR | Specification-grounded review. | Specifications provide grounding but require freshness and maintenance. | Context consistency includes code/spec alignment. |
| P13/P16 | Call graphs, summaries, and RAG routing. | More semantic context helps only when the model can use it. | Model capacity and attention load affect context usability. |
| P22/P48 | Static-analysis context. | Static analyzers provide focused signals, but warnings can be misinterpreted. | Tool-generated context needs provenance and interpretation checks. |
| P23 | Reviewer experience. | Reviewer history and ownership can signal reference quality. | Context includes human/provenance context, not only code. |
| P37/P38 | Human-review context. | Review supports knowledge transfer, maintainability, and team awareness. | Context includes socio-technical goals of review. |
| P39 | Useful review feedback. | Usefulness depends on reviewer/developer needs and context. | Context quality should include value-to-attention and developer relevance. |
| P40 — Reviewability | Input changes differ in how easy they are to review. | Change size, coherence, locality, and description quality affect review difficulty. | Reviewability is an input-side context-quality layer. |
| P41 | Explanations in reviews. | Explanations need grounded rationale and clarity. | Rationale context should be evaluated separately from issue detection. |
| P42 | Shared ChatGPT conversations in PRs/issues. | AI outputs become part of collaboration context. | AI-generated context needs provenance and verification. |
| P43/P44/P45 | LLM-for-SE and code-LLM surveys. | Broad coding benchmarks may miss workflow-specific context. | Benchmark context is not equal to real review context. |
| P46 | Vulnerability detection and repair. | Security claims need category, location, exploitability, and repair evidence. | Secure review requires specialized context and stronger evidence. |
| P49 — METAMON | Documentation-behavior consistency. | Documentation and behavior can diverge. | Context consistency and freshness should be explicit checks. |
| P50 | Efficiency benchmark. | Efficiency claims need workload and measurement context. | Non-functional comments require benchmark/workload grounding. |

## Proposed Dimensions of Context Quality

| Dimension | Question | Failure Mode |
|---|---|---|
| Relevance | Is the context related to the reviewed change? | Irrelevant retrieved files distract the model. |
| Completeness | Does the context include what is needed to judge the issue? | Missing file-level or framework-level information causes wrong assumptions. |
| Specificity | Is the context narrow enough to focus the model? | Overly broad context dilutes attention. |
| Consistency | Do the commit message, PR description, comments, specs, docs, and diff agree? | Inconsistent metadata or stale docs cause misleading review comments. |
| Groundability | Can each generated claim be traced to evidence in the context? | Unsupported claims and hallucinated concerns. |
| Locality | Is the relevant context near the changed lines or spread across files? | Wrong-location or non-traceable comments. |
| Freshness | Is the context aligned with the current version of the code? | Stale documentation or outdated examples cause false suggestions. |
| Reviewability | Is the input change understandable enough for reliable review? | Large, scattered, poorly described changes cause weak review. |
| Provenance | Where did the context come from: human reviewer, model, static analyzer, spec, docs, benchmark? | Unverified model-generated context or weak reference quality. |
| Behavioral evidence | Is there test, execution, benchmark, or behavioral evidence for the claim? | Performance/security/repair claims without evidence. |
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
- Stale documentation or stale examples.
- Documentation that disagrees with actual behavior.
- Unsupported inference from partial context.
- Generated claim that cannot be grounded in the diff.
- Static-analysis warning misinterpreted as project truth.
- Security claim without vulnerability evidence.
- Performance/efficiency claim without workload or benchmark evidence.
- AI-generated context shared without provenance or verification.
- Plausible but unverified assumption.

## Evaluation Questions

- [ ] What context was provided to the generator?
- [ ] What context was provided to the evaluator or judge?
- [ ] Is the context complete enough for the comment being generated?
- [ ] Is the context narrow enough to avoid distraction?
- [ ] Can every generated claim be mapped to a context span?
- [ ] Does the input change have enough reviewability for reliable automated review?
- [ ] Do documentation, specifications, PR description, and code behavior agree?
- [ ] Is the context human-written, tool-generated, model-generated, or mixed?
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
  reviewability,
  provenance,
  behavioral_evidence,
  attention_load,
  cost
}
```

This avoids the simplistic assumption that more context means better context.

## Relationship to Gate Design

Context quality can be used at multiple stages:

1. **Pre-generation gate**  
   Decide whether the available context is sufficient, fresh, consistent, and reviewable enough to generate a reliable review comment.

2. **Generation-time context selection**  
   Choose the smallest context set that is likely to support the review task.

3. **Post-generation grounding check**  
   Verify whether the generated comment is supported by the selected context.

4. **Consistency check**  
   Detect contradictions between code, documentation, specs, PR description, static analyzer output, and model-generated context.

5. **Human escalation**  
   Escalate when the model detects that context is insufficient, inconsistent, stale, or too risky.

## Open Questions

- [ ] Should context quality be a precondition for generation, an evaluation dimension, or both?
- [ ] Can context quality be estimated without generating the review comment first?
- [ ] How should context quality interact with hallucination detection?
- [ ] How much useful feedback is lost if we suppress comments generated under low-quality context?
- [ ] Is there an optimal context size for code review, or does it depend on issue type?
- [ ] How can we detect attention dilution caused by excessive context?
- [ ] How should context consistency be evaluated when docs, specs, and behavior disagree?

## Draft Paragraph for Paper

A recurring limitation in current LLM-based code review evaluation is that context is often treated as an input configuration rather than as an evaluation object. Recent work suggests that this assumption is unsafe. HalluJudge frames hallucination as a failure of grounding between generated claims and the code diff. RovoDev shows that missing language, framework, or surrounding-code context can lead to incorrect or non-actionable comments. SWE-PRBench further shows that adding more context can degrade review performance across models. Human-review studies add that context also includes reviewability, workflow goals, reviewer attention, and developer usefulness. METAMON-like consistency work further suggests that documentation and behavior may diverge, so stale or contradictory context should be checked explicitly. Together, these results suggest that future evaluation frameworks should measure context quality directly, including relevance, completeness, specificity, consistency, groundability, reviewability, provenance, freshness, behavioral evidence, and cost.
