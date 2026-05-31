---
version: 1.0
purpose: Source of Truth for cross-session behavioral corrections and validated patterns.
id_prefix: LL-XXX
last_updated: 2026-04-01
authority: This is a SoT file - entries promoted from agent MEMORY.md files during EPIC Phase E harvest
---

# Lessons Learned (SoT File)

> **Purpose**: Cross-session behavioral corrections and validated patterns that should persist across EPICs and template forks.
> **ID Prefix**: LL-XXX
> **Status**: Active SoT file
> **Harvest Source**: Agent MEMORY.md files (Phase E triage), EPIC observations
> **Audience**: All agents, all sessions
> **Cross-References**: Referenced by EPICs, agent MEMORY.md files

## Navigation by Category

**Process** (LL-001 to LL-099):

- _(Populated during Phase E Harvest of each EPIC)_

**Technical** (LL-101 to LL-199):

- _(Populated during Phase E Harvest of each EPIC)_

**Collaboration** (LL-201 to LL-299):

- _(Populated during Phase E Harvest of each EPIC)_

**Estimation** (LL-301 to LL-399):

- _(Populated during Phase E Harvest of each EPIC)_

---

## Example Entry

### LL-001: {Short title}

- **Rule**: {What to do or not do}
- **Why**: {What happened that taught us this}
- **How to apply**: {When this rule activates}
- **Source**: {EPIC-XX, agent memory, or manual}
- **Verified**: {YYYY-MM-DD}
- **Related IDs**: {BR-XXX, API-YYY, etc.}

---

## Deprecated Entries

> Entries that are no longer applicable. Keep for historical context.

_(None yet)_

---

## Cross-Reference Index

| LL ID | Related IDs | Category |
|-------|-------------|----------|
| LL-001 | {BR-XXX, API-YYY} | {Process / Technical / Collaboration / Estimation} |

---

## Update Protocol

1. **When**: During EPIC Phase E harvest, promote agent memory entries with 3+ occurrences or cross-EPIC relevance.
2. **Format**: Follow the entry template above. Include Rule → Why → How to apply → Source → Verified date.
3. **Archive**: Promoted entries are moved from agent MEMORY.md to MEMORY_ARCHIVE.md (preserve provenance).
4. **Review**: Entries older than 90 days without re-verification should be flagged as `⚠️ STALE`.
