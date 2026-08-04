#!/usr/bin/env python3
"""Build a conservative study-level SLR dataset from canonical Markdown notes."""

from __future__ import annotations

import csv
import re
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"
CANONICAL_NOTES = PAPERS / "canonical" / "notes"
BIB = ROOT / "references" / "references.bib"
PROGRESS = PAPERS / "slr-review-progress.md"
OUT_DIR = ROOT / "data"

CORE = {
    *range(1, 23), *range(24, 27), 35, 40, 49, *range(53, 56),
    *range(57, 61), *range(62, 67), 69,
}
SUPPORTING = {
    23, *range(27, 35), *range(36, 40), *range(41, 44), 46, 48,
    51, 52, 56, 61, 67, 68,
}
PERIPHERAL = {44, 45, 47, 50, 70, 71}

# Supplementary records are promoted to canonical only after the freeze step.
# Their provisional IDs are therefore discovered from the canonical note
# directory instead of being hard-coded into the baseline tier sets.
CANONICAL_PROJECT_NUMBERS = {
    int(path.name.split("-", 1)[0][1:])
    for path in CANONICAL_NOTES.glob("P[0-9]*-*.md")
}

FAILURES = {
    "unsupported_or_hallucinated": (r"hallucin", r"unsupported claim", r"ungrounded", r"context.misalign"),
    "incorrect_claim": (r"incorrect", r"factually false", r"technically wrong"),
    "irrelevant": (r"irrelev", r"off.topic", r"out.of.scope"),
    "wrong_location_or_cause": (r"wrong.location", r"wrong cause", r"mislocal", r"localization failure"),
    "vague_or_generic": (r"vague", r"generic comment", r"low specificity"),
    "non_actionable": (r"non.actionable", r"not actionable", r"low actionability"),
    "low_value_or_nitpick": (r"low.value", r"nitpick", r"poor value.to"),
    "redundant": (r"redundan", r"duplicate comment"),
    "invalid_fix": (r"invalid (?:fix|repair)", r"wrong fix", r"unsafe fix", r"regression"),
    "severity_miscalibration": (r"severity", r"overestimat", r"overcorrection"),
    "context_dependent": (r"context.dependent", r"insufficient.context", r"missing context"),
    "spurious_or_false_positive": (r"spurious", r"false.positive", r"false alarm"),
    "missed_issue_or_false_negative": (r"missed issue", r"false.negative", r"issue miss", r"coverage gap"),
    "adversarial_or_bias": (r"adversarial", r"confirmation bias", r"hijack", r"decept"),
}

DIMENSIONS = {
    "correctness": (r"correctness", r"factuality", r"technically correct"),
    "grounding": (r"grounding", r"groundedness", r"context alignment"),
    "relevance": (r"relevance", r"relevant to"),
    "usefulness": (r"usefulness", r"useful feedback", r"perceived value"),
    "actionability": (r"actionability", r"actionable"),
    "specificity": (r"specificity", r"specific enough"),
    "explanation_quality": (r"explanation", r"rationale"),
    "context_quality": (r"context quality", r"contextual adequacy", r"reviewability"),
    "coverage": (r"issue coverage", r"review coverage", r"recall"),
    "acceptance_or_adoption": (r"acceptance", r"adoption", r"code resolution"),
    "workflow_impact": (r"workflow", r"cycle time", r"reviewer overhead", r"abandonment"),
    "cost_or_latency": (r"cost", r"latency", r"token", r"model.call", r"time per"),
    "evaluator_validity": (r"evaluator validity", r"llm.as.a.judge", r"judge bias", r"agreement", r"position bias"),
    "security_validity": (r"vulnerab", r"exploitability", r"security"),
    "repair_validity": (r"repair correctness", r"behavior preservation", r"invalid repair"),
    "efficiency_validity": (r"efficiency", r"performance claim", r"workload"),
    "lexical_similarity": (r"bleu", r"rouge", r"exact match", r"lexical similarity"),
}

