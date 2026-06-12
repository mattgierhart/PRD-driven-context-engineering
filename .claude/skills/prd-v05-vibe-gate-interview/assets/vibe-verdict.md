# Vibe Verdict Template

This is the markdown block the decision sheet's "Copy my decisions" button produces, and the
shape Phase 7b parses. It lands in PRD v0.5 **"Outstanding Work → v0.6"** next to the
`ghm-gate-check` readiness score.

```markdown
**Vibe Verdict (v0.5 gate)**: GO | GO-WITH-CHECKS | PAUSE
**Decided**: YYYY-MM-DD by {PM name}
**Rationale**: {one line — why this verdict, citing IDs}

**Riskiest assumption** (→ RISK-XXX, owner = PM):
> {the single belief that sinks the product if wrong}

**Cheap checks** (→ one CFD- validation task each, confidence 1/5 until run):
| Check | Date | Status |
|---|---|---|
| {e.g. ten DMs to r/X members} | YYYY-MM-DD | scheduled |

**First 10 users**: {ten real people or one real place}
**Watering hole** (→ PER-XXX note): {the single community}
**First move**: {one concrete action}

**Complexity**: {N}/10 · **Timeline**: {V1 phases} · **Audience**: learning | real users

**If PAUSE — unblock condition**: {what must become true to flip to GO}
```

Recording rules (Phase 7b):

- RISK- entry uses the v0.5 template (`prd-v05-risk-discovery-interview/assets/risk.md`),
  `Added: v0.5`, owner = PM.
- Each cheap check becomes a CFD- entry tagged as a validation task with its date.
- The watering-hole line is appended to the primary PER- entry.
- Markdown is authoritative; the HTML sheet is disposable after this block is recorded.
