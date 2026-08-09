#!/usr/bin/env bash
# install.sh — Source-run install path for the PRD-Driven Context Engineering methodology.
#
# Deterministic source-run installer. Drops the framework (.claude/ hooks + skills + agents +
# rules, plus allowlisted scripts) into a target repo and
# seeds product templates and consumer docs ONCE — without ever clobbering product content. Idempotent:
# re-running updates the framework and leaves product files alone.
#
# Run this file from a trusted methodology source checkout for every install or upgrade. The
# consumer runtime deliberately does not receive another runnable installer or manifest.
#
# Usage:
#   bash install.sh [--target DIR] [--profile PROFILE] [--dry-run] [--force]
#
#   --target DIR     Where to install (default: current directory)
#   --profile NAME   domain-profile.yaml profile: product|library|infrastructure|research
#                    (default: leaves the shipped value)
#   --dry-run        Print planned actions, write nothing
#   --force          Overwrite framework files that have local drift (never product files)
#
# Reads .claude/install-manifest.yaml for the authoritative file lists.
set -euo pipefail

# --- Resolve source (this repo) and parse args ---
SOURCE="$(cd "$(dirname "$0")" && pwd)"
MANIFEST="$SOURCE/.claude/install-manifest.yaml"
TARGET="$(pwd)"
PROFILE=""
DRY_RUN=0
FORCE=0

while [ $# -gt 0 ]; do
  case "$1" in
    --target)  TARGET="$2"; shift 2 ;;
    --profile) PROFILE="$2"; shift 2 ;;
    --dry-run) DRY_RUN=1; shift ;;
    --force)   FORCE=1; shift ;;
    -h|--help) sed -n '2,30p' "$0"; exit 0 ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done

case "$PROFILE" in
  ""|product|library|infrastructure|research) ;;
  *) echo "Unknown profile: $PROFILE" >&2; exit 2 ;;
esac

say()  { printf '%s\n' "$*"; }
plan() { printf '  %-7s %s\n' "$1" "$2"; }   # action, path

# --- Preflight ---
say "▶ Preflight"
for bin in git python3 awk; do
  if ! command -v "$bin" >/dev/null 2>&1; then
    say "  ✗ missing required tool: $bin"; exit 1
  fi
done
if ! python3 -c 'import yaml' >/dev/null 2>&1; then
  say "  ⚠ readiness dependency missing: PyYAML"
  say "    install with: python3 -m pip install -r \"$SOURCE/scripts/requirements.txt\""
fi
[ -f "$MANIFEST" ] || { say "  ✗ manifest not found: $MANIFEST"; exit 1; }
TARGET_INPUT="$TARGET"
if ! python3 - "$TARGET_INPUT" <<'PY'
import os
import stat
import sys

target = os.path.abspath(sys.argv[1])
try:
    mode = os.lstat(target).st_mode
except OSError as exc:
    print(f"  ✗ target directory is unavailable: {exc}", file=sys.stderr)
    raise SystemExit(1)
if stat.S_ISLNK(mode):
    print(f"  ✗ refusing symlink target directory: '{target}'", file=sys.stderr)
    raise SystemExit(1)
if not stat.S_ISDIR(mode):
    print(f"  ✗ target is not a directory: '{target}'", file=sys.stderr)
    raise SystemExit(1)
PY
then
  exit 1
fi
TARGET="$(cd "$TARGET_INPUT" 2>/dev/null && pwd -P || true)"
[ -n "$TARGET" ] || { say "  ✗ target directory does not exist"; exit 1; }
if [ "$(cd "$SOURCE" && pwd)" = "$TARGET" ]; then
  say "  ✗ refusing to install onto the framework repo itself; pick a --target"; exit 1
