---
title: "GHM Visualization Suite - Implementation Plan"
version: 2.0
created: 2025-11-23
updated: 2025-11-23 (CODEX review incorporated)
author: Claude (reviewed by CODEX)
purpose: "Specification for building GHM-native visualization tools inspired by Hephaestus"
status: "Approved - Implementation in progress"
---

# GHM Visualization Suite
## A Documentation-First Approach to Visual Context Engineering

> **Inspiration**: Hephaestus (https://github.com/Ido-Levi/Hephaestus) - Semi-Structured Agentic Framework
> **Approach**: Borrow visual concepts, implement from scratch with GHM principles
> **License**: MIT (Gear Heart AI, LLC)
> **Attribution**: Design inspiration from Hephaestus (AGPL-3.0) - no code copied

---

## CODEX Review Summary

**Status**: ✅ Approved with scope adjustments

**Key Changes**:
1. **Start with deterministic snapshots** - Graphviz/PNG/SVG before interactive D3
2. **Single driver script** - `tools/generate-visuals.py` with modular feature imports
3. **Git-tracked outputs** - `docs/generated/` for diffable artifacts
4. **Config-driven** - `tools/config/visuals.yaml` for tunables
5. **One-week spike first** - Parse SoT → Graphviz + JSON, validate on this repo

**Full Review**: See `docs/ghm-visualization-suite-review.md`

---

## Executive Summary

**Problem**: The Gear Heart Methodology's ID-based knowledge graph, PRD lifecycle, and multi-agent coordination are powerful but **invisible** in markdown.

**Solution**: Build a lightweight **visualization layer** that reads GHM markdown files and renders **deterministic, diffable artifacts** while preserving documentation-first philosophy.

**Key Principle**: Markdown files remain the source of truth. Visualizations are **reproducible snapshots** generated from parsing README.md, PRD.md, EPICs, and SoT files.

---

## Design Principles (CODEX-Aligned)

### 1. **Documentation-First, Visuals-Second**
- Files are authority; visualizations are ephemeral views
- All outputs reproducible from repo state (no hidden caches)
- Generated artifacts committed to `docs/generated/` for PR reviews

### 2. **Deterministic Before Interactive**
- Phase 1: Static Graphviz graphs (SVG/PNG) - diffable, fast, reliable
- Phase 2: Interactive HTML (D3.js) - optional enhancement
- Staged rollout reduces parsing risk

### 3. **Single Driver Script**
- `tools/generate-visuals.py --all` - one command for all features
- Modular feature imports (parsers/, generators/)
- Predictable for CI/CD integration

### 4. **Configuration Over Convention**
- `tools/config/visuals.yaml` - color mappings, ID patterns, file globs
- Zero-config defaults work out-of-box
- Override via CLI flags or environment variables

### 5. **Provenance & Reproducibility**
- Every artifact includes: input commit SHA, tool version, config hash
- Deterministic ordering (sorted IDs) to minimize PR noise
- Graceful degradation on parse errors (partial results + warnings)

---

## Revised Feature Roadmap

### **Phase 1: Foundation (Week 1 Spike)**
**Goal**: Validate parsing approach with simplest possible output

**Deliverables**:
1. SoT parser (extract IDs + cross-references → JSON)
2. Graphviz static graph generator (SVG + PNG)
3. Driver script scaffold
4. Config file schema
5. Attribution templates

**Success Criteria**:
- [ ] Parse all SoT files in this repo without errors
- [ ] Generate ID graph with 100+ nodes in <10 seconds
- [ ] Output is deterministic (same input = byte-identical output)
- [ ] Graph identifies orphaned IDs and missing references

---

### **Phase 2: Core Features (Weeks 2-8)**
**Priority Order** (based on CODEX feedback):

#### 1. **ID Knowledge Graph** (Weeks 2-3)
- **Static**: Graphviz DOT → SVG/PNG (force-directed layout)
- **Interactive**: D3.js HTML (Phase 3 optional)
- **Features**: Click to highlight, filter by type, orphan detection, subgraph by EPIC
- **CODEX additions**:
  - Cache parsed SoT → JSON with checksums
  - Static fallback committed to `docs/generated/id-graph.svg`
  - Subgraph filter: `--epic EPIC-03` or `--ids BR-001,API-045`

#### 2. **Documentation Drift Detector** (Weeks 4-5)
- **Stage 1**: Broken/missing ID detection (ship first)
- **Stage 2**: Staleness detection (git timestamps)
- **Stage 3**: Semantic claim checks (future)
- **CODEX additions**:
  - Machine-readable JSON + human Markdown/HTML
  - CI can fail on critical issues
  - Toggleable stages via config

#### 3. **PRD Lifecycle Progress Bar** (Week 6)
- **Static**: Markdown badge for README.md
- **Rich**: HTML timeline for `docs/generated/`
- **CODEX additions**:
  - Parse `workflows/PRD-VERSION-LIFECYCLE.md` (no checklist duplication)
  - Idempotent generation (minimal diff noise)

#### 4. **Agent Activity Stream** (Week 7)
- **Parser**: Git metadata → agent attribution
- **CODEX additions**:
  - Mapping file: `tools/config/agents.yaml` (authors → AURA/APOLLO/JANUS)
  - Privacy guard: strip emails unless explicitly allowed
  - Filter by EPIC, agent, or date range

#### 5. **Temp File Lifecycle Dashboard** (Week 8)
- **Scanner**: Recursive temp/ with age + owner + extraction target
- **CODEX additions**:
  - Mark files with open extraction PRs (parse branch names)
  - Graceful frontmatter handling (fallback to git metadata)

---

### **Phase 3: Advanced Features (Weeks 9-12)**

#### 6. **Context Window Optimizer**
- **Start**: Non-transitive mode (direct references only)
- **CODEX additions**:
  - Prove accuracy before enabling transitive traversal
  - Token estimates with model-switching via config
  - Disclaimer on heuristics

#### 7. **Interactive Enhancements** (Optional)
- Upgrade static graphs to D3.js/Cytoscape
- Real-time file watching (optional)
- Web server for live updates (optional)

---

## Architecture

### Directory Structure
```
PRD-driven-context-engineering/
├── tools/
│   ├── generate-visuals.py       # Main driver script
│   ├── config/
│   │   ├── visuals.yaml          # Configuration defaults
│   │   └── agents.yaml           # Author → agent mapping
│   ├── parsers/
│   │   ├── __init__.py
│   │   ├── sot_parser.py         # Extract IDs from SoT files
│   │   ├── prd_parser.py         # Parse PRD metadata
│   │   ├── epic_parser.py        # Section 3A extraction
│   │   └── git_parser.py         # Git history analysis
│   ├── generators/
│   │   ├── __init__.py
│   │   ├── graph_generator.py    # Graphviz DOT generation
│   │   ├── progress_generator.py # Lifecycle progress bar
│   │   ├── activity_generator.py # Agent activity stream
│   │   ├── drift_detector.py     # Documentation validator
│   │   └── temp_scanner.py       # Temp file lifecycle
│   └── utils/
│       ├── __init__.py
│       ├── id_extractor.py       # Regex patterns for IDs
│       ├── provenance.py         # Git SHA, version, checksums
│       └── attribution.py        # Hephaestus credit blocks
├── docs/
│   ├── generated/                # Git-tracked outputs
│   │   ├── index.md              # Index page with timestamps
│   │   ├── id-graph.svg          # Static graph (deterministic)
│   │   ├── id-graph.html         # Interactive (optional)
│   │   ├── id-graph.json         # Parsed data (for debugging)
│   │   ├── lifecycle-progress.md # Embeddable badge
│   │   ├── drift-report.md       # Validation results
│   │   └── .provenance           # Build metadata (SHA, config hash)
│   └── ghm-visualization-suite-review.md
└── README.md                     # Link to docs/generated/
```

### Data Flow
```
┌─────────────────────────────────────────────────┐
│  GHM Source Files (Markdown)                    │
│  README.md, PRD.md, SoT/*.md, epics/*.md       │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│  Parsers (tools/parsers/)                       │
│  • sot_parser.py → Extract IDs + cross-refs    │
│  • prd_parser.py → Gate status, checklists     │
│  • epic_parser.py → Section 3A tables          │
│  • git_parser.py → Commit history              │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│  Intermediate JSON (cached with checksums)      │
│  • id-graph-data.json                          │
│  • prd-metadata.json                           │
│  • git-activity.json                           │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│  Generators (tools/generators/)                 │
│  • graph_generator.py → Graphviz DOT → SVG     │
│  • progress_generator.py → Markdown badge      │
│  • activity_generator.py → HTML timeline       │
│  • drift_detector.py → Validation report       │
└─────────────────────────────────────────────────┘
                    ↓
┌─────────────────────────────────────────────────┐
│  Committed Artifacts (docs/generated/)          │
│  • id-graph.svg (diffable in PRs)              │
│  • drift-report.md (CI can fail on errors)     │
│  • index.md (links to all outputs)             │
└─────────────────────────────────────────────────┘
```

---

## Configuration Schema

### `tools/config/visuals.yaml`
```yaml
# GHM Visualization Suite Configuration
version: 1.0

# ID extraction patterns
id_patterns:
  business_rules: 'BR-\d{3}'
  api_contracts: 'API-\d{3}'
  user_journeys: 'UJ-\d{3}'
  database_tables: 'DBT-\d{3}'
  test_cases: 'TEST-\d{3}'
  deployments: 'DEP-\d{3}'
  customer_feedback: 'CFD-\d{3}'
  designs: 'DES-\d{3}'

# File patterns for SoT parsing
sot_files:
  - 'source-of-truth/BUSINESS_RULES.md'
  - 'source-of-truth/API_CONTRACTS.md'
  - 'source-of-truth/USER-JOURNEYS.md'
  - 'source-of-truth/ACTUAL-SCHEMA.md'
  - 'source-of-truth/testing-playbook.md'
  - 'source-of-truth/deployment-playbook.md'
  - 'source-of-truth/customer-feedback.md'

# Graph styling
graph:
  node_colors:
    BR: '#3498db'  # Blue for business rules
    API: '#2ecc71' # Green for APIs
    UJ: '#9b59b6'  # Purple for user journeys
    DBT: '#e67e22' # Orange for database
    TEST: '#f1c40f' # Yellow for tests
    DEP: '#34495e'  # Gray for deployment
    CFD: '#e74c3c'  # Red for feedback
  layout: 'dot'      # Graphviz layout engine
  format: 'svg'      # Output format (svg, png, pdf)

# Lifecycle gates (parsed from workflows/PRD-VERSION-LIFECYCLE.md)
lifecycle:
  auto_parse: true
  gates_file: 'workflows/PRD-VERSION-LIFECYCLE.md'

# Temp file lifecycle
temp:
  directory: 'temp/'
  age_thresholds:
    fresh: 7    # days
    aging: 14   # days
    stale: 14   # days (>14 = stale)

# Privacy settings
privacy:
  strip_emails: true
  strip_usernames: false

# Attribution (Hephaestus credit)
attribution:
  enabled: true
  template: 'tools/templates/attribution.md'
```

### `tools/config/agents.yaml`
```yaml
# Author → Agent Role Mapping
# Used by Agent Activity Stream
agents:
  'claude': 'CLAUDE'
  'codex': 'CODEX'
  'aura': 'AURA'
  'apollo': 'APOLLO'
  'janus': 'JANUS'

# Map git authors to agent roles
author_mapping:
  'user@example.com': 'APOLLO'
  'matt@gearheart.ai': 'Human PM'
```

---

## Implementation: Week 1 Spike

### Objective
Validate parsing approach by building simplest possible output: static Graphviz graph.

### Tasks

#### 1. **Setup Project Structure** (Day 1)
```bash
mkdir -p tools/{config,parsers,generators,utils,templates}
mkdir -p docs/generated
touch tools/{__init__.py,generate-visuals.py}
touch tools/parsers/{__init__.py,sot_parser.py}
touch tools/generators/{__init__.py,graph_generator.py}
touch tools/utils/{__init__.py,id_extractor.py,provenance.py,attribution.py}
touch tools/config/{visuals.yaml,agents.yaml}
touch tools/templates/attribution.md
```

#### 2. **ID Extractor Utility** (Day 1)
```python
# tools/utils/id_extractor.py
import re
from typing import List, Dict, Set

ID_PATTERNS = {
    'BR': r'BR-\d{3}',
    'API': r'API-\d{3}',
    'UJ': r'UJ-\d{3}',
    'DBT': r'DBT-\d{3}',
    'TEST': r'TEST-\d{3}',
    'DEP': r'DEP-\d{3}',
    'CFD': r'CFD-\d{3}',
    'DES': r'DES-\d{3}',
}

def extract_ids(text: str, id_type: str = None) -> Set[str]:
    """Extract IDs from text. If id_type specified, only extract that type."""
    if id_type:
        pattern = ID_PATTERNS.get(id_type)
        if pattern:
            return set(re.findall(pattern, text))

    # Extract all ID types
    ids = set()
    for pattern in ID_PATTERNS.values():
        ids.update(re.findall(pattern, text))
    return ids

def extract_markdown_links(text: str) -> List[Dict[str, str]]:
    """Extract markdown links: [text](url)"""
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    return [{'text': m[0], 'url': m[1]} for m in re.findall(pattern, text)]
```

#### 3. **SoT Parser** (Day 2-3)
```python
# tools/parsers/sot_parser.py
import re
from pathlib import Path
from typing import Dict, List, Set
from ..utils.id_extractor import extract_ids, extract_markdown_links

class SoTParser:
    def __init__(self, repo_root: Path):
        self.repo_root = Path(repo_root)
        self.sot_files = [
            'source-of-truth/BUSINESS_RULES.md',
            'source-of-truth/API_CONTRACTS.md',
            'source-of-truth/USER-JOURNEYS.md',
            # ... add all SoT files
        ]

    def parse_all(self) -> Dict:
        """Parse all SoT files, return ID graph data."""
        graph_data = {
            'nodes': [],  # List of {id, type, file, excerpt}
            'edges': [],  # List of {source, target, relation}
        }

        for sot_file in self.sot_files:
            file_path = self.repo_root / sot_file
            if not file_path.exists():
                continue

            content = file_path.read_text()

            # Extract all IDs defined in this file (## BR-001:, ## API-045:, etc.)
            defined_ids = self._extract_defined_ids(content)

            for id_str in defined_ids:
                # Extract excerpt (first few lines after ID heading)
                excerpt = self._extract_excerpt(content, id_str)

                # Extract cross-references from excerpt
                references = extract_ids(excerpt) - {id_str}

                # Add node
                graph_data['nodes'].append({
                    'id': id_str,
                    'type': id_str.split('-')[0],  # BR, API, UJ, etc.
                    'file': sot_file,
                    'excerpt': excerpt[:200],  # First 200 chars
                })

                # Add edges
                for ref_id in references:
                    graph_data['edges'].append({
                        'source': id_str,
                        'target': ref_id,
                        'relation': 'references',
                    })

        return graph_data

    def _extract_defined_ids(self, content: str) -> Set[str]:
        """Find all IDs defined as headings: ## BR-001:"""
        pattern = r'##\s+(' + '|'.join(ID_PATTERNS.values()) + r')'
        return set(re.findall(pattern, content))

    def _extract_excerpt(self, content: str, id_str: str) -> str:
        """Extract text after ## ID-XXX: heading."""
        # Find heading, extract next 5 lines
        pattern = rf'##\s+{re.escape(id_str)}[:\s]+(.*?)(?=\n##|\Z)'
        match = re.search(pattern, content, re.DOTALL)
        return match.group(1).strip() if match else ""
```

#### 4. **Graphviz Generator** (Day 3-4)
```python
# tools/generators/graph_generator.py
import subprocess
from pathlib import Path
from typing import Dict

class GraphGenerator:
    def __init__(self, config: Dict):
        self.config = config
        self.node_colors = config['graph']['node_colors']
        self.layout = config['graph']['layout']
        self.format = config['graph']['format']

    def generate(self, graph_data: Dict, output_path: Path):
        """Generate Graphviz DOT file and render to SVG/PNG."""
        dot_content = self._build_dot(graph_data)

        # Write DOT file
        dot_path = output_path.with_suffix('.dot')
        dot_path.write_text(dot_content)

        # Render with Graphviz
        output_svg = output_path.with_suffix('.svg')
        subprocess.run([
            'dot',
            f'-T{self.format}',
            '-o', str(output_svg),
            str(dot_path)
        ], check=True)

        return output_svg

    def _build_dot(self, graph_data: Dict) -> str:
        """Build Graphviz DOT syntax."""
        lines = ['digraph IDGraph {']
        lines.append('  rankdir=LR;')
        lines.append('  node [shape=box, style=filled];')

        # Nodes
        for node in graph_data['nodes']:
            color = self.node_colors.get(node['type'], '#cccccc')
            label = f"{node['id']}\\n({node['type']})"
            lines.append(f'  "{node["id"]}" [label="{label}", fillcolor="{color}"];')

        # Edges
        for edge in graph_data['edges']:
            lines.append(f'  "{edge["source"]}" -> "{edge["target"]}";')

        lines.append('}')
        return '\n'.join(lines)
```

#### 5. **Driver Script** (Day 4-5)
```python
# tools/generate-visuals.py
#!/usr/bin/env python3
"""GHM Visualization Suite - Main Driver Script"""

import argparse
import json
from pathlib import Path
import yaml

from parsers.sot_parser import SoTParser
from generators.graph_generator import GraphGenerator
from utils.provenance import add_provenance
from utils.attribution import get_attribution_text

def main():
    parser = argparse.ArgumentParser(description='Generate GHM visualizations')
    parser.add_argument('--all', action='store_true', help='Generate all visualizations')
    parser.add_argument('--graph', action='store_true', help='Generate ID graph')
    parser.add_argument('--config', default='tools/config/visuals.yaml', help='Config file')
    parser.add_argument('--output-dir', default='docs/generated', help='Output directory')
    args = parser.parse_args()

    # Load config
    config = yaml.safe_load(Path(args.config).read_text())

    # Setup paths
    repo_root = Path.cwd()
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    # Parse SoT files
    print("Parsing SoT files...")
    sot_parser = SoTParser(repo_root)
    graph_data = sot_parser.parse_all()

    # Save JSON (for debugging/caching)
    json_path = output_dir / 'id-graph-data.json'
    json_path.write_text(json.dumps(graph_data, indent=2))
    print(f"Saved parsed data to {json_path}")

    # Generate graph
    if args.all or args.graph:
        print("Generating ID graph...")
        graph_gen = GraphGenerator(config)
        svg_path = graph_gen.generate(graph_data, output_dir / 'id-graph')
        print(f"Generated graph: {svg_path}")

    # Add provenance
    add_provenance(output_dir, config)

    # Create index page
    create_index(output_dir)

    print("Done!")

def create_index(output_dir: Path):
    """Create index.md linking to all outputs."""
    attribution = get_attribution_text()

    index_content = f"""# GHM Visualization Suite - Generated Artifacts

{attribution}

## ID Knowledge Graph
- [Static Graph (SVG)](id-graph.svg) - Diffable, deterministic
- [Parsed Data (JSON)](id-graph-data.json) - Raw extraction for debugging

## Build Metadata
See `.provenance` for input commit SHA, tool version, and config hash.

---
*Generated by `tools/generate-visuals.py`*
"""

    (output_dir / 'index.md').write_text(index_content)

if __name__ == '__main__':
    main()
```

#### 6. **Provenance & Attribution** (Day 5)
```python
# tools/utils/provenance.py
import subprocess
from pathlib import Path
from datetime import datetime
import hashlib

def get_git_sha() -> str:
    """Get current git commit SHA."""
    result = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True)
    return result.stdout.strip()

def get_config_hash(config: dict) -> str:
    """Hash config to detect changes."""
    import json
    config_str = json.dumps(config, sort_keys=True)
    return hashlib.sha256(config_str.encode()).hexdigest()[:8]

def add_provenance(output_dir: Path, config: dict):
    """Write .provenance file with build metadata."""
    provenance = {
        'build_time': datetime.utcnow().isoformat(),
        'git_commit': get_git_sha(),
        'config_hash': get_config_hash(config),
        'tool_version': '1.0.0',
    }

    import json
    (output_dir / '.provenance').write_text(json.dumps(provenance, indent=2))
```

```python
# tools/utils/attribution.py

def get_attribution_text() -> str:
    """Return Hephaestus attribution block."""
    return """## Inspiration & Attribution

This visualization suite is inspired by visual concepts from
[Hephaestus](https://github.com/Ido-Levi/Hephaestus), a semi-structured
agentic framework by Ido Levi (AGPL-3.0).

We adapted Hephaestus's visualization approaches (dependency graphs, Kanban
boards, agent monitoring) to align with Gear Heart Methodology's
documentation-first context engineering workflow.

**No code was copied from Hephaestus.** All implementations are original,
written from scratch to comply with GHM's MIT license. We gratefully
acknowledge the inspiration and design patterns from the Hephaestus project.
"""
```

```markdown
# tools/templates/attribution.md
## Inspiration & Attribution

This tool is part of the GHM Visualization Suite, inspired by visual concepts
from [Hephaestus](https://github.com/Ido-Levi/Hephaestus), a semi-structured
agentic framework by Ido Levi.

**Hephaestus License**: AGPL-3.0
**GHM License**: MIT (Gear Heart AI, LLC)

We adapted Hephaestus's visualization approaches (dependency graphs, Kanban
boards, agent monitoring) to align with Gear Heart Methodology's
documentation-first context engineering workflow.

**No code was copied from Hephaestus.** All implementations are original,
written from scratch to comply with GHM's MIT license. We gratefully
acknowledge the inspiration and design patterns from the Hephaestus project.
```

---

## Success Metrics

### Week 1 Spike
- [ ] Parse all SoT files in this repo (BUSINESS_RULES.md, API_CONTRACTS.md, etc.)
- [ ] Generate id-graph.svg with 100+ nodes in <10 seconds
- [ ] Output is deterministic (identical on repeated runs)
- [ ] Identify orphaned IDs (nodes with no incoming/outgoing edges)
- [ ] JSON export validates (can be re-imported)

### Phase 2 (Weeks 2-8)
- [ ] All 5 core features functional
- [ ] CI job runs `--check` mode (validates without building)
- [ ] Drift detector catches 100% of broken references in test repo
- [ ] Generated artifacts committed with <50 LOC diff per change

### Phase 3 (Weeks 9-12)
- [ ] Interactive HTML option available
- [ ] Context optimizer reduces token usage by 30%
- [ ] External user successfully generates visuals on their GHM repo

---

## Risks & Mitigations (Updated)

### Risk 1: Graphviz Dependency
**Risk**: Users don't have Graphviz installed
**Mitigation**:
- Check for Graphviz at runtime, provide install instructions
- Add to requirements (Homebrew, apt, etc.)
- Future: Pure Python fallback (NetworkX → matplotlib)

### Risk 2: Parsing Edge Cases
**Risk**: SoT files vary in format, parser breaks
**Mitigation**:
- Emit partial results with warnings (per CODEX)
- Log which files/IDs skipped
- Add `--strict` flag to fail hard (for CI)

### Risk 3: Git Noise
**Risk**: Generated files create large diffs
**Mitigation**:
- Deterministic ordering (sort IDs alphabetically)
- Idempotent generation (same input = same output)
- Timestamps in separate `.provenance` file (not in SVG)

---

## Next Steps (Post-CODEX Review)

1. ✅ **Incorporate CODEX feedback** - Update plan with scope adjustments
2. 🚧 **Week 1 spike** - Implement SoT parser + Graphviz generator
3. **Test on this repo** - Generate id-graph.svg, validate quality
4. **Share sample outputs** - Get UX feedback before Phase 2
5. **Formalize config** - Lock down visuals.yaml schema
6. **CI integration** - Add GitHub Action for `--check` mode

---

## Appendix: Revised Timeline

| Phase | Duration | Deliverables | Status |
|-------|----------|--------------|--------|
| **Week 1: Spike** | 5 days | SoT parser, Graphviz graph, driver script, config | 🚧 In progress |
| **Weeks 2-3: ID Graph** | 10 days | Static + interactive versions, caching, filters | 📋 Planned |
| **Weeks 4-5: Drift Detector** | 10 days | Stage 1 (broken IDs), JSON + Markdown output | 📋 Planned |
| **Week 6: Lifecycle Progress** | 5 days | Markdown badge + HTML timeline | 📋 Planned |
| **Week 7: Activity Stream** | 5 days | Git parser + agent attribution | 📋 Planned |
| **Week 8: Temp Dashboard** | 5 days | Scanner + extraction tracking | 📋 Planned |
| **Weeks 9-12: Advanced** | 20 days | Context optimizer, interactive enhancements | 📋 Planned |

**Total: 12 weeks** (reduced from 24 via staged rollout)

---

**End of Updated Plan**

*Status: Approved by CODEX, implementation in progress*
*Next: Complete Week 1 spike, share sample outputs for UX feedback*
