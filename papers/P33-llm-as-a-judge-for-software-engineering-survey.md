# P33 — LLM-as-a-Judge for Software Engineering: Literature Review, Vision, and the Road Ahead

> [!NOTE]
> Compact v2 analysis. P33 is the broader and newer survey/roadmap version of the LLM-as-a-Judge-in-SE line. It reviews primary studies and is useful for positioning our evaluator-validity discussion within the SE lifecycle. Metadata has been aligned with the spreadsheet: the official ACM TOSEM DOI is retained, and arXiv remains the preprint/PDF source.

## Status

- Paper ID: `P33`
- Analysis status: `First pass completed from PDF; metadata aligned with spreadsheet; needs BibTeX cleanup`
- Priority: `High`
- Reading depth: `Read once from PDF`
- Last updated: `2026-05-15`
- Confidence: `High`

## Bibliographic Information

| Field | Value |
|---|---|
| Title | LLM-as-a-Judge for Software Engineering: Literature Review, Vision, and the Road Ahead |
| Authors | Junda He, Jieke Shi, Terry Yue Zhuo, Christoph Treude, Jiamou Sun, Zhenchang Xing, Xiaoning Du, David Lo |
| Year | 2025 |
| Venue / Source | ACM Transactions on Software Engineering and Methodology |
| Publication type | Peer-reviewed journal article / survey |
| Link | https://dl.acm.org/doi/abs/10.1145/3797276 |
| DOI / arXiv | DOI: 10.1145/3797276; arXiv:2510.24367 |

```bibtex
% TODO: Add checked ACM BibTeX.
```

## One-Sentence Summary

> P33 surveys LLM-as-a-Judge studies in software engineering and proposes a roadmap toward reliable, robust, scalable, multi-faceted human-surrogate judges for SE artifacts.

## Main Contribution

The paper provides a literature review of LLM-as-a-Judge applications across the software lifecycle, formalizes the judge paradigm, identifies key limitations, and proposes a roadmap for benchmarks, empirical evaluation, domain expertise, tool augmentation, human-in-the-loop evaluation, multimodality, and robustness.

## Formal Definition

The paper defines LLM-as-a-Judge as:

```text
E(T, C, X, R) -> (Y, E, F)
```

| Symbol | Meaning |
|---|---|
| `T` | Evaluation type: point-wise, pair-wise, or list-wise. |
| `C` | Evaluation criteria such as correctness, helpfulness, readability. |
| `X` | Evaluation item or set of candidate artifacts. |
| `R` | Optional reference. |
| `Y` | Evaluation result: score, ranking, or best-choice selection. |
| `E` | Optional explanation/justification. |
| `F` | Optional feedback for improvement. |

## SE Artifact Taxonomy

| SE Activity | Artifacts / Coverage |
|---|---|
| Requirements engineering | Requirements documents, system specifications, user stories. |
| Coding assistance | Generated code, code summaries, translated code, answers to software questions. |
| Quality assurance | Bug reports, tests, vulnerability explanations. |
| Maintenance | Commit messages, code patches. |

## Common Evaluation Criteria

| Criterion Family | Examples |
|---|---|
| Code functionality | Functional correctness, fault tolerance, error handling. |
| Code quality | Complexity/efficiency, helpfulness, readability, stylistic consistency, reference similarity, minor warnings. |
| Summary quality | Language clarity, content adequacy, developer usefulness. |
| Requirements quality | Completeness, correctness, feasibility, necessity, unambiguity, verifiability. |
| Patch quality | Functional correctness, semantic equivalence, vulnerability relevance, actionability. |

## Method Families Reviewed

| Family | Examples / Role |
|---|---|
| Structured prompting | Rubrics, scoring scales, explicit output format. |
| Decomposition / multi-step reasoning | AST decomposition, pseudocode, recursive semantic comprehension, MCTS-style judging. |
| Agentic / tool-augmented judging | File-system interaction, execution, static linting, unit tests, dependency graphs. |
| Multi-judge / ensemble systems | Multiple evaluators for correctness, readability, runtime, negotiation/aggregation. |
| Specialized smaller judges | Knowledge distillation and fine-tuning on human judgments. |
| Judge-guided improvement | Candidate reranking and iterative refinement with judge feedback. |

## Key Limitations Identified

