---
title: "Agent Tools Specification"
version: 1.0
updated: "2025-12-07"
authority: "Tier 1 tool reference for GHM agents"
---

# AGENT_TOOLS.md — Tool Specification for GHM Agents

> **Purpose**: Define the tools available to primary agents and sub-agents across the PRD Version Lifecycle.
> **Usage**: Reference this when configuring agent tooling, MCP servers, or custom commands.

---

## 1. Tool Architecture Overview

GHM agents operate with three categories of tools:

| Category | Description | Examples |
|----------|-------------|----------|
| **Research Tools** | External data gathering via MCP servers | Web search, content retrieval, trends analysis |
| **Methodology Tools** | Internal GHM operations | ID management, gate checks, context loading |
| **Documentation Tools** | File and artifact generation | SoT updates, visualization, validation reports |

### Tool Access by Role

```
┌─────────────────────────────────────────────────────────────────┐
│                     TOOL ACCESS MATRIX                          │
├─────────────────────────────────────────────────────────────────┤
│  AURA (v0.1-v0.5)     │ Research ████████  Methodology ███      │
│  └─ Sub-agents        │ Research ████████  Methodology ██       │
├─────────────────────────────────────────────────────────────────┤
│  APOLLO (v0.6-v0.8)   │ Documentation ████  Methodology ████    │
│  └─ Sub-agents        │ Documentation ███   Methodology ███     │
├─────────────────────────────────────────────────────────────────┤
│  JANUS (v0.8-v1.0)    │ Documentation ███   Methodology ████    │
│  └─ Sub-agents        │ Documentation ██    Methodology ███     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. Research Tools (MCP Servers)

### 2.1 RivalSearchMCP Integration

**Server**: [RivalSearchMCP](https://github.com/damionrashford/RivalSearchMCP)
**Connection**: `https://RivalSearchMCP.fastmcp.app/mcp`

| Tool | Description | Primary Users | Lifecycle Gates |
|------|-------------|---------------|-----------------|
| `web_search` | Advanced search with Cloudflare bypass, multi-engine fallback | SPARK-SCOUT, SEGMENTOR, MOAT-MAPPER, RISK-ORACLE | v0.1-v0.5 |
| `research_topic` | End-to-end comprehensive topic analysis | All research sub-agents | v0.1-v0.5 |
| `retrieve_content` | Extract content from URLs with multiple methods | All agents | v0.1-v1.0 |
| `analyze_content` | AI-powered content extraction and insights | MOAT-MAPPER, SEGMENTOR | v0.2-v0.3 |
| `traverse_website` | Intelligent website exploration (research, docs, map modes) | MOAT-MAPPER, ARCHITECT | v0.3, v0.6 |
| `extract_links` | Analyze and extract links from web pages | All research sub-agents | v0.1-v0.5 |
| `search_trends` | Keyword research and trend analysis | SEGMENTOR, MOAT-MAPPER | v0.2-v0.3 |
| `get_interest_by_region` | Geographic interest data | SEGMENTOR | v0.2 |
| `get_trending_searches` | Current trending topics | SPARK-SCOUT, MOAT-MAPPER | v0.1, v0.3 |
| `stream_content` | Real-time streaming content processing | ADOPTION-ANALYST | v1.0 |
| `generate_llms_txt` | Create LLM-optimized documentation | ARCHITECT, QA-MAESTRO | v0.6-v0.7 |

#### Sub-Agent Tool Mapping

