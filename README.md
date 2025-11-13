# Gear Heart Methodology (GHM) — Open Source 🚀  

A PRD-driven **context engineering workflow** for AI-led and AI-only software.  
GHM treats your **PRD + README + SoT library** as a long-term memory for AI agents and a shared contract for humans.

---

## What this repo is for

This repository is a **workflow**, not just a set of templates.

You can use it in two ways:

- **1) As an AI context system**  
  Claude, CODEX, or other agents read these files to understand:
  - What product we’re building and why (PRD)
  - What the current state of work is (README)
  - Where the real specifications live (SoT IDs)

- **2) As a leadership-level playbook**  
  Senior PMs, founders, and executives can:
  - See how to “productize” AI agents into a repeatable delivery system  
  - Track work across phases of the **PRD Version Lifecycle**  
  - Plug the workflow into existing engineering orgs and rituals  

---

## Mission

GHM exists to solve five recurring problems in AI-powered product work:

1. **Single Source of Truth (via an ID graph)**  
   Eliminate doc sprawl by converging on one PRD and one README, backed by a Source-of-Truth (SoT) ID library. No duplicate specs, no drifting slide decks.

2. **Cross-session predictability for AI**  
   Make it easy for AI agents to re-enter the work at any time and quickly reconstruct context from the same stable structures.

3. **Multi-agent “pair programming” with low onboarding**  
   Let specialized agents (research, architecture, GTM, etc.) join mid-stream using the same navigation files and ID schemes, without a 5–10 minute context dump.

4. **ID-based context instead of context-window overload**  
   Use IDs (`BR-XXX`, `UJ-XXX`, `API-XXX`, etc.) to reference exactly what an agent needs, instead of pasting entire documents into the prompt.

5. **Human–AI collaboration and handoffs**  
   Encode who does what, where work moves next, and how AI output is validated before it is trusted.

---

## Principles

- **3+1+SoT+Temp Pattern**  
  Documentation organized into four layers:
  1. **“3” navigation files** (AI instruction, product, status):  
     - `CLAUDE.md` – AI instructions  
     - product `PRD.md` – progressive product definition  
     - product `README.md` – current status + navigation  
  2. **“+1” Active EPIC** – tracks the current window of work and ID deltas  
  3. **SoT (Source of Truth) library** – durable, ID-based specs (journeys, rules, contracts, tests, schemas, feedback)  
  4. **Temp files** – short-lived scratchpads that must be harvested into SoT before archive.

- **ID-Based Knowledge Graph**  
  Every meaningful artifact (user journey, API, business rule, test, dataset) gets a **unique, durable ID**. Cross-references use IDs, not duplicate prose. AI agents can load precise context in under a minute instead of scanning everything.

- **One Location Per Concept**  
  Each concept has a canonical home; duplication is treated as a defect. Navigation files point to SoT, not vice-versa.

- **Gate-Based Execution**  
  Work progresses through explicit gates (quality, security, performance, business rules) tied to the **PRD Version Lifecycle** and EPIC states.

- **Context Governance**  
  Clear authority hierarchy, predictable paths, archived history, and zero “mystery files.” If it isn’t in the graph, it doesn’t exist.

- **Test and Data First**  
  Every important behavior is backed by unit/integration/E2E tests and golden datasets. AI output is evaluated, not trusted by default.

---

## 3+1+SoT+Temp Stack  
### (The ecosystem of documentation)

| Layer | Purpose | Canonical Assets | How It Uses IDs |
|-------|---------|------------------|-----------------|
| **3 — Navigation Files** | Onboard any AI agent or sub-agent to the product in minimal tokens and show current truth. | instructions `CLAUDE.md`, status `README.md`, product `PRD.md` | Point to SoT anchors (e.g., `BR-112`, `UJ-014`) instead of restating specs. |
| **+1 — Active EPIC** | Focus the current window of work, record scope, and capture deltas. | `templates/epics/EPIC-template.md` (instantiated per EPIC) | Section 3A tracks every ID created, modified, or referenced during execution. |
| **SoT — Source of Truth Library** | Hold authoritative specifications for business rules, journeys, contracts, tests, schemas, and feedback. | Files under `templates/source-of-truth/` (e.g., `BUSINESS_RULES.md`, `API_CONTRACTS.md`, `ACTUAL-SCHEMA.md`, `customer-feedback.md`) | Each entry is an ID card (`BR-XXX`, `API-XXX`, `DBT-XXX`, `CFD-XXX`) with metadata, bidirectional references, and change history. |
| **Temp — Working Scratchpads** | Short-lived exploration and drafting before extraction into SoT. | `temp/` directories scoped per product/epic | Temporary content must be harvested into SoT IDs before archive; no durable knowledge lives here. |

