# SoT Patterns Reference

> Extracted from existing SoT files in the PRD Led Context Engineering methodology.

This reference documents the common structural patterns found across all Source of Truth files in the GHM methodology.

---

## 1. YAML Frontmatter Patterns

Every SoT file starts with YAML frontmatter. Two main patterns exist:

### Pattern A: Simple Metadata (Governance Files)

```yaml
---
title: "Human-readable title"
updated: "YYYY-MM-DD"
authority: "Source of authority"
---
```

Used by: `SoT.UNIQUE_ID_SYSTEM.md`, `SoT.README.md`

### Pattern B: Full Specification (Entry-based Files)

```yaml
---
version: 1.0
purpose: Brief description of what this file tracks
id_prefix: XXX-###
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs created here are referenced by [list files]
---
```

Used by: `SoT.BUSINESS_RULES.md`, `SoT.USER_JOURNEYS.md`, `SoT.API_CONTRACTS.md`

---

## 2. Purpose Block Pattern

Immediately after frontmatter, use a blockquote to state purpose:

```markdown
# {Title} (SoT File)

> **Purpose**: {What this file tracks}
> **ID Prefix**: {PREFIX}-XXX
> **Status**: Active SoT file
> **Cross-References**: {List of files that reference this}
```

This pattern makes the file's role immediately clear when opened.

---

## 3. Navigation Section Pattern

After the purpose block, include a navigation section:

```markdown
## Navigation by Category

**{Category A}** ({PREFIX}-001 to {PREFIX}-099):
- [{PREFIX}-001](#{prefix}-001-name) - {Title}
- [{PREFIX}-002](#{prefix}-002-name) - {Title}

**{Category B}** ({PREFIX}-101 to {PREFIX}-199):
- [{PREFIX}-101](#{prefix}-101-name) - {Title}
```

Benefits:
- Quick scanning for specific entries
- ID range indicates category at a glance
- Anchors enable direct linking

---

## 4. Entry Structure Pattern

Each entry follows a consistent structure:

```markdown
## {PREFIX}-XXX: {Title}

**ID**: {PREFIX}-XXX
**Category**: {Category Name}
**Status**: Active | Deprecated | Planned
**Owner**: {Team or Role}
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD

### {Primary Content Section}

{Main content of this entry}

### Related IDs

- [{OTHER-PREFIX}-XXX](SoT.OTHER_FILE.md#{id-anchor}) — {relationship-type}: {Description}
- [{OTHER-PREFIX}-YYY](SoT.OTHER_FILE.md#{id-anchor}) — {relationship-type}: {Description}

### Version History

| Date | Field | Previous | New | Reason | EPIC |
|------|-------|----------|-----|--------|------|
| YYYY-MM-DD | — | — | Initial creation | Created | EPIC-{XXX} |
```

Key principles:
- Metadata comes first (scannable)
- Related IDs use full markdown links with typed relationships (see cross-reference-patterns.md)
- Version History tracks field-level changes with previous/new values for drift detection

---

## 5. Cross-Reference Index Pattern

Near the end of the file, include a cross-reference index:

```markdown
## Cross-Reference Index

> **Auto-Generated Section**: Maintain manually unless you add tooling.

**{Prefix} by {Other Prefix}**:
- {OTHER}-045 {relationship}: {PREFIX}-001, {PREFIX}-002
- {OTHER}-046 {relationship}: {PREFIX}-001

**{Prefix} by {Category}**:
- {Category A}: {PREFIX}-001, {PREFIX}-102
- {Category B}: {PREFIX}-002, {PREFIX}-201
```

This enables bidirectional navigation and integrity checking.

---

## 6. Deprecated Entries Pattern

Deprecated entries go in a separate section:

```markdown
## Deprecated Entries

### {PREFIX}-XXX: {Title} [DEPRECATED]

**Status**: Deprecated (YYYY-MM-DD)
**Replacement**: [{PREFIX}-YYY](#{prefix}-yyy-title) | None
**Reason**: {Why deprecated}
**Migration Guide**: {How to transition}
**Removal Date**: {When this can be deleted}
```

