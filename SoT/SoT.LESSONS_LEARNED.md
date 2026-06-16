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

- [LL-101](#ll-101-ship-a-blueprint-not-a-binary--make-the-agent-runtime-the-installer): Ship a blueprint, not a binary — make the agent runtime the installer.

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

## Entries

### LL-101: Ship a blueprint, not a binary — make the agent runtime the installer

- **Rule**: To distribute a Claude Code methodology, ship plain files that a fresh Claude
  Code session installs (a "blueprint"), rather than a packaged runtime or an API-backed
  service. The agent *is* the installer, so adoption costs the user's subscription tokens,
  not metered API calls.
- **Why**: Analysis of `ZQadus/Xantham-system-blueprint` (2026-06) showed a self-installing
  multi-agent system that runs entirely on a Pro/Max subscription — API is touched only at
  optional edges (~$1/week consolidation). The leverage is structural: because every install
  step is file I/O the agent performs, there is no separate runtime to bill or host. Our
  prior adoption story was fork-the-whole-repo only; the README roadmap named "one-command
  install into existing repos" as the missing piece.
- **How to apply**: When adding a distribution/onboarding path, prefer (a) a manifest that
  classifies every path as framework / seed-once / never-touch, (b) a deterministic CLI
  installer *and* an interactive skill that both read that one manifest (so they can't
  drift), and (c) non-destructive brownfield behavior — seed templates once, merge into
  existing `settings.json`, never overwrite product content. Defer heavier hardening
  (Docker audit sandbox, signed checksums, MCP service) as explicit, labeled next steps.
- **Source**: manual — Xantham self-install analysis (branch `claude/xantham-self-install-analysis`)
- **Verified**: 2026-06-16
- **Related IDs**: _(none — see `.claude/install-manifest.yaml`, `install.sh`, skill `ghm-self-install`)_

---

## Deprecated Entries

> Entries that are no longer applicable. Keep for historical context.

_(None yet)_

---

## Cross-Reference Index

| LL ID | Related IDs | Category |
|-------|-------------|----------|
| LL-001 | {BR-XXX, API-YYY} | {Process / Technical / Collaboration / Estimation} |
| LL-101 | — (install-manifest.yaml, install.sh, ghm-self-install) | Technical |

---

## Update Protocol

1. **When**: During EPIC Phase E harvest, promote agent memory entries with 3+ occurrences or cross-EPIC relevance.
2. **Format**: Follow the entry template above. Include Rule → Why → How to apply → Source → Verified date.
3. **Archive**: Promoted entries are moved from agent MEMORY.md to MEMORY_ARCHIVE.md (preserve provenance).
4. **Review**: Entries older than 90 days without re-verification should be flagged as `⚠️ STALE`.
