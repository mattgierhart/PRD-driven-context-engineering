#!/usr/bin/env bash
# package-plugin.sh — Build the distributable `prd-ce` plugin payload from .claude/ source.
#
# Strategy B (de-risked): .claude/ stays the single source of truth during development;
# this deterministic transform generates plugins/prd-ce/{skills,rules,agents,hooks,scripts} from it.
# The generated payload is COMMITTED (tracked), because a GitHub plugin marketplace serves
# files from the cloned repo — consumers can only install what is committed. CI keeps the
# payload and .claude/ source from drifting (scripts/check-plugin-sync.sh). A later source-layout
# cutover, if approved, must preserve the same manifest and generated-payload contract.
#
# Transforms applied:
#   - skills/   : runnable skills copied; contributor-only indexes/template excluded
#   - rules/    : copied as inert references so relative links from skills remain closed
#   - agents/   : FLATTENED .claude/agents/<name>/AGENT.md -> agents/<name>.md (MEMORY.md NOT shipped)
#   - hooks/    : scripts copied; hooks.json generated from .claude/settings.json with hook
#                 command paths rewritten $CLAUDE_PROJECT_DIR/.claude/hooks -> ${CLAUDE_PLUGIN_ROOT}/hooks
#   - scripts/  : methodology scripts (readiness, validators) copied for hooks to call via PLUGIN_ROOT
#
# Usage: bash scripts/package-plugin.sh [--output DIR]   (run from repo root)
set -euo pipefail

SRC="$(cd "$(dirname "$0")/.." && pwd)"
DEFAULT_OUT="$SRC/plugins/prd-ce"
say() { printf '%s\n' "$*"; }
OUT_ARG=""
while [ $# -gt 0 ]; do
  case "$1" in
    --output) OUT_ARG="$2"; shift 2 ;;
    -h|--help) sed -n '2,24p' "$0"; exit 0 ;;
    *) echo "Unknown arg: $1" >&2; exit 2 ;;
  esac
done

[ -d "$SRC/.claude" ] || { say "✗ no .claude/ source at $SRC"; exit 1; }
if ! python3 - "$SRC" "$DEFAULT_OUT" <<'PY'
import os
import stat
import sys

source, output = map(os.path.abspath, sys.argv[1:])
try:
    relative = os.path.relpath(output, source)
except ValueError:
    relative = ".."
if relative == ".." or relative.startswith(".." + os.sep):
    print(f"✗ default plugin output is outside the source repo: {output}", file=sys.stderr)
    raise SystemExit(1)

# Cleanup addresses children through the output path. Refuse a symlink at the output or any of its
# in-repo ancestors so rm/cp cannot be redirected into an external directory.
current = source
for part in relative.split(os.sep):
    current = os.path.join(current, part)
    try:
        mode = os.lstat(current).st_mode
    except FileNotFoundError:
        continue
    except OSError as exc:
        print(f"✗ cannot inspect default plugin output path '{current}': {exc}", file=sys.stderr)
        raise SystemExit(1)
    if stat.S_ISLNK(mode):
        print(f"✗ refusing symlink in default plugin output path: '{current}'", file=sys.stderr)
        raise SystemExit(1)
PY
then
  exit 1
fi
[ -f "$DEFAULT_OUT/.claude-plugin/plugin.json" ] || { say "✗ missing authored manifest $DEFAULT_OUT/.claude-plugin/plugin.json"; exit 1; }

