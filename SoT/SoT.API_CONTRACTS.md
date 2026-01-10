---
version: 1.0
purpose: Source of Truth file for all API endpoint specifications. Each endpoint has a unique ID for cross-referencing.
id_prefix: API-XXX
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs created here are referenced by PRD.md, SoT.USER_JOURNEYS.md, SoT.testing_playbook.md, EPICs, and code
---

# API Contracts (SoT File)

> **Purpose**: Complete specifications for all API endpoints and integrations.
> **ID Prefix**: API-XXX
> **Status**: Active SoT file
> **Cross-References**: Referenced by PRD.md, SoT.USER_JOURNEYS.md, SoT.BUSINESS_RULES.md, SoT.testing_playbook.md, EPICs

## Navigation by Category

**Public APIs** (API-001 to API-099):
- [API-001](#api-001-endpoint-name) - {Endpoint name}
- [API-002](#api-002-endpoint-name) - {Endpoint name}

**Internal APIs** (API-101 to API-199):
- [API-101](#api-101-endpoint-name) - {Endpoint name}
- [API-102](#api-102-endpoint-name) - {Endpoint name}

**External Service Calls** (API-201 to API-299):
- [API-201](#api-201-service-name) - {External service integration}

**Webhooks** (API-301 to API-399):
- [API-301](#api-301-webhook-name) - {Webhook name}

**Background Jobs** (API-401 to API-499):
- [API-401](#api-401-job-name) - {Background job name}

---

## API-001: {Endpoint Name}

**ID**: API-001
**Category**: Public API | Internal API | External Service | Webhook | Background Job
**Status**: Active | Deprecated | Planned | Beta
**Owner**: Backend Team | Frontend Team | Integration Team
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD
**Version**: v1 | v2 | v3

### Endpoint Specification

**Method**: GET | POST | PUT | PATCH | DELETE
**Path**: `/api/v1/{resource}/{id}`
**Base URL**: `https://api.{product}.com` (Production)
**Full URL**: `https://api.{product}.com/api/v1/{resource}/{id}`

### Purpose & Use Case

**What It Does**: {Brief description of endpoint purpose}
**When To Use**: {Scenarios where this endpoint is appropriate}
**When NOT To Use**: {Common misconceptions or alternative endpoints}

### Authentication

**Method**: Bearer Token | API Key | Session Cookie | OAuth 2.0
**Required Headers**:

```http
Authorization: Bearer {access_token}
X-API-Key: {api_key}
Content-Type: application/json
```

**Permissions Required**:
- User Role: {role_name}
- Scope: `{scope_name}`
- Business Rule: [BR-XXX](SoT.BUSINESS_RULES.md#br-xxx) - {Permission rule}

### Request Format

**Headers**:

```http
Content-Type: application/json
Accept: application/json
X-Request-ID: {uuid}  # Optional, for tracing
```

**Path Parameters**:

| Parameter | Type | Required | Description | Example |
|-----------|------|----------|-------------|---------|
| `id` | string | Yes | Resource identifier | `prod_123abc` |
| `{param}` | {type} | {Yes/No} | {Description} | {Example} |

**Query Parameters**:

| Parameter | Type | Required | Default | Description | Example |
|-----------|------|----------|---------|-------------|---------|
| `page` | integer | No | 1 | Page number | `?page=2` |
| `limit` | integer | No | 20 | Items per page (max: 100) | `?limit=50` |
| `filter` | string | No | - | Filter criteria | `?filter=status:active` |

**Request Body** (for POST/PUT/PATCH):

```typescript
interface RequestBody {
  field1: string;           // Required - Description
  field2?: number;          // Optional - Description
  field3: {                 // Nested object
    subfield1: string;
    subfield2: boolean;
  };
  field4: string[];         // Array of strings
}
```

**Example Request**:

```http
POST /api/v1/products HTTP/1.1
Host: api.example.com
Authorization: Bearer eyJhbGciOiJIUzI1NiIs...
Content-Type: application/json

{
  "name": "Widget Pro",
  "category": "electronics",
  "price": 29.99,
  "metadata": {
    "sku": "WID-PRO-001",
    "inStock": true
  },
  "tags": ["featured", "new"]
}
```

### Response Format

**Success Response** (200 OK):

```typescript
interface SuccessResponse {
  success: true;
  data: {
    id: string;
    // Resource fields
  };
  metadata?: {
    requestId: string;
    timestamp: string;
  };
}
```

**Example Success**:

```json
{
  "success": true,
  "data": {
    "id": "prod_abc123",
    "name": "Widget Pro",
    "category": "electronics",
    "price": 29.99,
    "createdAt": "2025-11-09T10:30:00Z"
  },
  "metadata": {
    "requestId": "req_xyz789",
    "timestamp": "2025-11-09T10:30:00.123Z"
  }
}
```

**Error Responses**:

| Status Code | Error Code | Description | Recovery Action |
|-------------|------------|-------------|-----------------|
| 400 | `INVALID_REQUEST` | Invalid request format | Fix request body |
| 401 | `UNAUTHORIZED` | Missing/invalid auth | Refresh token |
| 403 | `FORBIDDEN` | Insufficient permissions | Upgrade plan/role |
| 404 | `NOT_FOUND` | Resource not found | Check resource ID |
| 422 | `VALIDATION_ERROR` | Business rule violation | See error details |
| 429 | `RATE_LIMIT_EXCEEDED` | Too many requests | Wait and retry |
| 500 | `INTERNAL_ERROR` | Server error | Retry with backoff |
| 503 | `SERVICE_UNAVAILABLE` | Temporary outage | Retry later |

**Example Error**:

```json
{
  "success": false,
  "error": {
    "code": "BR_001_VIOLATION",
    "message": "Free tier limited to 3 products. Upgrade to add more.",
    "details": {
      "currentCount": 3,
      "limit": 3,
      "tier": "FREE"
    },
    "action": "SHOW_UPGRADE_PROMPT",
    "businessRule": "BR-001"
  },
  "metadata": {
    "requestId": "req_xyz789",
    "timestamp": "2025-11-09T10:30:00.123Z"
  }
}
```

### Related IDs

**Used By User Journeys**:
- [UJ-XXX](SoT.USER_JOURNEYS.md#uj-xxx) - {Journey that calls this API}
- [UJ-YYY](SoT.USER_JOURNEYS.md#uj-yyy) - {Another journey}

**Enforces Business Rules**:
- [BR-XXX](SoT.BUSINESS_RULES.md#br-xxx) - {Business rule enforced}
- [BR-YYY](SoT.BUSINESS_RULES.md#br-yyy) - {Another rule}

**Database Operations**:
- [DBT-XXX](SoT.ACTUAL_SCHEMA.md#dbt-xxx) - {Table accessed} (Read/Write/Update/Delete)
- [DBT-YYY](SoT.ACTUAL_SCHEMA.md#dbt-yyy) - {Another table}

**Calls External Services** (if applicable):
- [API-ZZZ](#api-zzz-service-name) - {External service called}
- Third-party: {Service name} (e.g., Stripe, Google Cloud, AWS)

**Validated By Tests**:
- [TEST-XXX](SoT.testing_playbook.md#test-xxx) - {Test validating happy path}
- [TEST-YYY](SoT.testing_playbook.md#test-yyy) - {Test validating error handling}
- [TEST-ZZZ](SoT.testing_playbook.md#test-zzz) - {Test validating business rules}

**Deployment Requirements**:
- [DEP-XXX](SoT.deployment_playbook.md#dep-xxx) - {Deployment configuration}

### Rate Limits & Quotas

**Rate Limits**:

| Tier | Requests/Second | Requests/Hour | Requests/Day |
|------|----------------|---------------|--------------|
| Free | 1 | 100 | 1,000 |
| Basic | 10 | 1,000 | 10,000 |
| Pro | 50 | 10,000 | 100,000 |
| Enterprise | Custom | Custom | Custom |

**Quota Enforcement**:
- Counted by: User ID | API Key | IP Address
- Reset period: Sliding window | Fixed window (hourly/daily)
- Over-limit behavior: 429 error | Queueing | Throttling

**Caching Strategy**:
- Cache-Control: `public, max-age=300` (5 minutes)
- ETag support: Yes | No
- Conditional requests: If-None-Match, If-Modified-Since

### Performance SLA

**Target Performance**:
- p50 latency: <{X}ms
- p95 latency: <{Y}ms
- p99 latency: <{Z}ms
- Availability: {X}% uptime

**Performance Benchmarks**:

| Scenario | Target | Current | Status |
|----------|--------|---------|--------|
| Empty request | <100ms | 85ms | ✅ |
| Typical request | <200ms | 180ms | ✅ |
| Large payload | <500ms | 450ms | ✅ |
| With external call | <2s | 1.8s | ✅ |

**Monitoring**:
- Metrics: Prometheus/Grafana dashboard
- Alerts: PagerDuty/Slack on p95 > {threshold}
- Tracing: Request ID for end-to-end tracing

### Error Handling

**Retry Strategy**:
- Idempotent: Yes | No
- Safe to retry: Yes (GET, PUT) | No (POST without idempotency key)
- Recommended backoff: Exponential (1s, 2s, 4s, 8s)
- Max retries: 3

**Timeout Configuration**:
- Client timeout: {X} seconds
- Server timeout: {Y} seconds
- Connection timeout: {Z} seconds

### Implementation Notes

**Server-Side Logic** (reference only, actual code is source of truth):

```typescript
// High-level implementation pattern
async function handleRequest(req: Request): Promise<Response> {
  // 1. Validate authentication
  const user = await authenticateRequest(req);

  // 2. Validate business rules
  const validationResult = await validateBusinessRules(user, req.body);
  if (!validationResult.valid) {
    return errorResponse(422, validationResult.error);
  }

  // 3. Execute business logic
  const result = await performOperation(user, req.body);

  // 4. Return success response
  return successResponse(200, result);
}
```

**Client-Side Usage Pattern**:

```typescript
// Example SDK usage
const client = new APIClient({ apiKey: process.env.API_KEY });

try {
  const response = await client.products.create({
    name: "Widget Pro",
    category: "electronics",
    price: 29.99
  });

  console.log('Created product:', response.data.id);
} catch (error) {
  if (error.code === 'BR_001_VIOLATION') {
    // Handle business rule violation
    showUpgradePrompt();
  } else {
    // Handle other errors
    console.error('API error:', error.message);
  }
}
```

### Security Considerations

**Input Validation**:
- All inputs sanitized to prevent injection attacks
- Max payload size: {X} MB
- Content-Type validation: Required
- Field-level validation: {Describe validation rules}

**Sensitive Data**:
- PII fields: {List any personally identifiable information}
- Encryption: At rest and in transit
- Logging: Mask sensitive fields in logs
- Audit trail: Log all access to sensitive data

**CORS Configuration** (if public API):

```http
Access-Control-Allow-Origin: https://app.example.com
Access-Control-Allow-Methods: GET, POST, PUT, DELETE
Access-Control-Allow-Headers: Authorization, Content-Type
Access-Control-Max-Age: 86400
```

### Change Log & Versioning

**Breaking vs Non-Breaking Changes**:
- Breaking: Removing fields, changing types, new required fields
- Non-Breaking: Adding optional fields, new endpoints, expanded enums

**Version Strategy**:
- Current: v1 (stable)
- Beta: v2 (experimental, may change)
- Deprecated: v0 (sunset: YYYY-MM-DD)

### Detailed Specification

For additional implementation details and historical context, add appendices in this file or link external docs:
- OpenAPI/Swagger: `{link to interactive API docs}`
- Postman Collection: `{link to collection}`

### Version History

| Version | Date | Changes | Updated By | Breaking Change? |
|---------|------|---------|------------|------------------|
| 1.0 | YYYY-MM-DD | Initial creation | {Name} | N/A |
| 1.1 | YYYY-MM-DD | Added optional field `{field}` | {Name} | No |
| 2.0 | YYYY-MM-DD | Changed response format | {Name} | Yes |

---

## API-002: {Next Endpoint Name}

{Repeat the above structure for each API endpoint}

---

## Deprecated Endpoints

### API-XXX: {Deprecated Endpoint Name} [DEPRECATED]

**Status**: Deprecated (YYYY-MM-DD)
**Replacement**: [API-YYY](#api-yyy-endpoint-name)
**Reason**: {Why endpoint was deprecated}
**Sunset Date**: {When endpoint will be removed}
**Migration Guide**: {How to transition to new endpoint}

**Migration Example**:

```typescript
// OLD (API-XXX) - Deprecated
const response = await client.oldEndpoint.get(id);

// NEW (API-YYY) - Use this instead
const response = await client.newEndpoint.get(id);
```

---

## Cross-Reference Index

> **Auto-Generated Section**: Maintain manually unless you add tooling in a fork.

**Endpoints by User Journey**:
- UJ-101 calls: API-045, API-046, API-102
- UJ-102 calls: API-045

**Endpoints by Business Rule**:
- BR-001 enforced by: API-045, API-046
- BR-112 enforced by: API-101

**Endpoints by Database Table**:
- DBT-018 accessed by: API-045 (RW), API-046 (R), API-101 (RW)
- DBT-019 accessed by: API-045 (R)

**Endpoints by Test Coverage**:
- TEST-301 validates: API-045 (happy path)
- TEST-302 validates: API-045 (error handling)
- TEST-303 validates: API-046 (retry logic)

**External Dependencies**:
- Google Document AI used by: API-201, API-202
- Stripe used by: API-301, API-302
- AWS S3 used by: API-401

---

*End of SoT.API_CONTRACTS.md - This SoT file is the authoritative source for all API-XXX IDs*
