# Cross-Reference Patterns

**Purpose**: Valid and invalid ID relationship patterns for maintaining SoT integrity.

---

## Valid Reference Patterns

### Pattern 1: Evidence → Decision (CFD → BR)

**Relationship**: Customer feedback informs business rules

**Example**:
```
CFD-089: "Users request dark mode" (500+ support tickets)
  ↓
BR-091: "Provide dark mode toggle" (decision based on demand)
```

**Validation**: ✅ Valid (evidence drives decisions)

---

### Pattern 2: Decision → Feature (BR → FEA)

**Relationship**: Business rules drive feature requirements

**Example**:
```
BR-045: "Free tier limited to 100 API calls/day"
  ↓
FEA-023: "Rate limiting dashboard" (shows usage vs limit)
```

**Validation**: ✅ Valid (rules require features)

---

### Pattern 3: Feature → Implementation (FEA → API, DBT)

**Relationship**: Features implemented by APIs and data models

**Example**:
```
FEA-067: "User can export project data"
  ↓
API-034: "GET /api/projects/:id/export"
  ↓
DBT-012: "project_exports table" (stores export history)
```

**Validation**: ✅ Valid (features need implementation)

---

### Pattern 4: Persona → Journey (PER → UJ)

**Relationship**: User journeys designed for specific personas

**Example**:
```
PER-101: "Power User (Designer at agency)"
  ↓
UJ-045: "Bulk asset import workflow" (designed for power users)
```

**Validation**: ✅ Valid (journeys tailored to personas)

---

### Pattern 5: Journey → Feature (UJ → FEA)

**Relationship**: User journeys enabled by features

**Example**:
```
UJ-023: "User signs up and creates first project"
  ↓
FEA-012: "Project creation wizard"
FEA-015: "Template gallery"
```

**Validation**: ✅ Valid (journeys use features)

---

## Invalid Reference Patterns (Anti-Patterns)

### Anti-Pattern 1: Decision → Evidence (BR → CFD)

**Why Invalid**: Decisions don't create evidence (backward causality)

**Bad Example**:
```
BR-078: "We'll build dark mode"
  ↓
CFD-089: "Users want dark mode" ❌
```

**Fix**: Reverse relationship (CFD-089 → BR-078)

---

### Anti-Pattern 2: Implementation → Feature (API → FEA)

**Why Invalid**: APIs don't drive features (backward causality)

**Bad Example**:
```
API-045: "GET /api/users/:id"
  ↓
FEA-023: "User profile page" ❌
```

**Fix**: Reverse (FEA-023 → API-045)

---

### Anti-Pattern 3: Circular References

**Why Invalid**: Creates dependency loop (can't resolve)

**Bad Example**:
```
BR-045 references FEA-023
FEA-023 references BR-045 ❌ (circular)
```

**Fix**: One-way relationship (BR-045 → FEA-023 only)

---

## Cross-Reference Validation Rules

### Rule 1: Hierarchy Direction

**Valid**: Top → Down (abstract → concrete)
```
CFD (problem) → BR (decision) → FEA (feature) → API (implementation)
```

**Invalid**: Bottom → Up (concrete → abstract)

---

### Rule 2: No Orphans

**Valid**: All IDs reference or are referenced by at least one other ID

**Invalid**:
```
BR-099: "Some random rule" (no CFD, no FEA) ❌ Orphan
```

**Exception**: New IDs can be orphans temporarily (will be linked later)

---

### Rule 3: Reference Types Match

**Valid**: Feature references API (both implementation layer)

**Invalid**: Feature references Persona (different layers)
- Use: Feature → Journey → Persona (indirect relationship)

---

## Complex Reference Patterns

### Pattern: Problem → Solution → Validation

**Flow**:
```
CFD-089 (Pain): "Onboarding takes 15 minutes"
  ↓
BR-091 (Decision): "Onboarding must complete in < 5 min"
  ↓
FEA-034 (Solution): "Progressive onboarding wizard"
  ↓
UJ-012 (Journey): "New user onboarding"
  ↓
KPI-015 (Validation): "90% complete onboarding in < 5 min"
```

**Validation**: ✅ Valid (complete traceability)

---

### Pattern: Competitive → Positioning → Feature

**Flow**:
```
CFD-067 (Competitive): "Competitor A has feature X"
  ↓
BR-089 (Positioning): "We'll unbundle feature X, do it 10x better"
  ↓
FEA-045 (Feature): "Specialized version of feature X"
```

**Validation**: ✅ Valid (competitive insights drive strategy)

---

## Cross-Reference Checklist

When creating new ID:

- [ ] **Identify Upstream**: What informed this ID?
- [ ] **Identify Downstream**: What will this ID inform?
- [ ] **Validate Direction**: Is relationship top-down?
- [ ] **Check for Duplicates**: Does existing ID cover this?
- [ ] **Verify Existence**: Do all referenced IDs exist?

---

*Reference: Use these patterns when validating ID cross-references in `ghm-id-register` skill.*