if [ -n "$OUT_ARG" ]; then
  [ ! -e "$OUT_ARG" ] && [ ! -L "$OUT_ARG" ] || {
    say "✗ custom output must not already exist: $OUT_ARG"; exit 1;
  }
  OUT_PARENT="$(dirname "$OUT_ARG")"
  OUT_NAME="$(basename "$OUT_ARG")"
  [ -d "$OUT_PARENT" ] && [ "$OUT_NAME" != "." ] && [ "$OUT_NAME" != ".." ] || {
    say "✗ custom output requires an existing parent and a specific new directory: $OUT_ARG"; exit 1;
  }
  OUT_PARENT="$(cd "$OUT_PARENT" && pwd)"
  OUT="$OUT_PARENT/$OUT_NAME"
  [ "$OUT" != "/" ] || { say "✗ unsafe plugin output: $OUT"; exit 1; }
  case "$OUT" in
    "$SRC"/*) say "✗ custom output must be outside the source repo: $OUT"; exit 1 ;;
  esac
  mkdir "$OUT"
else
  OUT="$DEFAULT_OUT"
fi
[ "$OUT" != "$SRC" ] && [ "$OUT" != "/" ] || { say "✗ unsafe plugin output: $OUT"; exit 1; }
if [ ! -f "$OUT/.claude-plugin/plugin.json" ]; then
  mkdir -p "$OUT/.claude-plugin"
  cp -R "$DEFAULT_OUT/.claude-plugin/." "$OUT/.claude-plugin/"
fi

# Packaging replaces several generated directories. Serialize invocations so a sync check and a
# manual build cannot interleave their remove/copy phases and leave a conflicted payload.
GIT_DIR="$(git -C "$SRC" rev-parse --git-dir 2>/dev/null || true)"
[ -n "$GIT_DIR" ] || { say "✗ packaging requires a Git checkout"; exit 1; }
case "$GIT_DIR" in
  /*) ;;
  *) GIT_DIR="$SRC/$GIT_DIR" ;;
esac
PACKAGE_LOCK="$GIT_DIR/prd-ce-package.lock"
if ! mkdir "$PACKAGE_LOCK" 2>/dev/null; then
  say "✗ another prd-ce packaging process is already running"
  exit 1
fi
cleanup_lock() { rmdir "$PACKAGE_LOCK" 2>/dev/null || true; }
trap cleanup_lock EXIT
trap 'exit 130' INT
trap 'exit 143' TERM

say "▶ Packaging prd-ce plugin from .claude/ → $OUT"

# Clean only the generated payload; preserve authored .claude-plugin/
for d in skills rules agents hooks scripts templates; do rm -rf "${OUT:?}/$d"; done
mkdir -p "$OUT/skills" "$OUT/rules" "$OUT/agents" "$OUT/hooks" "$OUT/scripts" "$OUT/templates"

# 1. Skills — copy as-is
cp -R "$SRC/.claude/skills/." "$OUT/skills/"
# These operators manage a copied framework layout. Plugin consumers receive framework behavior
# live and must use /prd-ce:init for consumer-owned seeds, so publishing them would expose unusable
# local-path workflows and an overlapping initializer.
rm -rf \
  "$OUT/skills/ghm-self-install" \
  "$OUT/skills/ghm-template-sync" \
  "$OUT/skills/SKILL_TEMPLATE"
rm -f "$OUT/skills/README.md" "$OUT/skills/skills-inventory.md"
n_skills=$(find "$OUT/skills" -name SKILL.md | wc -l | tr -d ' ')
say "  skills    : $n_skills SKILL.md copied"

# Skills link to the operating rules with ../../rules/... paths. Rules do not auto-load from a
# plugin, but shipping this reference surface keeps those instructions readable and self-contained.
cp -R "$SRC/.claude/rules/." "$OUT/rules/"
python3 - "$OUT/rules" <<'PY'
from pathlib import Path
import sys

for path in Path(sys.argv[1]).glob("*.md"):
    text = path.read_text()
    # Canonical rules live under .claude/rules; packaged rules live one level shallower.
    text = text.replace("(../../docs/", "(../templates/docs/")
    path.write_text(text)
PY
say "  rules     : $(find "$OUT/rules" -type f | wc -l | tr -d ' ') references copied"

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
cp "$SRC"/.claude/hooks/*.py "$OUT/hooks/" 2>/dev/null || true
cp "$SRC/.claude/hooks/HOOK_CONTRACT.md" "$OUT/hooks/"
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

# 4. Methodology scripts the hooks/skills call. Use the manifest framework allowlist; entries also
# listed in direct_exclude (such as prd-ce-init.sh) remain plugin-only.
python3 - "$SRC" "$OUT/scripts" <<'PY'
from pathlib import Path
import re
import shutil
import sys

src_root, out_root = map(Path, sys.argv[1:])
manifest = src_root / ".claude" / "install-manifest.yaml"
framework, grab = [], False
for line in manifest.read_text().splitlines():
    if re.match(r"^framework:\s*$", line):
        grab = True
        continue
    if re.match(r"^[A-Za-z_]+:", line):
        grab = False
    if grab:
        match = re.match(r"^\s*-\s*(.+?)\s*$", line)
        if match:
            item = re.sub(r"\s+#.*$", "", match.group(1)).strip()
            if item.startswith("scripts/"):
                framework.append(item)

for item in framework:
    source = src_root / item
    target = out_root / Path(item).relative_to("scripts")
    if source.is_dir():
        shutil.copytree(source, target, dirs_exist_ok=True)
    elif source.is_file():
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
    else:
        raise SystemExit(f"manifest script source missing: {item}")
PY
say "  scripts   : $(find "$OUT/scripts" -type f | wc -l | tr -d ' ') files copied"

# 4b. Seed templates bundle — the consumer-owned scaffold /prd-ce:init plants.
# The framework ships LIVE in the plugin; these are the files init copies into a fresh
# repo. Mirror each template_seed SOURCE path under templates/<src> so prd-ce-init.sh
# resolves "$CLAUDE_PLUGIN_ROOT/templates/<src>" identically to the in-repo dogfood path.
python3 - "$SRC" "$OUT/templates" <<'PY'
import os
import posixpath
import re
import shutil
import sys

src_root, tpl_out = sys.argv[1], sys.argv[2]
manifest = os.path.join(src_root, ".claude", "install-manifest.yaml")

# Flat parse of seed sources and the explicit plugin-only review aliases.
sections = {"template_seed": [], "plugin_review_alias": []}
current = None
for line in open(manifest):
    top = re.match(r'^([A-Za-z_]+):\s*$', line)
    if top:
        current = top.group(1)
        continue
    if current in sections:
        m = re.match(r'^\s*-\s*(.+?)\s*$', line)
        if m:
            value = re.sub(r'\s*#.*$', '', m.group(1)).strip()
            if value:
                sections[current].append(value)

def safe_relative(path):
    if not path or os.path.isabs(path) or "\\" in path:
        return False
    normalized = posixpath.normpath(path)
    return normalized == path and normalized not in {"", "."} and ".." not in path.split("/")

seed_mapping = {}
for entry in sections["template_seed"]:
    if " -> " in entry:
        source, destination = entry.split(" -> ", 1)
    else:
        source = destination = entry
    if not safe_relative(source) or not safe_relative(destination):
        raise SystemExit(f"unsafe template seed path: {source!r} -> {destination!r}")
    if destination in seed_mapping:
        raise SystemExit(f"duplicate template seed destination: {destination}")
    seed_mapping[destination] = source

# Init also needs the manifest and its local CLAUDE consumer guide.
extra = [
    ".claude/install-manifest.yaml",
    "CLAUDE_plugin_stub.md",
]

def copy_path(source_relative, destination_relative):
    source = os.path.join(src_root, source_relative)
    destination = os.path.join(tpl_out, destination_relative)
    if not os.path.lexists(source):
        raise SystemExit(f"template source missing: {source_relative}")
    os.makedirs(os.path.dirname(destination), exist_ok=True)
    if os.path.isdir(source) and not os.path.islink(source):
        shutil.copytree(source, destination, dirs_exist_ok=True)
    else:
        shutil.copy2(source, destination)

n = 0
for source in list(seed_mapping.values()) + extra:
    if not safe_relative(source):
        raise SystemExit(f"unsafe bundled template path: {source!r}")
    copy_path(source, source)
    n += 1

aliases = sections["plugin_review_alias"]
for destination in aliases:
    if not safe_relative(destination):
        raise SystemExit(f"unsafe plugin review alias: {destination!r}")
    source = seed_mapping.get(destination)
    if source is None:
        raise SystemExit(f"plugin review alias is not a template seed destination: {destination}")
    if not os.path.isfile(os.path.join(src_root, source)):
        raise SystemExit(f"plugin review alias source is not a file: {source}")
    copy_path(source, destination)

print(
    "  templates : %d sources bundled + %d read-only review aliases"
    % (n, len(aliases))
)
PY

# 5. Validate JSON outputs
python3 -c "import json; json.load(open('$OUT/.claude-plugin/plugin.json')); json.load(open('$OUT/hooks/hooks.json')); json.load(open('$SRC/.claude-plugin/marketplace.json'))" \
  && say "  validate  : plugin.json + hooks.json + marketplace.json are valid JSON ✓"

if [ "$OUT" = "$DEFAULT_OUT" ]; then
  say "✔ Built plugins/prd-ce — commit the payload (it is tracked so the marketplace can serve it)"
else
  say "✔ Built verification payload at $OUT"
fi
