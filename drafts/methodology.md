# Methodology Draft

> [!NOTE]
> This is the working methodology for the paper. The method should be framed as a **framework-oriented focused evidence synthesis** supported by an operational taxonomy and a small annotated evidence layer. It should not be framed as a benchmark paper or a comparison of several mitigation methods.

## 1. Method Type

This study uses a focused evidence synthesis to analyze how current work evaluates LLM-generated code review comments and where those evaluations remain incomplete. The synthesis is used to derive an operational taxonomy, a multi-dimensional evaluation framework, and a trade-off matrix.

The study is not intended to be a full systematic literature review unless the search and screening protocol is expanded. It is also not intended to be a large-scale benchmark or a model-performance comparison. The empirical component, if included, should be framed as an illustrative annotated study that supports the taxonomy and framework.

The method has four connected parts:

1. focused evidence synthesis over the selected paper pool;
2. construction of an operational taxonomy of problematic comments;
3. design of a multi-dimensional, trade-off-aware evaluation framework;
4. a small annotated evidence layer to test whether the taxonomy can be applied consistently.

## 2. Research Questions

| RQ | Question | Output |
|---|---|---|
| RQ1 | What types of problematic comments occur in LLM-generated code review, and how can they be operationally annotated? | Operational taxonomy and annotation guideline |
| RQ2 | Which evaluation dimensions are needed to assess problematic comments beyond technical correctness? | Multi-dimensional evaluation matrix |
| RQ3 | How do common mitigation strategies trade off error reduction against useful-feedback preservation, review coverage, human effort, and computational cost? | Trade-off framework and measurable trade-off dimensions |
| RQ4 | How does context quality affect the occurrence, detection, and mitigation of problematic review comments? | Context-quality layer and context-failure analysis |
| RQ5 | What framework can guide trade-off-aware evaluation of LLM-generated code review comments? | Final evaluation framework |

## 3. Paper Selection Strategy

We conduct a focused literature review of recent and foundational papers related to LLM-based code review evaluation, automated code review, human-centered code review, LLM-as-a-Judge evaluation, and adjacent evidence on security, static analysis, context consistency, and non-functional quality.

We prioritize papers that include at least one of the following:

- evaluation of generated code review comments;
- hallucination, unsupported-claim, or context-alignment analysis;
- PR-level, benchmark-level, or production-level evaluation;
- human/user-study evaluation of generated review comments;
- cost, latency, reviewer-overhead, or workflow-related metrics;
- filtering, gating, aggregation, or LLM-as-a-Judge mechanisms;
- context selection, retrieval, or context-enrichment mechanisms for code review;
- human-centered evidence on code review usefulness, reviewability, or workflow value.

### Inclusion Criteria

A paper is included if it satisfies at least one of these criteria:

- It evaluates LLM-generated code review comments or review outputs.
- It proposes or evaluates a benchmark for code review automation.
- It studies hallucination, grounding, or context alignment in generated review comments.
- It reports human, user-study, or production signals for LLM-based code review.
- It discusses context, retrieval, specification, static analysis, or project-level information for code review.
- It evaluates filtering, gating, judging, aggregation, routing, or human escalation of generated comments.
- It provides foundational evidence on human code review usefulness, reviewability, or workflow value.
- It provides relevant evidence about evaluator validity, LLM-as-a-Judge bias, or measurement reliability.

### Exclusion Criteria

A paper is excluded if:

- it studies general code generation without relevance to code review evaluation;
- it studies program repair or bug fixing without review comments or review workflow;
- it only proposes a model without evaluation dimensions relevant to review comments;
- it is too far from LLM-based code review, automated code review, or evaluation methodology;
- it provides no usable evidence for taxonomy, context quality, evaluation dimensions, evaluator validity, or trade-offs.

### Paper Pool

The working paper pool is maintained in:

```text
matrices/paper-pool.md
```

The current synthesis is based on the P01–P50 paper pool. The paper pool includes both core papers and background/adjacent papers. Core papers provide direct evidence about LLM-based code review evaluation, while adjacent papers support specific framework dimensions such as human review usefulness, evaluator validity, security review, static-analysis-guided feedback, context consistency, or non-functional quality.

## 4. Coding Protocol

Each paper is coded using the repository paper-analysis template:

```text
templates/paper-analysis-template.md
```

For each paper, we extract:

- bibliographic metadata;
- study type and contribution type;
- dataset/study context;
- input context available to the model or evaluator;
- output being evaluated;
- models, systems, prompts, and context strategies;
- evaluation metrics and methods;
- human annotation, user-study, or production-feedback protocol;
- covered and missing evaluation dimensions;
- explicitly defined and inferred problematic comment types;
- context-quality dimensions and context failure types;
- filtering, gating, aggregation, routing, verification, or escalation trade-offs;
- evaluator-validity concerns when LLM-as-a-Judge is used;
- limitations from the paper’s perspective;
- limitations from our perspective;
- evidence relevant to the research questions.

## 5. Coding Labels

We use the following labels to separate evidence from interpretation:

