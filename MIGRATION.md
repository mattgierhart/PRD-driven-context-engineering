# Migration Guide

This document helps derivative repos sync with template changes. Each version section includes a checklist of required actions.

> **Tip**: Check `.claude/VERSION` in this template to see the current version, and compare it with the `template_version` field in your repo's CLAUDE.md frontmatter to determine your starting point.

---

## v3.0.0 → v3.1.0

**Released**: 2026-03-18

### What Changed

Two new skills added, one pre-existing skill registered. No breaking changes.

| Skill | Stage | What It Does |
|-------|-------|-------------|
| `prd-v04-visual-prototype-gate` | v0.4 | Converts SCR- entries into structured prompts for Google Stitch (or equivalent), captures feedback routed to SoT IDs |
| `prd-v06-environment-setup` | v0.6 | Documents dev environment requirements (CLIs, packages, config). **Already existed on disk — now registered in all indexes** |

### Migration Checklist

- [ ] **Copy new skill folder**: `.claude/skills/prd-v04-visual-prototype-gate/` (SKILL.md + assets/ + references/)
- [ ] **Update `.claude/domain-profile.yaml`** — add two entries to `domain:` list:
  - `prd-v04-visual-prototype-gate` (after `prd-v04-user-journey-mapping`)
  - `prd-v06-environment-setup` (after `prd-v06-architecture-design`) — skip if you already have this skill registered
- [ ] **Update `.claude/skills/skills-inventory.md`** — add entries to Quick Nav table, stage overview table, and skill spec section (or copy the file from template)
- [ ] **Update `.claude/agents/studio/AGENT.md`** — add `prd-v04-visual-prototype-gate` to "Skills I Invoke" table at v0.4
- [ ] **Update `.claude/agents/devlab/AGENT.md`** — add `prd-v06-environment-setup` to "Skills I Invoke" table at v0.6
- [ ] **Update `.claude/README.md`** — update skill counts in directory tree comments (v0.4: 3→4, v0.6: 2→3)
- [ ] **Update `.claude/VERSION`** — set to `3.1.0`
- [ ] **Update `template_version`** in CLAUDE.md frontmatter — set to `3.1.0`

### Notes for Repos Already Past v0.4

If your product has already completed v0.4 and advanced to v0.5+, the Visual Prototype Gate skill is **not retroactively required**. It becomes available for:
- Future products using the template
- Iteration cycles where you revisit v0.4 screens based on post-launch feedback
- New features that need visual validation before build

The environment-setup skill (v0.6) is similarly non-breaking — it adds ENV- entries to existing v0.6 workflows.

---

## v2.0.0 → v3.0.0

**Released**: 2026-02-12

### Breaking Changes

These require manual action in derivative repos:

- [ ] **Agents restructured**: flat files → subdirectories
  - `.claude/agents/HORIZON.md` → `.claude/agents/horizon/AGENT.md` + `MEMORY.md`
  - `.claude/agents/STUDIO.md` → `.claude/agents/studio/AGENT.md` + `MEMORY.md`
  - `.claude/agents/DEVLAB.md` → `.claude/agents/devlab/AGENT.md` + `MEMORY.md`
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
- [ ] `.claude/hooks/context-validation.sh` — SessionStart hook
- [ ] `.claude/hooks/context-density-gate.sh` — UserPromptSubmit hook
- [ ] `.claude/hooks/sot-update-trigger.sh` — Stop hook

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
- [ ] Hooks are shell-only (POSIX sh) — no Python dependency needed
- [ ] Drop SoT files that don't map to your domain; create domain-specific ones using `ghm-sot-builder`

---

## v1.0.0 → v2.0.0

**Released**: 2026-01-12

### Changes

- Complete skill library added (26 PRD lifecycle + 5 methodology skills)
- 3 hooks added (context-validation, context-density-gate, sot-update-trigger)
- 4 agent definitions added (HORIZON, STUDIO, DEVLAB, METRO)
- 12 SoT files standardized to ~100-150 lines each
- Methodology renamed to "PRD Led Context Engineering"

### Migration

- [ ] Copy `.claude/skills/` directory from template
- [ ] Copy `.claude/hooks/` directory from template
- [ ] Copy `.claude/agents/` directory from template
- [ ] Update `.claude/settings.json` to wire hooks
- [ ] Standardize SoT file structure to match new template
