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

Four agents form the AI team. But here's the insight that changes how you think about them:

> **Core Insight**: Agents are better thought of not as roles on your team, but as **rooms where work is done**. The sticky notes on the wall, the diary, the artifacts created—all of these are forms of memory that agents build over time. An agent's core identity doesn't come from their instructions; it comes from their **progressive memory** throughout the lifespan of development.

When you walk into WERK's room, you see architecture decisions pinned to the wall (ARC-), API contracts on the desk (API-), and a notebook of "things I tried that didn't work" in the drawer. That's not decoration—that's what makes WERK effective at building software.

### What's In Each Room

Each agent file (`.claude/agents/*.md`) defines the room:

| What You See | What It Represents | Example |
|--------------|-------------------|---------|
| **The walls** | IDs they own—the structured facts | API-, DBT-, ARC- pinned up in WERK's room |
| **The desk** | Context they need loaded to work | PRD v0.5+, current EPIC open and ready |
| **The drawers** | Patterns learned across sessions | "Supabase RLS needs explicit policies" |
| **The trash** | Ephemeral data that doesn't persist | Build logs, debug sessions, scratch notes |
| **The diary** | Project Memory—what happened, what worked | Decisions made, friction encountered, questions open |

### The Four Rooms

| Agent | Their Room | What's On The Walls | What They Write In The Diary |
|-------|------------|---------------------|------------------------------|
| **HORIZON** | Market strategy workshop | BR-, UJ-, PER-, KPI-, RISK-, CFD- | ICP signals that predicted success, pricing experiments, research shortcuts |
| **STUDIO** | Design studio | DES-, SCR-, DS- | Usability gotchas, components that transferred between projects, platform quirks |
| **WERK** | Build lab | API-, DBT-, ARC-, TECH-, TEST-, EPIC-, DEP-, RUN- | Implementation patterns, "why we didn't" decisions, architecture regrets |
| **METRO** | Launch command center | GTM-, MON-, contributes CFD- | Channel effectiveness, messaging that landed, adoption blockers discovered |

### House Rules vs. Room Contents

| Where | What Lives There | Nature |
|-------|------------------|--------|
| **CLAUDE.md** | Structural discipline, documentation standards, the rules of the house | Universal—everyone follows these |
| **Agent .md** | Identity, ID ownership, learning patterns, project memory | Unique—each room has its own contents |

CLAUDE.md tells you how to behave in this house.
Agent files tell you what's in each room.

### Compounding Mechanism

Here's where memory becomes infrastructure that **compounds**.

After each work session, agents capture what they learned:
- What pattern did I discover that should be reused?
- What mistake did I make that can be prevented?
- What decision was made and why?

When a pattern shows up three times, it gets **harvested**—promoted from personal memory to shared infrastructure:
- → **CLAUDE.md** if it's universal discipline
- → **Skills** if it's stage-specific wisdom
- → **Agent file** if it's domain-specific expertise

Each session adds to the walls. Each pattern makes the next session easier. The rooms get richer. The work gets faster.

This is compound context engineering.

> **Inspiration**: The compounding mechanism draws from [Every's Compound Engineering Plugin](https://github.com/EveryInc/compound-engineering-plugin), which pioneered the Plan → Work → Review → Compound loop for AI-assisted development. We've adapted their insight—that each unit of work should make future work easier—into our memory-as-infrastructure model.

## Reference

- [Claude Code Skills](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/skills)
- [Claude Code Hooks](https://docs.anthropic.com/en/docs/agents-and-tools/claude-code/hooks)
