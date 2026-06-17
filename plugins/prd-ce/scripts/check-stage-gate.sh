#!/bin/bash
#
# Stage Gate Validation Script
# Validates that required artifacts exist before advancing PRD stages.
#
# Usage: ./scripts/check-stage-gate.sh [target_stage]
#   target_stage: The stage you want to advance TO (e.g., "0.6" or "v0.6")
#
# Exit codes:
#   0 = Gate passed
#   1 = Gate failed (missing artifacts)
#   2 = Invalid usage
#
# This script performs FILE-EXISTENCE checks only.
# It does NOT validate content quality or semantic correctness.

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Get script directory to find repo root
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"

# Parse target stage
TARGET_STAGE="${1:-}"
if [[ -z "$TARGET_STAGE" ]]; then
    echo -e "${RED}Error: Target stage required${NC}"
    echo "Usage: $0 <target_stage>"
    echo "Example: $0 v0.6"
    exit 2
fi

# Normalize stage format (remove 'v' prefix if present)
TARGET_STAGE="${TARGET_STAGE#v}"

echo "========================================"
echo "Stage Gate Validation"
echo "Target Stage: v${TARGET_STAGE}"
echo "Repo Root: ${REPO_ROOT}"
echo "========================================"
echo ""

ERRORS=()
WARNINGS=()

# Helper function to check file exists
check_file() {
    local file="$1"
    local description="$2"
    local required="${3:-true}"

    if [[ -f "${REPO_ROOT}/${file}" ]]; then
        echo -e "${GREEN}✓${NC} ${description}: ${file}"
        return 0
    else
        if [[ "$required" == "true" ]]; then
            echo -e "${RED}✗${NC} ${description}: ${file} (MISSING)"
            ERRORS+=("Missing required file: ${file}")
            return 1
        else
            echo -e "${YELLOW}○${NC} ${description}: ${file} (optional, not found)"
            WARNINGS+=("Optional file not found: ${file}")
            return 0
        fi
    fi
}

# Helper function to check file contains text
check_file_contains() {
    local file="$1"
    local pattern="$2"
    local description="$3"

    if [[ -f "${REPO_ROOT}/${file}" ]]; then
        if grep -q "$pattern" "${REPO_ROOT}/${file}" 2>/dev/null; then
            echo -e "${GREEN}✓${NC} ${description}"
            return 0
        else
            echo -e "${RED}✗${NC} ${description} (pattern not found)"
            ERRORS+=("${description}: pattern '${pattern}' not found in ${file}")
            return 1
        fi
    else
        echo -e "${RED}✗${NC} ${description} (file not found: ${file})"
        ERRORS+=("File not found: ${file}")
        return 1
    fi
}

# Helper function to check directory has files matching pattern
check_dir_has_files() {
    local dir="$1"
    local pattern="$2"
    local description="$3"
    local required="${4:-true}"

    local count=$(find "${REPO_ROOT}/${dir}" -name "$pattern" 2>/dev/null | wc -l)

    if [[ $count -gt 0 ]]; then
        echo -e "${GREEN}✓${NC} ${description}: ${count} file(s) found"
        return 0
    else
        if [[ "$required" == "true" ]]; then
            echo -e "${RED}✗${NC} ${description}: No files matching ${pattern} in ${dir}"
            ERRORS+=("No files matching ${pattern} in ${dir}")
            return 1
        else
            echo -e "${YELLOW}○${NC} ${description}: No files found (optional)"
            return 0
        fi
    fi
}

echo "Checking prerequisites for v${TARGET_STAGE}..."
echo ""

