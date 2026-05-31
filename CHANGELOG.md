# Changelog

All notable changes to the PRD-Led Context Engineering template are documented in this file.

Format follows [Keep a Changelog](https://keepachangelog.com/). Template version tracked in `.claude/VERSION`.

---

## [3.2.0] — 2026-04-01

### Added
- `.claude/rules/` directory with 6 modular rule files (01-session-protocols through 06-cross-agent-communication) — auto-loaded by Claude Code via `alwaysApply: true` frontmatter
- `SoT/SoT.LESSONS_LEARNED.md` — new SoT file with LL-XXX prefix for cross-session behavioral corrections and validated patterns
- Staleness protocol in `SoT/SoT.UNIQUE_ID_SYSTEM.md` — <30d current, 30-90d review, >90d verify before use
- `MEMORY_ARCHIVE.md` for all 4 agents — stores entries promoted to SoT during Phase E harvest
- `.claude/hooks/traceability-gate.sh` — PreToolUse hook (Write|Edit) verifies active EPIC before source code writes
- `.claude/hooks/sot-sync-reminder.sh` — PostToolUse hook (Write|Edit) reminds agent to update SoT after code writes
- EPIC template: coordinator pattern (multi-agent routing table, synthesis checkpoint, self-contained worker prompts)
- EPIC template: memory harvest step in Phase E (agent memory → SoT.LESSONS_LEARNED.md)
- EPIC template: session ownership/locking with Active Session field (2-hour staleness threshold)
- Squad Status dashboard in README.md (agent activity + EPIC status tables)
- Cross-agent communication protocol rule (file-based async via SoT cross-references, EPIC observations, session state blockers)
- Git-based memory sync: `subagent-memory-save.sh` auto-stages MEMORY.md changes; commit convention `memory({agent}): {summary}`
- `context` and `allowed-tools` frontmatter fields added to all 33 skills
- `CLAUDE.local.md` added to `.gitignore` for per-developer overrides
- Context loading order documented as intentional cache architecture (stable→volatile for prompt cache efficiency)

### Changed
- **Agent renamed**: `werk` → `devlab` across all files (AGENT.md, domain-profile.yaml, CHANGELOG, MIGRATION, all cross-references in horizon/studio/metro AGENT.md files)
- Agent MEMORY.md simplified from 5-8 complex tables → 4 sections (Feedback, Patterns, Decisions, Handoff Notes) — prior format was never populated
- `subagent-memory-save.sh` upgraded from passive `systemMessage` → active `hookSpecificOutput` with `additionalContext` (matches load hook pattern)
- CLAUDE.md slimmed from 114 lines → ~30 lines (pointer to `.claude/rules/`)
- `settings.json` expanded from 5 hook events → 7 (added PreToolUse, PostToolUse)
- HOOK_CONTRACT.md updated with new hooks inventory, git commit conventions, Python dependency note
- `domain-profile.yaml` — added LL prefix, agent registry updated (werk → devlab)

### Breaking
- **Agent `werk` removed** — renamed to `devlab`. Repos referencing `werk` in EPIC leads, agent routing, or custom hooks must update to `devlab`
- **CLAUDE.md content moved** — rules now in `.claude/rules/*.md`. CLAUDE.md is a pointer only. Repos that grep CLAUDE.md for rule content must update to search `.claude/rules/`
- **MEMORY.md format changed** — old tables replaced with 4-section format. Repos with populated MEMORY.md files should migrate content into the new sections
- **settings.json schema expanded** — PreToolUse and PostToolUse entries added. Repos using `/localize` must re-sync settings.json

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
