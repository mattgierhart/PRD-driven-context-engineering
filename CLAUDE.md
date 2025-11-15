---
title: "CLAUDE Agent Operating Guide"
ghm_stack: "3+1+SoT+Temp"
lifecycle_focus: "v0.6–v0.9"
updated: "2025-02-14"
---

# CLAUDE.md — Gear Heart Methodology Operating Guide

This file directs Claude (and other build-oriented agents) when collaborating inside a repository that implements the Gear Heart Methodology (GHM).

---

## 1. Mission & Scope
- **Mission**: Build and maintain product software in lockstep with the PRD Version Lifecycle (v0.1 → v1.0).
- **Primary Focus**: Architecture through deployment (v0.6 → v0.9) with support for strategy revisions when loopbacks occur.
- **Authority Stack**: Always load the navigation files in order — `README.md` → `PRD.md` → this `CLAUDE.md` → active EPIC.

When instructions conflict, defer to `README.md` for status, then `PRD.md` for requirements, then SoT IDs for specifics.

---

## 2. Repository Load Order
1. **`README.md`** — Command Center. Confirms lifecycle gate, active EPIC, metrics, and critical alerts.
2. **`PRD.md`** — Lifecycle narrative. Identify the current gate, open questions, and referenced IDs.
3. **`CLAUDE.md` (this file)** — How you should behave while executing.
4. **Active EPIC (`epics/EPIC-XX-*.md`)** — Execution plan, Section 3A ID tracking, test strategy.
5. **SoT Files (`source-of-truth/*.md`)** — Load only the IDs referenced in the EPIC/PRD.

Use the Unique ID System (`workflows/UNIQUE-ID-SYSTEM.md`) to resolve any unfamiliar prefixes.

---

## 3. Execution Rules
- **Respect lifecycle gates**: Do not advance a gate without satisfying the checklist in [`workflows/PRD-VERSION-LIFECYCLE.md`](workflows/PRD-VERSION-LIFECYCLE.md).
- **Operate from IDs**: When editing code or docs, reference the relevant IDs in commit messages, EPIC updates, and PR comments.
- **Ground prompts in SoT**: Before asking AI to draft code or docs, translate requirements into explicit acceptance criteria tied to existing or planned IDs so the prompt mirrors reality ([CFD-401](source-of-truth/customer-feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build)).
- **Prefer existing artifacts**: Update the current PRD section or SoT entry instead of creating parallel documents.
- **Document changes**: Record code decisions in the active EPIC, Section 3A. Link new/updated IDs explicitly.
- **Surface blockers fast**: If a gate cannot be cleared, note the blocker in the EPIC and alert the product README “Critical Alerts”.

---

## 4. Collaboration with Other Agents
- **AURA (Strategy Lead)** owns v0.1–v0.5. Treat her briefs in `agents/` as authoritative for market context.
- **Build Leads (e.g., APOLLO)** own v0.6–v0.9. Align on architecture and testing strategy before coding.
- **Ops / GTM Agents (e.g., JANUS)** may own deployment or launch tasks. Follow their checklists for v0.8–v0.9.
- Sub-agents should always cite the EPIC and IDs they touch; avoid free-form explorations that bypass the lifecycle.

---

## 5. Coding Standards
- Match the stack defined in the PRD Architecture section (v0.6). If unclear, stop and request clarification via the EPIC.
- Maintain or improve automated test coverage. New features require corresponding TEST- IDs and executable tests.
- Keep secrets out of the repo. Use environment variables or secret management as documented in deployment playbooks.
- Prefer small, incremental commits tied to specific IDs. Reference them in commit messages (e.g., `BR-214`, `API-042`).

---

## 6. Testing & Verification
- Run the test commands listed in `README.md` before marking an EPIC task as done.
- When adding or modifying tests, update the relevant `TEST-###` entries in `source-of-truth/testing-playbook.md`.
- For performance or security-sensitive changes, consult SoT entries (e.g., `DEP-###`, `BR-###`) to ensure you meet the defined thresholds.
- Validate responsive behavior on the actual devices primary users rely on (not just browser emulation) early in the iteration to avoid late rework ([CFD-401](source-of-truth/customer-feedback.md#cfd-401-partial-ghm-adoption-during-48-hour-inventory-build)).

---

## 7. Deployment & Ops Hand-off
- Follow deployment instructions from the current EPIC and `source-of-truth/deployment-playbook.md`.
- Log release notes or operational updates in the EPIC and surface critical information in `README.md`.
- After deployment, update metrics via automation scripts in `tools/` (or note the manual steps taken).

---

## 8. Escalation Protocol
Escalate immediately when:
- A lifecycle gate checklist cannot be satisfied.
- A required SoT file is missing or outdated.
- External constraints (compliance, security, cost) threaten the plan.

Document the escalation in the EPIC with context, affected IDs, and a proposed next step.

---

## 9. Quick Reference
- Lifecycle guidance: [`workflows/PRD-VERSION-LIFECYCLE.md`](workflows/PRD-VERSION-LIFECYCLE.md)
- ID guidelines: [`workflows/UNIQUE-ID-SYSTEM.md`](workflows/UNIQUE-ID-SYSTEM.md)
- Templates: [`templates/`](templates/)
- Repo organization guide: [`docs/REPO-ORGANIZATION.md`](docs/REPO-ORGANIZATION.md)

Always leave the repo in a state where another agent can reload the 3+1+SoT+Temp stack and pick up within one context window.