fi
[ -d "$TARGET/.git" ] || say "  ⚠ target is not a git repo (recommended: 'git init' first)"
MODE="greenfield"; [ -d "$TARGET/.claude" ] && MODE="brownfield"
say "  ✓ tools present · target=$TARGET · mode=$MODE"
[ "$DRY_RUN" -eq 1 ] && say "  (dry-run: no files will be written)"

# --- Manifest parsing: print '- <item>' entries under a top-level section ---
manifest_section() {
  awk -v sec="$1" '
    /^[A-Za-z_]+:/ { inq = ($0 ~ "^" sec ":"); next }
    inq && /^[[:space:]]*-[[:space:]]/ {
      sub(/^[[:space:]]*-[[:space:]]*/, "")
      sub(/[[:space:]]*#.*$/, "")            # strip trailing comment
      sub(/[[:space:]]+$/, "")
      if (length) print
    }
  ' "$MANIFEST"
}

# The manifest's product-ownership boundary is executable, not commentary. Reject any framework
# path that would write a concrete `never_touch` path, including protected paths matched by globs.
if ! python3 - "$MANIFEST" "$SOURCE" "$TARGET" "$FORCE" <<'PY'
import fnmatch
import glob
import hashlib
import json
import os
import posixpath
import re
import stat
import sys

manifest, source, target, force_raw = sys.argv[1:]
force = force_raw == "1"
sections = {
    "framework": [],
    "template_seed": [],
    "direct_exclude": [],
    "never_touch": [],
    "obsolete_framework_scan_roots": [],
    "obsolete_framework_fingerprints": [],
}
current = None
for raw in open(manifest):
    top = re.match(r"^([A-Za-z_]+):\s*$", raw)
    if top:
        current = top.group(1)
        continue
    item = re.match(r"^\s*-\s*(.+?)\s*$", raw)
    if current in sections and item:
        value = re.sub(r"\s+#.*$", "", item.group(1)).strip()
        if value:
            sections[current].append(value)

def safe_relative(path: str) -> bool:
    if not path or os.path.isabs(path) or "\\" in path:
        return False
    normalized = posixpath.normpath(path)
    return normalized == path and normalized not in {"", "."} and ".." not in path.split("/")

def direct_excluded(path: str) -> bool:
    return any(
        path == excluded or path.startswith(excluded.rstrip("/") + "/")
        for excluded in sections["direct_exclude"]
    )

source_entries = [("framework", entry, entry) for entry in sections["framework"]]
for entry in sections["template_seed"]:
    if " -> " in entry:
        src, dst = entry.split(" -> ", 1)
    else:
        src = dst = entry
    source_entries.append(("template_seed", src, dst))

for section in ("direct_exclude", "never_touch"):
    for path in sections[section]:
        if not safe_relative(path):
            print(f"  ✗ unsafe {section} path: '{path}'", file=sys.stderr)
            raise SystemExit(1)

for section, src, dst in source_entries:
    if not safe_relative(src) or not safe_relative(dst):
        print(f"  ✗ unsafe {section} path: '{src}' -> '{dst}'", file=sys.stderr)
        raise SystemExit(1)
    if not os.path.lexists(os.path.join(source, src)):
        print(f"  ✗ missing {section} source: '{src}'", file=sys.stderr)
        raise SystemExit(1)
if ".claude/settings.json" in sections["framework"]:
    merge_helper = os.path.join(source, "scripts", "_merge_settings.py")
    if not os.path.isfile(merge_helper):
        print(f"  ✗ installer dependency not found: '{merge_helper}'", file=sys.stderr)
        raise SystemExit(1)

# Refuse every existing symlink component at or below the target root before any write.
# Framework directories are merged recursively, so checking only their manifest roots would miss
# a consumer symlink at (for example) .claude/hooks/<managed-file> and could write outside target.
destination_entries = []
for section, src, dst in source_entries:
    if section == "framework" and direct_excluded(dst):
        continue
    destination_entries.append((section, dst))
    source_path = os.path.join(source, src)
    if section != "framework" or not os.path.isdir(source_path) or os.path.islink(source_path):
        continue
    for dirpath, dirnames, filenames in os.walk(source_path, followlinks=False):
        for name in dirnames + filenames:
            child_source = os.path.join(dirpath, name)
            child_relative = os.path.relpath(child_source, source).replace(os.sep, "/")
            if direct_excluded(child_relative):
                continue
            child_under_entry = os.path.relpath(child_source, source_path).replace(os.sep, "/")
            destination_entries.append((section, f"{dst.rstrip('/')}/{child_under_entry}"))

requirements = {}
for section, destination in destination_entries:
    current = target
    components = [(current, ".")]
    for part in destination.split("/"):
        current = os.path.join(current, part)
        components.append((current, os.path.relpath(current, target).replace(os.sep, "/")))
    for index, (candidate, relative) in enumerate(components):
        requires_directory = index < len(components) - 1
        requirement = requirements.setdefault(candidate, {
            "relative": relative,
            "section": section,
            "destination": destination,
            "requires_directory": False,
        })
        if requires_directory and not requirement["requires_directory"]:
            requirement.update({
                "section": section,
                "destination": destination,
                "requires_directory": True,
            })

for candidate, requirement in sorted(requirements.items()):
    try:
        mode = os.lstat(candidate).st_mode
    except FileNotFoundError:
        continue
    except OSError as exc:
        print(f"  ✗ cannot inspect target path '{candidate}': {exc}", file=sys.stderr)
        raise SystemExit(1)
    if stat.S_ISLNK(mode):
        print(
            f"  ✗ refusing symlink at target path '{requirement['relative']}' "
            f"for {requirement['section']} destination '{requirement['destination']}'",
            file=sys.stderr,
        )
        raise SystemExit(1)
    if requirement["requires_directory"] and not stat.S_ISDIR(mode):
        print(
            f"  ✗ refusing non-directory target ancestor '{requirement['relative']}' "
            f"for {requirement['section']} destination '{requirement['destination']}'",
            file=sys.stderr,
        )
        raise SystemExit(1)

def validate_settings_schema(value, label: str) -> None:
    if not isinstance(value, dict):
        raise ValueError("top level must be an object")
    hooks = value.get("hooks", {})
    if not isinstance(hooks, dict):
        raise ValueError("hooks must be an object")
    for event, groups in hooks.items():
        if not isinstance(event, str) or not isinstance(groups, list):
            raise ValueError("each hooks event must map to a list of groups")
        for group in groups:
            if (
                not isinstance(group, dict)
                or "hooks" not in group
                or not isinstance(group["hooks"], list)
            ):
                raise ValueError(f"hooks.{event} groups must be objects with a hooks list")
            for handler in group["hooks"]:
                if not isinstance(handler, dict):
                    raise ValueError(f"hooks.{event} handlers must be objects")
                if "type" in handler and not isinstance(handler["type"], str):
                    raise ValueError(f"hooks.{event} handler type must be a string")
                if "command" in handler and not isinstance(handler["command"], str):
                    raise ValueError(f"hooks.{event} handler command must be a string")

loaded_settings = {}
for label, settings_path in (
    ("source", os.path.join(source, ".claude", "settings.json")),
    ("target", os.path.join(target, ".claude", "settings.json")),
):
    if not os.path.lexists(settings_path):
        continue
    if not os.path.isfile(settings_path):
        print(f"  ✗ {label} settings path is not a file: '{settings_path}'", file=sys.stderr)
        raise SystemExit(1)
    try:
        with open(settings_path) as handle:
            settings = json.load(handle)
        validate_settings_schema(settings, label)
        loaded_settings[label] = settings
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"  ✗ invalid {label} settings JSON: {exc}", file=sys.stderr)
        raise SystemExit(1)

