---
title: "Sub-Agent Registry"
version: 1.1
updated: "2025-12-07"
---

# Sub-Agent Registry — Gear Heart Methodology

> **Purpose**: Document specialized agents that support the primary leads (AURA, APOLLO, JANUS) across the PRD Version Lifecycle.
> **Usage**: Copy relevant entries into `agents/` or product-specific rosters when spinning up a new team.
> **Tool Reference**: See [`AGENT_TOOLS.md`](./AGENT_TOOLS.md) for full tool specifications and MCP configuration.

---

## 1. Research Lineup (v0.1 → v0.5)
These agents report to **AURA** and help advance the strategy gates.

| Agent | Lifecycle Gate | Core Question | Required Inputs | Expected Outputs |
|-------|----------------|---------------|-----------------|------------------|
| **SPARK-SCOUT** | v0.1 Spark | "Is this the right problem and what outcomes matter?" | README, PRD v0.1 draft, founder notes | Refined problem statement, desired outcomes, constraints, CFD- ID proposals |
| **SEGMENTOR** | v0.2 Market Definition | "Who exactly is this for (and not for)?" | PRD v0.1, existing research IDs | Segment table, "not for" list, CFD-/BR- ID proposals |
| **MOAT-MAPPER** | v0.3 Commercial Model | "Where are competitors leaving gaps we can own through SEO and demos?" | PRD v0.1–v0.2, competitor research | 1% better / 10% cheaper positioning, unaddressed pain points, SEO keyword targets, demo scripts, BR-/CFD- IDs |
| **JOURNEY-SCRIBE** | v0.4 User Journeys | "What does the user do step-by-step?" | PRD v0.1–v0.3, UX artifacts | 3–7 user journeys, UJ- ID proposals, dependency notes |
| **RISK-ORACLE** | v0.5 Red Team Review | "How could this fail and how do we mitigate it?" | PRD v0.1–v0.4, SoT risk references | Risk table, mitigation plan, TEST-/BR- ID proposals |

### Research Sub-Agent Tools

| Agent | Primary Tools (MCP) | Secondary Tools | Methodology Tools |
|-------|---------------------|-----------------|-------------------|
| **SPARK-SCOUT** | `web_search`, `research_topic`, `get_trending_searches` | `retrieve_content`, `extract_links` | `/load-context`, `id_create` |
| **SEGMENTOR** | `web_search`, `analyze_content`, `search_trends`, `get_interest_by_region` | `retrieve_content`, `extract_links` | `/load-context`, `id_create` |
| **MOAT-MAPPER** | `web_search`, `traverse_website`, `analyze_content`, `search_trends` | `retrieve_content`, `extract_links` | `/load-context`, `id_create` |
| **JOURNEY-SCRIBE** | `retrieve_content`, `analyze_content` | `web_search`, `extract_links` | `/load-context`, `id_create`, `id_link` |
| **RISK-ORACLE** | `web_search`, `research_topic`, `retrieve_content` | `analyze_content`, `extract_links` | `/load-context`, `id_create` |

