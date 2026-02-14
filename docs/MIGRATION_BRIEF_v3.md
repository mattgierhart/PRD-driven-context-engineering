# Template Update Brief: v3.0.0

**From**: Template maintainer
**To**: All product repos using PRD-Led Context Engineering
**Date**: 2026-02-13
**Action Required**: Update your repo to template v3.0.0

---

## Why This Update

Six derivative repo sync experiences surfaced recurring pain points that v3.0.0 addresses:

1. **No version tracking** -- you couldn't tell which template version you were on
2. **Merge conflicts on every sync** -- no way to separate "template core" from "your customizations"
3. **Python dependency for hooks** -- unnecessary for what the hooks actually do
4. **Agent files mixed concerns** -- project memory got overwritten on template sync
5. **EPIC numbering broke on section reorder** -- numbered headers caused drift
6. **No hook contract** -- unclear what hooks receive and must output

## What Changed

| Area | Before (v2) | After (v3) |
|------|-------------|------------|
| **Versioning** | None | `.claude/VERSION` + `template_version` frontmatter |
| **Hooks** | Python only | POSIX shell only (zero dependencies) |
| **Hook config** | Flat JSON | Anthropic-compliant 3-level nesting |
| **Agents** | Single flat files | `AGENT.md` + `MEMORY.md` subdirectories |
| **EPIC sections** | Numbered (`## 0.`) | Semantic (`## Session State`) |
| **Merge tooling** | None | `<!-- SECTION: -->` markers for surgical merges |
| **Domain separation** | Hardcoded | `domain-profile.yaml` parameterizes everything |
| **Hook contract** | Implicit | `HOOK_CONTRACT.md` with full Anthropic compliance |

## How to Update

### Quick Path (recommended)

Run this in your product repo:

```
/ghm-template-sync
```

This custom command will detect your current version, show you what needs to change, and automate the safe parts.

### Manual Path

If you prefer to do it manually, follow the checklist in `MIGRATION.md` (copy it from the template first).

### Step-by-Step Summary

**1. Safe to copy directly** (no product-specific content):

```bash
# From the template repo, copy these files into your repo:
.claude/VERSION
.claude/hooks/HOOK_CONTRACT.md
.claude/hooks/context-validation.sh
.claude/hooks/context-density-gate.sh
.claude/hooks/sot-update-trigger.sh
.claude/domain-profile.yaml
.claude/skills/ghm-template-sync/    # the new sync command itself
CHANGELOG.md                          # then customize with your history
MIGRATION.md
```

**2. Restructure agents** (preserve your MEMORY.md content):

```
# For each agent (horizon, studio, werk, metro):
mkdir -p .claude/agents/horizon/
# Copy AGENT.md from template (identity + skills - these are template-owned)
# Keep YOUR MEMORY.md content (project-specific memory)
# Delete the old flat file: .claude/agents/HORIZON.md
```

**3. Update settings.json** to use shell hooks with correct nesting:

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash \"$CLAUDE_PROJECT_DIR\"/.claude/hooks/context-validation.sh",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

**4. Update EPIC headers** (in-flight EPICs can wait):

- `## 0. Session State` --> `## Session State`
- `## 1. Objective & Scope` --> `## Objective & Scope`
- Same for sections 2, 3, 4

**5. Add frontmatter version** to your files:

```yaml
---
template_version: "3.0.0"
---
```

Add to: `CLAUDE.md`, `PRD.md`, `EPIC_TEMPLATE.md`, `SoT/SoT.README.md`

**6. Delete Python hooks** (replaced by shell):

```bash
rm .claude/hooks/context-validation.py
rm .claude/hooks/context-density-gate.py
rm .claude/hooks/sot-update-trigger.py
```

## What NOT to Touch

These files contain your product-specific content. The template update should not overwrite them:

- `PRD.md` (your product requirements -- just add the frontmatter version)
- `SoT/*.md` (your specs -- just add section markers if you want merge tooling)
- `epics/EPIC-*.md` (your in-flight work -- update headers when you close them)
- `.claude/agents/*/MEMORY.md` (your project memory -- preserve as-is)
- `README.md` (your dashboard -- just add section markers)

## Verification

After updating, run these checks:

```bash
# Hooks produce valid JSON
echo '{}' | bash .claude/hooks/context-validation.sh | python3 -m json.tool
echo '{"prompt": "test"}' | bash .claude/hooks/context-density-gate.sh
echo '{}' | bash .claude/hooks/sot-update-trigger.sh

# No Python hooks remain
ls .claude/hooks/*.py  # should be empty

# Version is set
cat .claude/VERSION  # should show 3.0.0
```

## Questions?

Open an issue on the template repo or check `MIGRATION.md` for the full checklist.
