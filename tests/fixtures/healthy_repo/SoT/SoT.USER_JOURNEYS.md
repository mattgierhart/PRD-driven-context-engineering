# User Journeys (SoT File)

## UJ-001 | List and archive an item

- **Step 1**: user logs in
- **Step 2**: user views items via API-001
- **Step 3**: user archives an item via API-002 — audit logged per BR-002
- **Related IDs**: [API-001](SoT.API_CONTRACTS.md#api-001), [API-002](SoT.API_CONTRACTS.md#api-002), [BR-002](SoT.BUSINESS_RULES.md#br-002).

## UJ-002 | Sign up and select region

- **Step 1**: user visits signup page
- **Step 2**: user authenticates via OAuth (TECH-003)
- **Step 3**: user selects storage region; account row persisted per BR-003
- **Related IDs**: [BR-003](SoT.BUSINESS_RULES.md#br-003), [TECH-003](SoT.TECHNICAL_DECISIONS.md#tech-003), [DBT-003](SoT.DATA_MODEL.md#dbt-003).

## UJ-003 | Monitor service health

- **Step 1**: operator calls API-003 health endpoint
- **Step 2**: response shows status + any degraded subsystems
- **Step 3**: if degraded, oncall consults runbook
- **Related IDs**: [API-003](SoT.API_CONTRACTS.md#api-003), [ARC-001](SoT.TECHNICAL_DECISIONS.md#arc-001).
