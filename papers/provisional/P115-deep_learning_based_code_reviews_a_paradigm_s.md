# P115 — Deep Learning-based Code Reviews: A Paradigm Shift or a Double-Edged Sword?

## 1. Identification

| Field | Value |
|---|---|
| Project ID | `P115` |
| Citation key | `p115_tufano2024_deep_learning_based_code_revie` |
| Authors | Rosalia Tufano; Alberto Martin-Lopez; Ahmad Tayeb; Ozren Dabić; Sonia Haiduc; Gabriele Bavota |
| Year | 2024 |
| Source | arXiv preprint, `2411.11401v3` |
| Study type | Controlled human experiment with automated-review assistance |

## 2. Screening

- **Scope decision:** Include as core evidence for reviewer behavior, anchoring, review quality, cost, and confidence.
- **Task:** Professional developers review Java/Python programs under manual, realistic automated-review, and ideal comprehensive-review treatments.
- **Evidence boundary:** The study evaluates final human reviews and behavior, not production pull requests or long-term adoption.
- **Metadata caveat:** Publisher/duplicate status and the provisional BibTeX record require verification.

## 3. Study overview

Twenty-nine professional developers completed 72 reviews across six projects in Java or Python. The study injected 48 quality issues, covering evolvability and functional defects. In manual code review (MCR), participants received no automated starting point. Automated code review (ACR) provided a ChatGPT Plus-generated review. Comprehensive code review (CCR) provided an idealized review covering all injected issues, allowing the authors to study behavior under near-perfect automation. Review outputs, IDE activity, time, issue severity, and self-rated confidence were collected.

## 4. Evidence mapped to review questions

| RQ | Evidence and interpretation | Evidence type | Location |
|---|---|---|---|
| RQ1 | Automated support changes review output and location focus; reviewers retain about 89% of LLM-identified issues. | Reported | Abstract; RQ0 |
| RQ2 | ACR/CCR do not increase detection of high-severity injected issues, although ACR increases low-severity issue findings. | Reported | RQ1 |
| RQ3 | Reviewers anchor on locations identified by automation and may miss issues elsewhere; the effect persists with idealized CCR. | Reported | Abstract; RQ1 |
| RQ4 | Automated review is presented as a starting-point set of comments; CCR supplies all injected issues, while MCR supplies no additional context. | Experimental condition | Study design |
| RQ5 | Human verification and maintaining manual inspection are necessary; concise, accurate automation is suggested to avoid review overhead. | Inferred/proposed | Discussion |
| RQ6 | 29 professionals, 72 reviews, issue injection, manual inspection, IDE telemetry, regression models, and confidence ratings support evaluation. | Reported | Sections II–III |

## 5. Failure and problematic-comment categories

| Category | Definition/example | Evidence type | Location |
|---|---|---|---|
| Anchoring | Reviewer focuses on code locations highlighted by the automated review. | Measured behavioral effect | Abstract; RQ0/RQ1 |
| Missed high-severity issue | Automation does not increase detection of injected serious issues over manual review. | Measured | RQ1 |
| Low-severity noise | ACR leads reviewers to identify more low-severity issues. | Measured | RQ1 |
| False-positive verification burden | Reviewers must inspect and validate generated comments before accepting them. | Reported | RQ2/discussion |
| Coverage blind spot | Attention to supplied locations can reduce search for issues elsewhere. | Reported/inferred | Abstract |

## 6. Evaluation dimensions and metrics

| Dimension | Operationalization/metric | Result or limitation | Location |
|---|---|---|---|
| Review quality | Identification of 48 injected issues plus additional manually found issues | Automated support does not improve high-severity detection; ACR increases low-severity findings. | RQ1 |
| Comment adoption | Proportion of generated issues retained in final review | Reviewers retain approximately 89% of LLM-identified issues. | Abstract |
| Review output | Number of issues, review length, and distinct covered lines | ACR/CCR produce more/longer and differently located reviews than MCR. | RQ0 |
| Review cost | Total, inspection, and writing time from IDE telemetry | No significant time saving; interpretation/verification offsets automation. | RQ2 |
| Reviewer confidence | Self-rating from 1 to 5 | MCR average 3.6, ACR 3.7, CCR 3.8; no significant treatment effect. | RQ3 |
| Behavioral focus | Files, tabs, edits, and commented locations recorded by Tako | Supports analysis of anchoring and workflow behavior. | Section II-C |

