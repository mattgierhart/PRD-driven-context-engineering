---
version: 2.1
purpose: Central command center with file operations tracking and single source of truth for product development
learnings_integrated: Example Product documentation crisis insights, File Operations Manifest integration
last_updated: 2025-09-06
template_type: product_command_center
change_log:
  - date: 2025-09-06
    change: Consolidated templates; archived COMMAND-CENTER-template.md; added change_log to metadata
---

# 🏛️ [PRODUCT_NAME] COMMAND CENTER & SINGLE SOURCE OF TRUTH

> **Version**: 2.0  
> **Last Updated**: [DATE]  
> **Product Owner**: Claude Code Product Owner Agent
> **Status**: [🟢 OPERATIONAL | 🟡 ACTIVE DEVELOPMENT | 🔴 BLOCKED]  
> **Live Sites**: [List all live URLs]

---

## 🎯 SINGLE SOURCE OF TRUTH TABLE
**CRITICAL**: These are the ONLY official values. Any conflicting numbers in other documents are INCORRECT.

| Metric | Official Value | Formula/Source | Last Validated | Authority |
|--------|---------------|----------------|----------------|-----------|
| **Risk Score** | [NUMBER] | `(Complexity × AI_Uncertainty × Integration_Points) / (Test_Coverage / 100)` | [DATE] | This table |
| **Golden Dataset Size** | [NUMBER] samples | Count from `/golden-datasets/` | [DATE] | This table |
| **Test Coverage Target** | [X]% | Minimum viable coverage | [DATE] | This table |
| **Sprint Velocity** | [X] story points | 3-sprint average | [DATE] | This table |
| **Context Window Budget** | [X] tokens | Per-session maximum | [DATE] | This table |
| **Infrastructure Cost** | $[X]/month | Actual from billing | [DATE] | This table |
| **Active Users** | [NUMBER] | From analytics | [DATE] | This table |
| **MRR** | $[X] | Stripe dashboard | [DATE] | This table |
| **Completion** | [X]% | Epic-weighted average | [DATE] | This table |
| **File Complexity Score** | [X] | `(Files_Created + Files_Modified × 2) / Total_Files` | [DATE] | This table |
| **Planned vs Actual Alignment** | [X]% | `(Planned_Operations_Completed / Total_Planned) × 100` | [DATE] | This table |
| **Unplanned Files Created** | [X] | Count from EPIC manifests | [DATE] | This table |

**Documentation Hierarchy**:
1. THIS TABLE (absolute authority)
2. Product Owner Running Log (context and history)
3. PRD.md (requirements, references this table)
4. EPIC files (execution details, reference this table)
5. All other documents (must reference above)

---

## 🔄 TECHNICAL PIVOTS & STRATEGIC CHANGES
**CRITICAL**: All major decisions and pivots MUST be documented here immediately.

### Active Pivots (Current Strategy)
| Date | From → To | Rationale | Impact | Risk Score Change |
|------|-----------|-----------|--------|-------------------|
| [DATE] | [Old approach] → [New approach] | [Why changed] | [What it affects] | [Old] → [New] |

### Historical Pivots (Learning Record)
| Date | Decision | Why It Happened | Lesson Learned |
|------|----------|-----------------|----------------|
| [DATE] | [What changed] | [Root cause] | [What we learned] |

---

## 🗺️ CODEBASE MAP & STRUCTURE

### ⚠️ SYMLINK VERIFICATION
```bash
# CRITICAL: Prevent .claude directory duplication
# This should output: .claude -> /development/.claude
ls -la .claude

# If not a symlink, fix immediately:
rm -rf .claude
ln -s /Users/mattgierhart/Library/CloudStorage/Dropbox/development/.claude .claude
```

### ✅ ACTIVE DIRECTORIES (USE THESE!)

```
/products/[product-name]/
├── .claude -> /development/.claude    ⚠️ MUST BE SYMLINK
├── PRD.md                            ← Single requirements file (v0.1→v0.2→v1.0)
├── claude.md                          ← Product-specific instructions
├── COMMAND_CENTER.md                  ← THIS FILE (single source of truth)
├── active-projects/
│   └── current/                       ← ONLY active development
│       ├── backend/                   ← ONE backend implementation
│       ├── frontend/                  ← ONE frontend implementation
│       └── mobile/                    ← ONE mobile implementation
├── epics/                             ← Development planning
│   ├── EPIC-00-[name].md             ← Progressive updates only
│   └── EPIC-01-[name].md             ← Never create new versions
└── archive/                           ← Old code (reference only)
    └── [timestamp]-[description]/    ← Archived with context
```

