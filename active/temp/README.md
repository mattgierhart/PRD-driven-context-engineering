---
title: "Temp Workspace Guide"
scope: "temp/"
updated: "2025-02-14"
---

# Temp Workspace

Short-lived notes and scratchpads live here. This directory is intentionally transient.

## Rules
- Attach an owner and expiry date at the top of each temp file.
- Harvest insights into the Source-of-Truth library before the expiry date.
- Delete or archive temp files during EPIC retrospectives—nothing in here should block gate reviews.

## Suggested filename format
`YYYY-MM-DD-topic-owner.md`

## When to use temp files
- Brainstorming before IDs are stable.
- Collecting raw interview transcripts before distilling into CFD- IDs.
- Drafting queries or SQL before adding them to `ACTUAL_SCHEMA.md`.

Avoid referencing temp files from `PRD.md` or `README.md`; convert them into SoT entries first.
