---
name: metrics-drift-check
trigger: Library (called by context-validation, sot-update-trigger, subagent-memory-save)
description: >
  Reusable validation that compares status/metrics.json against README.md
  section markers to detect value disagreements. Exits cleanly when
  metrics.json doesn't exist (pre-v0.7 projects unaffected).
---

# Metrics Drift Check

**Trigger**: Library — called by other hooks, not registered as a standalone hook.
**Purpose**: Detect disagreements between `status/metrics.json` and `README.md`.

## What This Script Does

1. Loads `status/metrics.json` (exits cleanly if absent — pre-v0.7 projects skip)
2. Extracts metric values from README `<!-- SECTION: truth-table -->` markers
3. Normalizes number formatting (1,552 vs 1552, trailing % signs)
4. Compares and reports specific disagreements

## Design Principles

From HomeFalcon learnings on documentation drift elimination:

- **README is the human-authored view.** `status/metrics.json` is the machine-writable source.
- **Validation ensures agreement.** Never auto-generate README content from JSON.
- **Section markers, not line numbers.** Uses `<!-- SECTION: truth-table -->` for durability.

## Usage

### As a Python library

```python
from metrics_drift_check import check_drift, format_drift_report

result = check_drift()
# result = {
#     "has_drift": True,
#     "skipped": False,
#     "drifts": [{"metric": "test_count", "metrics_json": "1552/1552", "readme": "1565/1565"}],
#     "checked": 3,
# }

report = format_drift_report(result, context="SessionStart")
# Returns formatted markdown or empty string if no drift
```

### As a standalone script

```bash
# Pre-commit validation: exits 0 if consistent, 1 if drift
python3 .claude/hooks/metrics-drift-check.py

# Pipe into pre-commit hook
python3 .claude/hooks/metrics-drift-check.py || exit 1
```

### As a pre-commit hook template

Projects can wire this into their git pre-commit:

```bash
# In .husky/pre-commit or .git/hooks/pre-commit
if git diff --cached --name-only | grep -qE "(metrics\.json|README\.md)"; then
    python3 .claude/hooks/metrics-drift-check.py
fi
```

## metrics.json Expected Shape

The script handles common shapes:

```json
{
  "tests": { "passed": 1552, "total": 1552 },
  "suites": { "passed": 76, "total": 76 },
  "coverage": { "statements": 88.18, "branches": 72.5 },
  "risk": { "score": 12 }
}
```

## Callers

| Hook | When it calls this | Purpose |
|------|-------------------|---------|
| `context-validation.py` | SessionStart | Surface drift before work begins |
| `sot-update-trigger.py` | Stop | Catch drift introduced during session |
| `subagent-memory-save.sh` | SubagentStop | Catch drift from subagent changes |

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Library, not standalone hook | Same logic needed at 3 trigger points |
| Exit cleanly when no metrics.json | Pre-v0.7 projects should not be affected |
| Section markers over line numbers | Line numbers drift on every README edit |
| Normalize before comparing | Handle 1,552 vs 1552, 88.180% vs 88.18% |

## Testing

```bash
# With no metrics.json (should exit 0 silently)
python3 .claude/hooks/metrics-drift-check.py

# Create test fixtures and run
mkdir -p status
echo '{"tests":{"passed":100,"total":100},"coverage":{"statements":85.5}}' > status/metrics.json
# Then edit README Truth Table to have different values and run again
python3 .claude/hooks/metrics-drift-check.py
echo $?  # Should be 1
```
