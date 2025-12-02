---
title: "Workflow Master Guide"
version: 1.0
updated: "2025-02-14"
---

# WORKFLOW_MASTER.md — Gear Heart Methodology

> **Authority**: Tier 1 workflow reference for repositories that implement the Gear Heart Methodology (GHM).
> **Purpose**: Describe how navigation files, SoT assets, and agents interact across the PRD Version Lifecycle.

---

## 1. How to Use This Document
1. Read `README.md` → `PRD.md` → active EPIC to understand the current context.
2. Use this file to confirm the operating rituals, gate reviews, and agent responsibilities.
3. Cross-reference the specialized guides when needed:
   - Lifecycle gates: [`PRD_VERSION_LIFECYCLE.md`](./PRD_VERSION_LIFECYCLE.md)
   - Unique IDs: [`UNIQUE-ID-SYSTEM.md`](./UNIQUE-ID-SYSTEM.md)
   - Primary agents: [`templates/agents/`](../templates/agents/)

Keep this document synchronized with templates and workflows. When the methodology evolves, update this file first.

---

## 2. Repository Layout (Copy-Friendly)
```
/
├── README.md              # Command Center — status & navigation
├── PRD.md                 # Lifecycle narrative (v0.1 → v1.0)
├── CLAUDE.md              # Execution rules for build agents
├── agents/                # Active agent briefs (e.g., AURA, APOLLO)
├── epics/                 # Active EPIC with Section 3A ID tracking
├── source_of_truth/       # ID-based specifications (BR-/UJ-/API-/...)
├── temp/                  # Scratchpads with owner + expiry
├── archive/               # Frozen history by YYYY-MM
├── templates/             # Canonical templates for cloning
├── workflows/             # Methodology workflows (this folder)
└── tools/                 # Automation scripts (metrics, ID registry)
```

Use `docs/REPO_ORGANIZATION.md` for additional guidance when copying the repository into a new product workspace.

---

## 3. Lifecycle Overview
GHM advances products through ten non-skippable gates (v0.1 → v1.0). Each gate has:
- **Owner** — strategy, build, ops, or GTM lead.
- **Definition of Ready** — prerequisites before work begins.
- **Definition of Done** — checklist before promotion.
- **Primary SoT IDs** — where durable knowledge is stored.

See [`PRD_VERSION_LIFECYCLE.md`](./PRD_VERSION_LIFECYCLE.md) for the full table and gate checklists.

### Loopback Rules
- When new information invalidates a gate, open a new revision row in the PRD change log (e.g., `v0.3r1`).
- Update the README lifecycle table and note the triggering ID.
- Capture remediation work in an EPIC and track all ID deltas in Section 3A.

---

## 4. Agent Operating Model
### Primary Agents
| Agent | Owner | Lifecycle Focus | Home File |
|-------|-------|-----------------|-----------|
| **AURA** | Strategy Lead | v0.1–v0.5 | `agents/AURA.md` (start from template) |
| **APOLLO or Build Lead** | Engineering | v0.6–v0.8 | `agents/APOLLO.md` (custom) |
| **JANUS or Ops/GTM Lead** | Operations / GTM | v0.8–v1.0 | `agents/JANUS.md` (custom) |

### Sub-Agent Registry
Document research and specialist sub-agents in `agents/` or the dedicated [`SUBAGENT_REGISTRY.md`](./SUBAGENT_REGISTRY.md). Each entry should list:
- Mission and lifecycle focus
- Required inputs (README, PRD sections, SoT IDs)
- Expected outputs mapped to IDs

### Collaboration Rituals
- **Daily / per-session**: Load 3+1 stack, update EPIC Section 3A, sync blockers.
- **Gate reviews**: Run the checklist, capture decision notes, update README + PRD.
- **Retrospectives**: Archive EPIC, log learnings, ensure all temp files are harvested into SoT.

---

## 5. Execution Workflow
1. **Plan** — Strategy agent (AURA) advances PRD gate; identifies IDs to touch.
2. **Scope** — Active EPIC is created with lifecycle goal and Section 3A seeded with known IDs.
3. **Build** — Execution agents implement code/tests, updating SoT entries as they change.
4. **Validate** — Run automated tests, update `testing_playbook.md`, confirm gate checklist.
5. **Deploy** — Follow deployment playbooks, update metrics via automation.
6. **Archive** — Move closed EPICs to `archive/`, record learnings, update README version history.

Automation hooks (e.g., ID registry refresh, metrics capture) should live under `tools/`. Reference them from EPIC tasks or README quick commands.

---

## 6. Governance & Quality
- **Single Source of Truth**: If information is duplicated, fix it by linking to the canonical SoT entry.
- **ID Discipline**: Never create an ID without logging it in SoT and EPIC Section 3A.
- **Security & Compliance**: Capture requirements as BR- or DEP- IDs and ensure tests enforce them.
- **Documentation Hygiene**: No orphaned files. README should link to every active EPIC and agent brief.

---

## 7. Change Management
- Update templates first, then propagate to active product repos.
- When major methodology changes occur, add a note in `docs/CHANGELOG.md` (if present) and communicate via README “Latest Change Notes”.
- Keep this master workflow short and opinionated—link out to deeper references instead of restating them.

---

## 8. Reference Index
- 3+1+SoT+Temp primer: `README.md`
- Lifecycle workflow: `workflows/PRD_VERSION_LIFECYCLE.md`
- Unique IDs: `workflows/UNIQUE-ID-SYSTEM.md`
- Agent templates: `templates/agents/`
- PRD/README templates: `templates/product/`
- EPIC template: `templates/epics/EPIC-template.md`
- Repo copying guide: `docs/REPO_ORGANIZATION.md`

Maintain alignment between this document and the templates to keep onboarding predictable for both humans and AI agents.