if ".claude/settings.json" in sections["framework"]:
    framework_destinations = {
        destination for section, destination in destination_entries if section == "framework"
    }
    hook_destinations = {
        relative
        for groups in loaded_settings["source"].get("hooks", {}).values()
        for group in groups
        for handler in group.get("hooks", [])
        for relative in re.findall(r"\.claude/hooks/[A-Za-z0-9_.-]+", handler.get("command", ""))
    }
    for relative in sorted(hook_destinations):
        if relative not in framework_destinations:
            print(f"  ✗ settings hook is not a managed framework destination: '{relative}'", file=sys.stderr)
            raise SystemExit(1)
        source_hook = os.path.join(source, *relative.split("/"))
        source_mode = os.lstat(source_hook).st_mode
        if not stat.S_ISREG(source_mode):
            print(f"  ✗ source settings hook is not a regular file: '{relative}'", file=sys.stderr)
            raise SystemExit(1)
        target_hook = os.path.join(target, *relative.split("/"))
        try:
            target_mode = os.lstat(target_hook).st_mode
        except FileNotFoundError:
            continue
        if not force and not stat.S_ISREG(target_mode):
            print(
                f"  ✗ framework hook destination is not a file: '{relative}' "
                "(re-run with --force to replace it)",
                file=sys.stderr,
            )
            raise SystemExit(1)

