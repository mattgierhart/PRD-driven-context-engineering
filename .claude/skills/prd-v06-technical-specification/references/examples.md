# Technical Specification Examples

## Complete API Specification Example

### Reports API

```
API-001: Create Report
Method: POST
Path: /api/v1/reports
Purpose: Create a new report from template and data source
Auth: User

Journey: UJ-001 (Step 1 - Click Create Report)
Screen: SCR-002 (Report Builder)

Request:
  Headers:
    - Authorization: Bearer <token>
    - Content-Type: application/json
  Body:
    {
      title: string (required, 1-255 chars) — Report display name
      templateId: uuid (required) — Template to use
      dataSourceId: uuid (required) — Data source to query
      options: {
        dateRange: {
          start: ISO8601 (required) — Period start
          end: ISO8601 (required) — Period end
        }
        filters: [{
          field: string — Field to filter
          operator: "eq" | "gt" | "lt" | "contains" — Comparison
          value: any — Filter value
        }]
      }
    }

Response:
  Success (201 Created):
    {
      data: {
        id: uuid
        title: string
        status: "pending"
        createdAt: ISO8601
        estimatedCompletion: ISO8601
      }
    }
  Errors:
    - 400 Bad Request: Missing required field, invalid templateId format
    - 401 Unauthorized: Invalid or expired token
    - 403 Forbidden: User doesn't own the data source
    - 404 Not Found: Template or data source doesn't exist
    - 422 Unprocessable: Date range invalid (end before start)
    - 429 Too Many Requests: Rate limit exceeded

Business Rules: BR-015 (max 100 reports), BR-016 (date range max 1 year)
Data: DBT-001 (reports), DBT-002 (templates), DBT-003 (data_sources)
Rate Limit: 10/minute
```

```
API-002: Get Report
Method: GET
Path: /api/v1/reports/{id}
Purpose: Retrieve a single report with its current status
Auth: User

Journey: UJ-001 (Step 4 - View Report)
Screen: SCR-003 (Report Detail)

Request:
  Headers:
    - Authorization: Bearer <token>
  Params:
    - id: uuid (required) — Report ID

Response:
  Success (200 OK):
    {
      data: {
        id: uuid
        title: string
        status: "pending" | "generating" | "ready" | "failed"
        template: {
          id: uuid
          name: string
        }
        dataSource: {
          id: uuid
          name: string
        }
        options: { ... }
        outputUrl: string | null — Download URL when ready
        createdAt: ISO8601
        updatedAt: ISO8601
      }
    }
  Errors:
    - 401 Unauthorized: Invalid or expired token
    - 403 Forbidden: Report belongs to another user
    - 404 Not Found: Report doesn't exist

Business Rules: None
Data: DBT-001 (reports), DBT-002 (templates), DBT-003 (data_sources)
Rate Limit: 60/minute
```

```
API-003: List Reports
Method: GET
Path: /api/v1/reports
Purpose: List user's reports with pagination and filtering
Auth: User

Journey: UJ-003 (Step 1 - View Report List)
Screen: SCR-001 (Dashboard - Recent Reports)

Request:
  Headers:
    - Authorization: Bearer <token>
  Query:
    - limit: integer (optional, default 20, max 100) — Items per page
    - cursor: string (optional) — Pagination cursor
    - status: string (optional) — Filter by status
    - sort: "created" | "updated" (optional, default "created") — Sort field
    - order: "asc" | "desc" (optional, default "desc") — Sort direction

Response:
  Success (200 OK):
    {
      data: [{
        id: uuid
        title: string
        status: string
        createdAt: ISO8601
      }]
      pagination: {
        nextCursor: string | null
        hasMore: boolean
        total: integer
      }
    }
  Errors:
    - 400 Bad Request: Invalid query parameters
    - 401 Unauthorized: Invalid or expired token

Business Rules: None (only returns user's own reports via RLS)
Data: DBT-001 (reports)
Rate Limit: 30/minute
```

---

## Complete Data Model Example

### Reports Schema

