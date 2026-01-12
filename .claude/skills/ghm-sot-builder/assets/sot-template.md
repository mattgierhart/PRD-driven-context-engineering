# SoT File Template

> Copy this template when creating a new Source of Truth file.
> Replace all `{PLACEHOLDER}` values with your specific content.
> Delete this instruction block after copying.

---

```markdown
---
version: 1.0
purpose: {Brief description of what this file tracks - one sentence}
id_prefix: {PREFIX}-###
last_updated: {YYYY-MM-DD}
authority: This is a SoT file - IDs created here are referenced by {list files: PRD.md, EPICs, other SoT files}
---

# {Artifact Type} (SoT File)

> **Purpose**: {What this file tracks - expand on frontmatter purpose}
> **ID Prefix**: {PREFIX}-XXX
> **Status**: Active SoT file
> **Cross-References**: {List files that reference or are referenced by this SoT}

## Navigation by Category

**{Category A}** ({PREFIX}-001 to {PREFIX}-099):
- [{PREFIX}-001](#{prefix}-001-title) - {Entry title}

**{Category B}** ({PREFIX}-101 to {PREFIX}-199):
- [{PREFIX}-101](#{prefix}-101-title) - {Entry title}

**{Category C}** ({PREFIX}-201 to {PREFIX}-299):
- [{PREFIX}-201](#{prefix}-201-title) - {Entry title}

---

## {PREFIX}-001: {Entry Title}

**ID**: {PREFIX}-001
**Category**: {Category Name}
**Status**: Active | Deprecated | Planned
**Owner**: {Team or Role}
**Created**: {YYYY-MM-DD}
**Last Updated**: {YYYY-MM-DD}

### {Primary Content Section Name}

{Main content for this entry - structure depends on artifact type}

### Related IDs

**{Relationship Type A}**:
- [{OTHER-PREFIX}-XXX](SoT.OTHER_FILE.md#{anchor}) - {Description}

**{Relationship Type B}**:
- [{OTHER-PREFIX}-YYY](SoT.OTHER_FILE.md#{anchor}) - {Description}

### Version History

| Version | Date | Changes | Updated By |
|---------|------|---------|------------|
| 1.0 | {YYYY-MM-DD} | Initial creation | {Name} |

---

## {PREFIX}-002: {Next Entry Title}

{Repeat the entry structure above for each new entry}

---

## Deprecated Entries

### {PREFIX}-XXX: {Deprecated Entry Title} [DEPRECATED]

**Status**: Deprecated ({YYYY-MM-DD})
**Replacement**: [{PREFIX}-YYY](#{prefix}-yyy-title) | None
**Reason**: {Why deprecated}
**Migration Guide**: {How to transition if applicable}
**Removal Date**: {When this can be cleaned up}

---

## Cross-Reference Index

> **Maintenance Note**: Update manually unless you add tooling in a fork.

**{PREFIX} by {Other Prefix}**:
- {OTHER}-XXX uses: {PREFIX}-001, {PREFIX}-002
- {OTHER}-YYY uses: {PREFIX}-001

**{PREFIX} by Category**:
- {Category A}: {PREFIX}-001, {PREFIX}-002
- {Category B}: {PREFIX}-101

---

## Update Protocol

### When to Add New {PREFIX}-XXX IDs

1. **{Scenario A}**: {When to create this type of entry}
2. **{Scenario B}**: {Another trigger for new entries}
3. **{Scenario C}**: {Another trigger for new entries}

### Bidirectional Reference Checklist

When adding a new {PREFIX}-XXX:
- [ ] Update {relevant SoT file} "{section}" for each {relationship}
- [ ] Update {another SoT file} "{section}" for each {relationship}
- [ ] Update EPIC Section 2 "Context & IDs" if part of active work
- [ ] Update SoT.UNIQUE_ID_SYSTEM.md registry tables

### Required Fields Validation

Before saving a new entry, verify:
- [ ] ID follows {PREFIX}-### format (3-digit, zero-padded)
- [ ] Title is descriptive and unique
- [ ] Status is set (Active/Planned/Deprecated)
- [ ] Created date is populated
- [ ] At least one Related ID exists (or documented reason why none)

---

*End of SoT.{FILENAME}.md - This SoT file is the authoritative source for all {PREFIX}-XXX IDs*
```

---

## Post-Creation Checklist

After creating your new SoT file using this template:

1. **Register in SoT.README.md**
   ```markdown
   | `SoT.{YOUR_FILE}.md` | {PREFIX}-### | {Purpose} |
   ```

2. **Register prefix in SoT.UNIQUE_ID_SYSTEM.md**
   - Add to Section 1.2 Standard Prefixes table
   - Add empty index table in Section 2.2

3. **Validate purity**
   - [ ] No methodology teaching in template
   - [ ] Update Protocol is file-specific
   - [ ] Self-documentation < 20% of file

4. **Test the template**
   - Create one real entry using only the template instructions
   - Verify cross-references resolve correctly
