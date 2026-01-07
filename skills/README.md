# PRD Skills Library

> **Purpose**: Agent Skills for each stage of the PRD Lifecycle. Skills are loaded on-demand to give agents specialized capabilities for specific tasks.

This library follows the [Agent Skills Specification](https://agentskills.io/specification).

---

## Quick Start

| Need | Go To |
|------|-------|
| **Full skill inventory & specs** | [`INVENTORY.md`](INVENTORY.md) |
| **Create a new skill** | [`SKILL_TEMPLATE/`](SKILL_TEMPLATE/) |
| **v0.1 Problem Framing** | [`prd-v01-problem-framing/`](prd-v01-problem-framing/) |
| **v0.1 User Value Articulation** | [`prd-v01-user-value-articulation/`](prd-v01-user-value-articulation/) |

---

## Current Status

```
skills/
├── README.md                          # This file
├── INVENTORY.md                       # Full inventory with specifications
├── SKILL_TEMPLATE/                    # Template for new skills
│
├── prd-v01-problem-framing/           # ✅ Ready
│   ├── SKILL.md
│   ├── assets/
│   │   └── problem-statement-template.md
│   └── references/
│       ├── examples.md
│       └── research-prompts.md
│
└── prd-v01-user-value-articulation/   # ✅ Ready
    ├── SKILL.md
    ├── assets/
    │   └── value-statement-template.md
    └── references/
        ├── research-prompts.md
        └── transformation-examples.md
```

**Status Legend:**
- ✅ Ready = SKILL.md + references + assets complete
- 📋 Spec = specification in INVENTORY.md, needs implementation

---

## PRD Stage → Skill Mapping

| Stage | Skills | Status |
|-------|--------|--------|
| **v0.1 Spark** | Problem Framing, User Value Articulation | ✅ ✅ |
| **v0.2 Market** | Competitive Landscape, Product Type Classification | 📋 📋 |
| **v0.3 Commercial** | Outcome Definition, Pricing Model, Our Moat, Market Moat, Fast-Follow | 📋 📋 📋 📋 📋 |

See [`INVENTORY.md`](INVENTORY.md) for full specifications of pending skills.

---

## Skill Structure

Each skill follows the standard format:

```
prd-v{XX}-{name}/
├── SKILL.md           # Core instructions (<5000 tokens)
├── references/        # Deep context, loaded on-demand
│   ├── examples.md
│   └── research-prompts.md
├── assets/            # Templates for structured output
│   └── template.md
└── scripts/           # Automation (optional)
```

---

## Creating a New Skill

1. Copy [`SKILL_TEMPLATE/`](SKILL_TEMPLATE/) to `prd-v{XX}-{name}/`
2. Update `SKILL.md` frontmatter:
   ```yaml
   ---
   name: prd-v{XX}-{name}
   description: >
     What this skill does.
     Triggers on [specific phrases].
     Outputs [what it produces].
   ---
   ```
3. Write concise instructions (<500 lines)
4. Add examples to `references/`
5. Add templates to `assets/`
6. Update [`INVENTORY.md`](INVENTORY.md)

**Best Practices** (from agentskills.io):
- Keep `SKILL.md` under 5000 tokens
- Use specific trigger phrases in description
- Keep reference files focused (loaded on-demand)
- Scripts should be self-contained

---

## How Skills Work

**Activation:**
1. Explicit invocation: User requests skill
2. Trigger matching: Description keywords match intent
3. Context awareness: Agent determines relevance

**Execution:**
1. Load `SKILL.md` into context
2. Load `references/` files as needed
3. Use `assets/` templates for output
4. Execute `scripts/` for automation

---

## Integration with PRD Ecosystem

```
README.md (Dashboard)
    ↓
PRD.md (Strategy) ←→ skills/ (Capabilities)
    ↓
epics/ (Execution) ←→ specs/ (Source of Truth)
```

Skills can:
- Reference `specs/SoT.*.md` for business rules
- Output to `epics/` for task tracking
- Create IDs: CFD-, BR-, KPI-, UJ-, API-

---

## Contributing

1. Check [`INVENTORY.md`](INVENTORY.md) for pending skills
2. Follow the skill structure above
3. See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines
