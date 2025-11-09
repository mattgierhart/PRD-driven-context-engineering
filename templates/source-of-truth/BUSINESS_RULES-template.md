---
version: 1.0
purpose: Source of Truth file for all business rules and constraints. Each rule has a unique ID for cross-referencing.
id_prefix: BR-XXX
last_updated: YYYY-MM-DD
authority: This is a SoT file - IDs created here are referenced by PRD.md, API_CONTRACTS.md, EPICs, and code
---

# Business Rules (SoT File)

> **Purpose**: Complete specifications for all business constraints and enforcement policies.
> **ID Prefix**: BR-XXX
> **Status**: Active SoT file
> **Cross-References**: Referenced by PRD.md, API_CONTRACTS.md, USER-JOURNEYS.md, testing-playbook.md, EPICs

## Navigation by Category

**Pricing & Entitlements** (BR-001 to BR-099):
- [BR-001](#br-001-rule-name) - {Rule name}
- [BR-002](#br-002-rule-name) - {Rule name}

**Data & Security** (BR-101 to BR-199):
- [BR-101](#br-101-rule-name) - {Rule name}
- [BR-102](#br-102-rule-name) - {Rule name}

**User Permissions** (BR-201 to BR-299):
- [BR-201](#br-201-rule-name) - {Rule name}

**Compliance & Legal** (BR-301 to BR-399):
- [BR-301](#br-301-rule-name) - {Rule name}

**Performance & Limits** (BR-401 to BR-499):
- [BR-401](#br-401-rule-name) - {Rule name}

---

## BR-001: {Rule Name}

**ID**: BR-001
**Category**: Pricing & Entitlements | Data & Security | User Permissions | Compliance & Legal | Performance & Limits
**Status**: Active | Deprecated | Planned
**Owner**: Product Team | Engineering | Compliance
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD
**Severity**: Critical | High | Medium | Low

### Rule Statement

{Clear, enforceable statement of the business rule. Use imperative language.}

**Example**: "Free tier users MUST be limited to a maximum of 3 products. Any attempt to add a 4th product MUST be blocked with upgrade prompt."

### Rationale

**Business Driver**: {Why this rule exists from a business perspective}
**User Impact**: {How this affects user experience}
**Revenue Impact**: {How this relates to monetization/costs}

### Enforcement Points

**Primary Enforcement**: {Where the rule is primarily enforced}
- Location: {File path or service}
- Method: Server-side | Client-side | Hybrid
- Timing: On action | Background job | Real-time validation

**Secondary Enforcement** (if applicable):
- {Additional enforcement points for defense-in-depth}

### Validation Logic

**Technical Implementation**:

```typescript
// Example enforcement logic
function validateBusinessRule_BR001(user: User, productCount: number): ValidationResult {
  if (user.tier === 'FREE' && productCount >= 3) {
    return {
      valid: false,
      errorCode: 'BR_001_VIOLATION',
      message: 'Free tier limited to 3 products. Upgrade to add more.',
      action: 'SHOW_UPGRADE_PROMPT'
    };
  }
  return { valid: true };
}
```

**Validation Criteria**:
- Input: {What data is checked}
- Logic: {How the rule is evaluated}
- Output: {What happens on pass/fail}

### Related IDs

**Enforced By APIs**:
- [API-XXX](API_CONTRACTS.md#api-xxx) - {Endpoint that enforces this rule}
- [API-YYY](API_CONTRACTS.md#api-yyy) - {Another enforcement point}

**Affects User Journeys**:
- [UJ-XXX](USER-JOURNEYS.md#uj-xxx) - {Journey where rule applies}
- [UJ-YYY](USER-JOURNEYS.md#uj-yyy) - {Another affected journey}

**Database Constraints**:
- [DBT-XXX](ACTUAL-SCHEMA.md#dbt-xxx) - {Table with constraint}
- Schema constraint: {SQL constraint if applicable}

**Validated By Tests**:
- [TEST-XXX](testing-playbook.md#test-xxx) - {Test validating compliance}
- [TEST-YYY](testing-playbook.md#test-yyy) - {Test validating violation handling}

**Referenced in PRD**:
- Section: [PRD.md#{section}](PRD.md#{section})

**Customer Feedback**:
- [CFD-XXX](customer-feedback.md#cfd-xxx) - {Feedback about this rule}

### Exceptions

**Allowed Exceptions**:
1. **{Exception scenario}**
   - Trigger: {When this exception applies}
   - Approval: {Who can authorize}
   - Duration: {How long exception lasts}
   - Example: Beta testers may exceed limit during testing phase

**Prohibited Exceptions**:
- {Scenarios where NO exceptions are allowed}
- {Reason for strict enforcement}

### Error Handling

**When Rule is Violated**:
- Error Code: `BR_001_VIOLATION`
- User Message: "{User-friendly error message}"
- Log Entry: "{What gets logged for debugging}"
- Recovery Action: {What user can do to resolve}

**Graceful Degradation** (if applicable):
- {How system behaves if enforcement temporarily fails}
- {Fallback behavior}

### Business Impact

**If Rule is Violated**:
- Revenue Impact: {Potential revenue loss/leakage}
- User Experience Impact: {How users are affected}
- Compliance Risk: {Legal/regulatory implications}
- Brand Impact: {Reputation/trust implications}

**Metrics to Monitor**:
- Violation rate: {X}% (target: <{Y}%)
- False positive rate: {X}% (target: <{Y}%)
- User complaints: {Count/month}

### Compliance & Regulations

**Regulatory Requirements** (if applicable):
- Framework: {GDPR | HIPAA | PCI-DSS | SOC2 | etc.}
- Specific Requirement: {Citation or reference}
- Audit Trail: {What must be logged}
- Retention Period: {How long to keep records}

### Configuration

**Environment-Specific Values**:

```yaml
# Development
free_tier_product_limit: 5  # Looser for testing

# Staging
free_tier_product_limit: 3  # Production rules

# Production
free_tier_product_limit: 3  # Strict enforcement
```

**Feature Flags** (if applicable):
- Flag Name: `enforce_br_001`
- Default State: Enabled
- Override Capability: Admin-only

### Detailed Specification

For additional context, implementation notes, and historical decisions, see:
- [business-rules/{filename}.md](business-rules/{filename}.md)
- Confluence/Wiki: {Link if applicable}

### Version History

| Version | Date | Changes | Updated By | Reason |
|---------|------|---------|------------|--------|
| 1.0 | YYYY-MM-DD | Initial creation | {Name} | {Why rule created} |
| 1.1 | YYYY-MM-DD | {Change description} | {Name} | {Business justification} |

---

## BR-002: {Next Rule Name}

{Repeat the above structure for each business rule}

---

## Deprecated Rules

### BR-XXX: {Deprecated Rule Name} [DEPRECATED]

**Status**: Deprecated (YYYY-MM-DD)
**Replacement**: [BR-YYY](#br-yyy-rule-name) | None (rule no longer needed)
**Reason**: {Why rule was deprecated}
**Migration Guide**: {How to transition to new rule if applicable}
**Enforcement Stopped**: {When enforcement was disabled}
**Code Cleanup**: {When related code can be removed}

---

## Cross-Reference Index

> **Auto-Generated Section**: Run `npm run codex:sync-business-rules` to rebuild

**Rules by API**:
- API-045 enforces: BR-001, BR-102
- API-046 enforces: BR-001

**Rules by User Journey**:
- UJ-101 affected by: BR-001, BR-102, BR-203
- UJ-102 affected by: BR-001

**Rules by Test Coverage**:
- TEST-301 validates: BR-001 (compliance path)
- TEST-302 validates: BR-001 (violation handling)

**Rules by Severity**:
- Critical: BR-001, BR-305, BR-401
- High: BR-002, BR-103
- Medium: BR-204, BR-205

**Rules by Compliance Framework**:
- HIPAA: BR-301, BR-302, BR-303
- GDPR: BR-101, BR-102, BR-304
- PCI-DSS: BR-401, BR-402

---

*End of BUSINESS_RULES.md - This SoT file is the authoritative source for all BR-XXX IDs*
