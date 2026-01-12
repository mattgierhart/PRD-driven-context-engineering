---
version: 1.0
purpose: Source of Truth for technology choices and architecture decisions (ADR-style).
id_prefix: TECH-XXX, ARC-XXX
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs here are referenced by PRD.md, EPICs, and code
---

# Technical Decisions (SoT File)

> **Purpose**: Record technology selections and architecture decisions with rationale.
> **ID Prefixes**: TECH-XXX (stack decisions), ARC-XXX (architecture decisions)
> **Status**: Active SoT file
> **Cross-References**: Referenced by PRD.md v0.5-v0.6, SoT.API_CONTRACTS.md, EPICs

## Navigation by Category

**Stack Decisions** (TECH-001 to TECH-099):

- [TECH-001](#tech-001-decision-name) - {Technology decision}

**Architecture Decisions** (ARC-001 to ARC-099):

- [ARC-001](#arc-001-decision-name) - {Architecture decision}

---

## TECH-001: {Decision Name}

**ID**: TECH-001
**Category**: Frontend | Backend | Database | Infrastructure | DevOps
**Status**: Accepted | Deprecated | Superseded
**Decision Date**: YYYY-MM-DD
**Last Reviewed**: YYYY-MM-DD

### Context

{What problem or need drove this decision?}

### Decision

{What technology/approach was chosen?}

### Rationale

- **Chosen because**: {Primary reasons}
- **Alternatives considered**: {What else was evaluated}
- **Trade-offs accepted**: {Known downsides}

### Related IDs

- [API-XXX](SoT.API_CONTRACTS.md#api-xxx) - {API using this technology}
- [BR-XXX](SoT.BUSINESS_RULES.md#br-xxx) - {Business rule driving this choice}
- [INT-XXX](SoT.INTEGRATIONS.md#int-xxx) - {Integration enabled by this}

---

## ARC-001: {Decision Name}

**ID**: ARC-001
**Category**: Data Flow | Security | Scaling | Integration | Patterns
**Status**: Accepted | Deprecated | Superseded
**Decision Date**: YYYY-MM-DD
**Last Reviewed**: YYYY-MM-DD

### Context

{What architectural challenge needed solving?}

### Decision

{What architecture pattern/approach was chosen?}

### Rationale

- **Chosen because**: {Primary reasons}
- **Alternatives considered**: {What else was evaluated}
- **Consequences**: {What this enables or constrains}

### Related IDs

- [TECH-XXX](#tech-xxx-decision-name) - {Technology enabling this}
- [DBT-XXX](SoT.DATA_MODEL.md#dbt-xxx) - {Data model affected}
- [UJ-XXX](SoT.USER_JOURNEYS.md#uj-xxx) - {Journey this supports}

---

## Deprecated Decisions

### TECH-XXX: {Decision Name} [SUPERSEDED]

**Status**: Superseded (YYYY-MM-DD)
**Replacement**: [TECH-YYY](#tech-yyy-decision-name)
**Reason**: {Why decision was changed}
**Migration**: {How to transition}

---

## Cross-Reference Index

**Decisions by Domain**:

- Frontend: TECH-001, ARC-001
- Backend: TECH-002, ARC-002

**Decisions by EPIC**:

- EPIC-01 implemented: TECH-001, ARC-001

---

## Update Protocol

### When to Add New IDs

1. **TECH-XXX**: Selecting a new technology, framework, or tool
2. **ARC-XXX**: Making a structural decision about system design

### Bidirectional Reference Checklist

When adding a new TECH/ARC-XXX:

- [ ] Update PRD.md v0.5/v0.6 section if applicable
- [ ] Update related API contracts if affected
- [ ] Update EPIC Section 2 "Context & IDs" list
- [ ] Update SoT.UNIQUE_ID_SYSTEM.md registry if maintained

---

*End of SoT.TECHNICAL_DECISIONS.md - Authoritative source for TECH-XXX and ARC-XXX IDs*
