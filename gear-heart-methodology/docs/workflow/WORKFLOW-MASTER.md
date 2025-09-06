# WORKFLOW-MASTER.md
**Master Workflow Documentation - Single Source of Truth**

**Version**: 1.7  
**Created**: June 24, 2025  
**Authority**: Tier 1 Global Authority File  
**Purpose**: Complete workflow processes, sub-agent orchestration, integration protocols

---

## Document Authority and Usage

**This is the single source of truth for all workflow processes.** 

### Documentation Hierarchy (CRITICAL)
**The following hierarchy MUST be respected for all metrics and decisions:**

1. **COMMAND CENTER** (`COMMAND_CENTER.md`) - ABSOLUTE AUTHORITY
   - Single Source of Truth Table (risk scores, golden datasets, all metrics)
   - Technical pivots and strategic changes log
   - Official formulas and calculations
   - Real-time project status

2. **Product Requirements** (`PRD.md`) - REQUIREMENTS AUTHORITY
   - Product vision and features (references Command Center for metrics)
   - Market analysis and user personas
   - Success criteria (uses Command Center values)

3. **EPIC Files** (`EPIC-XX-*.md`) - EXECUTION AUTHORITY
   - Implementation details (references Command Center for risk/metrics)
   - Task breakdowns in story points
   - Progress tracking (syncs with Command Center)

4. **Other Documents** - SUPPORTING MATERIALS
   - Must reference above documents for authoritative values
   - Never contain conflicting metrics
   - Link to Command Center for official numbers

**Referencing Files Should**:
- Link to specific sections in this document
- NOT duplicate workflow process information
- Focus on implementation details specific to their domain
- ALWAYS defer to Command Center for metrics

**Cross-References**:
- **Agent Catalog**: [/.claude/agents/](../../.claude/agents/)
- **Claude Code Instructions**: [/development/CLAUDE.md](/development/CLAUDE.md)
- **Development Standards**: [/development/STANDARDS.md](../../STANDARDS.md)
- **Custom Commands**: [/development/tools/CUSTOM-COMMANDS.md](/development/tools/CUSTOM-COMMANDS.md)
- **Progressive Documentation**: [PROGRESSIVE-DOCUMENTATION-GUIDE.md](./PROGRESSIVE-DOCUMENTATION-GUIDE.md)

### 📚 Workflow Component Documents
**This document provides the overview. For detailed execution:**
- **[WORKFLOW-PHASES.md](WORKFLOW-PHASES.md)** - Detailed phase execution guides
- **[WORKFLOW-GATES.md](WORKFLOW-GATES.md)** - Gate criteria and validation requirements
- **[SUBAGENT-NAVIGATION.md](SUBAGENT-NAVIGATION.md)** - Finding the right agent for any task
- **Progressive Doc Hook**: [/.claude/hooks/progressive-doc/](../../.claude/hooks/progressive-doc/)

---

## Overview

### APOLLO Enhanced Workflow
The APOLLO (Advanced Product Operations Leader for LLM-powered Optimization) workflow enables rapid product development with 14-21 day cycles focused on revenue generation. This system integrates specialized sub-agents across all phases.

### Sub-Agent Phase Mapping
| Phase | Lead Agent | Supporting Agents |
|-------|------------|-------------------|
| 1 - Product Definition | AURA | market-analysis-prd |
| 2 - Technical Feasibility | tech-stack-advisor | architecture-validator |
| 3 - Product Design | ux-journey-architect | design-system-selector, design-tool-orchestrator |
| 4 - Development | backlog-health-manager | testing-environment-architect, **puppeteer-mcp** |
| 5 - Deployment | deployment-playbook-creator | github-repo-manager, **vercel-mcp**, **puppeteer-mcp** |
| Cross-Phase | Product-specific owners | github-repo-manager, **vercel-mcp**, **puppeteer-mcp** |

### Workflow Philosophy
1. **Revenue First**: Every decision enables monetization
2. **Speed Over Perfection**: Ship fast, iterate based on data
3. **Cost Consciousness**: Profitability from day one
4. **Progressive Enhancement**: Start simple, add complexity when proven
5. **File-First Approach**: Documentation drives development

---

## Inspector (CODEX) Integration & Gates

The Inspector (referred to operationally as CODEX) is the quality authority for testing, security, performance, and documentation truth. CODEX enforces non-negotiable gates that must pass before integration and deployment.

### RACI for Quality Gates
- Responsible: Developer (Claude) – implements code and tests
- Accountable: Inspector (CODEX) – approves or blocks at gates
- Consulted: Strategist (Gemini) – architecture and feasibility validation
- Informed: Product Owner – receives pass/fail status and metrics