| Label | Meaning |
|---|---|
| `Reported` | Explicitly stated in the paper. |
| `Inferred` | Reconstructed from examples, tables, results, or implications. |
| `Our perspective` | Our critique, synthesis, or research positioning. |
| `Not reported` | The paper does not provide this information. |
| `Not applicable` | The field does not fit the paper. |
| `Partially` | The paper touches the dimension but does not operationalize it clearly. |

This distinction is important because the framework should not overclaim what individual papers actually report.

## 6. Cross-Paper Synthesis Process

After coding individual papers, we synthesize the evidence in four steps.

### Step 1 — Within-paper extraction

Each paper is analyzed using the template. Evidence is extracted for evaluation dimensions, problematic comment types, context quality, evaluator validity, and trade-offs.

### Step 2 — Cross-paper comparison

We compare papers across recurring dimensions:

- what they evaluate;
- what context they provide;
- what failure types they observe;
- what human, annotation, or production signals they use;
- what costs or workflow effects they measure;
- how they use LLM-as-a-Judge or human evaluators;
- which dimensions they omit.

### Step 3 — Gap synthesis

We identify gaps that recur across papers, especially missing links between:

```text
error reduction
useful-feedback preservation
review coverage
human effort
computational cost
context quality
evaluator validity
mitigation decision
```

### Step 4 — Framework construction

We derive a framework that connects:

```text
Input / Context Quality
      ↓
Generated Review Comment
      ↓
Problematic Comment Type
      ↓
Evaluation Dimension
      ↓
Mitigation Decision
      ↓
Trade-off / Cost / Workflow Impact
      ↓
Evaluator Validity
```

## 7. Taxonomy Construction

The taxonomy is derived from three sources:

1. failure types explicitly reported in the reviewed papers;
2. failure types inferred from examples, evaluation criteria, and limitations;
3. failure types needed to operationalize trade-off-aware evaluation.

The taxonomy is intended to be operational. Each category should eventually include:

- a definition;
- inclusion criteria;
- exclusion criteria;
- positive examples;
- negative examples;
- ambiguous cases;
- links to evaluation dimensions;
- likely mitigation decisions.

Candidate high-level categories include:

| Category | Description |
|---|---|
| Unsupported or hallucinated comment | The comment makes a claim not supported by the available diff or context. |
| Irrelevant comment | The comment is unrelated to the reviewed change. |
| Incorrect technical claim | The comment is technically wrong. |
| Wrong location or wrong cause | The comment identifies the wrong line, location, or causal explanation. |
| Non-actionable comment | The developer cannot determine what to do next. |
| Low-value nitpick | The comment may be valid but is not worth reviewer attention. |
| Invalid fix suggestion | The suggested fix does not solve the issue or may introduce a regression. |
| Context-dependent case | The comment cannot be judged reliably without more context. |
| Useful but not directly acceptable | The comment is not directly applicable but still provides useful insight. |

The current taxonomy draft lives in:

```text
synthesis/problematic-comment-taxonomy.md
```

## 8. Evaluation Framework Construction

The evaluation framework is built to avoid collapsing all quality concerns into a single score. It should separate at least seven layers:

1. **Input/context quality**  
   Relevance, completeness, specificity, consistency, freshness, reviewability, provenance, behavioral evidence, attention load, and cost.

2. **Generated-comment quality**  
   Correctness, relevance, grounding, specificity, explanation quality, usefulness, and actionability.

3. **Problematic-comment type**  
   The failure category assigned to the comment, if any.

4. **Usefulness and actionability**  
   Whether the comment provides value to the developer and whether it supports a concrete next step.

5. **Mitigation decision**  
   Whether the comment should be shown, suppressed, rewritten, aggregated, or escalated.

6. **Cost and workflow impact**  
   Computational cost, latency, human verification cost, reviewer overhead, review coverage, trust, and socio-technical review value.

7. **Evaluator validity**  
   Whether the evaluator or judge used to assess the comment is reliable, calibrated, and robust to prompt or order effects.

## 9. Annotation Protocol

The paper should include a small annotation layer to support the taxonomy and framework. This is important because using an existing dataset without a new annotation layer may leave the contribution too abstract.

### Annotation Goals

The annotation should answer:

- Can the taxonomy be applied consistently?
- Which problematic comment types appear in the sample?
- Which comments are useful but not directly acceptable?
- Which comments require more context to judge?
- What decisions would an evaluator make: show, suppress, rewrite, or escalate?
- What disagreements occur between annotators?

### Suggested Sample

A minimum viable sample should contain approximately 100–200 generated review comments. If resources are limited, a smaller pilot can be used first.

The sample may come from:

- an existing code review benchmark;
- generated comments over a controlled subset of code changes;
- comments collected from prior work, if licensing permits;
- or a hybrid of existing samples plus newly generated comments.

### Annotators

The preferred setup is at least two annotators with software engineering experience.

If only one annotator is available for the first pass, the paper should not overclaim annotation reliability. A second annotator should be added for at least a subset to estimate agreement.

### Pilot Round

Before full annotation, annotators should label a pilot subset. The pilot should be used to:

- refine label definitions;
- identify ambiguous cases;
- improve decision rules;
- align annotators on borderline examples.

