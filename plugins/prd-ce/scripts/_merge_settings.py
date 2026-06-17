#!/usr/bin/env python3
"""Merge framework hooks from a source settings.json into a target settings.json.

Used by install.sh on brownfield installs so an existing repo keeps its own hooks
and permissions while gaining the methodology's hook wiring. Non-destructive:

  - For each hook EVENT (SessionStart, PreToolUse, ...), our matcher-groups are
    appended only if an identical command isn't already wired for that event.
  - The target's existing `permissions` and any extra keys are preserved.

Usage: _merge_settings.py <source_settings.json> <target_settings.json>
"""
import json
import sys


def commands_in(event_groups):
    """All hook command strings already present for an event."""
    cmds = set()
    for group in event_groups or []:
        for h in group.get("hooks", []):
            if "command" in h:
                cmds.add(h["command"])
    return cmds


def main():
    src_path, dst_path = sys.argv[1], sys.argv[2]
    src = json.load(open(src_path))
    dst = json.load(open(dst_path))

    src_hooks = src.get("hooks", {})
    dst_hooks = dst.setdefault("hooks", {})

    added = 0
    for event, groups in src_hooks.items():
        existing = dst_hooks.setdefault(event, [])
        present = commands_in(existing)
        for group in groups:
            new_cmds = [h.get("command") for h in group.get("hooks", [])]
            # Skip groups whose commands are all already wired for this event.
            if new_cmds and all(c in present for c in new_cmds):
                continue
            existing.append(group)
            added += len(new_cmds)

    # Ensure a permissions block exists without overwriting the target's.
    dst.setdefault("permissions", src.get("permissions", {"allow": []}))

    json.dump(dst, open(dst_path, "w"), indent=2)
    open(dst_path, "a").write("\n")
    print(f"    merged {added} hook command(s) into {dst_path}")


if __name__ == "__main__":
    main()
