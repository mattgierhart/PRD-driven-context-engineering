---
version: 1.0
purpose: Source of Truth for user journeys, personas, and screen flows.
id_prefix: UJ-XXX, PER-XXX, SCR-XXX
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs here are referenced by PRD.md, EPICs, and other SoT files
---
<!-- SECTION: template-structure -->

# User Journeys (SoT File)

> **Purpose**: User flows, personas, and screen definitions for the product.
> **ID Prefixes**: UJ-XXX (journeys), PER-XXX (personas), SCR-XXX (screens)
> **Status**: Active SoT file
> **Cross-References**: Referenced by PRD.md, SoT.API_CONTRACTS.md, SoT.TESTING.md, EPICs

## Navigation by Category

**Personas** (PER-001 to PER-099):

- [PER-001](#per-001-persona-name) - {Persona name}

**Screens** (SCR-001 to SCR-099):

- [SCR-001](#scr-001-screen-name) - {Screen name}

**Core Journeys** (UJ-001 to UJ-099):

- [UJ-001](#uj-001-journey-name) - {Journey name}

**Feature Journeys** (UJ-101 to UJ-199):

- [UJ-101](#uj-101-journey-name) - {Journey name}

---

## PER-001: {Persona Name}

**ID**: PER-001
**Status**: Active | Deprecated
**Created**: YYYY-MM-DD

### Profile

- **Role**: {Job title or role}
- **Goals**: {What they want to achieve}
- **Pain Points**: {Current frustrations}
- **Tech Comfort**: High | Medium | Low

### Related IDs

- [UJ-XXX](#uj-xxx-journey-name) - {Primary journey for this persona}

---

## SCR-001: {Screen Name}

**ID**: SCR-001
**Status**: Active | Deprecated | Planned
**Created**: YYYY-MM-DD

### Purpose

{What this screen accomplishes}

### Key Elements

- {Element 1}
- {Element 2}

### Related IDs

- [UJ-XXX](#uj-xxx-journey-name) - {Journey containing this screen}
- [DES-XXX](SoT.DESIGN_COMPONENTS.md#des-xxx) - {Components used}

---

## UJ-001: {Journey Name}

**ID**: UJ-001
**Category**: Core | Feature | Admin | Error
**Status**: Active | Deprecated | Planned
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD

### Overview

- **User Goal**: {What user wants to accomplish}
- **Trigger**: {What initiates this journey}
- **Success Criteria**: {How we know it succeeded}

### Steps

1. **{Step}**: {Action} → {Response}
2. **{Step}**: {Action} → {Response}
3. **{Step}**: {Action} → {Response}

### Related IDs

- [PER-XXX](#per-xxx-persona-name) - {Persona taking this journey}
- [SCR-XXX](#scr-xxx-screen-name) - {Screens in this journey}
- [API-XXX](SoT.API_CONTRACTS.md#api-xxx) - {APIs called}
- [BR-XXX](SoT.BUSINESS_RULES.md#br-xxx) - {Rules enforced}
- [DES-XXX](SoT.DESIGN_COMPONENTS.md#des-xxx) - {Components used}
- [TEST-XXX](SoT.TESTING.md#test-xxx) - {Tests validating this}

<!-- /SECTION: template-structure -->

---
<!-- CUSTOMIZABLE: entries -->

## Deprecated Entries

### UJ-XXX: {Name} [DEPRECATED]

**Status**: Deprecated (YYYY-MM-DD)
**Replacement**: [UJ-YYY](#uj-yyy-name) | None
**Reason**: {Why deprecated}

<!-- /CUSTOMIZABLE: entries -->

---

## Cross-Reference Index

**Journeys by Persona**:

- PER-001 uses: UJ-001, UJ-101

**Journeys by Screen**:

- SCR-001 appears in: UJ-001, UJ-102

---

## Update Protocol

### When to Add New IDs

1. **PER-XXX**: New user segment or persona identified
2. **SCR-XXX**: New screen or significant screen redesign
3. **UJ-XXX**: New user flow from trigger to goal completion

### Bidirectional Reference Checklist

When adding a new UJ/PER/SCR-XXX:

- [ ] Update SoT.API_CONTRACTS.md for APIs used
- [ ] Update SoT.BUSINESS_RULES.md for rules enforced
- [ ] Update SoT.DESIGN_COMPONENTS.md for UI components
- [ ] Update SoT.TESTING.md with validation tests
- [ ] Update EPIC Section 2 "Context & IDs" list
- [ ] Update SoT.UNIQUE_ID_SYSTEM.md registry if maintained

---

*End of SoT.USER_JOURNEYS.md - Authoritative source for UJ-XXX, PER-XXX, SCR-XXX IDs*
