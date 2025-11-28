# PRD v0.8 Deployment & Ops Intake Instructions

> Part of the PRD Instruction Library (`docs/prd/instructions/`). At v0.8, ownership shifts from APOLLO (Build) to **JANUS (Deployment & Ops Lead)**. This file uses `janus-intake.md` to reflect that transition.

## Mission Alignment
**Objective:** Prepare the product for safe, repeatable deployment with release criteria, staging strategy, operational playbooks, and monitoring—ready for production launch.
**Inputs:** PRD v0.7 (build plan, EPICs completed), passing test suites, DEP-* dependencies provisioned, and any operational constraints from stakeholders.
**Deliverable:** PRD v0.8 sections (`Release Criteria`, `Deployment Pipeline`, `Staging Strategy`, `Operational Playbook`, `Monitoring & Alerting`), updated SoT entries for DEP-*/OPS-*/MON- IDs, and Gate 4 (Deployment) readiness assessment.

## ID Interlock Map
- **Inputs:**
  - Build artifacts and passing TEST-* from v0.7
  - DEP-* dependencies with provisioning status
  - BR-* constraints affecting deployment (compliance, data residency, uptime SLAs)
  - ARC-* architecture decisions impacting infrastructure
- **Processing:**
  - Validate all DEP-* dependencies are production-ready
  - Create OPS-* IDs for operational procedures (rollback, incident response, scaling)
  - Create MON-* IDs for monitoring, alerting, and observability
  - Document SEC-* security controls for production environment
- **Outputs:**
  - `DEP-*` entries updated with production configuration and verification
  - `OPS-*` entries for runbooks and operational procedures
  - `MON-*` entries for dashboards, alerts, and SLOs
  - `SEC-*` entries for security controls, access policies, and audit requirements
  - Gate 4 decision log with deployment readiness assessment

## Business Rule Criteria & Key Questions
1. **Release Criteria Clarity:** Is it unambiguous what must be true before deploying to production? Can any engineer verify readiness?
2. **Rollback Safety:** If deployment fails, can we revert within the defined SLO? Is the procedure documented?
3. **Environment Parity:** Do staging and production share the same configuration patterns? Are differences documented?
4. **Monitoring Coverage:** Are all critical paths instrumented? Do alerts exist for SLO breaches?
5. **Security Posture:** Are secrets managed properly? Is access control configured? Are audit logs enabled?
6. **Operational Handoff:** Can an on-call engineer respond to incidents using only the documented runbooks?
7. **Lifecycle Continuity:** Does Gate 4 criteria specify what evidence triggers v0.9 (GTM) readiness?

## Intake Checklist
Confirm inputs include:
- [ ] PRD v0.7 with Gate 3 PASS decision
- [ ] All critical EPICs completed with passing tests
- [ ] DEP-* dependencies list with provisioning status
- [ ] Infrastructure configuration (IaC, environment variables)
- [ ] Security requirements and compliance constraints
- [ ] Uptime and performance SLO targets

## Processing Workflow
1. **Context Load:** Review PRD v0.7, README, completed EPICs, and SoT entries. Note any deployment blockers from build phase.
2. **Dependency Verification:** Audit all DEP-* entries. Confirm production credentials, quotas, and configurations are in place.
3. **Environment Setup:** Document staging and production environment configurations. Ensure parity where required.
4. **Pipeline Definition:** Define CI/CD pipeline stages: build, test, staging deploy, smoke tests, production deploy, verification.
5. **Release Criteria:** Establish explicit go/no-go criteria (test pass rates, security scans, performance benchmarks, manual sign-offs).
6. **Staging Strategy:** Define staging deployment process, smoke test suite, and promotion criteria to production.
7. **Security Controls:** Document SEC-* entries for secrets management, access control, encryption, and audit logging.
8. **Monitoring Setup:** Define MON-* entries for dashboards, alerts, and SLO tracking. Instrument critical paths.
9. **Operational Playbooks:** Create OPS-* entries for common procedures: deployment, rollback, scaling, incident response.
10. **Disaster Recovery:** Document backup strategy, recovery procedures, and RTO/RPO targets.
11. **Gate 4 Assessment:** Define what constitutes "deployable" and verify all criteria can be met.
12. **Documentation Update:** Update PRD v0.8 sections, create SoT entries, and prepare handoff to GTM (JANUS continues or hands to GTM lead).

## Output Template Snippet
```markdown
## Deployment & Ops (v0.8)

### Release Criteria
| Criterion | Metric | Target | Verification |
|-----------|--------|--------|--------------|
| Test Suite | Pass rate | 100% critical, 95% all | CI pipeline |
| Security Scan | Critical vulnerabilities | 0 | Snyk/Trivy |
| Performance | P95 latency | <200ms | Load test |
| Manual Review | Sign-off | Required | Checklist |

### Deployment Pipeline
```
[Build] → [Unit Tests] → [Integration Tests] → [Security Scan]
    → [Staging Deploy] → [Smoke Tests] → [Manual QA]
    → [Production Deploy] → [Health Check] → [Monitoring]
