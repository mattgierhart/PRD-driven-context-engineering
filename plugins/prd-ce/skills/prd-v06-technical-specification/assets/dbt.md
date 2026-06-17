# DBT- Template

Copy and fill for each data entity:

```
DBT-XXX: [Entity Name]
Purpose: [What this entity represents]
Table: [database_table_name]

Fields:
  - id: uuid — Primary key
  - [field_name]: [type] — Description [constraints]
  - created_at: timestamp — Record creation
  - updated_at: timestamp — Last modification

Relationships:
  - belongs_to: [DBT-YYY] via [foreign_key]
  - has_many: [DBT-ZZZ]

Indexes:
  - [field_name] — [Query pattern it supports]

Constraints:
  - [field]: [constraint description]

Business Rules: [BR-XXX]
APIs: [API-XXX, API-YYY]
```

## Common Field Types

| Type | Use For | Example |
|------|---------|---------|
| uuid | Primary keys, references | id, user_id |
| varchar(N) | Short text with limit | title, name |
| text | Long text, no limit | description, content |
| integer | Whole numbers | count, quantity |
| decimal(P,S) | Money, precise numbers | price, amount |
| boolean | True/false | is_active, is_deleted |
| timestamp | Date + time | created_at, due_date |
| jsonb | Flexible structured data | options, metadata |
| enum | Fixed set of values | status, role |

## Common Constraints

| Constraint | Meaning |
|------------|---------|
| NOT NULL | Field is required |
| UNIQUE | No duplicates allowed |
| DEFAULT X | Value if not provided |
| CHECK (expr) | Custom validation |
| REFERENCES | Foreign key |

## Checklist Before Adding

- [ ] Is this entity needed by an API-?
- [ ] Are all fields documented with types?
- [ ] Are relationships defined?
- [ ] Are indexes planned for query patterns?
- [ ] Are constraints (NOT NULL, UNIQUE) specified?
- [ ] Is there a BR- that affects this entity?
