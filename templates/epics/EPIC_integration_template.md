---
version: 1.3
purpose: To detail the architecture, requirements, and implementation plan for integrating a third-party service or API.
summary: Added progressive documentation features, model-specific guidance, and testing-first approach.
last_updated: 2025-07-06
epic_id: EPIC-03
epic_name: "{Service/API Name} Integration"
epic_type: "integration"
status: "planning"
model_restrictions: "none"
---

# EPIC-03: Integration - [Service/API Name] v{0.1}

## Epic Meta Information
| Field | Value |
|-------|-------|
| **Current Version** | v0.1 |
| **Planning Version** | v0.1-0.3 (Opus) |
| **Execution Version** | v0.4+ (Sonnet) |
| **Last Updated** | [Date and Time] |
| **Last Editor** | [Model/User] |
| **Status** | Planning Phase |
| **Completion** | 0% |

## Version History
| Version | Date | Editor | Changes |
|---------|------|--------|---------|
| v0.1 | [Date] | [Editor] | Initial integration plan |

## Quick Navigation
- [Overview](#overview)
- [Integration Architecture](#integration-architecture)
- [Integration Requirements](#integration-requirements)
- [Testing Strategy](#testing-strategy)
- [API Documentation](#api-documentation)
- [Implementation Plan](#implementation-plan)
- [Error Handling](#error-handling)
- [Progress Log](#progress-log)
- [Handoff History](#handoff-history)

**Authority**: See [WORKFLOW_MASTER.md](../workflows/WORKFLOW_MASTER.md) for complete workflow processes  
**Template Usage**: See [README.md](./README.md) for template usage guide  
**Standards**: See [STANDARDS.md](../../STANDARDS.md) for documentation hierarchy

## Overview
**Purpose**: Integrate [service] for [functionality]
**Integration Type**: [REST API/Webhook/SDK/OAuth]
**Priority**: [High/Medium/Low]
**Created**: [Date]
**Last Updated**: [Date]

## Integration Architecture

### System Overview
```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Our App   │ <-> │  API Gateway │ <-> │  External   │
│             │     │  /Middleware │     │   Service   │
└─────────────┘     └─────────────┘     └─────────────┘
       |                   |                    |
   Request/             Auth/Rate            Service
   Response             Limiting              Logic
```

### Data Flow
```
User Action -> Our API -> External API -> Process Response -> Update UI
     |             |            |                |              |
  Validate      Add Auth    Make Request    Transform      Cache Result
```

## Integration Requirements

### Technical Requirements
- **API Version**: [v2/v3]
- **Protocol**: [REST/GraphQL/gRPC]
- **Authentication**: [API Key/OAuth/JWT]
- **Rate Limits**: [100 req/min]
- **Response Time**: [< 500ms]

### Business Requirements
- [ ] Support core functionality
- [ ] Handle errors gracefully
- [ ] Maintain data consistency
- [ ] Enable monitoring/analytics

## Testing Strategy {#testing-strategy}
<!-- Model: opus for strategy, sonnet for implementation -->

### Integration Testing Plan
**Mock First Development**:
- [ ] Create API mocks for all endpoints
- [ ] Test error scenarios with mocks
- [ ] Test rate limiting behavior
- [ ] Test timeout handling
- [ ] Validate data transformations

### Test Coverage Requirements
```typescript
// Example test structure
describe('[Service] Integration', () => {
  describe('Authentication', () => {
    it('should authenticate successfully')
    it('should handle auth failures')
    it('should refresh tokens automatically')
  })
  
  describe('API Operations', () => {
    it('should handle successful requests')
    it('should retry on transient failures')
    it('should respect rate limits')
  })
})
```

### Performance Testing
- Response time benchmarks
- Load testing with realistic traffic
- Fallback behavior validation

## API Documentation {#api-documentation}

### Authentication
```typescript
// API Key Authentication
const headers = {
  'Authorization': `Bearer ${process.env.API_KEY}`,
  'Content-Type': 'application/json',
};

// OAuth Flow
const oauth = {
  clientId: process.env.OAUTH_CLIENT_ID,
  clientSecret: process.env.OAUTH_CLIENT_SECRET,
  redirectUri: `${process.env.APP_URL}/api/callback`,
};
```

### Core Endpoints

#### 1. Authentication
```typescript
// POST /auth/token
interface TokenRequest {
  grant_type: 'client_credentials';
  client_id: string;
  client_secret: string;
}

interface TokenResponse {
  access_token: string;
  token_type: 'Bearer';
  expires_in: number;
}
```

#### 2. Main Resources
```typescript
// GET /api/v2/resources
interface ListRequest {
  page?: number;
  limit?: number;
  filters?: Record<string, any>;
}

interface ListResponse {
  data: Resource[];
  pagination: {
    total: number;
    page: number;
    pages: number;
  };
}

// POST /api/v2/resources
interface CreateRequest {
  name: string;
  type: string;
  metadata?: Record<string, any>;
}

interface CreateResponse {
  id: string;
  created_at: string;
  // ... other fields
}
```

### Webhook Handling
```typescript
// Webhook endpoint
// POST /api/webhooks/[service-name]

interface WebhookPayload {
  event: string;
  data: Record<string, any>;
  timestamp: string;
  signature: string;
}

// Signature verification
function verifyWebhook(payload: string, signature: string): boolean {
  const expected = crypto
    .createHmac('sha256', process.env.WEBHOOK_SECRET)
    .update(payload)
    .digest('hex');
  
  return crypto.timingSafeEqual(
    Buffer.from(signature),
    Buffer.from(expected)
  );
}
```

## Implementation Plan

### Phase 1: Setup & Authentication
- [ ] Register application with service
- [ ] Store credentials securely
- [ ] Implement authentication flow
- [ ] Create base API client

### Phase 2: Core Integration
- [ ] Implement main API endpoints
- [ ] Add error handling
- [ ] Create data models
- [ ] Add request/response logging

### Phase 3: Advanced Features
- [ ] Implement webhooks
- [ ] Add caching layer
- [ ] Create retry logic
- [ ] Build monitoring dashboard

### Phase 4: Testing & Optimization
- [ ] Write integration tests
- [ ] Performance optimization
- [ ] Security audit
- [ ] Documentation

## Code Implementation

### API Client
```typescript
// lib/integrations/[service-name]/client.ts
export class ServiceClient {
  private baseUrl: string;
  private apiKey: string;
  private rateLimiter: RateLimiter;

  constructor(config: ClientConfig) {
    this.baseUrl = config.baseUrl;
    this.apiKey = config.apiKey;
    this.rateLimiter = new RateLimiter({
      maxRequests: 100,
      perMilliseconds: 60000,
    });
  }

  async request<T>(
    method: string,
    endpoint: string,
    data?: any
  ): Promise<T> {
    await this.rateLimiter.check();

    const response = await fetch(`${this.baseUrl}${endpoint}`, {
      method,
      headers: {
        'Authorization': `Bearer ${this.apiKey}`,
        'Content-Type': 'application/json',
      },
      body: data ? JSON.stringify(data) : undefined,
    });

    if (!response.ok) {
      throw new ServiceError(response);
    }

    return response.json();
  }
}
```

### Error Handling
```typescript
// lib/integrations/[service-name]/errors.ts
export class ServiceError extends Error {
  constructor(
    public statusCode: number,
    public code: string,
    message: string,
    public details?: any
  ) {
    super(message);
    this.name = 'ServiceError';
  }

  static async fromResponse(response: Response) {
    const data = await response.json().catch(() => ({}));
    return new ServiceError(
      response.status,
      data.code || 'UNKNOWN_ERROR',
      data.message || 'An error occurred',
      data.details
    );
  }
}
```

### Caching Strategy
```typescript
// lib/integrations/[service-name]/cache.ts
export class IntegrationCache {
  private redis: Redis;
  private ttl: number;

  constructor(redis: Redis, ttl = 300) {
    this.redis = redis;
    this.ttl = ttl;
  }

  async get<T>(key: string): Promise<T | null> {
    const cached = await this.redis.get(key);
    return cached ? JSON.parse(cached) : null;
  }

  async set<T>(key: string, value: T): Promise<void> {
    await this.redis.setex(
      key,
      this.ttl,
      JSON.stringify(value)
    );
  }

  getCacheKey(operation: string, params: any): string {
    const hash = crypto
      .createHash('md5')
      .update(JSON.stringify(params))
      .digest('hex');
    return `integration:${operation}:${hash}`;
  }
}
```

## Implementation Plan {#implementation-plan}
<!-- Model: opus for architecture, sonnet for implementation -->

### Task Breakdown
<!-- Tasks will be added here during planning phase -->

### Task Template
```markdown
#### Task [ID] - [Task Title]
*   **Status:** `To Do` | `In Progress` | `Done` | `Blocked` | `blocked-for-opus` | `blocked-for-user`
*   **Model Suitability:** `opus-only` | `sonnet-ready` | `either`
*   **User Action Required:** [If blocked-for-user, specify what's needed: API key, OAuth setup, webhook URL, etc.]
*   **Context:** [Why this task is necessary]
*   **Action Plan:** [What needs to be done]
*   **Validation:** [How to verify completion]
```

## Monitoring & Analytics

### Metrics to Track
- API call volume
- Response times
- Error rates
- Rate limit usage
- Webhook delivery success

### Logging
```typescript
// lib/integrations/[service-name]/logger.ts
export function logApiCall(
  method: string,
  endpoint: string,
  duration: number,
  status: number
) {
  logger.info('API Call', {
    service: 'service-name',
    method,
    endpoint,
    duration,
    status,
    timestamp: new Date().toISOString(),
  });
}
```

## Security Considerations

### API Key Management
- [ ] Store in environment variables
- [ ] Rotate keys quarterly
- [ ] Use separate keys per environment
- [ ] Monitor for exposed keys

### Data Protection
- [ ] Encrypt sensitive data
- [ ] Validate all inputs
- [ ] Sanitize outputs
- [ ] Implement CORS properly

## Cost Management

### API Costs
- **Free Tier**: 1,000 calls/month
- **Basic**: $29/month (10,000 calls)
- **Pro**: $99/month (100,000 calls)

### Optimization Strategies
- Implement aggressive caching
- Batch API calls when possible
- Use webhooks vs polling
- Monitor usage daily

## Sub-Agent Commands

### Integration Development
```bash
@new-feature "API integration layer" --target lib/integrations/
@test-gen lib/integrations/ --integration-tests
@refactor lib/integrations/ --extract-common
```

### Performance Analysis
```bash
@perf-optimize lib/integrations/ --focus-on-api-calls
@arch-review lib/integrations/ --check-patterns
```

## Troubleshooting

### Common Issues

#### Authentication Failures
- Verify API credentials
- Check token expiration
- Validate OAuth flow

#### Rate Limit Errors
- Implement exponential backoff
- Add request queuing
- Monitor usage patterns

#### Timeout Issues
- Increase timeout limits
- Optimize request payload
- Consider async processing

## Success Criteria
- [ ] All endpoints integrated
- [ ] < 1% error rate
- [ ] < 500ms average response
- [ ] 99.9% uptime
- [ ] Comprehensive test coverage

## Migration Plan
If replacing existing integration:
1. Run new integration in parallel
2. Compare results for accuracy
3. Gradually shift traffic
4. Monitor for issues
5. Deprecate old integration

## Error Handling {#error-handling}
<!-- Error handling strategies documented in code samples above -->

## Progress Log {#progress-log}
<!-- APPEND new entries, don't replace -->
- [Date]: Integration planning started
- [Date]: API client implementation begun
- [Date]: Testing infrastructure ready
- [Date]: Integration deployed to staging

## Handoff History {#handoff-history}
<!-- Track model transitions and blockers -->

<!-- HANDOFF: From [Model] to [Model] - [Date] -->
<!-- Summary of what was completed and what needs attention -->
<!-- END HANDOFF -->

## Gemini's Development Considerations
<!-- This section will be added by Gemini during review -->
<!-- Do not edit this section unless you are Gemini -->

---
*Template Version: 1.3*