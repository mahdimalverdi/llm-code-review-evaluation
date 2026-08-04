# Cross-Paper Synthesis Matrix

> [!NOTE]
> This matrix turns individual paper notes into the backbone of the related-work, gap, taxonomy, and evaluation-framework sections. It is intentionally compact: detailed evidence lives in `papers/Pxx-*.md`.
> Paper IDs are internal traceability handles; publication-facing prose must replace or accompany them with the corresponding citation keys in `references/references.bib`.

## Compact Matrix

| Paper | Evaluation Focus | Main Strength | Missing Piece for Our Work | Best Use in Our Paper |
|---|---|---|---|---|
| P01 — DeepCRCEval | Multi-dimensional review-comment quality | Moves beyond BLEU/ROUGE and introduces domain-specific quality criteria | Does not fully model filtering, useful-comment preservation, or deployment trade-offs | Motivation + evaluation dimensions |
| P02 — HalluJudge | Hallucination / context misalignment | Strong reference-free safeguard/gate framing with claim-to-diff grounding | Mainly hallucination, not all low-value/non-actionable comments | Hallucination taxonomy + context alignment |
| P03 — RovoDev Code Reviewer | Production deployment and workflow impact | Industrial evidence using resolution, PR cycle time, human-comment reduction, and feedback | Limited fine-grained taxonomy and controlled annotation | Industrial validation + workflow-aware evaluation |
| P04 — SWE-PRBench | PR-level benchmark | Shows more context can hurt review performance | Ground truth is realistic but incomplete; cost/workflow effects underdeveloped | Context-quality argument |
| P05 — SWRBench | PR-centric full-project benchmark | Critiques fine-grained benchmarks; manually verified PRs and issue coverage | Full context does not solve context-quality, cost, or filtering trade-offs | Benchmark realism |
| P06 — ContextCRBench | Fine-grained enriched context | Critiques missing semantic context, noisy data, and coarse granularity | Context enrichment is not context-quality scoring | Semantic context + data quality |
| P07 — RevMate | Live user study | Acceptance, perceived value, reviewer overhead, downstream revisions | Does not isolate correctness or wrong-removal effects | Human-centered evaluation |
| P08 — Too Noisy To Learn | Data-quality cleaning | Shows noisy/vague/non-actionable comments harm learning | Dataset cleaning, not deployment filtering | Noisy-comment taxonomy |
| P09 — Hydra-Reviewer | Multi-agent review generation | Mitigates lack of comprehensiveness, incorrectness, and vagueness | Cost/latency and useful-feedback preservation limited | Multi-agent mitigation |
| P10 — BitsAI-CR | Industrial LLM review | RuleChecker, ReviewFilter, Outdated Rate, survey, data flywheel | Private data; precision-first filtering may lose useful comments | Production filters + proxy metrics |
| P11 — LAURA | RAG/context-enriched review | Context augmentation, exemplar retrieval, I/IH/M scoring | Not live; retrieval can distract; filtering may remove useful samples | RAG/context trade-offs |
| P12 — SGCR | Specification-grounded review | Human-authored specs, explicit/implicit paths, trust/explainability | Specification freshness/maintenance under-modeled | Specification grounding |
| P13 — Prompting/Fine-tuning | Prompting, QLoRA, semantic metadata | Call graphs can help; summaries/excessive context can hurt | Small human study; metric-heavy | Resource-aware adaptation |
| P14 — CodeReviewer | Foundational model/dataset | Diff-hunk dataset, baseline model, BLEU critique | Hunk-level/single-comment; no PR workflow | Foundational baseline |
| P15 — LLaMA-Reviewer | PEFT adaptation | LoRA/prefix tuning, input representation, thresholds | BLEU-heavy; no human/workflow validation | PEFT trade-offs |
| P16 — Context-Aware CRA | RAG/expert routing | Context collapse, model-capacity-dependent RAG, severity overestimation | Python/Home Assistant-specific; LLM judge central | Retrieval depth + routing |
| P17 — CodeReviewQA | Comprehension benchmark | CTR/CL/SI probes, contamination-aware curation | Diagnostic MCQA, not workflow | Comprehension-step evaluation |
| P18 — Curated Code Reviews | Data curation | Relevance/clarity/conciseness/civility; LLM-judge calibration | Reformulation may change intent | Reference-quality layer |
| P19 — Fine-Grained Classification | Usefulness-linked taxonomy | 17 review-comment categories linked to usefulness | Classification does not prove correctness/actionability | Taxonomy support |
| P20 — RAG-Reviewer | Retrieval-augmented generation | Pair retrieval, low-frequency-token coverage, semantic equivalence | Java/Tufano-only; BLEU/EM dominant | Exemplar design |
| P21 — iCodeReviewer | Secure review | Category + location + comment; prompt routing; production acceptance | Private data; routing false negatives under-modeled | Secure-review metrics |
| P22 — Static Analyzer + LLM | Hybrid mitigation | DAT/RAG/NCO comparison; calibrated LLM judge | Java/PMD/Checkstyle-specific; no live workflow | Static-analysis context |
| P23 — Reviewer Experience | Reviewer-experience-aware training | Reviewer ownership as data-quality/provenance signal | Experience is a proxy; small manual sample | Reference provenance |
| P24 — Reward Models | RL/reward-guided review | Semantic and downstream code-refinement rewards | Reward model imperfect; no live developer outcome | Downstream usefulness |
| P25 — Carllm | Comprehensible ACR | Detection, localization, explanation, repair suggestion | ChatGPT-annotated artifacts; no live deployment | Structured review output |
| P26 — Human-AI Synergy | Human vs AI-agent review | Large-scale GitHub analysis of adoption, interaction, code-quality impact | Public GitHub proxies; semantic quality incomplete | Human-AI workflow |
| P27 — Industry Claims vs Reality | CRA PR outcome + signal-to-noise | CRA-only lower merge, higher abandonment, low signal ratios | Correlational; keyword/open-coding heuristic | Signal-to-noise + abandonment |
| P28 — Support, Not Automation | Human-centered AI-supported review | Knowledge transfer, team awareness, shared ownership, rationale tracking | Vision paper; no empirical system | Socio-technical dimensions |
| P29 — Can LLMs Replace Human Evaluators? | LLM-as-judge validity in SE | Task dependence; output-based large judges best; pairwise instability | Not code-review-specific; 450 human-scored responses | Judge calibration + order bias |
| P30 — CodeUltraFeedback | Preference dataset | Five coding preferences; SFT/DPO alignment; judge-choice sensitivity | Not review-specific; labels judge-dependent | Preference dimensions |
| P31 — CodeJudgeBench | Coding-task judge benchmark | Thinking judges; position/source/preprocessing sensitivity | Correctness-focused; not review comments | Robustness checks |
| P32 — Bias in the Loop | SE-specific judge bias audit | Prompt perturbations, answer rate, A/B swap, consistency | Code tasks not review comments; pairwise setup | Bias-audit protocol |
| P33 — LLM-as-a-Judge for SE Survey | SE-specific judge survey/roadmap | SE artifact taxonomy, uncertainty, evaluator preferences, tool/human roadmap | Broad survey, not review-comment framework | Evaluator-validity background |
| P34 — From Code to Courtroom | Early SE judge vision | Strict LLM-as-Judge definition; concise roadmap | Earlier/shorter version of P33 | Definition and vision |
| P35 — LLM Critics Help Catch LLM Bugs | Critic-assisted human oversight | CBI, comprehensiveness, hallucinated bugs, nitpicks, FSBS trade-off | Short snippets; LLM-written code, not PR review | Human+critic dimensions |
| P36 — LLMs-as-Judges Survey | General judge taxonomy | Functionality/methodology/metrics/biases/attacks taxonomy | Less SE-specific | Bias vocabulary + meta-eval metrics |
| P37 — Modern Code Review at Google | Industrial human-review baseline | Shows review goals include workflow, maintainability, norms, and developer satisfaction | Not about LLMs or generated comments | Human-review baseline + workflow value |
| P38 — Expectations, Outcomes, and Challenges | Human review outcomes | Shows review is not only defect finding; includes knowledge transfer and alternative solutions | Pre-LLM, human-review focused | Socio-technical review goals |
| P39 — Useful Code Reviews | Developer-centered usefulness | Direct foundation for useful/non-useful feedback and value-to-attention framing | Not automated; Microsoft-specific | Usefulness dimension + low-value comments |
| P40 — Code Change Reviewability | Input-side reviewability | Change size, coherence, description quality, and locality affect review difficulty | Not LLM-specific | Context-quality / reviewability layer |
| P41 — Explaining Explanations | Explanation quality in reviews | Grounds rationale clarity, actionability, and explanation usefulness | Not generated-comment specific | Explanation/rationale quality |
| P42 — ChatGPT Conversations in GitHub PRs/Issues | Developer practice / provenance | Shows AI conversations appear in real PR/issue collaboration | Not code-review quality evaluation | Workflow/provenance background |
| P43 — Survey on LLMs for SE | Broad SE landscape | Places code review in the broader LLM-for-SE task space | Too broad for review-specific claims | Positioning/background |
| P44 — Survey on LLMs for Code Generation | Code-generation survey | Good background for coding benchmark and metric limitations | Not review-specific | Benchmark/metric-validity background |
| P45 — Survey of LLMs for Code | Code-specific LLM survey | Broad view of code LLM evolution, benchmarks, and trends | arXiv/background; not review-specific | Code-LLM context only |
| P46 — LLM for Vulnerability Detection and Repair | Security / repair review | Adds vulnerability category, location, repair correctness, severity, and false-positive/false-negative concerns | Security-specific, not general review | Secure-review sublayer |
| P47 — LLM Misalignment Survey | Trust and misalignment | Broad vocabulary for plausible but misaligned or overconfident outputs | Not SE/review-specific enough | High-level trust framing |
| P48 — LLMs for Code Quality Issues | Static-analysis/code-quality repair | Links LLM feedback to static-analysis warnings and quality issue resolution | Not review-comment specific | Static-analysis/code-quality sublayer |
| P49 — METAMON | Documentation-behavior consistency | Operationalizes inconsistency between documentation and behavior using LLM queries | Documentation-focused, not PR review | Context consistency / stale-context checks |
| P50 — COFFE | Efficiency benchmark | Adds non-functional quality and benchmark/proxy-validity evidence | Code-generation benchmark, not review comments | Efficiency/proxy-validity background |
| P51 — Modern Code Review SLR | Human-review taxonomy and evidence map | Provides vocabulary and empirical review dimensions | Predates the LLM-specific trade-off problem | Review goals and taxonomy boundary |
| P52 — Automating Code Review Activities | Automation task decomposition | Clarifies which review activities can be automated | Does not provide a unified LLM evaluation protocol | Automation-boundary framing |
| P53 — Code Review Automation | Strengths, weaknesses, and automation limits | Directly identifies benefits and failure risks | Limited trade-off measurement | Motivation and gap framing |
| P54 — CR-Bench | Real-world utility of review agents | PR-level utility and realistic task setting | Full deployment cost and preservation measures remain limited | Benchmark realism and utility |
| P55 — Automated Review in Practice | Industry deployment | Observes operational review behavior | Confounding and proprietary context | Production evidence |
| P56 — Human and Machine | Human perception of AI-assisted reviews | Compares engagement with human and AI feedback | Limited objective correctness evidence | Human-centered evaluation |
| P57 — Review Relevance | Relevance of generated comments | Direct relevance labels and agreement evidence | Relevance does not cover correctness or grounding | Relevance dimension |
| P58 — Overcorrection | Reliability and requirement-conformance errors | Exposes systematic overcorrection | Narrow task and benchmark boundary | False-positive and calibration risks |
| P59 — Comment Classification | Automated taxonomy classification | Supports scalable labeling of human comments | Classification is not comment-quality validation | Annotation pipeline |
| P60 — Feedback Usefulness | Developer usefulness labels | Directly grounds usefulness in review practice | Cross-context transfer and preservation remain open | Usefulness and value-to-attention |
| P61 — AI Review and Learning | Learning and self-regulated review | Shows socio-technical and educational outcomes | Experience-report evidence is limited | Workflow value |
| P62 — DeputyDev | Contextual assistant productivity | Links contextual assistance to developer outcomes | A/B confounding and limited failure taxonomy | Industrial workflow evidence |
| P63 — Confirmation Bias | Security-review evaluator bias | Measures confirmation effects in LLM-assisted security review | Security-specific and not general comment quality | Evaluator/context bias |
| P64 — Adversarial Comments | Comment-based attacks on security reviewers | Tests adversarial review context and defenses | Security boundary and specialized threat model | Adversarial robustness |
| P65 — QASecClaw | Multi-agent false-positive reduction | Demonstrates staged verification for SAST findings | Not ordinary review-comment generation | Verification and routing mitigation |
| P66 — Benchmark Survey | Benchmark and evaluation-practice survey | Consolidates pre-LLM and LLM benchmark limitations | Survey evidence is not a new empirical benchmark | Benchmark validity |
| P67 — Familiar-Pattern Attack | Bias in static-analysis judgments | Shows pattern familiarity can hijack LLM analysis | Security/static-analysis specific | Context manipulation threat |
| P68 — CoTDeceptor | Adversarial reasoning/code-agent robustness | Tests obfuscation against reasoning-enhanced agents | Not a review-comment evaluation study | Adversarial evaluator risk |
| P69 — Deep Assessment | Semantic and expert assessment of review generation | Moves beyond lexical similarity with graded review quality | Annotation and workflow costs need explicit reporting | Evaluation dimensions and metric validity |
| P70 — ChatGPT Code Refinement | Downstream refinement utility | Connects generated feedback to code changes | Review-comment connection is indirect | Supporting downstream-use evidence |
| P71 — Llama Code Refinement | Replicated refinement evaluation | Adds replication and manual assessment evidence | Indirect review setting and limited trade-off analysis | Supporting replication evidence |