def contains(parent: str, child: str) -> bool:
    return child == parent or child.startswith(parent.rstrip("/") + "/")

overlaps = set()
for protected in sections["never_touch"]:
    concrete = []
    if glob.has_magic(protected):
        concrete = [os.path.relpath(path, source) for path in glob.glob(
            os.path.join(source, protected), recursive=True
        )]
    else:
        concrete = [protected]
    for managed in sections["framework"]:
        if fnmatch.fnmatchcase(managed, protected):
            overlaps.add((managed, protected))
        if glob.has_magic(protected) and os.path.isdir(os.path.join(source, managed)):
            # Also reject a broad framework directory that could contain future protected matches,
            # even when the current source tree has no concrete file matching the glob yet.
            probe = re.sub(r"\[[^]]*\]", "X", protected).replace("*", "X").replace("?", "X")
            if contains(managed, probe):
                overlaps.add((managed, protected))
        for path in concrete:
            if contains(managed, path) or contains(path, managed):
                overlaps.add((managed, protected))

for scan_root in sections["obsolete_framework_scan_roots"]:
    if os.path.isabs(scan_root) or scan_root in {"", "."} or ".." in scan_root.split("/"):
        print(f"  ✗ unsafe obsolete scan root: '{scan_root}'", file=sys.stderr)
        raise SystemExit(1)

fingerprints = sections["obsolete_framework_fingerprints"]
if any(not re.fullmatch(r"[0-9a-f]{64}", value) for value in fingerprints):
    print("  ✗ obsolete framework fingerprints must be lowercase SHA-256", file=sys.stderr)
    raise SystemExit(1)
if len(fingerprints) != len(set(fingerprints)):
    print("  ✗ duplicate obsolete framework fingerprint", file=sys.stderr)
    raise SystemExit(1)

# Known concrete protected paths must never appear in the opaque retirement set.
protected_paths = set()
for protected in sections["never_touch"]:
    if glob.has_magic(protected):
        protected_paths.update(
            os.path.relpath(path, source).replace(os.sep, "/")
            for path in glob.glob(os.path.join(source, protected), recursive=True)
        )
    else:
        protected_paths.add(protected)
protected_hashes = {
    hashlib.sha256(path.encode()).hexdigest(): path for path in protected_paths
}
collisions = set(fingerprints) & set(protected_hashes)
if collisions:
    for digest in sorted(collisions):
        print(
            f"  ✗ obsolete fingerprint intersects protected path "
            f"'{protected_hashes[digest]}'",
            file=sys.stderr,
        )
    raise SystemExit(1)

