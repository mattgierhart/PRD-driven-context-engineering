---
title: "CLAUDE Agent Operating Guide"
updated: "2026-06-10"
authority: "PRD Led Context Engineering"
template_version: "3.2.0"
---

# CLAUDE.md — Agent Operating Guide

> **Mission**: Build software in lockstep with the PRD Version Lifecycle.
> **Authority**: Load `README.md` → `PRD.md` → `CLAUDE.md` → Active EPIC.
> **Core Rule**: If it's not in the ID Graph (Specs), it doesn't exist.

Rules are loaded automatically from `.claude/rules/*.md`.

## Quick Reference

- **Lifecycle Guide**: [`README.md`](README.md)
- **ID System**: [`SoT/SoT.UNIQUE_ID_SYSTEM.md`](SoT/SoT.UNIQUE_ID_SYSTEM.md)
- **SoT Index**: [`SoT/SoT.README.md`](SoT/SoT.README.md)
- **EPIC Template**: [`epics/EPIC_TEMPLATE.md`](epics/EPIC_TEMPLATE.md)
- **Active Work**: [`epics/`](epics/)
- **Domain Profile**: [`.claude/domain-profile.yaml`](.claude/domain-profile.yaml)
- **Hook Contract**: [`.claude/hooks/HOOK_CONTRACT.md`](.claude/hooks/HOOK_CONTRACT.md)
- **Agent Registry**: [`.claude/agents/`](.claude/agents/)
- **Rules**: [`.claude/rules/`](.claude/rules/)
- **SoT HTML Companion**: [`SoT/html/`](SoT/html/README.md) — human-review renders of each SoT file
- **Deliverables (concept)**: [`docs/DELIVERABLES_CONCEPT.md`](docs/DELIVERABLES_CONCEPT.md) — proposed input-mode layer where humans emit SoT markdown

## SoT HTML Companion (when to use it)

The pages in `SoT/html/` are **for humans, not for context loading**:

- **Read**: load the markdown SoT files for task context, never the HTML. The HTML duplicates
  markdown content in a heavier format — loading it wastes tokens.
- **Write**: when you add or change a SoT entry, mirror it in the companion page in the same
  session — duplicate the matching `<article class="entry" id="PREFIX-XXX">` block and fill the
  placeholders. Entry anchors must equal IDs; cross-references must be `a.id` hyperlinks.
- **Surface**: at gate reviews, EPIC handoffs, or whenever a human asks to "see" the specs, point
  them at `SoT/html/index.html` (opens from `file://`, no build).
- **Extend**: a new SoT file (via `ghm-sot-builder`) gets a companion page — follow "Extending
  the library" in [`SoT/html/README.md`](SoT/html/README.md) and register it in `index.html`.
- **Conflict rule**: if HTML and markdown disagree, markdown wins; fix the HTML.

**When in doubt, follow the Source of Truth.**
