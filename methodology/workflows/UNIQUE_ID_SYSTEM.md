---
version: 1.0
purpose: Comprehensive guide to the Unique ID system and how it integrates with 3+1+SoT+Temp documentation framework
last_updated: 2025-11-09
authority: Defines where IDs live, how they're created, and how they're used across all documentation
---

# Unique ID System Guide

## Overview

The Unique ID system assigns durable, globally unique identifiers to every meaningful artifact in your product documentation. This transforms documentation from duplicate prose into a precise knowledge graph where specifications live in ONE place and are referenced everywhere else.

**Core Benefit**: AI agents load context in <1 minute vs 5-10 minutes of full-document scanning.

## The Problem We're Solving

### Without IDs (Duplicate Prose)

```markdown
# PRD.md
Free tier users can create up to 3 products. This is enforced server-side
and validated in the UI. Users see an upgrade prompt when limit reached.

# API_CONTRACTS.md
POST /api/products validates that free tier users don't exceed 3 products.
Returns 422 error with upgrade prompt when limit exceeded.

# USER_JOURNEYS.md
When user adds a product, system checks if they're on free tier. If they
have 3 products already, show upgrade modal. Otherwise proceed.

# testing_playbook.md
TEST-301: Verify free tier users limited to 3 products
TEST-302: Verify upgrade prompt appears at limit
```

**Problems**:
- Same rule duplicated 4+ times
- Changes require updating multiple files
- Easy to miss updates, creating inconsistency
- AI agents must read everything to find all references

### With IDs (Single Source of Truth)

```markdown
# BUSINESS_RULES.md (Source of Truth)
## BR-001: Free Tier Product Limit
**Rule**: Free tier users MUST be limited to exactly 3 products.
**Enforcement**: Server-side validation required
**User Experience**: Show upgrade prompt when limit reached
**Error Code**: BR_001_VIOLATION

# API_CONTRACTS.md (References BR-001)
POST /api/products enforces [BR-001](BUSINESS_RULES.md#br-001)

# USER_JOURNEYS.md (References BR-001)
Step 3: Validate [BR-001](BUSINESS_RULES.md#br-001)

# testing_playbook.md (References BR-001)
TEST-301: Validates [BR-001](BUSINESS_RULES.md#br-001) compliance
TEST-302: Validates [BR-001](BUSINESS_RULES.md#br-001) error handling
```

**Benefits**:
- Rule specified ONCE with full detail
- All other files reference the ID
- Changes happen in one place
- AI agents load precise context via ID

## Integration with 3+1+SoT+Temp Framework

### The Framework Layers

```
┌─────────────────────────────────────────────────────────────┐
│                    Navigation Layer                         │
│                      (The "3")                              │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │  Claude.md   │  │   PRD.md     │  │  README.md   │     │
│  │ Process rules│  │ Requirements │  │  Dashboard   │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│  Role: Provide context, POINT TO IDs, show active work    │
│  IDs: NEVER create, only reference                         │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                   Change Tracking Layer                     │
│                      (The "+1")                             │
│               ┌──────────────────────┐                      │
│               │   Current EPIC       │                      │
│               │  EPIC-XX-{name}.md   │                      │
│               └──────────────────────┘                      │
│  Role: Track which IDs modified/created during development │
│  IDs: Section 3A documents all ID changes                  │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                  Reference Library Layer                    │
│                      (SoT Files)                            │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │USER_JOURNEYS │  │BUSINESS_RULES│  │API_CONTRACTS │     │
│  │   (UJ-XXX)   │  │   (BR-XXX)   │  │  (API-XXX)   │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐     │
│  │ACTUAL_SCHEMA │  │testing-play. │  │customer-feed.│     │
│  │  (DBT-XXX)   │  │  (TEST-XXX)  │  │  (CFD-XXX)   │     │
│  └──────────────┘  └──────────────┘  └──────────────┘     │
│  Role: CREATE and MAINTAIN IDs with full specifications   │
│  IDs: Each file type owns specific ID prefix               │
└─────────────────────────────────────────────────────────────┘
                              ↓
┌─────────────────────────────────────────────────────────────┐
│                    Temporary Storage                        │
│                      (temp/ folder)                         │
│  Role: Work-in-progress content that will be extracted to  │
│  SoT files when validated                                  │
│  IDs: May propose new IDs, finalized when moved to SoT     │
└─────────────────────────────────────────────────────────────┘
```

