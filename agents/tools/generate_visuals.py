#!/usr/bin/env python3
"""GHM Visualization Suite - Main Driver Script

Generates visual artifacts from GHM markdown files.

Usage:
    python tools/generate-visuals.py --all
    python tools/generate-visuals.py --graph
    python tools/generate-visuals.py --graph --epic EPIC-03
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML not installed. Install with: pip install pyyaml")
    sys.exit(1)

# Add tools directory to path
sys.path.insert(0, str(Path(__file__).parent))

from parsers.sot_parser import SoTParser
from generators.graph_generator import GraphGenerator
from utils.provenance import write_provenance
from utils.attribution import get_attribution_text


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description='Generate GHM visualizations from markdown files',
        epilog='For more information, see docs/ghm_visualization_suite_plan.md'
    )
    parser.add_argument(
        '--all',
        action='store_true',
        help='Generate all visualizations'
    )
    parser.add_argument(
        '--graph',
        action='store_true',
        help='Generate ID knowledge graph'
    )
    parser.add_argument(
        '--check',
        action='store_true',
        help='Validate parsing without generating artifacts (for CI)'
    )
    parser.add_argument(
        '--config',
        default='tools/config/visuals.yaml',
        help='Config file path (default: tools/config/visuals.yaml)'
    )
    parser.add_argument(
        '--output-dir',
        help='Output directory (default: from config or docs/generated)'
    )
    parser.add_argument(
        '--epic',
        help='Filter graph to specific EPIC (e.g., EPIC-03)'
    )
    parser.add_argument(
        '--ids',
        help='Filter graph to specific IDs (comma-separated, e.g., BR-001,API-045)'
    )

    args = parser.parse_args()

    # Load config
    config_path = Path(args.config)
    if not config_path.exists():
        print(f"ERROR: Config file not found: {config_path}")
        sys.exit(1)

    try:
        config = yaml.safe_load(config_path.read_text())
    except Exception as e:
        print(f"ERROR: Failed to parse config file: {e}")
        sys.exit(1)

    # Setup paths
    repo_root = Path.cwd()
    output_dir = Path(args.output_dir) if args.output_dir else Path(config.get('output', {}).get('directory', 'docs/generated'))
    output_dir.mkdir(parents=True, exist_ok=True)

    print("=" * 60)
    print("GHM Visualization Suite")
    print("=" * 60)
    print(f"Repository: {repo_root}")
    print(f"Config: {config_path}")
    print(f"Output: {output_dir}")
    print()

    # Parse SoT files
    print("[1/4] Parsing Source of Truth files...")
    sot_parser = SoTParser(repo_root, config)

    try:
        graph_data = sot_parser.parse_all()
    except Exception as e:
        print(f"ERROR: Failed to parse SoT files: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)

    # Print summary
    metadata = graph_data.get('metadata', {})
    print(f"  ✓ Parsed {metadata.get('files_parsed', 0)} files")
    print(f"  ✓ Found {metadata.get('total_ids', 0)} IDs")
    print(f"  ✓ Found {metadata.get('total_edges', 0)} cross-references")

    if metadata.get('files_skipped'):
        print(f"  ⚠ Skipped {len(metadata['files_skipped'])} files:")
        for f in metadata['files_skipped']:
            print(f"    - {f}")

    # Find orphaned and missing IDs
    orphaned = sot_parser.find_orphaned_ids(graph_data)
    missing = sot_parser.find_missing_targets(graph_data)

    if orphaned:
        print(f"\n  ⚠ Found {len(orphaned)} orphaned IDs (no connections):")
        for id_str in orphaned[:10]:  # Show first 10
            print(f"    - {id_str}")
        if len(orphaned) > 10:
            print(f"    ... and {len(orphaned) - 10} more")

    if missing:
        print(f"\n  ⚠ Found {len(missing)} referenced but undefined IDs:")
        for id_str in missing[:10]:  # Show first 10
            print(f"    - {id_str}")
        if len(missing) > 10:
            print(f"    ... and {len(missing) - 10} more")

    # Save JSON
    print("\n[2/4] Saving parsed data...")
    json_path = output_dir / 'id-graph-data.json'
    json_path.write_text(json.dumps(graph_data, indent=2))
    print(f"  ✓ Saved to {json_path}")

    # Check mode: stop here
    if args.check:
        print("\n✓ Check mode complete (no artifacts generated)")
        sys.exit(0 if not missing else 1)  # Fail if missing IDs

    # Generate graph
    if args.all or args.graph:
        print("\n[3/4] Generating ID knowledge graph...")

        # Filter if requested
        subgraph_ids = None
        if args.epic:
            # TODO: Parse EPIC Section 3A to get IDs
            print(f"  ⚠ EPIC filtering not yet implemented (--epic {args.epic})")
        elif args.ids:
            subgraph_ids = [id.strip() for id in args.ids.split(',')]
            print(f"  → Filtering to {len(subgraph_ids)} IDs")

        graph_gen = GraphGenerator(config)

        # Check Graphviz
        if not graph_gen.check_graphviz_installed():
            print("  ✗ Graphviz not installed. Skipping graph generation.")
            print("    Install: https://graphviz.org/download/")
        else:
            try:
                svg_path = graph_gen.generate(
                    graph_data,
                    output_dir / 'id-graph',
                    subgraph_ids=subgraph_ids
                )
                print(f"  ✓ Generated graph: {svg_path}")

                # Generate legend
                legend_path = graph_gen.generate_legend(output_dir / 'id-graph-legend')
                print(f"  ✓ Generated legend: {legend_path}")
            except Exception as e:
                print(f"  ✗ Failed to generate graph: {e}")
                import traceback
                traceback.print_exc()

    # Add provenance
    if config.get('output', {}).get('include_provenance', True):
        print("\n[4/4] Adding provenance metadata...")
        provenance_path = write_provenance(output_dir, config)
        print(f"  ✓ Written to {provenance_path}")

    # Create index page
    print("\nCreating index page...")
    create_index(output_dir, config, graph_data)
    print(f"  ✓ Created {output_dir / 'index.md'}")

    print("\n" + "=" * 60)
    print("✓ Generation complete!")
    print(f"\nView results:")
    print(f"  {output_dir / 'index.md'}")
    if (output_dir / 'id-graph.svg').exists():
        print(f"  {output_dir / 'id-graph.svg'}")
    print("=" * 60)


def create_index(output_dir: Path, config: dict, graph_data: dict):
    """Create index.md linking to all outputs.

    Args:
        output_dir: Output directory
        config: Configuration dict
        graph_data: Parsed graph data
    """
    from utils.provenance import get_git_sha_short

    attribution = get_attribution_text(
        Path(config.get('attribution', {}).get('template', 'tools/templates/attribution.md'))
    )

    metadata = graph_data.get('metadata', {})
    orphaned_count = len([n for n in graph_data['nodes'] if n['id'] not in {e['source'] for e in graph_data['edges']} and n['id'] not in {e['target'] for e in graph_data['edges']}])

    index_content = f"""# GHM Visualization Suite - Generated Artifacts