MITIGATIONS = {
    "data_cleaning": (r"data clean", r"curation", r"reformulat"),
    "prompting": (r"prompting", r"prompt design", r"few.shot"),
    "fine_tuning": (r"fine.tun", r"qlora", r"lora", r"peft"),
    "retrieval_or_rag": (r"\brag\b", r"retrieval", r"retrieved exemplar"),
    "context_gate": (r"context gate", r"reviewability gate", r"pre.generation gate"),
    "specification_grounding": (r"specification ground", r"specification", r"rule trace"),
    "static_analysis_hybrid": (r"static analy", r"sast", r"tool.output"),
    "routing": (r"routing", r"router", r"mixture.of.prompt"),
    "multi_agent": (r"multi.agent", r"multiple agent", r"agent aggregation"),
    "verification_or_critic": (r"verif", r"critic", r"grounding check", r"factuality gate"),
    "filtering_or_suppression": (r"filter", r"suppress", r"quality gate"),
    "rewriting": (r"rewrit", r"reformulat"),
    "human_escalation": (r"human escalation", r"escalat", r"human.in.the.loop"),
    "reward_optimization": (r"reward model", r"reward optimization", r"\bdpo\b"),
    "benchmark_or_rubric": (r"benchmark", r"rubric", r"evaluation framework"),
    "adversarial_defense": (r"adversarial defense", r"attack defense", r"robustness defense"),
}

CONTEXTS = {
    "diff_or_hunk": (r"\bdiff\b", r"hunk", r"changed line"),
    "file_or_function": (r"file.level", r"function.level", r"surrounding code"),
    "pr_or_issue": (r"pull request", r"\bpr\b", r"issue description", r"commit message"),
    "repository_or_project": (r"repository", r"project context", r"full project"),
    "retrieved_history": (r"retriev", r"review history", r"exemplar"),
    "specification_or_documentation": (r"specification", r"documentation", r"requirement"),
    "static_analysis_or_tool": (r"static analy", r"sast", r"tool output"),
    "reviewer_or_workflow": (r"reviewer", r"workflow", r"developer"),
    "execution_or_test": (r"execution", r"test result", r"runtime", r"benchmark evidence"),
    "adversarial_context": (r"adversarial", r"confirmation bias", r"obfuscat", r"hijack"),
}


def bib_entries() -> dict[str, dict[str, str]]:
    text = BIB.read_text(encoding="utf-8")
    entries: dict[str, dict[str, str]] = {}
    for match in re.finditer(r"@(\w+)\{([^,]+),(.*?)(?=\n@|\Z)", text, re.S):
        kind, key, body = match.groups()
        fields = {"entry_type": kind.lower()}
        for line in body.splitlines():
            fm = re.match(r"^\s*(\w+)\s*=\s*(.*?)\s*,?\s*$", line)
            if not fm:
                continue
            value = fm.group(2).strip().rstrip(",").strip()
            if len(value) >= 2 and ((value[0], value[-1]) in (("{", "}"), ('"', '"'))):
                value = value[1:-1]
            fields[fm.group(1).lower()] = re.sub(r"\s+", " ", value).strip()
        entries[key] = fields
    return entries


def progress_metadata() -> dict[str, dict[str, str]]:
    result: dict[str, dict[str, str]] = {}
    for line in PROGRESS.read_text(encoding="utf-8").splitlines():
        if not re.match(r"^\| P\d{2} \|", line):
            continue
        cells = [cell.strip().strip("`") for cell in line.strip("|").split("|")]
        if len(cells) >= 10:
            pid = cells[0]
            result[pid] = {
                "decision": cells[4], "relevance": cells[5],
                "quality": cells[6].split("/")[0], "confidence": cells[7],
            }
    return result


def note_quality_score(text: str) -> str:
    match = re.search(r"(?:Total|Overall)\s*:\s*`?(\d{1,2})\s*/\s*24", text, re.I)
    return match.group(1) if match else "NR"


