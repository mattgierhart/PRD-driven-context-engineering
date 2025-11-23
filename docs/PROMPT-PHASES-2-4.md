# Prompt: Develop GHM Visualization Suite Phases 2-4

## Context: What We've Built (Phase 1 - Complete ✅)

We've implemented a **documentation-first visualization layer** for the Gear Heart Methodology (GHM), inspired by Hephaestus but built from scratch.

### Phase 1 Achievements

**What's Working:**
- **ID Knowledge Graph** - Parses Source of Truth (SoT) markdown files, extracts IDs (BR-XXX, API-XXX, UJ-XXX, etc.), generates static Graphviz SVG graphs
- **Validation** - Identifies orphaned IDs (no connections) and missing references (referenced but not defined)
- **Provenance Tracking** - Captures git SHA, config hash, build timestamps
- **CLI Tool** - Single driver script: `python tools/generate-visuals.py --all`
- **Configuration** - YAML-driven (`tools/config/visuals.yaml`) with color mappings, ID patterns, file globs

**Architecture:**
```
tools/
├── generate-visuals.py          # Main driver (imports feature modules)
├── config/
│   ├── visuals.yaml            # Configuration
│   └── agents.yaml             # Agent role mapping
├── parsers/
│   └── sot_parser.py           # Extracts IDs from markdown
├── generators/
│   └── graph_generator.py      # Graphviz DOT → SVG
└── utils/
    ├── id_extractor.py         # Regex-based ID extraction
    ├── provenance.py           # Git metadata
    └── attribution.py          # Hephaestus credit blocks
```

**Key Design Principles (from CODEX Review):**
1. **Deterministic Before Interactive** - Static graphs first, D3.js later
2. **Documentation as Source of Truth** - Markdown files are authority, visualizations are views
3. **Git-Tracked Outputs** - Commit to `docs/generated/` for diffable artifacts
4. **Single Driver Script** - Modular feature imports, predictable CLI
5. **Graceful Degradation** - Partial results + warnings on parse errors
6. **Provenance** - Every artifact includes git SHA, config hash, timestamps

**Relevant Documentation:**
- `docs/ghm-visualization-suite-plan.md` - Full 12-week roadmap
- `docs/ghm-visualization-suite-review.md` - CODEX's technical review
- `tools/README.md` - Architecture, usage, troubleshooting
- `README.md` (root) - GHM methodology overview
- `workflows/UNIQUE-ID-SYSTEM.md` - ID system specification
- `workflows/PRD-VERSION-LIFECYCLE.md` - v0.1 → v1.0 lifecycle gates

---

## What We're Building: The Vision

The GHM Visualization Suite helps users **see** their documentation instead of just reading markdown:

1. **ID Knowledge Graph** (Phase 1 ✅) - Show how IDs interconnect
2. **PRD Lifecycle Progress** (Phase 2) - Visual v0.1 → v1.0 tracker
3. **Documentation Drift Detector** (Phase 2) - Catch broken references
4. **Agent Activity Stream** (Phase 2) - Git timeline showing AURA/APOLLO/JANUS work
5. **Temp File Dashboard** (Phase 3) - Aging monitor for temp/ files
6. **Context Window Optimizer** (Phase 3) - Recommend minimal ID set per EPIC

**Cost:** $0 (static files, no server needed)
**Hosting:** GitHub Pages, blob view, or local
**License:** MIT (all code original, Hephaestus inspiration only)

---

## Your Task: Implement Phases 2-4

Build the remaining 5 features following the established patterns from Phase 1.

### Phase 2 (Weeks 2-8) - Core Features

#### Feature 2.1: PRD Lifecycle Progress Bar

**What:** Visual indicator of v0.1 → v1.0 progression with gate completion percentages

**Input:**
- `PRD.md` (extract current gate from metadata)
- `workflows/PRD-VERSION-LIFECYCLE.md` (gate checklists at lines 93-153)

**Output:**
- `docs/generated/lifecycle-progress.md` - Embeddable markdown badge
- `docs/generated/lifecycle-progress.html` - Rich HTML timeline (optional)

