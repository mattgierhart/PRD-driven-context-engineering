"""Attribution text for Hephaestus inspiration

Provides standardized attribution blocks for all generated artifacts.
"""

from pathlib import Path
from typing import Optional


DEFAULT_ATTRIBUTION = """## Inspiration & Attribution

This visualization is part of the **GHM Visualization Suite**, inspired by visual
concepts from [Hephaestus](https://github.com/Ido-Levi/Hephaestus), a
semi-structured agentic framework by Ido Levi.

**Hephaestus License**: AGPL-3.0
**GHM Visualization Suite License**: MIT (Gear Heart AI, LLC)

We adapted Hephaestus's visualization approaches (dependency graphs, Kanban boards,
agent monitoring) to align with Gear Heart Methodology's documentation-first context
engineering workflow.

**No code was copied from Hephaestus.** All implementations are original, written
from scratch to comply with GHM's MIT license. We gratefully acknowledge the
inspiration and design patterns from the Hephaestus project.
"""


def get_attribution_text(template_path: Optional[Path] = None) -> str:
    """Get attribution text.

    Args:
        template_path: Optional path to attribution template file.
                      If None, uses default text.

    Returns:
        Attribution markdown text
    """
    if template_path and template_path.exists():
        return template_path.read_text()
    return DEFAULT_ATTRIBUTION


def get_attribution_html(template_path: Optional[Path] = None) -> str:
    """Get attribution as HTML.

    Args:
        template_path: Optional path to attribution template file

    Returns:
        Attribution HTML text
    """
    import re

    # Get markdown text
    md_text = get_attribution_text(template_path)

    # Simple markdown → HTML conversion
    html = md_text

    # Convert headers
    html = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)

    # Convert bold
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)

    # Convert links
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)

    # Convert line breaks
    html = html.replace('\n\n', '</p><p>')
    html = '<p>' + html + '</p>'

    return html
