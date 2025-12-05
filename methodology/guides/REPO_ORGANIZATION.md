---
title: "Repository Organization Guide"
audience: "Founders, PMs, AI agents"
updated: "2025-12-05"
---

# Repository Organization Guide

> Purpose: Provide a simple, repeatable structure for product repositories adopting the Gear Heart Methodology.
> Audience: Founders, PMs, and AI agents preparing to use this repo as a starter kit.

---

## Core Principles
1. **Predictable entry points** — Every product repo exposes the 3 navigation files (`README.md`, `PRD.md`, `CLAUDE.md`) at the root.
2. **Templates vs Active separation** — Templates (blank forms) live in `templates/`, while active project files live in `active/`.
3. **ID-first documentation** — Source-of-Truth (SoT) files use unique IDs (BR-/UJ-/API-/etc.) and live in `active/source_of_truth/`.
4. **Isolated execution windows** — Active work happens inside `active/epics/` with Section 3A tracking all ID deltas.
5. **Temp is temporary** — Scratchpads go in `active/temp/` with owner + expiry, then migrate into SoT before archiving.

---

## Repository Layout

```
/                        # Product root
├── README.md            # Command Center (navigation + metrics)
├── PRD.md               # Lifecycle narrative (v0.1 → v1.0)
├── CLAUDE.md            # Build agent instructions
├── CONTRIBUTING.md      # Contribution guidelines
│
├── active/              # INSTANCE FILES (your live project)
│   ├── agents/          # Agent briefs (AURA.md, APOLLO.md, etc.)
│   ├── epics/           # Active EPIC files (Section 3A for IDs)
│   ├── source_of_truth/ # SoT markdown files (BR-, UJ-, API-, etc.)
│   │   ├── USER_JOURNEYS.md
│   │   ├── BUSINESS_RULES.md
│   │   ├── customer_feedback.md
│   │   └── ...
│   └── temp/            # Short-lived scratchpads
│
├── methodology/         # HOW GHM WORKS
│   ├── workflows/       # PRD lifecycle, ID system, workflow guides
│   │   ├── PRD_VERSION_LIFECYCLE.md
│   │   ├── UNIQUE_ID_SYSTEM.md
│   │   └── ...
│   └── guides/          # Model usage, documentation guides, examples
│
├── templates/           # BLANK FORMS (copy to active/)
│   ├── agents/          # Agent brief templates
│   ├── epics/           # EPIC templates (feature, deployment, etc.)
│   ├── product/         # PRD, README, CLAUDE templates
│   ├── source_of_truth/ # SoT file templates
│   ├── testing/         # Test plan templates
│   ├── design/          # Design brief templates
│   └── hooks/           # Session protocol hooks
│
├── tools/               # Automation scripts
│   ├── generate_visuals.py
│   ├── validate_sessions.py
│   └── ...
│
└── docs/                # Onboarding & reference
    ├── getting_started.md
    └── AI_EVALUATOR_GUIDE.md
```

> Keep filenames lowercase with underscores (except the 3 navigation files) to avoid case sensitivity issues.

---

## Using This Repo for a New Product

1. **Clone** this methodology repo locally.
2. **Duplicate** the directory for your product (`cp -R PRD-driven-context-engineering new-product-repo`).
3. **Reset Git history** in the copy (`rm -rf .git && git init`).
4. **Update navigation files**:
   - Replace contents of `README.md`, `PRD.md`, and `CLAUDE.md` using templates from `templates/product/`.
5. **Initialize active files**:
   - Copy agent templates from `templates/agents/` to `active/agents/`.
   - Copy SoT templates from `templates/source_of_truth/` to `active/source_of_truth/`.
   - Create your first EPIC from `templates/epics/EPIC_template.md` in `active/epics/`.
6. **Wire automation**: adapt scripts in `tools/` for metrics + ID registry generation.
7. **Run the lifecycle workflow**: follow `methodology/workflows/PRD_VERSION_LIFECYCLE.md` to progress gates.

---

## Tips for Navigation Simplicity

- Keep all cross-file links relative so copying the repo maintains navigation.
- Surface key IDs in `README.md` and EPIC Section 3A to minimize search friction for agents.
- Use consistent naming patterns across repos to reduce onboarding time.

---

## Related References

- `methodology/workflows/PRD_VERSION_LIFECYCLE.md`
- `methodology/workflows/UNIQUE_ID_SYSTEM.md`
- `templates/product/README_template.md`
- `templates/agents/AURA_primary_agent_template.md`

Keep this guide updated as the methodology evolves or as new automation becomes standard.