## Cross-Paper Patterns

### 1. Text similarity is insufficient, but still persistent

P14 already recognized that BLEU is weak for review comments because valid comments are diverse and non-unique. Later work adds richer dimensions: grounding (P02), usefulness and relevance (P01/P18/P23/P24/P25/P39/P57/P60), security category/location (P21/P46), downstream refinability (P24/P48/P70/P71), suggestion adoption and code impact (P26), signal-to-noise and abandonment (P27), explanation quality (P41), and coding preferences (P30/P44/P45). P29/P31/P32/P33/P36/P63/P69 show that replacing lexical metrics with an LLM judge or a single semantic score is insufficient unless the measurement instrument and rubric are validated.

**Implication:** Our framework should not be another single metric. It should be a structured evaluation protocol with separate content, grounding, usefulness, explanation, workflow, and evaluator-validity dimensions.

### 2. Context quality is broader than code context

The literature moves from diff hunks (P14/P15) to PR/repository context (P04/P05/P06/P54/P62), retrieved exemplars (P11/P20), specifications (P12), semantic metadata (P13), static-analysis output (P22/P48/P65/P67), reviewer provenance (P23), structured reasoning chains (P25), socio-technical workflow context (P26/P28/P37/P38/P42/P55/P56/P61), input reviewability (P40), documentation-behavior consistency (P49), and evaluator or adversarial context (P29/P31/P32/P33/P36/P63/P64/P68).

