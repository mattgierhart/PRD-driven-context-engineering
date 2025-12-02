---
title: "Source-of-Truth Library Guide"
scope: "source_of_truth/"
updated: "2025-02-14"
---

# Source-of-Truth (SoT) Library

This directory holds the durable, ID-based specifications that make up the knowledge graph for your product.

## Structure
Each file focuses on one artifact type and uses a consistent ID prefix:

| File | ID Prefix | Purpose |
|------|-----------|---------|
| `BUSINESS_RULES.md` | BR-### | Commercial and operational rules that must never drift. |
| `USER_JOURNEYS.md` | UJ-### | Canonical user journeys tied to pains and value moments. |
| `API_CONTRACTS.md` | API-### | API and integration contracts, request/response rules. |
| `ACTUAL_SCHEMA.md` | DBT-### | Data models, tables, and analytics schemas. |
| `customer_feedback.md` | CFD-### | Interviews, surveys, and signal summaries. |
| `testing_playbook.md` | TEST-### | Critical tests, coverage expectations, and automation hooks. |
| `deployment_playbook.md` | DEP-### | Release procedures, runbooks, and operational guardrails. |

> See [`workflows/UNIQUE-ID-SYSTEM.md`](../workflows/UNIQUE-ID-SYSTEM.md) for full ID specifications and automation tips.

## How to initialize
1. Copy the templates from [`templates/source_of_truth/`](../templates/source_of_truth/).
2. Create the files you actually need today; keep unused templates out of the repo until required.
3. Populate each entry with an ID card (metadata, description, references, history).
4. Cross-link IDs from the PRD, README, EPICs, and other SoT files.

## Maintenance rules
- Never delete IDs—mark them as deprecated and link to the replacement.
- Update the `Last Reviewed` field for each entry when it changes or is revalidated.
- Add new IDs via EPIC Section 3A so the audit trail stays intact.
- Keep tables tight; break large lists into sub-sections by domain or lifecycle stage.

When the number of files grows, create subfolders (e.g., `source_of_truth/design/`) but preserve the ID prefixes and update the `README.md` table accordingly.