| Limitation | Why It Matters |
|---|---|
| Lack of large-scale expert-annotated benchmarks | Many studies use small human-alignment datasets. |
| Rating indeterminacy | Some SE qualities lack a single correct label. |
| Evaluator uncertainty | Experts may legitimately disagree. |
| Evaluator preferences | Team/project conventions influence judgment. |
| Inadequacy of traditional alignment metrics | IRA/correlation metrics assume simpler human-rater settings. |
| Inconsistent empirical findings | Different datasets/prompts/models lead to contradictory conclusions. |
| Bias in LLM judges | Position, verbosity, egocentric and auxiliary-information biases remain underexplored. |
| Insufficient SE expertise | Generating correct code does not guarantee judging alternatives well. |
| Mono-modal focus | SE includes diagrams, GUI mockups, screenshots, architecture sketches. |
| Limited tool integration | Many judges still rely only on internal LLM knowledge. |
| Adversarial threats | Semantics-preserving manipulations can mislead judges. |

## Roadmap

| Horizon | Direction |
|---|---|
| Short-term | Build comprehensive benchmarks and nuanced evaluation protocols. |
| Short-term | Conduct systematic empirical evaluations and bias analyses. |
| Long-term | Enhance SE domain expertise and expert tacit knowledge. |
| Long-term | Incorporate multi-modal assessment. |
| Long-term | Integrate SE tools such as static analyzers, formal verification, profilers, and model checkers. |
| Long-term | Establish human-in-the-loop collaboration and feedback loops. |
| Long-term | Build robust judges through adversarial testing and fortification. |

## Evaluation Dimensions Covered

| Dimension | Coverage | Notes |
|---|---|---|
| Judge taxonomy | Very high | Formal input/output definition. |
| SE artifact coverage | Very high | Lifecycle-wide mapping. |
| Benchmark gaps | High | Large-scale expert labels and subjectivity. |
| Human uncertainty/preferences | High | Key conceptual contribution. |
| Bias/adversarial robustness | High | Roadmap and limitations. |
| Tool augmentation | High | External SE tools and human-in-the-loop. |
| Multi-modal evaluation | Medium / High | Future direction. |
| Code review specificity | Low / Medium | Not focused on review comments. |

## Problematic Judge / Evaluation Types

- Single-gold-label evaluation for subjective SE qualities.
- Correlation-only human alignment without uncertainty/preference modeling.
- Reference-induced or auxiliary-information-induced judge bias.
- Judge with inadequate SE domain expertise.
- Mono-modal judge for multi-modal SE artifacts.
- Tool-free judge used where execution/static/formal evidence is available.
- Judge vulnerable to adversarial code/comment manipulation.

## Context-Quality Evidence

P33 broadens evaluator context from prompt text to the whole evaluation setting: criteria, reference, artifact type, evaluator preferences, uncertainty, tool evidence, multimodal evidence, and project-specific conventions all affect what “good judgment” means.

## Trade-off Extraction

| Strategy | Benefit | Risk / Cost |
|---|---|---|
| LLM-as-a-Judge | Scalable, reference-free, multi-faceted evaluation. | Bias, task dependence, reproducibility, and missing expertise. |
| Expert-annotated benchmarks | Stronger validation ground. | Expensive and hard to scale. |
| Distribution-aware evaluation | Preserves legitimate human disagreement. | More complex metrics and reporting. |
| Tool-augmented judging | Adds objective evidence. | Integration complexity and possible tool-output bias. |
| Human-in-the-loop judging | Handles high-uncertainty cases. | Slower and requires calibration workflow. |
| Multi-modal judging | Fits real SE artifacts better. | Harder benchmark construction and evaluation. |
| Adversarial testing | Improves robustness. | Requires threat models and attack datasets. |

## Relevance to Our Paper

P33 is useful for the related-work and evaluation-validity sections. It lets us frame LLM-as-a-Judge not as a simple replacement for human evaluation but as an evolving measurement system that must handle subjectivity, uncertainty, preferences, and tool-supported evidence.

## Limitations from Our Perspective

- Broad survey/roadmap; not a code-review-comment framework.
- Does not empirically validate the proposed roadmap.
- Some categories are high-level and need operationalization for review-comment evaluation.
- P34 is an earlier shorter vision paper; avoid double-counting its claims as independent evidence.

## Follow-up TODOs

- [ ] Add checked ACM BibTeX.
- [ ] Use P33 for evaluator-validity background.
- [ ] Add rating indeterminacy / evaluator uncertainty / evaluator preferences to framework.
- [ ] Add distribution-aware human alignment as a possible evaluation design.
- [ ] Add tool-augmented and human-in-the-loop judge directions to synthesis.
