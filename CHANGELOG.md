# Changelog

All notable changes to the PRD-Led Context Engineering template are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/). Template version tracked in `.claude/VERSION`.

---

## [3.1.0] — 2026-03-18

### Added
- `prd-v04-visual-prototype-gate` skill — converts SCR- entries into structured prompts for Google Stitch (or equivalent UI generation tool), captures stakeholder feedback routed back to SoT IDs. Sits between Screen Flow Definition and v0.5 Red Team Review.
- `prd-v06-environment-setup` registered in domain-profile.yaml, skills-inventory.md, and DEVLAB agent (skill existed on disk but was missing from all registries)

### Changed
- `.claude/domain-profile.yaml` — domain skills list updated (24 → 26 entries)
- `.claude/skills/skills-inventory.md` — added Visual Prototype Gate and Environment Setup entries (Quick Nav, stage overview tables, full skill specs)
- `.claude/agents/studio/AGENT.md` — added `prd-v04-visual-prototype-gate` to Skills I Invoke
- `.claude/agents/devlab/AGENT.md` — added `prd-v06-environment-setup` to Skills I Invoke
- `.claude/README.md` — updated v0.4 skill count (3 → 4) and v0.6 skill count (2 → 3)
- Skill count: 26 → 28 PRD lifecycle skills + 5 methodology skills

---

## [3.0.0] — 2026-02-12

### Added
- `.claude/VERSION` — single source of truth for template version
- `CHANGELOG.md` — structural changes documented per version
- `MIGRATION.md` — step-by-step migration guide for derivative repos
- `<!-- SECTION: -->` and `<!-- CUSTOMIZABLE: -->` markers in all template files for merge-friendly syncing
- `.claude/hooks/HOOK_CONTRACT.md` — universal hook interface specification (language-agnostic)
- `.claude/hooks/context-validation.sh` — shell variant of SessionStart hook
- `.claude/hooks/context-density-gate.sh` — shell variant of UserPromptSubmit hook
- `.claude/hooks/sot-update-trigger.sh` — shell variant of Stop hook
- `.claude/domain-profile.yaml` — parameterized ID prefixes, skill taxonomy (core vs domain), agent registry
- Dependency manifests in all hook `.md` documentation files
- `template_version` frontmatter field in CLAUDE.md, PRD.md, README_template.md, EPIC_TEMPLATE.md, SoT.README.md

### Changed
- EPIC template sections: numbered (`## 0. Session State`) → semantic (`## Session State`)
- CLAUDE.md: "Section 0" references → "Session State" semantic references
- ID Ownership in CLAUDE.md now references `domain-profile.yaml` as canonical registry
- `.claude/README.md` updated to reflect actual directory structure (agents, hooks, skills)
- Agent files restructured: flat `.claude/agents/DEVLAB.md` → `.claude/agents/devlab/AGENT.md` + `MEMORY.md`

### Breaking
- Agent paths changed: `agents/{NAME}.md` → `agents/{name}/AGENT.md` + `agents/{name}/MEMORY.md`
- EPIC section headers no longer numbered — scripts referencing "Section 0" must update to "Session State"
- See `MIGRATION.md` for complete derivative update checklist

---

## [2.0.0] — 2026-01-12

### Added
- Complete skill library: 26 PRD lifecycle skills (v0.1–v0.9) + 5 methodology skills (ghm-*) (note: count updated to 28 in v3.1.0)
- Skill-per-directory structure with SKILL.md + assets/ + references/
- 3 hooks: context-validation, context-density-gate, sot-update-trigger
- Hook .md documentation paired with each script
- 4 agent definitions: HORIZON, STUDIO, DEVLAB, METRO
- 12 SoT files standardized to ~100-150 lines each
- EPIC template with 5-phase execution model
- Progressive documentation protocol in CLAUDE.md
- README_template.md for derivative repos

### Changed
- Standardized SoT files to consistent structure with YAML frontmatter
- Methodology renamed to "PRD Led Context Engineering"

---

## [1.0.0] — 2025-12-22

### Added
- Initial template structure
- CLAUDE.md agent operating guide
- PRD.md progressive requirements template
- SoT directory with ID-based knowledge graph
- EPIC template for execution planning
- README.md methodology explainer
