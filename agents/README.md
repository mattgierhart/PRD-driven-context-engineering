---
title: "Agents Directory Guide"
scope: "agents/"
updated: "2025-02-14"
---

# Agents Directory

This folder holds active agent briefs for the product team.

## What belongs here
- Primary agent brief (e.g., `AURA.md`)
- Secondary agent briefs (e.g., APOLLO build lead, JANUS deployment)
- Sub-agent rosters specific to the product

Keep briefs lightweight and reference the authoritative workflow files rather than copying them.

## How to create a brief
1. Start from the templates under [`templates/agents/`](../templates/agents/).
2. Copy the relevant template into this directory and rename it (for example `AURA.md`).
3. Replace placeholders with product-specific details while keeping lifecycle and ID references intact.
4. When briefs change, note the update in the product `README.md` so other collaborators reload the file.

## Naming conventions
- Use uppercase filenames for individual agents (e.g., `AURA.md`, `APOLLO.md`).
- Use kebab-case for supporting documents (e.g., `research-subagents.md`).

## Relationship to the 3+1+SoT+Temp stack
- Agent briefs describe **how** an AI or human should operate.
- They defer to `README.md` for status, `PRD.md` for what to build, and the SoT library for authoritative specs.
- EPICs should reference the relevant agent brief whenever responsibilities or handoffs change.

Keep this directory small and current—retire unused briefs to `archive/` once the role is no longer active.
