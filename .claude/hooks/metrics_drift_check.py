#!/usr/bin/env python3
"""
Metrics Drift Check — Reusable validation library.

Compares status/metrics.json against README.md section markers to detect
value disagreements. Used by multiple hooks (SessionStart, Stop, SubagentStop)
and can serve as a pre-commit validation template.

Design principles (from HomeFalcon learnings):
- README is the human-authored view. metrics.json is the machine-writable source.
- Validation ensures agreement. Never auto-generate README content from JSON.
- Uses <!-- SECTION: truth-table --> markers, not line numbers, for durability.

Usage:
  As library:  from metrics_drift_check import check_drift
  As script:   python3 .claude/hooks/metrics_drift_check.py
               Exits 0 if consistent (or no metrics.json), 1 if drift detected.
"""
import json
import re
import sys
from pathlib import Path


def load_metrics(metrics_path: str = "status/metrics.json") -> dict | None:
    """Load metrics.json. Returns None if file doesn't exist (pre-v0.7 projects)."""
    path = Path(metrics_path)
    if not path.exists():
        return None
    try:
        return json.loads(path.read_text())
    except (json.JSONDecodeError, OSError):
        return None


def extract_truth_table(readme_path: str = "README.md") -> str | None:
    """Extract content between <!-- SECTION: truth-table --> markers."""
    path = Path(readme_path)
    if not path.exists():
        return None

    content = path.read_text()

    # Extract between section markers
    match = re.search(
        r"<!-- SECTION: truth-table -->(.*?)<!-- /SECTION: truth-table -->",
        content,
        re.DOTALL,
    )
    if match:
        return match.group(1)

    # Fallback: look for a "Truth Table" heading
    match = re.search(
        r"##\s+.*Truth Table.*?\n((?:\|.*\n)+)",
        content,
        re.I,
    )
    if match:
        return match.group(1)

    return None


def normalize_number(value: str) -> str:
    """Normalize number formatting for comparison (1,552 -> 1552, 88.18% -> 88.18)."""
    cleaned = value.strip().replace(",", "").rstrip("%")
    try:
        # Normalize float representation (88.180 -> 88.18)
        return str(float(cleaned))
    except ValueError:
        return cleaned


def extract_readme_metrics(readme_path: str = "README.md") -> dict:
    """Extract metric values from README, searching truth-table first, then full doc.

    Returns dict with normalized keys and raw values:
    {
        "test_count": "1552/1552",
        "coverage": "88.18%",
        "risk_score": "12",
        ...
    }
    """
    path = Path(readme_path)
    if not path.exists():
        return {}

    # Prefer truth table section, fall back to full content
    content = extract_truth_table(readme_path)
    if content is None:
        content = path.read_text()

    metrics = {}

    # Pattern: table rows like "| Test Count | 1552/1552 | ..."
    # or "| Coverage (stmts) | 88.18% | ..."
    table_rows = re.findall(r"\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|", content)
    for label, value in table_rows:
        label_lower = label.strip().lower()
        value_stripped = value.strip()

        if "test" in label_lower and ("count" in label_lower or "pass" in label_lower):
            metrics["test_count"] = value_stripped
        elif "suite" in label_lower:
            metrics["suite_count"] = value_stripped
        elif "coverage" in label_lower and "stmt" in label_lower:
            metrics["coverage_statements"] = value_stripped
        elif "coverage" in label_lower and "branch" in label_lower:
            metrics["coverage_branches"] = value_stripped
        elif "coverage" in label_lower:
            metrics["coverage"] = value_stripped
        elif "risk" in label_lower and "score" in label_lower:
            metrics["risk_score"] = value_stripped

    return metrics


