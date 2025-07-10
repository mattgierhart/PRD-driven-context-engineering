# WORKFLOW-MASTER.md
**Master Workflow Documentation - Single Source of Truth**

**Version**: 1.7  
**Created**: June 24, 2025  
**Authority**: Tier 1 Global Authority File  
**Purpose**: Complete workflow processes, sub-agent orchestration, integration protocols

---

## Document Authority and Usage

**This is the single source of truth for all workflow processes.** 

**Referencing Files Should**:
- Link to specific sections in this document
- NOT duplicate workflow process information
- Focus on implementation details specific to their domain

**Cross-References**:
- **Sub-agent Details**: [SUBAGENT-REGISTRY.md](./SUBAGENT-REGISTRY.md)
- **Claude Code Instructions**: [/development/CLAUDE.md](/development/CLAUDE.md)
- **Development Standards**: [/development/STANDARDS.md](/development/STANDARDS.md)
- **Custom Commands**: [/development/tools/CUSTOM-COMMANDS.md](/development/tools/CUSTOM-COMMANDS.md)
- **Model Usage Guide**: [MODEL-USAGE-GUIDE.md](./MODEL-USAGE-GUIDE.md)
- **Progressive Documentation**: [PROGRESSIVE-DOCUMENTATION-GUIDE.md](./PROGRESSIVE-DOCUMENTATION-GUIDE.md)

---

## Overview

### APOLLO Enhanced Workflow
The APOLLO (Advanced Product Operations Leader for LLM-powered Optimization) workflow enables rapid product development with 14-21 day cycles focused on revenue generation. This system integrates three specialized sub-agents:

- **AURA Strategic Lead**: Market research and product definition
- **APOLLO Technical Lead**: Technical feasibility and development coordination  
- **Product Designer Agent**: Design workflow and UX strategy

### Workflow Philosophy
1. **Revenue First**: Every decision enables monetization
2. **Speed Over Perfection**: Ship fast, iterate based on data
3. **Cost Consciousness**: Profitability from day one
4. **Progressive Enhancement**: Start simple, add complexity when proven
5. **File-First Approach**: Documentation drives development

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

#### Step 3.1: UX Journey Mapping
**Process**: AURA creates comprehensive user journey maps
**Deliverable**: `design/wireframes/user-journey-map.md` + PRD v0.8

#### Step 3.2: Information Architecture
**Process**: AURA defines site structure and navigation
**Deliverable**: `design/wireframes/information-architecture.md` + PRD v0.9

#### Step 3.3: Design Brief Creation
**Process**: AURA synthesizes design requirements
**Deliverable**: `{product-name}-DesignBrief.md` + PRD v1.0

