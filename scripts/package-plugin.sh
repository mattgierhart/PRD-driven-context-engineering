#!/usr/bin/env bash
# package-plugin.sh — Build the distributable `prd-ce` plugin payload from .claude/ source.
#
# Strategy B (de-risked): .claude/ stays the single source of truth during development;
# this deterministic transform generates plugins/prd-ce/{skills,agents,hooks,scripts} from it.
# The generated payload is COMMITTED (tracked), because a GitHub plugin marketplace serves
# files from the cloned repo — consumers can only install what is committed. CI keeps the
# payload and .claude/ source from drifting (scripts/check-plugin-sync.sh). The strategy-A
# cutover later makes the plugin the source outright. See temp/plugin-conversion-plan.md.
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
for d in skills agents hooks scripts templates; do rm -rf "${OUT:?}/$d"; done
mkdir -p "$OUT/skills" "$OUT/agents" "$OUT/hooks" "$OUT/scripts" "$OUT/templates"

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
# Dev/build-only tooling stays in the repo; it is not part of the shipped plugin.
rm -f "$OUT/scripts/package-plugin.sh" "$OUT/scripts/check-plugin-sync.sh"
say "  scripts   : $(find "$OUT/scripts" -type f | wc -l | tr -d ' ') files copied"

# 4b. Seed templates bundle — the consumer-owned scaffold /prd-ce:init plants.
# The framework ships LIVE in the plugin; these are the files init copies into a fresh
# repo. Mirror each template_seed SOURCE path under templates/<src> so prd-ce-init.sh
# resolves "$CLAUDE_PLUGIN_ROOT/templates/<src>" identically to the in-repo dogfood path.
python3 - "$SRC" "$OUT/templates" <<'PY'
import os, re, shutil, sys
src_root, tpl_out = sys.argv[1], sys.argv[2]
manifest = os.path.join(src_root, ".claude", "install-manifest.yaml")

# Flat parse of the `template_seed:` list (mirrors install.sh's awk contract).
seeds, grab = [], False
for line in open(manifest):
    if re.match(r'^template_seed:\s*$', line):
        grab = True; continue
    if re.match(r'^[A-Za-z_]+:', line):
        grab = False
    if grab:
        m = re.match(r'^\s*-\s*(.+?)\s*$', line)
        if m:
            seeds.append(re.sub(r'\s*#.*$', '', m.group(1)).strip())

# init also seeds consumer-owned config + needs the manifest to know what to seed.
extra = [".claude/domain-profile.yaml", ".claude/install-manifest.yaml"]

n = 0
for entry in seeds + extra:
    src_rel = entry.split("->")[0].strip()        # left of "->" is the SOURCE path
    src = os.path.join(src_root, src_rel)
    dst = os.path.join(tpl_out, src_rel)
    if not os.path.exists(src):
        print("  ⚠ templates: missing seed source %s (skipped)" % src_rel); continue
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    if os.path.isdir(src):
        shutil.copytree(src, dst, dirs_exist_ok=True)
    else:
        shutil.copy2(src, dst)
    n += 1
print("  templates : %d seed sources bundled (template_seed + consumer config)" % n)
PY

# 5. Validate JSON outputs
python3 -c "import json; json.load(open('$OUT/.claude-plugin/plugin.json')); json.load(open('$OUT/hooks/hooks.json')); json.load(open('$SRC/.claude-plugin/marketplace.json'))" \
  && say "  validate  : plugin.json + hooks.json + marketplace.json are valid JSON ✓"

say "✔ Built plugins/prd-ce — commit the payload (it is tracked so the marketplace can serve it)"