```yaml
# Research Sub-Agents (AURA's team)
SPARK-SCOUT:
  primary_tools:
    - web_search          # Problem/solution research
    - research_topic      # Comprehensive analysis
    - get_trending_searches  # Market signals
  secondary_tools:
    - retrieve_content
    - extract_links

SEGMENTOR:
  primary_tools:
    - web_search          # Segment research
    - analyze_content     # Competitor customer analysis
    - search_trends       # Market sizing signals
    - get_interest_by_region  # Geographic targeting
  secondary_tools:
    - retrieve_content
    - extract_links

MOAT-MAPPER:
  primary_tools:
    - web_search          # Competitor research
    - traverse_website    # Competitor site analysis
    - analyze_content     # Pricing/positioning extraction
    - search_trends       # Market momentum
    - get_trending_searches  # Emerging competitors
  secondary_tools:
    - retrieve_content
    - extract_links

JOURNEY-SCRIBE:
  primary_tools:
    - retrieve_content    # UX research articles
    - analyze_content     # Pattern extraction
  secondary_tools:
    - web_search
    - extract_links

RISK-ORACLE:
  primary_tools:
    - web_search          # Risk research
    - research_topic      # Deep-dive analysis
    - retrieve_content    # Incident reports, case studies
  secondary_tools:
    - analyze_content
    - extract_links
```

### 2.2 Additional Recommended MCP Servers

| Server | Purpose | Primary Users | Setup |
|--------|---------|---------------|-------|
| **Filesystem MCP** | Local file operations | All agents | Built-in with Claude |
| **GitHub MCP** | Repository operations, PR management | APOLLO sub-agents | `claude mcp add github` |
| **Memory MCP** | Persistent context across sessions | All primary agents | `claude mcp add memory` |
| **Playwright MCP** | Browser automation, screenshots | QA-MAESTRO | Custom setup |

---

## 3. Methodology Tools (Internal)

### 3.1 Context Management

| Tool | Command | Description | Users |
|------|---------|-------------|-------|
| **Load Context** | `/load-context` | Load 3+1+SoT stack for session start | All agents |
| **Gate Check** | `/gate-check` | Validate PRD lifecycle gate requirements | AURA, APOLLO, JANUS |
| **Harvest Temp** | `/harvest-temp` | Extract temp files into SoT during EPIC wrap-up | All agents |
| **ID Register** | `/id-register` | Validate ID format and log changes | All agents |

### 3.2 ID Operations

| Tool | Function | Input | Output |
|------|----------|-------|--------|
| `id_validate` | Check ID format compliance | ID string | Pass/fail + reason |
| `id_lookup` | Find ID definition in SoT | ID string | File path + content |
| `id_create` | Create new ID entry | Type, description, metadata | Formatted SoT entry |
| `id_link` | Generate cross-reference | Source ID, target ID | Markdown link |
| `id_orphan_check` | Find unlinked IDs | SoT directory | Orphan report |

### 3.3 Session Management

| Tool | Function | When to Use |
|------|----------|-------------|
| `session_start` | Initialize session state, load EPIC Section 0 | Session begin |
| `session_checkpoint` | Save progress to Section 0 | Every 30 mins or major milestone |
| `session_end` | Finalize session state, commit changes | Session end |
| `session_handoff` | Generate handoff notes for next agent | Context window limit approaching |

---

## 4. Documentation Tools

### 4.1 Visualization Suite

**Location**: `tools/generate_visuals.py`

| Tool | Command | Output | Users |
|------|---------|--------|-------|
| **ID Graph** | `--graph` | SVG/PNG dependency visualization | All agents |
| **Validation** | `--check` | Parsing validation report | CI/CD, QA-MAESTRO |
| **Filtered Graph** | `--graph --ids X,Y` | Subset visualization | Focused analysis |

### 4.2 Session Validation

**Location**: `tools/validate_sessions.py`

| Tool | Command | Output | Users |
|------|---------|--------|-------|
| **EPIC Audit** | `--epic EPIC-XX.md` | Section 0 compliance report | Session end |
| **Full Audit** | `--all` | All EPICs validation | Gate reviews |
| **Strict Mode** | `--all --strict` | Fail on any warning | CI/CD |

### 4.3 SoT Operations

| Tool | Function | Input | Output |
|------|----------|-------|--------|
| `sot_update` | Append/modify SoT entry | ID, content | Updated markdown |
| `sot_template` | Generate blank entry from template | ID type | Template with placeholders |
| `sot_diff` | Compare SoT versions | Two file paths | Change summary |
| `sot_migrate` | Move content between SoT files | Source, target | Migration report |