#### Step 3.4: UXPilot Design Generation (Primary Tool)
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
├── lovable-prompt.md      # Alternative: Full app with CLEAR framework  
└── figma-instructions.md  # Optional: Design system setup and handoff
```

#### Step 3.5: Design System Selection & Integration
**Process**: Product Designer Agent evaluates and recommends design systems
**Deliverable**: `design/design-system/` documentation

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
├── lovable-output/           # Alternative: Full application code
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

**Gate 4 Decision**: Launch readiness confirmed

### Phase 5: Product Enhancements (Subagent Integration)
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
- [ ] Sample tests passing in each layer
- [ ] Test database and mocks configured
- [ ] Coverage reporting functional (starts at 0%)
- [ ] CI/CD pipeline includes test execution
- [ ] Test data strategy documented
- [ ] `/test-verify` command shows all green

#### Gate 4: Launch Ready (MVP Complete)
**Criteria**:
- [ ] All MVP features implemented and tested
- [ ] Performance targets met (<2s page load, <500ms API)
- [ ] Security standards implemented
- [ ] Deployment pipeline functional
- [ ] User acceptance testing passed

### Standardized Audits and Testing
To ensure consistent quality and thorough evaluation across all products, the following standardized audits and tests are to be performed at relevant stages of the development lifecycle. The results of these audits will be stored in the `/products/{product-name}/epics/audits_and_testing/` directory, with each audit or test having its own progressive markdown file.

- **AI-Powered Unit & Integration Testing**: Combines foundational testing layers to ensure individual components work correctly on their own and with each other.
  - **Template**: [ai-powered-unit-and-integration-testing-template.md](../../tools/templates/ai-powered-unit-and-integration-testing-template.md)

- **AI-Driven End-to-End User Journey Testing**: Simulates real user behavior to validate complete application workflows from start to finish.
  - **Template**: [ai-driven-end-to-end-user-journey-testing-template.md](../../tools/templates/ai-driven-end-to-end-user-journey-testing-template.md)

- **Comprehensive API Testing (Functional, Performance, & Security)**: A consolidated test that ensures the application's APIs are functional, fast, and secure.
  - **Template**: [comprehensive-api-testing-template.md](../../tools/templates/comprehensive-api-testing-template.md)

- **Comprehensive Code Health Audit (Static Analysis, Quality, & Security)**: Provides a holistic assessment of the codebase's quality, maintainability, and security without executing the code.
  - **Template**: [comprehensive-code-health-audit-template.md](../../tools/templates/comprehensive-code-health-audit-template.md)

- **UI/UX & Accessibility Audit**: Focuses on the user-facing aspects of the application, ensuring a consistent visual experience and compliance with accessibility standards.
  - **Template**: [ui-ux-and-accessibility-audit-template.md](../../tools/templates/ui-ux-and-accessibility-audit-template.md)

---

## File Architecture Standards

### Enhanced Directory Structure
```
~/development/products/{product-name}/
├── {product-name}-PRD.md          # SINGLE FILE - ALL versions tracked (from product-PRD-template.md)
├── {product-name}-DesignBrief.md  # Design specifications (from design-brief-template.md)
├── DEVELOPMENT_STATUS.md          # Real-time project status (from DEVELOPMENT_STATUS-template.md)
├── CLAUDE.md                      # Claude Code instructions (from product-claude-template.md)
├── enhanced-product-workflow-tracker.md # Product-specific workflow tracking (moved from tools/workflows/)
├── BACKLOG.md                     # Product-specific development backlog (moved from root)
├── README-original.md             # Archived original README for the product (moved from root)
│
├── research/                       # Research outputs from AI tools
│   ├── perplexity-analysis.md     
│   ├── gemini-validation.md       
│   ├── competitive-landscape.md   
│   ├── user-validation.md         
│   └── red-team-analysis.md       
│
├── design/                        # Design workflow
│   ├── wireframes/
│   │   ├── user-journey-map.md
│   │   ├── information-architecture.md
│   │   └── screen-definitions/
│   ├── exports/
│   │   ├── uxpilot-output/           # PRIMARY: Wireframes and specifications
│   │   │   ├── html-wireframes/      # Individual page exports
│   │   │   ├── navigation-map.md     # Component relationships
│   │   │   ├── asset-specifications/ # Placeholder documentation
│   │   │   └── conversion-guide.md   # Instructions for Claude Code (from uxpilot-conversion-guide-template.md)
│   │   ├── lovable-output/           # Alternative: Full application code
│   │   └── figma-exports/            # Optional: Design assets
│   ├── design-system/
│   │   ├── components.2md
│   │   ├── style-guide.md
│   │   ├── brand-guidelines.md
│   │   └── design-tokens.md          # Design tokens (from design-tokens-template.md)
│   └── tool-prompts/
│       ├── uxpilot-prompt.md        # PRIMARY: Complete UXPilot specifications (from uxpilot-prompt-template.md)
│       ├── uxpilot-asset-specs.md   # Asset specifications extracted (from uxpilot-asset-specs-template.md)
│       ├── lovable-prompt.md        # Alternative: Full app generation
│       └── figma-instructions.md    # Optional: Design system setup
│
├── epics/                          # Development planning
│   ├── 01-environment.md          # Setup & tooling (from EPIC-environment-template.md)
│   ├── 02-core-features.md        # Core functionality (from EPIC-feature-template.md)
│   ├── 03-integrations.md         # External services (from EPIC-integration-template.md)
│   ├── 04-testing.md              # Quality assurance (from EPIC-testing-template.md)
│   ├── 05-deployment.md           # Launch preparation (from EPIC-deployment-template.md)
│   └── audits_and_testing/        # Standardized audit and testing results
│       ├── ai-powered-unit-and-integration-testing.md (from ai-powered-unit-and-integration-testing-template.md)
│       ├── ai-driven-end-to-end-user-journey-testing.md (from ai-driven-end-to-end-user-journey-testing-template.md)
│       ├── comprehensive-api-testing.md (from comprehensive-api-testing-template.md)
│       ├── comprehensive-code-health-audit.md (from comprehensive-code-health-audit-template.md)
│       └── ui-ux-and-accessibility-audit.md (from ui-ux-and-accessibility-audit-template.md)
│
├── scripts/                        # Product-specific executable scripts
│   ├── performance-tests/          # Performance test scripts
│   │   └── homefalcon-performance-test.js # HomeFalcon performance test (moved from root)
│   └── tests/                      # Product-specific test scripts
│       ├── test-config.js          # Configuration test (moved from root)
│       └── test-database.js        # Database connection test (moved from root)
│
├── active-projects/
│   └── mvp/
│       ├── src/                    # Code from Claude Code
│       ├── design-integration/     # Design tool outputs
│       └── deployment/
│
└── enhancements/                   # Post-MVP workflow
    ├── performance/
    ├── features/
    └── optimization/