{attribution}

---

## Summary

- **Total IDs**: {metadata.get('total_ids', 0)}
- **Cross-References**: {metadata.get('total_edges', 0)}
- **Files Parsed**: {metadata.get('files_parsed', 0)}
- **Orphaned IDs**: {orphaned_count} (no incoming/outgoing references)
- **Git Commit**: `{get_git_sha_short()}`

## Artifacts

### ID Knowledge Graph
- **[id-graph.svg](id-graph.svg)** - Complete ID dependency graph (static, diffable)
- **[id-graph-legend.svg](id-graph-legend.svg)** - Color legend for node types
- **[id-graph.dot](id-graph.dot)** - Graphviz DOT source (for debugging)
- **[id-graph-data.json](id-graph-data.json)** - Parsed ID data (for programmatic access)

### Build Metadata
- **[.provenance](.provenance)** - Build metadata (commit SHA, config hash, timestamps)

---

## Usage

### Viewing the Graph
Open `id-graph.svg` in a web browser or image viewer. Each node represents an ID (BR-XXX, API-XXX, etc.), and edges show cross-references.

### Filtering the Graph
To generate a subgraph focusing on specific IDs:
```bash
python tools/generate-visuals.py --graph --ids BR-001,API-045
```

### Validation Mode
To validate parsing without generating artifacts (useful for CI):
```bash
python tools/generate-visuals.py --check
```

---

## Interpreting the Graph

### Node Colors
See `id-graph-legend.svg` for the full color scheme. Common types:
- **Blue** - Business Rules (BR-XXX)
- **Green** - API Contracts (API-XXX)
- **Purple** - User Journeys (UJ-XXX)
- **Yellow** - Test Cases (TEST-XXX)

### Orphaned IDs
IDs with no connections may indicate:
- Newly created IDs not yet referenced
- Deprecated IDs that should be marked as such
- Potential documentation gaps

### Missing References
If `--check` reports missing IDs, these are referenced but not defined. Update SoT files to define them or remove the references.

---

*Generated by `tools/generate-visuals.py`*
*Last updated: {metadata.get('build_time', 'unknown')}*
"""

    (output_dir / 'index.md').write_text(index_content)


if __name__ == '__main__':
    main()
