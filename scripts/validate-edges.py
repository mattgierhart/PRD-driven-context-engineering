#!/usr/bin/env python3
"""Validate required cross-reference edges in the ID graph (U2 — schema contract).

Companion to ``validate-ids.sh``: that script checks *structural* integrity
(dangling / orphan / duplicate IDs); this checks *semantic* integrity — that
each durable spec carries the cross-reference edges the methodology requires of
its type. This is the enforcement half of "if it's not in the graph it isn't
true": it turns the ID registry from a convention into a checked contract (P12).

Rules are declared in ``.claude/domain-profile.yaml`` under ``required_edges:``
and are opt-in — a repo (or the methodology template) that declares none
validates clean. Rule schema (see docs/DEVELOPMENT_GRAPH.md §14):

    required_edges:
      - from: UJ            # every UJ- entry...
        requires: SCR       # ...must reference at least one SCR-
        direction: outbound # edge authored in the UJ body (default)
        severity: warn      # warn (report, exit 0) | block (report, exit 1)
        description: "A user journey must map to at least one screen"
      - from: API
        requires: TEST
        direction: inbound  # a TEST- entry must reference this API-

``requires`` may be a single prefix or a list (each is independently required).
``direction``: ``outbound`` (default) — the `from` entry's body must reference a
`requires` ID; ``inbound`` — some `requires` entry must reference the `from` one
(the convention for test coverage, where a TEST- points back at the API-/BR-).

Exit codes: 0 = clean OR warn-only OR no rules; 1 = >=1 ``block``-severity
violation; 2 = invalid rule/registry configuration. Mirrors validate-ids.sh so
the two compose in a gate without silently weakening misspelled rules.

Usage:
    python3 scripts/validate-edges.py [--repo PATH] [--quiet] [--json]
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _readiness.common import (  # noqa: E402
    SoTEntry,
    find_repo_root,
    index_all_entries,
    load_domain_profile,
    load_required_edges,
)

BAR = "━" * 43


def _prefix_of(id_: str) -> str:
    return id_.split("-")[0]


def build_inbound_prefixes(entries: dict[str, SoTEntry]) -> dict[str, set[str]]:
    """Map each referenced ID → the set of prefixes of entries that reference it."""
    inbound: dict[str, set[str]] = {}
    for entry in entries.values():
        for ref in entry.outbound_refs():
            inbound.setdefault(ref, set()).add(entry.prefix)
    return inbound


def validate_rule_schema(rules: list[dict], registered: set[str]) -> list[dict]:
    """Return normalized rules or raise ValueError on an unsafe configuration."""
    normalized: list[dict] = []
    for index, raw_rule in enumerate(rules, 1):
        label = f"required_edges rule {index}"
        if not isinstance(raw_rule, dict):
            raise ValueError(f"{label} must be an object")
        allowed_keys = {"from", "requires", "direction", "severity", "description"}
        unknown_keys = sorted(set(raw_rule) - allowed_keys)
        if unknown_keys:
            raise ValueError(f"{label} has unknown key(s): {', '.join(unknown_keys)}")

        from_pfx = raw_rule.get("from")
        if not isinstance(from_pfx, str) or not from_pfx:
            raise ValueError(f"{label}.from must be a registered prefix string")
        if from_pfx not in registered:
            raise ValueError(f"{label}.from uses unregistered prefix {from_pfx!r}")

        raw_requires = raw_rule.get("requires")
        if isinstance(raw_requires, str):
            requires = [raw_requires]
        elif isinstance(raw_requires, list) and raw_requires:
            requires = raw_requires
        else:
            raise ValueError(f"{label}.requires must be a prefix string or non-empty list")
        if not all(isinstance(prefix, str) and prefix for prefix in requires):
            raise ValueError(f"{label}.requires must contain only prefix strings")
        unknown = sorted(set(requires) - registered)
        if unknown:
            raise ValueError(f"{label}.requires uses unregistered prefix(es): {', '.join(unknown)}")

        direction = raw_rule.get("direction", "outbound")
        if direction not in {"outbound", "inbound"}:
            raise ValueError(f"{label}.direction must be outbound or inbound")
        severity = raw_rule.get("severity", "warn")
        if severity not in {"warn", "block"}:
            raise ValueError(f"{label}.severity must be warn or block")
        description = raw_rule.get("description", "")
        if not isinstance(description, str):
            raise ValueError(f"{label}.description must be a string when present")

        normalized.append({
            "from": from_pfx,
            "requires": requires,
            "direction": direction,
            "severity": severity,
            "description": description,
        })
    return normalized


def evaluate_rules(entries: dict[str, SoTEntry], rules: list[dict]) -> list[dict]:
    """Return one violation dict per (entry, missing-required-prefix) pair."""
    inbound = build_inbound_prefixes(entries)
    violations: list[dict] = []
    for rule in rules:
        from_pfx = rule.get("from")
        raw_req = rule.get("requires")
        if not from_pfx or not raw_req:
            continue
        reqs = [raw_req] if isinstance(raw_req, str) else list(raw_req)
        direction = str(rule.get("direction") or "outbound").lower()
        severity = str(rule.get("severity") or "warn").lower()
        description = rule.get("description") or ""

        froms = [e for e in entries.values() if e.prefix == from_pfx]
        for entry in froms:
            out_prefixes = {_prefix_of(r) for r in entry.outbound_refs()}
            for req in reqs:
                if direction == "inbound":
                    satisfied = req in inbound.get(entry.id, set())
                else:
                    satisfied = req in out_prefixes
                if not satisfied:
                    violations.append({
                        "id": entry.id,
                        "from": from_pfx,
                        "requires": req,
                        "direction": direction,
                        "severity": severity,
                        "description": description,
                        "file": entry.file,
                        "line": entry.line,
                    })
    return violations


def _print_human(violations: list[dict], rule_count: int, quiet: bool) -> None:
    if quiet:
        return
    print()
    print(BAR)
    print("  Required cross-reference edges")
    print(BAR)
    if rule_count == 0:
        print("  No required_edges declared in domain-profile.yaml — skipping.")
        return
    if not violations:
        print(f"  No violations across {rule_count} rule(s). CLEAN")
        return
    blocks = [v for v in violations if v["severity"] == "block"]
    warns = [v for v in violations if v["severity"] != "block"]
    for v in violations:
        arrow = "←" if v["direction"] == "inbound" else "→"
        tag = "BLOCK" if v["severity"] == "block" else "warn"
        loc = f"{v['file']}:{v['line']}"
        desc = f" — {v['description']}" if v["description"] else ""
        print(f"  [{tag}] {v['id']} {arrow} {v['requires']}- missing ({loc}){desc}")
    print(f"  {len(blocks)} blocking, {len(warns)} warning")


def run(repo: Path, quiet: bool, as_json: bool) -> int:
    rules = validate_rule_schema(
        load_required_edges(repo),
        set(load_domain_profile(repo)),
    )
    entries = index_all_entries(repo) if rules else {}
    violations = evaluate_rules(entries, rules)
    blocks = [v for v in violations if v["severity"] == "block"]

    if as_json:
        print(json.dumps({
            "rules": len(rules),
            "blocking": len(blocks),
            "violations": violations,
        }, indent=2))
    else:
        _print_human(violations, len(rules), quiet)

    return 1 if blocks else 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate required cross-reference edges.")
    ap.add_argument("--repo", type=Path, default=None,
                    help="Repo root (default: discovered from cwd).")
    ap.add_argument("--quiet", action="store_true",
                    help="Suppress human output; set exit code only.")
    ap.add_argument("--json", action="store_true",
                    help="Emit machine-readable JSON (implies quiet for human text).")
    args = ap.parse_args()
    repo = find_repo_root(args.repo or Path.cwd())
    try:
        return run(repo, quiet=args.quiet, as_json=args.json)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        if args.json:
            print(json.dumps({"configuration_error": str(exc)}, indent=2))
        elif not args.quiet:
            print(f"error: invalid required_edges configuration: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