```

### Environment Configuration
| Environment | DEP- IDs | Config Source | Secrets |
|-------------|----------|---------------|---------|
| Staging | DEP-001..005 | .env.staging | Vault/staging |
| Production | DEP-001..005 | .env.production | Vault/prod |

### Monitoring & Alerting (MON-*)
| MON ID | Metric | Threshold | Alert Channel |
|--------|--------|-----------|---------------|
| MON-001 | Error rate | >1% 5min | PagerDuty |
| MON-002 | P95 latency | >500ms | Slack |
| MON-003 | Uptime | <99.9% day | PagerDuty |

### Operational Playbooks (OPS-*)
| OPS ID | Procedure | Trigger | Owner |
|--------|-----------|---------|-------|
| OPS-001 | Rollback | Failed deploy | On-call |
| OPS-002 | Scale up | High load alert | On-call |
| OPS-003 | Incident response | P1 alert | On-call |

### Gate 4 Criteria
- [ ] All release criteria met
- [ ] Staging deployment successful with smoke tests passing
- [ ] Security scan clean (0 critical, <5 high)
- [ ] Monitoring and alerting configured
- [ ] Runbooks documented and reviewed
- [ ] Rollback procedure tested
- [ ] On-call rotation established
```

## Quality Gates
| Checkpoint | Pass Condition |
|------------|----------------|
| **Release Criteria** | All criteria defined with measurable targets and verification methods |
| **Pipeline Coverage** | CI/CD covers build, test, security, deploy, and verification |
| **Environment Parity** | Staging mirrors production configuration (documented exceptions only) |
| **Monitoring Completeness** | All critical paths have MON-* entries with alerts |
| **Runbook Quality** | OPS-* procedures are actionable by any on-call engineer |
| **Security Sign-off** | SEC-* controls documented and verified |
| **Rollback Tested** | Rollback procedure executed successfully in staging |

## Collaboration & Handoff
- Store operational playbooks in `source-of-truth/deployment-playbook.md` with OPS-* IDs.
- Create `source-of-truth/monitoring-playbook.md` for MON-* entries.
- Coordinate with APOLLO on any build changes needed for deployment.
- Prepare handoff notes for v0.9 (GTM) including operational status and known limitations.
- Establish on-call rotation and escalation paths before production launch.

## Reporting Checklist
- [ ] PRD v0.8 Deployment & Ops section completed
- [ ] Release criteria defined and documented
- [ ] CI/CD pipeline configured and tested
- [ ] Staging environment deployed and verified
- [ ] MON-* entries created with alerts configured
- [ ] OPS-* runbooks documented and reviewed
- [ ] SEC-* security controls verified
- [ ] Gate 4 criteria defined and achievable
- [ ] On-call rotation established

---

## Ready-to-Use Agent Prompt

> **Copy the block below into your AI assistant to execute v0.8 Deployment & Ops intake.**

```
You are JANUS, the Deployment & Ops Lead for Gear Heart Methodology (GHM).

## Your Mission
Prepare the product for safe, repeatable production deployment with release criteria, operational playbooks, and monitoring.

## Context to Load
Before responding, ensure you have access to:
1. PRD.md (especially v0.7 Build Plan and completed EPICs)
2. README.md (current status and any deployment blockers)
3. source-of-truth/ files for: DEP-*, TEST-*, ARC-*, BR-* IDs
4. Infrastructure configuration files (if any)
5. Compliance/security requirements

## Your Deliverables
Produce the following artifacts:

### 1. Release Criteria Table
Define explicit go/no-go criteria with:
- Criterion name
- Measurable target
- Verification method
- Owner for sign-off

### 2. Deployment Pipeline
Document the full CI/CD flow:
- Build and test stages
- Security scanning
- Staging deployment
- Smoke tests
- Production deployment
- Health checks

### 3. Environment Configuration
For each environment (staging, production):
- DEP-* dependencies required
- Configuration sources
- Secrets management approach
- Key differences and rationale

### 4. Monitoring & Alerting (MON-* IDs)
For each critical path:
- Metric being tracked
- Threshold for alerting
- Alert severity and channel
- Response procedure reference

### 5. Operational Playbooks (OPS-* IDs)
Document procedures for:
- OPS-DEPLOY: Standard deployment
- OPS-ROLLBACK: Rollback procedure
- OPS-SCALE: Scaling up/down
- OPS-INCIDENT: Incident response

### 6. Security Controls (SEC-* IDs)
Document:
- Secrets management
- Access control
- Encryption (at rest, in transit)
- Audit logging

## Output Format
Structure your response as:
1. Executive Summary (deployment readiness assessment)
2. Release Criteria Table
3. Deployment Pipeline Diagram
4. Environment Configuration Matrix
5. MON-* Registry
6. OPS-* Playbook Index
7. SEC-* Controls Summary
8. Gate 4 Criteria Checklist
9. Risks and Open Items

## Constraints
- Every MON-* must have an alert threshold and response procedure
- Every OPS-* must be executable by someone unfamiliar with the codebase
- Security controls must address secrets, access, and audit requirements
- Rollback procedure must be tested before Gate 4 PASS
- Document any staging/production differences explicitly

## Gate 4 Success Criteria
Your output should enable a PASS on Gate 4 (Deployment) when:
- All release criteria are defined and measurable
- CI/CD pipeline is configured and tested
- Monitoring covers all critical paths
- Runbooks exist for common operations
- Security controls are documented and verified
- Rollback has been tested in staging
```
