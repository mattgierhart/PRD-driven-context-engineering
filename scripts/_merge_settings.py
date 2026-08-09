#!/usr/bin/env python3
"""Merge framework hooks from a source settings.json into a target settings.json.

Used by install.sh on brownfield installs so an existing repo keeps its own hooks
and permissions while gaining the methodology's hook wiring. Non-destructive:

  - For each hook EVENT (SessionStart, PreToolUse, ...), framework command groups
    are refreshed from source by exact command identity.
  - The target's existing `permissions` and any extra keys are preserved.

Usage: _merge_settings.py <source_settings.json> <target_settings.json>
"""
import json
import sys


RETIRED_COMMANDS = {
    'bash "$CLAUDE_PROJECT_DIR"/.claude/hooks/sot-update-trigger.sh',
}


def remove_exact_commands(hooks, commands, *, event_name=None):
    """Remove only handlers whose stripped command exactly matches ``commands``.

    Custom commands and other handlers sharing the same event are preserved.
    """
    removed = 0
    events = [event_name] if event_name is not None else list(hooks)
    for event in events:
        kept_groups = []
        for group in hooks.get(event) or []:
            handlers = []
            for handler in group.get("hooks", []):
                command = handler.get("command", "")
                if isinstance(command, str) and command.strip() in commands:
                    removed += 1
                else:
                    handlers.append(handler)
            if handlers:
                kept = dict(group)
                kept["hooks"] = handlers
                kept_groups.append(kept)
        if kept_groups:
            hooks[event] = kept_groups
        else:
            hooks.pop(event, None)
    return removed


def source_commands(groups):
    """Exact command identities owned by one current framework event."""
    return {
        handler["command"].strip()
        for group in groups or []
        for handler in group.get("hooks", [])
        if isinstance(handler.get("command"), str) and handler["command"].strip()
    }


def main():
    src_path, dst_path = sys.argv[1], sys.argv[2]
    src = json.load(open(src_path))
    dst = json.load(open(dst_path))

    src_hooks = src.get("hooks", {})
    dst_hooks = dst.setdefault("hooks", {})
    removed = remove_exact_commands(dst_hooks, RETIRED_COMMANDS)
    refreshed = sum(
        remove_exact_commands(
            dst_hooks,
            source_commands(groups),
            event_name=event,
        )
        for event, groups in src_hooks.items()
    )

    added = 0
    for event, groups in src_hooks.items():
        existing = dst_hooks.setdefault(event, [])
        for group in groups:
            if group not in existing:
                existing.append(group)
                added += len(group.get("hooks", []))

    # Ensure a permissions block exists without overwriting the target's.
    dst.setdefault("permissions", src.get("permissions", {"allow": []}))

    json.dump(dst, open(dst_path, "w"), indent=2)
    open(dst_path, "a").write("\n")
    print(
        f"    merged {added} hook command(s), removed {removed} retired framework "
        f"command(s), refreshed {refreshed} framework command(s) in {dst_path}"
    )


if __name__ == "__main__":
    main()
