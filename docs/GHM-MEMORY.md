# GHM Memory Log Guide

`.ghm/memory.jsonl` is an append-only ledger of durable decisions and learnings. Use `tools/add_memory_entry.py` instead of editing the file manually.

```bash
python tools/add_memory_entry.py \
  --summary "**Decision:** ..." \
  --epic EPIC-01-onboarding \
  --task TASK-003 \
  --github-issue https://github.com/org/repo/issues/123 \
  --type architectural_decision \
  --ids BR-021 --ids API-007 --tags architecture,pattern
```

## When to log
- You chose an architecture or pattern that will affect future gates.
- You resolved a blocker that others are likely to hit.
- A PRD gate was passed/blocked and you want the rationale searchable across EPICs.

## Entry schema
Each line is JSON (valid YAML) with fields:
- `id` – sequential `mem-0001` style.
- `timestamp` – UTC ISO8601.
- `summary` – short markdown paragraphs (Decision/Problem/Alternatives/Trade-offs/Impact/Pattern).
- `epic`, `task`, `github_issue` – traceability back to the execution surface.
- `type` – `decision`, `pattern`, `lesson`, etc.
- `ids` – SoT IDs this decision touched or validated.
- `tags` – optional taxonomy for querying.

## Query tips
```
# Last five entries
tail -5 .ghm/memory.jsonl | jq -s '.'

# All entries for a TASK
rg --fixed-strings "\"task\": \"TASK-003\"" .ghm/memory.jsonl

# Filter by EPIC
jq -s '.[] | select(.epic == "EPIC-01-onboarding")' .ghm/memory.jsonl

# Filter by entry type (e.g., gate_passed)
jq -s '.[] | select(.type == "gate_passed")' .ghm/memory.jsonl
```

If you need to correct or supersede an entry, add a new line referencing the old `mem-####` id—never edit the file in place.
