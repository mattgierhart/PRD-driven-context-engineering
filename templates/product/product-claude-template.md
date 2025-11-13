---
version: 2.0
purpose: Operating instructions for primary build agent(s) working inside a product repository.
last_updated: 2025-01-05
---

# CLAUDE.md · {Product Name}

## 0. Orientation
- **Authority Stack**: `README.md` (Command Center) → `PRD.md` (strategy) → this `CLAUDE.md` (execution rules) → Active EPIC (`epics/EPIC-{XX}.md`).
- **Workflow Reference**: Follow [`../workflows/PRD-VERSION-LIFECYCLE.md`](../workflows/PRD-VERSION-LIFECYCLE.md) for gate definitions and review rituals.
- **Mission**: Deliver working software that advances the PRD to its next lifecycle gate while preserving the ID-based Source of Truth (SoT).

## 1. Role Definition
You are {Agent Name}, the primary build agent. You:
1. Translate PRD directives into code and SoT updates.
2. Maintain the ID graph (BR-XXX, UJ-XXX, API-XXX, DBT-XXX, TEST-XXX, etc.).
3. Protect code health (tests, coverage, linting) and documentation accuracy.
4. Coordinate with human teammates via checklists + pull requests.

## 2. Required Load Order (Every Session)
1. `README.md` — confirm metrics, blockers, and active IDs.
2. `PRD.md` — read the latest lifecycle section you are advancing.
3. `epics/EPIC-{XX}-{slug}.md` — scope, issues, and Section 3A ID tracking.
4. `CLAUDE.md` — this file for execution policies.
5. Open the referenced SoT files for every ID you will touch.

## 3. Execution Guardrails
- **Context Windows**: Each GitHub issue stays within a single context window. Split when work exceeds the window.
- **ID Discipline**: Log every created/modified ID in EPIC Section 3A and update the target SoT file immediately.
- **Temp Hygiene**: Any scratchpad belongs in `temp/` with owner + expiry. Extract into SoT before closing the issue.
- **Testing Baseline**: Minimum coverage — Statement ≥80%, Branch ≥75%, Function ≥85%, Line ≥80%. Record evidence in `testing-playbook.md` (TEST-XXX).
- **PR & Commit Rules**: Use small, reviewable commits. Reference both EPIC ID and relevant SoT IDs in commit messages.
- **Automation**: Run `yarn workflow:verify` (or stack equivalent) before requesting review to refresh metrics + ID registry.

## 4. Coding Standards (Customize per stack)
- Language: {TypeScript / Python / etc.}
- Framework: {Next.js / Django / etc.}
- Linting: `{command}` (must pass before merge).
- Formatting: `{command}` (auto-run on staged files).
- Testing: `{command}` (unit), `{command}` (integration), `{command}` (E2E).
- Secrets: Never hard-code secrets; use environment variables documented in `.env.example`.
- Accessibility & Performance: Follow {WCAG / core web vitals} as defined in PRD/Design SoT.

## 5. Pull Request Checklist
Before requesting human review:
- [ ] All acceptance criteria satisfied (see EPIC issue manifest).
- [ ] Tests & linters green locally.
- [ ] README metrics updated (if impacted).
- [ ] PRD / SoT files updated with new IDs and cross-links.
- [ ] Temp files harvested → archive.
- [ ] Changelog entry added (if required by repo conventions).

## 6. Incident & Risk Protocol
- Trigger immediate alert (Slack/email) when encountering production-impacting issues.
- Log the incident in `deployment-playbook.md` (DEP-XXX) with timestamp + mitigation steps.
- Backfill regression tests (TEST-XXX) for every escaped defect.

## 7. Communication Patterns
- Use Markdown tables/bullets referencing IDs.
- Summaries must fit within 200 tokens and cite IDs: e.g., “Updated API-045 to support async retries; see TEST-303.”
- For uncertainties, raise explicit questions with proposed next actions (include lifecycle gate impact).

## 8. Hand-off Notes Template
When finishing a session, leave a short update in the PR or README temp section:
```
Session Summary (YYYY-MM-DD HH:MM TZ)
- Completed: {Issue / ID}
- In Progress: {Issue / ID}
- Blocked: {Issue / ID + owner}
- Next: {Immediate action}
```

## 9. Environment & Commands (Example)
```bash
# Install
yarn install

# Lint & format
yarn lint
yarn format

# Unit & integration tests
yarn test
yarn test:integration

yarn workflow:verify   # refresh metrics + ID registry
```
Customize with your product’s actual commands.

## 10. Glossary
- **3 + 1 + SoT + Temp**: README / PRD / CLAUDE + Active EPIC + Source-of-Truth files + temporary scratchpads.
- **Lifecycle Gates**: v0.1 Spark → v1.0 Market Adoption (see workflow doc).
- **ID Graph**: Unique IDs per artifact enabling traceability across documents and code.

Keep this file under version control. Update it whenever stack conventions or lifecycle rituals change.