```
DBT-001: Reports
Purpose: Stores user-generated reports with configuration and generation status
Table: reports

Fields:
  - id: uuid — Primary key, default gen_random_uuid()
  - user_id: uuid — Report owner [NOT NULL, FK → users.id]
  - title: varchar(255) — Display name [NOT NULL]
  - template_id: uuid — Template used [NOT NULL, FK → templates.id]
  - data_source_id: uuid — Data source [NOT NULL, FK → data_sources.id]
  - status: report_status — Generation status [NOT NULL, DEFAULT 'pending']
  - options: jsonb — Configuration (date range, filters) [NOT NULL, DEFAULT '{}']
  - output_url: varchar(500) — Generated file URL [NULL until ready]
  - error_message: text — Error details if failed [NULL]
  - created_at: timestamp with time zone [NOT NULL, DEFAULT now()]
  - updated_at: timestamp with time zone [NOT NULL, DEFAULT now()]

Relationships:
  - belongs_to: DBT-010 (users) via user_id
  - belongs_to: DBT-002 (templates) via template_id
  - belongs_to: DBT-003 (data_sources) via data_source_id

Indexes:
  - PRIMARY KEY (id)
  - idx_reports_user_id ON (user_id) — Filter by user
  - idx_reports_user_created ON (user_id, created_at DESC) — List recent
  - idx_reports_status ON (status) WHERE status = 'pending' — Job queue

Constraints:
  - user_id: NOT NULL, REFERENCES users(id) ON DELETE CASCADE
  - template_id: NOT NULL, REFERENCES templates(id) ON DELETE RESTRICT
  - data_source_id: NOT NULL, REFERENCES data_sources(id) ON DELETE RESTRICT
  - title: NOT NULL, CHECK (char_length(title) BETWEEN 1 AND 255)
  - status: NOT NULL

Business Rules: BR-015 (max 100 reports per user — enforced in API)
APIs: API-001, API-002, API-003, API-004, API-005

-- Enum type
CREATE TYPE report_status AS ENUM ('pending', 'generating', 'ready', 'failed');

-- Row Level Security
ALTER TABLE reports ENABLE ROW LEVEL SECURITY;
CREATE POLICY reports_user_policy ON reports
  USING (user_id = auth.uid());
```

```
DBT-002: Templates
Purpose: Report templates with structure and formatting definitions
Table: templates

Fields:
  - id: uuid — Primary key
  - name: varchar(100) — Template name [NOT NULL]
  - description: text — Template description [NULL]
  - category: varchar(50) — Template category [NOT NULL]
  - config: jsonb — Template configuration [NOT NULL]
  - is_public: boolean — Available to all users [NOT NULL, DEFAULT false]
  - created_by: uuid — Template author [NULL for system templates]
  - created_at: timestamp with time zone [NOT NULL, DEFAULT now()]
  - updated_at: timestamp with time zone [NOT NULL, DEFAULT now()]

Relationships:
  - has_many: DBT-001 (reports)
  - belongs_to: DBT-010 (users) via created_by [optional]

Indexes:
  - PRIMARY KEY (id)
  - idx_templates_category ON (category) — Filter by category
  - idx_templates_public ON (is_public) WHERE is_public = true — List public

Constraints:
  - name: NOT NULL, CHECK (char_length(name) BETWEEN 1 AND 100)
  - category: NOT NULL

Business Rules: None
APIs: API-010 (list templates), API-011 (get template)
```

---

## Anti-Pattern Examples

### Bad: Vague API Response

```
API-001: Get Data
Method: GET
Path: /api/data
Response:
  Success (200):
    {
      data: any
    }
```

**Problem**: `any` doesn't tell developers what to expect.

### Good: Specific API Response

```
API-001: Get Report
Method: GET
Path: /api/reports/{id}
Response:
  Success (200):
    {
      data: {
        id: uuid
        title: string
        status: "pending" | "ready" | "failed"
        createdAt: ISO8601
      }
    }
```

---

### Bad: Missing Error Cases

```
API-001: Delete Report
Method: DELETE
Path: /api/reports/{id}
Response:
  Success (204): No content
```

**Problem**: What happens if report doesn't exist? Not authorized?

### Good: Complete Error Handling

```
API-001: Delete Report
Method: DELETE
Path: /api/reports/{id}
Response:
  Success (204): No content
  Errors:
    - 401: Unauthorized — Token invalid or expired
    - 403: Forbidden — Report belongs to another user
    - 404: Not found — Report doesn't exist
    - 409: Conflict — Report is currently generating
```
