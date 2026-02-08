#!/usr/bin/env python3
"""
GHM SoT Update Trigger Hook (Stop)
Reminds about Source of Truth updates after execution.
Now provides context-specific cascade checklists instead of generic reminders.
"""
import json
import sys
import re
from pathlib import Path

# Import cascade checklist and drift checker (same directory)
sys.path.insert(0, str(Path(__file__).parent))
try:
    from cascade_checklist import get_checklists, format_checklists

    HAS_CASCADE = True
except ImportError:
    HAS_CASCADE = False

try:
    from metrics_drift_check import check_drift, format_drift_report

    HAS_DRIFT_CHECK = True
except ImportError:
    HAS_DRIFT_CHECK = False

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
SOT_PATTERN = r"\b[A-Z]{2,4}(?:-[A-Z]{2,4})?-\d{3}\b"
SOT_RE = re.compile(SOT_PATTERN, re.I)


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
                content = path.read_text(encoding="utf-8", errors="ignore")
                refs = SOT_RE.findall(content)
                sot_refs.update(r.upper() for r in refs)
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

    # Check for SoT references in modified implementation files (if any)
    sot_refs = check_sot_references_in_files(impl_files) if impl_files else []

    # Determine if SoT update reminder needed
    # Fire only when implementation files were modified to avoid noise on doc-only edits.
    needs_reminder = bool(impl_files)

    if not needs_reminder:
        sys.exit(0)

    # Build context-specific guidance instead of generic reminder
    reminder_parts = ["## SoT Update Check"]

    if impl_files:
        reminder_parts.append(
            f"\n**Implementation files modified:** {len(impl_files)} file(s)"
        )

    if sot_refs:
        reminder_parts.append(
            f"\n**SoT references found:** {', '.join(sorted(set(sot_refs)))}"
        )

    # Generate context-specific cascade checklists if available
    if HAS_CASCADE and modified_files:
        checklists = get_checklists(modified_files)
        cascade_output = format_checklists(checklists)
        if cascade_output:
            reminder_parts.append("\n" + cascade_output)
        else:
            # Fallback to generic reminder if no checklists matched
            reminder_parts.append(
                """
**Action:** If this work affects documented specifications:
1. Check `README.md` -> SoT Directory for affected spec files
2. Update relevant Source of Truth files (SoT/)
3. Ensure Unique IDs remain consistent

*This is a reminder, not a blocker. Skip if changes are implementation-only.*"""
            )
    else:
        # Fallback when cascade_checklist module not available
        reminder_parts.append(
            """
**Action:** If this work affects documented specifications:
1. Check `README.md` -> SoT Directory for affected spec files
2. Update relevant Source of Truth files (SoT/)
3. Ensure Unique IDs remain consistent

*This is a reminder, not a blocker. Skip if changes are implementation-only.*"""
        )

    # Check for metrics drift introduced during this session
    if HAS_DRIFT_CHECK:
        drift_result = check_drift()
        drift_report = format_drift_report(drift_result, context="post-work check")
        if drift_report:
            reminder_parts.append("\n" + drift_report)

    # Output as non-blocking feedback
    output = {"additionalContext": "\n".join(reminder_parts)}
    print(json.dumps(output))
    sys.exit(0)


if __name__ == "__main__":
    main()