### ❌ FORBIDDEN PATTERNS (CI/CD WILL REJECT)
```
❌ active-projects/mvp/                ← No version-specific folders
❌ active-projects/v1.0/               ← Use Git tags instead
❌ backend-api/                        ← Use standard names only
❌ PRD-v2.md                          ← Update PRD.md instead
❌ .claude/ (as directory)             ← Must be symlink
❌ products/[name]/[name]-fresh/       ← No nested structures
```

---

## 📊 PROJECT HEALTH DASHBOARD

### Risk Score Calculation
```
Risk Score = (Complexity × AI_Uncertainty × Integration_Points) / (Test_Coverage / 100)

Where:
- Complexity: 1-10 (codebase complexity)
- AI_Uncertainty: 1-10 (how much we rely on AI behavior)
- Integration_Points: 1-10 (external dependencies)
- Test_Coverage: 0-100 (actual coverage percentage)

Current Calculation:
[X] × [Y] × [Z] / ([TC]/100) = [RISK_SCORE]
```

### Development Metrics (Effort-Based)
| Metric | Current | Target | Trend | Notes |
|--------|---------|--------|-------|-------|
| **Story Points Completed** | [X] | [Y] per sprint | [↑↓→] | Not calendar days |
| **Context Windows Used** | [X] | [Y] per session | [↑↓→] | AI effort metric |
| **Test Coverage** | [X]% | [Y]% | [↑↓→] | Affects risk score |
| **Tech Debt Score** | [X] | <[Y] | [↑↓→] | From static analysis |
| **Performance Score** | [X]/100 | >[Y] | [↑↓→] | Lighthouse/similar |

### File Operations Tracking
| Metric | Current Sprint | Cumulative | Threshold | Status |
|--------|---------------|------------|-----------|--------|
| **Files Created as Planned** | [X] | [Y] | - | ✅ |
| **Files Modified as Planned** | [X] | [Y] | - | ✅ |
| **Unplanned Files Created** | [X] | [Y] | <5/sprint | [✅⚠️] |
| **Unplanned Files Modified** | [X] | [Y] | <10/sprint | [✅⚠️] |
| **Abandoned Files** | [X] | [Y] | <2/sprint | [✅⚠️] |
| **File Operation Alignment** | [X]% | [Y]% | >80% | [✅⚠️] |

**File Debt Accumulation**:
- **Technical Debt from Unplanned Files**: [List files and impact]
- **Refactoring Candidates**: [Files with 3+ unplanned modifications]
- **Architecture Impact**: [Minimal/Moderate/Significant]

---

## 🚨 PRODUCT OWNER ACTIVATION TRIGGERS

### MANDATORY Engagement Events
The Product Owner Agent MUST be invoked when:
1. ✅ Product name "[PRODUCT_NAME]" is mentioned
2. ✅ Strategic pivot or major decision occurs
3. ✅ Risk score changes by >10%
4. ✅ Architecture modification proposed
5. ✅ Critical error or blocker discovered
6. ✅ EPIC completed or blocked
7. ✅ Golden dataset modifications
8. ✅ Test coverage drops below target
9. ✅ Infrastructure costs exceed budget
10. ✅ Documentation inconsistency detected

### Notification Template
```markdown
🚨 **PRODUCT OWNER NOTIFICATION**
**Event**: [Pivot/Decision/Change]
**Current State**: [Before]
**New State**: [After]
**Rationale**: [Why]
**Impact**: [What changes]
**Risk Score**: [Old] → [New]
**Action Required**: [What Product Owner should do]
```

---

## 🚀 DEPLOYMENT & INFRASTRUCTURE STATUS

### Frontend - [Platform]
- **Status**: [🟢 DEPLOYED | 🟡 BUILDING | 🔴 FAILED]
- **URL**: [production URL]
- **Project ID**: [exact platform ID]
- **Last Deploy**: [timestamp]
- **Deploy Command**: `[exact command]`
- **Rollback Command**: `[exact command]`

### Backend - [Platform]
- **Status**: [🟢 DEPLOYED | 🟡 BUILDING | 🔴 FAILED]
- **URL**: [production URL]
- **Service ID**: [exact platform ID]
- **Last Deploy**: [timestamp]
- **Deploy Command**: `[exact command]`
- **Rollback Command**: `[exact command]`

### Database - [Platform]
- **Status**: [🟢 ACTIVE | 🟡 MAINTENANCE | 🔴 DOWN]
- **Connection**: [masked but indicate location]
- **Backup Schedule**: [frequency]
- **Last Backup**: [timestamp]
- **Recovery Time**: [RTO in minutes]

---

## 📅 DAILY ACTIVITY LOG