**Implication:** Context quality should include code, retrieval, static-analysis, specification, reviewer/provenance, change reviewability, documentation freshness, behavioral consistency, socio-technical workflow, and evaluator-prompt context.

### 3. Data, reference, and provenance quality are first-class concerns

P08/P18 show that human review comments can be noisy. P17 shows strict curation improves reliability but reduces coverage. P22/P48/P65 show that synthetic or static-analysis signals can help but may contradict, be misinterpreted, or require staged verification. P23 shows reviewer experience affects reference quality. P25 restructures sparse comments into issue-location-explanation-repair chains. P30 shows preference data scales with LLM judges but becomes judge-dependent. P31/P32/P54/P66 show that benchmark construction and evaluation choices can expose or conceal failures. P35 shows known reference bugs improve agreement. P42 adds that shared AI conversations have provenance and verification issues. P57/P59/P60 further distinguish relevance, scalable category labels, and developer-perceived usefulness from correctness.

**Implication:** Evaluation should record who/what produced the reference, how complete it is, whether it targets a known issue, whether multiple valid comments exist, and whether AI-generated context has been verified.

### 4. Taxonomy must cover comment failures, workflow failures, and evaluator failures

The taxonomy should include hallucination, irrelevance, vagueness, non-actionability, wrong location, wrong category, severity miscalibration, redundancy, uncivil/unclear comments, missing explanation, missing repair suggestion, low-signal CRA feedback, complexity-increasing suggestions, low-value nitpicks, poor value-to-time comments, unverified shared AI advice, security false alarms, invalid repair suggestions, static-analysis warning misinterpretation, stale-documentation-based comments, unsupported efficiency claims, and evaluator failures such as position bias, verbosity bias, prompt sensitivity, invalid answer format, source-model sensitivity, preprocessing sensitivity, authority/sentiment/distraction/refinement/self-enhancement bias, and adversarial judge attacks.