### Gate 1 – End of Phase 3 (Development)
Blocking Criteria:
- Test coverage: ≥80% project-level; ≥90% on changed lines
- Unit/component tests for new/changed logic; critical paths covered
- Security: no high/critical vulnerabilities; no secrets; client env limited to `NEXT_PUBLIC_*`
- Documentation: `tests/TEST_MANIFEST.md` lists real file paths; `tests/TESTING-PLAYBOOK.md` phase items updated

Required Evidence:
- Green CI run (type-check, lint, unit/component)
- Coverage report artifact and diff coverage annotation

### Gate 2 – End of Phase 4 (Testing)
Blocking Criteria:
- Cross-browser E2E: Chromium, Firefox, WebKit pass; mobile profiles pass
- Accessibility: no serious axe violations; keyboard navigation validated
- Performance (Lighthouse): performance score ≥0.90; LCP <2.5s; FCP <1.5s; CLS <0.02
- Animations: timings within ±50ms of MOTION tokens; reduced-motion respected
- Progressive enhancement: no‑JS baseline content available for key flows

Required Evidence:
- Green CI run including Playwright, axe, and LHCI
- Updated `COMMAND_CENTER.md` “Inspector Gate Scoreboard” with metrics + latest CI link

### Documentation Sources of Truth (Quality)
- Global control: `/development/CODEX.md` – reading order, per-product overrides, thresholds, CI, triggers
- Product truth: `COMMAND_CENTER.md` (Inspector Gate Scoreboard), `tests/TEST_MANIFEST.md`, `tests/TESTING-PLAYBOOK.md`

> The golden rule applies: “No code without validation, no feature without gates, no session without context.”


### File Naming Conventions
- **Products**: `/products/{product-name}/` (lowercase, hyphenated)
- **EPICs**: `EPIC-{NUMBER}-{descriptive-name}.md`
- **PRDs**: `{product-name}-PRD.md`

### Progressive Documentation Standards
- **Single File Updates**: All updates happen in the SAME file (never create new versions)
- **Version Progression**: PRD v0.1 → v0.2 → v0.5 within same document
- **Collaborative Evolution**: AURA writes strategic context, APOLLO adds technical approach, Claude Code implements and logs progress
- **Archive Policy**: Never delete files - move to `archive/` directory when obsolete

---

## Complete Workflow Process

### Phase 1: Product Definition (File-First Research)
**Timeline**: 3-5 context windows over 5-7 days  
**Owner**: AURA Strategic Lead + User  
**Location**: `~/development/products/{product-name}/`

#### Step 1.1: Market Spark (User + AURA)
**Deliverable**: `{product-name}-PRD.md v0.1`

**Process**:
1. User provides initial product concept
2. AURA creates initial PRD with meta table structure
3. Establish research objectives and market hypotheses

**PRD Meta Table Structure (Required)**:
```markdown
## PRD Meta Information
| Field | Value |
|-------|-------|
| **Current Version** | v0.1 |
| **Last Updated** | [Date and Time] |
| **Last Editor** | AURA |
| **Status** | Research Phase |
| **Next Milestone** | Market Research → v0.2 |
| **Total Edits** | 1 |

## Version Change Log
| Version | Date | Editor | Changes Made |
|---------|------|--------|--------------|
| v0.1 | [Date] | User + AURA | Initial market spark and problem definition |
```

#### Step 1.1.1: Initialize Agent Directives (APOLLO)
**Deliverable**:
*   `products/{product-name}/COMMAND_CENTER.md` (CRITICAL - Single Source of Truth)
*   `products/{product-name}/claude.md`
*   `products/{product-name}/gemini.md`
*   `.claude/agents/{product-name}-product-owner.md`

**Process**:
1.  **Create COMMAND CENTER**: Copy `tools/templates/PRODUCT_COMMAND_CENTER_template.md` to create the single source of truth. This is THE authoritative document for all metrics, risk scores, and strategic decisions. Initialize the Truth Table with starting values.
2.  **Create `claude.md`**: Copy the `tools/templates/product-claude-template.md` to the product's root directory. This file will contain product-specific instructions for Claude, including mandatory Product Owner triggers and Command Center references.
3.  **Create `gemini.md`**: Create a `gemini.md` file in the product's root directory. This file will contain product-specific strategic guidance for Gemini, referencing the Command Center for all metrics.
4.  **Create Product Owner Agent**: Use the `tools/templates/product-owner-agent-template.md` to create a dedicated product owner agent that will protect the Command Center's integrity and maintain institutional memory. This agent MUST activate on product name mentions.
5.  **Setup .claude directory**: Create symlink to global .claude directory to prevent duplication: `ln -s /development/.claude .claude`

#### Step 1.1.2: Setup .claude Directory Structure
**Purpose**: Enable quality hooks and Claude tooling in product subdirectories
**Deliverable**: `.claude` symlinks in all working directories

