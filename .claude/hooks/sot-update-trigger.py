#!/usr/bin/env python3
"""
GHM SoT Update Trigger Hook (Stop)
Reminds about Source of Truth updates after execution.
"""
import json
import sys
import re
from pathlib import Path

# File patterns that likely implement spec'd behavior
IMPLEMENTATION_PATTERNS = [
    r"\.py$",
    r"\.ts$",
    r"\.js$",
    r"\.tsx$",
    r"\.jsx$",
    r"\.go$",
    r"\.rs$",
    r"\.java$",
    r"\.rb$",
]

# SoT reference pattern
SOT_PATTERN = r"\b(BR|UJ|API|CFD|KPI|COMP|UI|ERR|SEC|PERF|TEST)-\d{3}\b"


def is_implementation_file(path: str) -> bool:
    """Check if file is likely implementation code."""
    return any(re.search(p, path) for p in IMPLEMENTATION_PATTERNS)


def extract_modified_files(transcript: str) -> list:
    """Extract file paths from Edit/Write tool outputs in transcript."""
    # Look for common patterns in tool outputs
    patterns = [
        r"(?:Edit|Write|Create)(?:File)?\s*[:\-]?\s*[`\"]?([^\s`\"]+)[`\"]?",
        r"Modified:\s*([^\s]+)",
        r"Created:\s*([^\s]+)",
        r"file_path[\"']?\s*:\s*[\"']([^\"']+)[\"']",
    ]

    files = set()
    for pattern in patterns:
        matches = re.findall(pattern, transcript, re.I)
        files.update(matches)

    return list(files)


def check_sot_references_in_files(files: list) -> list:
    """Check if modified files contain SoT references."""
    sot_refs = set()
    for f in files:
        path = Path(f)
        if path.exists() and path.is_file():
            try:
                content = path.read_text()
                refs = re.findall(SOT_PATTERN, content, re.I)
                sot_refs.update(refs)
            except Exception:
                pass
    return list(sot_refs)


def main():
    input_data = json.load(sys.stdin)

    # Get transcript/session info if available
    transcript = input_data.get("transcript", "")
    tool_outputs = input_data.get("tool_outputs", [])

    # Combine sources for file detection
    combined_text = transcript
    if isinstance(tool_outputs, list):
        combined_text += " ".join(str(t) for t in tool_outputs)

    modified_files = extract_modified_files(combined_text)

    if not modified_files:
        # No file modifications detected
        sys.exit(0)

    # Check for implementation files
    impl_files = [f for f in modified_files if is_implementation_file(f)]

    # Check for SoT references in modified files
    sot_refs = check_sot_references_in_files(modified_files)

    # Determine if SoT update reminder needed
    needs_reminder = bool(impl_files) or bool(sot_refs)

    if not needs_reminder:
        sys.exit(0)

    # Build reminder message
    reminder_parts = ["## SoT Update Check"]

    if impl_files:
        reminder_parts.append(
            f"\n**Implementation files modified:** {len(impl_files)} file(s)"
        )

    if sot_refs:
        reminder_parts.append(
            f"\n**SoT references found:** {', '.join(sorted(set(sot_refs)))}"
        )

    reminder_parts.append(
        """
**Action:** If this work affects documented specifications:
1. Check `README.md` -> SoT Directory for affected spec files
2. Update relevant Source of Truth files (SoT/)
3. Ensure Unique IDs remain consistent

*This is a reminder, not a blocker. Skip if changes are implementation-only.*"""
    )

    # Output as non-blocking feedback
    output = {"additionalContext": "\n".join(reminder_parts)}
    print(json.dumps(output))
    sys.exit(0)


if __name__ == "__main__":
    main()