**Implication:** The final taxonomy should explicitly separate **generated-review failures**, **input/context failures**, **workflow failures**, and **evaluation-instrument failures**.

### 5. Mitigation strategies are trade-off choices, not free improvements

Mitigations include filtering (P10), data cleaning (P08/P18), RAG (P11/P16/P20), specification grounding (P12), PEFT/fine-tuning (P13/P15), multi-agent generation and verification (P09/P65), prompt routing (P21), static-analysis hybrids (P22/P48), reviewer-experience weighting (P23), reward optimization (P24), CoT curation (P25), human oversight (P26/P28/P35/P56), signal-to-noise monitoring (P27), thinking judges (P31), bias auditing (P32/P63), tool/human-augmented judges (P33/P34/P36), reviewability-aware gating (P40), context-consistency checks (P49), adversarial defenses (P64/P67/P68), and specialized security/performance evaluation (P46/P50).

**Implication:** Every mitigation should report what it reduces, what useful feedback it may suppress, what it costs, and what new failure modes it introduces.

### 6. Useful-feedback preservation is still under-measured

Most works measure improved scores or reduced bad comments, but few measure lost useful comments. Precision-first filters may suppress rare but valuable issues (P10/P21/P65). Cleaning/reformulation may change intent (P18/P25). Reward models may optimize model-easy usefulness (P24). AI suggestions may be adopted but increase complexity (P26), while relevance and usefulness labels still capture only part of quality (P57/P60). CRA-only review may be present but low-signal (P27). Automation may save time but remove socio-technical or learning benefits (P28/P37/P38/P56/P61). Strict reviewability, consistency, or adversarial gates (P40/P49/P64/P67/P68) may prevent bad output but also skip useful automation opportunities.

