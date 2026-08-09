#!/usr/bin/env bash
# prd-ce-init.sh — Seed the consumer-owned scaffold for a greenfield PRD-CE repo.
#
# Plugin-native seeder. When prd-ce is installed as a Claude Code plugin, the framework
# (skills / agents / hooks / scripts) is provided LIVE by the plugin runtime — it is not
# copied into the consumer repo. This script plants only the files the plugin cannot carry
# as behavior: the consumer's own PRD.md, SoT/, EPIC templates, domain-profile.yaml, the
# four agent MEMORY.md starters, and the allowlisted consumer docs those seeds reference.
#
# Properties:
#   - Idempotent + non-destructive — never overwrites an existing file (honors never_touch).
#   - Manifest-driven — reads `template_seed` from install-manifest.yaml, so it can't drift
#     from install.sh (single source for "what gets seeded").
#   - Deterministic seeds — direct and plugin installs copy the same bytes from explicit templates.
#   - Layout-aware — resolves its template bundle under ${CLAUDE_PLUGIN_ROOT}/templates when
#     running as an installed plugin, else falls back to the repo source tree (dogfood/dev).
#
# Usage: bash prd-ce-init.sh [--target DIR] [--profile PROFILE] [--dry-run]
set -euo pipefail

TARGET="$PWD"
DRY=0
PROFILE=""
RUNTIME_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
while [ $# -gt 0 ]; do
  case "$1" in
    --target) TARGET="$2"; shift 2 ;;
    --profile) PROFILE="$2"; shift 2 ;;
    --dry-run) DRY=1; shift ;;
    -h|--help) grep -E '^# ' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "✗ unknown arg: $1" >&2; exit 2 ;;
  esac
done

case "$PROFILE" in
  ""|product|library|infrastructure|research) ;;
  *) echo "✗ unknown profile: $PROFILE; no files were seeded" >&2; exit 2 ;;
esac
TARGET_INPUT="$TARGET"

# --- Resolve the template bundle root (plugin install vs in-repo dogfood) ---------------
# In both modes, template_seed source paths resolve as "$TPL/<src>": the packager mirrors
# the repo-relative src paths under templates/, and the dogfood repo already has them there.
if [ -n "${CLAUDE_PLUGIN_ROOT:-}" ] && [ -d "${CLAUDE_PLUGIN_ROOT}/templates" ]; then
  TPL="${CLAUDE_PLUGIN_ROOT}/templates"
else
  TPL="$(cd "$(dirname "$0")/.." && pwd)"   # repo root, two up from scripts/
fi

MANIFEST="$TPL/.claude/install-manifest.yaml"
[ -f "$MANIFEST" ] || MANIFEST="$TPL/install-manifest.yaml"
[ -f "$MANIFEST" ] || { echo "✗ install-manifest.yaml not found under $TPL" >&2; exit 1; }

for bin in python3 awk; do
  if ! command -v "$bin" >/dev/null 2>&1; then
    echo "✗ $bin is required; no files were seeded" >&2
    exit 1
  fi
done
if ! python3 -c 'import yaml' >/dev/null 2>&1; then
  echo "  ⚠ readiness dependency missing: PyYAML" >&2
  echo "    install with: python3 -m pip install -r \"$RUNTIME_ROOT/scripts/requirements.txt\"" >&2
fi

# Resolve and validate the complete seed write-set before the first mkdir/cp. A destination may be
# absent, but every existing ancestor below the target root must be a real directory and no
# destination component may be a symlink.
if ! TARGET="$(python3 - "$MANIFEST" "$TPL" "$TARGET_INPUT" <<'PY'
import os
import posixpath
import re
import stat
import sys

manifest, templates, target_input = sys.argv[1:]
target_input = os.path.abspath(target_input)
try:
    target_mode = os.lstat(target_input).st_mode
except OSError as exc:
    print(f"✗ target directory is unavailable: {exc}; no files were seeded", file=sys.stderr)
    raise SystemExit(1)
if stat.S_ISLNK(target_mode):
    print(f"✗ refusing symlink target directory: '{target_input}'; no files were seeded", file=sys.stderr)
    raise SystemExit(1)
if not stat.S_ISDIR(target_mode):
    print(f"✗ target is not a directory: '{target_input}'; no files were seeded", file=sys.stderr)
    raise SystemExit(1)

target = os.path.realpath(target_input)
seeds = []
current = None
for raw in open(manifest):
    top = re.match(r"^([A-Za-z_]+):\s*$", raw)
    if top:
        current = top.group(1)
        continue
    item = re.match(r"^\s*-\s*(.+?)\s*$", raw)
    if current == "template_seed" and item:
        value = re.sub(r"\s+#.*$", "", item.group(1)).strip()
        if value:
            seeds.append(value)

destinations = []
def safe_relative(relative):
    if not relative or os.path.isabs(relative) or "\\" in relative:
        return False
    normalized = posixpath.normpath(relative)
    return normalized == relative and normalized not in {"", "."} and ".." not in relative.split("/")

for entry in seeds:
    if " -> " in entry:
        source, destination = entry.split(" -> ", 1)
    else:
        source = destination = entry
    for label, relative in (("source", source), ("destination", destination)):
        if not safe_relative(relative):
            print(f"✗ unsafe template seed {label}: '{relative}'; no files were seeded", file=sys.stderr)
            raise SystemExit(1)
    destinations.append(("template_seed", destination))