### Session Entry Template
```markdown
### 📅 YYYY-MM-DD - [SESSION_ID]
**Session Focus**: [Main objective]
**Risk Score Start**: [NUMBER]
**Risk Score End**: [NUMBER] [↑↓→]

**✅ Completed**:
- [Task]: [Impact on metrics]
- [Task]: [Files affected]

**🔄 Decisions & Pivots**:
- **Decision**: [What] → **Rationale**: [Why] → **Impact**: [Future implications]

**🐛 Issues & Resolutions**:
- **Issue**: [Problem] → **Resolution**: [Fix] → **Prevention**: [Future safeguard]

**📁 Files Modified** (with purpose):
- `path/to/file.ext`: [Why changed, what it achieved]

**📊 Metrics Impact**:
- Test Coverage: [X]% → [Y]%
- Story Points: +[N] completed
- Context Windows: [N] used

**🎯 Next Session MUST**:
1. [Critical task with reason]
2. [Important task with reason]

**⚠️ Handoff Notes**:
[Specific warnings or context for next developer]
```

### [Most Recent Sessions Below]
[Add actual session logs here]

---

## 📋 EPIC STATUS TRACKER

### Active EPICs
| EPIC | Name | Progress | Blocked | Story Points | Risk Impact |
|------|------|----------|---------|--------------|-------------|
| EPIC-00 | [Name] | [X]% | [Y/N] | [Remaining] | [Risk change if delayed] |
| EPIC-01 | [Name] | [X]% | [Y/N] | [Remaining] | [Risk change if delayed] |

### Completed EPICs
| EPIC | Name | Completion Date | Actual vs Estimated | Lessons Learned |
|------|------|----------------|-------------------|------------------|
| [EPIC-XX] | [Name] | [Date] | [X] vs [Y] points | [Key learning] |

---

## 🏗️ ARCHITECTURAL DECISIONS RECORD

### Current Architecture
```
[ASCII diagram or description of current architecture]
```

### Decision Log
| Date | Decision | Rationale | Alternatives Considered | Reversal Cost |
|------|----------|-----------|------------------------|---------------|
| [DATE] | [What was decided] | [Why] | [What else we considered] | [Low/Medium/High] |

---

## 🧪 TESTING & QUALITY GATES

### Testing Infrastructure
- **Framework**: [Testing framework]
- **Coverage Tool**: [Coverage tool]
- **CI/CD**: [CI/CD platform]
- **Test Data Strategy**: [Approach]

### Quality Gates (Enforced)
- [ ] Test coverage ≥ [X]%
- [ ] No critical security vulnerabilities
- [ ] Performance score ≥ [X]
- [ ] Type checking passes
- [ ] Linting passes
- [ ] Build succeeds
- [ ] Golden dataset validation passes

### Golden Dataset Status
- **Total Samples**: [Use value from Truth Table]
- **Categories**: [List categories]
- **Last Validation**: [Date]
- **Success Rate**: [X]%

---

## 💰 BUSINESS METRICS & COSTS