---

## 5. Tool Specifications by Agent

### 5.1 Primary Agents

#### AURA (Strategy Lead)

```yaml
agent: AURA
lifecycle: v0.1-v0.5
tool_profile: research_heavy

required_tools:
  research:
    - RivalSearchMCP.web_search
    - RivalSearchMCP.research_topic
    - RivalSearchMCP.analyze_content
  methodology:
    - /load-context
    - /gate-check
    - id_validate
    - id_create
  documentation:
    - sot_update
    - session_checkpoint

delegated_tools:  # Via sub-agents
  - SPARK-SCOUT: web_search, research_topic, get_trending_searches
  - SEGMENTOR: search_trends, get_interest_by_region, analyze_content
  - MOAT-MAPPER: traverse_website, search_trends, analyze_content
  - JOURNEY-SCRIBE: retrieve_content, analyze_content
  - RISK-ORACLE: research_topic, web_search

output_artifacts:
  - PRD section updates (v0.1-v0.5)
  - CFD-XXX, BR-XXX, UJ-XXX ID proposals
  - Decision summaries with ID references
  - Hand-off notes for APOLLO
```

#### APOLLO (Build Lead)

```yaml
agent: APOLLO
lifecycle: v0.6-v0.8
tool_profile: documentation_heavy

required_tools:
  research:
    - RivalSearchMCP.retrieve_content  # Technical docs
    - RivalSearchMCP.traverse_website  # API docs exploration
  methodology:
    - /load-context
    - /gate-check
    - /harvest-temp
    - id_validate
    - id_create
    - id_link
  documentation:
    - generate_visuals.py --graph
    - validate_sessions.py
    - sot_update
    - sot_template

delegated_tools:  # Via sub-agents
  - ARCHITECT: traverse_website (docs mode), generate_llms_txt
  - QA-MAESTRO: validate_sessions.py, sot_diff
  - AUTOMATION-RUNNER: session_handoff, sot_update

output_artifacts:
  - Architecture documentation (API-XXX, DBT-XXX)
  - Test specifications (TEST-XXX)
  - Deployment playbooks (DEP-XXX)
  - ID knowledge graphs
```

#### JANUS (Ops/GTM Lead)

```yaml
agent: JANUS
lifecycle: v0.8-v1.0
tool_profile: ops_focused

required_tools:
  research:
    - RivalSearchMCP.stream_content  # Real-time monitoring
    - RivalSearchMCP.search_trends   # Launch timing
  methodology:
    - /load-context
    - /gate-check
    - id_validate
    - id_link
  documentation:
    - sot_update
    - generate_visuals.py

delegated_tools:  # Via sub-agents
  - LAUNCH-CALLER: search_trends, session_checkpoint
  - ADOPTION-ANALYST: stream_content, analyze_content, research_topic

output_artifacts:
  - Launch plans (GTM-XXX)
  - Metrics dashboards (KPI-XXX)
  - Feedback loop updates (CFD-XXX)
  - Adoption reports
```

### 5.2 Sub-Agent Tool Cards

Each sub-agent has a focused tool set. Full specifications below.

---

#### SPARK-SCOUT (v0.1)

