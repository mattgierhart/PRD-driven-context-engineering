#!/usr/bin/env python3
"""Append an entry to .ghm/memory.jsonl with Gear Heart metadata."""
from __future__ import annotations

import argparse
import json
import os
import re
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, List

MEMORY_PATH = Path(".ghm/memory.jsonl")
ID_PATTERN = re.compile(r"^mem-(\d{4,})$")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Append a GHM memory entry")
    parser.add_argument("--summary", required=True, help="Short markdown summary using Decision/Problem/etc.")
    parser.add_argument("--epic", required=True, help="EPIC id the decision belongs to")
    parser.add_argument("--task", required=True, help="TASK-### id (mirrors GitHub issue)")
    parser.add_argument("--github-issue", dest="github_issue", default="", help="Issue URL if available")
    parser.add_argument("--type", dest="entry_type", default="decision",
                        help="decision | pattern | lesson | gate_passed | blocker")
    parser.add_argument("--ids", action="append", default=[], help="Related SoT IDs (BR-/API-/TEST-)")
    parser.add_argument("--tags", action="append", default=[], help="Extra taxonomy tags (repeat) ")
    return parser.parse_args()


def _split(values: Iterable[str]) -> List[str]:
    seen = []
    for raw in values:
        if not raw:
            continue
        for token in str(raw).replace(",", " ").split():
            token = token.strip()
            if token and token not in seen:
                seen.append(token)
    return seen


def _utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _next_id(path: Path) -> str:
    max_n = 0
    if path.exists():
        for line in path.read_text().splitlines():
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except json.JSONDecodeError:
                continue
            raw_id = obj.get("id", "")
            match = ID_PATTERN.match(raw_id)
            if match:
                max_n = max(max_n, int(match.group(1)))
    return f"mem-{max_n + 1:04d}"


def append_entry(args: argparse.Namespace) -> None:
    MEMORY_PATH.parent.mkdir(parents=True, exist_ok=True)
    entry = {
        "id": _next_id(MEMORY_PATH),
        "timestamp": _utc_now(),
        "summary": args.summary.strip(),
        "epic": args.epic,
        "task": args.task,
        "github_issue": args.github_issue or "",
        "type": args.entry_type,
        "ids": _split(args.ids),
        "tags": _split(args.tags),
    }
    with MEMORY_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=False) + "\n")
    print(f"Appended {entry['id']} for {entry['task']} → {MEMORY_PATH}")


def main() -> None:
    args = parse_args()
    append_entry(args)


if __name__ == "__main__":
    main()
