# Gear Heart Methodology (GHM) — Open Source 🚀

GHM is a context engineering construct to a PRD led product development design specificly for AI led or AI only software development. For a visual overview, visit: https://gearheartai.org

## Mission
- Make quality inevitable by encoding it into the workflow — not as after‑the‑fact reviews, but as gates and habits that guide every change.
- Replace sprawling, conflicting documentation with a single source of truth that is easy to maintain and hard to misinterpret.
- Enable confident collaboration between humans and AI agents through clear roles, boundaries, and handoffs.

## Principles
- 3+1+SoT+Temp Pattern: Documentation organized in four layers: (1) the "3" navigation files (CLAUDE.md, PRD.md, README.md) provide context and point to details, (2) the "+1" current EPIC tracks active work and ID changes, (3) SoT (Source of Truth) files create and maintain IDs with full specifications (USER-JOURNEYS.md, BUSINESS_RULES.md, API_CONTRACTS.md, etc.), (4) Temp files hold work-in-progress before extraction to SoT.
- ID‑Based Knowledge Graph: Every meaningful artifact (user journey, API, business rule, test) gets a unique, durable ID. Cross-references use IDs, not duplicate prose. This enables AI agents to load precise context in <1 minute vs 5-10 minutes of full-document scanning.
- One Location Per Concept: Code and docs live where automation expects them; duplication is a defect.
- Gate‑Based Execution: Phase loops with explicit validation gates for quality, security, performance, and business rules.
- Context Governance: Clear authority hierarchy, predictable paths, archived history, and zero "mystery files."
- Test and Data First: Accuracy and speed are validated with unit/integration/E2E tests and golden datasets.

## 3+1+SoT+Temp Stack (How the Docs Fit Together)

| Layer | Purpose | Canonical Assets | How It Uses IDs |
|-------|---------|------------------|-----------------|
| **3 — Navigation Files** | Onboard any agent in under a minute and show current truth. | `CLAUDE.md`, product `README.md`, product `PRD.md` | Point to SoT anchors (e.g., `BR-112`) instead of restating specs. |
| **+1 — Active EPIC** | Focus the current window of work, record scope, and capture deltas. | `templates/epics/EPIC-template.md` | Section 3A tracks every ID created, modified, or referenced during execution. |
| **SoT — Source of Truth Library** | Hold authoritative specifications for business rules, journeys, contracts, tests, etc. | Files under `templates/source-of-truth/` (e.g., `BUSINESS_RULES.md`, `API_CONTRACTS.md`) | Each entry is an ID card (`BR-XXX`, `API-XXX`, `TEST-XXX`) with metadata, bidirectional references, and change history. |
| **Temp — Working Scratchpads** | Short-lived exploration before extraction into SoT. | `temp/` directories scoped per product/epic | Temporary content must be extracted into SoT IDs before archive, ensuring no durable knowledge lives outside the graph. |

- **Unique IDs everywhere:** The [Unique ID System](workflows/UNIQUE-ID-SYSTEM.md) defines naming, lifecycle, and automation hooks. Templates reference these IDs explicitly so SoT changes propagate back to navigation files without duplication.
- **Workflow alignment:** The [WORKFLOW-MASTER](workflows/WORKFLOW-MASTER.md) ladder advances the PRD and EPIC gates only when SoT IDs are updated and referenced correctly, enforcing stack discipline.

## Validation Approach
- Gates: Each phase ends with checks that must pass before proceeding (quality, performance, security, business rules).
- Business Rules: Enforce domain‑critical constraints (e.g., plan limits, pricing policies) with automated checks.
- Performance Targets: Define and verify latency/SLOs with scriptable tests; avoid regressions by default.
- Security Hygiene: Secrets never committed; CI secrets only where needed; scans and reviews at boundaries.
- Documentation Gates: Structure and authority checks prevent drift (e.g., Three‑File Discipline, no versioned duplicates).

## Testing Approach
- Unit: Fast checks for logic boundaries and critical utilities.
- Integration: Validate system seams (auth, data access, workflows).
- E2E: User‑journey validation for the highest‑value flows.
- Golden Datasets: Curated truth data for AI and deterministic checks; report accuracy and coverage over time.
- Performance: Benchmarks aligned to targets; run on PRs when relevant files change.

## Context Governance
- Authority: Command Center is the single source of truth; extracted docs reference back; archives hold history.
- Paths: Stable, predictable locations so automation and humans always agree where to look.
- Templates vs Examples: Canonical templates are separate from examples; no ambiguous “almost‑templates.”
- Vendor Isolation: Third‑party code lives under a vendor area or submodules, not mixed with standards and templates.

## What's Inside

### Core Documentation
- [ID-Based Knowledge Graph](docs/ID-KNOWLEDGE-GRAPH.md) - Durable ID system for cross-referencing
- [AI Evaluator Guide](AI-EVALUATOR-GUIDE.md) - Guide for evaluating AI-generated work
- [Contributing](CONTRIBUTING.md) - How to contribute to this methodology