def last_section(text: str, number: int) -> str:
    pattern = re.compile(rf"^(#{{2,3}})\s+{number}\.\s+.*$", re.M)
    matches = list(pattern.finditer(text))
    if not matches:
        return ""
    match = matches[-1]
    level = len(match.group(1))
    start = match.end()
    end = len(text)
    for heading in re.finditer(r"^(#{2,3})\s+\d+\.\s+.*$", text[start:], re.M):
        if len(heading.group(1)) <= level:
            end = start + heading.start()
            break
    return text[start:end].strip()


def last_titled_section(text: str, title_pattern: str, fallback_number: int) -> str:
    pattern = re.compile(rf"^(#{{2,3}})\s+(?:\d+\.\s+)?(?:{title_pattern}).*$", re.M | re.I)
    matches = list(pattern.finditer(text))
    if not matches:
        return last_section(text, fallback_number)
    match = matches[-1]
    level = len(match.group(1))
    start = match.end()
    end = len(text)
    for heading in re.finditer(r"^(#{2,3})\s+", text[start:], re.M):
        if len(heading.group(1)) <= level:
            end = start + heading.start()
            break
    return text[start:end].strip()


def codes(text: str, vocabulary: dict[str, tuple[str, ...]]) -> str:
    found = [label for label, patterns in vocabulary.items() if any(re.search(p, text, re.I) for p in patterns)]
    return ";".join(found) if found else "NR"


def code_evidence(text: str, vocabulary: dict[str, tuple[str, ...]]) -> dict[str, str]:
    evidence: dict[str, str] = {}
    blocks = [block.strip() for block in text.splitlines() if block.strip()]
    negative_evidence = re.compile(
        r"not (?:directly )?(?:assessed|reported|measured|evaluated)|"
        r"do not attribute|should not be claimed|outside (?:the )?scope|"
        r"not applicable|unavailable|\bno (?:full )?(?:review )?workflow(?: evidence)?",
        re.I,
    )
    for label, patterns in vocabulary.items():
        for block in blocks:
            if negative_evidence.search(block):
                continue
            if any(re.search(pattern, block, re.I) for pattern in patterns):
                evidence[label] = re.sub(r"\s+", " ", block).strip(" |-:")[:500]
                break
    return evidence


def substantive(text: str, positive: tuple[str, ...], negative: tuple[str, ...]) -> str:
    if any(re.search(p, text, re.I) for p in negative):
        return "no"
    if any(re.search(p, text, re.I) for p in positive):
        return "yes"
    return "NR"


def labeled_line(section: str, labels: tuple[str, ...]) -> str:
    for line in section.splitlines():
        if any(re.match(rf"^\s*[-*]?\s*(?:\*\*)?{label}", line, re.I) for label in labels):
            return re.sub(r"\*\*", "", line).strip()
    return ""


def reporting_status(section: str, field: str) -> str:
    label_map = {
        "preservation": ("useful-feedback preservation", "useful feedback potentially lost", "preservation"),
        "coverage": ("review coverage", "coverage effect", "coverage"),
        "escalation": ("human escalation effect", "human escalation"),
        "cost": ("computational/operational cost", "operational cost", "cost"),
    }
    line = labeled_line(section, label_map[field])
    if not line:
        return "NR"
    low = line.lower()
    generic_absence = (
        "not reported", "not measured", "not directly measured", "not assessed",
        "unreported", "no formal rate", "not defined", "otherwise not reported",
        "retained useful-issue coverage is incomplete", "task-specific",
        "not directly enumerated", "deployment escalation is not applicable",
    )
    if any(phrase in low for phrase in generic_absence):
        return "no"
    if field == "preservation" and any(phrase in low for phrase in ("absent", "not quantified", "incomplete")):
        return "no"
    if field == "coverage" and any(phrase in low for phrase in (
        "coverage is incomplete", "coverage incomplete",
        "downstream issue coverage is not",
        "useful-issue retention after mitigation is incomplete",
        "useful-issue retention after intervention is incomplete",
    )):
        return "no"
    if field == "escalation" and "reviewers inspect and decide" in low:
        return "no"
    # A non-empty, non-negative labeled field is evidence that the note records a
    # qualitative or quantitative result. Numeric detail is preserved in the audit snippet.
    return "yes"