**Process**:
```bash
# From product root directory
cd ~/development/products/{product-name}/

# Create symlink to global .claude directory
ln -sf ../../../.claude .claude

# For nested directories (backend, frontend, mobile)
cd active-projects/mvp/{project-name}-backend/
ln -sf ../../../../../.claude .claude

cd ../frontend/
ln -sf ../../../../../.claude .claude

cd ../mobile/
ln -sf ../../../../../.claude .claude
```

**Verification**:
```bash
# Test that quality hooks are accessible
ls -la .claude/hooks/react-app/quality-check.js
# Should show: quality-check.js exists via symlink
```

**Why This Matters**:
- Quality hooks fail when Claude Code can't find `.claude/hooks/` in working directory
- Symlinks maintain single source of truth while enabling local access
- Prevents "Cannot find module" errors during file operations

#### Step 1.2: Market Definition Research
**Process**:
1. AURA generates Perplexity research prompt
2. User executes research in Perplexity  
3. User saves results to `research/perplexity-analysis.md`
4. AURA generates Gemini validation prompt
5. User executes validation in Gemini
6. User saves results to `research/gemini-validation.md`
7. AURA processes results → PRD v0.2

**Research File Structure**:
```
research/
├── perplexity-analysis.md     # User pastes Perplexity outputs
├── gemini-validation.md       # User pastes Gemini outputs
├── competitive-landscape.md   # Competitive analysis
├── user-validation.md         # User research
└── red-team-analysis.md       # Final kill criteria
```

#### Step 1.3: Competitive Landscape Analysis
**Process**: Multi-AI competitive intelligence
**Deliverable**: `research/competitive-landscape.md` + PRD v0.3

#### Step 1.4: User Needs Research  
**Process**: User validation through multi-AI synthesis
**Deliverable**: `research/user-validation.md` + PRD v0.4

#### Step 1.5: Red Team Analysis
**Process**: Systematic kill criteria evaluation
**Deliverable**: `research/red-team-analysis.md` + PRD v0.5

**Gate 1 Decision**: Proceed to technical feasibility or kill

### EPIC-00: Pre-Development Foundation Setup
**Timeline**: 1 context window over 1-2 days  
**Owner**: Claude Code + User  
**Location**: `~/development/products/{product-name}/`  
**Trigger**: PRD v0.5+ approved and Gate 1 passed

#### Purpose
Establish development environment foundation, security protocols, and quality frameworks before technical implementation begins. This EPIC creates the essential infrastructure that enables rapid, secure development.

#### Step EPIC-00.1: Environment Foundation Setup
**Process**: Interactive setup of development environment and service accounts
**Deliverable**: Complete development environment ready for coding

**Core Tasks**:
- **Environment Configuration**: `.env.example` and `.env` with all required services
- **Security Foundation**: Comprehensive `.gitignore` and secrets management
- **Production Secrets**: Complete deployment secrets strategy guide
- **Quality Framework**: Golden datasets structure (for AI products)
- **Developer Experience**: Setup guide and troubleshooting documentation

**Service Account Provisioning** (Interactive):
- Supabase Pro account setup and configuration
- AI services (OpenAI, Google Document AI, Perplexity) API keys
- Infrastructure services (Redis, Sentry) account creation
- Development tools (Expo, GitHub) access verification

#### Step EPIC-00.2: Repository Foundation
**Process**: Initialize secure, production-ready repository structure
**Deliverable**: Git repository with proper security and development standards

**Repository Tasks**:
- Initial commit with environment templates and documentation
- Branch protection and CI/CD pipeline setup
- Secret scanning and security policies
- Development workflow automation

#### Step EPIC-00.3: Quality Assurance Framework
**Process**: Establish testing and validation infrastructure
**Deliverable**: Testing framework ready for development validation

**Quality Tasks** (Product-Type Specific):
- **AI Products**: Golden datasets structure (OCR, RAG, Scripts as needed)
- **Mobile Products**: iOS Simulator validation, device testing setup
- **Web Products**: Browser testing, accessibility validation setup
- **All Products**: Performance benchmarking, error monitoring setup

**Gate EPIC-00**: Development foundation complete and validated
- [ ] All service accounts provisioned and tested
- [ ] Environment variables configured and validated  
- [ ] Repository security and workflow established
- [ ] Quality framework appropriate for product type
- [ ] Initial commit created with foundation files
- [ ] Phase 1.1 agent setup ready to proceed

### Phase 2: Technical Feasibility (APOLLO Analysis)
**Timeline**: 1-2 context windows over 2-3 days  
**Owner**: APOLLO Technical Lead  
**Location**: Continues in `~/development/products/{product-name}/`

