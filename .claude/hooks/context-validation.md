---
name: context-validation
trigger: SessionStart
description: >
  Ensures agents follow CLAUDE → README → PRD → accepted SoT → v0.7+ EPIC at session start.
  Injects reading order guidance rather than file contents to preserve context window.
---

# Context Validation Hook

**Trigger**: `SessionStart` (every session start, resume, or clear)
**Purpose**: Enforce lifecycle-aware context loading order at session start.

## What This Hook Does

On every session start, this hook:

1. Checks if core files exist (README.md, PRD.md, CLAUDE.md)
2. Reads PRD lifecycle gate (if specified) to assess if EPICs apply (v0.7+)
3. Selects exactly one numeric EPIC whose `State` field is `In Progress` when v0.7+ applies
4. Injects reading order directive into context

## Logic Flow

```
1. Check PRD.md exists -> parse its frontmatter `version` (with a narrowly named gate fallback)
2. At v0.7+, inspect numeric `epics/EPIC-...md` files for an exact `State: In Progress`
3. If zero or multiple active EPICs are found, warn (non-blocking); never select a template,
   planned, queued, or completed EPIC as the active context
4. Output additionalContext with reading order directive
```

## Output Example

```markdown
## Context Loading Required

Before responding to any task, read these files in order:
1. `CLAUDE.md`
2. `README.md`
3. `PRD.md`
4. Accepted `SoT/` records referenced by `PRD.md`
5. `epics/EPIC-03-onboarding-flow.md` (v0.7+ only)

This establishes:
- Structural rules and documentation discipline (CLAUDE.md)
- Current project status and navigation (README.md)
- Product definition and current lifecycle stage (PRD.md)
- Accepted durable product detail (SoT records referenced by PRD.md)
- Active work unit and acceptance criteria (epics/EPIC-03-onboarding-flow.md)
```

## Dependencies

- Bash, `grep`, `sed`, `head`, `wc`
- No external packages required

> See [HOOK_CONTRACT.md](HOOK_CONTRACT.md) for the universal hook interface specification.

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
        "hooks": [
          {
            "type": "command",
            "command": "bash \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/context-validation.sh",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

## Testing

```bash
echo '{}' | bash .claude/hooks/context-validation.sh
echo '{}' | bash .claude/hooks/context-validation.sh | python3 -m json.tool
```
