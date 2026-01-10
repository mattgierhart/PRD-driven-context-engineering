---
version: 1.0
purpose: Auto-generated central registry of all IDs across Source of Truth files
generation: Hybrid (script-generated + human validation)
sync_command: npm run codex:sync-registry
last_synced: YYYY-MM-DD HH:MM:SS
authority: This file is AUTO-GENERATED - do not edit manually. Run sync command to rebuild.
---

# ID Registry (Auto-Generated)

> **Purpose**: Central index of all unique IDs across the knowledge graph
> **Update Method**: Run `npm run codex:sync-registry` to rebuild from SoT files
> **Status**: Auto-generated (do not edit manually)

## Quick Stats

| ID Type | Count | SoT File | Status |
|---------|-------|----------|--------|
| UJ-XXX | {count} | USER-JOURNEYS.md | ✅ Active |
| BR-XXX | {count} | BUSINESS_RULES.md | ✅ Active |
| API-XXX | {count} | API_CONTRACTS.md | ✅ Active |
| DBT-XXX | {count} | ACTUAL-SCHEMA.md | ✅ Active |
| CFD-XXX | {count} | customer-feedback.md | ✅ Active |
| TEST-XXX | {count} | testing-playbook.md | ✅ Active |
| DEP-XXX | {count} | deployment-playbook.md | ✅ Active |
| DES-XXX | {count} | design-brief.md | ✅ Active |
| SEC-XXX | {count} | security-playbook.md | ⚠️ Optional |
| PERF-XXX | {count} | performance-playbook.md | ⚠️ Optional |

**Last Sync**: {timestamp}
**Total IDs**: {total_count}

---

## User Journeys (UJ-XXX)

**Source**: USER-JOURNEYS.md

| ID | Title | Status | Used By |
|----|-------|--------|---------|
| UJ-001 | {Journey Title} | Active | API-XXX, TEST-XXX |
| UJ-002 | {Journey Title} | Active | API-YYY |

---

## Business Rules (BR-XXX)

**Source**: BUSINESS_RULES.md

| ID | Rule Name | Severity | Enforced By |
|----|-----------|----------|-------------|
| BR-001 | {Rule Name} | Critical | API-XXX |
| BR-002 | {Rule Name} | High | API-YYY |

---

## API Contracts (API-XXX)

**Source**: API_CONTRACTS.md

| ID | Endpoint | Method | Used By |
|----|----------|--------|---------|
| API-001 | {Endpoint Path} | POST | UJ-XXX |
| API-002 | {Endpoint Path} | GET | UJ-YYY |

---

## Database Tables (DBT-XXX)

**Source**: ACTUAL-SCHEMA.md

| ID | Table Name | Accessed By |
|----|------------|-------------|
| DBT-001 | {table_name} | API-XXX |
| DBT-002 | {table_name} | API-YYY |

---

## Customer Feedback (CFD-XXX)

**Source**: customer-feedback.md

| ID | Category | Status | Affects |
|----|----------|--------|---------|
| CFD-001 | Feature Request | Planned | UJ-XXX |
| CFD-002 | Bug Report | In Progress | API-YYY |

---

## Tests (TEST-XXX)

**Source**: testing-playbook.md

| ID | Test Name | Category | Validates |
|----|-----------|----------|-----------|
| TEST-001 | {Test Name} | Unit | API-XXX |
| TEST-002 | {Test Name} | Integration | UJ-YYY |

---

## Deployments (DEP-XXX)

**Source**: deployment-playbook.md

| ID | Configuration | Environment | Used By |
|----|--------------|-------------|---------|
| DEP-001 | {Config Name} | Production | API-XXX |
| DEP-002 | {Config Name} | Staging | API-YYY |

---

## Design Components (DES-XXX)

**Source**: design-brief.md

| ID | Component Name | Platform | Used In |
|----|---------------|----------|---------|
| DES-001 | {Component Name} | Web | UJ-XXX |
| DES-002 | {Component Name} | Mobile | UJ-YYY |

---

## Security Controls (SEC-XXX)

**Source**: security-playbook.md (optional)

| ID | Control Name | Compliance | Enforced By |
|----|-------------|------------|-------------|
| SEC-001 | {Control Name} | SOC2 | API-XXX |
| SEC-002 | {Control Name} | GDPR | API-YYY |

---

## Performance Metrics (PERF-XXX)

**Source**: performance-playbook.md (optional)

| ID | Metric Name | Target | Monitored By |
|----|------------|--------|--------------|
| PERF-001 | {Metric Name} | <200ms | DEP-XXX |
| PERF-002 | {Metric Name} | <500ms | DEP-YYY |

---

## Cross-Reference Validation

### Orphaned IDs
IDs referenced but not defined in any SoT file:
- {ID-XXX} - Referenced by {FILE} but not found in {SOURCE_FILE}

### Dangling References
IDs defined but never referenced:
- {ID-YYY} - Defined in {SOURCE_FILE} but not referenced anywhere

### Broken Links
Cross-references pointing to non-existent IDs:
- {SOURCE} references {TARGET} which doesn't exist

---

## Sync Scripts

### npm run codex:sync-registry

Rebuilds this file by scanning all SoT files for ID definitions.

```bash
#!/bin/bash
# scripts/codex-sync-registry.sh

echo "🔄 Syncing ID Registry from Source of Truth files..."

# Scan each SoT file for IDs
UJ_COUNT=$(grep -c "^## UJ-" USER-JOURNEYS.md 2>/dev/null || echo 0)
BR_COUNT=$(grep -c "^## BR-" BUSINESS_RULES.md 2>/dev/null || echo 0)
API_COUNT=$(grep -c "^## API-" API_CONTRACTS.md 2>/dev/null || echo 0)
# ... (continue for all ID types)

# Rebuild .codex/ID-REGISTRY.md with current data
# Include timestamp and counts

echo "✅ ID Registry synced successfully"
echo "   Total IDs: $TOTAL_COUNT"
echo "   Last sync: $(date)"
```

### npm run codex:check-links

Validates all cross-references between IDs.

```bash
#!/bin/bash
# scripts/codex-check-links.sh

echo "🔗 Checking bidirectional links..."

# For each ID, verify:
# 1. All referenced IDs exist
# 2. Bidirectional links are present
# 3. No orphaned IDs

echo "✅ Link check complete"
```

### npm run codex:find-orphans

Finds IDs that are defined but never referenced.

```bash
#!/bin/bash
# scripts/codex-find-orphans.sh

echo "🔍 Finding orphaned IDs..."

# Scan for IDs defined in SoT files
# Check if they're referenced anywhere
# Report orphans

echo "✅ Orphan scan complete"
```

---

## NPM Script Configuration

Add to `package.json`:

```json
{
  "scripts": {
    "codex:sync-registry": "bash scripts/codex-sync-registry.sh",
    "codex:check-links": "bash scripts/codex-check-links.sh",
    "codex:find-orphans": "bash scripts/codex-find-orphans.sh",
    "codex:validate": "npm run codex:sync-registry && npm run codex:check-links && npm run codex:find-orphans"
  }
}
```

---

*This file is auto-generated by the CODEX sync scripts. Do not edit manually. Run `npm run codex:sync-registry` to rebuild.*
