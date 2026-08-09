#!/usr/bin/env python3
"""Reconstruct decision state as of a past PRD version (U1 — valid-time query).

Git gives you *transaction time* — when a file changed. It does not answer
"which architecture decision was authoritative while we were building v0.6?".
That is *valid time*, and it lives in three optional fields on durable decision
IDs (see SoT/SoT.UNIQUE_ID_SYSTEM.md §1.6):

    **Valid From**: v0.6        # version the decision took effect
    **Valid To**: v0.8          # version it stopped being authoritative (— while current)
    **Invalidated By**: ARC-002 # the ID that superseded it (— while current)

Given a target version, this prints the decisions that were in force then —
keeping a single current reality *and* an auditable, queryable history without
git archaeology. Unstamped entries are treated as always-valid (lenient default).

Usage:
    python3 scripts/asof.py <version> [--prefix ARC,TECH] [--repo PATH] [--json]

Examples:
    python3 scripts/asof.py v0.6
    python3 scripts/asof.py v0.9 --prefix ARC --repo tests/fixtures/temporal_repo
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from _readiness.common import find_repo_root, index_all_entries  # noqa: E402

_UNSET = {"—", "-", "", "current", "none", "n/a", "tbd"}


def parse_version(raw: str | None) -> tuple[int, ...] | None:
    """Parse 'v0.6' / '0.6.1' → (0, 6) / (0, 6, 1). Returns None if unset/unparseable."""
    if not raw:
        return None
    s = re.sub(r"<!--.*?-->", "", raw).strip().lstrip("vV").strip()
    if s.lower() in _UNSET:
        return None
    try:
        return tuple(int(p) for p in s.split("."))
    except ValueError:
        return None


def _field(body: str, name: str) -> str | None:
    """Extract a `**Name**: value` / `- Name: value` field from an entry body."""
    m = re.search(rf"^\s*-?\s*\*?\*?{name}\*?\*?:\s*(.+?)\s*$",
                  body, re.IGNORECASE | re.MULTILINE)
    if not m:
        return None
    val = re.sub(r"<!--.*?-->", "", m.group(1)).strip()
    return val or None


def _classify(valid_from, valid_to, target: tuple[int, ...]) -> str:
    """Where does `target` fall relative to the entry's [valid_from, valid_to) window?"""
    if valid_from is not None and target < valid_from:
        return "future"       # decided after the target version
    if valid_to is not None and target >= valid_to:
        return "superseded"   # replaced at or before the target version
    return "current"          # authoritative as of the target version


def _heading_label(repo: Path, rel_file: str, line: int, entry_id: str, cache: dict) -> str:
    """Pull the human label off the entry's heading line (after the ID)."""
    if rel_file not in cache:
        try:
            cache[rel_file] = (repo / rel_file).read_text(errors="replace").splitlines()
        except OSError:
            cache[rel_file] = []
    lines = cache[rel_file]
    raw = lines[line - 1] if 0 < line <= len(lines) else ""
    return re.sub(
        rf"^#{{1,3}}\s+{re.escape(entry_id)}\s*[|:\-]?\s*", "", raw
    ).strip()


def as_of(repo: Path, target_raw: str, prefixes: list[str]) -> dict:
    """Reconstruct decision state as of `target_raw`, grouped current/superseded/future."""
    target = parse_version(target_raw)
    if target is None:
        raise SystemExit(f"error: could not parse version '{target_raw}' (try 'v0.6')")

    wanted = {p.upper() for p in prefixes}
    entries = index_all_entries(repo)
    cache: dict = {}
    groups: dict[str, list[dict]] = {"current": [], "superseded": [], "future": []}

    for entry in entries.values():
        if entry.prefix not in wanted:
            continue
        vf_raw = _field(entry.body, "Valid From")
        vt_raw = _field(entry.body, "Valid To")
        inv = _field(entry.body, "Invalidated By")
        vf, vt = parse_version(vf_raw), parse_version(vt_raw)
        bucket = _classify(vf, vt, target)
        groups[bucket].append({
            "id": entry.id,
            "label": _heading_label(repo, entry.file, entry.line, entry.id, cache),
            "valid_from": vf_raw,
            "valid_to": vt_raw,
            "invalidated_by": inv,
        })

    for items in groups.values():
        items.sort(key=lambda d: d["id"])
    return {"target": target_raw, "prefixes": sorted(wanted), **groups}


def _trunc(s: str, n: int = 38) -> str:
    return s if len(s) <= n else s[: n - 1] + "…"


def _print_report(result: dict) -> None:
    target = result["target"]
    pfx = ", ".join(result["prefixes"])
    print(f"\n{pfx} decisions authoritative as of {target}")
    print("━" * 64)
    current = result["current"]
    if not current:
        print("  (none in force as of this version)")
    for d in current:
        window = f"{d['valid_from'] or '—'} → {d['valid_to'] or 'current'}"
        print(f"  {d['id']:<10} {_trunc(d['label']):<39} valid {window}")

    if result["superseded"]:
        print("\nsuperseded before this version:")
        for d in result["superseded"]:
            repl = f" → {d['invalidated_by']}" if d["invalidated_by"] else ""
            window = f"{d['valid_from'] or '—'} → {d['valid_to'] or '—'}"
            print(f"  {d['id']:<10} {_trunc(d['label']):<39} valid {window}{repl}")

    if result["future"]:
        print("\nnot yet decided as of this version:")
        for d in result["future"]:
            print(f"  {d['id']:<10} {_trunc(d['label']):<39} (from {d['valid_from'] or '—'})")
    print()


def main() -> int:
    ap = argparse.ArgumentParser(description="Reconstruct decision state as of a PRD version.")
    ap.add_argument("version", help="Target PRD version, e.g. v0.6")
    ap.add_argument("--prefix", default="ARC,TECH",
                    help="Comma-separated ID prefixes to reconstruct (default: ARC,TECH).")
    ap.add_argument("--repo", type=Path, default=None,
                    help="Repo root (default: discovered from cwd).")
    ap.add_argument("--json", action="store_true", help="Emit machine-readable JSON.")
    args = ap.parse_args()

    repo = find_repo_root(args.repo or Path.cwd())
    prefixes = [p.strip() for p in args.prefix.split(",") if p.strip()]
    result = as_of(repo, args.version, prefixes)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        _print_report(result)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
