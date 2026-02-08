---
name: cascade-checklist
trigger: Library (called by sot-update-trigger)
description: >
  Generates context-specific cascade checklists based on which files changed.
  Replaces generic "update SoT" reminders with actionable, file-specific steps
  that reference section anchors, not line numbers.
---

# Cascade Checklist Generator

**Trigger**: Library — called by `sot-update-trigger.py`, not registered standalone.
**Purpose**: Replace generic "update SoT" reminders with specific, actionable cascade steps.

## What This Script Does

1. Accepts a list of changed file paths
2. Classifies them into categories (test changes, API changes, epic phases, etc.)
3. Returns the specific cascade checklist for each matched category
4. References `<!-- SECTION: -->` markers for durable README locations

## Why This Exists

From HomeFalcon learnings: the original SoT update trigger said "update SoT files" generically. Subagents followed the spirit but missed specifics because the instruction didn't say *which* files, *which* sections, or *which* values. This script makes the cascade concrete.

## Usage

### As a Python library

```python
from cascade_checklist import get_checklists, format_checklists

checklists = get_checklists(["tests/test_auth.py", "src/api/handler.py"])
# Returns:
# [
#     {"category": "test_changes", "trigger_files": ["tests/test_auth.py"], "steps": [...]},
#     {"category": "api_changes", "trigger_files": ["src/api/handler.py"], "steps": [...]},
# ]

output = format_checklists(checklists)
# Returns formatted markdown with specific steps per category
```

### As a standalone script

```bash
echo '["tests/test_auth.py", "src/api/handler.py"]' | python3 .claude/hooks/cascade-checklist.py
```

## Change Categories

| Category | Trigger Patterns | Cascade Steps |
|----------|-----------------|---------------|
| **test_changes** | `*.test.*`, `*.spec.*`, `__tests__/`, `tests/` | Update metrics.json, README Truth Table, SoT.TESTING.md |
| **epic_phase_change** | `epics/EPIC-*.md` | Update README dashboard, status header, PRD.md |
| **api_changes** | `*/api/*`, `*/routes/*`, `*.controller.*` | Update SoT.API_CONTRACTS.md, TEST- entries |
| **schema_changes** | `migrations/`, `*.model.*`, `models/` | Update SoT.DATA_MODEL.md, DBT- entries |
| **business_rule_changes** | `rules/`, `validators/`, `policies/` | Update SoT.BUSINESS_RULES.md, BR- entries |
| **sot_changes** | `SoT/` | Verify cross-references, update README |
| **readme_changes** | `README.md` | Verify metrics match, check section consistency |
| **config_changes** | `package.json`, `Dockerfile`, `docker-compose` | Update SoT.DEPLOYMENT.md, DEP-/RUN- entries |

## Customization

Projects should customize the `CHECKLISTS` dict in `cascade-checklist.py` to match their file structure. The default patterns cover common conventions but may need adjustment for:

- Non-standard test directory names
- Custom API route locations
- Project-specific SoT file names

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Data-driven checklists | Easy to customize per project |
| Section anchors, not line numbers | Line numbers drift; markers are stable |
| Multiple categories per file | A file can trigger both "api_changes" and "test_changes" |
| Non-blocking output | Reminders, not gates — skip what doesn't apply |

## Testing

```bash
# Test with test files
echo '["tests/test_auth.py"]' | python3 .claude/hooks/cascade-checklist.py

# Test with API files
echo '["src/api/handler.py", "src/routes/index.ts"]' | python3 .claude/hooks/cascade-checklist.py

# Test with mixed files
echo '["tests/test_auth.py", "epics/EPIC-04-auth.md", "src/api/handler.py"]' | python3 .claude/hooks/cascade-checklist.py

# Test with no matching patterns (should produce no output)
echo '["assets/logo.png"]' | python3 .claude/hooks/cascade-checklist.py
```
