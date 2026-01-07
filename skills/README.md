# PRD Skills Library

> **Purpose**: Agent Skills for each stage of the PRD Lifecycle. Skills are loaded on-demand to give agents specialized capabilities for specific tasks.

This library follows the [Agent Skills Specification](https://agentskills.io/specification).

---

## Skill Structure

Each skill follows the standard Agent Skills format:

```
skills/
├── prd-v01-problem-framing/       # v0.1 Spark stage skills
│   ├── SKILL.md                   # Core instructions (<5000 tokens)
│   ├── references/                # Loaded on-demand for deep context
│   ├── assets/                    # Templates and static files
│   └── scripts/                   # Executable automation (optional)
├── prd-v02-market-definition/     # v0.2 Market stage skills
├── ...
└── SKILL_TEMPLATE/                # Template for creating new skills
```

---

## PRD Lifecycle → Skill Mapping

| PRD Stage | Skill Prefix | Focus | Primary Skills |
|-----------|--------------|-------|----------------|
| **v0.1** Spark | `prd-v01-` | Problem & Outcomes | Problem Framing, Evidence Collection |
| **v0.2** Market | `prd-v02-` | Segments & ICP | Market Sizing, ICP Definition |
| **v0.3** Commercial | `prd-v03-` | Value & Pricing | Competitive Analysis, Pricing Strategy |
| **v0.4** Journeys | `prd-v04-` | Personas & Flows | Journey Mapping, Dependency Modeling |
| **v0.5** Red Team | `prd-v05-` | Risks & Feasibility | Risk Assessment, Mitigation Planning |
| **v0.6** Architecture | `prd-v06-` | Technical Strategy | System Design, API Contracts |
| **v0.7** Build | `prd-v07-` | Implementation | Code Review, Test Generation |
| **v0.8** Release | `prd-v08-` | Deployment & Ops | Runbook Creation, Monitoring Setup |
| **v0.9** Launch | `prd-v09-` | Go-to-Market | Launch Planning, KPI Definition |
| **v1.0** Growth | `prd-v10-` | Market Adoption | Retention Analysis, Optimization |

---

## Skill Naming Convention

```
prd-v{XX}-{action}-{target}
```

**Examples**:
- `prd-v01-problem-framing` - Frame problems for Spark stage
- `prd-v02-market-sizing` - Size market segments
- `prd-v04-journey-mapping` - Map user journeys
- `prd-v06-api-contracts` - Draft API specifications

---

## Creating a New Skill

1. Copy `SKILL_TEMPLATE/` to `prd-v{XX}-{name}/`
2. Update `SKILL.md` frontmatter (name, description)
3. Write concise instructions (<500 lines, <5000 tokens)
4. Add reference files for detailed context (loaded on-demand)
5. Add templates to `assets/` if needed
6. Add automation scripts to `scripts/` if needed

**Best Practices** (from agentskills.io):
- Keep `SKILL.md` under 5000 tokens - it's loaded when skill activates
- Use specific trigger phrases in description
- Reference files are loaded on-demand - keep them focused
- Scripts should be self-contained with documented dependencies

---

## Usage

Skills are discovered and activated by agents based on:
1. **Explicit invocation**: User requests a specific skill
2. **Trigger matching**: Description keywords match user intent
3. **Context awareness**: Agent determines skill relevance

When activated, the agent:
1. Loads `SKILL.md` into context
2. Loads relevant `references/` files as needed
3. Uses `assets/` templates for structured output
4. Executes `scripts/` for automation

---

## Integration with PRD Ecosystem

Skills integrate with the broader documentation ecosystem:

```
README.md (Dashboard)
    ↓
PRD.md (Strategy) ←→ skills/ (Capabilities)
    ↓
epics/ (Execution) ←→ specs/ (Source of Truth)
```

Skills can:
- Reference `specs/SoT.*.md` for business rules and contracts
- Output to `epics/` for task tracking
- Update `specs/` when generating new IDs (BR-, UJ-, API-)

---

## Contributing

See [CONTRIBUTING.md](../CONTRIBUTING.md) for contribution guidelines.
