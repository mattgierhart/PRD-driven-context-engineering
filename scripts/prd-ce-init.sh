#!/usr/bin/env bash
# prd-ce-init.sh — Seed the consumer-owned scaffold for a greenfield PRD-CE repo.
#
# Plugin-native seeder. When prd-ce is installed as a Claude Code plugin, the framework
# (skills / agents / hooks / scripts) is provided LIVE by the plugin runtime — it is not
# copied into the consumer repo. This script plants only the files the plugin cannot carry
# as behavior: the consumer's own PRD.md, SoT/, EPIC templates, domain-profile.yaml, the
# four agent MEMORY.md starters, and an optional human CLAUDE.md stub.
#
# Properties:
#   - Idempotent + non-destructive — never overwrites an existing file (honors never_touch).
#   - Manifest-driven — reads `template_seed` from install-manifest.yaml, so it can't drift
#     from install.sh / ghm-template-sync (single source for "what gets seeded").
#   - PRD frontmatter reset — a freshly seeded PRD.md is reset to a clean v0.1 state.
#   - Layout-aware — resolves its template bundle under ${CLAUDE_PLUGIN_ROOT}/templates when
#     running as an installed plugin, else falls back to the repo source tree (dogfood/dev).
#
# Usage: bash prd-ce-init.sh [--target DIR] [--dry-run]
set -euo pipefail

TARGET="$PWD"
DRY=0
while [ $# -gt 0 ]; do
  case "$1" in
    --target) TARGET="$2"; shift 2 ;;
    --dry-run) DRY=1; shift ;;
    -h|--help) grep -E '^# ' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) echo "✗ unknown arg: $1" >&2; exit 2 ;;
  esac
done
TARGET="$(cd "$TARGET" && pwd)"

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

# Reset a freshly seeded PRD.md frontmatter to a clean v0.1 state.
reset_prd_frontmatter() {
  local f="$1"
  [ -f "$f" ] || return 0
  [ "$DRY" -eq 0 ] || { say "  would reset : PRD.md frontmatter -> v0.1, today, drop template_version"; return 0; }
  python3 - "$f" <<'PY'
import sys, re, datetime
f = sys.argv[1]
s = open(f).read()
if s.startswith('---'):
    end = s.find('\n---', 3)
    if end != -1:
        fm, rest = s[:end], s[end:]
        fm = re.sub(r'(?m)^version:.*$',          'version: 0.1', fm)
        fm = re.sub(r'(?m)^last_updated:.*$',      'last_updated: %s' % datetime.date.today().isoformat(), fm)
        fm = re.sub(r'(?m)^template_version:.*\n', '', fm)   # stale template marker → drop
        open(f, 'w').write(fm + rest)
PY
  say "  reset      : PRD.md frontmatter -> v0.1"
}

# --- Run --------------------------------------------------------------------------------
say "▶ prd-ce:init — seeding greenfield scaffold"
say "  target    : $TARGET"
say "  templates : $TPL"
[ "$DRY" -eq 1 ] && say "  (dry-run — no files written)"

prd_was_seeded=0
while IFS= read -r entry; do
  [ -n "$entry" ] || continue
  src="${entry%%->*}"; src="${src%"${src##*[![:space:]]}"}"; src="${src#"${src%%[![:space:]]*}"}"
  if [[ "$entry" == *"->"* ]]; then
    dest="${entry##*->}"; dest="${dest#"${dest%%[![:space:]]*}"}"; dest="${dest%"${dest##*[![:space:]]}"}"
  else
    dest="$src"
  fi
  if seed_one "$TPL/$src" "$TARGET/$dest"; then
    [ "$dest" = "PRD.md" ] && prd_was_seeded=1
  fi
done < <(parse_section template_seed)

# domain-profile.yaml is framework-class in fork mode, but consumer-owned config in plugin
# mode (skills read the CONSUMER's copy) — so init seeds it too when absent.
seed_one "$TPL/.claude/domain-profile.yaml" "$TARGET/.claude/domain-profile.yaml" || true

[ "$prd_was_seeded" -eq 1 ] && reset_prd_frontmatter "$TARGET/PRD.md"

say "✔ init complete — next: customize README.md + PRD.md, then \"frame the problem\" (v0.1)"
