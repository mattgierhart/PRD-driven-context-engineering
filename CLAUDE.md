# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Global Development Environment - APOLLO

### Development Mission
**Focus**: Rapid Product development for revenue generation (14-21 day cycles)
**Quality Standard**: Technically sound but fast, optimize for speed and cost
**Success Metric**: Time to first revenue, not technical perfection

### Standard Tech Stack
**Frontend**: React + TypeScript + Tailwind CSS + shadcn/ui
**Backend**: Supabase (PostgreSQL + Edge Functions) or Next.js API routes
**Database**: Supabase PostgreSQL with Row Level Security
**Auth**: Supabase Authentication
**Storage**: Supabase Storage
**Hosting**: Vercel (Frontend) + Supabase (Backend/Database)
**Payments**: Stripe
**AI/Vector**: pgvector (via Supabase)

### Directory Structure
```
~/development/
├── products/
│   ├── active-projects/    # Current development
│   ├── experiments/        # Quick validation projects  
│   ├── templates/         # Starter templates
│   └── archive/           # Completed projects
└── tools/                 # Development utilities
```

### Default Editor
**Primary**: VS Code (`code` command)
**Terminal**: Built-in terminal in VS Code

### Cost-First Development
- Start with Supabase free tier (generous limits)
- Target <$0.10/user infrastructure cost
- Monitor costs weekly via Supabase dashboard
- Budget alerts at $25 (Supabase Pro), $50, $100/month
- Upgrade only after revenue validation

### Standard Commands
```bash
# Project setup
npm create next-app@latest --typescript --tailwind --app
npm install @supabase/supabase-js @supabase/auth-helpers-nextjs
npm install stripe @stripe/stripe-js
npx shadcn-ui@latest init

# Development
npm run dev
npm run build
npm test

# Supabase
npx supabase init
npx supabase link --project-ref [project-id]
npx supabase gen types typescript --linked > types/supabase.ts

# Deployment  
npx vercel --prod
```

### Default Project Structure
```
/project-root
├── app/                   # Next.js app directory
├── components/            # Reusable components
├── lib/                   # Utilities and helpers
├── public/                # Static assets
├── styles/                # Global styles
└── types/                 # TypeScript definitions
```

### Security Defaults
- Environment variables for all secrets
- Input validation on all user inputs
- HTTPS enforcement
- Rate limiting for APIs
- Never commit .env files

### Performance Standards
- Page load: <2 seconds
- API response: <500ms (95th percentile)
- Core Web Vitals: Green scores
- Mobile-first responsive design

### Git Workflow
- Branch naming: `feature/description`, `fix/description`
- Conventional commits
- Squash and merge
- Main branch auto-deploys to production

### Claude Code Integration
- Load this global config for all projects
- Use `/init` command for new projects
- Use `/compact` during long development sessions
- Use `/clear` between distinct tasks
- See [CUSTOM-COMMANDS.md](tools/CUSTOM-COMMANDS.md) for workflow-specific commands

### Progressive Documentation Philosophy
**Core Principle**: When working on a product, prioritize progressing and updating existing .md files (e.g., PRDs, EPICs, technical documentation) rather than creating new ones, whenever feasible. This ensures a single, evolving source of truth and minimizes fragmentation of information.

**Implementation Guidelines**:
- Update PRD versions (v0.1 → v0.2 → v0.5) within the same file
- Append to EPIC files rather than creating new task documents
- Evolve design briefs incrementally
- Consolidate research findings into existing research files
- Version control through git history, not file proliferation

### Gemini Strategic Partnership

**Role Separation**: Claude Code (executor) + Gemini (reviewer/strategist)
**Core Directive Files**: `CLAUDE.md` (this file) and `Gemini.md` are immutable to each other
**Collaboration Space**: All other .md files are shared workspace

### Model Usage Protocol

**Planning Phase (Opus Model)**
- Complex architecture decisions
- Epic breakdown and detailed task planning
- Error resolution strategies when Sonnet is blocked
- Cross-epic dependency analysis
- Test strategy design
- Design system architecture

**Execution Phase (Sonnet Model)**
- Code implementation from detailed plans
- Simple bug fixes (up to 3 attempts)
- Test writing from specifications
- Documentation updates
- Routine maintenance
- Following detailed epic instructions

**Error Handling Protocol**
When Sonnet encounters blocking issues:
1. Make 3 reasonable attempts to resolve
2. Document the issue in the epic with:
   - Error details and stack traces
   - Attempted solutions
   - Context needed for resolution
3. Mark task as `blocked-for-opus` in epic
4. Continue with other non-dependent tasks
5. Generate handoff summary using `/handoff-claude` command

