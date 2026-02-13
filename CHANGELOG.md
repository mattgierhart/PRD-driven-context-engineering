# Changelog

All notable changes to the PRD-Led Context Engineering template are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/). Template version tracked in `.claude/VERSION`.

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
- Agent files restructured: flat `.claude/agents/WERK.md` → `.claude/agents/werk/AGENT.md` + `MEMORY.md`

### Breaking
- Agent paths changed: `agents/{NAME}.md` → `agents/{name}/AGENT.md` + `agents/{name}/MEMORY.md`
- EPIC section headers no longer numbered — scripts referencing "Section 0" must update to "Session State"
- See `MIGRATION.md` for complete derivative update checklist

---

## [2.0.0] — 2026-01-12

### Added
- Complete skill library: 26 PRD lifecycle skills (v0.1–v0.9) + 5 methodology skills (ghm-*)
- Skill-per-directory structure with SKILL.md + assets/ + references/
- 3 Python hooks: context-validation, context-density-gate, sot-update-trigger
- Hook .md documentation paired with each .py file
- 4 agent definitions: HORIZON, STUDIO, WERK, METRO
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