effective_framework = set()
for managed in sections["framework"]:
    managed_path = os.path.join(source, managed)
    if not direct_excluded(managed):
        effective_framework.add(managed)
    if os.path.isdir(managed_path) and not os.path.islink(managed_path):
        for dirpath, dirnames, filenames in os.walk(managed_path, followlinks=False):
            for name in dirnames + filenames:
                relative = os.path.relpath(os.path.join(dirpath, name), source).replace(os.sep, "/")
                if not direct_excluded(relative):
                    effective_framework.add(relative)
framework_hashes = {
    hashlib.sha256(path.encode()).hexdigest(): path for path in effective_framework
}
collisions = set(fingerprints) & set(framework_hashes)
if collisions:
    for digest in sorted(collisions):
        print(
            f"  ✗ obsolete fingerprint intersects current framework path "
            f"'{framework_hashes[digest]}'",
            file=sys.stderr,
        )
    raise SystemExit(1)
if overlaps:
    for managed, protected in sorted(overlaps):
        print(
            f"  ✗ manifest ownership overlap: managed path '{managed}' "
            f"intersects never_touch '{protected}'",
            file=sys.stderr,
        )
    raise SystemExit(1)
PY
then
  say "  ✗ manifest ownership invariant failed"
  exit 1
fi

copied=0; updated=0; seeded=0; skipped=0; protected=0; profile_seeded=0

# cp helper honoring dry-run; copies file or directory tree
do_copy() {  # src dest
  if [ "$DRY_RUN" -eq 1 ]; then return; fi
  mkdir -p "$(dirname "$2")"
  cp -R "$1" "$2"
}