```yaml
sub_agent: SPARK-SCOUT
reports_to: AURA
lifecycle_gate: v0.1 Spark
core_question: "Is this the right problem and what outcomes matter?"

tools:
  primary:
    - name: web_search
      provider: RivalSearchMCP
      use_case: "Research problem space, existing solutions, market pain points"
      example_queries:
        - "{problem_domain} challenges {target_industry}"
        - "why do {target_users} struggle with {pain_point}"
        - "{competitor_category} alternatives comparison"

    - name: research_topic
      provider: RivalSearchMCP
      use_case: "Deep-dive comprehensive analysis of problem domain"
      example_prompt: "Research the landscape of {problem_domain} including key players, common pain points, and unmet needs"

    - name: get_trending_searches
      provider: RivalSearchMCP
      use_case: "Identify emerging problems and market signals"

  secondary:
    - name: retrieve_content
      provider: RivalSearchMCP
      use_case: "Extract specific content from industry reports, blog posts"

    - name: extract_links
      provider: RivalSearchMCP
      use_case: "Build research corpus from initial sources"

  methodology:
    - /load-context
    - id_create (CFD-XXX)
    - session_checkpoint

outputs:
  - Refined problem statement
  - Desired outcomes with measurable signals
  - Constraints and dependencies
  - CFD-XXX ID proposals for research findings
  - Open questions gating v0.2
```

---

#### SEGMENTOR (v0.2)

```yaml
sub_agent: SEGMENTOR
reports_to: AURA
lifecycle_gate: v0.2 Market Definition
core_question: "Who exactly is this for (and not for)?"

tools:
  primary:
    - name: web_search
      provider: RivalSearchMCP
      use_case: "Research target segments, buyer personas, market sizing"
      example_queries:
        - "{segment_name} demographics statistics"
        - "{industry} buyer persona characteristics"
        - "who buys {competitor_product}"

    - name: analyze_content
      provider: RivalSearchMCP
      use_case: "Extract segment insights from competitor case studies, reviews"
      example_prompt: "Analyze customer segments mentioned in this content, identify pain points by segment"

    - name: search_trends
      provider: RivalSearchMCP
      use_case: "Understand segment behavior patterns over time"

    - name: get_interest_by_region
      provider: RivalSearchMCP
      use_case: "Geographic targeting for initial market"

  secondary:
    - name: retrieve_content
      use_case: "Industry reports, census data, market research"

    - name: extract_links
      use_case: "Discover segment-specific communities and forums"

  methodology:
    - /load-context
    - id_create (CFD-XXX, BR-XXX)
    - session_checkpoint

outputs:
  - 1-3 ICP definitions with pains & urgency
  - "Not for" exclusion list with rationale
  - Segment size estimates with sources
  - CFD-XXX, BR-XXX ID proposals
  - Geographic/demographic targeting recommendations
```

---

#### MOAT-MAPPER (v0.3)

```yaml
sub_agent: MOAT-MAPPER
reports_to: AURA
lifecycle_gate: v0.3 Commercial Model
core_question: "How do we win vs competitors and monetize?"

tools:
  primary:
    - name: web_search
      provider: RivalSearchMCP
      use_case: "Competitor research, pricing intelligence, market positioning"
      example_queries:
        - "{competitor} pricing plans"
        - "{product_category} market share"
        - "{competitor} vs {competitor} comparison"

    - name: traverse_website
      provider: RivalSearchMCP
      mode: research
      use_case: "Deep exploration of competitor sites for pricing, features, positioning"
      targets:
        - Pricing pages
        - Feature comparison pages
        - Case studies and testimonials

    - name: analyze_content
      provider: RivalSearchMCP
      use_case: "Extract competitive intelligence from landing pages, reviews"
      example_prompt: "Extract pricing model, key features, and positioning from this competitor page"

    - name: search_trends
      provider: RivalSearchMCP
      use_case: "Identify momentum in competitive landscape"

    - name: get_trending_searches
      provider: RivalSearchMCP
      use_case: "Spot emerging competitors and alternative solutions"

  secondary:
    - name: retrieve_content
      use_case: "Analyst reports, G2/Capterra reviews"

    - name: extract_links
      use_case: "Build competitive intelligence link graph"

  methodology:
    - /load-context
    - id_create (BR-XXX, CFD-XXX)
    - session_checkpoint

outputs:
  - Anchor competitor profiles (3-5)
  - Pricing model analysis and recommendations
  - Fast-follow positioning (1-10% delta strategy)
  - Monetization hypotheses
  - BR-XXX, CFD-XXX ID proposals
```

