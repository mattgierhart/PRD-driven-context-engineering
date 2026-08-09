#!/usr/bin/env bash
# check-plugin-sync.sh — Guard against drift between the .claude/ authoring source and
# the committed plugin payload under plugins/prd-ce/.
#
# Strategy B keeps .claude/ as the source and generates the plugin payload from it. Because
# the payload is committed (a GitHub marketplace can only serve committed files), the two
# can silently diverge if someone edits .claude/ without re-running the packager. This check
# generates a payload in an isolated temporary directory, then compares it with both the working
# payload and Git index. This works in CI and before a local commit without mutating tracked files:
# correctly staged payloads pass, while stale generation, forgotten `git add` changes, and newly
# generated untracked files fail.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PAYLOAD="$ROOT/plugins/prd-ce"
SYNC_TMP="$(mktemp -d)"
cleanup_sync_tmp() { rm -rf "$SYNC_TMP"; }
trap cleanup_sync_tmp EXIT
trap 'exit 130' INT
trap 'exit 143' TERM
GENERATED="$SYNC_TMP/prd-ce"

cd "$ROOT"
bash scripts/package-plugin.sh --output "$GENERATED" >/dev/null

DRIFT=""
for surface in skills rules agents hooks scripts templates; do
  # Git cannot carry empty directories. Compare the generated and working file sets plus bytes,
  # while the index/untracked checks below continue to reject every commit-surface difference.
  # This avoids false drift from sync-provider conflict directories that contain no files.
  if ! python3 - "$GENERATED/$surface" "$PAYLOAD/$surface" <<'PY'
from pathlib import Path
import sys

generated, payload = map(Path, sys.argv[1:])

def files(root: Path) -> dict[Path, bytes]:
    return {
        path.relative_to(root): path.read_bytes()
        for path in root.rglob("*")
        if path.is_file()
    }

raise SystemExit(0 if files(generated) == files(payload) else 1)
PY
  then
    DRIFT="${DRIFT}${surface}\n"
  fi
done

UNTRACKED="$(git ls-files --others --exclude-standard -- plugins/prd-ce)"
if [ -n "$DRIFT" ] || ! git diff --quiet -- plugins/prd-ce || [ -n "$UNTRACKED" ]; then
  echo "✗ plugin payload is out of sync with .claude/ source." >&2
  echo "  Fix: bash scripts/package-plugin.sh && git add plugins/prd-ce && commit." >&2
  echo "  Drifted paths:" >&2
  [ -z "$DRIFT" ] || printf '%b' "$DRIFT" >&2
  git diff --name-only -- plugins/prd-ce >&2 || true
  [ -z "$UNTRACKED" ] || printf '%s\n' "$UNTRACKED" >&2
  exit 1
fi

echo "✓ plugin payload is in sync with .claude/ source"