#### Step 2.1: Tech Stack Analysis
**Process**: APOLLO evaluates technical requirements using [TECH-STACK-BLUEPRINT.md](../tech-stack/TECH-STACK-BLUEPRINT.md)
**Deliverable**: PRD v0.6 with technical assessment

**Supabase Cost Analysis**:
- Use `mcp__supabase__get_cost` to estimate project costs
- Validate against <$0.10/user target
- Consider free tier for MVP validation

**Technical Feasibility Framework**:
```markdown
## Technical Feasibility Matrix - APOLLO Standard

### Complexity Assessment (1-10)
**Frontend Complexity**: [Score] - [Rationale + Cost Impact]
**Backend Complexity**: [Score] - [Rationale + Timeline Impact]  
**Integration Complexity**: [Score] - [Third-party Dependencies]
**Infrastructure Complexity**: [Score] - [Scaling Considerations]

### Cost Analysis (Critical for Revenue)
**Infrastructure Cost/User**: $[Amount] - Must be <$0.10
**Development Tool Costs**: $[Monthly] - Budget impact
**Third-party Service Costs**: $[Per transaction/user]
**Break-even Analysis**: [Users needed for profitability]
```

#### Step 2.2: Feasibility Scoring
**Process**: Cost, complexity, timeline analysis with Supabase-first approach
**Deliverable**: PRD v0.7 with go/no-go recommendation

**Supabase Feasibility Checklist**:
- [ ] Database design fits PostgreSQL + RLS model
- [ ] Authentication requirements match Supabase Auth capabilities
- [ ] File storage needs align with Supabase Storage (5GB free tier)
- [ ] Real-time features can use Supabase Realtime
- [ ] Cost projection within Supabase free tier for MVP
- [ ] pgvector suitable for any AI/search requirements

**Gate 2 Decision**: Technical feasibility confirmed with Supabase architecture

### Phase 3: Product Design (Design-First Approach)
**Timeline**: 2-3 context windows over 3-5 days  
**Owner**: AURA (Design Strategy) + Product Designer Agent + User  
**Location**: `~/development/products/{product-name}/design/`

#### Step 3.1: Design System Selection
**Process**: Product Designer Agent evaluates design systems using selection framework
**Critical Decision**: Select primary design system (shadcn/ui, Material-UI, NewsKit, etc.)
**Framework**: Use [design-system-selection-guide.md](../templates/design-system-selection-guide.md)
**Deliverable**: `design/design-system-decision.md` with evaluation matrix and rationale
**Gate 3A**: Design system selected and documented before proceeding

#### Step 3.2: UX Journey Mapping
**Process**: AURA creates comprehensive user journey maps
**Deliverable**: `design/wireframes/user-journey-map.md` + PRD v0.8

#### Step 3.3: Information Architecture
**Process**: AURA defines site structure and navigation
**Deliverable**: `design/wireframes/information-architecture.md` + PRD v0.9

#### Step 3.4: Design Brief Creation
**Process**: AURA synthesizes design requirements
**Deliverable**: `{product-name}-DesignBrief.md` + PRD v1.0

#### Step 3.5: UXPilot Design Generation (Primary Tool)
**Process**: Product Designer Agent creates UXPilot-optimized prompts using wireframe-first approach
**Deliverable**: `design/tool-prompts/uxpilot-prompt.md` with complete specifications

**UXPilot Configuration**:
- **Mode**: Wireframes (recommended for best results)
- **Export**: Individual HTML files for component extraction
- **Asset Strategy**: Placeholder-driven creation after wireframe approval
- **Design System**: Tailwind-based with APOLLO cost optimization

**Tool Prompt Structure**:
```
design/tool-prompts/
├── uxpilot-prompt.md      # PRIMARY: Wireframe-first component generation
├── uxpilot-asset-specs.md # Asset specifications extracted from wireframes
  
└── figma-instructions.md  # Optional: Design system setup and handoff
```



#### Step 3.6: UXPilot Implementation & Asset Planning
**Process**: User executes UXPilot wireframe generation followed by asset specification extraction
**Deliverable**: `design/exports/uxpilot-output/` with HTML wireframes and asset specifications

**UXPilot Workflow**:
1. **Wireframe Generation**: Create all pages in single UXPilot session
2. **Asset Extraction**: Document placeholder specifications for future creation
3. **Navigation Mapping**: Define component relationships and routing
4. **Design Token Verification**: Ensure Tailwind classes align with APOLLO standards

**Design Export Structure**:
```
design/exports/
├── uxpilot-output/           # PRIMARY: Wireframes and specifications
│   ├── html-wireframes/      # Individual page exports
│   ├── navigation-map.md     # Component relationships
│   ├── asset-specifications/ # Placeholder documentation
│   └── conversion-guide.md   # Instructions for Claude Code
└── figma-exports/            # Optional: Design assets and specifications
```