### Layer Responsibilities

#### 1. Navigation Layer (The "3") - REFERENCE ONLY

**Files**: `Claude.md`, `PRD.md`, `README.md`

**Role**:
- Provide high-level context and navigation
- Point readers to detailed specifications in SoT files
- Show current state and active work
- Enable quick orientation for AI agents and humans

**ID Behavior**:
- ✅ **Reference** IDs via markdown links: `[BR-001](BUSINESS_RULES.md#br-001)`
- ✅ **Show active IDs** in README for quick navigation
- ❌ **NEVER create** new IDs (no ID ownership)
- ❌ **NEVER duplicate** specifications (link instead)

**Example (README.md)**:
```markdown
## 📍 Active IDs in Scope

**Modified This EPIC**:
- [UJ-101](USER_JOURNEYS.md#uj-101) - Product Onboarding (improving)
- [API-045](API_CONTRACTS.md#api-045) - Create Product (modified)

**Created This EPIC**:
- [API-046](API_CONTRACTS.md#api-046) - Retry Failed OCR (new)

**Key Business Rules**:
- [BR-001](BUSINESS_RULES.md#br-001) - Free Tier Limit
- [BR-112](BUSINESS_RULES.md#br-112) - Server-side Validation Required
```

**Example (PRD.md)**:
```markdown
## R3: Household Collaboration

**User Story**: Families need to share product information across members.

**Business Rules**:
- [BR-045](BUSINESS_RULES.md#br-045) - Maximum 4 household members
- [BR-046](BUSINESS_RULES.md#br-046) - Real-time sync required

**User Journeys**:
- [UJ-201](USER_JOURNEYS.md#uj-201) - Invite family member
- [UJ-202](USER_JOURNEYS.md#uj-202) - Accept household invitation

**APIs Required**:
- [API-150](API_CONTRACTS.md#api-150) - Create household
- [API-151](API_CONTRACTS.md#api-151) - Send invitation
```

#### 2. Change Tracking Layer (The "+1") - TRACK CHANGES

**Files**: Current EPIC (e.g., `epics/🚧 EPIC-03-authentication.md`)

**Role**:
- Document active development work
- Track which IDs are being modified or created
- Map dependencies and impact
- Validate cross-references before completion

**ID Behavior**:
- ✅ **Track** all ID changes in Section 3A
- ✅ **Document** impact map and dependency chains
- ✅ **Validate** bidirectional references
- ❌ **Don't create** permanent IDs (propose, finalize in SoT)

**Example (EPIC Section 3A)**:
```markdown
## 3A. ID Tracking (Knowledge Graph)

### IDs Modified This EPIC

| ID | Type | SoT File | Description | Status | Date Modified |
|----|------|----------|-------------|--------|---------------|
| API-045 | Endpoint | API_CONTRACTS.md | Create Product | ✅ | 2025-11-08 |
| TEST-301 | Test | testing_playbook.md | Product Creation | 🚧 | - |

### IDs Created This EPIC

| ID | Type | SoT File | Description | Status | Date Created | Related IDs |
|----|------|----------|-------------|--------|--------------|-------------|
| API-046 | Endpoint | API_CONTRACTS.md | Retry Failed OCR | ✅ | 2025-11-08 | API-045, TEST-303 |
| BR-118 | Rule | BUSINESS_RULES.md | OCR Retry Limit | ✅ | 2025-11-08 | API-046 |
| TEST-303 | Test | testing_playbook.md | Retry Logic | ✅ | 2025-11-09 | API-046, BR-118 |

### ID Impact Map

**Primary Changes**: API-045, API-046, BR-118
**Downstream Impact**: UJ-101 (improved), TEST-301 (updated), TEST-302 (updated)
**Dependencies**: DEP-027 (Google Document AI), DBT-018 (products table)

### ID Dependency Chain

```
BR-118 (new: OCR retry limit)
  └─→ API-046 (new: retry endpoint)
      ├─→ API-045 (modified: original endpoint)
      ├─→ TEST-303 (new: validates retry)
      ├─→ UJ-101 (improved: better UX)
      └─→ DEP-027 (uses: Google Document AI)
