---
name: context-validation
trigger: SessionStart
description: >
  Ensures agent loads 3+1 files (README.md, PRD.md, CLAUDE.md, current EPIC) at session start.
  Injects reading order guidance rather than file contents to preserve context window.
---

# Context Validation Hook

**Trigger**: `SessionStart` (every session start, resume, or clear)
**Purpose**: Enforce 3+1 file loading order for methodology compliance.

## What This Hook Does

On every session start, this hook:

1. Checks if core files exist (README.md, PRD.md, CLAUDE.md)
2. Reads PRD lifecycle gate (if specified) to assess if EPICs apply (v0.7+)
3. Finds active EPIC when available (README.md link preferred, fallback to highest EPIC)
4. Injects reading order directive into context

## Logic Flow

```
1. Check PRD.md exists -> extract Current Lifecycle Gate (e.g., "v0.5") from PRD Metadata (if present)
2. Attempt to find active EPIC:
   - Prefer an explicit `epics/EPIC-XX-...md` link in README.md
   - Otherwise, pick the highest-numbered EPIC file (ignoring templates)
3. If lifecycle gate is v0.7+ but no EPIC is found, warn (non-blocking)
4. Output additionalContext with reading order directive
```

## Output Example

```markdown
## Context Loading Required

Before responding to any task, read these files in order:
1. `README.md`
2. `PRD.md`
3. `CLAUDE.md`
4. `epics/EPIC-03-onboarding-flow.md`

This establishes:
- Current project status and navigation (README.md)
- Product definition and current lifecycle stage (PRD.md)
- Structural rules and execution discipline (CLAUDE.md)
- Active work unit and acceptance criteria (epics/EPIC-03-onboarding-flow.md)
```

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Inject pointers, not content | Preserves context window for actual work |
| Warn on missing files, don't block | Project may be initializing |
| Version-aware EPIC detection | EPICs only exist at v0.7+ |

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
