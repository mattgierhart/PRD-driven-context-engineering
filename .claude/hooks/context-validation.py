#!/usr/bin/env python3
"""
GHM Context Validation Hook (SessionStart)
Ensures agent loads 3+1 files in correct order.
"""
import json
import sys
import re
from pathlib import Path


def get_prd_version():
    """Extract current version from PRD.md header or status section."""
    prd_path = Path("PRD.md")
    if not prd_path.exists():
        return None

    content = prd_path.read_text()[:2000]  # First 2000 chars
    # Match patterns like "Current Version: v0.5" or "## v0.5 — "
    match = re.search(r"v(\d+\.\d+)", content)
    return float(match.group(1)) if match else None


def find_epic_path(epic_num: str, slug: str | None = None) -> str | None:
    """Resolve EPIC file path using EPIC-XX-<slug>.md convention."""
    epics_dir = Path("epics")
    if not epics_dir.exists():
        return None

    if slug:
        slug = slug.strip().lower()
        candidate = epics_dir / f"EPIC-{epic_num}-{slug}.md"
        if candidate.exists():
            return str(candidate)

    matches = sorted(epics_dir.glob(f"EPIC-{epic_num}-*.md"))
    if matches:
        return str(matches[0])
    return None


def get_active_epic():
    """Find active EPIC from README.md or epics/ directory."""
    readme = Path("README.md")
    if readme.exists():
        content = readme.read_text()

        # Prefer explicit path if present
        path_match = re.search(
            r"(epics/EPIC-\d{2}(?:-[A-Za-z0-9-]+)?\.md)", content
        )
        if path_match:
            epic_path = Path(path_match.group(1))
            if epic_path.exists():
                return str(epic_path)

        # Look for "Active EPIC: EPIC-XX-slug" or similar
        match = re.search(
            r"(?:active|current)\s+epic[:\s]+EPIC-(\d{2})(?:-([A-Za-z0-9-]+))?",
            content,
            re.I,
        )
        if match:
            epic_num = match.group(1)
            slug = match.group(2)
            resolved = find_epic_path(epic_num, slug)
            if resolved:
                return resolved

        # Fallback: any EPIC mention in README
        match = re.search(r"EPIC-(\d{2})(?:-([A-Za-z0-9-]+))?", content, re.I)
        if match:
            epic_num = match.group(1)
            slug = match.group(2)
            resolved = find_epic_path(epic_num, slug)
            if resolved:
                return resolved

    # Fallback: find highest-numbered epic file
    epics_dir = Path("epics")
    if epics_dir.exists():
        candidates = list(epics_dir.glob("EPIC-*.md"))
        if candidates:
            def sort_key(path: Path) -> tuple[int, str]:
                match = re.search(r"EPIC-(\d{2})-", path.name)
                return (int(match.group(1)) if match else 0, path.name)

            return str(sorted(candidates, key=sort_key, reverse=True)[0])
    return None


def main():
    # Core 3 files (always required)
    core_files = ["CLAUDE.md", "README.md", "PRD.md"]
    missing = [f for f in core_files if not Path(f).exists()]

    if missing:
        # Warn but don't block - project may be initializing
        warning = f"Missing core files: {', '.join(missing)}"
    else:
        warning = None

    # Determine reading order based on PRD version
    version = get_prd_version()
    epic_path = None

    if version and version >= 0.7:
        epic_path = get_active_epic()

    # Build reading order directive
    reading_order = ["CLAUDE.md", "README.md", "PRD.md"]
    if epic_path:
        reading_order.append(epic_path)

    directive = f"""## Context Loading Required

Before responding to any task, read these files in order:
{chr(10).join(f'{i+1}. `{f}`' for i, f in enumerate(reading_order))}

This establishes:
- Structural rules and documentation discipline (CLAUDE.md)
- Current project status and navigation (README.md)
- Product definition and current lifecycle stage (PRD.md)
{'- Active work unit and acceptance criteria (' + epic_path + ')' if epic_path else '- EPICs not yet created (pre-v0.7)'}
"""

    if warning:
        directive = warning + "\n\n" + directive

    output = {"additionalContext": directive}
    print(json.dumps(output))
    sys.exit(0)


if __name__ == "__main__":
    main()
