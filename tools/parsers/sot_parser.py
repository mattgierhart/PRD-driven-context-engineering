"""Source of Truth (SoT) file parser

Extracts IDs and cross-references from GHM SoT markdown files.
"""

import re
from pathlib import Path
from typing import Dict, List, Set, Any

try:
    from ..utils.id_extractor import IDExtractor
except ImportError:
    from utils.id_extractor import IDExtractor


class SoTParser:
    """Parse Source of Truth markdown files to extract ID graph"""

    def __init__(self, repo_root: Path, config: Dict[str, Any]):
        """Initialize parser.

        Args:
            repo_root: Root directory of the repository
            config: Configuration dict with 'sot_files' and 'id_patterns'
        """
        self.repo_root = Path(repo_root)
        self.config = config
        self.sot_files = config.get('sot_files', [])
        self.extractor = IDExtractor(config.get('id_patterns'))

    def parse_all(self) -> Dict[str, Any]:
        """Parse all SoT files and return ID graph data.

        Returns:
            Dict with 'nodes' (list of ID info) and 'edges' (list of relationships)
        """
        graph_data = {
            'nodes': [],  # List of {id, type, file, excerpt, line_number}
            'edges': [],  # List of {source, target, relation}
            'metadata': {
                'total_ids': 0,
                'total_edges': 0,
                'files_parsed': 0,
                'files_skipped': [],
            }
        }

        seen_ids = set()  # Track IDs we've already added

        for sot_file in self.sot_files:
            file_path = self.repo_root / sot_file

            if not file_path.exists():
                graph_data['metadata']['files_skipped'].append(str(sot_file))
                continue

            graph_data['metadata']['files_parsed'] += 1

            try:
                content = file_path.read_text(encoding='utf-8')
            except Exception as e:
                graph_data['metadata']['files_skipped'].append(f"{sot_file} (error: {e})")
                continue

            # Extract all IDs defined in this file (## BR-001:, ## API-045:, etc.)
            defined_ids = self._extract_defined_ids(content)

            for id_str in defined_ids:
                if id_str in seen_ids:
                    continue  # Skip duplicates

                seen_ids.add(id_str)

                # Extract excerpt and line number
                excerpt, line_num = self._extract_excerpt(content, id_str)

                # Extract cross-references from excerpt
                references = self.extractor.extract_ids(excerpt) - {id_str}

                # Add node
                graph_data['nodes'].append({
                    'id': id_str,
                    'type': self.extractor.get_id_type(id_str) or 'UNKNOWN',
                    'file': str(sot_file),
                    'excerpt': excerpt[:300],  # First 300 chars
                    'line_number': line_num,
                })

                # Add edges
                for ref_id in sorted(references):  # Sort for determinism
                    graph_data['edges'].append({
                        'source': id_str,
                        'target': ref_id,
                        'relation': 'references',
                    })

        # Update metadata
        graph_data['metadata']['total_ids'] = len(graph_data['nodes'])
        graph_data['metadata']['total_edges'] = len(graph_data['edges'])

        # Sort nodes and edges for deterministic output
        if self.config.get('output', {}).get('deterministic', True):
            graph_data['nodes'].sort(key=lambda n: n['id'])
            graph_data['edges'].sort(key=lambda e: (e['source'], e['target']))

        return graph_data

    def _extract_defined_ids(self, content: str) -> Set[str]:
        """Find all IDs defined as headings: ## BR-001: or ## BR-001 —

        Args:
            content: Markdown file content

        Returns:
            Set of ID strings
        """
        ids = set()

        # Build pattern from all ID types
        patterns = list(self.extractor.patterns.values())
        pattern_str = '|'.join(f'({p})' for p in patterns)

        # Match headings: ## ID-XXX: or ## ID-XXX —
        heading_pattern = rf'^\s*##\s+({pattern_str})[\s:—-]'
        matches = re.finditer(heading_pattern, content, re.MULTILINE)

        for match in matches:
            # Extract the actual ID (first group that matched)
            id_str = next(g for g in match.groups()[1:] if g is not None)
            ids.add(id_str)

        return ids

    def _extract_excerpt(self, content: str, id_str: str) -> tuple[str, int]:
        """Extract text after ## ID-XXX: heading.

        Args:
            content: Markdown file content
            id_str: ID to find (e.g., 'BR-001')

        Returns:
            Tuple of (excerpt text, line number)
        """
        # Find heading and extract next section (until next ## heading or EOF)
        pattern = rf'^\s*##\s+{re.escape(id_str)}[\s:—-]+(.*?)(?=^\s*##|\Z)'
        match = re.search(pattern, content, re.DOTALL | re.MULTILINE)

        if not match:
            return "", 0

        excerpt = match.group(1).strip()

        # Find line number
        line_num = content[:match.start()].count('\n') + 1

        return excerpt, line_num

    def find_orphaned_ids(self, graph_data: Dict[str, Any]) -> List[str]:
        """Find IDs with no incoming or outgoing references.

        Args:
            graph_data: Graph data from parse_all()

        Returns:
            List of orphaned ID strings
        """
        all_ids = {node['id'] for node in graph_data['nodes']}
        connected_ids = set()

        for edge in graph_data['edges']:
            connected_ids.add(edge['source'])
            connected_ids.add(edge['target'])

        orphaned = all_ids - connected_ids
        return sorted(orphaned)

    def find_missing_targets(self, graph_data: Dict[str, Any]) -> List[str]:
        """Find IDs that are referenced but not defined.

        Args:
            graph_data: Graph data from parse_all()

        Returns:
            List of missing ID strings
        """
        defined_ids = {node['id'] for node in graph_data['nodes']}
        referenced_ids = {edge['target'] for edge in graph_data['edges']}

        missing = referenced_ids - defined_ids
        return sorted(missing)
