# Stage Gate Validation Hook

## Purpose

Enforces PRD lifecycle discipline by validating that required artifacts exist before advancing to the next stage. This hook implements the "block-at-submit, not block-at-write" principle — it doesn't interrupt work, it validates at boundaries.

## Trigger

The hook validates when:
- An agent invokes a skill for a stage higher than the current stage
- Example: Invoking `prd-v07-epic-scoping` when PRD is at v0.5

## Validation Script

Location: `scripts/check-stage-gate.sh`

```bash
# Usage
./scripts/check-stage-gate.sh <target_stage>

# Examples
./scripts/check-stage-gate.sh v0.6    # Check if ready for v0.6
./scripts/check-stage-gate.sh 0.7     # Check if ready for v0.7
```

### Exit Codes

| Code | Meaning |
|------|---------|
| 0 | Gate passed — ready to advance |
| 1 | Gate failed — missing artifacts |
| 2 | Invalid usage |

## What Gets Validated

The script performs **file-existence checks only**. It does NOT validate content quality or semantic correctness.

### Gate Criteria by Stage

| Target Stage | Required Artifacts |
|--------------|-------------------|
| v0.2 Market Definition | PRD.md with v0.1 section, SoT.customer_feedback.md |
| v0.3 Commercial Model | PRD.md with v0.2 section, SoT.BUSINESS_RULES.md |
| v0.4 User Journeys | PRD.md with v0.3 section, SoT.BUSINESS_RULES.md |
| v0.5 Red Team Review | PRD.md with v0.4 section, SoT.USER_JOURNEYS.md |
| v0.6 Architecture | PRD.md with v0.5 section, SoT.USER_JOURNEYS.md, SoT.BUSINESS_RULES.md |
| v0.7 Build Execution | PRD.md with v0.6 section, SoT.TECHNICAL_DECISIONS.md |
| v0.8 Release | PRD.md with v0.7 section, at least one EPIC-*.md |
| v0.9 Go-to-Market | PRD.md with v0.8 section |
| v1.0 Market Adoption | PRD.md with v0.9 section |

## What Hooks DON'T Do

| Hooks Handle | CLAUDE.md / Skills Handle |
|--------------|---------------------------|
| "Did you create the required files?" | "How should you create them?" |
| Binary pass/fail checks | Nuanced guidance and patterns |
| Blocking bad state transitions | Encouraging good practices |

## Agent Workflow When Blocked

When the gate blocks a stage transition:

1. **Read the error message** — it lists exactly what's missing
2. **Run `/ghm-gate-check`** — for detailed guidance on what to create
3. **Create the missing artifacts** — using the appropriate skills
4. **Re-attempt the transition** — gate should pass

If stuck after 2 attempts, escalate to human review.

## Force Gate Override

In exceptional cases, you can bypass the gate:

1. Document the reason in the PRD.md Change Log
2. Use the `--force-gate` flag (conceptual — actual mechanism TBD)
3. Create a follow-up task to address the missing artifacts

**This should be rare.** If you're frequently forcing gates, the methodology needs adjustment.

## Integration with Skills

Skills in `.claude/skills/prd-v0*` should:
1. Check current PRD stage before executing
2. Warn if attempting to skip stages
3. Reference this hook for validation

## Future Enhancements

Potential improvements (not yet implemented):
- Actual Claude Code hook integration (PreToolUse)
- Semantic validation of content (requires LLM)
- Warning accumulator for soft checks
- Integration with CI/CD pipelines