def rq_status(section: str, rq: int) -> str:
    line = next((ln for ln in section.splitlines() if re.search(rf"\|\s*RQ{rq}\s*\|", ln, re.I)), "")
    if not line:
        bullet = next((ln for ln in section.splitlines() if re.search(rf"RQ{rq}\s*:", ln, re.I)), "")
        line = bullet
    low = line.lower()
    if not line or "not reported" in low or "not assessed" in low:
        return "NR"
    if "our perspective" in low and "reported" not in low and "inferred" not in low:
        return "perspective_only"
    if "inferred" in low or "our perspective" in low:
        return "inferred_or_mixed"
    if "reported" in low:
        return "reported"
    return "present"


def venue_and_type(fields: dict[str, str]) -> tuple[str, str]:
    kind = fields.get("entry_type", "other")
    venue = fields.get("journal") or fields.get("booktitle") or fields.get("howpublished") or fields.get("publisher") or "NR"
    low = venue.lower()
    if kind == "inproceedings" or re.search(r"conference|proceedings|\bfase\b|\bicse\b|\bfse\b|\base\b|\bmsr\b", low):
        pub_type = "conference"
    elif re.search(r"arxiv|preprint", low):
        pub_type = "preprint_or_other"
    elif kind == "article" or re.search(r"journal|transactions", low):
        pub_type = "journal"
    else:
        pub_type = {"misc": "preprint_or_other", "book": "book"}.get(kind, kind)
    return venue, pub_type


