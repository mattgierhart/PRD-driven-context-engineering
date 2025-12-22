"""Graphviz graph generator

Generates static SVG/PNG graphs from ID graph data using Graphviz DOT.
"""

import subprocess
import shutil
from pathlib import Path
from typing import Dict, List, Any, Optional


class GraphGenerator:
    """Generate static graphs using Graphviz"""

    def __init__(self, config: Dict[str, Any]):
        """Initialize generator.

        Args:
            config: Configuration dict with 'graph' settings
        """
        self.config = config
        self.graph_config = config.get('graph', {})
        self.node_colors = self.graph_config.get('node_colors', {})
        self.layout = self.graph_config.get('layout', 'dot')
        self.format = self.graph_config.get('format', 'svg')
        self.rankdir = self.graph_config.get('rankdir', 'LR')

    def check_graphviz_installed(self) -> bool:
        """Check if Graphviz is installed.

        Returns:
            True if 'dot' command is available
        """
        return shutil.which('dot') is not None

    def generate(
        self,
        graph_data: Dict[str, Any],
        output_path: Path,
        subgraph_ids: Optional[List[str]] = None
    ) -> Path:
        """Generate Graphviz DOT file and render to SVG/PNG.

        Args:
            graph_data: Graph data from SoTParser.parse_all()
            output_path: Output path (without extension)
            subgraph_ids: Optional list of IDs to include (filters graph)

        Returns:
            Path to generated SVG/PNG file

        Raises:
            RuntimeError: If Graphviz is not installed
        """
        if not self.check_graphviz_installed():
            raise RuntimeError(
                "Graphviz not installed. Please install it:\n"
                "  macOS: brew install graphviz\n"
                "  Ubuntu: apt-get install graphviz\n"
                "  See: https://graphviz.org/download/"
            )

        # Filter graph if subgraph_ids specified
        if subgraph_ids:
            graph_data = self._filter_subgraph(graph_data, subgraph_ids)

        # Build DOT content
        dot_content = self._build_dot(graph_data)

        # Write DOT file
        dot_path = output_path.with_suffix('.dot')
        dot_path.write_text(dot_content)

        # Render with Graphviz
        output_file = output_path.with_suffix(f'.{self.format}')
        try:
            subprocess.run([
                'dot',
                f'-K{self.layout}',
                f'-T{self.format}',
                '-o', str(output_file),
                str(dot_path)
            ], check=True, capture_output=True, text=True)
        except subprocess.CalledProcessError as e:
            raise RuntimeError(f"Graphviz rendering failed: {e.stderr}")

        return output_file

    def _filter_subgraph(
        self,
        graph_data: Dict[str, Any],
        subgraph_ids: List[str]
    ) -> Dict[str, Any]:
        """Filter graph to only include specified IDs and their direct neighbors.

        Args:
            graph_data: Full graph data
            subgraph_ids: List of IDs to include

        Returns:
            Filtered graph data
        """
        subgraph_set = set(subgraph_ids)

        # Find all neighbors (direct connections)
        for edge in graph_data['edges']:
            if edge['source'] in subgraph_set:
                subgraph_set.add(edge['target'])
            if edge['target'] in subgraph_set:
                subgraph_set.add(edge['source'])

        # Filter nodes and edges
        filtered_data = {
            'nodes': [n for n in graph_data['nodes'] if n['id'] in subgraph_set],
            'edges': [
                e for e in graph_data['edges']
                if e['source'] in subgraph_set and e['target'] in subgraph_set
            ],
            'metadata': graph_data.get('metadata', {}),
        }

        return filtered_data

    def _build_dot(self, graph_data: Dict[str, Any]) -> str:
        """Build Graphviz DOT syntax from graph data.

        Args:
            graph_data: Graph data with nodes and edges

        Returns:
            DOT format string
        """
        lines = ['digraph IDGraph {']

        # Graph attributes
        lines.append(f'  rankdir={self.rankdir};')
        lines.append('  node [shape=box, style="filled,rounded", fontname="Arial"];')
        lines.append('  edge [color="#666666"];')
        lines.append('')

        # Nodes
        for node in graph_data['nodes']:
            node_id = node['id']
            node_type = node['type']
            color = self.node_colors.get(node_type, '#cccccc')

            # Escape quotes in label
            excerpt = node.get('excerpt', '')[:100].replace('"', '\\"')
            label = f"{node_id}\\n{node_type}"
            if excerpt:
                label += f"\\n{excerpt}..."

            lines.append(
                f'  "{node_id}" ['
                f'label="{label}", '
                f'fillcolor="{color}", '
                f'tooltip="{node.get("file", "")}"'
                f'];'
            )

        lines.append('')

        # Edges
        for edge in graph_data['edges']:
            source = edge['source']
            target = edge['target']
            lines.append(f'  "{source}" -> "{target}";')

        lines.append('}')
        return '\n'.join(lines)

    def generate_legend(self, output_path: Path) -> Path:
        """Generate a separate legend showing node color meanings.

        Args:
            output_path: Output path for legend

        Returns:
            Path to generated legend file
        """
        lines = ['digraph Legend {']
        lines.append('  rankdir=LR;')
        lines.append('  node [shape=box, style="filled,rounded"];')
        lines.append('')

        for id_type, color in self.node_colors.items():
            lines.append(
                f'  "{id_type}" [label="{id_type}", fillcolor="{color}"];'
            )

        lines.append('}')

        dot_content = '\n'.join(lines)
        dot_path = output_path.with_suffix('.dot')
        dot_path.write_text(dot_content)

        # Render
        output_file = output_path.with_suffix(f'.{self.format}')
        subprocess.run([
            'dot',
            f'-T{self.format}',
            '-o', str(output_file),
            str(dot_path)
        ], check=True, capture_output=True)

        return output_file
