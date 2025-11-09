# ID-Based Knowledge Graph System

## Overview

The ID-Based Knowledge Graph is a documentation architecture that assigns unique, durable IDs to every meaningful artifact in your product documentation. This enables precise cross-referencing without duplicate prose and dramatically improves AI agent context loading (from 5-10 minutes to <1 minute).

## Core Concept

Instead of duplicating specifications across multiple documents, each artifact gets a unique ID that can be referenced elsewhere:

**Without IDs** (Duplicate Prose):
```markdown
# PRD.md
Users can create up to 3 products on the free tier.

# API_CONTRACTS.md
POST /products validates that free tier users don't exceed 3 products.

# USER-JOURNEYS.md
When adding a product, system checks free tier limit of 3 products.

# testing-playbook.md
Test that free tier users are limited to 3 products.
```

**With IDs** (Single Source of Truth):
```markdown
# BUSINESS_RULES.md
## BR-001: Free Tier Product Limit
Free tier users MUST be limited to 3 products maximum.

# API_CONTRACTS.md
POST /products enforces [BR-001](BUSINESS_RULES.md#br-001)

# USER-JOURNEYS.md
Step 3 validates [BR-001](BUSINESS_RULES.md#br-001)

# testing-playbook.md
TEST-301 validates [BR-001](BUSINESS_RULES.md#br-001)
```

## Architecture

### Three Layers

1. **Navigation Layer** (The "3" Files):
   - Claude.md - Process rules and workflow
   - PRD.md - Product requirements and context
   - README.md - Operational dashboard
   - **Role**: Provide context, point to IDs, show active work
   - **Rule**: NEVER create IDs, only reference them

2. **Reference Library** (Source of Truth Files):
   - USER-JOURNEYS.md (UJ-XXX)
   - BUSINESS_RULES.md (BR-XXX)
   - API_CONTRACTS.md (API-XXX)
   - ACTUAL-SCHEMA.md (DBT-XXX)
   - testing-playbook.md (TEST-XXX)
   - deployment-playbook.md (DEP-XXX)
   - customer-feedback.md (CFD-XXX)
   - **Role**: Create and maintain IDs with full specifications
   - **Rule**: Each ID type has its own SoT file

3. **Change Tracking** (EPIC Files):
   - **Role**: Track which IDs were modified/created during development
   - **Rule**: Include Section 3A "ID Tracking" in every EPIC

### ID Types and Prefixes

| Prefix | Type | SoT File | Example |
|--------|------|----------|---------|
| UJ-XXX | User Journey | USER-JOURNEYS.md | UJ-101: Product Onboarding |
| BR-XXX | Business Rule | BUSINESS_RULES.md | BR-001: Free Tier Limit |
| API-XXX | API Endpoint | API_CONTRACTS.md | API-045: Create Product |
| DBT-XXX | Database Table | ACTUAL-SCHEMA.md | DBT-018: products |
| TEST-XXX | Test Case | testing-playbook.md | TEST-301: Validates BR-001 |
| DEP-XXX | Deployment Config | deployment-playbook.md | DEP-027: Railway Config |
| DES-XXX | Design Component | {product}-DesignBrief.md | DES-042: Product Card |
| CFD-XXX | Customer Feedback | customer-feedback.md | CFD-089: Request Sharing |
| SEC-XXX | Security Control | security-playbook.md | SEC-012: API Rate Limiting |
| PERF-XXX | Performance Target | performance-playbook.md | PERF-005: API <200ms |

## Progressive Adoption

### Phase 1: Core IDs (Start Here)
Start with the 5 most impactful ID types:
- BR-XXX (Business Rules) - Critical for enforcement
- API-XXX (API Endpoints) - Critical for implementation
- UJ-XXX (User Journeys) - Critical for UX validation
- DBT-XXX (Database Tables) - Critical for data integrity
- TEST-XXX (Tests) - Critical for quality gates

### Phase 2: Quality & Operations
Add as complexity grows:
- DEP-XXX (Deployment) - When infrastructure becomes complex
- CFD-XXX (Customer Feedback) - When feedback becomes systematic

### Phase 3: Advanced IDs
Add for mature products:
- DES-XXX (Design) - When design system is established
- SEC-XXX (Security) - When security requirements are extensive
- PERF-XXX (Performance) - When performance SLAs are critical

## Implementation Workflow

### During Development (EPIC Phase)

1. **Phase A - Planning**: Identify which IDs will be affected
2. **Phase B - Implementation**: Create new IDs, modify existing ones
3. **Phase C - Testing**: Validate ID relationships work correctly
4. **Phase E - Documentation**: Update all bidirectional references

### EPIC Section 3A: ID Tracking

Every EPIC includes this section to track ID changes:

```markdown
## 3A. ID Tracking (Knowledge Graph)

### IDs Modified This EPIC
| ID | Type | SoT File | Description | Status | Date Modified |
|----|------|----------|-------------|--------|---------------|
| API-045 | Endpoint | API_CONTRACTS.md | OCR upload | ✅ | 2025-11-08 |

### IDs Created This EPIC
| ID | Type | SoT File | Description | Status | Date Created |
|----|------|----------|-------------|--------|--------------|
| API-046 | Endpoint | API_CONTRACTS.md | Retry OCR | ✅ | 2025-11-08 |

### ID Impact Map
**Primary IDs**: API-045, API-046
**Affected IDs**: UJ-101, TEST-301, TEST-302
**Referenced IDs**: BR-112, DEP-027, DBT-018
```