- **Unique IDs everywhere**  
  The [Unique ID System](workflows/UNIQUE-ID-SYSTEM.md) defines naming, lifecycle, and automation hooks. Templates reference these IDs explicitly so SoT changes propagate back to navigation files without duplication.

- **Workflow alignment**  
  The PRD workflow (see `/workflows`) advances the PRD and EPIC gates only when SoT IDs are updated and referenced correctly. This is how we enforce discipline on both humans and agents.

---

## AI as Dynamic Memory

The 3+1+SoT+Temp stack is designed as a **dynamic memory layer for AI**:

- **Claude / CODEX** read:
  - `CLAUDE.md` for “how to behave”  
  - `README.md` for “where we are now”  
  - `PRD.md` for “what we’re building and why”  

- **Agents retrieve SoT entries by ID**, not by dumping full docs:
  - “Load `BR-021`, `API-007`, and `UJ-013`, then propose changes.”
  - “Compare `CFD-010` (customer feedback) with `UJ-004` (journey) and suggest optimizations.”

- **Context windows stay small**, but the effective memory is large and structured.

You can attach your own agent roster (e.g., AURA for market research, APOLLO for architecture, JANUS for deployment and ops) to specific **PRD lifecycle stages**, and they will all speak the same language of IDs and files.

---

## Validation Approach

- **Gates**  
  Each phase ends with checks that must pass before proceeding (quality, performance, security, business rules, and documentation).

- **Business Rules**  
  Domain-critical constraints (e.g., plan limits, pricing policies, compliance rules) are encoded as `BR-XXX` IDs, backed by tests and referenced from PRD sections.

- **Performance Targets**  
  Latency and SLOs are defined early and verified with scriptable tests; regressions block promotion.

- **Security Hygiene**  
  No secrets in the repo. CI secrets only where needed. Scans and reviews at boundaries (e.g., before new integrations or external exposure).

- **Documentation Gates**  
  Structure and authority checks prevent drift:
  - Three-File Discipline (CLAUDE, PRD, README) remains clean and current  
  - No versioned duplicates of specs  
  - SoT entries are the single reference, never forked in slideware.

---

## Testing Approach

- **Unit Tests** – Fast checks for logic boundaries and critical utilities.  
- **Integration Tests** – Validate seams: auth, data access, external systems, internal workflows.  
- **E2E Tests** – User-journey validation for highest-value flows; map to `UJ-XXX` IDs.  
- **Golden Datasets** – Curated “truth” for AI and deterministic checks; report accuracy and coverage over time.  
- **Performance Benchmarks** – Thresholds aligned to product targets; run on PRs when relevant files change.

---

## Context Governance

- **Authority**  
  The combination of product `README.md` + SoT library is the **single source of truth**. PRD and EPICs reference that authority; archives retain history.

- **Paths**  
  Stable, predictable locations so automation and humans always agree where to look:
  - `templates/product/` for PRD/README/CLAUDE templates  
  - `templates/epics/` for EPICs  
  - `templates/source-of-truth/` for SoT structures  

- **Templates vs Examples**  
  Canonical templates are separated from examples. No “almost-templates” hiding in random folders.

- **Vendor Isolation**  
  Third-party code and experiments live under a vendor/experimental area or as submodules, not mixed with standards and templates.

---

## What’s Inside

### Core Documentation

- [ID-Based Knowledge Graph](docs/ID-KNOWLEDGE-GRAPH.md) – Durable ID system for cross-referencing  
- [AI Evaluator Guide](AI-EVALUATOR-GUIDE.md) – How to evaluate AI-generated work using this method  
- [Contributing](CONTRIBUTING.md) – How to contribute to this methodology  

### Templates

- **Product Templates** (`templates/product/`)
  - Product PRD template  
  - Product CLAUDE instructions template  
  - Product README template (with ID navigation)

- **EPIC Templates** (`templates/epics/`)
  - EPIC template (with Section 3A: ID Tracking)  
  - Feature / deployment / environment EPICs  
  - GitHub issue & sizing patterns

- **Source of Truth Templates** (`templates/source-of-truth/`)
  - `USER-JOURNEYS.md` (UJ-XXX)  
  - `BUSINESS_RULES.md` (BR-XXX)  
  - `API_CONTRACTS.md` (API-XXX)  
  - `ACTUAL-SCHEMA.md` (DBT-XXX)  
  - `customer-feedback.md` (CFD-XXX)