```

### Cross-Reference Validation

- [x] All modified IDs have bidirectional references updated
- [x] All created IDs added to their SoT files with complete metadata
- [x] All referenced IDs exist (BR-118, API-045, API-046, TEST-303, UJ-101, DEP-027, DBT-018)
- [x] README.md updated with active IDs
```

#### 3. Reference Library (SoT Files) - CREATE & MAINTAIN

**Files**:
- `USER_JOURNEYS.md` (UJ-XXX)
- `BUSINESS_RULES.md` (BR-XXX)
- `API_CONTRACTS.md` (API-XXX)
- `ACTUAL_SCHEMA.md` (DBT-XXX)
- `testing_playbook.md` (TEST-XXX)
- `deployment_playbook.md` (DEP-XXX)
- `{product}-DesignBrief.md` (DES-XXX)
- `customer_feedback.md` (CFD-XXX)

**Role**:
- Create new IDs with unique identifiers
- Maintain full specifications for each ID
- Own the authoritative definition
- Maintain bidirectional cross-references

**ID Behavior**:
- ✅ **Create** new IDs following prefix conventions
- ✅ **Specify** complete details (metadata, description, relationships)
- ✅ **Maintain** bidirectional references to all related IDs
- ✅ **Update** when IDs are modified
- ✅ **Deprecate** (don't delete) when IDs become obsolete

**Example (BUSINESS_RULES.md)**:
```markdown
## BR-001: Free Tier Product Limit

**ID**: BR-001
**Category**: Pricing & Entitlements
**Status**: Active
**Severity**: Critical
**Created**: 2025-10-15
**Last Updated**: 2025-11-08

### Rule Statement

Free tier users MUST be limited to exactly 3 products. Any attempt to create
a 4th product MUST be blocked with an upgrade prompt.

### Enforcement Points

**Primary**: Server-side validation in product creation endpoint
- Location: [API-045](API_CONTRACTS.md#api-045)
- Method: Server-side
- Timing: On product creation request

### Related IDs

**Enforced By**:
- [API-045](API_CONTRACTS.md#api-045) - Create Product endpoint
- [API-012](API_CONTRACTS.md#api-012) - User entitlement check

**Affects User Journeys**:
- [UJ-101](USER_JOURNEYS.md#uj-101) - Product Onboarding
- [UJ-105](USER_JOURNEYS.md#uj-105) - Add Additional Product

**Validated By**:
- [TEST-301](testing_playbook.md#test-301) - Free tier limit enforcement
- [TEST-302](testing_playbook.md#test-302) - Upgrade prompt display

**Customer Feedback**:
- [CFD-023](customer_feedback.md#cfd-023) - Users confused by limit
```

**Example (API_CONTRACTS.md)**:
```markdown
## API-045: Create Product

**ID**: API-045
**Method**: POST
**Path**: `/api/v1/products`
**Status**: Active
**Created**: 2025-10-15
**Last Updated**: 2025-11-08

### Business Rules Enforced

- [BR-001](BUSINESS_RULES.md#br-001) - Free tier product limit
- [BR-012](BUSINESS_RULES.md#br-012) - Server-side validation required
- [BR-034](BUSINESS_RULES.md#br-034) - Product name uniqueness

### Used By

- [UJ-101](USER_JOURNEYS.md#uj-101) - Product Onboarding (step 3)
- [UJ-105](USER_JOURNEYS.md#uj-105) - Add Additional Product (step 2)

### Database Operations

- [DBT-018](ACTUAL_SCHEMA.md#dbt-018) - products (INSERT)
- [DBT-002](ACTUAL_SCHEMA.md#dbt-002) - users (SELECT)

### Validated By

- [TEST-301](testing_playbook.md#test-301) - Happy path
- [TEST-302](testing_playbook.md#test-302) - Free tier limit
- [TEST-305](testing_playbook.md#test-305) - Validation errors
```

#### 4. Temporary Storage (temp/) - WORK IN PROGRESS

**Files**: `temp/*.md`

**Role**:
- Capture work-in-progress thinking
- Develop and refine specifications
- Experiment with structures
- Stage content before finalizing

**ID Behavior**:
- ✅ **Propose** new IDs during exploration
- ✅ **Reference** existing IDs from SoT files
- ✅ **Draft** full specifications before moving to SoT
- ❌ **Not authoritative** until extracted to SoT
- ❌ **Don't reference** temp files from permanent docs

**Lifecycle**:
1. Create temp file for exploration
2. Develop content and propose IDs
3. Validate with team/Product Owner
4. Extract finalized content to appropriate SoT file(s)
5. Archive temp file (don't delete)
6. Update EPIC Phase E checklist

**Example (temp/feature-household-sharing.md)**:
```markdown
# Household Sharing Feature Exploration

## Proposed Business Rules

**BR-045 (PROPOSED)**: Maximum 4 household members
- Rationale: Technical limit due to sync complexity
- Status: Needs Product Owner approval

**BR-046 (PROPOSED)**: Real-time sync required
- Rationale: Core value proposition
- Status: Needs architecture validation

## Proposed User Journeys

**UJ-201 (PROPOSED)**: Invite Family Member
- Steps: [draft steps here]
- Status: Needs UX review

## Proposed APIs

**API-150 (PROPOSED)**: Create Household
- Enforces: BR-045 (pending)
- Status: Needs schema design first

---

**Next Steps**:
1. Get Product Owner approval on BR-045, BR-046
2. Finalize UJ-201 with UX team
3. Design schema for households (DBT-XXX)
4. Extract approved content to SoT files
5. Archive this temp file
```

## ID Types and Prefixes

| Prefix | Type | SoT File | Description | Example |
|--------|------|----------|-------------|---------|
| **UJ-XXX** | User Journey | USER_JOURNEYS.md | Complete user flows and experiences | UJ-101: Product Onboarding |
| **BR-XXX** | Business Rule | BUSINESS_RULES.md | Business constraints and policies | BR-001: Free Tier Limit |
| **API-XXX** | API Endpoint | API_CONTRACTS.md | API specifications and contracts | API-045: Create Product |
| **DBT-XXX** | Database Table | ACTUAL_SCHEMA.md | Schema and database objects | DBT-018: products |
| **TEST-XXX** | Test Case | testing_playbook.md | Test specifications and validation | TEST-301: Validates BR-001 |
| **DEP-XXX** | Deployment | deployment_playbook.md | Infrastructure and deployment configs | DEP-027: Railway Config |
| **DES-XXX** | Design | {product}-DesignBrief.md | UI/UX components and patterns | DES-042: Product Card |
| **CFD-XXX** | Feedback | customer_feedback.md | Customer insights and requests | CFD-089: Sharing Request |
| **SEC-XXX** | Security | security_playbook.md | Security controls and policies | SEC-012: Rate Limiting |
| **PERF-XXX** | Performance | performance_playbook.md | Performance targets and benchmarks | PERF-005: API <200ms |

## Workflow: Creating and Using IDs

### During Development (EPIC Lifecycle)

#### Phase A: Planning
1. **Identify Scope**: Determine which IDs will be affected
2. **Check Existing IDs**: Review README Active IDs and relevant SoT files
3. **Plan New IDs**: List IDs that need to be created
4. **Start EPIC Section 3A**: Initialize ID tracking tables

#### Phase B: Implementation
1. **Create IDs in SoT Files**: Add new IDs with complete specifications
2. **Update Modified IDs**: Edit existing IDs in SoT files
3. **Maintain Bidirectional References**: Ensure all references are mutual
4. **Update EPIC Section 3A**: Track all ID changes in real-time

#### Phase C: Testing
1. **Reference IDs in Tests**: Link test cases to IDs they validate
2. **Validate Cross-References**: Ensure all ID links resolve correctly
3. **Check Impact Map**: Verify all affected IDs are identified

#### Phase E: Documentation
1. **Update README Active IDs**: Show current scope
2. **Validate Bidirectional References**: Complete checklist in Section 3A
3. **Auto-Generate Registry**: Run `npm run codex:sync-registry` (if available)
4. **Archive Temp Files**: Extract to SoT, archive originals

### Example: Adding a New Feature

**Scenario**: Add "Retry Failed OCR" feature

**Step 1 - Planning (EPIC Phase A)**:
```markdown
## 3A. ID Tracking (Knowledge Graph)

### Planning Notes
Will need to:
- Modify: API-045 (add retry logic)
- Create: API-046 (new retry endpoint)
- Create: BR-118 (retry limit rule)
- Create: TEST-303 (validate retry)
- Update: UJ-101 (improved UX)
```

**Step 2 - Create BR-118 in BUSINESS_RULES.md**:
```markdown
## BR-118: OCR Retry Limit

**ID**: BR-118
**Status**: Active
**Created**: 2025-11-08

### Rule Statement
Failed OCR operations MAY be retried up to 3 times. After 3 failures,
user MUST be prompted to enter data manually.

### Related IDs
**Enforced By**: [API-046](API_CONTRACTS.md#api-046) (will create)
**Affects**: [UJ-101](USER_JOURNEYS.md#uj-101) (will update)
```

**Step 3 - Create API-046 in API_CONTRACTS.md**:
```markdown
## API-046: Retry Failed OCR

**ID**: API-046
**Method**: POST
**Path**: `/api/v1/ocr/retry`
**Status**: Active
**Created**: 2025-11-08

### Business Rules Enforced
- [BR-118](BUSINESS_RULES.md#br-118) - OCR retry limit

### Related APIs
- [API-045](API_CONTRACTS.md#api-045) - Original OCR endpoint

### Validated By
- [TEST-303](testing_playbook.md#test-303) (will create)
```

**Step 4 - Update API-045 in API_CONTRACTS.md**:
```markdown
## API-045: Process OCR Upload

...existing content...

### Related APIs
- [API-046](API_CONTRACTS.md#api-046) - Retry endpoint (NEW)

**Last Updated**: 2025-11-08
```

**Step 5 - Update UJ-101 in USER_JOURNEYS.md**:
```markdown
## UJ-101: Product Onboarding

...existing steps...

3. **Process Receipt Image**
   - System Response: Process via [API-045](API_CONTRACTS.md#api-045)
   - Error Flow: If failed, offer retry via [API-046](API_CONTRACTS.md#api-046)
   - Business Rule: [BR-118](BUSINESS_RULES.md#br-118) limits to 3 retries

**Last Updated**: 2025-11-08
```

**Step 6 - Update EPIC Section 3A**:
```markdown
### IDs Modified This EPIC
| ID | Type | SoT File | Description | Status | Date Modified |
|----|------|----------|-------------|--------|---------------|
| API-045 | Endpoint | API_CONTRACTS.md | OCR upload | ✅ | 2025-11-08 |
| UJ-101 | Journey | USER_JOURNEYS.md | Onboarding | ✅ | 2025-11-08 |

### IDs Created This EPIC
| ID | Type | SoT File | Description | Status | Date Created | Related IDs |
|----|------|----------|-------------|--------|--------------|-------------|
| API-046 | Endpoint | API_CONTRACTS.md | Retry OCR | ✅ | 2025-11-08 | API-045, BR-118, TEST-303 |
| BR-118 | Rule | BUSINESS_RULES.md | Retry limit | ✅ | 2025-11-08 | API-046 |
| TEST-303 | Test | testing_playbook.md | Retry validation | ✅ | 2025-11-09 | API-046, BR-118 |
```

**Step 7 - Update README.md Active IDs**:
```markdown
## 📍 Active IDs in Scope

**Modified This EPIC**:
- [API-045](API_CONTRACTS.md#api-045) - OCR Upload (enhanced with retry)
- [UJ-101](USER_JOURNEYS.md#uj-101) - Onboarding (improved error handling)

**Created This EPIC**:
- [API-046](API_CONTRACTS.md#api-046) - Retry Failed OCR (new)
- [BR-118](BUSINESS_RULES.md#br-118) - OCR Retry Limit (new)
- [TEST-303](testing_playbook.md#test-303) - Retry Validation (new)
```

## Bidirectional Cross-References

**Critical Rule**: If A references B, then B MUST reference A.

### Why Bidirectional References Matter

**Forward Reference Only** (Incomplete):
```markdown
# API_CONTRACTS.md
## API-045: Create Product
Enforces: [BR-001](BUSINESS_RULES.md#br-001)

# BUSINESS_RULES.md
## BR-001: Free Tier Limit
{specification}
```

**Problem**: You can navigate API → BR, but not BR → API. Impact analysis is incomplete.

**Bidirectional References** (Complete):
```markdown
# API_CONTRACTS.md
## API-045: Create Product
Enforces: [BR-001](BUSINESS_RULES.md#br-001)

# BUSINESS_RULES.md
## BR-001: Free Tier Limit
{specification}

### Related IDs
**Enforced By**:
- [API-045](API_CONTRACTS.md#api-045) - Create Product endpoint
```

**Benefit**: You can navigate in both directions. Complete impact analysis.

### Validation Checklist

Before completing an EPIC, validate all bidirectional references:

```markdown
### Cross-Reference Validation

- [ ] All modified IDs have bidirectional references updated
- [ ] All created IDs added to ID_REGISTRY.md (auto-sync)
- [ ] All referenced IDs exist in their SoT files
- [ ] README.md updated with active IDs from this EPIC
```

## Progressive Adoption Strategy

### Phase 1: Core IDs (Weeks 1-2)

Start with the 5 most impactful ID types:

1. **BR-XXX** (Business Rules)
   - Extract from Claude.md and PRD.md
   - Create BUSINESS_RULES.md
   - Assign IDs to critical constraints

2. **API-XXX** (API Endpoints)
   - List all existing endpoints
   - Create API_CONTRACTS.md
   - Link to BR-XXX for rules

3. **UJ-XXX** (User Journeys)
   - Map core user flows
   - Create USER_JOURNEYS.md
   - Link to API-XXX and BR-XXX

4. **DBT-XXX** (Database Tables)
   - Document schema
   - Create ACTUAL_SCHEMA.md
   - Link to API-XXX

5. **TEST-XXX** (Tests)
   - Catalog test cases
   - Update testing_playbook.md
   - Link to BR-XXX, API-XXX, UJ-XXX

### Phase 2: Quality & Operations (Weeks 3-4)

Add as complexity grows:

6. **DEP-XXX** (Deployment)
   - Document infrastructure
   - Create/update deployment_playbook.md
   - Link to API-XXX, DBT-XXX

7. **CFD-XXX** (Customer Feedback)
   - Catalog user requests
   - Create customer_feedback.md
   - Link to UJ-XXX, BR-XXX

### Phase 3: Advanced IDs (Ongoing)

Add for mature products:

8. **DES-XXX** (Design Components)
9. **SEC-XXX** (Security Controls)
10. **PERF-XXX** (Performance Targets)

## Automation & Tooling

### Auto-Generated Registry

```bash
# Generate central ID registry from all SoT files
npm run codex:sync-registry
```

**Output**: `.codex/ID_REGISTRY.md`
- Complete alphabetical list of all IDs
- Cross-reference count (how many places reference this ID)
- Orphaned ID detection (IDs with zero references)
- Duplicate ID detection (same ID used twice)

### Validation Scripts

```bash
# Validate bidirectional references
npm run codex:validate-references
# Output: List of one-way references that need completion

# Check for broken links
npm run codex:check-links
# Output: List of IDs referenced but not found

# Find orphaned IDs
npm run codex:find-orphans
# Output: IDs that exist but have no references
```

## Best Practices

### DO

✅ **Assign IDs to reference-worthy artifacts**
- If referenced ≥2 times, it deserves an ID
- Prevents duplicate specifications

✅ **Use sequential numbering**
- BR-001, BR-002, BR-003 (simple)
- Don't overthink number ranges

✅ **Maintain bidirectional references**
- Every reference must go both ways
- Enables complete impact analysis

✅ **Track ID changes in EPICs**
- Section 3A captures all modifications
- Provides audit trail

✅ **Update README with active IDs**
- Quick navigation for AI agents
- Shows current scope at a glance

✅ **Deprecate, don't delete**
- Mark as [DEPRECATED], don't renumber
- Preserves history and references

### DON'T

❌ **Create IDs for every tiny detail**
- Avoid over-granularity
- Not everything needs an ID

❌ **Skip bidirectional references**
- One-way references break impact analysis
- Always complete the loop

❌ **Duplicate specifications**
- Write once in SoT file
- Reference ID everywhere else

❌ **Renumber IDs**
- Numbers are permanent
- Gaps are OK (deprecated IDs)

❌ **Create IDs in "3" files**
- Claude.md, PRD.md, README.md reference only
- IDs live in SoT files

❌ **Reference temp files**
- Temp content is not authoritative
- Extract to SoT before referencing

## Migration Guide

### For Existing Products

**Week 1: Business Rules**
1. Read Claude.md and PRD.md
2. Extract all business constraints
3. Create BUSINESS_RULES.md
4. Assign BR-XXX IDs
5. Replace duplicates with references

**Week 2: APIs and User Journeys**
1. List all API endpoints
2. Create API_CONTRACTS.md with API-XXX IDs
3. Link to BR-XXX where rules enforced
4. Map core user flows
5. Create USER_JOURNEYS.md with UJ-XXX IDs
6. Link to API-XXX and BR-XXX

**Week 3: Database and Tests**
1. Document schema
2. Create ACTUAL_SCHEMA.md with DBT-XXX IDs
3. Catalog test cases
4. Update testing_playbook.md with TEST-XXX IDs
5. Link tests to BR-XXX, API-XXX, UJ-XXX

**Week 4: Refinement**
1. Update README with active IDs
2. Validate bidirectional references
3. Run automation scripts (if available)
4. Update Claude.md and PRD.md to reference IDs

### For New Products

Start with IDs from EPIC-00:
1. EPIC-00 creates first BR-XXX, API-XXX, DBT-XXX
2. Each subsequent EPIC adds to the graph
3. Natural accumulation of ID ecosystem
4. No migration needed

## Troubleshooting

### Broken Reference
**Symptom**: `[BR-045](BUSINESS_RULES.md#br-045)` links to nothing

**Fix**:
1. Check if ID exists: Search BUSINESS_RULES.md for "BR-045"
2. If missing: Create the ID or remove the reference
3. If exists: Fix the markdown anchor format

### Orphaned ID
**Symptom**: BR-045 exists but has zero references

**Fix**:
1. Determine if ID is actually used
2. If yes: Add missing references
3. If no: Mark as [DEPRECATED] with reason

### Duplicate Specification
**Symptom**: Same rule text in multiple files

**Fix**:
1. Choose authoritative location (SoT file)
2. Keep full specification there only
3. Replace all duplicates with ID references

### Missing Bidirectional Reference
**Symptom**: API-045 references BR-001, but BR-001 doesn't reference API-045

**Fix**:
1. Add to BR-001:
```markdown
### Related IDs
**Enforced By**:
- [API-045](API_CONTRACTS.md#api-045) - Create Product endpoint
```

## Templates and Tools

All templates include integrated ID system support:

- **[EPIC-template.md](../templates/EPIC-template.md)** - Section 3A for ID tracking
- **[README-template.md](../templates/README-template.md)** - Active IDs section
- **[USER_JOURNEYS-template.md](../templates/USER_JOURNEYS-template.md)** - UJ-XXX structure
- **[BUSINESS_RULES-template.md](../templates/BUSINESS_RULES-template.md)** - BR-XXX structure
- **[API_CONTRACTS-template.md](../templates/API_CONTRACTS-template.md)** - API-XXX structure
- **[ACTUAL_SCHEMA-template.md](../templates/ACTUAL_SCHEMA-template.md)** - DBT-XXX structure
- **[customer_feedback-template.md](../templates/customer_feedback-template.md)** - CFD-XXX structure

## Related Documentation

- [Three-File Discipline](../CLAUDE.md#documentation-discipline)
- [3+3 Pattern](../CLAUDE.md#the-33-pattern)
- [EPIC Workflow](WORKFLOW-PRD-DEVELOPMENT.md)
- [Temp File Lifecycle](WORKFLOW-PRD-DEVELOPMENT.md#temp-file-lifecycle-enforcement)

---

*This guide integrates the Unique ID system with the 3+1+SoT+Temp documentation framework to create a precise, maintainable knowledge graph.*