```

### Tools and Workflow Support Files
```
~/development/tools/
├── scripts/                        # Executable scripts for workflow automation
│   ├── doc-health-check.sh         # Script for documentation health checks (moved from tools/workflows/)
│   └── performance-tests/          # General performance test scripts
│       └── simple-performance-test.js # Simple performance test (moved from root)
│
├── workflows/                      # Core workflow definitions and related documentation
│   ├── WORKFLOW-MASTER.md          # Master workflow documentation
│   ├── SUBAGENT-REGISTRY.md        # Complete sub-agent catalog
│   ├── automation-plans/           # Plans for workflow automation tools
│   │   ├── AUTOMATION-SCRIPT-PLAN.md # Plan for documentation automation script (moved from tools/workflows/)
│   │   └── PATH-STANDARDIZATION-PLAN.md # Plan for path standardization (moved from tools/workflows/)
│   └── reports/                    # Reports generated from workflow processes
│       ├── CLOUD-SYNC-STATUS.md    # Cloud synchronization status (intended location, file not found)
│       ├── CROSS-REFERENCE-VALIDATION-REPORT.md # Report on cross-reference validation (moved from tools/workflows/)
│       ├── END-TO-END-WORKFLOW-TEST-REPORT.md # End-to-end workflow test report (intended location, file not found)
│       └── WORKFLOW_DOCUMENTATION_AUDIT_REPORT.md # Report on workflow documentation audit (moved from tools/workflows/)
│
├── mcp-integrations/               # Guides and configurations for MCP servers
│   ├── FETCH-MCP-GUIDE.md          # Guide for Fetch MCP server (moved from root)
│   ├── SUPABASE-MCP-GUIDE.md       # Guide for Supabase MCP server (moved from root)
│   ├── SERENA-MCP-GUIDE.md         # Guide for Serena MCP server
│   └── mcp-setup-guide.md          # General MCP setup guide (moved from root)
│
└── templates/                      # Standardized templates for documentation
    ├── README.md                   # Template usage guide
    └── ... (all other templates)
```

---

## Technology Standards

### Default Tech Stack (APOLLO Standard)
**Frontend**: React + TypeScript + Tailwind CSS + shadcn/ui  
**Backend**: Supabase (PostgreSQL + Edge Functions) or Next.js API routes  
**Database**: Supabase PostgreSQL with Row Level Security  
**Auth**: Supabase Authentication  
**Storage**: Supabase Storage  
**Hosting**: Vercel (Frontend) + Supabase (Backend/Database)  
**Payments**: Stripe  
**AI/Vector**: pgvector (via Supabase)

**Tech Stack Details**: See [TECH-STACK-BLUEPRINT.md](../tech-stack/TECH-STACK-BLUEPRINT.md)

### Performance Requirements
- **Page Load**: < 2 seconds
- **API Response**: < 500ms (95th percentile)
- **Infrastructure Cost**: < $0.10/user
- **Bundle Size**: < 500KB
- **Uptime**: 99.9%

### Architecture Principles
- **Supabase-First**: Leverage managed services to reduce operational overhead
- **AI-Friendly Architecture**: Use structured, predictable patterns (AIX > DX)
- **Cost-Conscious**: Design for <$0.10/user from day one
- **Progressive Enhancement**: Start simple, add complexity when validated
- **Source Code Ownership**: Prefer shadcn/ui's copy-paste model over black-box libraries

---

## Context Window Planning Standards

### Context Window Estimates
- **Micro**: 0.1-0.3 windows (Simple updates, small fixes)
- **Mini**: 0.5-1 window (Single feature, component creation)
- **Standard**: 1-2 windows (Complex feature, integration work)
- **Complex**: 3+ windows (Architecture changes, major features)

### Planning Guidelines
- All estimates in context windows, not time
- Add 30% buffer for honesty in estimates
- Track actual vs. estimated for continuous improvement
- Break complex tasks into standard or smaller chunks

---

## Integration Points

### With MCP Servers
**Task Master Integration**: 38 advanced project management tools
- Project initialization and task generation
- PRD parsing and task breakdown
- Research coordination and synthesis
- Progress tracking and quality gates

**Other MCP Servers**:
- Filesystem: Enhanced file operations
- Brave Search: Web research capabilities
- GitHub Integration: Repository management
- Sequential Thinking: Complex reasoning support

### With External Tools
**Design Tools**: UXPilot (primary), Lovable, Figma
**Research Tools**: Perplexity, Gemini, Claude
**Development Tools**: Claude Code, GitHub, Vercel
**Analytics**: Stripe, Mixpanel, monitoring tools

### UXPilot Integration Best Practices
**Configuration Standards**:
- Always use Wireframes mode for optimal structure
- Export individual HTML files for easier component extraction
- Maintain consistent Page Context across all pages in session
- Follow placeholder naming convention: `[ASSET TYPE: Description dimensions]`

**Workflow Optimization**:
- Create all pages in single UXPilot session for design consistency
- Document navigation relationships during wireframe creation
- Extract asset specifications before creating actual assets
- Verify Tailwind classes align with APOLLO cost optimization standards

---

## Emergency Procedures

### Development Blocked >4 Hours
1. Document blocker in DEVELOPMENT_STATUS.md
2. Attempt 2 alternative approaches
3. Engage user if no progress
4. Update context window estimates
5. Never let perfect block good

### Cost Overrun Alert
1. Immediate audit of all services
2. Right-size resources (downgrade if needed)
3. Implement aggressive caching
4. Document savings achieved
5. Update cost models

### Technical Infeasibility Discovery
1. Stop work immediately
2. Document specific barriers
3. Propose 3 pivot options
4. Update Gate 2 assessment
5. Communicate transparently

---

## Success Metrics and KPIs

### Development Velocity Metrics
- **Research Phase**: Days from spark to PRD v0.5
- **Design Phase**: Hours from PRD v1.0 to working prototype
- **Development Phase**: Context windows from design to MVP
- **Total Timeline**: Days from idea to deployable product

### Quality Metrics
- **Design Integration Success Rate**: % of design exports requiring minimal code changes
- **Strategic Preservation**: % of original market intent maintained through v1.0
- **Technical Debt**: Code quality score of final MVP
- **User Satisfaction**: Early user feedback on design and functionality

### Revenue Metrics
- **Time to First Revenue**: Days from launch to first payment
- **Cost per User**: Infrastructure and operational costs
- **Conversion Rate**: Trial to paid conversion
- **Monthly Recurring Revenue**: Growth rate and sustainability

---

## Continuous Improvement

### Workflow Reflection Protocol
After each major milestone, complete this reflection:

```markdown
## Workflow Reflection: {Milestone}
**Date**: [Current date]
**Product**: [Product name]
**Phase Completed**: [Phase description]