- **Design Templates** (`templates/design/`)  
- **Testing Templates** (`templates/testing/`)

### Workflows

- [CLAUDE.md](CLAUDE.md) – Global Claude Code instructions  
- PRD workflow guides under `/workflows/` (PRD lifecycle and EPIC gates)

---

## PRD Version Lifecycle (v0.1 → v1.0)

The PRD is a **living artifact** that progresses through versions as reality unfolds.  
You can revisit earlier states (e.g., return from v0.7 to v0.4), but you **shouldn't skip** them.

| Milestone | Focus | Key Gate / Question | PRD State After This Stage |
|-----------|-------|---------------------|----------------------------|
| **v0.1 — Spark** | Initial problem statement, success metrics draft, rough scope. | **Alignment:** Do we agree on the problem, outcomes, and basic constraints? | PRD created with a seed narrative, early success metrics, and ID scaffolding. |
| **v0.2 — Market Definition** | Market slices, ICP, target personas, supporting research IDs. | **Clarity:** Is the market definition specific enough to say who this is *not* for? | PRD updated with validated opportunity statements and focused market segments. |
| **v0.3 — Commercial Model** | Monetization & pricing hypotheses, competitive landscape, “fast-follow” anchor(s). | **Desirability + Viability:** Is there a credible way to win (e.g., 1–10% cheaper or clearly better) against named competitors? | PRD captures the commercial model, anchor competitors, and feature themes driven by market positioning. |
| **v0.4 — User Journeys** | Real user journeys mapped to specific pains; critical moments that matter. | **User Value:** Do these journeys meaningfully solve pains for concrete users/personas? | PRD updated with key user journeys, journey-to-pain mappings, and a navigation schema. |
| **v0.5 — Red Team Review** | Risk, failure, and threat modeling; anticipated development challenges. | **Reality Check:** What breaks first? Where might this fail in practice? | PRD enriched with risk scenarios, mitigations, and flags for architecture & implementation. |
| **v0.6 — Architecture** | UI component approach, environment setup, architecture & data schema sketches. | **Architecture Gate:** Is the stack coherent, feasible, and aligned with the risks from v0.5? | PRD records target stack, patterns, integration boundaries, and initial `API-XXX` / `DBT-XXX` stubs. |
| **v0.7 — Build Execution** | EPIC and issues backlog, integration/deployment playbook, testing strategy. | **Buildability:** Do we have a realistic plan to ship, and are the right EPICs and tests defined? | PRD defines high-level EPICs and test criteria; day-to-day change happens in EPICs, not in the PRD. |
| **v0.8 — Deployment & Ops** | Release criteria, staging strategy, smoke tests, security checks. | **Deployment Gate:** Can we safely and repeatedly release this into the target environment(s)? | PRD updated with deployment details, operational checks, and links to live environments. |
| **v0.9 — Go-to-Market** | Marketing plan, messaging, engagement targets, analytics plan. | **Feedback Loop:** Do we know how we’ll attract users and measure behavior end-to-end? | PRD updated with GTM plan, analytics events, funnel assumptions, and feedback capture paths. |
| **v1.0 — Market Adoption & Optimization** | Real customer usage, pricing validation, optimization roadmap. | **Adoption & Profitability:** Are paying customers using the product, and do we understand how to improve conversion and economics? | PRD becomes a launch-ready, living contract connected to real market data and ongoing optimization. |

Each version increment requires:

- Updating the PRD metadata table and version history.  
- Linking supporting evidence from SoT files by ID.  
- Running the appropriate gates from the PRD workflow (see `/workflows`).

---

## Legacy Gear Heart Methodology Package

Legacy organization (being migrated to the new structure):

- [Methodology README](gear-heart-methodology/README.md)  
- [Workflow](gear-heart-methodology/docs/workflow/WORKFLOW-MASTER.md)  
- [Standards](gear-heart-methodology/docs/standards/)  
- [Security](gear-heart-methodology/docs/security/SECRETS-MANAGEMENT.md)  
- [MCP (optional)](gear-heart-methodology/docs/mcp/)

---

## License & Community

- **License:** MIT (Gear Heart AI, LLC)  
- **Contribute:** See [CONTRIBUTING.md](CONTRIBUTING.md)  
- **Code of Conduct:** See [CODE_OF_CONDUCT.md](gear-heart-methodology/CODE_OF_CONDUCT.md)

---

## Quick Start

1. **Clone**

   ```bash
   git clone https://github.com/mattgierhart/PRD-driven-context-engineering.git
   cd PRD-driven-context-engineering
