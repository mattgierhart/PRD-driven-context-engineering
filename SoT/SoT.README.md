---
title: "Source-of-Truth Library Guide"
scope: "source_of_truth/"
updated: "2025-01-10"
---

# Source-of-Truth (SoT) Library

This directory holds the durable, ID-based specifications that make up the knowledge graph for your product.

## Structure

Each file focuses on one artifact type and uses a consistent ID prefix:

| File                            | ID Prefix           | Purpose                                                   |
| ------------------------------- | ------------------- | --------------------------------------------------------- |
| `SoT.UNIQUE_ID_SYSTEM.md`       | (all)               | ID governance, format, prefixes, and central registry.    |
| `SoT.TEMPLATE_PURITY_STANDARD.md` | (governance)        | Template quality standard and contamination guidelines.   |
| `SoT.BUSINESS_RULES.md`         | BR-###              | Commercial and operational rules that must never drift.   |
| `SoT.USER_JOURNEYS.md`          | UJ-###              | Canonical user journeys tied to pains and value moments.  |
| `SoT.API_CONTRACTS.md`          | API-###             | API and integration contracts, request/response rules.    |
| `SoT.ACTUAL_SCHEMA.md`          | DBT-###             | Data models, tables, and analytics schemas.               |
| `SoT.DESIGN_BRIEF.md`           | DES-###             | Design components, tokens, and visual specifications.     |
| `SoT.customer_feedback.md`      | CFD-###             | Interviews, surveys, and signal summaries.                |
| `SoT.testing_playbook.md`       | TEST-###            | Critical tests, coverage expectations, and automation.    |
| `SoT.deployment_playbook.md`    | DEP/GTM/RUN/MON-### | Release procedures, GTM activities, runbooks, monitoring. |

> See [`README.md`](../README.md) for full ID specifications and automation tips.

## How to initialize

1. Fork this repository for your product.
2. Populate each `SoT.*.md` file with entries specific to your product.
3. Each entry gets a unique ID card (metadata, description, references, history).
4. Cross-link IDs from PRD, README, EPICs, and other SoT files.

## Maintenance rules

- Never delete IDs—mark them as deprecated and link to the replacement.
- Update the `Last Reviewed` field for each entry when it changes or is revalidated.
- Add new IDs via EPIC Section 2 so the audit trail stays intact.
- Keep tables tight; break large lists into sub-sections by domain or lifecycle stage.

When the number of files grows, create subfolders (e.g., `SoT/design/`) but preserve the ID prefixes and update the `SoT.README.md` table accordingly.
