# PRD Skills Library

> **Purpose**: Agent Skills for each stage of the PRD Lifecycle. Skills are loaded on-demand to give agents specialized capabilities for specific tasks.

This library follows the [Agent Skills Specification](https://agentskills.io/specification).

---

## Quick Start

| Need | Go To |
|------|-------|
| **Full skill inventory & specs** | [`skills-inventory.md`](skills-inventory.md) |
| **Create a new skill** | [`SKILL_TEMPLATE/`](SKILL_TEMPLATE/) |
| **v0.1 Problem Framing** | [`prd-v01-problem-framing/`](prd-v01-problem-framing/) |
| **v0.1 User Value Articulation** | [`prd-v01-user-value-articulation/`](prd-v01-user-value-articulation/) |
| **v0.2 Competitive Landscape** | [`prd-v02-competitive-landscape-mapping/`](prd-v02-competitive-landscape-mapping/) |
| **v0.2 Product Type** | [`prd-v02-product-type-classification/`](prd-v02-product-type-classification/) |
| **v0.3 Outcome Definition** | [`prd-v03-outcome-definition/`](prd-v03-outcome-definition/) |
| **v0.3 Pricing Model** | [`prd-v03-pricing-model/`](prd-v03-pricing-model/) |
| **v0.3 Moat Definition** | [`prd-v03-moat-definition/`](prd-v03-moat-definition/) |
| **v0.3 Feature Value Planning** | [`prd-v03-features-value-planning/`](prd-v03-features-value-planning/) |

---

## Current Status

```
skills/
├── README.md                              # This file
├── skills-inventory.md                    # Full inventory with specifications
├── SKILL_TEMPLATE/                        # Template for new skills
│
├── prd-v01-problem-framing/               # v0.1 Spark
├── prd-v01-user-value-articulation/       # v0.1 Spark
├── prd-v02-competitive-landscape-mapping/ # v0.2 Market
├── prd-v02-product-type-classification/   # v0.2 Market
├── prd-v03-outcome-definition/            # v0.3 Commercial
├── prd-v03-pricing-model/                 # v0.3 Commercial
├── prd-v03-moat-definition/               # v0.3 Commercial
├── prd-v03-features-value-planning/       # v0.3 Commercial
├── prd-v04-persona-definition/            # v0.4 Journeys
├── prd-v04-user-journey-mapping/          # v0.4 Journeys
├── prd-v04-screen-flow-definition/        # v0.4 Journeys
├── prd-v05-risk-discovery-interview/      # v0.5 Red Team
├── prd-v05-technical-stack-selection/     # v0.5 Red Team
├── prd-v06-architecture-design/           # v0.6 Architecture
├── prd-v06-technical-specification/       # v0.6 Architecture
├── prd-v07-epic-scoping/                  # v0.7 Build
├── prd-v07-test-planning/                 # v0.7 Build
├── prd-v07-implementation-loop/           # v0.7 Build
├── prd-v08-release-planning/              # v0.8 Release
├── prd-v08-runbook-creation/              # v0.8 Release
├── prd-v08-monitoring-setup/              # v0.8 Release
├── prd-v09-gtm-strategy/                  # v0.9 Launch
├── prd-v09-launch-metrics/                # v0.9 Launch
├── prd-v09-feedback-loop-setup/           # v0.9 Launch
├── ghm-gate-check/                        # Methodology
├── ghm-id-register/                       # Methodology
├── ghm-status-sync/                       # Methodology
├── ghm-harvest/                           # Methodology
└── ghm-sot-builder/                       # Methodology
```

**30 skills total** covering the complete PRD lifecycle v0.1→v1.0.

---

## PRD Stage → Skill Mapping

| Stage              | Skills                                                           | Count |
| ------------------ | ---------------------------------------------------------------- | ----- |
| **v0.1 Spark**     | Problem Framing, User Value Articulation                         | 2     |
| **v0.2 Market**    | Competitive Landscape, Product Type Classification               | 2     |
| **v0.3 Commercial**| Outcome Definition, Pricing Model, Moat Definition, Features     | 4     |
| **v0.4 Journeys**  | Persona Definition, User Journey Mapping, Screen Flow Definition | 3     |
| **v0.5 Red Team**  | Risk Discovery Interview, Technical Stack Selection              | 2     |
| **v0.6 Arch**      | Architecture Design, Technical Specification                     | 2     |
| **v0.7 Build**     | Epic Scoping, Test Planning, Implementation Loop                 | 3     |
| **v0.8 Release**   | Release Planning, Runbook Creation, Monitoring Setup             | 3     |
| **v0.9 Launch**    | GTM Strategy, Launch Metrics, Feedback Loop Setup                | 3     |
| **Methodology**    | Gate Check, ID Register, Status Sync, Harvest, SoT Builder       | 5     |

See [`skills-inventory.md`](skills-inventory.md) for full specifications.

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
6. Update [`skills-inventory.md`](skills-inventory.md)

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
epics/ (Execution) ←→ SoT/ (Source of Truth)
```

Skills can:

- Reference `SoT/SoT.*.md` for business rules and specifications
- Output to `epics/` for task tracking
- Create IDs: CFD-, BR-, KPI-, UJ-, API-, FEA-, DES-, TEST-, DEP-

---

## Contributing

1. Check [`skills-inventory.md`](skills-inventory.md) for pending skills
2. Follow the skill structure above
3. See [CONTRIBUTING.md](../CONTRIBUTING.md) for guidelines
