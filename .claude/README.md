# .claude Directory

This directory contains Claude Code configuration following Anthropic's official structure.

<!-- SECTION: directory-tree -->
## Structure

```text
.claude/
├── domain-profile.yaml         # ID prefix registry, skill taxonomy, agent registry
├── VERSION                     # Template version (semver)
├── skills/                     # PRD lifecycle + methodology skills
│   ├── SKILL_TEMPLATE/         # Template for creating new skills
│   ├── prd-v01-*/              # v0.1 Spark: Problem & Value (2 skills)
│   ├── prd-v02-*/              # v0.2 Market: Segments & Classification (2 skills)
│   ├── prd-v03-*/              # v0.3 Commercial: Features, Moat, Pricing (4 skills)
│   ├── prd-v04-*/              # v0.4 Journeys: Personas, Flows & Prototype (4 skills)
│   ├── prd-v05-*/              # v0.5 Red Team: Risks & Tech Stack (2 skills)
│   ├── prd-v06-*/              # v0.6 Architecture: Design, Specs & Environment (3 skills)
│   ├── prd-v07-*/              # v0.7 Build: Implementation (3 skills)
│   ├── prd-v08-*/              # v0.8 Release: Deployment & Ops (3 skills)
│   ├── prd-v09-*/              # v0.9 Launch: GTM & Metrics (3 skills)
│   ├── ghm-status-sync/        # Methodology: Sync README dashboard
│   ├── ghm-id-register/        # Methodology: Validate & register SoT IDs
│   ├── ghm-gate-check/         # Methodology: Validate gate criteria
│   ├── ghm-sot-builder/        # Methodology: Create new SoT files
│   └── ghm-harvest/            # Methodology: Extract temps to SoT
├── rules/                      # Modular rule files (auto-loaded via alwaysApply)
│   ├── 01-session-protocols.md
│   ├── 02-document-ecosystem.md
│   ├── 03-documentation-discipline.md
│   ├── 04-coding-standards.md
│   ├── 05-lifecycle-gates.md
│   └── 06-cross-agent-communication.md
├── hooks/                      # Event-triggered automation
│   ├── HOOK_CONTRACT.md        # Universal hook interface specification
│   ├── context-validation.sh   # SessionStart: Load 3+1 files + session lock check
│   ├── context-density-gate.sh # UserPromptSubmit: Epic/gate assessment
│   ├── sot-update-trigger.sh   # Stop: SoT update reminder
│   ├── subagent-memory-load.sh # SubagentStart: Inject agent MEMORY.md
│   ├── subagent-memory-save.sh # SubagentStop: Active memory extraction + git staging
│   ├── traceability-gate.sh    # PreToolUse (Write|Edit): Verify active EPIC
│   └── sot-sync-reminder.sh    # PostToolUse (Write|Edit): SoT update reminder
├── agents/                     # Agent definitions (subdirectories)
│   ├── horizon/                # Strategy Agent (v0.1-v0.5)
│   │   ├── AGENT.md            # Identity, responsibilities, skills
│   │   └── MEMORY.md           # Project memory (RESET ON FORK)
│   ├── studio/                 # Design Agent (v0.3-v0.6)
│   │   ├── AGENT.md
│   │   ├── MEMORY.md
│   │   └── MEMORY_ARCHIVE.md
│   ├── devlab/                 # Build Agent (v0.6-v0.8)
│   │   ├── AGENT.md
│   │   ├── MEMORY.md
│   │   └── MEMORY_ARCHIVE.md
│   └── metro/                  # Ops Agent (v0.9-v1.0)
│       ├── AGENT.md
│       └── MEMORY.md
├── settings.json               # Hook configuration
└── settings.local.json         # Local permissions (gitignored)
```
<!-- /SECTION: directory-tree -->

## Skills

Skills are specialized knowledge sets invoked via `/skill-name`.

### Naming Convention

| Prefix | Type | Example | When Used |
|--------|------|---------|-----------|
| `prd-v{XX}-` | PRD Lifecycle | `/prd-v01-problem-framing` | At specific PRD stage |
| `ghm-` | Methodology | `/ghm-gate-check` | Anytime (workflow ops) |

### Skill Structure

```text
skills/prd-v01-problem-framing/
├── SKILL.md                    # Skill definition with prompts
├── assets/                     # Templates for outputs
│   └── problem-statement-template.md
└── references/                 # Supporting documentation
    ├── examples.md
    └── research-prompts.md
```

<!-- SECTION: hooks-table -->
## Hooks

Hooks are event-triggered automation. Configured in `settings.json`, documented in `hooks/`. See [HOOK_CONTRACT.md](hooks/HOOK_CONTRACT.md) for the universal interface specification.

| Hook | Trigger | Script | Purpose |
|------|---------|--------|---------|
| Context Validation | SessionStart | `context-validation.sh` | Inject 3+1 file reading order + session lock check |
| Context Density Gate | UserPromptSubmit | `context-density-gate.sh` | Assess epic/gate context readiness |
| Traceability Gate | PreToolUse (Write\|Edit) | `traceability-gate.sh` | Verify active EPIC before source code writes |
| SoT Sync Reminder | PostToolUse (Write\|Edit) | `sot-sync-reminder.sh` | Remind to update SoT after source code writes |
| SoT Update Trigger | Stop | `sot-update-trigger.sh` | Remind about spec updates |
| Subagent Memory Load | SubagentStart | `subagent-memory-load.sh` | Inject agent MEMORY.md into subagent context |
| Subagent Memory Save | SubagentStop | `subagent-memory-save.sh` | Active memory extraction + git auto-staging |

All hooks are POSIX shell scripts. Python is used optionally for date math in `context-validation.sh` (graceful fallback if unavailable).
<!-- /SECTION: hooks-table -->

<!-- SECTION: agents-table -->
## Agents

Four primary agents form the AI team. Each agent has an `AGENT.md` (identity + skills) and `MEMORY.md` (project-specific memory, reset on fork):

| Agent | Directory | Role | Lifecycle |
|-------|-----------|------|-----------|
| **HORIZON** | `agents/horizon/` | Strategy | v0.1-v0.5 |
| **STUDIO** | `agents/studio/` | Design | v0.3-v0.6 |
| **DEVLAB** | `agents/devlab/` | Build | v0.6-v0.8 |
| **METRO** | `agents/metro/` | Ops | v0.9-v1.0 |

See [`.claude/domain-profile.yaml`](domain-profile.yaml) for the full agent registry and skill taxonomy (core vs domain).
<!-- /SECTION: agents-table -->

## Reference

- [Claude Code Skills](https://code.claude.com/docs/en/skills)
- [Claude Code Hooks](https://code.claude.com/docs/en/hooks)
- [Claude Code Sub-agents](https://code.claude.com/docs/en/sub-agents)
