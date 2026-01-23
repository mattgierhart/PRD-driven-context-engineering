---
version: 2.0
purpose: Source of Truth for deployment configuration, environments, secrets inventory, procedures, runbooks, and monitoring.
id_prefix: DEP-XXX, RUN-XXX, MON-XXX, SEC-XXX
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs here are referenced by PRD.md, EPICs, and operations docs
---

# Deployment (SoT File)

> **Purpose**: Deployment configuration, secrets inventory, operational runbooks, and monitoring rules.
> **ID Prefixes**: DEP-XXX (Deployment), RUN-XXX (Runbooks), MON-XXX (Monitoring), SEC-XXX (Secrets)
> **Status**: Active SoT file
> **Cross-References**: Referenced by PRD.md v0.7/v0.8, EPICs, SoT.TESTING.md
> **Note**: GTM-XXX (Go-to-Market) IDs live in PRD.md v0.9 section

---

## Navigation by Category

**Environments** (ENV-001 to ENV-099):
- See [SoT.TECHNICAL_DECISIONS.md](SoT.TECHNICAL_DECISIONS.md) for ENV-XXX IDs

**Secrets Inventory** (SEC-001 to SEC-099):
- [SEC-001](#sec-001-secret-name) - {Secret name}

**Deployment Procedures** (DEP-001 to DEP-099):
- [DEP-001](#dep-001-procedure-name) - {Procedure name}

**Operational Runbooks** (RUN-001 to RUN-099):
- [RUN-001](#run-001-runbook-name) - {Runbook name}

**Monitoring Rules** (MON-001 to MON-099):
- [MON-001](#mon-001-metric-name) - {Metric name}

---

## Environments

| ID | Environment | Platform | URL | Branch Trigger |
|----|-------------|----------|-----|----------------|
| ENV-001 | Production | [Platform] | [URL] | main |
| ENV-002 | Preview | [Platform] | [Pattern] | Pull requests |
| ENV-003 | Development | Local | localhost:[port] | N/A |

> **Note**: ENV-XXX IDs are defined in [SoT.TECHNICAL_DECISIONS.md](SoT.TECHNICAL_DECISIONS.md). This table provides a deployment-focused view.

---

## Secrets Inventory

Track all secrets required for deployment. **Do not store actual values here** — only metadata.

| ID | Secret Name | Environment(s) | Storage Location | Owner | Last Rotated |
|----|-------------|----------------|------------------|-------|--------------|
| SEC-001 | DATABASE_URL | Production, Preview | [Platform secrets] | [Name] | YYYY-MM-DD |
| SEC-002 | API_KEY | All | [Platform secrets] | [Name] | YYYY-MM-DD |
| SEC-003 | [Name] | [Env] | [Location] | [Owner] | YYYY-MM-DD |

### Secret Categories

**Web Secrets**
- Database connection strings
- Third-party API keys
- Authentication secrets (JWT, OAuth)
- Analytics/monitoring keys

**Mobile Secrets** (if applicable)
- Code signing credentials (certificates, provisioning profiles)
- App store API keys
- Push notification credentials
- Keystore passwords (Android)

**Shared Secrets**
- Secrets used by both web and mobile
- Note sync requirements between platforms

### SEC-001: {Secret Name}

**ID**: SEC-001
**Category**: Database | API | Authentication | Signing
**Status**: Active | Deprecated | Planned
**Environments**: Production, Preview, Development
**Storage**: [Platform secrets manager]
**Owner**: [Name/Team]
**Last Rotated**: YYYY-MM-DD

#### Purpose

{What this secret is used for.}

#### Rotation Procedure

1. Generate new secret value in source system
2. Update secret in [storage location]
3. Trigger redeployment if needed
4. Verify application works with new secret
5. Revoke old secret value

#### Related IDs

- [DEP-XXX](#dep-xxx-procedure-name) - {Deployment using this secret}
- [RUN-XXX](#run-xxx-runbook-name) - {Runbook for rotation}

---

## CI/CD Configuration

### Pipeline Overview

```
[Trigger] → [Quality Checks] → [Build] → [Deploy] → [Verify]
```

### Workflow Files

| Workflow | Trigger | Purpose | File Location |
|----------|---------|---------|---------------|
| CI | Push, PR | Lint, test, typecheck | .github/workflows/ci.yml |
| Deploy Web | Merge to main | Production deployment | [Platform-managed or workflow] |
| Deploy Mobile | Version tag | App store submission | .github/workflows/mobile.yml |

### Branch Protection Rules

| Rule | Enabled | Notes |
|------|---------|-------|
| Require PR before merge | Yes/No | |
| Require status checks | Yes/No | Checks: [list] |
| Require up-to-date branch | Yes/No | |
| Require approvals | Yes/No | Count: [n] |

---

## Platform-Specific Configuration

### Web Deployment

| Setting | Value |
|---------|-------|
| Platform | [e.g., Vercel, Netlify, AWS] |
| Framework preset | [e.g., Next.js, Vite] |
| Build command | [command] |
| Output directory | [path] |
| Node version | [version] |

### Mobile Deployment (if applicable)

| Setting | iOS | Android |
|---------|-----|---------|
| Signing approach | [Manual/Managed/Automated] | [Keystore location] |
| Beta distribution | [TestFlight/Other] | [Play Store Internal/Other] |
| Production track | App Store | Play Store Production |
| Build automation | [Tool] | [Tool] |

---

## Setup Checklist

Use this checklist when initializing deployment for a new product.

### Initial Setup
- [ ] Create hosting account/project
- [ ] Connect repository to hosting platform
- [ ] Configure environment variables
- [ ] Set up branch protection rules
- [ ] Verify preview deployments work

### Mobile Setup (if applicable)
- [ ] Create app store accounts (Apple Developer, Google Play Console)
- [ ] Generate code signing credentials
- [ ] Store signing credentials securely
- [ ] Configure build automation
- [ ] Test beta deployment flow
- [ ] Test production deployment flow

### Verification
- [ ] Push to feature branch → Preview deployment works
- [ ] Merge to main → Production deployment works
- [ ] All secrets are documented in inventory (not values, just metadata)
- [ ] Team members can deploy without tribal knowledge

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
- [SEC-XXX](#sec-xxx-secret-name) - {Secrets required}

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

## Runbook: Common Operations

### Rotate a Secret
1. Generate new secret value in source system
2. Update secret in [storage location]
3. Trigger redeployment if needed
4. Update "Last Rotated" in secrets inventory
5. Revoke old secret value

### Rollback Production
1. [Platform-specific rollback steps]
2. Verify rollback successful
3. Document incident

### Add New Environment Variable
1. Add to [storage location] for each environment
2. Update secrets inventory
3. Update application code to use variable
4. Deploy and verify

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

---

## Deprecated Entries

### DEP-XXX: {Name} [DEPRECATED]

**Status**: Deprecated (YYYY-MM-DD)
**Replacement**: [DEP-YYY](#dep-yyy-name) | None
**Reason**: {Why deprecated}

---

## Update Protocol

### When to Add New IDs

1. **SEC-XXX**: New secret or credential required for deployment
2. **DEP-XXX**: New deployment procedure or environment
3. **RUN-XXX**: New incident response or maintenance procedure
4. **MON-XXX**: New metric, alert, or dashboard

### Bidirectional Reference Checklist

When adding a new SEC/DEP/RUN/MON-XXX:

- [ ] Update SoT.TESTING.md if deployment has tests
- [ ] Update EPIC Section 2 "Context & IDs" list
- [ ] Link runbooks to monitoring alerts
- [ ] Link secrets to deployments that use them
- [ ] Update SoT.UNIQUE_ID_SYSTEM.md registry if maintained

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| YYYY-MM-DD | Added Secrets Inventory, CI/CD Configuration, Platform Configuration sections | [Name] |
| YYYY-MM-DD | Initial deployment configuration | [Name] |

---

*End of SoT.DEPLOYMENT.md - Authoritative source for DEP-XXX, RUN-XXX, MON-XXX, SEC-XXX IDs*
