# Template Update Brief: v3.2.0

**From**: Template maintainer
**To**: All product repos using PRD-Led Context Engineering
**Date**: 2026-04-01
**Action Required**: Update your repo to template v3.2.0

---

## Why This Update

Claude Code's open-source release (March 2026) revealed how Anthropic's engineers solve the same problems our methodology addresses: context management, session continuity, knowledge persistence, and multi-agent coordination. This release adopts their battle-tested patterns.

### Problems Solved

1. **Agent memories never populated** — the 5-8 table MEMORY.md format was too complex. Agents skipped it every time.
2. **No enforcement before code writes** — agents could write code without an active EPIC or proper traceability.
3. **CLAUDE.md couldn't be customized per-team** — one monolithic file meant derivative repos couldn't swap individual rules.
4. **No cross-EPIC learning** — insights died when EPICs closed. No promotion pipeline to durable knowledge.
5. **No multi-agent coordination in EPICs** — the template assumed single-agent execution despite having 4 specialized agents.
6. **Skill metadata incomplete** — no tool restrictions or execution context, leading to over-permissioned skill runs.

## What Changed

| Area | Before (v3.1) | After (v3.2) |
|------|---------------|--------------|
| **Agent name** | `werk` (Build agent) | `devlab` (renamed everywhere) |
| **MEMORY.md** | 5-8 empty tables | 4 sections: Feedback, Patterns, Decisions, Handoff Notes |
| **Memory extraction** | Passive `systemMessage` reminder | Active `hookSpecificOutput` instruction with current memory injected |
| **Memory sync** | Manual | Git auto-staging + `memory({agent}):` commit convention |
| **CLAUDE.md** | 114-line monolith | ~30-line pointer → `.claude/rules/01-06*.md` (auto-loaded) |
| **Code write enforcement** | None | PreToolUse hook checks for active EPIC |
| **SoT update reminders** | On Stop (too late) | PostToolUse (immediate, per-write) |
| **Cross-session learning** | None | `SoT/SoT.LESSONS_LEARNED.md` with LL-XXX prefix |
| **Staleness tracking** | None | Verified dates with 30/90-day protocol |
| **EPIC coordination** | Single-agent assumed | Multi-agent routing, synthesis checkpoint, self-contained worker prompts |
| **EPIC locking** | None | Active Session field with 2-hour staleness |
| **Phase E harvest** | Temp cleanup only | + Memory harvest (agent memory → SoT promotion) |
| **Skill frontmatter** | name + description only | + `context: fork\|inline` + `allowed-tools` |
| **README** | Product status only | + Squad Status dashboard (agent activity + EPIC tables) |
| **Agent communication** | Implicit | Explicit rule: SoT cross-refs, EPIC observations, session state blockers |

## How to Update

### Quick Path (recommended)

```
/ghm-template-sync
```

### Manual Path

Follow the checklist in `MIGRATION.md` section "v3.1.0 → v3.2.0".

### Priority Order

If you can't do everything at once, prioritize in this order:

1. **Agent rename** (werk → devlab) — blocks everything else
2. **MEMORY.md simplification** — enables the memory system to actually work
3. **New hooks** (traceability-gate + sot-sync-reminder + updated save hook) — immediate enforcement value
4. **Modular rules** — enables per-team customization
5. **SoT.LESSONS_LEARNED.md + staleness** — enables cross-EPIC learning
6. **EPIC template updates** — enables multi-agent coordination
7. **Skill frontmatter** — can be done incrementally

## What NOT to Touch

These files contain your product-specific content:

- `PRD.md` — just update `template_version` in frontmatter
- `SoT/*.md` (except UNIQUE_ID_SYSTEM) — add LL to prefix tables, add staleness protocol
- `epics/EPIC-*.md` — in-flight EPICs can keep old format
- `.claude/agents/*/MEMORY.md` — **migrate content** to new format, don't overwrite (see MIGRATION.md for instructions)
- `README.md` — add Squad Status section, don't overwrite product content

## Key Decisions

**Why rename werk → devlab?** The original intent was always `devlab` as the Build agent. `werk` was a placeholder that persisted. All product repos should rename once.

**Why 4 memory sections, not 8?** Claude Code's own memory system uses 4 types (feedback, project, reference, user). Our 8-table format was never populated — too much friction. The 4-section format maps directly to what actually gets captured.

**Why modular rules?** Claude Code auto-loads `.claude/rules/*.md` files. By extracting CLAUDE.md sections into individual rule files, derivative repos can swap individual rules (e.g., replace coding standards) without forking the whole operating guide.

**Why PreToolUse not just Stop?** The `sot-update-trigger.sh` (Stop event) fires after the session — too late to prevent drift. PreToolUse fires before each write, catching missing EPICs in real-time. PostToolUse fires after each write, reminding about SoT updates while the change is fresh.

## Verification

After updating, run:

```bash
# All hooks produce valid JSON
echo '{}' | bash .claude/hooks/context-validation.sh | python3 -m json.tool
echo '{"tool_input":{"file_path":"src/app.ts"}}' | bash .claude/hooks/traceability-gate.sh | python3 -m json.tool

# No werk references remain
grep -rl "werk" .claude/agents/ .claude/domain-profile.yaml

# Rules loaded
ls .claude/rules/  # 6 files

# Version correct
cat .claude/VERSION  # 3.2.0
```

## Questions?

Open an issue on the template repo or check `MIGRATION.md` for the full checklist.