---

#### JOURNEY-SCRIBE (v0.4)

```yaml
sub_agent: JOURNEY-SCRIBE
reports_to: AURA
lifecycle_gate: v0.4 User Journeys
core_question: "What does the user do step-by-step?"

tools:
  primary:
    - name: retrieve_content
      provider: RivalSearchMCP
      use_case: "UX research articles, journey mapping guides, competitor walkthroughs"

    - name: analyze_content
      provider: RivalSearchMCP
      use_case: "Extract journey patterns from case studies and user research"
      example_prompt: "Identify the key user journey steps, pain points, and value moments in this content"

  secondary:
    - name: web_search
      use_case: "Find UX patterns, journey templates, accessibility guidelines"

    - name: extract_links
      use_case: "Build reference corpus for UX patterns"

  methodology:
    - /load-context
    - id_create (UJ-XXX)
    - id_link (to BR-XXX, API-XXX dependencies)
    - session_checkpoint

outputs:
  - 3-7 user journeys with:
    - Persona reference
    - Trigger event
    - Step-by-step flow
    - Pain points per step
    - Value moments
  - UJ-XXX ID proposals
  - Dependency notes (BR-XXX, API-XXX requirements)
```

---

#### RISK-ORACLE (v0.5)

```yaml
sub_agent: RISK-ORACLE
reports_to: AURA
lifecycle_gate: v0.5 Red Team Review
core_question: "How could this fail and how do we mitigate it?"

tools:
  primary:
    - name: web_search
      provider: RivalSearchMCP
      use_case: "Research failure modes, post-mortems, industry risks"
      example_queries:
        - "{product_type} startup failures"
        - "{industry} security incidents"
        - "{technology} scalability issues"

    - name: research_topic
      provider: RivalSearchMCP
      use_case: "Comprehensive risk domain analysis"
      example_prompt: "Research common failure modes for {product_category} products including market, technical, and operational risks"

    - name: retrieve_content
      provider: RivalSearchMCP
      use_case: "Incident reports, post-mortems, security advisories"

  secondary:
    - name: analyze_content
      use_case: "Extract risk patterns from case studies"

    - name: extract_links
      use_case: "Build risk reference library"

  methodology:
    - /load-context
    - id_create (BR-XXX, TEST-XXX)
    - id_link
    - session_checkpoint

outputs:
  - Risk table by category:
    - Market risks
    - Product risks
    - Technical risks
    - Operational risks
  - Early warning signals per risk
  - Mitigation strategies with ownership
  - BR-XXX, TEST-XXX ID proposals
  - Development challenges for APOLLO
```

---

#### ARCHITECT (v0.6)

```yaml
sub_agent: ARCHITECT
reports_to: APOLLO
lifecycle_gate: v0.6 Architecture
core_question: "What technical blueprint satisfies the constraints?"

tools:
  primary:
    - name: traverse_website
      provider: RivalSearchMCP
      mode: docs
      use_case: "Explore technical documentation, API references"
      targets:
        - Framework documentation
        - Cloud provider docs
        - Third-party API references

    - name: generate_llms_txt
      provider: RivalSearchMCP
      use_case: "Create LLM-optimized documentation for architecture decisions"

    - name: retrieve_content
      provider: RivalSearchMCP
      use_case: "Extract technical specifications, best practices"

  secondary:
    - name: web_search
      use_case: "Research architectural patterns, technology comparisons"

    - name: analyze_content
      use_case: "Extract patterns from technical articles"

  methodology:
    - /load-context
    - id_create (API-XXX, DBT-XXX)
    - id_link
    - generate_visuals.py --graph
    - session_checkpoint

outputs:
  - Architecture decision records (ADRs)
  - API-XXX contract definitions
  - DBT-XXX schema specifications
  - Integration plan with third parties
  - Technical constraints for QA-MAESTRO
```

---

#### QA-MAESTRO (v0.7)

