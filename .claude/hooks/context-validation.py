#!/usr/bin/env python3
"""
GHM Context Validation Hook (SessionStart)
Ensures agent loads 3+1 files in correct order.
"""
import json
import sys
import re
from pathlib import Path
from typing import Optional


def get_prd_lifecycle_gate() -> Optional[float]:
    """Extract current lifecycle gate from PRD.md metadata.

    Preferred source is the PRD Metadata table row:
    | **Current Lifecycle Gate** | v0.7 |
    """
    prd_path = Path("PRD.md")
    if not prd_path.exists():
        return None

    content = prd_path.read_text(encoding="utf-8", errors="ignore")

    # Prefer the explicit PRD Metadata value. If present but non-numeric (e.g., v0.x),
    # treat as unknown rather than falling back to the first v0.1/v0.2 headings.
    meta_match = re.search(
        r"^\|\s*\*\*Current Lifecycle Gate\*\*\s*\|\s*([^|]+)\|",
        content,
        re.M,
    )
    if meta_match:
        raw = meta_match.group(1).strip()
        gate_match = re.search(r"\bv(\d+\.\d+)\b", raw, re.I)
        if not gate_match:
            return None
        try:
            return float(gate_match.group(1))
        except ValueError:
            return None

    # Fallback: best-effort if metadata row is missing entirely.
    match = re.search(r"\bv(\d+\.\d+)\b", content)
    if not match:
        return None
    try:
        return float(match.group(1))
    except ValueError:
        return None


def find_epic_path(epic_num: str, slug: Optional[str] = None) -> Optional[str]:
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


def get_active_epic() -> Optional[str]:
    """Find active EPIC from README.md or epics/ directory."""
    readme = Path("README.md")
    if readme.exists():
        content = readme.read_text(encoding="utf-8", errors="ignore")

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
        candidates = []
        for path in epics_dir.glob("EPIC-*.md"):
            # Ignore templates or non-standard files like EPIC_TEMPLATE.md
            if not re.search(r"^EPIC-(\d{2})(?:-[A-Za-z0-9-]+)?\.md$", path.name):
                continue
            candidates.append(path)

        if candidates:
            def sort_key(path: Path):
                match = re.search(r"^EPIC-(\d{2})", path.name)
                return (int(match.group(1)) if match else 0, path.name)

            return str(sorted(candidates, key=sort_key, reverse=True)[0])
    return None


def main():
    # Core 3 files (always required)
    # Match documented authority chain: README → PRD → CLAUDE → EPIC
    core_files = ["README.md", "PRD.md", "CLAUDE.md"]
    missing = [f for f in core_files if not Path(f).exists()]

    if missing:
        # Warn but don't block - project may be initializing
        warning = f"Missing core files: {', '.join(missing)}"
    else:
        warning = None

    lifecycle_gate = get_prd_lifecycle_gate()
    epic_path = get_active_epic()

    # Build reading order directive
    reading_order = list(core_files)
    if epic_path:
        reading_order.append(epic_path)

    epic_note = None
    if epic_path:
        epic_note = f"- Active work unit and acceptance criteria ({epic_path})"
    elif lifecycle_gate is not None and lifecycle_gate >= 0.7:
        epic_note = "- PRD gate is v0.7+ but no active EPIC was found. Create one in `epics/` and link it from `README.md`."
    else:
        epic_note = "- EPICs not required (pre-v0.7) or lifecycle gate is unspecified."

    directive = f"""## Context Loading Required

Before responding to any task, read these files in order:
{chr(10).join(f'{i+1}. `{f}`' for i, f in enumerate(reading_order))}

This establishes:
- Current project status and navigation (README.md)
- Product definition and current lifecycle stage (PRD.md)
- Structural rules and execution discipline (CLAUDE.md)
{epic_note}
"""

    if warning:
        directive = warning + "\n\n" + directive

    output = {"additionalContext": directive}
    print(json.dumps(output))
    sys.exit(0)


if __name__ == "__main__":
    main()
