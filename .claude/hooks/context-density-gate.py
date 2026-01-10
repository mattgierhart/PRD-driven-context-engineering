#!/usr/bin/env python3
"""
GHM Context Density Gate Hook (UserPromptSubmit)
Assesses context readiness before epic/gate work begins.
"""
import json
import sys
import re
from pathlib import Path

# Thresholds (tokens ~ chars/4)
MIN_EPIC_TOKENS = 500
MAX_EPIC_TOKENS = 4000
MAX_SOT_REFERENCES = 10


def estimate_tokens(text: str) -> int:
    """Rough token estimate: chars/4."""
    return len(text) // 4


def count_sot_references(content: str) -> list:
    """Find SoT ID references (BR-, UJ-, API-, CFD-, etc.)."""
    pattern = r"\b(BR|UJ|API|CFD|KPI|COMP|UI|ERR|SEC|PERF|TEST)-\d{3}\b"
    return list(set(re.findall(pattern, content, re.I)))


def resolve_epic_path(epic_num: str, slug: str | None = None) -> str:
    """Resolve EPIC-XX-<slug>.md path from epics/ directory."""
    epics_dir = Path("epics")
    if not epics_dir.exists():
        return f"epics/EPIC-{epic_num}-<slug>.md"

    if slug:
        slug = slug.strip().lower()
        candidate = epics_dir / f"EPIC-{epic_num}-{slug}.md"
        if candidate.exists():
            return str(candidate)

    matches = sorted(epics_dir.glob(f"EPIC-{epic_num}-*.md"))
    if matches:
        return str(matches[0])
    return f"epics/EPIC-{epic_num}-<slug>.md"


def check_epic_density(epic_path: str) -> dict:
    """Assess epic file for context density."""
    path = Path(epic_path)
    if not path.exists():
        return {
            "status": "missing",
            "message": f"Epic file not found: {epic_path}",
            "recommendation": "Create the epic file before starting work.",
        }

    content = path.read_text()
    tokens = estimate_tokens(content)
    sot_refs = count_sot_references(content)

    issues = []

    # Check for sparse context
    if tokens < MIN_EPIC_TOKENS and len(sot_refs) == 0:
        issues.append(
            {
                "type": "sparse",
                "message": f"Epic has ~{tokens} tokens and no SoT references.",
                "recommendation": "Add acceptance criteria, link relevant specs (BR-, UJ-), or decompose from PRD requirements before starting.",
            }
        )

    # Check for bloated epic
    if tokens > MAX_EPIC_TOKENS:
        issues.append(
            {
                "type": "dense",
                "message": f"Epic has ~{tokens} tokens (exceeds {MAX_EPIC_TOKENS} threshold).",
                "recommendation": "Consider splitting into multiple epics. Large epics cause context drift.",
            }
        )

    # Check for scope creep
    if len(sot_refs) > MAX_SOT_REFERENCES:
        unique_types = set(r[0] for r in sot_refs)
        issues.append(
            {
                "type": "broad",
                "message": f"Epic references {len(sot_refs)} SoT items across {len(unique_types)} spec types.",
                "recommendation": "Scope may be too broad. Consider splitting by spec type or domain.",
            }
        )

    if not issues:
        return {
            "status": "ready",
            "message": f"Context check passed: ~{tokens} tokens, {len(sot_refs)} SoT references.",
            "recommendation": None,
        }

    return {"status": "warning", "issues": issues}


def check_gate_readiness(version: str) -> dict:
    """Assess gate readiness for PRD version transition."""
    prd = Path("PRD.md")
    if not prd.exists():
        return {
            "status": "missing",
            "message": "PRD.md not found.",
            "recommendation": "Cannot assess gate without PRD.",
        }

    # Gate requirements by version (simplified)
    gate_requirements = {
        "0.1": ["Problem statement defined"],
        "0.2": ["Market definition complete", "Product type classified"],
        "0.3": ["Success metrics defined", "KPIs established"],
        "0.5": ["Core features specified", "User journeys documented"],
        "0.7": ["Technical architecture defined", "EPICs created"],
        "1.0": ["All specs complete", "Ready for development"],
    }

    reqs = gate_requirements.get(version, [])
    return {
        "status": "info",
        "message": f"Gate v{version} requirements: {', '.join(reqs) if reqs else 'No specific requirements defined.'}",
        "recommendation": "Verify these items are complete in PRD.md before approving gate.",
    }


def main():
    input_data = json.load(sys.stdin)
    prompt = input_data.get("prompt", "")

    # Check for epic work initiation
    epic_match = re.search(
        r"(?:start|begin|work on|continue)\s+(?:work\s+on\s+)?epic[- ]?(\d{1,2})(?:-([A-Za-z0-9-]+))?",
        prompt,
        re.I,
    )

    # Check for gate approval request
    gate_match = re.search(
        r"(?:approve|check|assess)\s+(?:the\s+)?gate\s+(?:for\s+)?v?(\d+\.\d+)",
        prompt,
        re.I,
    )

    if not epic_match and not gate_match:
        # No epic/gate reference - passthrough
        sys.exit(0)

    assessment = None

    if epic_match:
        epic_num = epic_match.group(1).zfill(2)
        slug = epic_match.group(2)
        epic_path = resolve_epic_path(epic_num, slug)
        assessment = check_epic_density(epic_path)
        context_type = f"EPIC-{epic_num}"

    elif gate_match:
        version = gate_match.group(1)
        assessment = check_gate_readiness(version)
        context_type = f"Gate v{version}"

    # Format output
    if assessment["status"] == "ready":
        message = f"""## Context Check: {context_type}

{assessment['message']}

Proceeding with work."""

    elif assessment["status"] == "warning":
        issues_text = "\n".join(
            f"- **{i['type'].upper()}**: {i['message']}\n  -> {i['recommendation']}"
            for i in assessment.get("issues", [])
        )
        message = f"""## Context Check: {context_type}

Issues detected:
{issues_text}

**Recommendation:** Address these before starting to reduce drift risk."""

    else:  # missing or info
        message = f"""## Context Check: {context_type}

{assessment['message']}
{('-> ' + assessment['recommendation']) if assessment.get('recommendation') else ''}"""

    output = {"additionalContext": message}
    print(json.dumps(output))
    sys.exit(0)


if __name__ == "__main__":
    main()
