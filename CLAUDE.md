---
title: "CLAUDE Agent Operating Guide"
ghm_stack: "3+1+SoT+Temp"
lifecycle_focus: "v0.6–v0.9"
updated: "2025-11-27"
version: "2.0"
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

---

## 10. Session Protocols

> **Why this matters**: Each context window is a discrete "shift." The next agent arrives with no memory of your session. These protocols ensure seamless handoffs.
>
> Reference: [Anthropic - Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)

### 10.1 Session Start Protocol

**Before writing any code or making changes:**

1. **Load the active EPIC** and read **Section 0 (Session State)** first
2. **Verify understanding** of where the previous session stopped:
   - What was completed?
   - What is the current blocker or next task?
   - Any warnings or context from the previous agent?
3. **Check git status/log** for recent changes not yet reflected in Session State
4. **Confirm the active Issue** you'll be working on
5. **If unclear**, read the full EPIC and relevant SoT IDs before proceeding

```
# Quick start checklist (mental or explicit)
□ Read EPIC Section 0 (Session State)
□ Understand stopping point from last session
□ Confirmed active Issue and Phase
□ Loaded relevant SoT IDs
□ Ready to continue
```

### 10.2 Session End Protocol (MANDATORY)

**Before ending your session, you MUST:**

1. **Update EPIC Section 0** with:
   - Work completed this session (be specific, link IDs)
   - Exact stopping point (file paths, function names, line numbers)
   - Any blockers encountered
   - Clear instructions for the next session
   - Files changed this session

2. **Commit your changes** with a descriptive message:
   ```
   session: [EPIC-XX] <summary of session work>

   - Completed: <what was done>
   - Stopped at: <where work stopped>
   - Next: <what the next session should do>
   ```

3. **Move current session to Session History table** if starting fresh next time

4. **Verify** the EPIC is ready for the next agent:
   - Could someone with no context pick this up?
   - Are all file changes documented?
   - Are blockers clearly explained?

### 10.3 Session State Quality Checklist

A good Session State entry should pass these checks:

| Check | Question |
|-------|----------|
| **Specific** | Can the next agent find exactly where to resume? (file:line, not just "auth work") |
| **Complete** | Are all changed files listed? |
| **Actionable** | Does "Next Session Should" give clear first steps? |
| **Contextual** | Are blockers explained with enough detail to resolve? |
| **Linked** | Are relevant IDs (BR-XXX, API-XXX) referenced? |

### 10.4 Context Window Discipline

- **Target**: Complete each Issue within 1 context window
- **Warning signs**: Repeated tool calls, circular reasoning, forgetting earlier decisions
- **When approaching limit**:
  1. Stop new work immediately
  2. Update Session State with current progress
  3. Commit all work-in-progress
  4. Note explicit stopping point for next session
- **Split threshold**: If estimated work exceeds 1 window, create sub-issues BEFORE starting

### 10.5 Session Handoff Validation

Before ending, verify:
```
□ EPIC Section 0 updated with current session details
□ Session History table has previous sessions logged
□ Git commit made with session summary
□ No uncommitted changes left behind
□ Blockers documented with resolution paths
□ Next agent can start within 5 minutes of reading Session State
```

> **Enforcement**: This protocol is validated by `tools/validate-sessions.py` and may be enforced by pre-exit hooks. See [`templates/hooks/`](templates/hooks/) for hook examples.
