# Skill Execution Modes (quick / standard / deep)

PRD-lifecycle skills run in one of three depth modes. The mode shapes time budget, output depth, and which optional steps run — it does not change whether the skill is correct or which Source-of-Truth IDs it owns.

| Mode | Time | When to pick it | Output shape |
|------|------|-----------------|--------------|
| **quick** | < 15 min | Solo founder gut-check, "before I commit", rough first pass | 3–5 SoT IDs, no validation rounds, confidence may be 1/5 |
| **standard** (default) | 30–45 min | Normal session, first real attempt at the stage | Full skill execution, every `Consumes` input checked, confidence ≥ 2/5 |
| **deep** | 60–90 min | Critical decision, team-facing, pre-investor, audit | Full + research loops + assumptions log + cross-skill validation, confidence ≥ 3/5 where evidence exists |

## Picking a mode

Default is **standard**. Use the user's framing to infer otherwise.

| Signal in user request | Mode |
|------------------------|------|
| "rough idea", "quick pass", "gut-check", "before I commit" | quick |
| "define", "set up", "plan", "let's do" | standard |
| "audit", "deep dive", "thorough", "investor-ready", "team review", "stress-test" | deep |

Quick is **appropriate, not degraded**. Don't refuse it because "the proper way is more thorough" — the user picked the trade. Honor the time budget by cutting optional steps (`[standard+]`, `[deep only]`), not by speed-running every step.

Only ask the user when framing is genuinely ambiguous.

## Tagging skill phases (for skill authors)

In `SKILL.md` execution steps, annotate optional phases:

- *(no tag)* — runs in all modes
- `[standard+]` — runs in standard and deep only
- `[deep only]` — runs in deep only

Each skill's frontmatter declares supported modes:

```yaml
execution_modes:
  default: standard
  supports: [quick, standard, deep]
```

If a skill genuinely only supports one mode (e.g., a `TEST-` generator that must be exhaustive), declare `supports: [standard]` and explain why in the SKILL.md preamble.

## How depth shows up in outputs

| Output dimension | quick | standard | deep |
|------------------|-------|----------|------|
| SoT IDs created | 3–5 | full | full + assumption log |
| Confidence floor ([P4](../skills/PRINCIPLES.md)) | 1/5 OK | 2/5 minimum | 3/5 minimum where evidence exists |
| Consumes / Produces sections | always emitted | always emitted | always emitted |
| Consumes detail | only obviously-linked IDs | full chain | full chain + downstream impact analysis |
| Anti-pattern check | skipped | done | done with concrete examples called out |
| Cross-skill validation | none | one pass | iterative until clean |

`Consumes` and `Produces` sections are emitted in **every** mode — the mode affects depth of *content*, not whether the section exists.

## Anti-patterns

| Pattern | Fix |
|---------|-----|
| Always running deep regardless of question | Pick the mode that fits the decision |
| Calling output "quick" but doing standard work | Honor the budget; cut optional phases |
| Skipping confidence floors in deep mode | Deep raises the evidence bar, doesn't lower it |
| Adding `[deep only]` to mandatory phases | If a phase is required for correctness, it runs in all modes |
| Quick mode without acknowledging the trade | Say which optional phases you skipped and why |

## Relationship to P3 and P4

Modes are a **time/scope dial**, not a research bypass:

- **quick mode** acknowledges confidence will be 1/5–2/5 and tags outputs accordingly. It does not pretend evidence is stronger than it is.
- **deep mode** raises the confidence floor — if you can't reach 3/5 with available evidence, the skill output should explicitly say *"blocked on research"* and surface the missing inputs.

See [`PRINCIPLES.md`](../skills/PRINCIPLES.md) P3 (Research Drives Scope) and P4 (SoT is Living Evidence) for the underlying discipline.
