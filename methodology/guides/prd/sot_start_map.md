# SoT Kickoff by PRD Stage

This checklist shows when each Source of Truth (SoT) file must begin during the PRD lifecycle. Teams can start earlier, but each file **must be created no later than the listed stage** and then updated continuously.

| PRD Stage | Required SoT File to Start | Notes |
| --- | --- | --- |
| V0.1 — Market Definition | New SoT record (seed the SoT library) | Capture initial IDs to anchor market findings and avoid orphaned research. |
| V0.2 | — | No additional SoT file required beyond the seed record. |
| V0.3 — Commercial Model | `BUSINESS_RULES.md` | Document monetization rules, constraints, and pricing hypotheses as BR-XXX entries. |
| V0.4 — User Journeys & UI Screens | `USER_JOURNEYS.md` | Add UJ-XXX journeys with UI notes so downstream specs reference real flows. |
| V0.5 | — | No new SoT file required; refine existing IDs. |
| V0.6 — Architecture & Readiness | `API_CONTRACTS.md`, `testing_playbook.md`, `deployment_playbook.md`, `component_library.md` | Stub API-XXX, TEST-XXX, DEP-XXX, and DES-XXX items to align build, validation, and rollout. |
| V0.7 — Build Execution | `ACTUAL_SCHEMA.md` | Start DBT-XXX schema entries to back APIs and tests with concrete tables. |
| V0.8 — Customer Feedback | `customer_feedback.md` | Capture CFD-XXX insights and trace them to journeys, rules, and tests. |
| V0.9 — Go-To-Market | `marketing_playbook.md` | Define GTM hypotheses, experiments, and launch assets with MKT-XXX IDs. |
