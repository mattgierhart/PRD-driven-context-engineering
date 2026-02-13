---
name: context-density-gate
trigger: UserPromptSubmit
description: >
  Assesses context readiness before epic/gate work begins.
  Detects sparse (too little context) and dense (too much context) conditions.
---

# Context Density Gate Hook

**Trigger**: `UserPromptSubmit` (when prompt matches epic/gate patterns)
**Purpose**: Ensure right-sized context before significant work begins.

## What This Hook Does

When user initiates epic or gate work, this hook:

1. Parses prompt for epic/gate reference patterns
2. If epic: Assesses token count and SoT references
3. If gate: Checks gate requirements for that version
4. Outputs assessment as advisory (non-blocking)

## Trigger Patterns

The hook activates on prompts containing:

**Epic patterns:**
- "start work on EPIC-04-onboarding-flow"
- "begin EPIC 02"
- "work on EPIC-01-auth-basics"
- "continue EPIC-03-user-onboarding"

**Gate patterns:**
- "approve gate for v0.5"
- "check gate v1.0"
- "assess the gate for v0.7"

## Density Thresholds

| Condition | Threshold | Assessment |
|-----------|-----------|------------|
| Sparse | < 500 tokens AND no SoT refs | Not enough context to start |
| Ready | 500-4000 tokens | Good to proceed |
| Dense | > 4000 tokens | Epic may need splitting |
| Broad | > 10 SoT references | Scope too wide |

## Output Examples

**Ready:**
```markdown
## Context Check: EPIC-03

Context check passed: ~1200 tokens, 5 SoT references.

Proceeding with work.
```

**Sparse Warning:**
```markdown
## Context Check: EPIC-03

Issues detected:
- **SPARSE**: Epic has ~150 tokens and no SoT references.
  -> Add acceptance criteria, link relevant specs (BR-, UJ-), or decompose from PRD requirements before starting.

**Recommendation:** Address these before starting to reduce drift risk.
```

**Dense Warning:**
```markdown
## Context Check: EPIC-03

Issues detected:
- **DENSE**: Epic has ~5200 tokens (exceeds 4000 threshold).
  -> Consider splitting into multiple epics. Large epics cause context drift.

**Recommendation:** Address these before starting to reduce drift risk.
```

## Dependencies

**Python variant** (`context-density-gate.py`):
- Python 3.10+ standard library only (`json`, `sys`, `re`, `pathlib`)
- No external packages required
- No local module imports

**Shell variant** (`context-density-gate.sh`):
- POSIX shell, `grep`, `sed`, `wc`
- No external packages required

> See [HOOK_CONTRACT.md](HOOK_CONTRACT.md) for the universal hook interface specification.

## Key Design Decisions

| Decision | Rationale |
|----------|-----------|
| Only trigger on epic/gate patterns | Avoid overhead on every prompt |
| Advise, don't block | False positives frustrate users |
| Token estimation (chars/4) | Simple, good enough for assessment |

## Configuration

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "type": "command",
        "command": "python3 .claude/hooks/context-density-gate.py",
        "timeout": 10000
      }
    ]
  }
}
```

## Testing

```bash
# Test Python variant
echo '{"prompt": "start work on EPIC-04-onboarding-flow"}' | python3 .claude/hooks/context-density-gate.py
echo '{"prompt": "approve gate for v0.5"}' | python3 .claude/hooks/context-density-gate.py
echo '{"prompt": "fix the login bug"}' | python3 .claude/hooks/context-density-gate.py  # passthrough

# Test Shell variant
echo '{"prompt": "start work on EPIC-04-onboarding-flow"}' | bash .claude/hooks/context-density-gate.sh
echo '{"prompt": "approve gate for v0.5"}' | bash .claude/hooks/context-density-gate.sh
echo '{"prompt": "fix the login bug"}' | bash .claude/hooks/context-density-gate.sh  # passthrough
```
