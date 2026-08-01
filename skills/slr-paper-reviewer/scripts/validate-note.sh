#!/usr/bin/env bash

set -u

if [[ $# -eq 0 ]]; then
  printf 'Usage: %s papers/PXX-note.md [...]\n' "$0" >&2
  exit 2
fi

failed=0

sections=(
  'Identification'
  'Screening'
  'Study overview'
  'Evidence mapped'
  'Failure and problematic-comment categories'
  'Evaluation dimensions and metrics'
  'Mitigation and trade-offs'
  'Annotation and evaluator validity'
  'Quality appraisal'
  'Review-process reliability and bias'
  'Synthesis-ready conclusion'
)

for note in "$@"; do
  note_failed=0

  if [[ ! -f "$note" ]]; then
    printf 'FAIL %s: file not found\n' "$note"
    failed=1
    continue
  fi

  for section in "${sections[@]}"; do
    if ! rg -qi "^#{2,4} ([0-9]+\\. )?.*${section}" "$note"; then
      printf 'FAIL %s: missing section %s\n' "$note" "$section"
      note_failed=1
    fi
  done

  for rq in 1 2 3 4 5 6; do
    if ! rg -q "^\\| RQ${rq} \\|" "$note"; then
      printf 'FAIL %s: missing canonical RQ%s row\n' "$note" "$rq"
      note_failed=1
    fi
  done

  for q in {1..12}; do
    if ! rg -q "^\\| Q${q}( |[^0-9])" "$note"; then
      printf 'FAIL %s: missing Q%s evidence row\n' "$note" "$q"
      note_failed=1
    fi
  done

  for field in 'Useful feedback potentially lost' 'Coverage' 'Human escalation' 'Cost'; do
    if ! rg -qi "${field}" "$note"; then
      printf 'FAIL %s: missing trade-off field %s\n' "$note" "$field"
      note_failed=1
    fi
  done

  if [[ $note_failed -eq 0 ]]; then
    printf 'PASS %s\n' "$note"
  else
    failed=1
  fi
done

exit "$failed"
