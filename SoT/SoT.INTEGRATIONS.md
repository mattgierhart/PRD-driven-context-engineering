---
version: 1.0
purpose: Source of Truth for third-party service integrations and external dependencies.
id_prefix: INT-XXX
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs here are referenced by SoT.API_CONTRACTS.md, EPICs, and code
---

# Integrations (SoT File)

> **Purpose**: Catalog of third-party services, external APIs, and integration dependencies.
> **ID Prefix**: INT-XXX
> **Status**: Active SoT file
> **Cross-References**: Referenced by SoT.API_CONTRACTS.md, SoT.DEPLOYMENT.md, EPICs

## Navigation by Category

**Payment Services** (INT-001 to INT-099):

- [INT-001](#int-001-integration-name) - {Service name}

**Authentication Services** (INT-101 to INT-199):

- [INT-101](#int-101-integration-name) - {Service name}

**Data Services** (INT-201 to INT-299):

- [INT-201](#int-201-integration-name) - {Service name}

**Communication Services** (INT-301 to INT-399):

- [INT-301](#int-301-integration-name) - {Service name}

---

## INT-001: {Integration Name}

**ID**: INT-001
**Category**: Payment | Auth | Data | Communication | Analytics | Storage
**Status**: Active | Deprecated | Planned
**Provider**: {Company name}
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD

### Description

{2-3 sentences describing this integration's purpose.}

### Configuration

**Environment Variables**:

- `{SERVICE}_API_KEY` - API key
- `{SERVICE}_WEBHOOK_SECRET` - Webhook signing secret

**Endpoints**:

- Production: `https://api.{service}.com`
- Sandbox: `https://sandbox.{service}.com`

### Constraints

- **Rate Limits**: {Requests/second or /minute}
- **Cost Model**: {Per-request, monthly, usage-based}
- **SLA**: {Uptime guarantee}

### Related IDs

- [API-XXX](SoT.API_CONTRACTS.md#api-xxx) - {API that calls this service}
- [BR-XXX](SoT.BUSINESS_RULES.md#br-xxx) - {Business rule requiring this}
- [DEP-XXX](SoT.DEPLOYMENT.md#dep-xxx) - {Deployment config for this}
- [TECH-XXX](SoT.TECHNICAL_DECISIONS.md#tech-xxx) - {Why this was chosen}

---

## Deprecated Integrations

### INT-XXX: {Integration Name} [DEPRECATED]

**Status**: Deprecated (YYYY-MM-DD)
**Replacement**: [INT-YYY](#int-yyy-integration-name) | None
**Reason**: {Why deprecated}
**Migration Guide**: {How to transition}

---

## Cross-Reference Index

**Integrations by API**:

- API-001 uses: INT-001, INT-101

**Integrations by Category**:

- Payment: INT-001
- Auth: INT-101
- Data: INT-201

---

## Update Protocol

### When to Add New INT-XXX IDs

1. **New Third-Party Service**: Adding a new external dependency
2. **Service Migration**: Switching providers (create new, deprecate old)
3. **API Version Change**: Major version upgrade requiring config changes

### Bidirectional Reference Checklist

When adding a new INT-XXX:

- [ ] Update SoT.API_CONTRACTS.md "External Services" section
- [ ] Update SoT.DEPLOYMENT.md with required environment variables
- [ ] Update EPIC Section 2 "Context & IDs" list
- [ ] Document in SoT.TECHNICAL_DECISIONS.md if significant choice
- [ ] Update SoT.UNIQUE_ID_SYSTEM.md registry if maintained

---

*End of SoT.INTEGRATIONS.md - Authoritative source for all INT-XXX IDs*