**Gate 3 Decision**: Design-technical alignment confirmed

### Phase 4: Product Development (Enhanced File-Based)
**Timeline**: 5-8 context windows over 10-14 days  
**Owner**: APOLLO + Claude Code  
**Location**: `~/development/products/{product-name}/epics/`

#### Step 4.1: Epic Planning & Breakdown
**Process**: APOLLO creates detailed epic files
**Deliverable**: All 5 epic .md files with plans

**EPIC Distribution Target**:
- Environment: 10% effort (Setup & tooling)
- Features: 50% effort (Core functionality)  
- Integrations: 20% effort (External services)
- Testing: 10% effort (Quality assurance)
- Deployment: 10% effort (Launch preparation)

#### Step 4.2: UXPilot-to-React Conversion
**Process**: Claude Code converts UXPilot HTML wireframes to React components using conversion guide
**Deliverable**: `active-projects/mvp/src/` with React components maintaining Tailwind classes

**Conversion Priorities**:
1. **Preserve UXPilot Structure**: Maintain exact Tailwind classes and component hierarchy
2. **Extract Reusable Components**: Follow component identification from navigation map
3. **Implement Routing**: Use navigation map to create React Router structure
4. **Maintain Placeholders**: Keep asset placeholders for future integration
5. **Progressive Enhancement**: Build foundation for asset integration and state management

#### Step 4.3: Supabase Project Setup
**Process**: Initialize Supabase project and configure database
**Deliverable**: Configured Supabase project with schema

**Supabase Setup Checklist**:
1. Create project: `mcp__supabase__create_project`
2. Design database schema with RLS policies
3. Apply migrations: `mcp__supabase__apply_migration`
4. Generate TypeScript types: `mcp__supabase__generate_typescript_types`
5. Configure authentication providers
6. Set up storage buckets with policies

#### Step 4.4: Development Execution
**Process**: Claude Code follows epic plans with Supabase integration
**Deliverable**: Working MVP with full backend integration

**Development with Supabase MCP**:
- Monitor logs: `mcp__supabase__get_logs`
- Check security: `mcp__supabase__get_advisors --type security`
- Deploy Edge Functions: `mcp__supabase__deploy_edge_function`
- Use branching for features: `mcp__supabase__create_branch`

#### Enhanced Mobile Development Integration

**Xcode and iOS Development Requirements**:
- **macOS + Xcode Required**: iOS development mandates macOS with latest Xcode installed
- **iOS Simulator Setup**: Configure simulators for iPhone 14, 15 Pro target devices
- **Apple Developer Account**: Required for device testing and App Store distribution
- **Development Environment Validation**: Run `xcode-select --install` and `xcrun simctl list devices`

**Browser Automation for Mobile Testing**:
- **Puppeteer Mobile Emulation**: Automated mobile web testing using device emulation
- **Cross-Platform Consistency**: Validate React Native and mobile web feature parity
- **Mobile Performance Testing**: Core Web Vitals measurement on mobile viewports
- **Responsive Design Validation**: Automated testing across device breakpoints

**Mobile-First Development Workflow**:
```bash
# Required package.json scripts for mobile products
"ios": "expo start --ios",
"ios:simulator": "expo start --ios", 
"ios:device": "expo start --ios --device",
"dev:mobile": "concurrently \"npm run dev\" \"npm run ios\"",
"mobile:setup": "expo install && expo prebuild",
"mobile:doctor": "expo doctor",
"test:mobile": "jest --config=jest.mobile.config.js",
"test:mobile:e2e": "npm run test:e2e -- --config=mobile.puppeteer.config.js",
"test:responsive": "npm run test:e2e -- --config=responsive.puppeteer.config.js"
```

**Daily Mobile Validation Process**:
1. **Start Development**: Launch with `npm run dev:mobile` for automatic iOS Simulator
2. **Feature Testing**: Every feature must pass both iOS Simulator and browser mobile emulation
3. **Cross-Platform Validation**: Automated responsive testing ensures web-mobile feature parity
4. **Real Device Testing**: Physical iPhone testing recommended for production features
5. **E2E Mobile Testing**: Automated user journey testing on mobile viewports

**Monorepo and Mobile Development Considerations**:
- **Monorepo Structure**: When working in a monorepo, ensure changes are isolated to the relevant `apps/` or `packages/` directories. Shared components should be developed and tested in their respective `packages/` directories.
- **Expo Development**: For mobile applications, utilize Expo CLI commands for development (`expo start`), building (`eas build`), and publishing (`eas update`). Ensure `app.json` or `app.config.js` is correctly configured for each mobile app within the monorepo.
- **CI/CD for Monorepos**: GitHub Actions workflows (e.g., `build-mobile.yml.template`, `deploy-production.yml.template`) should be configured to trigger based on changes within specific monorepo paths, ensuring efficient and targeted deployments.

