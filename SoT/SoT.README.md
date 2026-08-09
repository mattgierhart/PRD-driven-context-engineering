---
title: "Source-of-Truth Library Guide"
scope: "SoT/"
updated: "2026-08-08"
template_version: "3.3.0"
---

# Source-of-Truth (SoT) Library

This directory holds the durable, ID-based specifications that make up the knowledge graph for your product.

> **Acceptance boundary:** root `SoT/` is repository-owned, but only records named in `PRD.md`'s
> **Accepted SoT snapshot** are accepted product truth. Starter/example blocks elsewhere remain
> non-authoritative until the PRD gate snapshot explicitly accepts them.

<!-- SECTION: sot-registry -->
## Structure

Each file focuses on one artifact type with a consistent ID prefix (~100-150 lines each):

| File | ID Prefix | Purpose |
|------|-----------|---------|
| `SoT.UNIQUE_ID_SYSTEM.md` | (governance) | ID format, prefixes, and registry |
| `SoT.BUSINESS_RULES.md` | BR-XXX | Business constraints and rules |
| `SoT.USER_JOURNEYS.md` | UJ, PER, SCR | User journeys, personas, screens |
| `SoT.API_CONTRACTS.md` | API-XXX | API endpoint specifications |
| `SoT.DATA_MODEL.md` | DBT-XXX | Database tables and schema |
| `SoT.TESTING.md` | TEST-XXX | Test cases and coverage |
| `SoT.DEPLOYMENT.md` | DEP, RUN, MON, SEC | Deployment, runbooks, monitoring, and secrets inventory |
| `SoT.customer_feedback.md` | CFD-XXX | Customer feedback and insights |
| `SoT.DESIGN_COMPONENTS.md` | DES-XXX | UI components and design tokens |
| `SoT.TECHNICAL_DECISIONS.md` | TECH, ARC, ENV | Tech stack, architecture, and environment profiles |
| `SoT.INTEGRATIONS.md` | INT-XXX | Third-party service integrations |
| `SoT.LESSONS_LEARNED.md` | LL-XXX | Cross-session behavioral feedback |
| `SoT.ADOPTION.md` | ADO-XXX | Adoption stage, beachhead, whole-product, and reference evidence |

**IDs in PRD/README** (not SoT files): FEA-XXX, RISK-XXX, GTM-XXX, KPI-XXX
<!-- /SECTION: sot-registry -->

> See [SoT.UNIQUE_ID_SYSTEM.md](SoT.UNIQUE_ID_SYSTEM.md) for full ID specifications.

> **Human-review views**: each SoT file has an HTML companion in [`html/`](html/README.md) that
> renders its entries the way the artifact's natural reviewer expects (journey maps, API reference,
> ER cards, ADRs, runbooks, adoption curve…). Entry anchors equal IDs
> (`html/SoT.BUSINESS_RULES.html#BR-001`), and every cross-reference is a hyperlink. Activated
> records in these Markdown files become authoritative only when accepted by the PRD;
> uninitialized examples are format guidance. HTML is a render for review, never the first place a
> decision is recorded. Start at [`html/index.html`](html/index.html).

> **The as-built layer (v0.7)**: the IDs in these files are the *spec* layer of the knowledge graph. During build execution the product's code becomes a second layer — extracted into `status/devgraph.json` and bridged back to these IDs via the `@implements` tags in code. The IDs you define here are the anchors those bridges point to; an `ARC-` entry can carry a **Conformance Rule** the code is checked against. See [`../docs/DEVELOPMENT_GRAPH.md`](../docs/DEVELOPMENT_GRAPH.md).

## How to Initialize

1. Install or copy the generic scaffold into your product repository
2. Replace the example content in the first uninitialized SoT file you need; do not append beside fake examples
3. Change that file's `template_state` from `uninitialized` to `active`
4. Give each real entry a unique ID (metadata, description, references)
5. Cross-link the ID from the current PRD gate log and accepted SoT snapshot; at v0.7+ also add it to the active EPIC

`SoT.BUSINESS_RULES.md` and `SoT.TECHNICAL_DECISIONS.md` are already active for this repository's
accepted Wave 0B records. The remaining starter files stay non-authoritative until initialized by
the steps above.

## Maintenance Rules

- **Never delete IDs** — mark as deprecated and link to replacement
- **Update timestamps** — change `Last Updated` when entry changes
- **Before v0.7** — track new IDs in the current PRD gate change log and SoT snapshot; no EPIC exists
- **From v0.7 onward** — track new IDs in the active EPIC **Context & IDs** section
- **Wave 0B note** — these governance-bootstrap decisions follow the pre-v0.7 rule, state their
  lifecycle origin, and do not imply gate advancement or implementation authorization
- **Keep files lean** — target 80-120 lines per SoT file

## Template Contract

All SoT files follow this structure:

```
1. YAML Frontmatter (10-15 lines)
2. Title + Purpose Block (5-10 lines)
3. Navigation by Category (10-20 lines)
4. ONE Example Entry (30-50 lines)
5. Deprecated Section (5-10 lines)
6. Cross-Reference Index (10-15 lines)
7. Update Protocol (15-20 lines)
```