**Implication:** Harmful-comment reduction and useful-feedback preservation must be measured separately.

### 7. LLM-as-a-Judge must be evaluated as a measurement instrument

P29 shows strong task dependence and pairwise instability. P30 shows judge choice affects rankings. P31 shows sensitivity to response order, source model, prompt format, and preprocessing. P32 adds answer rate, repeated-run consistency, prompt-perturbation bias audits, and token-confidence shifts. P33 adds evaluator uncertainty and preferences. P36 provides general bias/adversarial taxonomy and meta-evaluation metrics.

**Implication:** LLM-as-a-Judge is not ground truth. Any judge-based result should include a judge-validation protocol.

### 8. Critic-assisted oversight is different from judge-only scoring

P35 shifts the design point from scalar judging to natural-language critique. It evaluates critiques by comprehensiveness, Critique-Bug Inclusion (CBI), hallucinated bugs, nitpicks, conciseness, and helpfulness. Human+critic teams can improve comprehensiveness while reducing hallucinations compared with model-only critics.

**Implication:** Review-comment evaluation can borrow critic-evaluation dimensions: known-issue inclusion, severe-issue coverage, false-problem rate, nitpick rate, and human-edit/remove behavior.

### 9. Code review is a socio-technical workflow, not only a defect detector

P37/P38/P39/P51 establish that human review provides maintainability, learning, awareness, shared ownership, and useful feedback beyond defect finding. P52/P53 clarify that automation targets different review activities and carries activity-specific limitations. P26/P56 show differences between human and AI feedback or engagement, while P55/P62 add deployment evidence with context-specific confounding. P27 shows CRA-only review has worse merge/abandonment outcomes than human-only review. P28 argues AI should support review rather than automate it because review also provides knowledge transfer, team awareness, shared ownership, rationale tracking, and accountability. P42 shows LLM output is already becoming part of PR/issue communication, and P61 adds learning and self-regulation outcomes.

**Implication:** The framework should include reviewer attention, interaction rounds, human final judgment, signal-to-noise, adoption, abandonment, code-quality deltas, knowledge transfer, team awareness, shared ownership, provenance, and accountability.