**Gate 4 Decision**: Launch readiness confirmed

### Phase 5: Product Deployment & Validation (Enhanced Browser Automation)
**Timeline**: 1-2 context windows over 2-3 days  
**Owner**: deployment-playbook-creator + Specialized Subagents  
**Location**: `~/development/products/{product-name}/deployment/`

#### Step 5.1: Deployment Pipeline with E2E Validation
**Process**: Automated deployment with comprehensive browser-based verification
**Deliverable**: Production deployment with validated user journeys

**Puppeteer-Enhanced Deployment Workflow**:
1. **Pre-Deployment E2E Testing**: Run complete test suite including visual regression
2. **Automated Deployment**: Deploy to production with staging environment validation
3. **Post-Deployment Smoke Testing**: Automated critical path verification using browser automation
4. **Performance Validation**: Real browser performance testing on production environment
5. **Cross-Browser Production Testing**: Verify functionality across browsers in production
6. **Mobile Experience Validation**: Test responsive design and mobile workflows in production

#### Step 5.2: Production Monitoring & Continuous Validation
**Process**: Ongoing automated testing and performance monitoring
**Deliverable**: Continuous production health verification

**Browser Automation for Production Monitoring**:
- **Synthetic User Testing**: Automated user journeys running continuously
- **Performance Monitoring**: Regular Core Web Vitals measurement through real browser testing
- **Uptime Verification**: Automated critical functionality validation
- **Regression Detection**: Visual and functional regression monitoring

### Phase 6: Product Enhancements (Subagent Integration)
**Timeline**: Ongoing post-launch  
**Owner**: Specialized Subagents  
**Location**: `~/development/products/{product-name}/enhancements/`

---

## Progressive PRD Versioning System

### Version Increment Triggers
- **v0.1**: Initial market spark (User + AURA)
- **v0.2**: Market research integration (AURA)
- **v0.3**: Competitive analysis integration (AURA)
- **v0.4**: User research validation (AURA)
- **v0.5**: Red team analysis and Gate 1 decision (AURA)
- **v0.6**: Technical stack analysis (APOLLO)
- **v0.7**: Technical feasibility assessment (APOLLO)
- **v0.8**: UX journey mapping (AURA)
- **v0.9**: Information architecture (AURA)
- **v1.0**: Final approved PRD ready for development (All agents + User)

### Agent Editing Protocol
1. **Always update meta table first** when beginning edits
2. **Add change log entry** describing what will be modified
3. **Make content changes** in designated sections
4. **Update "Last Updated" timestamp** when completed
5. **Increment version number** according to milestone completion

---

## Sub-Agent Coordination Protocols

### Handoff Standards
Each sub-agent must complete tasks with:

```markdown
## Task Completion: {Agent Name}
**Date**: {Completion date}
**Task**: {What was accomplished}
**Output Location**: {File paths to deliverables}
**Next Agent**: {Who should take over}
**Handoff Notes**: {Important context for next agent}
**Workflow Status**: {Overall process health}
```

### Quality Gates and Success Criteria

#### Gate 1: Research Complete (PRD v0.5)
**Criteria**:
- [ ] Market opportunity score >70%
- [ ] Clear competitive wedge identified
- [ ] User need validation evidence collected
- [ ] Feasible revenue model outlined ($1K-$10K monthly potential)
- [ ] Red team analysis shows GO recommendation

#### Gate 2: Technical Feasibility (PRD v0.7)
**Criteria**:
- [ ] Technical complexity assessed as manageable
- [ ] Architecture design completed and validated
- [ ] Development timeline confirmed as <14 days
- [ ] Infrastructure costs <$0.10/user validated
- [ ] APOLLO provides GO recommendation

#### Gate 3: Design Complete (Design Brief + Code Ready)
**Criteria**:
- [ ] Design brief approved by all stakeholders
- [ ] User journey maps validated and complete
- [ ] Design system selected and implemented
- [ ] Design tool exports integrated and optimized
- [ ] Code quality meets development standards

#### Gate 3.5: Testing Infrastructure Verified (NEW)
**Criteria**:
- [ ] Testing frameworks installed for all layers (unit, integration, e2e)
- [ ] Jest/testing configuration files properly set up
- [ ] **Puppeteer E2E testing framework configured and operational**
- [ ] Sample tests passing in each layer including browser automation
- [ ] Test database and mocks configured
- [ ] **Browser automation test environment verified (headless + windowed)**
- [ ] Coverage reporting functional (starts at 0%)
- [ ] CI/CD pipeline includes test execution with E2E testing
- [ ] Test data strategy documented including E2E test scenarios
- [ ] **Mobile device emulation configured for responsive testing**
- [ ] `/test-verify` command shows all green including E2E infrastructure

