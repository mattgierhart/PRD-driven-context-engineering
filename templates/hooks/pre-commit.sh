#!/bin/bash
# GHM Pre-Commit Hook
# Validates that EPIC Session State is updated when code changes are committed
#
# Installation:
#   cp templates/hooks/pre-commit.sh .git/hooks/pre-commit
#   chmod +x .git/hooks/pre-commit

set -e

# Colors for output
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo "GHM Pre-Commit Hook: Checking session state..."

# Check if any code files are being committed (not just docs)
CODE_CHANGES=$(git diff --cached --name-only | grep -E '\.(py|js|ts|tsx|jsx|go|rs|java|rb|php|swift|kt)$' || true)

if [ -z "$CODE_CHANGES" ]; then
    # No code changes, allow commit
    echo -e "${GREEN}✓ No code changes detected, skipping EPIC check${NC}"
    exit 0
fi

# Check if an EPIC file is also being committed
EPIC_CHANGES=$(git diff --cached --name-only | grep -E 'epics/EPIC-.*\.md$' || true)

if [ -z "$EPIC_CHANGES" ]; then
    echo -e "${YELLOW}⚠ Warning: Code changes detected but no EPIC file updated${NC}"
    echo ""
    echo "You're committing code changes without updating the EPIC Session State."
    echo "This may make it difficult for the next agent to continue your work."
    echo ""
    echo "Files being committed:"
    echo "$CODE_CHANGES" | sed 's/^/  - /'
    echo ""
    echo "Recommended actions:"
    echo "  1. Update the active EPIC's Section 0 (Session State)"
    echo "  2. Stage the EPIC: git add epics/EPIC-XX.md"
    echo "  3. Try commit again"
    echo ""
    echo "To skip this check (not recommended):"
    echo "  git commit --no-verify"
    echo ""

    # Prompt for confirmation (only works in interactive mode)
    if [ -t 0 ]; then
        read -p "Continue without EPIC update? (y/N) " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            echo -e "${RED}✗ Commit aborted. Update EPIC Session State first.${NC}"
            exit 1
        fi
    else
        # Non-interactive mode (CI/automation) - warn but don't block
        echo -e "${YELLOW}⚠ Non-interactive mode: allowing commit with warning${NC}"
    fi
fi

# If EPIC is being updated, validate Section 0 has content
if [ -n "$EPIC_CHANGES" ]; then
    for epic_file in $EPIC_CHANGES; do
        if [ -f "$epic_file" ]; then
            # Check for Session State section
            if ! grep -q "## 0. Session State" "$epic_file"; then
                echo -e "${RED}✗ EPIC file missing Section 0 (Session State): $epic_file${NC}"
                exit 1
            fi

            # Check for placeholder content that wasn't filled in
            if grep -q "{YYYY-MM-DD" "$epic_file" | head -5 | grep -q "Session Date"; then
                echo -e "${YELLOW}⚠ Warning: EPIC Session State may contain unfilled placeholders${NC}"
            fi
        fi
    done
    echo -e "${GREEN}✓ EPIC Session State check passed${NC}"
fi

exit 0
