# GHM Visualization Suite

A documentation-first visualization layer for the Gear Heart Methodology, inspired by [Hephaestus](https://github.com/Ido-Levi/Hephaestus).

## Quick Start

### Prerequisites

1. **Python 3.10+** with PyYAML:
   ```bash
   pip install -r tools/requirements.txt
   ```

2. **Graphviz** (for graph generation):
   ```bash
   # macOS
   brew install graphviz

   # Ubuntu/Debian
   apt-get install graphviz

   # Windows
   # See https://graphviz.org/download/
   ```

### Generate Visualizations

```bash
# Generate all visualizations
python tools/generate-visuals.py --all

# Generate only ID graph
python tools/generate-visuals.py --graph

# Validate parsing without generating (for CI)
python tools/generate-visuals.py --check

# Filter graph to specific IDs
python tools/generate-visuals.py --graph --ids BR-001,API-045
```

### View Results

Open `docs/generated/index.md` for links to all generated artifacts.

## What It Does

The visualization suite parses your GHM markdown files and generates:

1. **ID Knowledge Graph** - Visual dependency graph showing how IDs (BR-XXX, API-XXX, UJ-XXX, etc.) cross-reference each other
2. **Validation Reports** - Identifies orphaned IDs and missing references
3. **Provenance Metadata** - Tracks git commit, config hash, and build time

## Features

### Current (Phase 1 - Week 1 Spike)

- ✅ Parse Source of Truth (SoT) markdown files
- ✅ Extract IDs and cross-references
- ✅ Generate static Graphviz graphs (SVG/PNG)
- ✅ Identify orphaned IDs
- ✅ Identify missing references
- ✅ Provenance tracking (git SHA, config hash)
- ✅ Configurable via YAML
- ✅ Deterministic output (minimal PR noise)

### Planned (Future Phases)

- PRD Lifecycle Progress Bar (v0.1 → v1.0 tracker)
- Agent Activity Stream (git timeline)
- Temp File Lifecycle Dashboard
- Context Window Optimizer
- Documentation Drift Detector
- Interactive D3.js graphs (optional)

See `docs/ghm_visualization_suite_plan.md` for the full roadmap.

## Configuration

Edit `tools/config/visuals.yaml` to customize:

- ID extraction patterns (regex)
- Node colors by ID type
- Graph layout engine (dot, neato, fdp, etc.)
- Output formats (svg, png, pdf)
- File paths to scan

## Architecture

```
tools/
├── generate-visuals.py      # Main driver script
├── config/
│   ├── visuals.yaml         # Configuration
│   └── agents.yaml          # Agent mapping (future)
├── parsers/
│   └── sot_parser.py        # Extract IDs from SoT files
├── generators/
│   └── graph_generator.py   # Generate Graphviz graphs
└── utils/
    ├── id_extractor.py      # ID regex patterns
    ├── provenance.py        # Git SHA + metadata
    └── attribution.py       # Hephaestus credit
```

## Inspiration & Attribution

This suite is inspired by visual concepts from [Hephaestus](https://github.com/Ido-Levi/Hephaestus) (AGPL-3.0), a semi-structured agentic framework by Ido Levi.

**No code was copied from Hephaestus.** All implementations are original, written from scratch to comply with GHM's MIT license. We gratefully acknowledge the design inspiration.

## License

MIT License - Copyright (c) 2025 Gear Heart AI, LLC

See `LICENSE` for full text.

## Development

### Running Tests

```bash
# Validate parsing
python tools/generate-visuals.py --check

# Check for missing SoT files
python tools/generate-visuals.py --graph 2>&1 | grep "Skipped"
```

### Adding New Features

See `docs/ghm_visualization_suite_plan.md` for feature specifications and implementation guidelines.

### Troubleshooting

**Import Errors:**
- Make sure you run from repo root: `python tools/generate-visuals.py`
- Don't run from tools/ directory

**Graphviz Not Found:**
- Install Graphviz system package (not Python package)
- Verify: `which dot` (should show path to dot command)

**No IDs Found:**
- Check that SoT files exist in locations specified in config
- Verify ID patterns match your naming (e.g., `BR-001` not `BR-1`)

## Contributing

See main `CONTRIBUTING.md` for guidelines.

For visualization-specific contributions:
1. Maintain deterministic output (sorted IDs, no timestamps in artifacts)
2. Preserve provenance metadata
3. Keep attribution blocks in generated files
4. Test on repos with 0, 10, and 100+ IDs