#### Gate 4: Launch Ready (MVP Complete)
**Criteria**:
- [ ] All MVP features implemented and tested
- [ ] **Complete E2E test suite passing for all critical user journeys**
- [ ] All TypeScript Quality Hook checks passing
- [ ] Performance targets met (<2s page load, <500ms API)
- [ ] **Cross-browser compatibility verified via automated testing**
- [ ] **Mobile responsive design validated through device emulation**
- [ ] **Visual regression testing baseline established**
- [ ] Security standards implemented
- [ ] Deployment pipeline functional with E2E smoke testing
- [ ] User acceptance testing passed including browser automation verification

### Standardized Audits and Testing
To ensure consistent quality and thorough evaluation across all products, use our universal testing template for all testing needs:

- **Master Testing Template**: [testing-template.md](../../tools/templates/testing-template.md)
  - Combines all testing types: Unit, Integration, E2E, Performance, and API testing
  - Interactive progress tracking and visual status indicators
  - Progressive test run logging with historical data
  - Issue tracking and flaky test monitoring
  - Built-in coverage analysis and trend reporting

- **Epic Template for Test Planning**: [EPIC-template.md](../../tools/templates/EPIC-template.md)
  - Use with `epic_type: testing` for dedicated test epics
  - Integrates testing strategy directly into development workflow
  - Model-specific task allocation for test creation
  - Automated test coverage tracking

Testing results should be stored in `/products/{product-name}/epics/` using the progressive documentation approach.

---

## Claude's Strategic Review of Workflow & Standards

### Executive Summary

The recent workflow and technical standards improvements represent a significant step forward in establishing predictable, secure, and efficient development practices. The documentation is comprehensive and well-structured, though opportunities exist for further streamlining and gap closure.

### Key Strengths Identified

1. **Clear Phase-Based Workflow**: The 5-phase APOLLO workflow provides excellent structure with defined gates, timelines, and ownership
2. **Progressive Documentation Philosophy**: The PRD versioning system (v0.1 → v1.0) effectively tracks product evolution
3. **Tiered Standards Approach**: The 4-tier secrets management and 3-layer Git workflow demonstrate mature security thinking
4. **Pilot Implementation**: The Example Product project successfully demonstrates the standards in practice

### Strategic Recommendations

#### 1. Documentation Consolidation (Priority: High)
- **CLAUDE.md Reduction**: Extract workflow details and mobile development section to reduce from 484 to ~200 lines
- **Create Focused Documents**:
  - `MOBILE-DEVELOPMENT.md` in tech-stack/
  - `CONTEXT-MANAGEMENT.md` for AI agents
  - `ERROR-RECOVERY.md` for systematic failure handling

#### 2. Critical Missing Standards (Priority: High)
- **MONITORING-ALERTING.md**: Production monitoring, SLAs, and alert thresholds
- **DEPLOYMENT-ROLLBACK.md**: Safe deployment procedures and automated rollback triggers
- **PERFORMANCE-STANDARDS.md**: Specific metrics, testing tools, and optimization strategies
- **DISASTER-RECOVERY.md**: Data backup, service restoration, and incident response

#### 3. Streamlining Opportunities (Priority: Medium)
- **Visual Workflow Diagram**: Create a single-page visual for the 5-phase workflow
- **Quick Reference Cards**: Command cheatsheets for common operations
- **Interactive Gate Checklists**: Automated tools to verify gate criteria
- **Template Consolidation**: Merge similar templates to reduce cognitive load

#### 4. Enhancement Suggestions (Priority: Medium)
- **MCP-CONFIGURATION.md**: Expand from 11 lines to include health monitoring and fallback strategies
- **DOCKER-WORKFLOW.md**: Add troubleshooting guide and resource limit standards
- **Branch Protection Rules**: Explicitly define in GIT-WORKFLOW.md
- **Context Window Strategy**: Add specific guidance for long-running development sessions

#### 5. Consistency Improvements (Priority: Low)
- **Document Length Standards**: Target 50-150 lines per technical standard
- **Section Templates**: Standardize with "When to use", "When not to use", "Troubleshooting"
- **Code Examples**: Add practical examples to each standard
- **Cross-Reference Matrix**: Show which standards apply at each workflow phase

### Implementation Priorities

1. **Immediate (Week 1)**:
   - Extract mobile development from CLAUDE.md
   - Create MONITORING-ALERTING.md
   - Add branch protection rules to GIT-WORKFLOW.md

2. **Short-term (Week 2-3)**:
   - Create visual workflow diagram
   - Expand MCP-CONFIGURATION.md
   - Add DEPLOYMENT-ROLLBACK.md

