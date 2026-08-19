#!/usr/bin/env bash
# make-demo.sh — build the scratch repo used by the readiness GIF (docs/v2/V2_GO_LIVE_POLISH_PLAN.md §10.3).
#
#   bash docs/assets/readiness-demo/make-demo.sh prepare   # copy the healthy fixture to $DEMO and stub the API contracts → BLOCK
#   bash docs/assets/readiness-demo/make-demo.sh fix       # restore SoT.API_CONTRACTS.md → PASS
#   bash docs/assets/readiness-demo/make-demo.sh clean     # remove $DEMO
#
# Never records against this repository's own SoT/. DEMO defaults to /tmp/prd-ce-demo.
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/../../.." && pwd)"
DEMO="${DEMO:-/tmp/prd-ce-demo}"
FIXTURE="$ROOT/tests/fixtures/healthy_repo"
STUB='# API Contracts (SoT File)

_No contracts drafted yet._
'
case "${1:-}" in
  prepare)
    rm -rf "$DEMO"; cp -R "$FIXTURE" "$DEMO"; rm -rf "$DEMO/status"
    cp "$DEMO/SoT/SoT.API_CONTRACTS.md" "$DEMO/.api-contracts.keep"
    printf '%s' "$STUB" > "$DEMO/SoT/SoT.API_CONTRACTS.md"
    echo "prepared $DEMO (API contracts stubbed → expect v0.7 BLOCK, 'Populate SoT.API_CONTRACTS.md')"
    ;;
  fix)
    cp "$DEMO/.api-contracts.keep" "$DEMO/SoT/SoT.API_CONTRACTS.md"
    echo "restored SoT.API_CONTRACTS.md → expect v0.7 PASS"
    ;;
  clean)
    rm -rf "$DEMO"; echo "removed $DEMO" ;;
  *)
    echo "usage: $0 {prepare|fix|clean}" >&2; exit 2 ;;
esac
