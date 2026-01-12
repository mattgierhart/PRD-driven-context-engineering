---
version: 1.0
purpose: Source of Truth for API endpoint specifications and contracts.
id_prefix: API-XXX
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs here are referenced by PRD.md, SoT.USER_JOURNEYS.md, SoT.TESTING.md, EPICs, and code
---

# API Contracts (SoT File)

> **Purpose**: Specifications for all API endpoints and integrations.
> **ID Prefix**: API-XXX
> **Status**: Active SoT file
> **Cross-References**: Referenced by PRD.md, SoT.USER_JOURNEYS.md, SoT.BUSINESS_RULES.md, SoT.TESTING.md, EPICs

## Navigation by Category

**Public APIs** (API-001 to API-099):

- [API-001](#api-001-endpoint-name) - {Endpoint name}

**Internal APIs** (API-101 to API-199):

- [API-101](#api-101-endpoint-name) - {Endpoint name}

**Webhooks** (API-201 to API-299):

- [API-201](#api-201-webhook-name) - {Webhook name}

**Background Jobs** (API-301 to API-399):

- [API-301](#api-301-job-name) - {Job name}

---

## API-001: {Endpoint Name}

**ID**: API-001
**Category**: Public | Internal | Webhook | Background
**Status**: Active | Deprecated | Planned
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD

### Specification

**Method**: GET | POST | PUT | PATCH | DELETE
**Path**: `/api/v1/{resource}/{id}`
**Auth**: Bearer Token | API Key | None

### Purpose

{Brief description of what this endpoint does.}

### Request

**Parameters**: {Key parameters with types}
**Body**: {Key fields for POST/PUT}

### Response

**Success (200)**: `{ success: true, data: {...} }`
**Errors**: 400, 401, 403, 404, 422, 500

### Related IDs

- [UJ-XXX](SoT.USER_JOURNEYS.md#uj-xxx) - {Journey using this API}
- [BR-XXX](SoT.BUSINESS_RULES.md#br-xxx) - {Rule enforced}
- [DBT-XXX](SoT.DATA_MODEL.md#dbt-xxx) - {Table accessed}
- [INT-XXX](SoT.INTEGRATIONS.md#int-xxx) - {External service called}
- [TEST-XXX](SoT.TESTING.md#test-xxx) - {Test validating this}

---

## Deprecated Endpoints

### API-XXX: {Name} [DEPRECATED]

**Status**: Deprecated (YYYY-MM-DD)
**Replacement**: [API-YYY](#api-yyy-name) | None
**Sunset Date**: YYYY-MM-DD
**Reason**: {Why deprecated}

---

## Cross-Reference Index

**Endpoints by Journey**:

- UJ-001 calls: API-001, API-002

**Endpoints by Business Rule**:

- BR-001 enforced by: API-001

---

## Update Protocol

### When to Add New API-XXX IDs

1. **New Endpoint**: Public or internal API endpoint
2. **Webhook**: Incoming webhook handler
3. **Background Job**: Scheduled or queued task

### Bidirectional Reference Checklist

When adding a new API-XXX:

- [ ] Update SoT.USER_JOURNEYS.md "APIs Used" section
- [ ] Update SoT.BUSINESS_RULES.md if rule is enforced
- [ ] Update SoT.TESTING.md with endpoint tests
- [ ] Update EPIC Section 2 "Context & IDs" list
- [ ] Update SoT.UNIQUE_ID_SYSTEM.md registry if maintained

---

*End of SoT.API_CONTRACTS.md - Authoritative source for all API-XXX IDs*