# Gate checks by stage
case "$TARGET_STAGE" in
    "0.2")
        echo "=== v0.2 Market Definition Gate ==="
        check_file "PRD.md" "PRD document exists"
        check_file_contains "PRD.md" "v0.1 Spark" "PRD has v0.1 section"
        check_file "SoT/SoT.customer_feedback.md" "Customer feedback SoT exists"
        ;;

    "0.3")
        echo "=== v0.3 Commercial Model Gate ==="
        check_file "PRD.md" "PRD document exists"
        check_file_contains "PRD.md" "v0.2 Market Definition" "PRD has v0.2 section"
        check_file "SoT/SoT.BUSINESS_RULES.md" "Business rules SoT exists"
        ;;

    "0.4")
        echo "=== v0.4 User Journeys Gate ==="
        check_file "PRD.md" "PRD document exists"
        check_file_contains "PRD.md" "v0.3 Commercial Model" "PRD has v0.3 section"
        check_file "SoT/SoT.BUSINESS_RULES.md" "Business rules SoT exists"
        ;;

    "0.5")
        echo "=== v0.5 Red Team Review Gate ==="
        check_file "PRD.md" "PRD document exists"
        check_file_contains "PRD.md" "v0.4 User Journeys" "PRD has v0.4 section"
        check_file "SoT/SoT.USER_JOURNEYS.md" "User journeys SoT exists"
        ;;

    "0.6")
        echo "=== v0.6 Architecture Gate ==="
        check_file "PRD.md" "PRD document exists"
        check_file_contains "PRD.md" "v0.5 Red Team" "PRD has v0.5 section"
        check_file "SoT/SoT.USER_JOURNEYS.md" "User journeys SoT exists"
        check_file "SoT/SoT.BUSINESS_RULES.md" "Business rules SoT exists"
        ;;

    "0.7")
        echo "=== v0.7 Build Execution Gate ==="
        check_file "PRD.md" "PRD document exists"
        check_file_contains "PRD.md" "v0.6 Architecture" "PRD has v0.6 section"
        check_file "SoT/SoT.TECHNICAL_DECISIONS.md" "Technical decisions SoT exists"
        check_file "SoT/SoT.API_CONTRACTS.md" "API contracts SoT exists" "false"
        check_file "SoT/SoT.DATA_MODEL.md" "Data model SoT exists" "false"
        ;;

    "0.8")
        echo "=== v0.8 Release & Deployment Gate ==="
        check_file "PRD.md" "PRD document exists"
        check_file_contains "PRD.md" "v0.7 Build" "PRD has v0.7 section"
        check_dir_has_files "epics" "EPIC-*.md" "At least one EPIC exists"
        check_file "SoT/SoT.TESTING.md" "Testing SoT exists" "false"
        ;;

    "0.9")
        echo "=== v0.9 Go-to-Market Gate ==="
        check_file "PRD.md" "PRD document exists"
        check_file_contains "PRD.md" "v0.8" "PRD has v0.8 section"
        check_file "SoT/SoT.DEPLOYMENT.md" "Deployment SoT exists" "false"
        ;;

    "1.0")
        echo "=== v1.0 Market Adoption Gate ==="
        check_file "PRD.md" "PRD document exists"
        check_file_contains "PRD.md" "v0.9 Go-to-Market" "PRD has v0.9 section"
        ;;

    *)
        echo -e "${YELLOW}Warning: Unknown stage v${TARGET_STAGE}${NC}"
        echo "Known stages: 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0"
        echo "Skipping validation (no checks defined for this stage)"
        exit 0
        ;;
esac

echo ""
echo "========================================"

# Report results
if [[ ${#WARNINGS[@]} -gt 0 ]]; then
    echo -e "${YELLOW}Warnings:${NC}"
    for warning in "${WARNINGS[@]}"; do
        echo "  - $warning"
    done
    echo ""
fi

if [[ ${#ERRORS[@]} -gt 0 ]]; then
    echo -e "${RED}GATE FAILED${NC}"
    echo ""
    echo "Missing requirements:"
    for error in "${ERRORS[@]}"; do
        echo "  - $error"
    done
    echo ""
    echo "Run /ghm-gate-check for detailed guidance on what's missing."
    exit 1
else
    echo -e "${GREEN}GATE PASSED${NC}"
    echo "Ready to advance to v${TARGET_STAGE}"
    exit 0
fi