### 10. Specialized sublayers are needed for security, static analysis, and non-functional quality

P46 shows security review has distinct dimensions: vulnerability type, location, exploitability, severity, repair correctness, false alarms, and missed vulnerabilities. P63/P64/P67/P68 add confirmation bias and adversarial-context risks, and P65 adds staged false-positive verification. P48 shows static-analysis/code-quality feedback has issue-resolution and behavior-preservation concerns. P50 shows efficiency needs measurable workload and benchmark evidence. These should not be collapsed into generic “comment quality.”

**Implication:** A general framework should allow optional secure-review, static-analysis/code-quality, and non-functional-quality sublayers.

## Evaluator-Validity Checklist

Any LLM-as-a-Judge used in our framework should report at least:

| Check | Why |
|---|---|
| Task-specific rubric | Generic “quality” is unstable across SE tasks. |
| Answer rate / parseability | Invalid or missing structured judgments are measurement failures. |
| A/B order swap | Detects position and recency bias. |
| Repeated-run consistency | Detects stochastic instability. |
| Prompt-perturbation suite | Detects authority, sentiment, verbosity, refinement, distraction, and CoT biases. |
| Judge-choice sensitivity | Different judges can produce different rankings. |
| Source-model sensitivity | Judges may react to style/model artifacts, not correctness. |
| Preprocessing sensitivity | Raw response, code-only, and no-comment variants can change results. |
| Human uncertainty/preferences | Human disagreement should be modeled, not hidden. |
| Adversarial robustness | Prompt injection or adversarial phrases can manipulate judges. |
| Tool/evidence integration | Execution, static analysis, tests, or benchmarks may be needed for SE artifacts. |
| Cost/latency | Thinking/multi-judge protocols may be more accurate but expensive. |

## Emerging Gap Statement

Across the 71-paper corpus, LLM-based code review evaluation is moving from lexical similarity toward richer rubrics, PR-level utility benchmarks, context enrichment, production telemetry, data curation, RAG, specification grounding, static-analysis hybrids, reviewer provenance, reward-guided generation, structured comprehensibility, human-AI workflow and learning outcomes, signal-to-noise measures, judge robustness, adversarial-context testing, foundational human-review theory, reviewability, explanation quality, secure-review evaluation, code-quality repair, context consistency, and non-functional benchmark validity.

Within the reviewed corpus, we did not identify a single framework that jointly operationalizes all of the following elements. This is a corpus-bounded finding rather than a claim that no such work exists outside the search and screening scope:

- generated-comment quality: grounding, correctness, category, location, severity, explanation, repair suggestion, clarity, civility, and actionability,
- input/context quality: diff, PR, repository, retrieval, specification, static-analysis, semantic metadata, reviewer provenance, reviewability, documentation freshness, behavioral consistency, and socio-technical workflow context,
- reference/provenance quality: completeness, source, reviewer expertise, known-issue anchoring, multiple-valid-comment cases, annotation reliability, and AI-output verification,
- workflow value: acceptance, adoption, abandonment, signal-to-noise, reviewer effort, knowledge transfer, team awareness, shared ownership, provenance, and accountability,
- useful-feedback preservation under filtering, cleaning, routing, retrieval, reward optimization, static-analysis hybridization, judge-based suppression, reviewability gates, and consistency checks,
- evaluator validity: task dependence, answer rate, order bias, prompt sensitivity, judge-choice sensitivity, source-model sensitivity, preprocessing sensitivity, human uncertainty, and adversarial robustness,
- proxy-validity limits of BLEU, ROUGE, BERTScore, EM, CodeBLEU, LLM-judge scores, Outdated Rate, acceptance, adoption, signal-to-noise, abandonment, static-analysis warning resolution, code metric deltas, and benchmark efficiency scores,
- cost: token budget, latency, training cost, API cost, judge cost, routing cost, reward-model cost, expert-maintenance cost, reviewer overhead, context-consistency checking cost, and human-AI interaction cost.

## Working Contribution Direction