Key rules:
- Never delete IDs, only deprecate
- Always link to replacement if one exists
- Include migration guidance

---

## 7. Update Protocol Pattern

Every SoT file ends with an update protocol:

```markdown
## Update Protocol

### When to Add New {PREFIX}-XXX IDs

1. **{Scenario A}**: {Description}
2. **{Scenario B}**: {Description}
3. **{Scenario C}**: {Description}

### Bidirectional Reference Checklist

When adding a new {PREFIX}-XXX:
- [ ] Update {OTHER_FILE}.md "Used By" section
- [ ] Update {ANOTHER_FILE}.md "Related" section
- [ ] Update EPIC **Context & IDs** section
- [ ] Update SoT.UNIQUE_ID_SYSTEM.md registry tables
```

This is **template self-documentation** (keep in file), not methodology teaching (move to skills).

---

## 8. File Naming Pattern

```
SoT.{ARTIFACT_TYPE}.md
```

Examples:
- `SoT.BUSINESS_RULES.md` (uppercase for emphasis)
- `SoT.customer_feedback.md` (lowercase also acceptable)
- `SoT.DESIGN_COMPONENTS.md`

Conventions:
- Always start with `SoT.`
- Use descriptive artifact type name
- Use `.md` extension
- Prefer uppercase for primary SoT files

---

## 9. ID Prefix Patterns

### Standard Prefixes (Already Defined)

| Prefix | Domain | Notes |
|--------|--------|-------|
| BR- | Business Rules | Commercial constraints |
| UJ- | User Journeys | User flows |
| API- | API Contracts | Endpoint definitions |
| DBT- | Data Schema | Database tables |
| CFD- | Customer Feedback | Insights from users |
| DES- | Design | UI components |
| TEST- | Tests | Validation specs |
| DEP- | Deployment | Release steps |
| GTM- | Go-to-Market | Launch activities |
| RUN- | Runbooks | Operational procedures |
| MON- | Monitoring | Observability |
| KPI- | Metrics | Key indicators |

### Creating New Prefixes

When existing prefixes don't fit:

1. **Check for overlap** — Could this be a category within an existing prefix?
2. **Choose 2-4 letters** — Short but descriptive
3. **Verify uniqueness** — Check `SoT.UNIQUE_ID_SYSTEM.md`
4. **Register immediately** — Add to ID system file

Examples of valid new prefixes:
- `PIC-` for Partner Integration Contracts
- `MIG-` for Migration Procedures
- `SEC-` for Security Controls

---

## 10. Category Range Pattern

Reserve ID ranges for logical groupings:

```
001-099: Core/Primary entries
101-199: Secondary/Feature-specific
201-299: Admin/Internal
301-399: Edge cases/Exceptions
401-499: Performance/Limits
```

This convention allows:
- Guessing category from ID number
- Parallel work without collision
- Logical grouping in navigation

---

## 11. Template Purity Litmus Test

When adding content to a SoT template, ask:

> "Is this teaching me how to maintain the FILE STRUCTURE, or teaching me DOMAIN KNOWLEDGE about what makes good content?"

### KEEP in Template (File Structure)

- Update protocols (when/how to modify)
- ID numbering conventions
- Cross-reference integrity checks
- Required fields checklist
- File-specific maintenance procedures

### MOVE to Skill References (Domain Knowledge)

- "Key learnings" or "best practices"
- Evaluation criteria (what makes good content)
- Example workflows or prompts
- Cross-file coordination instructions
- Good/bad pattern examples

---

## 12. Context Efficiency Rule

If content is only useful when THIS template is active → Keep in template (just-in-time)
If content is useful when CREATING content for this template → Move to skill references (skill-loaded)

This ensures:
- Templates remain lean for quick loading
- Skills load methodology only when needed
- Context window isn't bloated with unused content