## 7. Mitigation and trade-offs

- **Mitigation family:** Treat automated reviews as assistive starting points, preserve human inspection, and optimize comment concision and correctness.
- **Intervention point:** Review workflow and presentation of generated comments.
- **What it reduces:** Writing effort and orientation burden in principle, although measured time savings did not materialize.
- **Useful feedback potentially lost:** Anchoring on automated locations can suppress independent discovery of issues not highlighted by the model.
- **Coverage:** Ideal CCR demonstrates that even complete issue coverage does not guarantee faster review; human interpretation remains necessary.
- **Human escalation:** Human reviewers retain responsibility for validating comments and searching beyond supplied locations.
- **Cost:** Verification and interpretation of generated feedback can offset generation-time savings.
- **New failure modes:** Automation bias, anchoring, low-severity noise, false-positive checking, and misplaced confidence.

## 8. Annotation and evaluator validity

- **Participants:** 29 developers with a mean of 11.4 years of programming experience; most had both reviewer and contributor experience.
- **Ground truth:** Authors manually inject and inspect quality issues across six programs and two languages.
- **Design:** Within-participant treatment assignment, rotated treatments, IDE telemetry, and final-review inspection support causal comparison.
- **Human evaluation:** Two authors manually inspect all 72 reviews and classify issue severity/type.
- **Limitations:** Convenience sample, small programs, injected issues covering 73% of a prior taxonomy, ChatGPT-generated/rephrased comments, and excluded/uncertain time records.

## 9. Quality appraisal

| Criterion | Score (0–2) | Evidence note |
|---|---:|---|
| Q1 | 2 | Four research questions and outcomes are explicit. |
| Q2 | 2 | Professional participants, languages, programs, and injected issues are detailed. |
| Q3 | 2 | Treatments, prompts, IDE, telemetry, and procedure are specified. |
| Q4 | 2 | Quality, time, behavior, and confidence outcomes are measured. |
| Q5 | 2 | Injected issues and manual inspection provide a concrete validity basis. |
| Q6 | 1 | Double inspection is described, but formal agreement is limited. |
| Q7 | 2 | MCR, realistic ACR, and idealized CCR conditions are compared. |
| Q8 | 1 | Professional participants and real tools, but small synthetic programs. |
| Q9 | 2 | Workflow support and idealized coverage are directly manipulated. |
| Q10 | 2 | IDE telemetry measures review time and activity. |
| Q11 | 2 | Severity, anchoring, adoption, cost, and confidence trade-offs are analyzed. |
| Q12 | 2 | Direct human review outcomes align closely with the framework. |

**Total: 22/24 — high confidence for reviewer-behavior and workflow-impact evidence.**

## 10. Review-process reliability and bias

- **Construct bias:** Injected issues approximate review problems but cannot represent the full complexity of production changes.
- **Treatment realism:** CCR is deliberately idealized and estimates possible future automation rather than current capability.
- **Anchoring confound:** ACR/CCR differ from MCR in supplied locations and review content, so presentation effects are part of the intervention.
- **Sample bias:** Convenience recruitment and language expertise assignment limit generalization.
- **Measurement risk:** Thirteen of 72 time records were excluded as measurement errors; interruptions may affect timing.
- **Missing outcomes:** No longitudinal adoption, accepted fixes, knowledge transfer, or production-quality effect is measured.

## 11. Synthesis-ready conclusion

- P115 provides unusually strong evidence that automated review assistance changes human reviewer behavior, especially through anchoring on suggested locations.
- Starting from an automated review does not improve detection of high-severity issues and does not save time, even when the supplied review is idealized.
- Reviewers largely accept generated findings, but verification remains necessary and automation can increase low-severity noise.
- Evaluation of LLM review systems should measure human outcomes, search coverage, review time, and confidence—not only model-level comment accuracy.
- Use as core evidence for human-AI trade-offs, automation bias, and the risk that useful feedback can be lost outside model-highlighted locations.

