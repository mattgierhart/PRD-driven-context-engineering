#!/usr/bin/env python3
"""
Cascade Checklist Generator — Context-specific cascade guidance.

Given a list of changed files (or file categories), outputs the specific
cascade checklist for that change type. Replaces generic "update SoT" reminders
with actionable, file-specific steps.

Design principles (from HomeFalcon learnings):
- Abstract cascade rules ("update README") don't work for subagents.
- Specific checklists with section anchors (not line numbers) are durable.
- Checklists are data-driven and customizable per project.

Usage:
  As library:  from cascade_checklist import get_checklists
  As script:   echo '["src/api/handler.py", "tests/test_auth.py"]' | \
               python3 .claude/hooks/cascade-checklist.py
"""
import json
import re
import sys
from pathlib import Path

# Checklist definitions keyed by change category.
# Each entry has:
#   trigger: list of glob-like patterns that activate this checklist
#   steps: ordered list of cascade actions with section anchors
CHECKLISTS = {
    "test_changes": {
        "trigger": [
            r"\.test\.",
            r"\.spec\.",
            r"__tests__/",
            r"tests?/",
            r"\.test$",
        ],
        "steps": [
            "Verify `status/metrics.json` was updated (posttest hook should handle this automatically)",
            "Update README `<!-- SECTION: truth-table -->` if test count or coverage changed",
            "Update `SoT/SoT.TESTING.md` if test structure changed (new suites, removed suites, changed categories)",
        ],
    },
    "epic_phase_change": {
        "trigger": [
            r"epics/EPIC-.*\.md$",
        ],
        "steps": [
            "Update README `<!-- SECTION: status-dashboard -->` Active EPICs table",
            "If EPIC completed: move entry to Completed EPICs section",
            "Update `PRD.md` progress notes if this represents a milestone",
            "Update README `<!-- SECTION: status-header -->` if Active EPIC changed",
        ],
    },
    "api_changes": {
        "trigger": [
            r"/api/",
            r"/routes/",
            r"/endpoints/",
            r"\.controller\.",
            r"\.handler\.",
        ],
        "steps": [
            "Update `SoT/SoT.API_CONTRACTS.md` with new/changed endpoints",
            "Update relevant `TEST-` entries if contract shape changed",
            "Check if `API-` IDs need new entries or version bumps",
        ],
    },
    "schema_changes": {
        "trigger": [
            r"migrations?/",
            r"schema",
            r"\.model\.",
            r"models/",
            r"entities/",
        ],
        "steps": [
            "Update `SoT/SoT.DATA_MODEL.md` with schema changes",
            "Check if `DBT-` entries need updating",
            "Verify API contracts still match the new schema shape",
        ],
    },
    "business_rule_changes": {
        "trigger": [
            r"rules/",
            r"policies/",
            r"validators/",
            r"constraints/",
        ],
        "steps": [
            "Update `SoT/SoT.BUSINESS_RULES.md` with new/changed rules",
            "Check if `BR-` IDs need new entries",
            "Verify test coverage exists for the changed business logic",
        ],
    },
    "sot_changes": {
        "trigger": [
            r"SoT/",
        ],
        "steps": [
            "Verify cross-references to other SoT files remain valid",
            "Check if README needs updating to reflect changed specs",
            "Ensure Unique IDs are registered in `SoT/SoT.UNIQUE_ID_SYSTEM.md`",
        ],
    },
    "readme_changes": {
        "trigger": [
            r"README\.md$",
        ],
        "steps": [
            "If metrics were updated: verify they match `status/metrics.json`",
            "If status changed: verify `<!-- SECTION: status-header -->` and `<!-- SECTION: status-dashboard -->` agree",
            "Avoid duplicating metric values outside the Truth Table and status header",
        ],
    },
    "config_changes": {
        "trigger": [
            r"package\.json$",
            r"tsconfig",
            r"\.env\.example",
            r"docker-compose",
            r"Dockerfile",
        ],
        "steps": [
            "Update `SoT/SoT.DEPLOYMENT.md` if deployment config changed",
            "Check if `DEP-` or `RUN-` entries need updating",
            "Verify README Quick Commands section still works",
        ],
    },
}


def classify_files(file_paths: list[str]) -> dict[str, list[str]]:
    """Classify changed files into checklist categories.

    Returns dict mapping category name to list of matching file paths.
    A file can match multiple categories.
    """
    matches = {}
    for category, config in CHECKLISTS.items():
        category_matches = []
        for file_path in file_paths:
            for pattern in config["trigger"]:
                if re.search(pattern, file_path, re.I):
                    category_matches.append(file_path)
                    break
        if category_matches:
            matches[category] = category_matches
    return matches


def get_checklists(file_paths: list[str]) -> list[dict]:
    """Get applicable cascade checklists for a set of changed files.

    Returns list of checklist dicts:
    [
        {
            "category": "test_changes",
            "trigger_files": ["tests/test_auth.py"],
            "steps": ["Verify status/metrics.json...", ...],
        }
    ]
    """
    classifications = classify_files(file_paths)
    result = []
    for category, matching_files in classifications.items():
        result.append(
            {
                "category": category,
                "trigger_files": matching_files,
                "steps": CHECKLISTS[category]["steps"],
            }
        )
    return result


def format_checklists(checklists: list[dict]) -> str:
    """Format checklists as human-readable markdown."""
    if not checklists:
        return ""

    lines = ["## Cascade Checklist"]
    lines.append("")
    lines.append(
        "The following files were modified. Complete these cascade steps:"
    )

    for checklist in checklists:
        category_label = checklist["category"].replace("_", " ").title()
        lines.append("")
        lines.append(f"### {category_label}")
        files_str = ", ".join(f"`{f}`" for f in checklist["trigger_files"][:3])
        if len(checklist["trigger_files"]) > 3:
            files_str += f" (+{len(checklist['trigger_files']) - 3} more)"
        lines.append(f"*Triggered by: {files_str}*")
        lines.append("")
        for i, step in enumerate(checklist["steps"], 1):
            lines.append(f"{i}. {step}")

    lines.append("")
    lines.append(
        "*Skip steps that don't apply. These are context-specific reminders, not blockers.*"
    )
    return "\n".join(lines)


def main():
    """Read file list from stdin (JSON array), output checklists."""
    try:
        file_paths = json.load(sys.stdin)
    except json.JSONDecodeError:
        # Try line-separated input
        sys.stdin.seek(0)
        file_paths = [line.strip() for line in sys.stdin if line.strip()]

    if not isinstance(file_paths, list):
        file_paths = [str(file_paths)]

    checklists = get_checklists(file_paths)
    output = format_checklists(checklists)

    if output:
        print(output)
    sys.exit(0)


if __name__ == "__main__":
    main()
