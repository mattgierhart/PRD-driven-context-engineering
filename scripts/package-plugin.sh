#!/usr/bin/env bash
# package-plugin.sh — Build the distributable `prd-ce` Claude Code plugin from the
# methodology source in `.claude/` (strategy B: `.claude/` stays the single source of
# truth during development; the plugin payload is GENERATED, not hand-duplicated).
#
# Produces plugins/prd-ce/{skills,agents,hooks,scripts} by applying the transforms a
# plugin requires:
#   - skills:  copied as-is (plugin skills/ layout already matches .claude/skills/)
#   - agents:  flattened  .claude/agents/<name>/AGENT.md -> agents/<name>.md
#              (MEMORY.md is product state — NOT shipped)
#   - hooks:   scripts copied; hooks.json generated from .claude/settings.json with
#              $CLAUDE_PROJECT_DIR/.claude/hooks/  ->  ${CLAUDE_PLUGIN_ROOT}/hooks/
#   - scripts: readiness + validators copied (referenced by hooks via ${CLAUDE_PLUGIN_ROOT})
#
# The authored manifests (plugin.json, marketplace.json) are NOT regenerated.
# Re-run anytime; output is deterministic. See temp/plugin-conversion-plan.md.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SRC="$ROOT/.claude"
OUT="$ROOT/plugins/prd-ce"

say() { printf '%s\n' "$*"; }

[ -d "$SRC" ] || { say "✗ source not found: $SRC"; exit 1; }
[ -f "$OUT/.claude-plugin/plugin.json" ] || { say "✗ authored plugin.json missing at $OUT/.claude-plugin/"; exit 1; }

say "▶ Building plugin payload → plugins/prd-ce"

# --- Clean generated payload (never touch the authored .claude-plugin/) ---
for d in skills agents hooks scripts; do rm -rf "${OUT:?}/$d"; done

# --- Skills (layout already matches; copy the tree) ---
mkdir -p "$OUT/skills"
cp -R "$SRC/skills/." "$OUT/skills/"
skill_count=$(find "$OUT/skills" -name SKILL.md | wc -l | tr -d ' ')
say "  skills    : $skill_count SKILL.md"

# --- Agents: flatten <name>/AGENT.md -> <name>.md, drop MEMORY*.md ---
mkdir -p "$OUT/agents"
agent_count=0
for agent_dir in "$SRC"/agents/*/; do
  [ -d "$agent_dir" ] || continue
  name=$(basename "$agent_dir")
  if [ -f "$agent_dir/AGENT.md" ]; then
    cp "$agent_dir/AGENT.md" "$OUT/agents/$name.md"
    agent_count=$((agent_count+1))
  fi
done
say "  agents    : $agent_count flattened (MEMORY.md held back — product state)"

# --- Hooks: copy scripts, then generate hooks.json from settings.json ---
mkdir -p "$OUT/hooks"
cp "$SRC"/hooks/*.sh "$OUT/hooks/" 2>/dev/null || true
# include python helpers some hooks shell out to
cp "$SRC"/hooks/*.py "$OUT/hooks/" 2>/dev/null || true

python3 - "$SRC/settings.json" "$OUT/hooks/hooks.json" <<'PY'
import json, sys
src, dst = sys.argv[1], sys.argv[2]
cfg = json.load(open(src))
hooks = cfg.get("hooks", {})

OLD = '"$CLAUDE_PROJECT_DIR"/.claude/hooks/'
NEW = '"${CLAUDE_PLUGIN_ROOT}"/hooks/'

def rewrite(node):
    if isinstance(node, dict):
        return {k: rewrite(v) for k, v in node.items()}
    if isinstance(node, list):
        return [rewrite(v) for v in node]
    if isinstance(node, str):
        return node.replace(OLD, NEW)
    return node

out = {"hooks": rewrite(hooks)}
json.dump(out, open(dst, "w"), indent=2)
open(dst, "a").write("\n")
print(f"  hooks     : hooks.json ({len(hooks)} events, paths -> ${{CLAUDE_PLUGIN_ROOT}})")
PY

# --- Scripts: methodology logic referenced by hooks/skills ---
mkdir -p "$OUT/scripts"
cp -R "$ROOT/scripts/." "$OUT/scripts/"
# the packager itself does not belong inside the plugin
rm -f "$OUT/scripts/package-plugin.sh"
say "  scripts   : readiness + validators copied"

say ""
say "✔ Plugin built. Verify locally with:"
say "    claude --plugin-dir $OUT"
say "  Generated payload is gitignored (strategy B). Authored: .claude-plugin/{plugin,marketplace}.json"
