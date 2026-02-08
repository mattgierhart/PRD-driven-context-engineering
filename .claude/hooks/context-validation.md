---
name: context-validation
trigger: SessionStart
description: >
  Ensures agent loads 3+1 files (CLAUDE.md, README.md, PRD.md, current EPIC) at session start.
  Injects reading order guidance rather than file contents to preserve context window.
  Also checks for metrics drift to prevent stale context propagation.
---

# Context Validation Hook

**Trigger**: `SessionStart` (every session start, resume, or clear)
**Purpose**: Enforce 3+1 file loading order and detect metrics drift at session start.

## What This Hook Does

On every session start, this hook:

1. Checks if core files exist (CLAUDE.md, README.md, PRD.md)
2. Determines PRD version to assess if EPICs apply (v0.7+)
3. Finds active EPIC if applicable
4. Injects reading order directive into context
5. Checks for metrics drift between `status/metrics.json` and `README.md` (v0.7+ projects)

## Logic Flow

```
1. Check PRD.md exists -> extract current_version (e.g., "v0.5")
2. Determine if EPIC layer applies:
   - If current_version < v0.7 -> EPICs not yet created, skip EPIC requirement
   - If current_version >= v0.7 -> Check for active EPIC in README.md or epics/
3. Output additionalContext with reading order directive
```

## Output Example

```markdown
## Context Loading Required

Before responding to any task, read these files in order:
1. `CLAUDE.md`
2. `README.md`
3. `PRD.md`
4. `epics/EPIC-03-onboarding-flow.md`

This establishes:
- Structural rules and documentation discipline (CLAUDE.md)
- Current project status and navigation (README.md)
- Product definition and current lifecycle stage (PRD.md)
- Active work unit and acceptance criteria (epics/EPIC-03-onboarding-flow.md)
```

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Inject pointers, not content | Preserves context window for actual work |
| Warn on missing files, don't block | Project may be initializing |
| Version-aware EPIC detection | EPICs only exist at v0.7+ |
| Drift check at session start | Prevents stale context propagation (HomeFalcon root cause #4) |
| Graceful import fallback | Works even if metrics-drift-check.py is missing |

## Configuration

```json
{
  "hooks": {
    "SessionStart": [
      {
        "type": "command",
        "command": "python3 .claude/hooks/context-validation.py",
        "timeout": 10000
      }
    ]
  }
}
```

## Testing

```bash
# Test with minimal input
echo '{}' | python3 .claude/hooks/context-validation.py

# Verify JSON output is valid
echo '{}' | python3 .claude/hooks/context-validation.py | python3 -m json.tool
```