**Handoff Best Practices**
- Use `/plan` command reminder when switching to Opus
- Use `/execute` command reminder when switching to Sonnet
- Document model-specific sections in epics
- See [MODEL-USAGE-GUIDE.md](tools/workflows/MODEL-USAGE-GUIDE.md) for detailed protocols

#### When to Invoke Gemini

1. **PRD Review (Phase 1-2)**: After PRD v0.5 for strategic risk analysis
   ```
   "Gemini, please perform a full strategic review of the PRD for {product-name}."
   ```

2. **Code Review (Phase 4)**: After completing major features or epics
   ```
   "Gemini, I have completed the initial implementation for {product-name}. Please do a full codebase evaluation and add your findings to the relevant EPIC files."
   ```

3. **Architecture Decisions**: Before major technical choices or refactors
4. **Cross-Platform Strategy**: When building multi-platform products

#### Handling Gemini Feedback

- Gemini will update shared .md files (PRDs, EPICs) with actionable tasks
- Look for `### Gemini's Development Considerations` sections in EPICs
- Prioritize security, performance, and architectural feedback
- Incorporate feedback before proceeding to next gate

### Workflow and Sub-Agent Integration

**Complete Workflow Documentation**: [WORKFLOW-MASTER.md](tools/workflows/WORKFLOW-MASTER.md)  
**Complete Sub-Agent Registry**: [SUBAGENT-REGISTRY.md](tools/workflows/SUBAGENT-REGISTRY.md)

## APOLLO Product Development Workflow

The APOLLO workflow is a 5-phase, file-first approach to rapid product development:

### Phase 1: Product Definition (File-First Research)
**Timeline**: 3-5 context windows over 5-7 days  
**Owner**: AURA Strategic Lead + User  
**Location**: `~/development/products/{product-name}/`

1. **Market Spark** → PRD v0.1
2. **Market Research** → PRD v0.2 (Perplexity + Gemini validation)
3. **Competitive Analysis** → PRD v0.3
4. **User Validation** → PRD v0.4
5. **Red Team Analysis** → PRD v0.5 (Gate 1 Decision)
   - **Gemini Review**: Strategic risk analysis and alternative approaches

### Phase 2: Technical Feasibility (APOLLO Analysis)
**Timeline**: 1-2 context windows over 2-3 days  
**Owner**: APOLLO Technical Lead

1. **Tech Stack Analysis** → PRD v0.6
2. **Feasibility Scoring** → PRD v0.7 (Gate 2 Decision)

### Phase 3: Product Design (Design-First Approach)
**Timeline**: 2-3 context windows over 3-5 days  
**Owner**: AURA (Design Strategy) + Product Designer Agent + User

1. **UX Journey Mapping** → PRD v0.8
2. **Information Architecture** → PRD v0.9
3. **Design Brief Creation** → PRD v1.0
4. **UXPilot Design Generation** (Primary Tool - Wireframes Mode)
5. **Design System Integration** (Gate 3 Decision)

### Phase 4: Product Development (Enhanced File-Based)
**Timeline**: 5-8 context windows over 10-14 days  
**Owner**: APOLLO + Claude Code

1. **Epic Planning & Breakdown** (5 epic files)
2. **UXPilot-to-React Conversion** (Design integration)
3. **Test Infrastructure Validation**: Ensure all testing frameworks are correctly configured and existing tests pass. (Critical pre-development step)
4. **Development Execution** 
   - **Gemini Review**: Code evaluation, performance audit, and EPIC updates after major features
   - **Continuous Testing**: Run unit and integration tests frequently.
   - **Performance Monitoring**: Regularly check for performance regressions.
5. **Pre-Launch Review** (Gate 4 Decision - Launch Ready)

### Test-First Development Approach

**Philosophy**: Write tests alongside planning, implement against tests
**Timing**: After Gate 2 (Technical Feasibility) but before coding begins

#### Testing Integration Points

1. **During Epic Planning (Phase 4.1)**
   - Define testable acceptance criteria for each feature
   - Create test scenarios from user stories
   - Plan test data requirements
   - Identify edge cases and error scenarios

2. **Gate 3.5: Testing Infrastructure Verification** (NEW)
   Before any development begins:
   - Testing frameworks installed and configured
   - Sample tests passing for each layer (unit, integration, e2e)
   - Coverage reporting functional
   - Test database/mocks configured
   - CI/CD test pipeline ready

3. **During Development (Phase 4.4)**
   - Write tests before implementing features
   - Use tests to validate implementation
   - Maintain minimum 80% code coverage
   - Run tests before committing code