> **MCP Server**: Research tools provided by [RivalSearchMCP](https://github.com/damionrashford/RivalSearchMCP). See [`tools/config/mcp_servers.yaml`](../../tools/config/mcp_servers.yaml) for setup.

Starter prompts for each agent are available in [`templates/agents/AURA_primary_agent_template.md`](../../templates/agents/AURA_primary_agent_template.md).

---

## 2. Build & Architecture Lineup (v0.6 → v0.8)
These agents report to the build lead (e.g., **APOLLO**).

| Agent | Lifecycle Gate | Core Question | Required Inputs | Expected Outputs |
|-------|----------------|---------------|-----------------|------------------|
| **ARCHITECT** | v0.6 Architecture | "What technical blueprint satisfies the constraints?" | PRD v0.6 targets, risk register, BR-/API-/DBT- IDs | Architecture summary, API/DBT ID updates, integration plan |
| **QA-MAESTRO** | v0.7 Build Execution | "How do we prove this works?" | EPIC Section 3A, testing playbook, PRD acceptance criteria | Test strategy, TEST- ID updates, coverage report |
| **AUTOMATION-RUNNER** | v0.8 Deployment & Ops | "How do we ship and operate safely?" | Deployment playbook, DEP- IDs, infrastructure notes | Deployment checklist, monitoring hooks, release notes |

### Build Sub-Agent Tools

| Agent | Primary Tools | Secondary Tools | Methodology Tools |
|-------|---------------|-----------------|-------------------|
| **ARCHITECT** | `traverse_website` (docs mode), `generate_llms_txt`, `retrieve_content` | `web_search` | `/load-context`, `id_create`, `generate_visuals.py` |
| **QA-MAESTRO** | `validate_sessions.py`, `sot_diff` | `retrieve_content`, `web_search` | `/load-context`, `id_create`, `/gate-check` |
| **AUTOMATION-RUNNER** | `sot_update`, `session_handoff` | `retrieve_content`, `web_search` | `/load-context`, `id_create`, `/harvest-temp` |

---

## 3. Go-to-Market & Adoption Lineup (v0.8 → v1.0)
These agents support GTM and operations leads (e.g., **JANUS**).

| Agent | Lifecycle Gate | Core Question | Required Inputs | Expected Outputs |
|-------|----------------|---------------|-----------------|------------------|
| **LAUNCH-CALLER** | v0.9 Go-to-Market | "How do we coordinate launch and measure success?" | PRD v0.9, README metrics, CFD-/GTM- IDs | Launch plan, analytics instrumentation, feedback loop updates |
| **ADOPTION-ANALYST** | v1.0 Market Adoption | "What signals prove we have market traction?" | Metrics dashboard, KPI- IDs, customer feedback | Adoption report, optimization backlog, new KPI-/CFD- IDs |

### GTM Sub-Agent Tools

| Agent | Primary Tools (MCP) | Secondary Tools | Methodology Tools |
|-------|---------------------|-----------------|-------------------|
| **LAUNCH-CALLER** | `search_trends` | `web_search`, `analyze_content` | `/load-context`, `id_create`, `session_checkpoint` |
| **ADOPTION-ANALYST** | `stream_content`, `analyze_content`, `research_topic` | `web_search`, `search_trends` | `/load-context`, `id_create`, `sot_update` |

---

## 4. Operating Guidelines for Sub-Agents

### Context Loading
- Load the 3 navigation files (`README.md`, `PRD.md`, `CLAUDE.md`) before executing.
- Use `/load-context` command to ensure proper initialization.
- Verify MCP server connectivity before starting research tasks.

### Output Requirements
- Cite every new insight with an ID proposal or update. Untracked output is considered incomplete.
- Deliver outputs as Markdown blocks that AURA/APOLLO/JANUS can paste directly into the PRD, EPIC, or SoT files.
- If a required input is missing, stop and request it rather than guessing.

### Tool Usage
- **Research tools** require MCP server configuration (see [`tools/config/mcp_servers.yaml`](../../tools/config/mcp_servers.yaml)).
- **Methodology tools** are custom commands defined in [`tools/custom_commands/CUSTOM_COMMANDS.md`](../../tools/custom_commands/CUSTOM_COMMANDS.md).
- **Documentation tools** are Python scripts in [`tools/`](../../tools/README.md).

### Session Handoffs
- Use `session_checkpoint` at regular intervals (every 30 minutes or major milestone).
- Before ending, ensure all work is documented in EPIC Section 0.
- Pass relevant context to the next agent via `session_handoff`.

Customize this registry per product—remove unused agents and add domain-specific ones as needed. Always keep the roster synchronized with `agents/` so collaborators know who is active.

---

## 5. Quick Reference: Tool Providers

| Provider | Tools | Setup |
|----------|-------|-------|
| **RivalSearchMCP** | `web_search`, `research_topic`, `retrieve_content`, `analyze_content`, `traverse_website`, `extract_links`, `search_trends`, `get_interest_by_region`, `get_trending_searches`, `stream_content`, `generate_llms_txt` | `claude mcp add RivalSearchMCP --url https://RivalSearchMCP.fastmcp.app/mcp` |
| **Internal** | `validate_sessions.py`, `generate_visuals.py`, `sot_update`, `sot_diff`, `session_checkpoint`, `session_handoff` | Built into repository (`tools/`) |
| **Methodology** | `/load-context`, `/gate-check`, `/harvest-temp`, `/id-register`, `id_create`, `id_link` | Custom commands (`tools/custom_commands/`) |
