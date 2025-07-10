# APOLLO Development Workflow 🚀

> A rapid product development workflow system for building revenue-generating products in 14-21 day cycles

## Overview

APOLLO (Accelerated Product Optimization Launch Loop Operations) is a comprehensive workflow system designed to take products from idea to revenue in under 21 days. It combines AI-assisted development, progressive documentation, and gate-based quality checks to ensure rapid, yet sustainable product development.

### Key Features

- **14-21 Day Development Cycles** - From concept to deployed MVP
- **Revenue-First Focus** - Target $0.10/user infrastructure cost
- **AI-Augmented Workflow** - Leveraging Claude, Gemini, and specialized sub-agents
- **Gate-Based Quality Control** - 4 quality gates ensure product readiness
- **Progressive Documentation** - Single source of truth that evolves with the product
- **Test-First Development** - Built-in testing infrastructure from day one

## Quick Start

### Prerequisites

- Node.js 18+ and npm
- Git
- VS Code (recommended)
- Supabase CLI
- Vercel CLI

### Getting Started

1. **Clone this repository**
   ```bash
   git clone https://github.com/mattgierhart/PRD-driven-context-engineering.git
   cd PRD-driven-context-engineering
   ```

2. **Review the core workflow**
   - Start with [workflows/WORKFLOW-MASTER.md](workflows/WORKFLOW-MASTER.md)
   - Understand the 5 phases and 4 quality gates

3. **Choose your starting point**
   - **New Product**: Use templates in `templates/product/`
   - **Existing Product**: Follow enhancement workflows
   - **Learning**: Check `examples/sample-product/`

## The APOLLO Workflow

### 5 Phases of Development

1. **Product Definition** (3-5 days)
   - Market research and validation
   - PRD creation (v0.1 → v0.5)
   - Gate 1: Market opportunity validated

2. **Technical Feasibility** (2-3 days)
   - Tech stack analysis
   - Cost projections
   - Gate 2: Development timeline confirmed

3. **Product Design** (3-5 days)
   - UX journey mapping
   - Design system creation
   - Gate 3: Code-ready designs

4. **Product Development** (10-14 days)
   - Epic planning and execution
   - Test-driven development
   - Gate 4: Launch ready

5. **Product Enhancement** (Ongoing)
   - Performance optimization
   - Feature additions
   - Scaling infrastructure

### Standard Tech Stack

- **Frontend**: React + TypeScript + Tailwind CSS + shadcn/ui
- **Backend**: Supabase (PostgreSQL + Edge Functions)
- **Hosting**: Vercel + Supabase
- **Payments**: Stripe
- **AI/Vectors**: pgvector

## Repository Structure

```
apollo-development-workflow/
├── workflows/              # Core workflow documentation
├── templates/              # Ready-to-use project templates
├── tools/                  # Automation scripts and configs
├── examples/               # Sample implementations
└── docs/                   # Additional guides
```

## Key Concepts

### Progressive Documentation
- Single PRD file tracks all versions (v0.1 → v1.0)
- EPICs evolve throughout development
- Git history provides versioning

### Model Usage Protocol
- **Planning**: Use Opus for complex architecture
- **Execution**: Use Sonnet for implementation
- **Review**: Gemini for strategic analysis

### Quality Gates
- Gate 1: Market validation
- Gate 2: Technical feasibility
- Gate 3: Design complete
- Gate 4: Launch ready

## Templates

### Product Templates
- [Product PRD Template](templates/product/product-PRD-template.md)
- [Product Claude.md Template](templates/product/product-claude-template.md)

### Epic Templates
- [Feature Epic](templates/epics/EPIC-feature-template.md)
- [Environment Epic](templates/epics/EPIC-environment-template.md)
- [Testing Epic](templates/epics/EPIC-testing-template.md)
- [Integration Epic](templates/epics/EPIC-integration-template.md)
- [Deployment Epic](templates/epics/EPIC-deployment-template.md)

### Testing Templates
- [Unit Test Plan](templates/testing/test-unit-plan-template.md)
- [Integration Test Plan](templates/testing/test-integration-plan-template.md)
- [E2E Test Plan](templates/testing/test-e2e-plan-template.md)

## Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

### How to Contribute

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

### Areas for Contribution

- New templates
- Workflow improvements
- Case studies
- Tool integrations
- Documentation

## Community

- **Discussions**: Use GitHub Discussions for questions
- **Issues**: Report bugs or request features
- **Show & Tell**: Share your APOLLO success stories

## Resources

### Documentation
- [Complete Workflow Guide](workflows/WORKFLOW-MASTER.md)
- [Sub-Agent Registry](workflows/SUBAGENT-REGISTRY.md)
- [Model Usage Guide](workflows/MODEL-USAGE-GUIDE.md)
- [Progressive Documentation](workflows/PROGRESSIVE-DOCUMENTATION-GUIDE.md)

### External Tools
- [Claude Code](https://claude.ai/code)
- [Supabase](https://supabase.com)
- [Vercel](https://vercel.com)
- [shadcn/ui](https://ui.shadcn.com)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Built with and for Claude Code
- Inspired by rapid product development methodologies
- Community feedback and contributions

---

**Ready to build?** Start with the [Getting Started Guide](docs/getting-started.md) or jump into the [templates](templates/)!