A strong contribution is a **taxonomy and trade-off-aware evaluation framework** for LLM-generated code review comments. The framework should jointly cover context quality, reviewability, reference provenance, structured review outputs, downstream usefulness, socio-technical review value, evaluator validity, problematic-comment types, useful-feedback preservation, proxy-validity analysis, specialized security/static-analysis/non-functional sublayers, and the consequences of filtering, cleaning, prompting, fine-tuning, retrieving, routing, rewarding, judging, verifying, aggregating, suppressing, blocking, or expanding generated comments.

## Paper-to-Argument Mapping

| Argument Need | Best Supporting Papers | Notes |
|---|---|---|
| Text similarity is insufficient | P14, P01, P11, P13, P16, P17, P18, P20, P21, P22, P23, P24, P25, P26, P29, P30, P31, P41, P44, P45, P54, P57, P60, P66, P69 | LLM judges and semantic scores do not automatically solve metric validity. |
| Context quality matters | P04, P05, P06, P10, P11, P12, P13, P16, P20, P21, P22, P23, P25, P26, P28, P29, P31, P32, P40, P42, P49, P54, P55, P62, P63, P64, P67, P68 | Includes evaluator, adversarial, workflow, reviewability, and documentation context. |
| Data/reference/provenance quality matters | P08, P14, P17, P18, P20, P22, P23, P25, P30, P31, P35, P42, P54, P57, P59, P60, P66 | Relevance, categories, usefulness, and benchmark construction are distinct evidence layers. |
| Taxonomy/usefulness categories matter | P01, P02, P08, P10, P18, P19, P21, P23, P25, P26, P27, P28, P30, P35, P39, P41, P51, P57, P59, P60 | Include comment, explanation, workflow, relevance, and developer-usefulness categories. |
| Hybrid mitigation needs trade-off analysis | P09, P10, P11, P12, P16, P20, P21, P22, P24, P25, P35, P40, P46, P48, P49, P58, P64, P65, P67, P68 | Include verification, adversarial defense, and overcorrection risks. |
| Downstream usefulness matters | P07, P10, P20, P24, P25, P26, P27, P35, P39, P48, P54, P55, P56, P60, P61, P62, P70, P71 | Separate developer outcomes from indirect code-refinement evidence. |
| Structured output matters | P17, P21, P25, P30, P35, P41, P46 | Issue, location, explanation, repair, known-bug inclusion, vulnerability type. |
| LLM-as-a-Judge needs calibration/robustness | P16, P18, P22, P24, P29, P30, P31, P32, P33, P34, P36 | Strongest evidence now P29–P36. |
| Bias/adversarial threat model matters | P31, P32, P33, P36, P47, P58, P63, P64, P67, P68 | Distinguish evaluator bias, model overcorrection, and adversarial context. |
| Human-AI workflow matters | P03, P07, P10, P12, P21, P26, P27, P28, P35, P37, P38, P42, P51, P52, P53, P55, P56, P61, P62 | Includes automation boundaries, learning, perception, and deployment outcomes. |
| Useful-feedback preservation is missing | P10, P11, P12, P18, P20, P21, P22, P23, P24, P25, P26, P27, P28, P32, P39, P40, P49, P57, P58, P60, P64, P65 | Include lost feedback under filters, verification, and defensive gates. |
| Specialized security/code-quality/performance layers matter | P21, P22, P46, P48, P50, P63, P64, P65, P67, P68 | Keep specialized threats and verification separate from general comment quality. |

## Tensions Worth Highlighting

### Context tension

- **P04:** More context can degrade performance.
- **P11/P20:** Retrieved exemplars help when relevant.
- **P13:** Call graphs can help; summaries can hurt.
- **P16:** Smaller models can collapse under retrieval context.
- **P22/P48:** Static-analysis context helps only when integrated carefully.
- **P28/P37/P38/P42:** Review context includes people, rationale, process, learning goals, and provenance.
- **P29/P31/P32/P33:** Evaluator context itself changes judgments.
- **P40/P49:** Context must be reviewable and internally consistent.
- **P54/P62:** Rich PR/repository context improves realism but increases cost and confounding.
- **P63/P64/P67/P68:** Context can also bias or adversarially manipulate reviewers and evaluators.

### Usefulness tension