# This plugin-only consumer guide is intentionally outside template_seed, so include it explicitly
# in the same all-or-nothing destination preflight.
destinations.append(("plugin guide", "CLAUDE.md"))

requirements = {}
for label, destination in destinations:
    current_path = target
    components = [(current_path, ".")]
    for part in destination.split("/"):
        current_path = os.path.join(current_path, part)
        components.append(
            (current_path, os.path.relpath(current_path, target).replace(os.sep, "/"))
        )
    for index, (candidate, relative) in enumerate(components):
        requires_directory = index < len(components) - 1
        requirement = requirements.setdefault(candidate, {
            "relative": relative,
            "label": label,
            "destination": destination,
            "requires_directory": False,
        })
        if requires_directory and not requirement["requires_directory"]:
            requirement.update({
                "label": label,
                "destination": destination,
                "requires_directory": True,
            })

for candidate, requirement in sorted(requirements.items()):
    try:
        mode = os.lstat(candidate).st_mode
    except FileNotFoundError:
        continue
    except OSError as exc:
        print(f"✗ cannot inspect target path '{candidate}': {exc}; no files were seeded", file=sys.stderr)
        raise SystemExit(1)
    if stat.S_ISLNK(mode):
        print(
            f"✗ refusing symlink at target path '{requirement['relative']}' "
            f"for {requirement['label']} destination '{requirement['destination']}'; "
            "no files were seeded",
            file=sys.stderr,
        )
        raise SystemExit(1)
    if requirement["requires_directory"] and not stat.S_ISDIR(mode):
        print(
            f"✗ refusing non-directory target ancestor '{requirement['relative']}' "
            f"for {requirement['label']} destination '{requirement['destination']}'; "
            "no files were seeded",
            file=sys.stderr,
        )
        raise SystemExit(1)

print(target)
PY
)"; then
  exit 1
fi

say()  { printf '%s\n' "$*"; }
act()  { [ "$DRY" -eq 1 ] && printf '  would seed : %s\n' "$1" || printf '  seeded     : %s\n' "$1"; }
skip() { printf '  exists, keep: %s\n' "$1"; }

# Extract a flat list section ("- item" lines) from the manifest, stripping inline comments.
parse_section() {
  awk -v sec="$1:" '
    $0 ~ "^"sec"[[:space:]]*$" { grab=1; next }
    /^[A-Za-z_]+:/             { grab=0 }
    grab && /^[[:space:]]*-/ {
      sub(/^[[:space:]]*-[[:space:]]*/, "")
      sub(/[[:space:]]*#.*/, "")
      gsub(/[[:space:]]+$/, "")
      if (length) print
    }
  ' "$MANIFEST"
}

# Copy one seed source -> dest, never clobbering an existing dest. Handles files and dirs.
seed_one() {
  local src="$1" dest="$2"
  if [ ! -e "$src" ]; then
    say "  ⚠ missing src: ${src#$TPL/} (skipped)"
    return
  fi
  if [ -e "$dest" ]; then
    skip "${dest#$TARGET/}"
    return 1   # signal: already present (so callers don't post-process)
  fi
  if [ "$DRY" -eq 0 ]; then
    mkdir -p "$(dirname "$dest")"
    cp -R "$src" "$dest"
  fi
  act "${dest#$TARGET/}"
  return 0
}

# --- Run --------------------------------------------------------------------------------
say "▶ prd-ce:init — seeding greenfield scaffold"
say "  target    : $TARGET"
say "  templates : $TPL"
[ "$DRY" -eq 1 ] && say "  (dry-run — no files written)"

profile_seeded=0

while IFS= read -r entry; do
  [ -n "$entry" ] || continue
  src="${entry%%->*}"; src="${src%"${src##*[![:space:]]}"}"; src="${src#"${src%%[![:space:]]*}"}"
  if [[ "$entry" == *"->"* ]]; then
    dest="${entry##*->}"; dest="${dest#"${dest%%[![:space:]]*}"}"; dest="${dest%"${dest##*[![:space:]]}"}"
  else
    dest="$src"
  fi
  if seed_one "$TPL/$src" "$TARGET/$dest"; then
    [ "$dest" = ".claude/domain-profile.yaml" ] && profile_seeded=1
  fi
done < <(parse_section template_seed)

if [ -n "$PROFILE" ]; then
  if [ "$profile_seeded" -eq 1 ]; then
    if [ "$DRY" -eq 1 ]; then
      say "  would set  : .claude/domain-profile.yaml profile=$PROFILE"
    else
      python3 - "$TARGET/.claude/domain-profile.yaml" "$PROFILE" <<'PY'
import re
import sys

path, profile = sys.argv[1:]
text = open(path).read()
text = re.sub(r"(?m)^profile:.*$", f"profile: {profile}", text, count=1)
open(path, "w").write(text)
PY
      say "  profile set: $PROFILE (new seed only)"
    fi
  else
    say "  ⚠ profile '$PROFILE' not applied; existing domain-profile.yaml is consumer-owned"
  fi
fi

# README_template links a local CLAUDE.md. In plugin mode behavior stays live, while this small
# consumer guide makes the authority chain and local links explicit without copying the framework.
seed_one "$TPL/CLAUDE_plugin_stub.md" "$TARGET/CLAUDE.md" || true

say "✔ init complete — next: customize README.md + PRD.md, then \"frame the problem\" (v0.1)"
