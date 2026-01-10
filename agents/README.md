---
title: "Agent Ecosystem"
updated: 2025-01-09
---

# Agent Ecosystem

## Architecture

Two-layer system:
1. **Static layer** (`agents/{AGENT}.md`) — Methodology, role, handoffs
2. **Memory layer** (`agents/memory/{AGENT}.project.md`) — Project-specific learning

## Agents

| Agent | Domain | Lifecycle | File |
|-------|--------|-----------|------|
| AURA | Market & Product Strategy | v0.1–v0.5 | [AURA.md](AURA.md) |
| Designer | User Experience | v0.3–v0.4, v0.6 | [Designer.md](Designer.md) |
| APOLLO | Technical Leadership | v0.6–v0.8 | [APOLLO.md](APOLLO.md) |
| GTM | Go-to-Market | v0.9–v1.0 | [GTM.md](GTM.md) |

## Loading an Agent

```
Load agents/AURA.md for v0.3 Commercial work
```

The agent file provides:
- Role boundaries and decision authority
- Input/output specifications
- Handoff contracts
- Anti-patterns to avoid
- Subagent templates (if applicable)

## Memory Layer

Project-specific patterns accumulate in `agents/memory/`:
- Updated per session by Session-Closer
- Harvested to skills/ when pattern reaches 3+ occurrences
- Persists across product iterations

See [memory/README.md](memory/README.md) for protocol.

## Subagents

Isolated-context helpers for repeatable tasks:
- README-Status-Updater
- ID-Registrar
- Session-Closer
- Gate-Checker
- Harvest-Agent

See [subagents/README.md](subagents/README.md) for definitions.

## Tools

Located in `agents/tools/`:
- `generate_visuals.py` — Dependency graphs
- `validate_sessions.py` — EPIC compliance audit

## MCP Servers

See `agents/tools/config/mcp_servers.yaml` for external tool configuration.
