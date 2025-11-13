---
title: "Repository Organization Guide"
audience: "Founders, PMs, AI agents"
updated: "2025-02-14"
---

# Repository Organization Guide

> Purpose: Provide a simple, repeatable structure for product repositories adopting the Gear Heart Methodology.
> Audience: Founders, PMs, and AI agents preparing to copy this repo as a starter kit.
> Status: This repository already includes empty-but-documented folders (`agents/`, `epics/`, `source-of-truth/`, `temp/`, `archive/`) so you can copy it directly into a new product workspace.

---

## Core Principles
1. **Predictable entry points** — Every product repo exposes the 3 navigation files (`README.md`, `PRD.md`, `CLAUDE.md`) at the root.
2. **ID-first documentation** — Source-of-Truth (SoT) files live at the root (or a `source-of-truth/` folder) and use unique IDs (BR-/UJ-/API-/etc.).
3. **Isolated execution windows** — Active work happens inside `epics/` with Section 3A tracking all ID deltas.
4. **Temp is temporary** — Scratchpads go in `temp/` with owner + expiry, then migrate into SoT before archiving.

---

## Recommended Folder Layout
```
/                     # Product root (clone of methodology repo)
├── README.md         # Command Center (navigation + metrics)
├── PRD.md            # Lifecycle narrative (v0.1 → v1.0)
├── CLAUDE.md         # Build agent instructions
├── agents/           # Primary/secondary agent briefs (e.g., AURA, APOLLO)
├── epics/            # Active + archived EPIC files (Section 3A for IDs)
├── source-of-truth/  # Optional folder housing SoT markdown files
│   ├── USER-JOURNEYS.md
│   ├── BUSINESS_RULES.md
│   ├── customer-feedback.md
│   └── ...
├── src/              # Application code
├── tests/            # Automated tests
├── docs/             # Supporting docs (ID Knowledge Graph, decision logs)
├── temp/             # Short-lived scratchpads (purge or harvest every EPIC)
├── archive/          # Frozen history (YYYY-MM folders)
└── tools/            # Automation scripts (metrics, registry sync)
```

> Keep filenames lowercase (except the 3 navigation files) to avoid case sensitivity issues when copying between OSs.

---

## Copying This Repo for a New Product
1. **Clone** this methodology repo locally.
2. **Duplicate** the directory for your product (`cp -R PRD-driven-context-engineering new-product-repo`).
3. **Reset Git history** in the copy (`rm -rf .git && git init`).
4. **Update templates**:
   - Replace the contents of `README.md`, `PRD.md`, and `CLAUDE.md` using the templates under `templates/product/`.
   - Create agent briefs from `templates/agents/` as needed (AURA, etc.).
   - Initialize SoT files from `templates/source-of-truth/`.
   - Start your first EPIC using `templates/epics/EPIC-template.md`.
5. **Wire automation**: adapt scripts in `tools/` or create equivalents for metrics + ID registry generation.
6. **Run the lifecycle workflow**: follow `workflows/PRD-VERSION-LIFECYCLE.md` to progress gates.

---

## Tips for Navigation Simplicity
- Keep all cross-file links relative (`./PRD.md`) so copying the repo maintains navigation.
- Surface key IDs in `README.md` and EPIC Section 3A to minimize search friction for agents.
- Use consistent emoji/label patterns across repos to reduce onboarding time.
- Archive closed EPICs monthly (`archive/YYYY-MM/`) and link lessons learned in the README “EPIC Learning” section.

---

## Related References
- `workflows/PRD-VERSION-LIFECYCLE.md`
- `workflows/UNIQUE-ID-SYSTEM.md`
- `templates/product/README-template.md`
- `templates/agents/AURA-primary-agent-template.md`

Keep this guide updated as the methodology evolves or as new automation becomes standard.
