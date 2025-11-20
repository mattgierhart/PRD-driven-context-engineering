---
title: "PRD Stage Tooling Map"
version: 0.1
updated: "2025-02-15"
authority: Companion to `PRD-VERSION-LIFECYCLE.md`
---

# PRD Stage Tooling & Outputs

Use this guide alongside the lifecycle checklist to know **which artifacts, scripts, and IDs must exist at each gate**. Hooks reference this file to remind agents of missing tooling.

| Gate | Core Outputs | Required Tools / Scripts | SoT IDs / Files |
|------|--------------|--------------------------|-----------------|
| **v0.1 Spark** | PRD spark narrative, outcome hypotheses, constraint list | `temp/research/` scratchpads → archive; `tools/analysis/*.md` templates | CFD-### (founder notes) |
| **v0.2 Market Definition** | Segment + TAM table, "not for" statements | `tools/segment-table.py`, market research templates, spreadsheet import guide | CFD-### (research docs), BR-### (business guardrails) |
| **v0.3 Commercial Model** | Competitor matrix, monetization model, pricing guardrails | Pricing workbook (`tools/pricing-model.xlsx` placeholder), `temp/finance/` to SoT extraction script | CFD-### (pricing intel), BR-### (pricing rules), KPI- seeds |
| **v0.4 User Journeys** | Personas, journey narratives, validation backlog | Interview transcription workflow (`tools/transcribe.sh`), `templates/source-of-truth/USER-JOURNEYS.md` updates | UJ-###, CFD-### references, dependency BR/API IDs |
| **v0.5 Red Team Review** | Risk table, mitigation plan, Gate 1 decision memo | `tools/risk-register.md`, checklist script for mitigation IDs | BR-### (mitigation), TEST-### proposals |
| **v0.6 Architecture** | Stack summary, integration contracts, schema deltas | `tools/architecture/diagram-template.drawio`, OpenAPI generator instructions, schema migration helper | API-###, DBT-###, ARC-### baseline |
| **v0.7 Build Execution** | EPIC backlog, QA strategy, README metrics | `tools/create_task.py`, `.ghm/task-backlog.yaml`, CI instructions, test harness scripts | TEST-###, DEP-###, SoT IDs updated each task |
| **v0.8 Deployment & Ops** | Deployment checklist, monitoring plan, runbooks | `tools/deploy/*.sh`, `tools/observability/alerts.md`, Infra IaC templates | DEP-###, RUN-###, MON-### |
| **v0.9 Go-to-Market** | Launch plan, messaging, analytics instrumentation | GTM workbook, analytics setup scripts, README GTM widget | GTM-###, CFD-### feedback IDs, KPI-### metrics |
| **v1.0 Market Adoption** | Adoption report, optimization backlog, loopback triggers | `tools/metrics/pull-dashboard.sh`, retention analysis scripts | KPI-###, CFD-###, EPIC references for optimization |

## Usage Notes
- When you mark a gate complete in `workflows/PRD-VERSION-LIFECYCLE.md`, cross-check this table to confirm every tool + artifact shipped or was logged as a follow-up task.
- Add rows or expand tool descriptions as the repo accumulates concrete scripts and templates. Keep the map synchronized with `.ghm/config.yaml` so stricter profiles (e.g., `production`) require additional artifacts.
- Hooks can surface the "Required Tools" column as todo items when starting/reloading sessions.

### Example: v0.7 Build Execution Flow
1. Approve plan → run `python3 tools/create_task.py --title "Validate OCR retry" --epic EPIC-07-retries --gate v0.7 --github-issue https://github.com/org/repo/issues/321`.
2. Update the GitHub issue with the generated `TASK-###` path so humans ↔ agents share references.
3. Keep `.ghm/task-backlog.yaml` as the source of truth for in-flight work; run `python3 tools/validate_ghm.py` before ending the session to ensure backlog, tasks, and memory stay consistent.