```yaml
sub_agent: QA-MAESTRO
reports_to: APOLLO
lifecycle_gate: v0.7 Build Execution
core_question: "How do we prove this works?"

tools:
  primary:
    - name: validate_sessions.py
      provider: internal
      use_case: "Validate EPIC Session State compliance"

    - name: sot_diff
      provider: internal
      use_case: "Track changes to SoT entries during testing"

  secondary:
    - name: retrieve_content
      provider: RivalSearchMCP
      use_case: "Testing best practices, framework documentation"

    - name: web_search
      use_case: "Research testing patterns, coverage strategies"

  methodology:
    - /load-context
    - id_create (TEST-XXX)
    - id_link
    - generate_visuals.py --check
    - session_checkpoint

outputs:
  - Test strategy document
  - TEST-XXX specifications
  - Coverage reports
  - Regression test plans
  - Integration test scenarios
```

---

#### AUTOMATION-RUNNER (v0.8)

```yaml
sub_agent: AUTOMATION-RUNNER
reports_to: APOLLO
lifecycle_gate: v0.8 Deployment & Ops
core_question: "How do we ship and operate safely?"

tools:
  primary:
    - name: sot_update
      provider: internal
      use_case: "Update deployment playbooks and runbooks"

    - name: session_handoff
      provider: internal
      use_case: "Prepare ops handoff documentation"

  secondary:
    - name: retrieve_content
      provider: RivalSearchMCP
      use_case: "Cloud provider deployment guides, CI/CD documentation"

    - name: web_search
      use_case: "Research deployment patterns, monitoring solutions"

  methodology:
    - /load-context
    - id_create (DEP-XXX)
    - id_link
    - /harvest-temp
    - session_checkpoint

outputs:
  - DEP-XXX deployment specifications
  - Release checklists
  - Monitoring and alerting configurations
  - Rollback procedures
  - SLO definitions
```

---

#### LAUNCH-CALLER (v0.9)

```yaml
sub_agent: LAUNCH-CALLER
reports_to: JANUS
lifecycle_gate: v0.9 Go-to-Market
core_question: "How do we coordinate launch and measure success?"

tools:
  primary:
    - name: search_trends
      provider: RivalSearchMCP
      use_case: "Identify optimal launch timing"

    - name: session_checkpoint
      provider: internal
      use_case: "Track launch preparation progress"

  secondary:
    - name: web_search
      use_case: "Research launch strategies, GTM patterns"

    - name: analyze_content
      use_case: "Extract launch insights from case studies"

  methodology:
    - /load-context
    - id_create (GTM-XXX, KPI-XXX)
    - id_link
    - session_checkpoint

outputs:
  - Launch plan with timeline
  - GTM-XXX specifications
  - Analytics instrumentation plan
  - KPI-XXX success metrics
  - Feedback loop configuration
```

---

#### ADOPTION-ANALYST (v1.0)

```yaml
sub_agent: ADOPTION-ANALYST
reports_to: JANUS
lifecycle_gate: v1.0 Market Adoption
core_question: "What signals prove we have market traction?"

tools:
  primary:
    - name: stream_content
      provider: RivalSearchMCP
      use_case: "Real-time monitoring of market signals, mentions, reviews"

    - name: analyze_content
      provider: RivalSearchMCP
      use_case: "Extract insights from user feedback, reviews"

    - name: research_topic
      provider: RivalSearchMCP
      use_case: "Comprehensive analysis of market reception"

  secondary:
    - name: web_search
      use_case: "Track mentions, reviews, competitive responses"

    - name: search_trends
      use_case: "Monitor trend trajectory"

  methodology:
    - /load-context
    - id_create (KPI-XXX, CFD-XXX)
    - id_link
    - sot_update
    - session_checkpoint

outputs:
  - Adoption metrics report
  - KPI-XXX performance tracking
  - CFD-XXX user feedback entries
  - Optimization backlog
  - Competitive response analysis
```

---

## 6. MCP Configuration

### 6.1 Claude Code Setup

