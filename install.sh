#!/usr/bin/env bash
# install.sh — Self-install path for the PRD-Driven Context Engineering methodology.
#
# Deterministic CLI fallback for the `ghm-self-install` skill. Drops the framework
# (.claude/ hooks + skills + agents + rules, scripts/, docs/) into a target repo and
# seeds product templates ONCE — without ever clobbering product content. Idempotent:
# re-running updates the framework and leaves product files alone.
#
# This is the "blueprint, not a binary" pattern: the methodology installs from plain
# files, so it runs entirely inside your Claude Code subscription — no API key, no
# metered calls, no service to stand up.
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

say()  { printf '%s\n' "$*"; }
plan() { printf '  %-7s %s\n' "$1" "$2"; }   # action, path

# --- Preflight (Xantham Q0 analog) ---
say "▶ Preflight"
for bin in git python3 awk; do
  if ! command -v "$bin" >/dev/null 2>&1; then
    say "  ✗ missing required tool: $bin"; exit 1
  fi
done
[ -f "$MANIFEST" ] || { say "  ✗ manifest not found: $MANIFEST"; exit 1; }
TARGET="$(cd "$TARGET" 2>/dev/null && pwd || true)"
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

copied=0; updated=0; seeded=0; skipped=0; protected=0

# cp helper honoring dry-run; copies file or directory tree
do_copy() {  # src dest
  if [ "$DRY_RUN" -eq 1 ]; then return; fi
  mkdir -p "$(dirname "$2")"
  cp -R "$1" "$2"
}

# --- Framework: install new, update on --force, merge settings.json ---
say "▶ Framework"
while IFS= read -r rel; do
  [ -n "$rel" ] || continue
  src="$SOURCE/$rel"; dst="$TARGET/$rel"
  [ -e "$src" ] || { plan "miss" "$rel (not in source — skipped)"; continue; }

  if [ "$rel" = ".claude/settings.json" ]; then
    if [ ! -f "$dst" ]; then
      plan "new" "$rel"; do_copy "$src" "$dst"; copied=$((copied+1))
    else
      plan "merge" "$rel (hooks unioned, permissions preserved)"
      if [ "$DRY_RUN" -eq 0 ]; then
        python3 "$SOURCE/scripts/_merge_settings.py" "$src" "$dst"
      fi
      updated=$((updated+1))
    fi
    continue
  fi

  if [ ! -e "$dst" ]; then
    plan "new" "$rel"; do_copy "$src" "$dst"; copied=$((copied+1))
  elif diff -rq "$src" "$dst" >/dev/null 2>&1; then
    skipped=$((skipped+1))   # identical — silent
  elif [ "$FORCE" -eq 1 ]; then
    plan "update" "$rel"
    [ "$DRY_RUN" -eq 0 ] && rm -rf "$dst"
    do_copy "$src" "$dst"; updated=$((updated+1))
  else
    plan "drift" "$rel (differs — re-run with --force to update)"; skipped=$((skipped+1))
  fi
done < <(manifest_section framework)

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
  fi
done < <(manifest_section template_seed)

# --- Apply profile + stamp version ---
if [ -n "$PROFILE" ] && [ "$DRY_RUN" -eq 0 ] && [ -f "$TARGET/.claude/domain-profile.yaml" ]; then
  case "$PROFILE" in
    product|library|infrastructure|research)
      python3 - "$TARGET/.claude/domain-profile.yaml" "$PROFILE" <<'PY'
import re, sys
path, profile = sys.argv[1], sys.argv[2]
s = open(path).read()
s = re.sub(r'(?m)^profile:.*$', f'profile: {profile}', s, count=1)
open(path, 'w').write(s)
PY
      say "▶ Profile set to: $PROFILE" ;;
    *) say "  ⚠ unknown profile '$PROFILE' — left unchanged" ;;
  esac
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
say "  4. Verify the engine:    python scripts/readiness.py run"