is_direct_excluded() {  # repository-relative path
  local candidate="$1" pattern
  while IFS= read -r pattern; do
    [ -n "$pattern" ] || continue
    case "$candidate" in
      "$pattern"|"$pattern"/*) return 0 ;;
    esac
  done < <(manifest_section direct_exclude)
  return 1
}

do_framework_copy() {  # manifest rel, src, dest
  if [ "$DRY_RUN" -eq 1 ]; then return; fi
  if [ ! -d "$2" ]; then
    do_copy "$2" "$3"
    return
  fi
  mkdir -p "$3"
  while IFS= read -r child; do
    child="${child#./}"
    full_rel="$1/$child"
    is_direct_excluded "$full_rel" && continue
    if [ -d "$2/$child" ]; then
      mkdir -p "$3/$child"
    elif [ -f "$2/$child" ]; then
      mkdir -p "$(dirname "$3/$child")"
      cp -p "$2/$child" "$3/$child"
    fi
  done < <(cd "$2" && find . -mindepth 1 -print)
}

# Merge a framework directory file-by-file. Missing canonical files are installed on every run;
# consumer additions and locally differing canonical files are preserved unless --force is explicit.
do_framework_merge() {  # manifest rel, src, dest
  local stats
  stats="$(python3 - "$1" "$2" "$3" "$MANIFEST" "$FORCE" "$DRY_RUN" <<'PY'
import filecmp
import os
import re
import shutil
import sys

base, source, target, manifest, force_raw, dry_raw = sys.argv[1:]
force = force_raw == "1"
dry_run = dry_raw == "1"

excluded = []
grab = False
for raw in open(manifest):
    if re.match(r"^direct_exclude:\s*$", raw):
        grab = True
        continue
    if re.match(r"^[A-Za-z_]+:", raw):
        grab = False
    if grab:
        item = re.match(r"^\s*-\s*(.+?)\s*$", raw)
        if item:
            value = re.sub(r"\s+#.*$", "", item.group(1)).strip()
            if value:
                excluded.append(value)

def is_excluded(relative):
    return any(
        relative == item or relative.startswith(item.rstrip("/") + "/")
        for item in excluded
    )

def remove(path):
    if os.path.isdir(path) and not os.path.islink(path):
        shutil.rmtree(path)
    else:
        os.unlink(path)

added = refreshed = drift = 0
for dirpath, dirnames, filenames in os.walk(source, topdown=True, followlinks=False):
    under_source = os.path.relpath(dirpath, source)
    relative_dir = base if under_source == "." else f"{base}/{under_source.replace(os.sep, '/')}"
    if under_source != "." and is_excluded(relative_dir):
        dirnames[:] = []
        continue

    destination_dir = target if under_source == "." else os.path.join(target, under_source)
    if under_source != "." and not os.path.lexists(destination_dir):
        if not dry_run:
            os.mkdir(destination_dir)
    elif under_source != "." and not os.path.isdir(destination_dir):
        if force:
            if not dry_run:
                remove(destination_dir)
                os.mkdir(destination_dir)
            refreshed += 1
        else:
            drift += 1
            dirnames[:] = []
            continue

    retained_dirs = []
    for name in dirnames:
        child_under_source = name if under_source == "." else os.path.join(under_source, name)
        child_relative = f"{base}/{child_under_source.replace(os.sep, '/')}"
        if not is_excluded(child_relative):
            retained_dirs.append(name)
    dirnames[:] = retained_dirs

    for name in filenames:
        child_under_source = name if under_source == "." else os.path.join(under_source, name)
        child_relative = f"{base}/{child_under_source.replace(os.sep, '/')}"
        if is_excluded(child_relative):
            continue
        source_file = os.path.join(source, child_under_source)
        target_file = os.path.join(target, child_under_source)
        if not os.path.lexists(target_file):
            if not dry_run:
                os.makedirs(os.path.dirname(target_file), exist_ok=True)
                shutil.copy2(source_file, target_file)
            added += 1
        elif os.path.isfile(target_file) and filecmp.cmp(source_file, target_file, shallow=False):
            continue
        elif force:
            if not dry_run:
                remove(target_file)
                shutil.copy2(source_file, target_file)
            refreshed += 1
        else:
            drift += 1

print(added, refreshed, drift)
PY
)"
  read -r MERGE_ADDED MERGE_REFRESHED MERGE_DRIFT <<< "$stats"
}

# Update framework-owned paths in place. A directory merge overwrites canonical framework files
# but preserves unrelated consumer additions in the same namespace.
do_framework_update() {  # manifest rel, src, dest
  if [ "$DRY_RUN" -eq 1 ]; then return; fi
  if [ -d "$2" ] && [ -d "$3" ]; then
    do_framework_copy "$1" "$2" "$3"
  else
    rm -rf "$3"
    do_framework_copy "$1" "$2" "$3"
  fi
}

# Compare every canonical source file while deliberately ignoring unrelated destination extras.
# This keeps custom additions from causing perpetual drift after a safe directory merge.
framework_matches() {  # manifest rel, src, dest
  if [ -f "$2" ] && [ -f "$3" ]; then
    diff -q "$2" "$3" >/dev/null 2>&1
    return
  fi
  [ -d "$2" ] && [ -d "$3" ] || return 1
  while IFS= read -r rel_file; do
    rel_file="${rel_file#./}"
    is_direct_excluded "$1/$rel_file" && continue
    [ -f "$3/$rel_file" ] || return 1
    diff -q "$2/$rel_file" "$3/$rel_file" >/dev/null 2>&1 || return 1
  done < <(cd "$2" && find . -type f -print)
}

# Canonical settings reference framework hooks, so defer writing settings until the hook merge is
# complete and its command paths are known to resolve.
# --- Framework: install new, merge directories, update drift on --force ---
say "▶ Framework"
SETTINGS_MANAGED=0
while IFS= read -r rel; do
  [ -n "$rel" ] || continue
  is_direct_excluded "$rel" && continue
  src="$SOURCE/$rel"; dst="$TARGET/$rel"
  [ -e "$src" ] || { plan "miss" "$rel (not in source — skipped)"; continue; }

  if [ "$rel" = ".claude/settings.json" ]; then
    SETTINGS_MANAGED=1
    continue
  fi

  if [ ! -e "$dst" ]; then
    plan "new" "$rel"; do_framework_copy "$rel" "$src" "$dst"; copied=$((copied+1))
  elif [ -d "$src" ] && [ -d "$dst" ]; then
    do_framework_merge "$rel" "$src" "$dst"
    if [ "$MERGE_ADDED" -gt 0 ] || [ "$MERGE_REFRESHED" -gt 0 ]; then
      plan "merge" "$rel ($MERGE_ADDED missing added, $MERGE_REFRESHED refreshed)"
    fi
    if [ "$MERGE_DRIFT" -gt 0 ]; then
      plan "drift" "$rel ($MERGE_DRIFT differing canonical path(s) preserved)"
    fi
    copied=$((copied+MERGE_ADDED))
    updated=$((updated+MERGE_REFRESHED))
    skipped=$((skipped+MERGE_DRIFT))
  elif framework_matches "$rel" "$src" "$dst"; then
    skipped=$((skipped+1))   # identical — silent
  elif [ "$FORCE" -eq 1 ]; then
    plan "update" "$rel"
    do_framework_update "$rel" "$src" "$dst"; updated=$((updated+1))
  else
    plan "drift" "$rel (differs — re-run with --force to update)"; skipped=$((skipped+1))
  fi
done < <(manifest_section framework)

if [ "$SETTINGS_MANAGED" -eq 1 ]; then
  settings_src="$SOURCE/.claude/settings.json"
  settings_dst="$TARGET/.claude/settings.json"
  if [ "$DRY_RUN" -eq 0 ]; then
    if ! python3 - "$settings_src" "$TARGET" <<'PY'
import json
import os
import re
import stat
import sys

settings_path, target = sys.argv[1:]
settings = json.load(open(settings_path))
missing = set()
for groups in settings.get("hooks", {}).values():
    for group in groups:
        for handler in group.get("hooks", []):
            command = handler.get("command", "")
            for relative in re.findall(r"\.claude/hooks/[A-Za-z0-9_.-]+", command):
                destination = os.path.join(target, *relative.split("/"))
                try:
                    mode = os.lstat(destination).st_mode
                except OSError:
                    missing.add(relative)
                    continue
                if not stat.S_ISREG(mode):
                    missing.add(relative)
if missing:
    for relative in sorted(missing):
        print(f"  ✗ settings hook destination is absent or not a file: '{relative}'", file=sys.stderr)
    raise SystemExit(1)
PY
    then
      say "  ✗ refusing to write settings with unresolved framework hooks"
      exit 1
    fi
  fi
  if [ ! -f "$settings_dst" ]; then
    plan "new" ".claude/settings.json"
    do_copy "$settings_src" "$settings_dst"
    copied=$((copied+1))
  else
    plan "merge" ".claude/settings.json (hooks unioned, permissions preserved)"
    if [ "$DRY_RUN" -eq 0 ]; then
      python3 "$SOURCE/scripts/_merge_settings.py" "$settings_src" "$settings_dst"
    fi
    updated=$((updated+1))
  fi
fi

# --- Retired framework paths: opaque exact tombstones, removed only on approved --force upgrades ---
say "▶ Retired framework paths"
while IFS= read -r rel; do
  [ -n "$rel" ] || continue
  dst="$TARGET/$rel"
  [ -e "$dst" ] || continue
  if [ "$FORCE" -eq 1 ]; then
    plan "retire" "$rel"
    if [ "$DRY_RUN" -eq 0 ]; then rm -rf "$dst"; fi
    updated=$((updated+1))
  else
    plan "retired" "$rel (present — re-run with --force to remove)"
    skipped=$((skipped+1))
  fi
done < <(python3 - "$TARGET" "$MANIFEST" <<'PY'
import hashlib
import os
import re
import sys

target, manifest = sys.argv[1:]
sections = {
    "obsolete_framework_scan_roots": [],
    "obsolete_framework_fingerprints": [],
}
current = None
for raw in open(manifest):
    top = re.match(r"^([A-Za-z_]+):\s*$", raw)
    if top:
        current = top.group(1)
        continue
    item = re.match(r"^\s*-\s*(.+?)\s*$", raw)
    if current in sections and item:
        value = re.sub(r"\s+#.*$", "", item.group(1)).strip()
        if value:
            sections[current].append(value)

fingerprints = set(sections["obsolete_framework_fingerprints"])
matches = set()
for relative_root in sections["obsolete_framework_scan_roots"]:
    scan_root = os.path.join(target, relative_root)
    if not os.path.lexists(scan_root):
        continue
    candidates = [scan_root]
    if os.path.isdir(scan_root) and not os.path.islink(scan_root):
        for dirpath, dirnames, filenames in os.walk(scan_root, followlinks=False):
            candidates.extend(os.path.join(dirpath, name) for name in dirnames)
            candidates.extend(os.path.join(dirpath, name) for name in filenames)
    for candidate in candidates:
        relative = os.path.relpath(candidate, target).replace(os.sep, "/")
        digest = hashlib.sha256(relative.encode()).hexdigest()
        if digest in fingerprints:
            matches.add(relative)

for relative in sorted(matches, key=lambda value: (value.count("/"), value), reverse=True):
    print(relative)
PY
)

# --- Template seed: copy ONCE, never overwrite ---
say "▶ Template seed (once)"
while IFS= read -r line; do
  [ -n "$line" ] || continue
  if printf '%s' "$line" | grep -q ' -> '; then
    rel_src="${line%% -> *}"; rel_dst="${line##* -> }"
  else
    rel_src="$line"; rel_dst="$line"
  fi
  src="$SOURCE/$rel_src"; dst="$TARGET/$rel_dst"
  [ -e "$src" ] || { plan "miss" "$rel_src (not in source)"; continue; }
  if [ -e "$dst" ]; then
    plan "keep" "$rel_dst (already present — product-owned)"; protected=$((protected+1))
  else
    plan "seed" "$rel_dst"; do_copy "$src" "$dst"; seeded=$((seeded+1))
    [ "$rel_dst" = ".claude/domain-profile.yaml" ] && profile_seeded=1
  fi
done < <(manifest_section template_seed)

# --- Apply profile + stamp version ---
if [ -n "$PROFILE" ]; then
  if [ "$profile_seeded" -eq 1 ]; then
    if [ "$DRY_RUN" -eq 1 ]; then
      say "▶ Profile would be set on the new seed: $PROFILE"
    else
      python3 - "$TARGET/.claude/domain-profile.yaml" "$PROFILE" <<'PY'
import re, sys
path, profile = sys.argv[1], sys.argv[2]
s = open(path).read()
s = re.sub(r'(?m)^profile:.*$', f'profile: {profile}', s, count=1)
open(path, 'w').write(s)
PY
      say "▶ Profile set on new seed: $PROFILE"
    fi
  else
    say "  ⚠ profile '$PROFILE' not applied; existing domain-profile.yaml is consumer-owned"
  fi
fi

# --- Summary ---
say ""
suffix=""; [ "$DRY_RUN" -eq 1 ] && suffix=", dry-run"
say "✔ Install summary ($MODE$suffix)"
say "    new=$copied  updated=$updated  seeded=$seeded  unchanged=$skipped  protected=$protected"
say ""
say "Next steps in $TARGET:"
say "  1. Open the repo in Claude Code (SessionStart hook loads the read order)."
say "  2. Customize README.md (your product dashboard) and PRD.md v0.1."
say "  3. Start the lifecycle:  \"Let's frame the problem\"  → prd-v01-problem-framing"
say "  4. Install dependencies:  python3 -m pip install -r scripts/requirements.txt"
say "  5. Verify the engine:      python3 scripts/readiness.py run"