```bash
# Add RivalSearchMCP for research capabilities
claude mcp add RivalSearchMCP --url https://RivalSearchMCP.fastmcp.app/mcp

# Verify installation
claude mcp list
```

### 6.2 Claude Desktop Configuration

Add to Claude Desktop settings:

```json
{
  "mcpServers": {
    "RivalSearchMCP": {
      "url": "https://RivalSearchMCP.fastmcp.app/mcp",
      "description": "Web research, content discovery, and trends analysis"
    }
  }
}
```

### 6.3 Cursor/VS Code Configuration

Add to `.cursor/mcp.json` or VS Code MCP settings:

```json
{
  "servers": {
    "RivalSearchMCP": {
      "url": "https://RivalSearchMCP.fastmcp.app/mcp"
    }
  }
}
```

---

## 7. Tool Usage Patterns

### 7.1 Research Phase Pattern (v0.1-v0.5)

```
1. AURA activates sub-agent (e.g., SPARK-SCOUT)
2. Sub-agent loads context: /load-context
3. Sub-agent uses research tools:
   - web_search for broad discovery
   - research_topic for deep analysis
   - analyze_content for extraction
4. Sub-agent creates IDs: id_create (CFD-XXX)
5. Sub-agent checkpoints: session_checkpoint
6. Sub-agent returns structured output to AURA
7. AURA integrates into PRD section
```

### 7.2 Build Phase Pattern (v0.6-v0.8)

```
1. APOLLO loads context: /load-context
2. ARCHITECT uses traverse_website (docs mode) for technical research
3. Implementation proceeds with IDE tools
4. QA-MAESTRO validates: validate_sessions.py, generate_visuals.py --check
5. AUTOMATION-RUNNER prepares deployment: sot_update (DEP-XXX)
6. Gate check: /gate-check
7. Handoff: session_handoff for JANUS
```

### 7.3 Launch Phase Pattern (v0.8-v1.0)

```
1. JANUS loads context: /load-context
2. LAUNCH-CALLER uses search_trends for timing analysis
3. Launch execution
4. ADOPTION-ANALYST uses stream_content for real-time monitoring
5. ADOPTION-ANALYST uses analyze_content for feedback analysis
6. Metrics update: sot_update (KPI-XXX, CFD-XXX)
7. Final gate check: /gate-check
```

---

## 8. Extending the Tool Set

### 8.1 Adding New MCP Servers

1. Identify capability gap in agent workflow
2. Research available MCP servers (see [MCP Server Registry](https://github.com/modelcontextprotocol/servers))
3. Add to configuration (Section 6)
4. Document in this file with:
   - Server name and URL
   - Tools provided
   - Primary users
   - Lifecycle gates
5. Update sub-agent tool cards as needed

### 8.2 Creating Custom Methodology Tools

1. Define tool in `tools/custom_commands/CUSTOM_COMMANDS.md`
2. Implement automation in `tools/` if needed
3. Add to Section 3 of this document
4. Reference in relevant sub-agent tool cards

### 8.3 Tool Versioning

When tool capabilities change:
1. Update this document's version and date
2. Note breaking changes in CHANGELOG
3. Update affected sub-agent tool cards
4. Communicate changes via README "Latest Change Notes"

---

## 9. Reference Index

- MCP Protocol: [Model Context Protocol](https://modelcontextprotocol.io/)
- RivalSearchMCP: [GitHub Repository](https://github.com/damionrashford/RivalSearchMCP)
- Sub-Agent Registry: [`SUBAGENT_REGISTRY.md`](./SUBAGENT_REGISTRY.md)
- Custom Commands: [`tools/custom_commands/CUSTOM_COMMANDS.md`](../../tools/custom_commands/CUSTOM_COMMANDS.md)
- Visualization Suite: [`tools/README.md`](../../tools/README.md)

---

*Maintain this document as the authoritative source for agent tooling. When workflows evolve, update tool cards here first, then propagate to templates.*