def map_metrics_json_to_comparable(metrics_json: dict) -> dict:
    """Map metrics.json structure to comparable keys.

    Handles common metrics.json shapes:
    - { "tests": { "passed": 1552, "total": 1552 }, "suites": { ... } }
    - { "coverage": { "statements": 88.18, "branches": 72.5 } }
    - { "risk": { "score": 12 } }
    """
    comparable = {}

    # Test counts
    tests = metrics_json.get("tests", {})
    if isinstance(tests, dict):
        passed = tests.get("passed", tests.get("pass"))
        total = tests.get("total")
        if passed is not None and total is not None:
            comparable["test_count"] = f"{passed}/{total}"

    suites = metrics_json.get("suites", {})
    if isinstance(suites, dict):
        passed = suites.get("passed", suites.get("pass"))
        total = suites.get("total")
        if passed is not None and total is not None:
            comparable["suite_count"] = f"{passed}/{total}"

    # Coverage
    coverage = metrics_json.get("coverage", {})
    if isinstance(coverage, dict):
        stmts = coverage.get("statements", coverage.get("stmts"))
        if stmts is not None:
            comparable["coverage_statements"] = f"{stmts}%"
            comparable["coverage"] = f"{stmts}%"
        branches = coverage.get("branches")
        if branches is not None:
            comparable["coverage_branches"] = f"{branches}%"

    # Risk
    risk = metrics_json.get("risk", {})
    if isinstance(risk, dict):
        score = risk.get("score")
        if score is not None:
            comparable["risk_score"] = str(score)

    return comparable


def check_drift(
    metrics_path: str = "status/metrics.json",
    readme_path: str = "README.md",
) -> dict:
    """Compare metrics.json against README.md and return drift report.

    Returns:
        {
            "has_drift": bool,
            "skipped": bool,         # True if metrics.json doesn't exist
            "drifts": [              # List of specific disagreements
                {
                    "metric": "test_count",
                    "metrics_json": "1552/1552",
                    "readme": "1565/1565",
                }
            ],
            "checked": int,          # Number of metrics compared
        }
    """
    metrics_json = load_metrics(metrics_path)
    if metrics_json is None:
        return {"has_drift": False, "skipped": True, "drifts": [], "checked": 0}

    json_values = map_metrics_json_to_comparable(metrics_json)
    readme_values = extract_readme_metrics(readme_path)

    if not json_values or not readme_values:
        return {"has_drift": False, "skipped": True, "drifts": [], "checked": 0}

    drifts = []
    checked = 0

    for key, json_val in json_values.items():
        if key in readme_values:
            checked += 1
            readme_val = readme_values[key]

            # Normalize both sides for comparison
            if normalize_number(json_val) != normalize_number(readme_val):
                drifts.append(
                    {
                        "metric": key,
                        "metrics_json": json_val,
                        "readme": readme_val,
                    }
                )

    return {
        "has_drift": len(drifts) > 0,
        "skipped": False,
        "drifts": drifts,
        "checked": checked,
    }


def format_drift_report(result: dict, context: str = "") -> str:
    """Format drift check result as human-readable markdown."""
    if result["skipped"]:
        return ""

    if not result["has_drift"]:
        return ""

    lines = [f"## Metrics Drift Detected{f' ({context})' if context else ''}"]
    lines.append("")
    lines.append(
        "`status/metrics.json` and `README.md` disagree on these values:"
    )
    lines.append("")

    for drift in result["drifts"]:
        label = drift["metric"].replace("_", " ").title()
        lines.append(
            f"- **{label}**: metrics.json says `{drift['metrics_json']}`, "
            f"README says `{drift['readme']}`"
        )

    lines.append("")
    lines.append(
        "**Action**: Update README Truth Table to match metrics.json, "
        "or re-run tests if metrics.json is stale."
    )
    return "\n".join(lines)


def main():
    """Run as standalone script. Exit 0 if consistent, 1 if drift."""
    result = check_drift()

    if result["skipped"]:
        # No metrics.json — nothing to validate
        sys.exit(0)

    report = format_drift_report(result, context="pre-commit check")
    if report:
        print(report, file=sys.stderr)
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
