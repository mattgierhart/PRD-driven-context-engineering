---
name: ghm-template-sync
description: >
  Detect template version drift and guide migration to the latest template version.
  Compares current repo against the template, identifies what's outdated, and automates
  safe updates while protecting product-specific content.
  Triggers on requests to sync with template, update template version, check for template
  drift, or when user asks "sync template", "update to v3", "template drift", "check template version".
disable-model-invocation: true
context: fork
allowed-tools:
  - Read
  - Write
  - Edit
  - Glob
  - Grep
  - Bash
---

# Template Sync

Detect template version drift and migrate to the latest template version.

## Workflow

### Phase 1: Detect Current State

1. Read `.claude/VERSION` (if it exists) to get current template version
2. If no VERSION file, check `CLAUDE.md` frontmatter for `template_version`
3. If neither exists, assume v1.0.0 (pre-versioning)
4. Report: "Your repo is on template v{X}. Latest is v{Y}."

### Phase 2: Diff Against Template

Compare your repo structure against what the current template version expects:

**Check for missing files:**
- `.claude/VERSION`
- `.claude/domain-profile.yaml`
- `.claude/hooks/HOOK_CONTRACT.md`
- `.claude/hooks/context-validation.sh`
- `.claude/hooks/context-density-gate.sh`
- `CHANGELOG.md`
- `MIGRATION.md`

**Check for stale files (should be removed):**
- `.claude/hooks/context-validation.py`
- `.claude/hooks/context-density-gate.py`
- `.claude/agents/HORIZON.md` (replaced by subdirectory)
- `.claude/agents/STUDIO.md`
- `.claude/agents/DEVLAB.md`
- `.claude/agents/METRO.md`

**Check for structure issues:**
- `settings.json`: Does it use 3-level nesting? Are timeouts in seconds?
- Agent directories: Do `horizon/`, `studio/`, `devlab/`, `metro/` subdirectories exist with `AGENT.md` + `MEMORY.md`?
- EPIC template: Does it use semantic headers (not numbered)?
- Frontmatter: Do key files have `template_version`?

### Phase 3: Generate Migration Plan

Output a table:

| File | Status | Action | Risk |
|------|--------|--------|------|
| `.claude/VERSION` | Missing | Copy from template | None |
| `.claude/hooks/*.py` | Stale | Delete (replaced by .sh) | None |
| `.claude/agents/HORIZON.md` | Stale | Split into horizon/AGENT.md + MEMORY.md | **Preserve MEMORY.md content** |
| `settings.json` | Outdated | Update hook nesting + commands | Check for custom hooks |
| `CLAUDE.md` | Missing frontmatter | Add `template_version: "3.0.0"` | None |

### Phase 4: Execute Safe Updates

**Auto-safe** (do without asking):
- Create `.claude/VERSION` with current template version
- Add `template_version` frontmatter only to framework-owned files that lack it
- Report what was done

**Confirm first** (show diff, ask user):
- Update `settings.json` hook configuration
- Restructure agent files (must preserve MEMORY.md)
- Delete only the obsolete Python hook filenames listed in Phase 2

**Never touch** (product-specific):
- `PRD.md`, including its frontmatter (report version drift; owner edits it explicitly)
- `SoT/*.md` content
- `epics/EPIC-*.md` and `epics/EPIC_TEMPLATE.md` content
- `.claude/agents/*/MEMORY.md` content
- `README.md` content

### Phase 5: Verify

After all changes:
1. Test all shell hooks produce valid JSON
2. Verify none of the obsolete Python hook filenames listed in Phase 2 remain
3. Confirm `settings.json` uses correct nesting
4. Check agent subdirectories have both AGENT.md and MEMORY.md
5. Report summary of changes made

## Version Migration Matrix

| From | To | Key Changes |
|------|----|-------------|
| v1.0.0 | v2.0.0 | Add skills, hooks, agents, SoT standardization |
| v2.0.0 | v3.0.0 | Shell hooks, agent subdirs, semantic EPICs, versioning, domain-profile |
| v1.0.0 | v3.0.0 | All of the above (cumulative) |

## Safety Rules

1. **NEVER overwrite MEMORY.md** -- these contain product-specific agent memory
2. **NEVER modify SoT content or frontmatter** -- report drift and require an explicit owner edit
3. **NEVER modify PRD.md**, including frontmatter -- report drift and require an explicit owner edit
4. **ALWAYS show diff before destructive changes** (deletes, restructures)
5. **ALWAYS verify hooks work** after updating settings.json
6. **Commit changes incrementally** -- one commit per phase, not one giant commit