#### Standard Testing Setup by Stack

**React/Next.js Frontend**
```bash
npm install -D jest @testing-library/react @testing-library/jest-dom
npm install -D @testing-library/user-event jest-environment-jsdom
```

**Node.js/Express Backend**
```bash
npm install -D jest supertest jest-mock-extended
npm install -D @types/jest @types/supertest
```

**Supabase/PostgreSQL**
```bash
npm install -D @supabase/supabase-js jest-mock-extended
# Create /lib/__mocks__/db.ts for database mocking
```

See epic templates for detailed testing setup guides

### Phase 5: Product Enhancements (Subagent Integration)
**Timeline**: Ongoing post-launch  
**Owner**: Specialized Subagents

For complete workflow details, see [WORKFLOW-MASTER.md](tools/workflows/WORKFLOW-MASTER.md)

#### Core Workflow Agents
1. **AURA Strategic Lead** - Market research and product definition
2. **APOLLO Technical Lead** - Technical feasibility and development coordination  
3. **Product Designer Agent** - Design workflow and UX strategy

#### Development Enhancement Agents
4. **@tech-debt-finder-fixer** (Technical Debt Analysis & Fixing)
5. **@arch-review** (Architecture Analysis & Documentation)
6. **@test-gen** (Comprehensive Test Generation)
7. **@perf-optimize** (Performance Optimization)
8. **@migrate** (Migration Assistant)
9. **@refactor** (Intelligent Code Refactoring)
10. **@new-feature** (Feature Development)
11. **Design Integration Agent** (Design-to-Code Integration)

#### Quality Gates
- **Gate 1**: Research Complete (PRD v0.5) - Market opportunity validated
  - **Gemini Checkpoint**: Strategic risk analysis complete, alternative approaches considered
- **Gate 2**: Technical Feasibility (PRD v0.7) - Development timeline confirmed
- **Gate 3**: Design Complete - Code-ready design system integrated
- **Gate 4**: Launch Ready - MVP complete and tested
  - **Gemini Checkpoint**: Codebase evaluation complete, critical issues addressed

#### Key Success Criteria
- **Infrastructure Cost**: <$0.10/user validated at Gate 2
- **Development Timeline**: <14 days confirmed at Gate 2  
- **Performance Standards**: <2s page load, <500ms API response
- **Revenue Target**: $1K-$10K monthly potential identified at Gate 1

#### APOLLO-Specific Parameters (Available on All Subagents)
- `--revenue-focus` - Prioritize revenue-generating improvements
- `--mvp-priority` - Focus on MVP functionality
- `--cost-optimize` - Minimize operational costs (target: $0.10/user)
- `--design-integration` - Ensure design-to-code alignment
- `--progressive-enhancement` - Build incrementally
- `--gate-analysis` - Validate against APOLLO gate criteria

### Revenue Generation Focus
**Primary Goal**: Validate market demand within 21 days
**Secondary Goal**: Build foundation for scaling to $5K+/month
**Optimization Priority**: User conversion over technical perfection

## Project Structure Standards

All products follow a standardized structure after passing Gate 3:

### Product Location
- Products live in `~/development/products/{product-name}/`
- Each product must have:
  - `claude.md` - Technical instructions specific to this product
  - `{product-name}-PRD.md` - Product requirements document (single file, all versions)
  - `{product-name}-DesignBrief.md` - Design specifications
  - `research/` - Multi-AI research outputs
  - `design/` - Design workflow and exports
  - `epics/` - Development planning (5 epic files)
  - `active-projects/mvp/` - Current development work

### File Structure Standards
```
~/development/products/{product-name}/
├── {product-name}-PRD.md          # Single file - all versions tracked
├── {product-name}-DesignBrief.md  # Design specifications
├── research/                      # Multi-AI research outputs
├── design/                        # Design workflow and tool exports
├── epics/                         # 5 development epic files
└── active-projects/mvp/           # Code and deployment
```

### Shared Resources
- Reusable components: `~/development/tools/shared-components/`
- MCP integrations: `~/development/tools/mcp-integrations/`
- Scripts and automation: `~/development/tools/scripts/`
- Templates: `~/development/tools/templates/`

## MCP Server Integrations



### Available MCP Servers

- **Filesystem** - Enhanced file operations
- **Brave Search** - Web research capabilities
- **Puppeteer** - Browser automation
- **Sequential Thinking** - Complex reasoning support
- **GitHub Integration** - Repository management
- **Magic UI Design** - Design system support

### MCP Server Status Check
```bash
# Verify all MCP servers are running
ps aux | grep mcp
