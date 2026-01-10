---
title: "CLAUDE Agent Operating Guide"
updated: "2025-01-09"
authority: "Gear Heart Methodology"
---

# CLAUDE.md — Universal Operating Rules

> **Mission**: Build software in lockstep with the PRD lifecycle.
> **Load Order**: README.md → PRD.md → CLAUDE.md → agents/{ROLE}.md → Active EPIC

---

## Context Loading

1. Always load README.md first (project status)
2. Load PRD.md (current lifecycle gate)
3. For role-specific work, load `agents/{AGENT}.md`
4. Load active EPIC from `epics/`

## Documentation Discipline

- Reference SoT IDs (BR-, UJ-, API-, CFD-) in code comments and commits
- Update `specs/` files during changes, never "later"
- One document, many versions—never create PRD-v2.md

## Commit Format

```
{type}({scope}): {description}

Types: feat, fix, docs, refactor, test
Example: feat(api): implement BR-101 limit check
```

## Session Protocol

**Start**: Load context per above, read EPIC Section 0 for state
**End**: Update EPIC Section 0 with:
- Progress (with ID references)
- Stop point (file:line)
- Next steps (numbered)
Commit: `session: [EPIC-XX] {summary}`

## Escalation Rules

- Context full → Suggest session handoff with state summary
- Gate blocked → Update EPIC, stop, do not proceed
- Pattern observed (3x) → Log to agent memory, consider skill extraction

## ID Quick Reference

| Prefix | Domain | SoT File |
|--------|--------|----------|
| BR- | Business Rules | `specs/SoT.BUSINESS_RULES.md` |
| UJ- | User Journeys | `specs/SoT.USER_JOURNEYS.md` |
| API- | Contracts | `specs/SoT.API_CONTRACTS.md` |
| CFD- | Feedback | `specs/SoT.customer_feedback.md` |
| DES- | Design | `specs/SoT.DESIGN_BRIEF.md` |
| TEST- | Tests | `specs/SoT.testing_playbook.md` |

---

**For agent-specific behavior, load `agents/{AGENT}.md`**