- **P07:** Non-accepted comments may still be valuable.
- **P10:** Correct comments may be practically superfluous.
- **P24:** Model-refinement usefulness may not equal human usefulness.
- **P26:** Adopted AI suggestions may increase complexity.
- **P27:** CRA comments may be low-signal and associated with abandonment.
- **P28/P37/P38:** Automation may remove knowledge transfer and shared ownership.
- **P35:** More comprehensive critiques can include more hallucinations/nitpicks.
- **P39:** Useful feedback is developer-centered and cannot be reduced to correctness.
- **P57/P60:** Relevance and perceived usefulness are necessary but do not establish correctness or grounding.
- **P58/P65:** Aggressive correction or verification can reduce false positives while creating omission risks.

### Ground truth and evaluator-validity tension

- **P14:** Earliest-comment references are incomplete.
- **P23:** Human reference quality depends on reviewer experience.
- **P24:** Rewards define usefulness through proxies.
- **P29:** LLM-as-Judge is task-dependent.
- **P30:** Judge choice changes rankings.
- **P31:** Judge accuracy changes with order/source/preprocessing.
- **P32:** High consistency can mean consistently biased.
- **P33/P36:** Human uncertainty, preferences, biases, and adversarial attacks must be modeled.
- **P35:** Known reference bugs improve critique evaluation, but inserted bugs may differ from natural bugs.
- **P50:** Benchmark efficiency may not equal workflow value.
- **P54/P66/P69:** Realistic benchmarks and richer semantic assessment improve validity but raise annotation, coverage, and cost questions.

## Supplementary Core Evidence Added at the 121-Study Freeze

The 50 unique supplementary core studies were admitted after duplicate and
companion resolution. The following synthesis records only changes or material
reinforcement to the baseline claims; it is not a paper-by-paper summary.

### Data and reference validity

- **P72/P75:** Training-pair selection and comment curation affect both target quality and the distribution of intents available to the model.
- **P97/P102:** Review-comment type and change-description hallucination show that reference construction must distinguish task intent from surface similarity.
- **P101/P112:** Verifier failure and nondeterministic judgment can create evaluation error even when the generated artifact is unchanged.

### Agent and workflow validity

- **P74/P76/P85/P91:** Repository-scale and agentic review distribute evidence gathering, issue detection, and response generation across trajectories; comment-level scoring alone is incomplete.
- **P77/P100/P110:** Offline quality does not establish workflow value. Timing, granularity, addressing behavior, and developer control affect whether feedback is used.
- **P86/P89:** Human and automated reviewers emphasize different themes and improvement types, limiting direct substitution claims.

### Context selection and retrieval

- **P79/P85:** Issue lists and repository-local context can improve grounding when context is selected for the review task.
- **P93:** Additional retrieval can reduce performance when retrieved evidence is noisy or mismatched.
- **P94/P96:** Issue-oriented decomposition and resource-aware serving make context and cost part of the intervention, not merely implementation detail.

### Safety, communication, and social validity

- **P78:** Review content can be a social-engineering attack surface, extending problematic feedback beyond technical incorrectness.
- **P82/P84:** Toxicity and identity-cue sensitivity require communication-safety and bias checks in addition to factual evaluation.
- **P90/P95:** Secure agentic review adds tool grounding and verification but inherits tool coverage and orchestration risks.

### Evaluation and mitigation trade-offs

- **P73:** Explanations may increase trust without guaranteeing correctness, so trust and calibrated reliance must be separated.
- **P83:** Larger models can increase cost without a corresponding improvement across all review dimensions.
- **P88/P98:** Holistic and multidimensional scoring improves construct coverage but increases rubric and evaluator complexity.
- **P107:** Tool-verifiable reward signals improve grounding for detectable issue classes while narrowing evaluation to selected tools.
- **P108/P116:** These IDs are retained as duplicate provenance records and are excluded from the 121-study denominator.

### Implication for the framework

The expanded evidence supports a shift from a single-comment quality model to a
decision-oriented evaluation pipeline. The unit of analysis may be a comment,
issue set, review trajectory, or workflow outcome. Each result should therefore
identify its unit, evidence source, evaluator, mitigation action, preservation
effect, coverage effect, escalation behavior, and cost. Claims should not be
transferred across these units without an explicit argument.

## Update Rule

Update this matrix after every 3–5 completed paper notes. New papers should be added only if they change at least one synthesis claim, taxonomy category, evaluation dimension, or gap statement.