### Process Effectiveness (1-10): [Rating]
**Workflow Clarity**: [How clear were the processes]
**Agent Coordination**: [How well did agents work together]
**File Organization**: [How well did file structure work]
**Timeline Accuracy**: [Estimated vs. actual time]

### Quality Assessment (1-10): [Rating]
**Output Quality**: [Quality of deliverables]
**Strategic Alignment**: [Maintained strategic intent]
**Technical Excellence**: [Code and architecture quality]
**User Value**: [Delivered value to users]

### Improvement Recommendations
- [Specific process improvement]
- [Agent coordination enhancement]
- [File structure optimization]
- [Timeline estimation improvement]

### Next Phase Readiness
**Ready to Proceed**: [Yes/No]
**Blocking Issues**: [Any issues preventing progress]
**Required Actions**: [Actions needed before next phase]
```

### Version History Tracking
All major workflow changes must be documented:

```markdown
## Workflow Version History
| Version | Date | Changes | Impact |
|---------|------|---------|--------|
| 1.0 | 2025-06-24 | Initial consolidated workflow | Baseline |
```

---

## Document Maintenance

### Update Procedures
1. **Major Changes**: Require version increment and change log
2. **Minor Updates**: Update timestamp and note in change log
3. **Cross-References**: Must be updated when file structure changes
4. **Validation**: Changes must be tested with actual workflow execution

### Change Log
| Date | Editor | Changes | Version |
|------|--------|---------|---------|
| 2025-06-24 | Claude Code | Initial creation from consolidated workflow docs | 1.0 |
| 2025-07-02 | Gemini | Updated template references, progressive documentation principles, and file architecture standards. | 1.2 |
| 2025-07-02 | Gemini | Reorganized files from the root `/development/` directory into their appropriate product or tools subfolders, and updated file architecture standards. Noted missing files. | 1.5 |
| 2025-07-02 | Gemini | Integrated the detailed tech stack analysis into a new `TECH-STACK-BLUEPRINT.md` and updated `WORKFLOW-MASTER.md` to reference it. | 1.6 |
| 2025-07-02 | Gemini | Moved MCP guides to `tools/mcp-integrations/` and updated references to reflect this. | 1.4 |
| 2025-07-02 | Claude Code | Updated tech stack to emphasize Supabase as primary backend/database solution, added Supabase-specific workflow steps in Phase 2 and Phase 4, updated all Railway references to Supabase | 1.7 |

---

*This document serves as the master reference for all workflow processes. All other workflow-related files should reference this document rather than duplicating its content.*