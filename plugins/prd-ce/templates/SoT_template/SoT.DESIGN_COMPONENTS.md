---
version: 1.0
purpose: Source of Truth for UI components, design tokens, and pattern library.
id_prefix: DES-XXX
last_updated: YYYY-MM-DD
authority: Template structure only; example IDs are non-authoritative until replaced and activated.
template_state: uninitialized
---
<!-- SECTION: template-structure -->

# Design Components (SoT File)

> **Purpose**: Catalog of UI components, design tokens, and reusable patterns.
> **ID Prefix**: DES-XXX
> **Status**: Uninitialized template — no DES records are accepted
> **Cross-References**: Referenced by SoT.USER_JOURNEYS.md, PRD.md, EPICs

## Navigation by Category

**Core Components** (DES-001 to DES-099):

- [DES-001](#des-001-component-name) - {Component name}

**Feature Components** (DES-101 to DES-199):

- `DES-101` - {Component name}

**Shared Components** (DES-201 to DES-299):

- `DES-201` - {Component name}

**Design Tokens** (DES-301 to DES-399):

- `DES-301` - {Token category}

---

## DES-001: {Component Name}

**ID**: DES-001
**Category**: Core | Feature | Shared | Token
**Status**: Active | Deprecated | Planned
**Platform**: Web | Mobile | Both
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD

### Description

{2-3 sentences describing this component's purpose and usage.}

### Specifications

**Dimensions**: {Size constraints}
**Variants**: {List of variants}
**States**: {Interactive states}

### Related IDs

- [UJ-XXX](SoT.USER_JOURNEYS.md#uj-xxx) - {Journey using this component}
- [API-XXX](SoT.API_CONTRACTS.md#api-xxx) - {API this component calls}
- [BR-XXX](SoT.BUSINESS_RULES.md#br-xxx) - {Business rule affecting display}

### Assets

- Figma: {Link to design file}
- Code: `src/components/{ComponentName}.tsx`

<!-- /SECTION: template-structure -->

---
<!-- CUSTOMIZABLE: entries -->

## Deprecated Components

### DES-XXX: {Component Name} [DEPRECATED]

**Status**: Deprecated (YYYY-MM-DD)
**Replacement**: `DES-YYY` | None
**Reason**: {Why deprecated}

<!-- /CUSTOMIZABLE: entries -->

---

## Cross-Reference Index

**Components by User Journey**:

- UJ-001 uses: DES-001, DES-201

**Components by Platform**:

- Web only: DES-001
- Mobile only: DES-101
- Both: DES-201

---

## Update Protocol

### When to Add New DES-XXX IDs

1. **New UI Component**: Distinct, reusable interface element
2. **Design Token Update**: New color, typography, or spacing token
3. **Pattern Library Addition**: Recurring design solution

### Bidirectional Reference Checklist

When adding a new DES-XXX:

- [ ] Update SoT.USER_JOURNEYS.md "Design Components" section
- [ ] Before v0.7, update the PRD gate change log / SoT snapshot; at v0.7+, update the active EPIC "Context & IDs" list
- [ ] Create corresponding component file in codebase
- [ ] Update SoT.UNIQUE_ID_SYSTEM.md registry if maintained

---

*End of SoT.DESIGN_COMPONENTS.md — canonical DES record location once activated and accepted; currently template structure only.*