**Requirements (from CODEX):**
- Parse gates directly from `PRD-VERSION-LIFECYCLE.md` (don't duplicate checklists)
- Emit both markdown badge (for README) AND rich HTML
- Idempotent generation (minimal diff noise)
- Show: current gate, % complete, traffic light (🟢/🟡/🔴), next requirements

**Example Output:**
```
v0.1 ✅ → v0.2 ✅ → v0.3 ✅ → v0.4 ✅ → v0.5 ✅ → v0.6 🟡 (67%)
                                                      ↓
                                                  v0.7 ⚪ (not started)

Current: v0.6 Architecture (67% complete)
  ✅ Architecture summary
  ✅ API contracts created
  🟡 Schema documented (in progress)
  🔴 Integration requirements (blocked)

Next Gate: v0.7 Build Execution (4 requirements)
```

**Implementation:**
- Add `tools/parsers/prd_parser.py` - Extract gate metadata from PRD
- Add `tools/generators/progress_generator.py` - Generate progress bar
- Update `tools/generate-visuals.py` - Add `--progress` flag
- Estimate: 3 weeks

---

#### Feature 2.2: Documentation Drift Detector

**What:** Validates ID references across files, catches inconsistencies

**Input:**
- All markdown files (README, PRD, EPICs, SoT)
- Parsed ID graph from Phase 1

**Output:**
- `docs/generated/drift-report.md` - Human-readable report
- `docs/generated/drift-report.json` - Machine-readable (for CI)

**Requirements (from CODEX):**
- **Stage 1 (ship first):** Broken/missing ID detection
- **Stage 2:** Staleness detection (git timestamps)
- **Stage 3 (future):** Semantic claim checks
- Machine-readable JSON + human Markdown
- CI can fail on critical issues
- Toggleable stages via config

**Example Output:**
```
# Documentation Drift Report

## 🔴 Critical Issues (2)
- README.md:145 references BR-045 (does NOT exist in BUSINESS_RULES.md)
- EPIC-03.md Section 3A lists API-999 as modified (NOT found in API_CONTRACTS.md)

## 🟡 Warnings (2)
- BR-001 spec says "3 products" but PRD.md line 78 says "5 products"
- UJ-101 last modified: 2025-10-01 (older than PRD by 45 days)

## 🟢 Validated (147 IDs)
All references resolve correctly
```

**Implementation:**
- Add `tools/generators/drift_detector.py`
- Reuse `sot_parser.py` from Phase 1
- Add `--check-drift` flag
- Estimate: 5 weeks (3 stages)

---

#### Feature 2.3: Agent Activity Stream

**What:** Git timeline showing which agent (AURA/APOLLO/JANUS) modified which IDs

**Input:**
- Git commit history (`git log --format=...`)
- EPIC Section 3A tables (which IDs changed)
- `tools/config/agents.yaml` (author → agent mapping)

**Output:**
- `docs/generated/agent-activity.html` - Scrollable timeline

**Requirements (from CODEX):**
- Parse git metadata (not just commit messages) for attribution
- Mapping file: `tools/config/agents.yaml` (authors → agent roles)
- Privacy guard: strip emails unless explicitly allowed
- Filter by EPIC, agent, or date range

**Example Output:**
```
┌──────────────────────────────────────────────────────┐
│  Agent Activity Stream (Last 30 Days)               │
│                                                      │
│  2025-11-23 14:32 | APOLLO | EPIC-03 (Build)       │
│  Modified: API-045, API-046, BR-118                 │
│  Commit: "Add OCR retry endpoint"                   │
│                                                      │
│  2025-11-23 10:15 | AURA | EPIC-02 (Verify)        │
│  Modified: UJ-101, CFD-023                          │
│  Commit: "Updated onboarding journey"               │
└──────────────────────────────────────────────────────┘
```

**Implementation:**
- Add `tools/parsers/git_parser.py` - Use `gitpython` library
- Add `tools/parsers/epic_parser.py` - Extract Section 3A
- Add `tools/generators/activity_generator.py` - Timeline HTML
- Estimate: 3 weeks

---

### Phase 3 (Weeks 9-12) - Advanced Features

#### Feature 3.1: Temp File Lifecycle Dashboard

**What:** Scans `temp/` directory, shows age/owner/extraction status

**Input:**
- `temp/` directory (recursive scan)
- Frontmatter metadata (owner, extraction_target, expiry)
- Git file creation dates

**Output:**
- `docs/generated/temp-dashboard.md` - Sortable table

**Requirements (from CODEX):**
- Mark files with open extraction PRs (parse branch names if possible)
- Graceful frontmatter handling (fallback to git metadata)
- Age thresholds: 🟢 Fresh (<7d), 🟡 Aging (7-14d), 🔴 Stale (>14d)

**Example Output:**
```
# Temp File Lifecycle Dashboard

🔴 temp/feature-household-sharing.md
   Age: 18 days | Owner: AURA | Target: USER-JOURNEYS.md
   Action: Extract UJ-201, UJ-202 → archive

🟡 temp/pricing-analysis.md
   Age: 10 days | Owner: AURA | Target: BUSINESS_RULES.md
   Action: Review BR-045 proposal → finalize
```

**Implementation:**
- Add `tools/generators/temp_scanner.py`
- Add frontmatter parser (YAML)
- Estimate: 2.5 weeks

---

#### Feature 3.2: Context Window Optimizer

**What:** Recommends minimal set of IDs to load for an EPIC

**Input:**
- EPIC Section 3A (IDs modified, created, referenced)
- ID dependency graph from Phase 1
- Token estimation heuristic

**Output:**
- Text report showing MUST/OPTIONAL/SKIP IDs

**Requirements (from CODEX):**
- **Start with non-transitive mode** (direct references only)
- Prove accuracy before enabling transitive traversal
- Token estimates with model-switching via config
- Clear heuristic disclaimer

**Example Output:**
```
# Context Window Optimization for EPIC-03

🔴 MUST LOAD (Core Dependencies):
   BR-118, API-045, API-046, DBT-018
   Estimated tokens: 1,200

🟡 OPTIONAL (Related but not blocking):
   UJ-101, TEST-301, TEST-302
   Estimated tokens: 800

🟢 SKIP (Not needed for this EPIC):
   BR-001, BR-045, CFD-023

Total if all loaded: 2,000 tokens (10% of window)
Recommendation: Load MUST + OPTIONAL (safe headroom)
```

**Implementation:**
- Add `tools/generators/context_optimizer.py`
- Use NetworkX for graph traversal (add to requirements.txt)
- Add tiktoken for token estimation (optional)
- Estimate: 3.5 weeks

---

## Phase 4 (Optional) - Polish & Scale

- Performance optimization (handle 1000+ IDs)
- Interactive D3.js graphs (upgrade from static Graphviz)
- CI/CD integration (.github/workflows/)
- External user testing

---

## Technical Constraints

### Must Follow
1. **Modular imports** - Add new parsers/generators, import in `generate-visuals.py`
2. **Config-driven** - Tunables in `visuals.yaml`, not hardcoded
3. **Deterministic** - Sorted output for minimal git diffs
4. **Provenance** - Include git SHA, config hash in all artifacts
5. **Graceful degradation** - Emit partial results + warnings on errors
6. **Attribution** - Include Hephaestus credit in generated files

### Existing Patterns to Reuse
- `tools/utils/id_extractor.py` - Regex patterns for IDs
- `tools/utils/provenance.py` - Git SHA + metadata
- `tools/utils/attribution.py` - Credit text
- `tools/parsers/sot_parser.py` - Markdown parsing example

### Dependencies
- **Current:** `pyyaml` only
- **Add for Phase 2:** `gitpython` (git log parsing)
- **Add for Phase 3:** `networkx` (graph traversal), `tiktoken` (token estimation - optional)

---

## Success Criteria

### Phase 2 (Weeks 2-8)
- [ ] Progress bar shows v0.1 → v1.0 with % complete
- [ ] Drift detector catches 100% of broken references in test repo
- [ ] Activity stream shows last 30 days of git history

### Phase 3 (Weeks 9-12)
- [ ] Temp dashboard identifies files >14 days old
- [ ] Context optimizer reduces token usage by 30%
- [ ] All features integrated in `--all` mode

---

## Questions to Answer

1. **Architecture:** Should we create a `BaseGenerator` class for common functionality (provenance, attribution)?
2. **Progress Bar:** Embed in README automatically, or just generate file?
3. **Drift Detector:** Should we auto-fix broken references, or just report?
4. **Activity Stream:** Use vis.js Timeline library, or simple HTML/CSS?
5. **Temp Dashboard:** Integrate with GitHub PR API to detect extraction PRs?

---

## Getting Started

1. Read existing codebase:
   - `tools/generate-visuals.py` - Driver pattern
   - `tools/parsers/sot_parser.py` - Parsing example
   - `tools/generators/graph_generator.py` - Generator example

2. Start with Feature 2.1 (Progress Bar):
   - Create `tools/parsers/prd_parser.py`
   - Create `tools/generators/progress_generator.py`
   - Add `--progress` flag to driver
   - Test on this repo (currently at v0.6 according to PRD)

3. Follow CODEX principles:
   - Deterministic output
   - Config-driven
   - Graceful degradation

---

## Repository Context

**Repo:** PRD-driven-context-engineering (Gear Heart Methodology)
**Branch:** Create new branch for Phase 2
**Base:** `claude/hephaestus-visualization-fork-01XhhcbWhYUm7b3e81sNm9Sr` (Phase 1 complete)

**Key Files to Read:**
- `docs/ghm-visualization-suite-plan.md` (lines 200-600: Phase 2-4 specs)
- `docs/ghm-visualization-suite-review.md` (CODEX's full review)
- `workflows/PRD-VERSION-LIFECYCLE.md` (gate structure)
- `workflows/UNIQUE-ID-SYSTEM.md` (ID system rules)

**Methodology Overview:**
GHM uses a 3+1+SoT+Temp pattern:
- **3 navigation files:** README, PRD, CLAUDE
- **+1 EPIC:** Active work window
- **SoT:** Source of Truth files (BUSINESS_RULES, API_CONTRACTS, USER-JOURNEYS, etc.)
- **Temp:** Short-lived scratchpads

IDs are unique identifiers (BR-XXX, API-XXX, UJ-XXX) that cross-reference specs. The visualization suite makes these connections visible.

---

## Deliverables

For each feature, deliver:
1. **Code** - New parser/generator modules
2. **Tests** - Run on this repo, validate output
3. **Documentation** - Update `tools/README.md` with usage
4. **Sample Output** - Generated artifact in `docs/generated/`
5. **Integration** - Add to `generate-visuals.py` driver

---

Ready to build! Start with Feature 2.1 (PRD Lifecycle Progress Bar) and work sequentially through the phases. 🚀