### Revenue Metrics
| Metric | Current | Target | Month-over-Month | Actions |
|--------|---------|--------|------------------|---------|
| **MRR** | $[X] | $[Y] | [+/-X]% | [What we're doing] |
| **Users** | [X] | [Y] | [+/-X]% | [What we're doing] |
| **Churn** | [X]% | <[Y]% | [+/-X]% | [What we're doing] |
| **CAC** | $[X] | <$[Y] | [+/-X]% | [What we're doing] |

### Infrastructure Costs
| Service | Monthly Cost | Optimization | Savings Potential |
|---------|--------------|--------------|-------------------|
| [Hosting] | $[X] | [What we could do] | $[Y] |
| [Database] | $[X] | [What we could do] | $[Y] |
| [Storage] | $[X] | [What we could do] | $[Y] |
| **TOTAL** | $[X] | Target: <$[Y] | $[Z] possible |

---

## 🔄 PRE-SESSION CHECKLIST

**MANDATORY** before any development session:
1. [ ] Read entire Single Source of Truth table
2. [ ] Check for recent pivots/decisions
3. [ ] Verify .claude is symlink: `ls -la .claude`
4. [ ] Review last 3 session logs
5. [ ] Check deployment status
6. [ ] Verify test coverage hasn't dropped
7. [ ] Check for Product Owner notifications
8. [ ] Review active blockers
9. [ ] Confirm using correct directories
10. [ ] Test critical user flows still work

---

## ⚠️ CRITICAL WARNINGS & NEVER FORGETS

### NEVER
1. Create duplicate .claude directories
2. Make new versions of existing documents
3. Use deprecated/archive directories
4. Change risk score without recalculating
5. Skip Product Owner on pivots
6. Deploy without checking quality gates
7. Modify Truth Table without validation

### ALWAYS
1. Update THIS document first for metrics
2. Use symlinks for .claude
3. Progress documents (v0.1→v0.2→v1.0)
4. Document pivots immediately
5. Calculate risk score with standard formula
6. Measure in story points, not days
7. Validate against golden dataset

---

## 🚀 FEATURE STATUS TRACKER

### Live Features 🟢
| Feature | Launch Date | Adoption | Performance | Revenue Impact |
|---------|------------|----------|-------------|----------------|
| [Feature 1] | [Date] | [X]% users | [Metrics] | $[X] MRR |
| [Feature 2] | [Date] | [X]% users | [Metrics] | $[X] MRR |

### Beta Features 🟡
| Feature | Beta Users | Feedback Score | GA Date | Risk Level |
|---------|------------|----------------|---------|------------|
| [Feature 1] | [X] | [X]/10 | [Date] | [Low/Med/High] |
| [Feature 2] | [X] | [X]/10 | [Date] | [Low/Med/High] |

### In Development 🔵
| Feature | Progress | Target Date | Dependencies | Story Points Remaining |
|---------|----------|-------------|--------------|----------------------|
| [Feature 1] | [X]% | [Date] | [List] | [X] points |
| [Feature 2] | [X]% | [Date] | [List] | [X] points |

---

## 🏥 SYSTEM & TEAM HEALTH

### Infrastructure Health
| Metric | Current | Target | Trend | Alert Threshold |
|--------|---------|--------|-------|----------------|
| **Uptime** | [X]% | >99.9% | [↑↓→] | <99% |
| **Response Time** | [X]ms | <500ms | [↑↓→] | >1000ms |
| **Error Rate** | [X]% | <1% | [↑↓→] | >5% |
| **Database Size** | [X] GB | <[Y] GB | [↑↓→] | >[Z] GB |

### Recent Incidents
| Date | Issue | Duration | Impact | Resolution | Prevention |
|------|-------|----------|--------|------------|------------|
| [Date] | [Issue] | [Xm] | [Users affected] | [Fix applied] | [What prevents recurrence] |

### Team Health Indicators
**Morale**: [🟢 High | 🟡 Medium | 🔴 Low]  
**Capacity**: [X]% utilized (Target: 70-85%)  
**Burnout Risk**: [🟢 Low | 🟡 Medium | 🔴 High]  
**Context Switch Frequency**: [X] per day (Target: <3)

### Recent Wins 🎉
- [Team win 1 with business impact]
- [Team win 2 with business impact]
- [Team win 3 with business impact]

### Current Challenges & Mitigations 😅
- **[Challenge 1]**: [How we're addressing it] → [Expected resolution]
- **[Challenge 2]**: [How we're addressing it] → [Expected resolution]

---

## 🔧 QUICK COMMANDS & SCRIPTS

```bash
# Verify structure compliance
./tools/scripts/verify-structure.sh

# Check symlinks
ls -la .claude | grep -E "^l"

# Calculate risk score
echo "($COMPLEXITY * $AI_UNCERTAINTY * $INTEGRATION) / ($TEST_COVERAGE / 100)" | bc

# Run golden dataset validation
npm run test:golden-dataset

# Generate metrics report
npm run metrics:report

# Check for documentation inconsistencies
./tools/scripts/doc-consistency-check.sh
```

---

## 📚 REFERENCE DOCUMENTS

### Authoritative Sources (in order)
1. **This Command Center** - Single source of truth
2. **PRD.md** - Requirements (references this)
3. **EPIC files** - Execution details
4. **claude.md** - Development instructions

### Supporting Documentation
- **Testing Playbook**: `/testing-playbook.md`
- **Deployment Playbook**: `/deployment-playbook.md`
- **Architecture Diagrams**: `/architecture/`
- **API Documentation**: `/api-docs/`

---

## 🎯 SUCCESS CRITERIA & EXIT CONDITIONS

### MVP Launch Criteria
- [ ] Risk Score < [X]
- [ ] Test Coverage > [Y]%
- [ ] Golden Dataset Pass Rate > [Z]%
- [ ] All EPICs complete
- [ ] Product Owner sign-off
- [ ] Revenue model validated

### Handoff Criteria
- [ ] Documentation complete
- [ ] Knowledge transfer session held
- [ ] All passwords/secrets transferred
- [ ] Monitoring configured
- [ ] Support playbook created

---

*This Command Center is the ABSOLUTE AUTHORITY for all [PRODUCT_NAME] metrics and decisions.*
*Last structural validation: [DATE]*
*Next required review: [DATE]*

**Remember**: In case of ANY discrepancy, this document's Truth Table is the final authority.
