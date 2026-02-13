---
version: 1.0
purpose: Source of Truth for deployment procedures, runbooks, and monitoring.
id_prefix: DEP-XXX, RUN-XXX, MON-XXX
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs here are referenced by PRD.md, EPICs, and operations docs
---
<!-- SECTION: template-structure -->

# Deployment (SoT File)

> **Purpose**: Deployment procedures, operational runbooks, and monitoring rules.
> **ID Prefixes**: DEP-XXX (Deployment), RUN-XXX (Runbooks), MON-XXX (Monitoring)
> **Status**: Active SoT file
> **Cross-References**: Referenced by PRD.md, EPICs, SoT.TESTING.md
> **Note**: GTM-XXX (Go-to-Market) IDs live in PRD.md v0.9 section

## Navigation by Category

**Deployment Procedures** (DEP-001 to DEP-099):

- [DEP-001](#dep-001-procedure-name) - {Procedure name}

**Operational Runbooks** (RUN-001 to RUN-099):

- [RUN-001](#run-001-runbook-name) - {Runbook name}

**Monitoring Rules** (MON-001 to MON-099):

- [MON-001](#mon-001-metric-name) - {Metric name}

---

## DEP-001: {Procedure Name}

**ID**: DEP-001
**Category**: Infrastructure | Application | Database
**Status**: Active | Deprecated | Planned
**Created**: YYYY-MM-DD

### Purpose

{What this deployment procedure accomplishes.}

### Steps

1. **Prepare**: {Preparation step}
2. **Deploy**: {Deployment step}
3. **Verify**: {Verification step}

### Rollback

{How to rollback if deployment fails.}

### Related IDs

- [TEST-XXX](SoT.TESTING.md#test-xxx) - {Deployment validation test}
- [MON-XXX](#mon-xxx-metric-name) - {Metrics to watch}

---

## RUN-001: {Runbook Name}

**ID**: RUN-001
**Category**: Incident Response | Maintenance | Recovery
**Status**: Active | Deprecated
**Created**: YYYY-MM-DD

### When to Use

{Trigger conditions for this runbook.}

### Steps

1. **Assess**: {Assessment step}
2. **Mitigate**: {Mitigation step}
3. **Resolve**: {Resolution step}

### Related IDs

- [MON-XXX](#mon-xxx-metric-name) - {Alert triggering this runbook}

---

## MON-001: {Metric Name}

**ID**: MON-001
**Category**: Performance | Availability | Business
**Status**: Active | Planned
**Created**: YYYY-MM-DD

### Definition

**What**: {What is being measured}
**Thresholds**: Warning: {value} | Critical: {value}

### Related IDs

- [RUN-XXX](#run-xxx-runbook-name) - {Runbook if threshold breached}
- [BR-XXX](SoT.BUSINESS_RULES.md#br-xxx) - {SLA or requirement}

<!-- /SECTION: template-structure -->

---
<!-- CUSTOMIZABLE: entries -->

## Deprecated Entries

### DEP-XXX: {Name} [DEPRECATED]

**Status**: Deprecated (YYYY-MM-DD)
**Replacement**: [DEP-YYY](#dep-yyy-name) | None
**Reason**: {Why deprecated}

<!-- /CUSTOMIZABLE: entries -->

---

## Update Protocol

### When to Add New IDs

1. **DEP-XXX**: New deployment procedure or environment
2. **RUN-XXX**: New incident response or maintenance procedure
3. **MON-XXX**: New metric, alert, or dashboard

### Bidirectional Reference Checklist

When adding a new DEP/RUN/MON-XXX:

- [ ] Update SoT.TESTING.md if deployment has tests
- [ ] Update EPIC Section 2 "Context & IDs" list
- [ ] Link runbooks to monitoring alerts
- [ ] Update SoT.UNIQUE_ID_SYSTEM.md registry if maintained

---

*End of SoT.DEPLOYMENT.md - Authoritative source for DEP-XXX, RUN-XXX, MON-XXX IDs*
