# Foundational Code Review Dimensions

> [!NOTE]
> This file synthesizes the foundational human-code-review papers added in P37–P41. These papers are not primarily LLM-code-review papers, but they define what code review is supposed to achieve and therefore constrain how LLM-generated review comments should be evaluated.

## Why These Papers Matter

The LLM-code-review literature often evaluates generated comments as if code review were only a defect-detection task. P37–P41 show that this is too narrow.

Modern code review is also about:

- maintainability;
- knowledge transfer;
- team awareness;
- shared ownership;
- rationale and explanation;
- author learning;
- reviewer attention and effort;
- change reviewability;
- and workflow fit.

Therefore, an evaluation framework for LLM-generated code review comments should measure whether automation preserves these values, not only whether it produces technically plausible comments.

## Paper Roles

| Paper | Role in Our Framework | Main Dimension Added |
|---|---|---|
| P37 — Modern Code Review at Google | Industrial grounding for review goals and workflow realities | Workflow impact; reviewer overhead; review value beyond defects |
| P38 — Expectations, Outcomes, and Challenges | Foundational evidence that review outcomes include knowledge transfer and alternative solutions | Usefulness beyond correctness; socio-technical value |
| P39 — Characteristics of Useful Code Reviews | Direct source for usefulness as a developer-centered property | Usefulness; actionability; value-to-time |
| P40 — Code Change Reviewability | Input-side view: some changes are easier or harder to review | Reviewability; context quality; attention load |
| P41 — Explaining Explanations | Explanation-side view: review comments often need useful rationale | Explanation quality; grounded rationale; clarity |

## Evaluation Dimensions Strengthened by P37–P41

| Dimension | Meaning for LLM-Generated Review Comments | Strongest Supporting Papers |
|---|---|---|
| Usefulness | The comment should provide practical value to the developer, not merely be technically plausible. | P38, P39 |
| Actionability | The comment should help the author decide what to do next. | P39, P41 |
| Explanation / rationale quality | The comment should explain why the concern matters and should ground that rationale. | P41 |
| Reviewability of input change | The reliability of the generated review depends on whether the input change is understandable, focused, and well-described. | P40 |
| Reviewer time overhead | Even correct comments can be harmful if they consume reviewer/author attention without enough value. | P37, P38, P39, P40 |
| Workflow impact | Generated comments should be evaluated by their effect on review process, not only isolated comment quality. | P37, P38 |
| Knowledge transfer / team awareness | Automation should not erase the educational and coordination roles of review. | P37, P38 |
| Developer trust | Trust depends on clarity, relevance, rationale, and fit with review norms. | P37, P39, P41 |

## Taxonomy Implications

P37–P41 motivate several problematic-comment types that are easy to miss in model-centric evaluations:

| Failure Type | Description | Source Lens |
|---|---|---|
| Low-value nitpick | Technically valid but not worth review attention. | P37, P39 |
| Non-actionable explanation | Gives a rationale or concern but does not help the author act. | P39, P41 |
| Vague rationale | The comment gestures at a problem without enough explanation. | P41 |
| Poor value-to-time comment | Costs more reviewer/author attention than the value it adds. | P37, P39, P40 |
| Context-poor comment | The comment may be weak because the input change is hard to review. | P40 |
| Knowledge-transfer loss | Automation suppresses human discussion that would have helped shared understanding. | P37, P38 |
| Workflow-friction comment | Comment increases review friction without improving correctness, maintainability, or understanding. | P37, P38 |

## Context-Quality Implications

P40 is especially important because it shifts part of evaluation from the generated output to the input change.

A generated comment should be interpreted together with:

- change size;
- locality of the change;
- coherence of the change;
- quality of the change description;
- availability of rationale;
- surrounding-code needs;
- and reviewer cognitive load.

This supports a pre-generation or pre-evaluation question:

> Is the available context reviewable enough for reliable automated review?

## Trade-off Implications

| Trade-off | Benefit | Risk | Related Papers |
|---|---|---|---|
| Automate review comments | Scales feedback and may reduce reviewer effort | May remove learning, shared ownership, and team awareness | P37, P38 |
| Filter low-value comments | Reduces noise and reviewer overhead | May suppress subtle but useful feedback | P39 |
| Require richer explanations | Improves understanding and trust | Increases reading time and may add unsupported rationale | P41 |
| Add more context | Can improve grounding | Can increase cognitive/token load and reduce focus | P40 |
| Use reviewability gates | Avoids unreliable generation on hard changes | May reduce coverage or skip useful automation opportunities | P40 |

## How This Changes Our Framework

The framework should include a human-code-review foundation layer:

```text
Generated comment quality
+ Input change reviewability
+ Explanation/rationale quality
+ Developer usefulness
+ Reviewer overhead
+ Workflow and knowledge-transfer impact
```

This layer prevents the framework from becoming a narrow classifier of hallucinated or correct comments.

## Suggested Integration Points

- Add `reviewability` to the input/context-quality layer.
- Add `knowledge transfer` and `team awareness` to workflow-level evaluation.
- Add `value-to-time ratio` as a human-centered metric.
- Treat `usefulness` as separate from correctness and acceptance.
- Treat `explanation quality` as separate from issue detection.
- Add `automation may remove socio-technical value` to the trade-off framework.

## Draft Claim for the Paper

Foundational code-review studies show that review quality cannot be reduced to defect detection. Modern code review also supports maintainability, knowledge transfer, team awareness, shared ownership, and author understanding. Therefore, evaluating LLM-generated code review comments requires a broader framework that includes usefulness, actionability, explanation quality, reviewability of the input change, reviewer overhead, and workflow impact.
