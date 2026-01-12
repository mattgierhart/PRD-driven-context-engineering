---
title: "Epics Directory Guide"
scope: "epics/"
updated: "2025-02-14"
---

# Epics Directory

This folder stores the active and archived EPIC files that make up the "+1" layer of the PRD Led Context Engineering stack.

## Getting started

1. Copy [`epics/EPIC_TEMPLATE.md`](EPIC_TEMPLATE.md).
2. Rename it using the format `EPIC-XX-short-slug.md` (e.g., `EPIC-07-onboarding-flow.md`).
3. Update Section 0 with the lifecycle gate it advances and the owner.
4. Use **Section 2 (Context & IDs)** to log every SoT ID created, modified, or referenced.

## Workflow expectations

- Only one EPIC should be marked as **Active** at a time; others stay in "Queued" or are marked "Complete".
- Link to the EPIC from the product `README.md` (Current Work Surface) so agents can load it quickly.
- Close the EPIC with a retrospective or learning summary.

## File hygiene checklist

- Keep tables narrow enough for Markdown readability—split into subsections when needed.
- Avoid duplicating PRD sections; reference lifecycle stages instead (e.g., "Supports PRD v0.4").
- When handing off to another agent, add a `### Handoff Notes` block with the relevant IDs.

For detailed gate criteria, review [`README.md`](../README.md).