### Templates
- **Product Templates** (`templates/product/`)
  - Product PRD template
  - Product Claude instructions template
  - README template (with ID navigation)
- **EPIC Templates** (`templates/epics/`)
  - EPIC template (with Section 3A: ID Tracking)
  - Feature/deployment/environment EPICs
- **Source of Truth Templates** (`templates/source-of-truth/`)
  - USER-JOURNEYS.md template (UJ-XXX)
  - BUSINESS_RULES.md template (BR-XXX)
  - API_CONTRACTS.md template (API-XXX)
  - ACTUAL-SCHEMA.md template (DBT-XXX)
  - customer-feedback.md template (CFD-XXX)
- **Design Templates** (`templates/design/`)
- **Testing Templates** (`templates/testing/`)

### Workflows
- [CLAUDE.md](CLAUDE.md) - Global Claude Code instructions
- Workflow guides in `workflows/`

## PRD Version Ladder (v0.1 → v1.0)

| Milestone | Lead Agent(s) | Key Deliverables | Decision or Gate | Resulting PRD State |
|-----------|----------------|------------------|------------------|---------------------|
| **v0.1 — Spark** | User + AURA | Initial problem statement, success metrics draft | Kickoff alignment | PRD created with seed narrative and ID scaffolding |
| **v0.2 — Market Research** | AURA | Market sizing, target personas, supporting research IDs | Research evidence review | PRD updated with validated opportunity statements |
| **v0.3 — Competitive Analysis** | AURA | Competitive landscape summary, differentiation map | Competitive moat checkpoint | PRD references comparative insights and risk notes |
| **v0.4 — User Validation** | AURA | User interviews, journey hypotheses, `UJ-XXX` IDs | User need validation gate | PRD aligns with verified user pains and outcomes |
| **v0.5 — Red Team Review** | AURA | Threat scenarios, failure analysis, mitigation IDs | **Gate 1**: Research complete | PRD cleared for technical evaluation |
| **v0.6 — Technical Stack** | APOLLO | Feasibility notes, draft architecture, `API-XXX`/`DBT-XXX` stubs | Stack viability check | PRD records target stack and constraints |
| **v0.7 — Technical Feasibility** | APOLLO | Detailed architecture, integration plan, risk heatmap | **Gate 2**: Tech feasibility | PRD confirms buildable path with owner commitments |
| **v0.8 — UX Journey Mapping** | AURA | Wireframes, refined journeys, `DES-XXX` references | UX cohesion review | PRD anchors solution narrative to SoT design assets |
| **v0.9 — Information Architecture** | AURA | Navigation schema, data taxonomy, updated IDs | Content architecture checkpoint | PRD locked for development handoff prep |
| **v1.0 — Build Ready** | All agents + User | Final PRD package, signed-off SoT updates, release criteria | **Gate 3**: Launch-ready PRD | PRD is authoritative build contract tied to IDs |

Each increment requires updating the PRD metadata table, logging the change in the version history, and ensuring that supporting evidence lives in SoT files with their respective IDs. The [WORKFLOW-MASTER](workflows/WORKFLOW-MASTER.md) describes the validation activities tied to each gate.

### Gear Heart Methodology Package
Legacy organization (being migrated to new structure):
- [Methodology README](gear-heart-methodology/README.md)
- [Workflow](gear-heart-methodology/docs/workflow/WORKFLOW-MASTER.md)
- [Standards](gear-heart-methodology/docs/standards/)
- [Security](gear-heart-methodology/docs/security/SECRETS-MANAGEMENT.md)
- [MCP (optional)](gear-heart-methodology/docs/mcp/)

## License & Community
- License: MIT (Gear Heart AI, LLC)
- Contribute: See [CONTRIBUTING.md](gear-heart-methodology/CONTRIBUTING.md)
- Code of Conduct: See [CODE_OF_CONDUCT.md](gear-heart-methodology/CODE_OF_CONDUCT.md)

## Quick Start
1) Clone
```bash
git clone https://github.com/mattgierhart/PRD-driven-context-engineering.git
cd PRD-driven-context-engineering
```
2) Adopt the core docs
- Copy `gear-heart-methodology/docs/templates/COMMAND_CENTER_template.md`, `PRD-template.md`, and `EPIC-template.md` into your product folder
- Fill them in and commit
3) Run the workflow
- Use `gear-heart-methodology/docs/workflow/WORKFLOW-MASTER.md` as your operating manual
- Add tests and golden data as you implement features
4) Keep truth tight
- Update the Command Center continuously; extract only when sections grow beyond the threshold
5) Enable validation
- Add CI to enforce gates, structure, and no‑secrets policies; use the link‑check workflow as a starting point