3. **Medium-term (Month 1)**:
   - Consolidate templates
   - Create interactive checklists
   - Add troubleshooting sections

### Risk Mitigation

The current documentation gap around error handling and recovery procedures poses the highest risk. I recommend prioritizing the creation of ERROR-RECOVERY.md and DISASTER-RECOVERY.md to ensure robust failure handling across all products.

### Conclusion

The workflow and standards improvements establish a strong foundation for consistent, high-quality development. With the recommended consolidations and additions, the framework will provide comprehensive guidance while remaining accessible and actionable for both human developers and AI agents.

---

## Technical Standards and Best Practices

For detailed information on our technical standards, including file architecture, local development setup, Git workflow, secrets management, and MCP server configuration, please refer to our dedicated standards library:

**[APOLLO Technical Standards Library (tools/tech-stack/README.md)](../tech-stack/README.md)**

This library is the single source of truth for how we implement and manage our technical environment. It includes:

*   **File & Directory Structure**
*   **Git & GitHub Workflow**
*   **Secrets Management Strategy**
*   **MCP Server Configuration**
*   **Docker Workflow for Local Development**
*   **Supabase Best Practices**

### Discipline Enforcement & Repository Management

**Purpose**: Prevent structural chaos that leads to development failures and context confusion.

#### Core Structural Rules (CRITICAL)
**The "One Location Rule"**:
- **One Backend**: Only `/active-projects/mvp/backend/` (never backend-api, Example Product-backend, etc.)
- **One Frontend**: Only `/active-projects/mvp/frontend/` (never frontend-app, client, etc.)
- **One Mobile**: Only `/active-projects/mvp/mobile/` (never mobile-app, Example Product-mobile, etc.)
- **One PRD**: Only `PRD.md` at product root (never PRD-v2.md, requirements.md, etc.)

#### Required Directory Structure
```
products/{product-name}/
├── PRD.md                    ← THE source of truth
├── claude.md                 ← Product-specific instructions
├── research/                 ← Market research
├── design/                   ← Design decisions
├── epics/                    ← EPIC-01 through EPIC-05
├── active-projects/
│   └── mvp/                  ← ONLY active code here
│       ├── backend/          ← ONE backend
│       ├── frontend/         ← ONE frontend
│       └── mobile/           ← ONE mobile (optional)
├── docs/                     ← Supplementary docs
└── archive/                  ← Old stuff goes here
```

#### Forbidden Patterns (Auto-blocked by CI/CD)
- **Nested Structures**: No `active-projects/*/active-projects/`
- **Duplicate Implementations**: Multiple backend/frontend/mobile directories
- **PRD Fragmentation**: Multiple PRD-like files (requirements.md, product-vision.md, etc.)
- **Version Confusion**: No Example Product-mvp-fresh, backend-v2, etc.

#### Structure Validation (Automated)
**Pre-commit Hook** (`.claude/hooks/structure-guard.js`):
- Validates single implementation rule
- Ensures PRD.md exists at root
- Prevents nested active-projects
- Checks required directory structure
- Blocks PRD fragmentation

**GitHub Actions** (Continuous Validation):
- Runs structure validation on all PRs
- Prevents deployment of violating structures
- Generates violation reports with remediation steps

#### Session Protocols
**Every Development Session Must**:
1. **Start**: Run structure validation check
2. **During**: Maintain single implementation rule
3. **End**: Verify no new violations introduced
4. **Commit**: Pass automated structure validation

**Implementation**: [GitHub Playbook Template](../templates/github-playbook-template.md)**

---

## Key Resources and Templates

### Core Templates
- **[EPIC-template.md](../templates/EPIC-template.md)** - Universal epic template for all development work
- **[testing-template.md](../templates/testing-template.md)** - Comprehensive testing documentation
- **[product-PRD-template.md](../templates/product-PRD-template.md)** - Product requirements template
- **[product-owner-agent-template.md](../templates/product-owner-agent-template.md)** - Reusable template for creating product-specific owner agents with structured running logs

### Related Standards
- **[MONITORING-ALERTING.md](../tech-stack/MONITORING-ALERTING.md)** - Production monitoring setup
- **[DEPLOYMENT-ROLLBACK.md](../tech-stack/DEPLOYMENT-ROLLBACK.md)** - Safe deployment practices
- **[MOBILE-DEVELOPMENT.md](../tech-stack/MOBILE-DEVELOPMENT.md)** - Mobile app standards

### Workflow Integration
- Templates support progressive documentation
- Cross-references maintain document relationships
- Visual progress tracking built into templates

---

## Context Window Planning Standards

---

*This document serves as the master reference for all workflow processes. All other workflow-related files should reference this document rather than duplicating its content.*
