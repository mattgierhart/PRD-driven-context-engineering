# AI Workforce

This directory contains the tools, skills, and configurations for the AI Agents working on this project.

## Structure

- **`tools/`**: Python scripts and utilities (Skills) that Agents can execute.
- **`.Claude/`**: Specific configuration rules for Claude.
- **`.Gemini/`**: Specific configuration rules for Gemini.

## Agent Manifest (The Roster)

### 1. Research Lineup (v0.1 → v0.5)

> **Goal**: Validate strategy and find the "Moat".

| Agent              | Lifecycle Gate  | Core Question                | Tools                                                     |
| ------------------ | --------------- | ---------------------------- | --------------------------------------------------------- |
| **SPARK-SCOUT**    | v0.1 Spark      | "Is this the right problem?" | `web_search`, `research_topic`, `get_trending_searches`   |
| **SEGMENTOR**      | v0.2 Market     | "Who is this for?"           | `web_search`, `analyze_content`, `get_interest_by_region` |
| **MOAT-MAPPER**    | v0.3 Commercial | "Where is the gap?"          | `traverse_website`, `analyze_content`, `search_trends`    |
| **JOURNEY-SCRIBE** | v0.4 Journeys   | "What is the flow?"          | `retrieve_content`, `analyze_content`                     |
| **RISK-ORACLE**    | v0.5 Red Team   | "How does this fail?"        | `web_search`, `research_topic`                            |

### 2. Build Lineup (v0.6 → v0.8)

> **Goal**: Execute the Architecture and Code.

| Agent                 | Lifecycle Gate | Core Question            | Tools                                          |
| --------------------- | -------------- | ------------------------ | ---------------------------------------------- |
| **ARCHITECT**         | v0.6 Specs     | "What is the blueprint?" | `traverse_website` (docs), `generate_llms_txt` |
| **QA-MAESTRO**        | v0.7 Build     | "Does it work?"          | `validate_sessions`, `sot_diff`                |
| **AUTOMATION-RUNNER** | v0.8 Release   | "How do we ship?"        | `sot_update`, `session_handoff`                |

### 3. GTM Lineup (v0.8 → v1.0)

> **Goal**: Launch and Expand.

| Agent                | Lifecycle Gate | Core Question           | Tools                                 |
| -------------------- | -------------- | ----------------------- | ------------------------------------- |
| **LAUNCH-CALLER**    | v0.9 Launch    | "Are we go for launch?" | `search_trends`, `session_checkpoint` |
| **ADOPTION-ANALYST** | v1.0 Growth    | "Are they staying?"     | `stream_content`, `analyze_content`   |

---

## Tool Reference

### Research Tools (MCP)

Provided by [RivalSearchMCP](https://github.com/damionrashford/RivalSearchMCP).

- `web_search`: Multi-engine search.
- `traverse_website`: Deep crawl for docs or competitor pricing.
- `analyze_content`: Extract insights from text.
- `search_trends`: SEO and volume analysis.

### Internal Tools (`agents/tools/`)

- `generate_visuals.py`: Create dependency graphs.
- `validate_sessions.py`: Audit EPIC compliance.

### Methodology Tools

- `/load-context`: Load the navigation stack.
- `/gate-check`: Verify DoD.
- `id_create`: Generate `BR-XXX` or `UJ-XXX`.
