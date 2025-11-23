"""ID extraction utilities for GHM Visualization Suite

Extracts unique IDs (BR-XXX, API-XXX, etc.) from markdown text.
"""

import re
from typing import Set, List, Dict, Optional

# Default ID patterns (can be overridden by config)
DEFAULT_ID_PATTERNS = {
    'BR': r'BR-\d{3}',
    'API': r'API-\d{3}',
    'UJ': r'UJ-\d{3}',
    'DBT': r'DBT-\d{3}',
    'TEST': r'TEST-\d{3}',
    'DEP': r'DEP-\d{3}',
    'CFD': r'CFD-\d{3}',
    'DES': r'DES-\d{3}',
    'SEC': r'SEC-\d{3}',
    'PERF': r'PERF-\d{3}',
}


class IDExtractor:
    """Extract IDs from markdown text"""

    def __init__(self, patterns: Optional[Dict[str, str]] = None):
        """Initialize with ID patterns.

        Args:
            patterns: Dict mapping ID type to regex pattern.
                     If None, uses DEFAULT_ID_PATTERNS.
        """
        self.patterns = patterns or DEFAULT_ID_PATTERNS

    def extract_ids(self, text: str, id_type: Optional[str] = None) -> Set[str]:
        """Extract IDs from text.

        Args:
            text: Markdown text to search
            id_type: If specified, only extract this type (e.g., 'BR', 'API')

        Returns:
            Set of unique IDs found in text
        """
        if id_type:
            pattern = self.patterns.get(id_type)
            if pattern:
                return set(re.findall(pattern, text))
            return set()

        # Extract all ID types
        ids = set()
        for pattern in self.patterns.values():
            ids.update(re.findall(pattern, text))
        return ids

    def extract_markdown_links(self, text: str) -> List[Dict[str, str]]:
        """Extract markdown links: [text](url)

        Args:
            text: Markdown text to parse

        Returns:
            List of dicts with 'text' and 'url' keys
        """
        pattern = r'\[([^\]]+)\]\(([^)]+)\)'
        matches = re.findall(pattern, text)
        return [{'text': m[0], 'url': m[1]} for m in matches]

    def get_id_type(self, id_str: str) -> Optional[str]:
        """Get the type prefix from an ID string.

        Args:
            id_str: ID string like 'BR-001' or 'API-045'

        Returns:
            Type prefix ('BR', 'API', etc.) or None if not recognized
        """
        for id_type, pattern in self.patterns.items():
            if re.match(pattern, id_str):
                return id_type
        return None
