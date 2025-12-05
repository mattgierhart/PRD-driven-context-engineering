---
title: "GHM Visualization Suite - Hephaestus-Inspired Design Plan"
version: 1.0
created: 2025-11-23
author: Claude (for CODEX review)
purpose: "Specification for building GHM-native visualization tools inspired by Hephaestus"
status: "Draft - Awaiting CODEX feedback"
extraction_target: "To be determined after review"
---

# GHM Visualization Suite
## A Documentation-First Approach to Visual Context Engineering

> **Inspiration**: Hephaestus (https://github.com/Ido-Levi/Hephaestus) - Semi-Structured Agentic Framework
> **Approach**: Borrow visual concepts and patterns, not execution philosophy
> **License**: AGPL-3.0 (Hephaestus) - we will properly attribute borrowed concepts
> **Our License**: MIT (Gear Heart AI, LLC)

---

## Executive Summary

**Problem**: The Gear Heart Methodology's ID-based knowledge graph, PRD lifecycle, and multi-agent coordination are powerful but **invisible** in markdown. Users struggle to visualize:
- How 200+ IDs interconnect (BR-XXX → API-XXX → TEST-XXX chains)
- Where they are in the v0.1 → v1.0 lifecycle
- Which agents are modifying which artifacts
- Whether documentation has drifted from reality

**Solution**: Build a lightweight **visualization layer** that reads GHM markdown files and renders interactive dashboards, while preserving GHM's documentation-first philosophy.

**Key Principle**: The markdown files remain the source of truth. Visualizations are **read-only views** generated from parsing README.md, PRD.md, EPICs, and SoT files. No new data storage layer.

---

## Design Principles

### 1. **Documentation-First (Not Execution-First)**
- **Hephaestus**: Agents generate code, discover issues, spawn tickets dynamically
- **GHM Viz**: Parse existing markdown, render static snapshots, validate against SoT
- Files are the authority; visualizations are ephemeral views

### 2. **Zero New File Formats**
- No proprietary databases or JSON configs beyond what GHM already uses
- Everything parses from: README.md, PRD.md, CLAUDE.md, EPICs, SoT files
- Output: Interactive HTML dashboards that can be committed to `docs/` or served locally

### 3. **Context-Window Aware**
- Visualizations help agents load *less* context, not more
- "Which IDs do I need for this EPIC?" → show minimal subgraph
- Aligns with GHM's "load precise context via ID" philosophy (workflows/UNIQUE-ID-SYSTEM.md:9-14)

### 4. **Agent Assistance, Not Replacement**
- Visualizations inform agent decisions but don't replace CLAUDE.md behavioral rules
- Agents still update markdown; viz tools just make changes visible
- Complements existing workflow, doesn't rewrite it

### 5. **Progressive Enhancement**
- Can be adopted incrementally (start with 1-2 features)
- Works with partial GHM adoption (e.g., if you only have BR-XXX and API-XXX)
- Degrades gracefully (if parsing fails, shows raw markdown links)

---

## Feature Specifications

### **Feature 1: ID Knowledge Graph Visualizer**

#### What It Does
Parses all SoT files (BUSINESS_RULES.md, API_CONTRACTS.md, USER_JOURNEYS.md, etc.) and renders an **interactive force-directed graph** showing:
- **Nodes**: Each ID (BR-001, API-045, UJ-101, TEST-301, etc.)
- **Edges**: Cross-references (BR-001 → API-045 means "API-045 enforces BR-001")
- **Colors**: Node type (Business Rules = blue, APIs = green, Tests = yellow, etc.)
- **Size**: Number of references (highly-referenced IDs = larger nodes)

**Interactions**:
- Click node → highlight all connected IDs + show markdown excerpt from SoT file
- Filter by type (show only BR-XXX and API-XXX)
- Search for ID → zoom to node
- "Show impact radius" → highlight all IDs affected by changing this one
- "Show orphans" → highlight IDs with zero references (potential cleanup targets)

**Inspired by Hephaestus**:
- Their **dependency graph** showing ticket blocking relationships
- Our adaptation: Show ID cross-references instead of ticket blocks

**What We Borrow**:
1. **Visual concept**: Force-directed graph with colored nodes and clickable edges
2. **Interaction patterns**: Click to highlight, filter by type, zoom to selection
3. **Layout approach**: Organize by relationship density (high-centrality nodes in center)

**What We Build Custom**:
- Markdown parser for SoT files (Hephaestus uses tickets, not markdown)
- ID extraction logic (regex for BR-XXX, API-XXX, UJ-XXX patterns)
- Bidirectional reference validator (check if A→B implies B→A)
- GHM-specific node types and color scheme

**Technology Stack**:
- **Graph Library**: D3.js force-directed graph OR Cytoscape.js (both open-source)
- **Parser**: Python or Node.js script to parse markdown → JSON graph structure
- **Frontend**: Static HTML + JavaScript (no server needed after generation)
- **Alternative**: Graphviz for simpler, non-interactive SVG diagrams

**Effort Estimate**:
- **Markdown parser**: 1 week (regex patterns, cross-reference extraction, validation)
- **Graph generation**: 1 week (convert parsed data to D3.js/Cytoscape format)
- **Interactive UI**: 2 weeks (click handlers, filters, search, zoom, tooltips)
- **Testing & refinement**: 1 week (test on real GHM repos with 100+ IDs)
- **Total: 5 weeks**

**Deliverables**:
- `tools/generate-id-graph.py` - CLI tool: `python generate-id-graph.py → docs/id-graph.html`
- `docs/id-graph.html` - Standalone interactive visualization
- `workflows/ID-GRAPH-USAGE.md` - Guide for interpreting the graph

**Attribution**:
```markdown
## Inspiration
This ID Knowledge Graph Visualizer is inspired by the dependency graph
visualization in Hephaestus (https://github.com/Ido-Levi/Hephaestus),
a semi-structured agentic framework by Ido Levi (AGPL-3.0).

We adapted their visual approach to GHM's ID-based knowledge graph,
but implemented from scratch to align with our documentation-first
methodology.
```

---

### **Feature 2: PRD Lifecycle Progress Bar**

#### What It Does
Parses PRD.md and workflows/PRD_VERSION_LIFECYCLE.md to render a **visual progress indicator** showing:
- Current gate (e.g., v0.6 Architecture)
- Checklist completion percentage per gate (workflows/PRD_VERSION_LIFECYCLE.md:93-153)
- Traffic light status: 🟢 Complete | 🟡 In Progress | 🔴 Blocked
- Next gate requirements with links to checklists

**Example Output**:
```
┌────────────────────────────────────────────────────────┐
│  PRD Lifecycle: v0.1 → v1.0                            │
│                                                        │
│  v0.1 ✅ → v0.2 ✅ → v0.3 ✅ → v0.4 ✅ → v0.5 ✅       │
│         ↓                                              │
│       v0.6 🟡 (67% complete)                          │
│         ├─ Architecture summary ✅                    │
│         ├─ API contracts created ✅                   │
│         ├─ Schema documented 🟡 (in progress)        │
│         └─ Integration requirements 🔴 (blocked)     │
│                                                        │
│  Next Gate: v0.7 Build Execution                      │
│  Requirements: 4 items (view checklist →)             │
└────────────────────────────────────────────────────────┘
```

**Inspired by Hephaestus**:
- Their **Kanban board** showing Backlog → Building → Testing → Done progression
- Our adaptation: Linear lifecycle progression with gate checkpoints

**What We Borrow**:
1. **Visual concept**: Column-based progression with status indicators
2. **Status colors**: Green (done), yellow (in progress), red (blocked)
3. **Percentage completion**: Show how close each gate is to passing

**What We Build Custom**:
- Parser for PRD.md to extract current gate from metadata
- Checklist evaluator (scan for `[x]` vs `[ ]` in gate checklists)
- Blocker detection (if SoT IDs referenced don't exist yet)
- Gate requirement linker (click "view checklist" → jump to relevant section)

**Technology Stack**:
- **Parser**: Python script to extract gate metadata + checklist status
- **Visualization**: HTML/CSS progress bar + SVG timeline
- **Alternative**: Markdown table with emoji indicators (lowest-tech option)

**Effort Estimate**:
- **PRD metadata parser**: 3 days (extract version, gate history)
- **Checklist evaluator**: 1 week (parse markdown checkboxes, validate ID references)
- **Visual timeline**: 1 week (SVG or CSS-based horizontal progress bar)
- **Testing**: 3 days (test across multiple PRD versions)
- **Total: 3 weeks**

**Deliverables**:
- `tools/generate-lifecycle-progress.py` - CLI: `python generate-lifecycle-progress.py`
- Output embedded in `README.md` (replace manual "Current Gate" section)
- Or standalone `docs/lifecycle-dashboard.html`

**Attribution**:
```markdown
This progress bar visualization is inspired by Hephaestus's Kanban
board progression indicators, adapted for GHM's PRD Version Lifecycle.
```

---

### **Feature 3: Agent Activity Stream**

#### What It Does
Parses git commit history and EPIC Section 3A tables to show a **chronological timeline** of:
- Which agent (AURA, APOLLO, JANUS, or human) made changes
- Which files/IDs were modified
- EPIC assignment and phase (Plan/Build/Verify/Wrap)
- Commit messages and timestamps

**Example Output**:
```
┌──────────────────────────────────────────────────────┐
│  Agent Activity Stream (Last 7 Days)                 │
│                                                      │
│  2025-11-23 14:32 | APOLLO | EPIC-03 (Build)       │
│  Modified: API-045, API-046, BR-118                 │
│  Commit: "Add OCR retry endpoint"                    │
│                                                      │
│  2025-11-23 10:15 | AURA | EPIC-02 (Verify)        │
│  Modified: UJ-101, CFD-023                          │
│  Commit: "Updated onboarding journey with feedback" │
│                                                      │
│  2025-11-22 16:45 | JANUS | EPIC-04 (Wrap)         │
│  Modified: DEP-027, deployment_playbook.md          │
│  Commit: "Configured Railway staging environment"   │
└──────────────────────────────────────────────────────┘
```

**Inspired by Hephaestus**:
- Their **agent observability interface** showing agents working in isolated sessions
- Our adaptation: Post-facto timeline of agent contributions (not real-time)

**What We Borrow**:
1. **Visual concept**: Timeline showing agent activity with timestamps
2. **Agent attribution**: Color-code by agent type (strategy, build, ops)
3. **Activity grouping**: Group by EPIC or date range

**What We Build Custom**:
- Git commit parser to extract author, timestamp, files changed
- Agent identifier (look for "AURA:", "APOLLO:", etc. in commit messages, or map authors)
- ID change extractor (parse Section 3A from EPIC files to see what IDs changed)
- Activity aggregator (group by agent, EPIC, or time period)

**Technology Stack**:
- **Git parsing**: `gitpython` library (Python) or `git log --format` commands
- **Visualization**: HTML timeline (vertical scrollable list) or Gantt chart
- **Real-time option** (future): WebSocket server watching git commits

**Effort Estimate**:
- **Git commit parser**: 1 week (extract commits, parse messages, map to agents)
- **Section 3A parser**: 3 days (extract ID changes from EPIC tables)
- **Timeline renderer**: 1 week (HTML/CSS timeline or library like vis.js Timeline)
- **Agent attribution logic**: 3 days (map commit authors → AURA/APOLLO/JANUS)
- **Total: 3 weeks**

**Deliverables**:
- `tools/generate-activity-stream.py` - CLI: `python generate-activity-stream.py --days 7`
- `docs/agent-activity.html` - Scrollable timeline visualization
- Optional: Embed summary in README.md "Recent Changes" section

**Attribution**:
```markdown
This activity stream is inspired by Hephaestus's agent observability
dashboard, adapted to show post-facto git history rather than real-time
monitoring.
```

---

### **Feature 4: Temp File Lifecycle Dashboard**

#### What It Does
Scans `temp/` directory and shows:
- List of all temp files with age (days since creation)
- Owner (parsed from frontmatter or filename)
- Extraction target (which SoT file this should be harvested into)
- Status: 🟢 Fresh (<7 days) | 🟡 Aging (7-14 days) | 🔴 Stale (>14 days)

**Example Output**:
```
┌────────────────────────────────────────────────────────────┐
│  Temp File Lifecycle Dashboard                            │
│                                                            │
│  🔴 temp/feature-household-sharing.md                     │
│     Age: 18 days | Owner: AURA | Target: USER_JOURNEYS.md│
│     Action: Extract UJ-201, UJ-202 → archive             │
│                                                            │
│  🟡 temp/pricing-analysis.md                              │
│     Age: 10 days | Owner: AURA | Target: BUSINESS_RULES.md│
│     Action: Review BR-045 proposal → finalize            │
│                                                            │
│  🟢 temp/deployment-notes.md                              │
│     Age: 3 days | Owner: JANUS | Target: DEP-027         │
│     Action: No action needed yet                          │
└────────────────────────────────────────────────────────────┘
```

**Inspired by Hephaestus**:
- Their **ticket lifecycle** tracking (Backlog → Building → Testing → Done)
- Our adaptation: Track temp file aging and extraction status

**What We Borrow**:
1. **Visual concept**: List view with status indicators and age tracking
2. **Status colors**: Fresh/aging/stale (similar to their ticket states)
3. **Action prompts**: Suggest next steps based on lifecycle state

**What We Build Custom**:
- Temp directory scanner (list `.md` files, extract creation date)
- Frontmatter parser (extract owner, extraction target, expiry date)
- Age calculator (compare creation date to today)
- Archive checker (scan archive/ to see if file was already harvested)

**Technology Stack**:
- **Scanner**: Python `os.walk()` or `pathlib.Path.rglob()`
- **Date parsing**: `datetime` library + git file creation date
- **Visualization**: HTML table with sortable columns OR markdown table

**Effort Estimate**:
- **Directory scanner**: 3 days (recursive scan, filter for .md files)
- **Frontmatter parser**: 3 days (YAML parsing, handle missing fields)
- **Age logic + status**: 2 days (calculate age, assign status)
- **Dashboard renderer**: 1 week (HTML table with sort/filter or simple markdown)
- **Total: 2.5 weeks**

**Deliverables**:
- `tools/scan-temp-files.py` - CLI: `python scan-temp-files.py`
- Output: Markdown table added to README.md "Temp Files" section
- Or standalone: `docs/temp-file-dashboard.html`

**Attribution**:
```markdown
This dashboard is inspired by Hephaestus's ticket lifecycle tracking,
adapted for GHM's temporary file management workflow.
```

---

### **Feature 5: Context Window Optimizer**

#### What It Does
Given an EPIC, recommends the **minimal set of IDs to load** into an agent's context window:
- Reads EPIC Section 3A (IDs modified, created, referenced)
- Reads PRD to find current lifecycle gate requirements
- Traverses ID dependency graph to find transitive dependencies
- Estimates token count for loading those SoT entries
- Suggests "must load" vs "optional" vs "skip" IDs

**Example Output**:
```
┌────────────────────────────────────────────────────────────┐
│  Context Window Optimization for EPIC-03                  │
│                                                            │
│  🔴 MUST LOAD (Core Dependencies):                        │
│     BR-118, API-045, API-046, DBT-018                     │
│     Estimated tokens: 1,200                               │
│                                                            │
│  🟡 OPTIONAL (Related but not blocking):                  │
│     UJ-101, TEST-301, TEST-302                            │
│     Estimated tokens: 800                                 │
│                                                            │
│  🟢 SKIP (Not needed for this EPIC):                      │
│     BR-001, BR-045, CFD-023, DEP-027                      │
│                                                            │
│  Total context if all loaded: 2,000 tokens (10% of window)│
│  Recommendation: Load MUST + OPTIONAL (safe headroom)     │
└────────────────────────────────────────────────────────────┘
```

**Inspired by Hephaestus**:
- Their **dependency tracking** for ticket blocking relationships
- Our adaptation: Dependency tracking for ID loading optimization

**What We Borrow**:
1. **Visual concept**: Categorized list with priority levels (must/optional/skip)
2. **Dependency logic**: Traverse graph to find transitive dependencies
3. **Resource estimation**: Show cost (tokens) of loading each set

**What We Build Custom**:
- EPIC Section 3A parser (extract IDs from markdown tables)
- ID dependency traverser (from ID graph, find all connected IDs)
- Token estimator (count words in SoT entries, multiply by ~1.3 for tokens)
- Priority classifier (must = directly referenced; optional = 1 hop away; skip = 2+ hops)

**Technology Stack**:
- **Parser**: Python to read EPIC Section 3A + SoT files
- **Graph traversal**: NetworkX library (build graph from ID references)
- **Token estimation**: Simple heuristic (words * 1.3) or tiktoken library
- **Output**: Text report or HTML summary

**Effort Estimate**:
- **Section 3A parser**: 3 days (extract tables, list IDs)
- **Graph traversal logic**: 1 week (build dependency graph, implement BFS/DFS)
- **Token estimation**: 3 days (count tokens in SoT entries)
- **Priority classifier**: 1 week (implement must/optional/skip rules)
- **Report generator**: 3 days (format output)
- **Total: 3.5 weeks**

**Deliverables**:
- `tools/optimize-context.py` - CLI: `python optimize-context.py --epic EPIC-03`
- Output: Text report showing recommended IDs to load
- Integration: Add to EPIC template as automated checklist

**Attribution**:
```markdown
This optimizer is inspired by Hephaestus's dependency tracking system,
adapted to optimize AI agent context window usage in GHM workflows.
```

---

### **Feature 6: Documentation Drift Detector**

#### What It Does
Compares claims in PRD.md and README.md against actual SoT specifications to find **inconsistencies**:
- PRD says "Free tier limited to 3 products" → verify BR-001 matches
- README lists API-045 as "modified" → verify it actually exists in API_CONTRACTS.md
- EPIC Section 3A claims TEST-303 created → verify it's in testing_playbook.md
- Identify forward references (PRD references BR-999 which doesn't exist yet)

**Example Output**:
```
┌────────────────────────────────────────────────────────────┐
│  Documentation Drift Report                                │
│                                                            │
│  🔴 CRITICAL MISMATCHES:                                   │
│     PRD.md line 145: References "BR-045" (doesn't exist)  │
│     README.md: Lists API-999 as modified (not in SoT)    │
│                                                            │
│  🟡 WARNINGS:                                              │
│     BR-001 spec: "3 products" but PRD.md says "5 products"│
│     UJ-101 last updated: 2025-10-01 (older than PRD)     │
│                                                            │
│  🟢 VALIDATED:                                             │
│     API-045, API-046, BR-118, TEST-301 all consistent     │
│                                                            │
│  Summary: 2 critical issues, 2 warnings, 147 IDs validated│
└────────────────────────────────────────────────────────────┘
```

**Inspired by Hephaestus**:
- Their **Guardian** that validates agent work stays aligned with phase objectives
- Our adaptation: Guardian validates documentation consistency across files

**What We Borrow**:
1. **Visual concept**: Validation report with severity levels (critical/warning/ok)
2. **Guardian philosophy**: Continuous validation of alignment with rules
3. **Automated checking**: Run as pre-commit hook or scheduled task

**What We Build Custom**:
- ID reference extractor (find all `[BR-XXX]` links in README/PRD/EPICs)
- SoT file validator (check if each referenced ID actually exists)
- Content matcher (compare PRD claims with BR-XXX/API-XXX specifications)
- Staleness detector (compare last-modified dates across files)

**Technology Stack**:
- **Parser**: Python regex to extract ID references from markdown
- **Validator**: Check if each ID has corresponding anchor in SoT files
- **Diff engine**: Simple string matching for content consistency
- **Output**: Markdown report or HTML dashboard

**Effort Estimate**:
- **ID reference extractor**: 1 week (regex patterns, handle various link formats)
- **SoT validator**: 3 days (check file existence, validate anchors)
- **Content matcher**: 2 weeks (parse specs, compare with PRD claims, fuzzy matching)
- **Staleness detector**: 3 days (git file timestamps, compare dates)
- **Report generator**: 1 week (prioritize issues, format output)
- **Total: 5 weeks**

**Deliverables**:
- `tools/validate-documentation.py` - CLI: `python validate-documentation.py`
- `docs/drift-report.html` - Latest validation results
- `.github/workflows/validate-docs.yml` - Optional CI check

**Attribution**:
```markdown
This drift detector is inspired by Hephaestus's Guardian monitoring
system, adapted to validate documentation consistency in GHM repositories.
```

---

## Technology Stack Summary

### Core Technologies
| Component | Technology | Rationale |
|-----------|-----------|-----------|
| **Parsing** | Python 3.10+ | Easy markdown/YAML parsing, rich ecosystem |
| **Graph Visualization** | D3.js or Cytoscape.js | Industry-standard, highly customizable |
| **Timeline Visualization** | vis.js Timeline or custom CSS | Clean timelines, low dependency |
| **Git Integration** | gitpython | Native Python git access |
| **Dependency Graphs** | NetworkX | Graph algorithms (BFS/DFS for traversal) |
| **Frontend** | HTML + vanilla JS | No build step, works offline, committable to repo |
| **Alternative** | React + TypeScript | If building a full web app (overkill for MVP) |

### Libraries & Tools
```python
# requirements.txt
pyyaml>=6.0          # Parse frontmatter
markdown>=3.4        # Parse markdown to AST
gitpython>=3.1       # Read git history
networkx>=3.0        # Graph algorithms
tiktoken>=0.5        # Token estimation (optional)
```

```javascript
// For interactive visualizations
- d3.js v7 (graph visualization)
- cytoscape.js (alternative graph library)
- vis.js Timeline (activity stream)
```

### Borrowed from Hephaestus
We are **NOT forking or copying code** from Hephaestus (AGPL-3.0 would require us to open-source any derivatives). Instead, we borrow:
- **Visual design patterns** (Kanban columns, dependency graphs, timeline layouts)
- **Interaction concepts** (click to highlight, filter by type, zoom to selection)
- **Guardian philosophy** (continuous validation of rule compliance)

**All code will be written from scratch**, aligned with GHM's MIT license.

---

## Phased Rollout Plan

### **Phase 1: Foundation (Weeks 1-5)** - MVP Core
**Goal**: Prove value with highest-impact feature

**Deliverables**:
1. **ID Knowledge Graph Visualizer** (5 weeks)
   - Parsers for SoT files → JSON graph
   - D3.js interactive graph
   - Basic filters (by ID type)
   - Orphan detection

**Success Metrics**:
- Can parse 100+ IDs without crashing
- Graph renders in <3 seconds
- Users can click node → see SoT excerpt
- Identifies at least 5 orphaned IDs in test repo

**Decision Point**: After Phase 1, assess user feedback. If graph isn't valuable, pivot to simpler tools (Markdown + Mermaid). If it is, continue to Phase 2.

---

### **Phase 2: Workflow Integration (Weeks 6-11)** - Daily Use
**Goal**: Integrate into agent workflow for daily visibility

**Deliverables**:
1. **PRD Lifecycle Progress Bar** (3 weeks)
   - Gate completion tracker
   - Embed in README.md
2. **Agent Activity Stream** (3 weeks)
   - Git commit timeline
   - Agent attribution

**Success Metrics**:
- Progress bar updates automatically when gate checklists change
- Activity stream shows last 30 days of changes
- Agents reference viz in EPIC notes ("see activity stream for conflicts")

---

### **Phase 3: Quality & Governance (Weeks 12-19)** - Production
**Goal**: Catch errors and prevent drift

**Deliverables**:
1. **Temp File Lifecycle Dashboard** (2.5 weeks)
   - Temp file scanner + aging report
2. **Context Window Optimizer** (3.5 weeks)
   - Dependency traversal
   - Token estimation
3. **Documentation Drift Detector** (5 weeks)
   - ID reference validator
   - Content consistency checker

**Success Metrics**:
- Drift detector catches 100% of broken ID references in test scenarios
- Context optimizer reduces average context load by 30%
- Temp dashboard prevents files from aging >14 days

---

### **Phase 4: Polish & Scale (Weeks 20-24)** - Open Source Ready
**Goal**: Production-ready, documented, shareable

**Deliverables**:
1. Comprehensive documentation (workflows/GHM-VISUALIZATION-SUITE.md)
2. CI/CD integration (.github/workflows/ for automated validation)
3. Performance optimization (handle 1000+ IDs without lag)
4. Example repos (templates/ with pre-generated visualizations)

**Success Metrics**:
- External user can run `python tools/generate-all.py` and get full suite in <1 minute
- Documentation includes troubleshooting for 10+ common scenarios
- At least 3 other GHM adopters successfully use the tools

---

## Total Effort & Timeline

### Summary by Feature
| Feature | Effort | Priority |
|---------|--------|----------|
| 1. ID Knowledge Graph Visualizer | 5 weeks | P0 (MVP) |
| 2. PRD Lifecycle Progress Bar | 3 weeks | P1 |
| 3. Agent Activity Stream | 3 weeks | P1 |
| 4. Temp File Lifecycle Dashboard | 2.5 weeks | P2 |
| 5. Context Window Optimizer | 3.5 weeks | P2 |
| 6. Documentation Drift Detector | 5 weeks | P1 |
| **Total Development** | **22 weeks** | |
| Documentation & Polish | 2 weeks | |
| **Grand Total** | **24 weeks (~6 months)** | |

### Team Requirements
- **1 full-time engineer** for 6 months (all features)
- **OR 2 part-time engineers** for 3-4 months each (parallel development)
- **Skills needed**: Python, JavaScript/D3.js, markdown parsing, basic graph theory

### Accelerated Timeline (MVP Only)
If you want to validate value quickly:
- **Phase 1 only** (ID Graph Visualizer): 5 weeks
- **Add 1-2 more features**: +6-8 weeks
- **Total MVP**: 11-13 weeks (~3 months)

---

## Code Attribution & Licensing

### Hephaestus Attribution
Every tool will include this notice:

```markdown
## Inspiration & Attribution

This tool is part of the GHM Visualization Suite, inspired by visual
concepts from Hephaestus (https://github.com/Ido-Levi/Hephaestus),
a semi-structured agentic framework by Ido Levi.

**Hephaestus License**: AGPL-3.0
**GHM License**: MIT (Gear Heart AI, LLC)

We adapted Hephaestus's visualization approaches (dependency graphs,
Kanban boards, agent monitoring) to align with Gear Heart Methodology's
documentation-first context engineering workflow.

**No code was copied from Hephaestus.** All implementations are original,
written from scratch to comply with GHM's MIT license. We gratefully
acknowledge the inspiration and design patterns from the Hephaestus project.
```

### Our License
All GHM Visualization Suite code: **MIT License**
- Allows commercial use
- Compatible with GHM's existing MIT license
- Users can fork/modify without AGPL restrictions

### Community Contribution
Once mature, we'll:
1. Share back learnings with Hephaestus community (blog post, GitHub discussion)
2. Link to Hephaestus in GHM docs as "related work"
3. Encourage cross-pollination of ideas (they might borrow our ID graph concept!)

---

## Risks & Mitigations

### Risk 1: Parsing Complexity
**Risk**: GHM markdown files vary in format; parser breaks on edge cases
**Mitigation**:
- Start with strict templates (validate input structure)
- Add "lint" command to check file format before parsing
- Graceful degradation (show raw markdown if parsing fails)

### Risk 2: Graph Performance
**Risk**: 1000+ IDs makes graph unresponsive
**Mitigation**:
- Lazy loading (render visible subgraph, load more on zoom)
- Pre-compute layouts (save positions, don't recalculate every time)
- Offer "simplified view" (collapse related IDs into clusters)

### Risk 3: Maintenance Burden
**Risk**: Tools break when GHM workflow evolves
**Mitigation**:
- Version parsers alongside workflow versions
- Automated tests on example repos (detect breaking changes early)
- Keep visualizations optional (markdown files still work standalone)

### Risk 4: Over-Engineering
**Risk**: Build too much, not enough users
**Mitigation**:
- Start with Phase 1 MVP (ID Graph) only
- Get 5+ users to validate before Phase 2
- Kill features that don't get used (don't force adoption)

### Risk 5: License Conflict
**Risk**: Accidentally copy Hephaestus code, violate AGPL
**Mitigation**:
- Never copy-paste from Hephaestus repository
- Write from scratch using standard libraries (D3.js, NetworkX)
- Legal review before open-sourcing (if needed)

---

## Success Criteria

**After Phase 1 (5 weeks):**
- [ ] Can generate ID graph for PRD-driven-context-engineering repo in <10 seconds
- [ ] Graph identifies all BR-XXX, API-XXX, UJ-XXX, TEST-XXX relationships
- [ ] 3+ users test and provide feedback
- [ ] At least 2 actionable insights (orphaned IDs, missing refs)

**After Phase 3 (19 weeks):**
- [ ] All 6 tools functional and integrated
- [ ] Documentation complete (workflows/ + tools/ + README updates)
- [ ] Drift detector catches 100% of broken references in test scenarios
- [ ] Tools adopted by at least 1 other GHM user

**After Phase 4 (24 weeks):**
- [ ] Open-sourced with MIT license
- [ ] CI/CD pipeline auto-generates visualizations on PR
- [ ] External contributor submits first PR (community validation)
- [ ] Mentioned in at least 1 external blog/article about context engineering

---

## Alternatives Considered

### Option A: Use Obsidian + Plugins
**Pros**: Obsidian Graph View already visualizes markdown links
**Cons**: Requires desktop app, not web-shareable, less customizable
**Verdict**: Good for personal use, not for team dashboards

### Option B: Mermaid Diagrams in Markdown
**Pros**: Zero tooling, renders on GitHub, very lightweight
**Cons**: Static (not interactive), manual updates, limited to simple graphs
**Verdict**: Good complement to visualizations (use for docs), not replacement

### Option C: Full Fork of Hephaestus
**Pros**: Get all features immediately, proven codebase
**Cons**: 3-5 months integration, AGPL license incompatible, execution-first philosophy
**Verdict**: Too much misalignment (covered in original analysis)

### Option D: Commercial Tools (Roam, Notion, etc.)
**Pros**: Polished UX, maintained by vendors
**Cons**: Proprietary, not markdown-based, loses GHM's file-first philosophy
**Verdict**: Breaks core principle (files as source of truth)

**Our Choice**: Build custom, inspired by Hephaestus, aligned with GHM principles.

---

## Next Steps (After CODEX Review)

1. **CODEX Feedback**: Share this plan for technical review
   - Architecture comments?
   - Effort estimates realistic?
   - Any features to add/remove?

2. **Prioritization**: Confirm Phase 1 scope
   - Should we start with ID Graph, or different feature?
   - MVP timeline: 5 weeks or shorter?

3. **Resource Allocation**: Assign engineer(s)
   - Internal team member?
   - Contract developer?
   - Community contribution?

4. **Proof of Concept**: Before committing 5 weeks, consider:
   - 1-week spike: Parse SoT files → generate simple graph with NetworkX/Graphviz
   - If valuable, proceed to full D3.js interactive version
   - If not, pivot to simpler tools (Mermaid, Obsidian, etc.)

5. **Hephaestus Outreach**: Inform Ido Levi
   - Share this plan (transparency)
   - Invite collaboration/feedback
   - Offer to credit prominently

---

## Appendix: Visual Mockups

### ID Knowledge Graph Example
```
          BR-001 ─────────┐
         (Free Tier)      │
              │           │
              ↓           ↓
          API-045     API-012
        (Create)    (Entitlements)
              │           │
              ├───────────┤
              ↓           ↓
          UJ-101      UJ-105
         (Onboard)  (Add Product)
              │           │
              ↓           ↓
         TEST-301    TEST-302
        (Limit)     (Prompt)

[Blue nodes = BR | Green nodes = API | Purple nodes = UJ | Yellow nodes = TEST]
[Click BR-001 → highlights all 6 connected nodes]
[Shows "Impact Radius: 6 IDs affected by changing BR-001"]
```

### PRD Lifecycle Progress
```
v0.1 ✅ ─→ v0.2 ✅ ─→ v0.3 ✅ ─→ v0.4 ✅ ─→ v0.5 ✅
                                               ↓
                                           v0.6 🟡 (67%)
                                               ↓
                                           v0.7 ⚪ (not started)
```

### Agent Activity Stream
```
Timeline →
├─ 2025-11-23 14:32 [APOLLO] Modified API-045, API-046 in EPIC-03
├─ 2025-11-23 10:15 [AURA]   Updated UJ-101 in EPIC-02
└─ 2025-11-22 16:45 [JANUS]  Deployed DEP-027 in EPIC-04
```

---

## Questions for CODEX

1. **Architecture**: Does the "parse markdown → generate static HTML" approach align with your vision? Or prefer a live server?

2. **Priority**: Is ID Graph the right MVP, or should we start with Lifecycle Progress Bar (simpler, faster win)?

3. **Integration**: Should visualizations embed in README.md (text-based), or live as separate docs/*.html files?

4. **Real-Time**: Any value in real-time updates (WebSocket watching file changes), or is batch generation sufficient?

5. **Licensing**: Any concerns about MIT license for this suite, given Hephaestus is AGPL-3.0? (We're not copying code, just concepts)

6. **Team**: Do you have engineering bandwidth, or should we scope for community contributions?

7. **Hephaestus Contact**: Want me to draft an email to Ido Levi sharing this plan?

---

**End of Plan**
*Ready for CODEX review and feedback. Next step: Validate Phase 1 scope and begin proof-of-concept.*
