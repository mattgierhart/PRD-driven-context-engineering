# Migration Guide

This document helps derivative repos sync with template changes. Each version section includes a checklist of required actions.

> **Tip**: Check `.claude/VERSION` in this template to see the current version, and compare it with the `template_version` field in your repo's CLAUDE.md frontmatter to determine your starting point.

---

## v2.0.0 → v3.0.0

**Released**: 2026-02-12

### Breaking Changes

These require manual action in derivative repos:

- [ ] **Agents restructured**: flat files → subdirectories
  - `.claude/agents/HORIZON.md` → `.claude/agents/horizon/AGENT.md` + `MEMORY.md`
  - `.claude/agents/STUDIO.md` → `.claude/agents/studio/AGENT.md` + `MEMORY.md`
  - `.claude/agents/WERK.md` → `.claude/agents/werk/AGENT.md` + `MEMORY.md`
  - `.claude/agents/METRO.md` → `.claude/agents/metro/AGENT.md` + `MEMORY.md`
  - **Split point**: Everything above `## Project Memory (CRITICAL)` goes in AGENT.md; everything from that heading onward goes in MEMORY.md (promote header to H1)
  - **Note**: If your agents have accumulated project-specific memory, preserve MEMORY.md content — only the AGENT.md structure should match the template

- [ ] **EPIC sections changed from numbered to semantic headers**
  - `## 0. Session State` → `## Session State`
  - `## 1. Objective & Scope` → `## Objective & Scope`
  - `## 2. Context & IDs` → `## Context & IDs`
  - `## 3. Execution Plan` → `## Execution Plan`
  - `## 4. Change Log` → `## Change Log`
  - **Note**: Existing in-flight EPICs can keep old numbering until completed. Only the EPIC_TEMPLATE.md needs updating.

- [ ] **CLAUDE.md references updated**
  - "Section 0" → "Session State section"
  - "Update EPIC Section 0" → "Update the EPIC Session State section"
  - ID Ownership now references `.claude/domain-profile.yaml`

### New Files to Add

- [ ] `CHANGELOG.md` — Copy from template (update with your repo's history)
- [ ] `.claude/VERSION` — Copy from template
- [ ] `MIGRATION.md` — Copy from template
- [ ] `.claude/domain-profile.yaml` — Copy from template, customize `id_prefixes` if you use a non-product domain
- [ ] `.claude/hooks/HOOK_CONTRACT.md` — Copy from template
- [ ] `.claude/hooks/context-validation.sh` — Shell variant of SessionStart hook
- [ ] `.claude/hooks/context-density-gate.sh` — Shell variant of UserPromptSubmit hook
- [ ] `.claude/hooks/sot-update-trigger.sh` — Shell variant of Stop hook

### Files to Update

- [ ] **CLAUDE.md** frontmatter: add `template_version: "3.0.0"`
- [ ] **PRD.md** frontmatter: add `template_version: "3.0.0"`
- [ ] **EPIC_TEMPLATE.md**: add frontmatter with `template_version: "3.0.0"`, update numbered sections to semantic
- [ ] **SoT/SoT.README.md** frontmatter: add `template_version: "3.0.0"`
- [ ] **Hook .md files**: add Dependencies section (see template for format)
- [ ] **`.claude/README.md`**: update directory tree, hooks table, and agents table to match new structure
- [ ] Add `<!-- SECTION: -->` and `<!-- CUSTOMIZABLE: -->` markers to template files (see template for placement)

### For Non-Product Repos

If your repo is not a product development repo (e.g., dotfiles, infrastructure, library):

- [ ] Copy `.claude/domain-profile.yaml` and customize:
  - Change `profile:` to your domain type
  - Replace `id_prefixes` with your domain's taxonomy
  - Remove `prd-v*` domain skills, keep `ghm-*` core skills
  - Remove `agents` section if role specialization doesn't apply
- [ ] Use shell hook variants (`.sh`) instead of Python if your repo has no Python dependency
- [ ] Drop SoT files that don't map to your domain; create domain-specific ones using `ghm-sot-builder`

---

## v1.0.0 → v2.0.0

**Released**: 2026-01-12

### Changes

- Complete skill library added (26 PRD lifecycle + 5 methodology skills)
- 3 Python hooks added (context-validation, context-density-gate, sot-update-trigger)
- 4 agent definitions added (HORIZON, STUDIO, WERK, METRO)
- 12 SoT files standardized to ~100-150 lines each
- Methodology renamed to "PRD Led Context Engineering"

### Migration

- [ ] Copy `.claude/skills/` directory from template
- [ ] Copy `.claude/hooks/` directory from template
- [ ] Copy `.claude/agents/` directory from template
- [ ] Update `settings.json` to wire hooks
- [ ] Standardize SoT file structure to match new template