def main() -> None:
    all_canonical = set(CANONICAL_PROJECT_NUMBERS)
    supplementary_core = {number for number in all_canonical if number >= 72}
    core_ids = CORE | supplementary_core
    if CORE & SUPPORTING or CORE & PERIPHERAL or SUPPORTING & PERIPHERAL:
        raise SystemExit("Evidence-tier sets overlap")
    if CORE | SUPPORTING | PERIPHERAL != set(range(1, 72)):
        raise SystemExit("Baseline evidence-tier sets do not cover P01–P71 exactly")

    bib = bib_entries()
    progress = progress_metadata()
    rows: list[dict[str, str]] = []
    audit_rows: list[dict[str, str]] = []
    for path in sorted(CANONICAL_NOTES.glob("P[0-9]*-*.md")):
        pid = path.name.split("-", 1)[0]
        num = int(pid[1:])
        text = path.read_text(encoding="utf-8")
        key_match = re.search(r"`(p\d+_[^`]+)`", text)
        if not key_match:
            raise SystemExit(f"Missing citation key in {path}")
        key = key_match.group(1)
        fields = bib.get(key, {})
        venue, pub_type = venue_and_type(fields)
        s4, s5, s6, s10 = (last_section(text, n) for n in (4, 5, 6, 10))
        s7 = last_titled_section(text, r"Mitigation and trade-offs", 7)
        s8 = last_titled_section(text, r"Annotation and evaluator validity", 8)
        relevant = "\n".join((s4, s5, s6, s7, s8))
        meta = progress.get(pid, {})
        tier = "Core" if num in core_ids else "Supporting" if num in SUPPORTING else "Peripheral"
        evaluator_types = []
        if re.search(r"human|annotator|developer|participant", s8, re.I): evaluator_types.append("human")
        if re.search(r"llm|gpt|judge", s8, re.I): evaluator_types.append("llm_judge")
        if re.search(r"automatic metric|bleu|rouge|bertscore|codebleu", s6, re.I): evaluator_types.append("automatic_metric")
        if re.search(r"execution|test|static analy|tool", s6 + s8, re.I): evaluator_types.append("tool_or_execution")
        intervention = []
        for label, phrase in (("before_generation", "before generation"), ("during_generation", "during generation"), ("after_generation", "after generation"), ("before_display", "before display")):
            if phrase in s7.lower(): intervention.append(label)
        mitigation_vocab = {k: v for k, v in MITIGATIONS.items() if k != "human_escalation"}
        mitigation_evidence = code_evidence(s7, mitigation_vocab)
        mitigation_labels = list(mitigation_evidence)
        escalation_line = next((line for line in s7.splitlines() if re.search(r"human escalation", line, re.I)), "")
        if escalation_line and reporting_status(s7, "escalation") == "yes":
            mitigation_labels.append("human_escalation")
            mitigation_evidence["human_escalation"] = re.sub(r"\s+", " ", escalation_line).strip(" |-:")[:500]
        failure_evidence = code_evidence(s5, FAILURES)
        dimension_evidence = code_evidence(s6, DIMENSIONS)
        context_evidence = code_evidence(relevant, CONTEXTS)
        row = {
            "paper_id": pid,
            "citation_key": key,
            "title": fields.get("title", re.sub(rf"^#\s+{pid}\s+[—-]\s+", "", text.splitlines()[0]).strip()),
            "year": fields.get("year", "NR"),
            "venue": venue,
            "publication_type": pub_type,
            "evidence_tier": tier,
            "decision": meta.get("decision", "NR"),
            "relevance": meta.get("relevance", "NR"),
            "quality_score": meta.get("quality", note_quality_score(text)),
            "confidence": meta.get("confidence", "NR"),
            "context_types": ";".join(context_evidence) if context_evidence else "NR",
            "failure_types": ";".join(failure_evidence) if failure_evidence else "NR",
            "evaluation_dimensions": ";".join(dimension_evidence) if dimension_evidence else "NR",
            "mitigation_families": ";".join(mitigation_labels) if mitigation_labels else "NR",
            "intervention_points": ";".join(intervention) if intervention else "NR",
            "preservation_reported": reporting_status(s7, "preservation"),
            "coverage_reported": reporting_status(s7, "coverage"),
            "escalation_reported": reporting_status(s7, "escalation"),
            "cost_reported": reporting_status(s7, "cost"),
            "annotation_reported": "yes" if re.search(r"annotator|annotation|participant|user study|human evaluat", s8, re.I) and not re.search(r"not reported|unavailable", s8, re.I) else "no" if re.search(r"not reported|unavailable", s8, re.I) else "NR",
            "evaluator_types": ";".join(evaluator_types) if evaluator_types else "NR",
            "limitations_reported": "yes" if len(s10) > 80 and not re.fullmatch(r".*not reported.*", s10, re.I | re.S) else "NR",
            **{f"rq{i}_evidence": rq_status(s4, i) for i in range(1, 7)},
            "source_note": str(path.relative_to(ROOT)),
        }
        rows.append(row)
        for field, evidence_map in (
            ("failure_types", failure_evidence),
            ("evaluation_dimensions", dimension_evidence),
            ("mitigation_families", mitigation_evidence),
            ("context_types", context_evidence),
        ):
            for code, snippet in evidence_map.items():
                audit_rows.append({"paper_id": pid, "field": field, "code": code, "evidence_snippet": snippet, "source_note": row["source_note"]})
        for field in ("preservation", "coverage", "escalation", "cost"):
            audit_rows.append({
                "paper_id": pid,
                "field": f"{field}_reported",
                "code": row[f"{field if field != 'preservation' else 'preservation'}_reported"],
                "evidence_snippet": labeled_line(s7, {
                    "preservation": ("useful-feedback preservation", "useful feedback potentially lost", "preservation"),
                    "coverage": ("review coverage", "coverage effect", "coverage"),
                    "escalation": ("human escalation effect", "human escalation"),
                    "cost": ("computational/operational cost", "operational cost", "cost"),
                }[field]),
                "source_note": row["source_note"],
            })

    expected_ids = {f"P{i:02d}" for i in all_canonical}
    if len(rows) != len(expected_ids) or {r["paper_id"] for r in rows} != expected_ids:
        raise SystemExit("Dataset does not contain exactly the canonical note set")

    OUT_DIR.mkdir(exist_ok=True)
    csv_path = OUT_DIR / "slr-extraction.csv"
    with csv_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]), lineterminator="\n")
        writer.writeheader(); writer.writerows(rows)
    audit_path = OUT_DIR / "slr-coding-evidence.csv"
    with audit_path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=("paper_id", "field", "code", "evidence_snippet", "source_note"),
            lineterminator="\n",
        )
        writer.writeheader(); writer.writerows(audit_rows)

    def count_multi(field: str) -> Counter[str]:
        c: Counter[str] = Counter()
        for row in rows:
            if row[field] != "NR": c.update(row[field].split(";"))
        return c

    summary = ["# Generated SLR Descriptive Summary", "", "> Generated by `scripts/build_slr_dataset.py`; do not edit manually.", ""]
    summary += ["## Corpus", "", "| Measure | Count |", "|---|---:|", f"| Records | {len(rows)} |"]
    for tier in ("Core", "Supporting", "Peripheral"):
        summary.append(f"| {tier} evidence | {sum(r['evidence_tier'] == tier for r in rows)} |")
    summary += ["", "## Publication years", "", "| Year | Studies |", "|---|---:|"]
    year_counts = Counter(r["year"] for r in rows)
    summary += [f"| {year} | {count} |" for year, count in sorted(year_counts.items(), key=lambda item: (item[0] == "NR", item[0]))]
    summary += ["", "## Publication types", "", "| Type | Studies |", "|---|---:|"]
    summary += [f"| `{kind}` | {count} |" for kind, count in Counter(r["publication_type"] for r in rows).most_common()]
    for field, title in (("failure_types", "RQ1 failure types"), ("evaluation_dimensions", "RQ2 evaluation dimensions"), ("mitigation_families", "RQ3 mitigation families"), ("context_types", "RQ5 context types")):
        summary += ["", f"## {title}", "", "| Code | Studies with coded evidence |", "|---|---:|"]
        summary += [f"| `{name}` | {count} |" for name, count in count_multi(field).most_common()]
    summary += ["", "## RQ4 reporting availability", "", "| Field | Yes | No | NR |", "|---|---:|---:|---:|"]
    for field in ("preservation_reported", "coverage_reported", "escalation_reported", "cost_reported"):
        c = Counter(r[field] for r in rows); summary.append(f"| `{field}` | {c['yes']} | {c['no']} | {c['NR']} |")
    summary += ["", "## Quality score", ""]
    scores = [int(r["quality_score"]) for r in rows if r["quality_score"].isdigit()]
    summary += [f"- Records scored: {len(scores)}", f"- Mean: {sum(scores)/len(scores):.2f}/24", f"- Minimum: {min(scores)}/24", f"- Maximum: {max(scores)}/24"]
    summary += ["", "| Evidence tier | Studies | Mean quality |", "|---|---:|---:|"]
    for tier in ("Core", "Supporting", "Peripheral"):
        tier_scores = [int(r["quality_score"]) for r in rows if r["evidence_tier"] == tier and r["quality_score"].isdigit()]
        summary.append(f"| {tier} | {len(tier_scores)} | {sum(tier_scores)/len(tier_scores):.2f}/24 |")
    (OUT_DIR / "slr-summary.md").write_text("\n".join(summary) + "\n", encoding="utf-8")
    print(f"Wrote {csv_path.relative_to(ROOT)} ({len(rows)} records)")
    print(f"Wrote {audit_path.relative_to(ROOT)} ({len(audit_rows)} evidence rows)")
    print("Wrote data/slr-summary.md")


if __name__ == "__main__":
    main()
