#!/usr/bin/env python3
"""Read-only consistency audit for the PRD lifecycle contract."""

from __future__ import annotations

import ast
import re
from pathlib import Path
from typing import Any

from conformance import Finding, Severity


GATE_HEADING_RE = re.compile(
    r"^##\s+(v\d\.\d+)\s+→\s+(v\d\.\d+)\s+Gate\b", re.MULTILINE
)
PREFIX_RE = re.compile(r"\b([A-Z]{2,}(?:-[A-Z]+)*)-")


def _load_gate_requirements(stage_path: Path) -> dict[str, dict[str, Any]]:
    tree = ast.parse(stage_path.read_text(encoding="utf-8"))
    for node in tree.body:
        if isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            if node.target.id == "GATE_REQUIREMENTS":
                value = ast.literal_eval(node.value)
                if not isinstance(value, dict):
                    break
                return value
    raise ValueError(f"GATE_REQUIREMENTS not found in {stage_path}")


def _gate_criteria_prefixes(path: Path) -> dict[str, set[str]]:
    text = path.read_text(encoding="utf-8")
    headings = list(GATE_HEADING_RE.finditer(text))
    result: dict[str, set[str]] = {}
    for index, heading in enumerate(headings):
        start = heading.end()
        end = headings[index + 1].start() if index + 1 < len(headings) else len(text)
        section = text[start:end]
        prefixes = {
            match.group(1)
            for match in re.finditer(
                r"\*\*[^*\n]+\*\*\s*\(([A-Z]{2,}(?:-[A-Z]+)*)\)",
                section,
            )
        }
        result[heading.group(2)] = prefixes
    return result


def _domain_prefix_owners(path: Path) -> dict[str, str]:
    owners: dict[str, str] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        match = re.match(
            r'^\s{2}([A-Z][A-Z0-9-]*):\s+\{\s*file:\s*"([^"]+)"',
            line,
        )
        if match:
            owners[match.group(1)] = match.group(2)
    return owners


def _registry_stage(path: Path, prefix: str) -> str:
    pattern = re.compile(
        rf"^\|\s*\*\*{re.escape(prefix)}\*\*\s*\|.*?\|\s*(v\d\.\d+)\b",
        re.MULTILINE,
    )
    match = pattern.search(path.read_text(encoding="utf-8"))
    return match.group(1) if match else ""


def audit_repository_lifecycle(repo: Path) -> tuple[Finding, ...]:
    repo = repo.resolve()
    stage_path = repo / "scripts" / "_readiness" / "stage.py"
    criteria_path = (
        repo
        / ".claude"
        / "skills"
        / "ghm-gate-check"
        / "references"
        / "gate-criteria.md"
    )
    requirements = _load_gate_requirements(stage_path)
    criteria_prefixes = _gate_criteria_prefixes(criteria_path)
    owners = _domain_prefix_owners(repo / ".claude" / "domain-profile.yaml")
    readme = (repo / "README.md").read_text(encoding="utf-8")
    prd = (repo / "PRD.md").read_text(encoding="utf-8")
    registry = repo / "SoT" / "SoT.UNIQUE_ID_SYSTEM.md"
    findings: list[Finding] = []

    for target, expected_prefixes in sorted(criteria_prefixes.items()):
        executable = set(requirements.get(target, {}).get("required_prefixes", {}))
        missing = sorted(expected_prefixes - executable)
        for prefix in missing:
            findings.append(
                Finding(
                    "LIFECYCLE_GATE_REQUIREMENT_GAP",
                    Severity.CONFLICT,
                    (target, prefix),
                    f"Gate prose requires {prefix}, but the executable count "
                    f"contract for {target} does not.",
                )
            )

    for target, config in sorted(requirements.items()):
        for relative in config.get("relevant_sots", ()):
            if not (repo / relative).is_file():
                findings.append(
                    Finding(
                        "LIFECYCLE_RELEVANT_SOURCE_MISSING",
                        Severity.CONFLICT,
                        (target, relative),
                        "Executable readiness references a source file that does not exist.",
                    )
                )
        for prefix in config.get("required_prefixes", {}):
            owner = owners.get(prefix)
            if not owner:
                continue
            named_sources = set(config.get("relevant_sots", ()))
            wrong_named_source = {
                source
                for source in named_sources
                if Path(source).stem.casefold().endswith(prefix.casefold() + "s")
                and source != owner
            }
            if wrong_named_source:
                findings.append(
                    Finding(
                        "LIFECYCLE_OWNER_CONFLICT",
                        Severity.CONFLICT,
                        (target, prefix, owner, *sorted(wrong_named_source)),
                        f"{prefix} is owned by {owner}, but readiness names a "
                        "different source.",
                    )
                )

    readme_v02 = next(
        (
            line
            for line in readme.splitlines()
            if "| **v0.2**" in line and "Business Rules" in line and "created" in line
        ),
        "",
    )
    if readme_v02:
        readme_prefixes = set(PREFIX_RE.findall(readme_v02))
        for prefix in sorted(readme_prefixes):
            registry_value = _registry_stage(registry, prefix)
            if registry_value and registry_value != "v0.2":
                findings.append(
                    Finding(
                        "LIFECYCLE_PREFIX_STAGE_CONFLICT",
                        Severity.CONFLICT,
                        (prefix, "README:v0.2", f"registry:{registry_value}"),
                        f"README says {prefix} is created in v0.2, while the "
                        f"ID registry assigns it to {registry_value}.",
                    )
                )

    v10_name = requirements.get("v1.0", {}).get("name", "")
    methodology_calls_v10_adoption = (
        "v1.0 Market Adoption" in prd
        and "| **v1.0**" in readme
        and "Market Adoption" in readme
    )
    if methodology_calls_v10_adoption and "Launch" in v10_name:
        findings.append(
            Finding(
                "LIFECYCLE_TARGET_NAME_CONFLICT",
                Severity.CONFLICT,
                ("v1.0", "Market Adoption", v10_name),
                "The methodology names v1.0 Market Adoption, while executable "
                "readiness names the target Launch.",
            )
        )

    v10_row = next(
        (line for line in readme.splitlines() if "| **v1.0**" in line), ""
    )
    v10_required = set(requirements.get("v1.0", {}).get("required_prefixes", {}))
    if "ADO-" in v10_row and "ADO" in owners and "ADO" not in v10_required:
        findings.append(
            Finding(
                "LIFECYCLE_ADOPTION_UNGATED",
                Severity.CAUTION,
                ("v1.0", "ADO"),
                "The v1.0 lifecycle describes ADO evidence, but no executable "
                "readiness requirement validates adoption artifacts.",
            )
        )
    return tuple(sorted(findings))

