# Gear Heart Methodology (GHM) — Open Source 🚀

GHM is a context engineering construct to a PRD led product development design specificly for AI led or AI only software development. For a visual overview, visit: https://gearheartai.org

## Mission
- Make quality inevitable by encoding it into the workflow — not as after‑the‑fact reviews, but as gates and habits that guide every change.
- Replace sprawling, conflicting documentation with a single source of truth that is easy to maintain and hard to misinterpret.
- Enable confident collaboration between humans and AI agents through clear roles, boundaries, and handoffs.

## Principles
- 3+1+SoT+Temp Pattern: Documentation organized in four layers: (1) The "3" navigation files (Claude.md, PRD.md, README.md) provide context and point to details, (2) The "+1" current EPIC tracks active work and ID changes, (3) SoT (Source of Truth) files create and maintain IDs with full specifications (USER-JOURNEYS.md, BUSINESS_RULES.md, API_CONTRACTS.md, etc.), (4) Temp files hold work-in-progress before extraction to SoT.
- ID‑Based Knowledge Graph: Every meaningful artifact (user journey, API, business rule, test) gets a unique, durable ID. Cross-references use IDs, not duplicate prose. This enables AI agents to load precise context in <1 minute vs 5-10 minutes of full-document scanning.
- One Location Per Concept: Code and docs live where automation expects them; duplication is a defect.
- Gate‑Based Execution: Phase loops with explicit validation gates for quality, security, performance, and business rules.
- Context Governance: Clear authority hierarchy, predictable paths, archived history, and zero "mystery files."
- Test and Data First: Accuracy and speed are validated with unit/integration/E2E tests and golden datasets.

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