## Bidirectional Cross-References

**Critical Rule**: If A references B, then B MUST reference A.

**Example**:
```markdown
# API_CONTRACTS.md
## API-045: Create Product
Enforces: [BR-001](BUSINESS_RULES.md#br-001)

# BUSINESS_RULES.md
## BR-001: Free Tier Limit
Enforced by: [API-045](API_CONTRACTS.md#api-045)
```

## Benefits

### For AI Agents
- **Context Loading**: <1 minute vs 5-10 minutes
- **Precision**: Load only relevant IDs instead of entire documents
- **Traceability**: Follow dependency chains automatically
- **Validation**: Check all references exist before implementing

### For Humans
- **Single Source of Truth**: Specifications live in ONE place
- **Impact Analysis**: See all dependencies instantly
- **Maintenance**: Update once, referenced everywhere
- **Onboarding**: Follow ID trails to understand system

### For Quality
- **Consistency**: No duplicate, conflicting specifications
- **Completeness**: Cross-reference index shows coverage
- **Traceability**: Every requirement traced to implementation
- **Automation**: Scripts can validate ID integrity

## Common Patterns

### Pattern 1: API Implements Business Rule
```markdown
BR-001 (rule definition)
  └─→ API-045 (enforcement)
      └─→ TEST-301 (validation)
```

### Pattern 2: User Journey Across Multiple Systems
```markdown
UJ-101 (journey specification)
  ├─→ API-045 (step 1 backend)
  ├─→ API-046 (step 2 backend)
  ├─→ DES-042 (step 1 UI)
  ├─→ BR-001 (rule enforced)
  └─→ TEST-303 (E2E validation)
```

### Pattern 3: Customer Feedback → Implementation
```markdown
CFD-089 (user request)
  └─→ UJ-105 (new journey created)
      ├─→ API-050 (new endpoint)
      ├─→ DBT-025 (new table)
      └─→ TEST-310 (validation)
```

## Automation

### Auto-Generated Registry
```bash
# Generate central ID registry from all SoT files
npm run codex:sync-registry

# Output: .codex/ID-REGISTRY.md
# - Complete list of all IDs
# - Cross-reference validation
# - Orphaned ID detection
# - Duplicate ID detection
```

### Validation Scripts
```bash
# Validate bidirectional references
npm run codex:validate-references

# Check for broken links
npm run codex:check-links

# Find orphaned IDs (no references)
npm run codex:find-orphans
```

## Migration Strategy

### For Existing Products

**Step 1**: Start with Business Rules
- Extract all business constraints from Claude.md
- Assign BR-XXX IDs
- Create BUSINESS_RULES.md

**Step 2**: Document APIs
- List all endpoints
- Assign API-XXX IDs
- Create API_CONTRACTS.md
- Link to BR-XXX where rules are enforced

**Step 3**: Map User Journeys
- Identify core user flows
- Assign UJ-XXX IDs
- Create USER-JOURNEYS.md
- Link to API-XXX and BR-XXX

**Step 4**: Expand to Other Types
- Add remaining ID types as needed
- Maintain bidirectional references
- Update README with active IDs

### For New Products

**Start with EPIC-00**:
- Begin creating IDs from day one
- EPIC-00 establishes first BR-XXX, API-XXX, DBT-XXX
- Each subsequent EPIC adds to the graph
- Natural accumulation of ID ecosystem

## Best Practices

### DO
- ✅ Assign IDs to "reference-worthy" artifacts (referenced ≥2 times)
- ✅ Use sequential numbering (BR-001, BR-002, BR-003)
- ✅ Maintain bidirectional references always
- ✅ Track ID changes in EPIC Section 3A
- ✅ Update README with active IDs for quick navigation
- ✅ Use automation to validate ID integrity

### DON'T
- ❌ Create IDs for every tiny detail (over-granularity)
- ❌ Skip the bidirectional reference
- ❌ Duplicate specifications (use ID references instead)
- ❌ Renumber IDs when removing items (mark as deprecated)
- ❌ Create IDs in the "3" files (Claude.md, PRD.md, README.md)
- ❌ Forget to update cross-reference sections

## Troubleshooting

### Broken Reference
**Symptom**: Link to ID that doesn't exist
**Fix**: Either create the missing ID or remove the reference

### Orphaned ID
**Symptom**: ID exists but has no references
**Fix**: Either add references or mark as deprecated

### Duplicate Specification
**Symptom**: Same information in multiple places
**Fix**: Keep only one (in SoT file), replace others with ID references

### Missing Bidirectional Reference
**Symptom**: A references B, but B doesn't reference A
**Fix**: Add the missing reference to maintain integrity

## Templates Available

All templates include ID system integration:
- **templates/epics/EPIC-template.md** - Section 3A for ID tracking
- **templates/product/README-template.md** - Active IDs navigation
- **templates/source-of-truth/USER-JOURNEYS-template.md**
- **templates/source-of-truth/BUSINESS_RULES-template.md**
- **templates/source-of-truth/API_CONTRACTS-template.md**
- **templates/source-of-truth/ACTUAL-SCHEMA-template.md**
- **templates/source-of-truth/customer-feedback-template.md**

## Learn More

- [Three-File Discipline](../CLAUDE.md#documentation-discipline)
- [EPIC Template](../templates/epics/EPIC-template.md)
- [Source of Truth Templates](../templates/source-of-truth/)
- [README Template](../templates/product/README-template.md)
