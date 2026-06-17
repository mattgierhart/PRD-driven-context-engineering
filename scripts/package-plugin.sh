#!/usr/bin/env bash
# package-plugin.sh — Build the distributable `prd-ce` plugin payload from .claude/ source.
#
# Strategy B (de-risked): .claude/ stays the single source of truth during development;
# this deterministic transform generates plugins/prd-ce/{skills,agents,hooks,scripts} from it.
# The generated payload is gitignored until the strategy-A cutover (when the plugin becomes
# the source and the repo dogfoods it). See temp/plugin-conversion-plan.md.
#
# Transforms applied:
#   - skills/   : copied as-is (.claude/skills/<name>/SKILL.md shape already matches plugins)
#   - agents/   : FLATTENED .claude/agents/<name>/AGENT.md -> agents/<name>.md (MEMORY.md NOT shipped)
#   - hooks/    : scripts copied; hooks.json generated from .claude/settings.json with hook
#                 command paths rewritten $CLAUDE_PROJECT_DIR/.claude/hooks -> ${CLAUDE_PLUGIN_ROOT}/hooks
#   - scripts/  : methodology scripts (readiness, validators) copied for hooks to call via PLUGIN_ROOT
#
# Usage: bash scripts/package-plugin.sh   (run from repo root)
set -euo pipefail

SRC="$(cd "$(dirname "$0")/.." && pwd)"
OUT="$SRC/plugins/prd-ce"
say() { printf '%s\n' "$*"; }

[ -d "$SRC/.claude" ] || { say "✗ no .claude/ source at $SRC"; exit 1; }
[ -f "$OUT/.claude-plugin/plugin.json" ] || { say "✗ missing authored manifest $OUT/.claude-plugin/plugin.json"; exit 1; }

say "▶ Packaging prd-ce plugin from .claude/ → plugins/prd-ce/"

# Clean only the generated payload; preserve authored .claude-plugin/
for d in skills agents hooks scripts; do rm -rf "${OUT:?}/$d"; done
mkdir -p "$OUT/skills" "$OUT/agents" "$OUT/hooks" "$OUT/scripts"

# 1. Skills — copy as-is
cp -R "$SRC/.claude/skills/." "$OUT/skills/"
n_skills=$(find "$OUT/skills" -name SKILL.md | wc -l | tr -d ' ')
say "  skills    : $n_skills SKILL.md copied"

# 2. Agents — flatten <name>/AGENT.md -> <name>.md, drop MEMORY*
n_agents=0
for agent_md in "$SRC"/.claude/agents/*/AGENT.md; do
  [ -f "$agent_md" ] || continue
  name="$(basename "$(dirname "$agent_md")")"
  cp "$agent_md" "$OUT/agents/$name.md"
  n_agents=$((n_agents+1))
done
say "  agents    : $n_agents flattened (MEMORY.md held back as seed)"

# 3. Hook scripts + generated hooks.json (path rewrite)
cp "$SRC"/.claude/hooks/*.sh "$OUT/hooks/" 2>/dev/null || true
python3 - "$SRC/.claude/settings.json" "$OUT/hooks/hooks.json" <<'PY'
import json, sys
src, dst = sys.argv[1], sys.argv[2]
cfg = json.load(open(src))
OLD = '"$CLAUDE_PROJECT_DIR"/.claude/hooks/'
NEW = '"${CLAUDE_PLUGIN_ROOT}"/hooks/'
def fix(s): return s.replace(OLD, NEW) if isinstance(s, str) else s
hooks = cfg.get("hooks", {})
for event, groups in hooks.items():
    for g in groups:
        for h in g.get("hooks", []):
            if "command" in h:
                h["command"] = fix(h["command"])
json.dump({"hooks": hooks}, open(dst, "w"), indent=2)
open(dst, "a").write("\n")
print("  hooks     : hooks.json generated, %d events, paths -> ${CLAUDE_PLUGIN_ROOT}" % len(hooks))
PY

# 4. Methodology scripts the hooks/skills call
cp "$SRC"/scripts/*.py "$OUT/scripts/" 2>/dev/null || true
cp "$SRC"/scripts/*.sh "$OUT/scripts/" 2>/dev/null || true
# don't ship the packager itself into the plugin
rm -f "$OUT/scripts/package-plugin.sh"
say "  scripts   : $(find "$OUT/scripts" -type f | wc -l | tr -d ' ') files copied"

# 5. Validate JSON outputs
python3 -c "import json; json.load(open('$OUT/.claude-plugin/plugin.json')); json.load(open('$OUT/hooks/hooks.json')); json.load(open('$SRC/.claude-plugin/marketplace.json'))" \
  && say "  validate  : plugin.json + hooks.json + marketplace.json are valid JSON ✓"

say "✔ Built plugins/prd-ce (payload is gitignored during strategy-B dev)"