### Agreement Reporting

The study should report inter-annotator agreement where feasible. Possible metrics include:

- Cohen’s kappa for two annotators and categorical labels;
- Krippendorff’s alpha when labels are missing or more annotators are involved;
- percentage agreement as a supplementary descriptive metric.

Agreement should be reported separately for different label groups when possible, because technical correctness, usefulness, actionability, and decision labels may have different ambiguity levels.

### Conflict Resolution

Disagreements should be resolved through discussion or adjudication. The final dataset should preserve:

- annotator 1 label;
- annotator 2 label;
- final resolved label;
- disagreement reason where useful.

The detailed annotation guideline should be stored in:

```text
method/annotation-guideline.md
```

The evaluation schema should be stored in:

```text
method/evaluation-schema.md
```

## 10. Annotated Evidence Layer

The annotated evidence layer should support the framework rather than become the main identity of the paper. It can be framed as an illustrative study.

The layer should report:

- label distribution across problematic-comment types;
- distribution of show/suppress/rewrite/escalate decisions;
- examples of useful but not directly acceptable comments;
- examples of context-dependent comments;
- disagreement patterns between annotators;
- observed trade-offs between error reduction and useful-feedback preservation;
- basic cost indicators if mitigation strategies are evaluated.

The study should avoid claiming general model superiority unless the experimental design is expanded substantially.

## 11. Trade-off Analysis

For each mitigation strategy or evaluation decision, the analysis should ask:

| Question | Purpose |
|---|---|
| What failure type does it reduce? | Error-reduction effect |
| What useful feedback might it suppress? | Useful-feedback preservation |
| What review coverage is preserved or lost? | Coverage effect |
| What additional human effort is required? | Human cost |
| What additional model calls or latency are required? | Computational cost |
| When should the system escalate to a human? | Risk control |
| How reliable is the evaluator? | Evaluator validity |

The paper should avoid presenting a mitigation strategy as simply better unless these trade-offs are reported.

## 12. Main Analytical Distinctions

### Evaluation dimensions vs problematic comment types

Evaluation dimensions and failure types should remain separate.

Examples of evaluation dimensions:

- correctness;
- relevance;
- grounding;
- usefulness;
- actionability;
- specificity;
- coverage;
- cost;
- latency;
- workflow impact.

Examples of problematic comment types:

- hallucinated comment;
- unsupported claim;
- irrelevant comment;
- non-actionable comment;
- vague comment;
- low-value nitpick;
- wrong API/type assumption;
- missed issue;
- technically plausible but unsupported comment.

### Context quantity vs context quality

More context can increase available evidence, but it can also increase noise, token cost, latency, attention dilution, irrelevant retrieved material, or inconsistent signals. Therefore, context is treated as an evaluation object, not only an input configuration.

### Acceptance vs usefulness

Reviewer acceptance and usefulness should be separated. A generated comment may be rejected but still useful as a development or review tip. Conversely, a comment may be accepted but still be low-value or harmful in broader workflow terms.

### Filtering success vs useful-feedback preservation

A filter or gate should not only be evaluated by how many problematic comments it removes. It should also be evaluated by how many useful comments it wrongly removes, how much cost it adds, how it affects review coverage, and whether it creates reviewer trust or overreliance issues.

## 13. Threats to Validity

Potential threats:

- paper selection may be incomplete;
- recent papers may change quickly;
- some analyzed papers are preprints;
- industrial studies may use proprietary data;
- inferred taxonomy items may depend on our interpretation;
- human feedback and benchmark ground truth are imperfect;
- the annotation sample may be too small to generalize;
- annotators may disagree on usefulness and actionability;
- generated comments may depend on one model or prompt setup;
- LLM-as-a-Judge results may introduce evaluator bias.

Mitigation:

- use explicit inclusion/exclusion criteria;
- label claims as `Reported`, `Inferred`, or `Our perspective`;
- separate paper limitations from our critique;
- keep a transparent paper pool and cross-paper synthesis matrix;
- use a pilot annotation round;
- report inter-annotator agreement;
- preserve disagreement notes;
- avoid claiming broad model superiority from an illustrative sample;
- treat LLM-as-a-Judge as a measurement instrument rather than ground truth.

## 14. Current Methodological Positioning

The paper should be positioned as:

> a framework-oriented focused evidence synthesis of LLM-based code review evaluation, supported by an operational taxonomy, an annotation protocol, and a small annotated evidence layer.

It should not be positioned as:

- a new LLM model;
- a new leaderboard benchmark;
- only a hallucination detector;
- only a RAG/context retrieval method;
- a generic survey of LLMs for software engineering;
- or a small method-comparison paper whose main result is a winning strategy.

## 15. Next Methodology Tasks

- [ ] Create `method/annotation-guideline.md`.
- [ ] Create `method/evaluation-schema.md`.
- [ ] Create `synthesis/final-framework.md`.
- [ ] Decide the initial dataset and sampling plan.
- [ ] Define the pilot annotation size.
- [ ] Decide whether LLM-as-a-Judge is used only as support or also as one evaluated instrument.
