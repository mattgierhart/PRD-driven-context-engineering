---
title: "Epics Directory Guide"
scope: "epics/"
updated: "2026-08-08"
---

# Epics Directory

This folder stores the active and archived EPIC files that make up the "+1" layer of the PRD Led Context Engineering stack.

## Getting started

Do not create or copy an EPIC until the PRD reaches v0.7 and the owner approves implementation.
Before v0.7, track definition work in the PRD gate log and accepted SoT snapshot.

1. Copy [`epics/EPIC_TEMPLATE.md`](EPIC_TEMPLATE.md).
2. Rename it using the established execution format `EPIC-NN-short-slug.md`; use `EPIC-XX` only
   as a non-allocated placeholder in documentation.
3. Update the **Session State** section with the lifecycle gate it advances and the owner.
4. Use the **Context & IDs** section to log every SoT ID created, modified, or referenced.

## Workflow expectations

- Exactly one implementation EPIC may have **State: In Progress**; others remain **Planned**,
  move through **Testing**, or are marked **Complete**.
- Link to the EPIC from the product `README.md` (Current Work Surface) so agents can load it quickly.
- Close the EPIC with a retrospective or learning summary.

## File hygiene checklist

- Keep tables narrow enough for Markdown readability—split into subsections when needed.
- Avoid duplicating PRD sections; reference lifecycle stages instead (e.g., "Supports PRD v0.4").
- When handing off to another agent, add a `### Handoff Notes` block with the relevant IDs.

For detailed gate criteria and lifecycle authorization, review [`PRD.md`](../PRD.md);
`README.md` reports current status and navigation.
