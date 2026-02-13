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
│   ├── prd-v04-*/              # v0.4 Journeys: Personas & Flows (3 skills)
│   ├── prd-v05-*/              # v0.5 Red Team: Risks & Tech Stack (2 skills)
│   ├── prd-v06-*/              # v0.6 Architecture: Design & Specs (2 skills)
│   ├── prd-v07-*/              # v0.7 Build: Implementation (3 skills)
│   ├── prd-v08-*/              # v0.8 Release: Deployment & Ops (3 skills)
│   ├── prd-v09-*/              # v0.9 Launch: GTM & Metrics (3 skills)
│   ├── ghm-status-sync/        # Methodology: Sync README dashboard
│   ├── ghm-id-register/        # Methodology: Validate & register SoT IDs
│   ├── ghm-gate-check/         # Methodology: Validate gate criteria
│   ├── ghm-sot-builder/        # Methodology: Create new SoT files
│   └── ghm-harvest/            # Methodology: Extract temps to SoT
├── hooks/                      # Event-triggered automation
│   ├── HOOK_CONTRACT.md        # Universal hook interface specification
│   ├── context-validation.py   # SessionStart: Load 3+1 files (Python)
│   ├── context-validation.sh   # SessionStart: Load 3+1 files (Shell)
│   ├── context-validation.md   # Documentation
│   ├── context-density-gate.py # UserPromptSubmit: Epic/gate assessment (Python)
│   ├── context-density-gate.sh # UserPromptSubmit: Epic/gate assessment (Shell)
│   ├── context-density-gate.md # Documentation
│   ├── sot-update-trigger.py   # Stop: SoT update reminder (Python)
│   ├── sot-update-trigger.sh   # Stop: SoT update reminder (Shell)
│   └── sot-update-trigger.md   # Documentation
├── agents/                     # Agent definitions (subdirectories)
│   ├── horizon/                # Strategy Agent (v0.1-v0.5)
│   │   ├── AGENT.md            # Identity, responsibilities, skills
│   │   └── MEMORY.md           # Project memory (RESET ON FORK)
│   ├── studio/                 # Design Agent (v0.3-v0.6)
│   │   ├── AGENT.md
│   │   └── MEMORY.md
│   ├── werk/                   # Build Agent (v0.6-v0.8)
│   │   ├── AGENT.md
│   │   └── MEMORY.md
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

| Hook | Trigger | Python | Shell | Purpose |
|------|---------|--------|-------|---------|
| Context Validation | SessionStart | `context-validation.py` | `context-validation.sh` | Inject 3+1 file reading order |
| Context Density Gate | UserPromptSubmit | `context-density-gate.py` | `context-density-gate.sh` | Assess epic/gate context readiness |
| SoT Update Trigger | Stop | `sot-update-trigger.py` | `sot-update-trigger.sh` | Remind about spec updates |

**Default**: `settings.json` uses Python. To use Shell instead, change `python3 ... .py` to `bash ... .sh` in `settings.json`.

### Hook Execution Order

**SessionStart**: `context-validation` runs first, injecting reading order.

**UserPromptSubmit**: `context-density-gate` runs only when prompt matches epic/gate patterns.

**Stop**: `sot-update-trigger` runs, reminding about SoT updates.
<!-- /SECTION: hooks-table -->

<!-- SECTION: agents-table -->
## Agents

Four primary agents form the AI team. Each agent has an `AGENT.md` (identity + skills) and `MEMORY.md` (project-specific memory, reset on fork):

| Agent | Directory | Role | Lifecycle |
|-------|-----------|------|-----------|
| **HORIZON** | `agents/horizon/` | Strategy | v0.1-v0.5 |
| **STUDIO** | `agents/studio/` | Design | v0.3-v0.6 |
| **WERK** | `agents/werk/` | Build | v0.6-v0.8 |
| **METRO** | `agents/metro/` | Ops | v0.9-v1.0 |

See [`.claude/domain-profile.yaml`](domain-profile.yaml) for the full agent registry and skill taxonomy (core vs domain).
<!-- /SECTION: agents-table -->

## Reference

- [Claude Code Skills](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/skills)
- [Claude Code Hooks](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/hooks)
