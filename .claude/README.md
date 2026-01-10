# .claude Directory

This directory contains Claude Code configuration following Anthropic's official structure.

## Structure

```text
.claude/
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
│   └── ghm-harvest/            # Methodology: Extract temps to SoT
├── hooks/                      # Event-triggered automation
│   ├── context-validation.py   # SessionStart: Load 3+1 files
│   ├── context-validation.md   # Documentation
│   ├── context-density-gate.py # UserPromptSubmit: Epic/gate assessment
│   ├── context-density-gate.md # Documentation
│   ├── sot-update-trigger.py   # Stop: SoT update reminder
│   └── sot-update-trigger.md   # Documentation
├── agents/                     # Agent definitions (flat files only)
│   ├── HORIZON.md              # Strategy Agent (v0.1-v0.5)
│   ├── STUDIO.md               # Design Agent (v0.3-v0.6)
│   ├── WERK.md                 # Build Agent (v0.6-v0.8)
│   └── METRO.md                # Ops Agent (v0.9-v1.0)
├── settings.json               # Hook configuration
└── settings.local.json         # Local permissions (gitignored)
```

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

## Hooks

Hooks are event-triggered automation. Configured in `settings.json`, documented in `hooks/`.

| Hook                 | Trigger          | File                      | Purpose                            |
| -------------------- | ---------------- | ------------------------- | ---------------------------------- |
| Context Validation   | SessionStart     | `context-validation.py`   | Inject 3+1 file reading order      |
| Context Density Gate | UserPromptSubmit | `context-density-gate.py` | Assess epic/gate context readiness |
| SoT Update Trigger   | Stop             | `sot-update-trigger.py`   | Remind about spec updates          |

### Hook Execution Order

**SessionStart**: `context-validation.py` runs first, injecting reading order.

**UserPromptSubmit**: `context-density-gate.py` runs only when prompt matches epic/gate patterns.

**Stop**: `sot-update-trigger.py` runs, reminding about SoT updates.

## Agents

Four primary agents form the AI team, each with embedded project memory:

| Agent | Role | Focus |
|-------|------|-------|
| **HORIZON** | Strategy | Research, market analysis, PRD development (v0.1-v0.5) |
| **STUDIO** | Design | User journeys, wireframes, design systems (v0.3-v0.6) |
| **WERK** | Build | Implementation, testing, deployment (v0.6-v0.8) |
| **METRO** | Ops | Go-to-market, metrics, feedback (v0.9-v1.0) |

## Reference

- [Claude Code Skills](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/skills)
- [Claude Code Hooks](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/hooks)
