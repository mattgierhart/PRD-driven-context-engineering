# Migration Guide

This document helps derivative repos sync with template changes. Each version section includes a checklist of required actions.

> **Tip**: Check `.claude/VERSION` in this template to see the current version, and compare it with the `template_version` field in your repo's CLAUDE.md frontmatter to determine your starting point.

---

## v3.1.0 → v3.2.0

**Released**: 2026-04-01

### What Changed

Major improvements to memory system, multi-agent coordination, and enforcement hooks based on patterns from Claude Code's source code. **One breaking rename: `werk` → `devlab`.**

### Migration Checklist

#### Breaking: Agent Rename (werk → devlab)

- [ ] **Rename agent directory**: `.claude/agents/werk/` → `.claude/agents/devlab/`
- [ ] **Update AGENT.md**: Replace all `werk`/`Werk`/`WERK` with `devlab`/`DevLab`/`DEVLAB` in `.claude/agents/devlab/AGENT.md`
- [ ] **Update other AGENT.md files**: horizon, studio, metro AGENT.md files reference `WERK` in handoff contracts — change to `DEVLAB`
- [ ] **Update domain-profile.yaml**: agent registry entry name and path
- [ ] **Update EPIC files**: any in-flight EPIC with `Epic Lead: werk` → `devlab`
- [ ] **Update custom scripts/hooks**: anything that references `werk` agent type

#### Breaking: CLAUDE.md → Modular Rules

- [ ] **Create `.claude/rules/` directory** and copy 6 rule files from template:
  - `01-session-protocols.md`
  - `02-document-ecosystem.md`
  - `03-documentation-discipline.md`
  - `04-coding-standards.md`
  - `05-lifecycle-gates.md`
  - `06-cross-agent-communication.md`
- [ ] **Update CLAUDE.md** — slim to pointer format (copy from template). Your product-specific CLAUDE.md customizations should move to a rule file or `CLAUDE.local.md`
- [ ] **Add `CLAUDE.local.md` to `.gitignore`** — for per-developer overrides

#### New: Memory System Overhaul

- [ ] **Simplify MEMORY.md** for each agent — replace old tables with 4-section format (copy from template). **Important**: If you have populated MEMORY.md content, migrate entries into the new sections:
  - Old "Patterns Learned" → new "Patterns"
  - Old "Key Decisions" → new "Decisions"
  - Old "Collaboration Notes" / "Handoff Friction" → new "Handoff Notes"
  - Old "Open Questions" → new "Feedback" (if corrections) or discard
- [ ] **Create MEMORY_ARCHIVE.md** for each agent — copy empty template from template repo
- [ ] **Copy `SoT/SoT.LESSONS_LEARNED.md`** from template
- [ ] **Add LL prefix to `domain-profile.yaml`**: `LL: { file: "SoT/SoT.LESSONS_LEARNED.md", description: "Lessons learned" }`
- [ ] **Add LL to `SoT/SoT.UNIQUE_ID_SYSTEM.md`** — prefix tables + file registry
- [ ] **Add staleness protocol** to `SoT/SoT.UNIQUE_ID_SYSTEM.md` (copy section 1.5 from template)
- [ ] **Update `SoT/SoT.README.md`** — add LESSONS_LEARNED to index table

#### New: Hooks

- [ ] **Copy new hook scripts**:
  - `.claude/hooks/traceability-gate.sh` (PreToolUse: Write|Edit)
  - `.claude/hooks/sot-sync-reminder.sh` (PostToolUse: Write|Edit)
- [ ] **Update `.claude/hooks/subagent-memory-save.sh`** — copy from template (upgraded to `hookSpecificOutput` + git auto-staging)
- [ ] **Update `.claude/settings.json`** — add PreToolUse and PostToolUse entries (copy from template)
- [ ] **Update `.claude/hooks/HOOK_CONTRACT.md`** — copy from template (new hooks + git conventions)

#### New: EPIC Template Enhancements

- [ ] **Update `epics/EPIC_TEMPLATE.md`** — copy from template. New features:
  - Agents + Coordination Mode fields in header
  - Agent Routing table in Phase A
  - Synthesis Checkpoint between Phase A and B
  - Agent assignment per Context Window in Phase C
  - Memory Harvest step in Phase E
  - Active Session lock field in Session State
- [ ] **In-flight EPICs**: Add `Active Session: none` to Session State section if desired; other new fields are optional for existing EPICs

#### New: Skill Frontmatter

- [ ] **Update all SKILL.md files** — add `context: fork|inline` and `allowed-tools:` fields. Copy individual files from template, or run:
  ```
  /ghm-template-sync
  ```

#### New: README Squad Dashboard

- [ ] **Add Squad Status section to README.md** — copy the `<!-- SECTION: squad-status -->` block from template README.md and place it after your Repository Structure section

#### Housekeeping

- [ ] **Update `.claude/VERSION`** — set to `3.2.0`
- [ ] **Update `template_version`** — set to `3.2.0` in CLAUDE.md and EPIC_TEMPLATE.md frontmatter
- [ ] **Update `context-validation.sh`** — copy from template (adds session lock checking with Python date math fallback)

### Notes for Repos with Populated Agent Memories

If your agents have accumulated MEMORY.md content from real usage, **do not blindly overwrite**. Instead:
1. Read your existing entries
2. Categorize each into: Feedback, Patterns, Decisions, or Handoff Notes
3. Write them into the new 4-section format
4. Any entries with 3+ occurrences should also go into `SoT/SoT.LESSONS_LEARNED.md` as LL-XXX

### Verification

```bash
# All hooks produce valid JSON
echo '{}' | bash .claude/hooks/context-validation.sh | python3 -m json.tool
echo '{"agent_type":"horizon"}' | bash .claude/hooks/subagent-memory-save.sh | python3 -m json.tool
echo '{"tool_input":{"file_path":"src/app.ts"}}' | bash .claude/hooks/traceability-gate.sh | python3 -m json.tool
echo '{"tool_input":{"file_path":"src/app.ts"}}' | bash .claude/hooks/sot-sync-reminder.sh | python3 -m json.tool

# Settings valid
python3 -m json.tool .claude/settings.json > /dev/null && echo "OK"

# No remaining werk references
grep -rl "werk" .claude/agents/ .claude/domain-profile.yaml  # should be empty

# Rules exist
ls .claude/rules/  # should show 6 files

# Version correct
cat .claude/VERSION  # should show 3.2.0
```

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
