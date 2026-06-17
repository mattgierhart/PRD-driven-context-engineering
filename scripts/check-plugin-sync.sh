#!/usr/bin/env bash
# check-plugin-sync.sh — Guard against drift between the .claude/ authoring source and
# the committed plugin payload under plugins/prd-ce/.
#
# Strategy B keeps .claude/ as the source and generates the plugin payload from it. Because
# the payload is committed (a GitHub marketplace can only serve committed files), the two
# can silently diverge if someone edits .claude/ without re-running the packager. This check
# regenerates the payload and fails if anything under plugins/prd-ce/ changed — i.e. the
# committed payload was stale. Runs in CI (clean checkout) and locally before committing.
set -euo pipefail
cd "$(dirname "$0")/.."

bash scripts/package-plugin.sh >/dev/null

DIRTY="$(git status --porcelain -- plugins/prd-ce)"
if [ -n "$DIRTY" ]; then
  echo "✗ plugin payload is out of sync with .claude/ source." >&2
  echo "  Fix: bash scripts/package-plugin.sh && git add plugins/prd-ce && commit." >&2
  echo "  Drifted paths:" >&2
  printf '%s\n' "$DIRTY" >&2
  exit 1
fi

echo "✓ plugin payload is in sync with .claude/ source"
