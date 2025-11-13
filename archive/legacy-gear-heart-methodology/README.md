---
status: legacy
scope: "Command_Center export (2024)"
note: "Retained for historical reference. Do not copy directly into new repos."
updated: "2025-02-14"
---

# Gear Heart Methodology (GHM) — Legacy Export

> ⚠️ This folder preserves the 2024 "Command_Center" era documentation. It is not aligned with the current Gear Heart Methodolo
gy (README-as-Command-Center, 3+1+SoT+Temp lifecycle). Keep for historical comparison only.

GHM is a vendor‑neutral, product‑agnostic methodology for shipping software with clarity and speed. It codifies a few simple, powerful ideas:

- Three‑File Discipline: One operational truth, one PRD, one current EPIC. Update in place. No forks of truth.
- 3+3 Pattern (when needed): If a section grows, extract a single focused doc (e.g., Technical Architecture), but keep the summary in the Command Center.
- Gate‑based Execution: Small, phase‑based loops with explicit validation gates for quality, performance, security, and business rules.
- Agent Coordination: Clear roles and handoffs for research, technical feasibility, design, implementation, and testing — human or AI.

This repository packages the methodology as docs and templates you can drop into any project.

What’s Inside
- Core workflow: `docs/workflow/`
- Engineering standards: `docs/standards/`
- Security: `docs/security/`
- Templates: `docs/templates/`
- MCP integration guides (optional): `docs/mcp/`

Philosophy
- Clarity over volume: Fewer, stronger docs with clear authority.
- Evidence over opinion: Gates enforce realities (tests, metrics), not vibes.
- One location per concept: Code and docs are where the automation expects them.
- Progressive refinement: Draft early, refine continuously — no parallel versions.

Getting Started
1) Copy `docs/templates/COMMAND_CENTER_template.md`, `PRD-template.md`, and `EPIC-template.md` into your product folder and fill them in.
2) Use `docs/workflow/WORKFLOW-MASTER.md` to run the 5‑phase loop and gates.
3) Keep updates flowing to the Command Center (single source of truth).

Status: Initial public export. License: MIT.
