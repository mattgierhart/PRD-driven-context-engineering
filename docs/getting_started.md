# Getting Started with Gear Heart Methodology (GHM)

This guide will walk you through your first product build using the GHM workflow.

## Prerequisites

Before you begin, ensure you have:

- **Python 3.10+** for GHM validation tools
- **Git** for version control
- **Your preferred editor** (VS Code, Cursor, etc.)
- **GitHub account** for repository hosting
- **Your preferred backend/hosting** (choose based on your project needs)

### Install GHM Tools

```bash
# Clone the GHM repository
git clone https://github.com/mattgierhart/PRD-driven-context-engineering.git
cd PRD-driven-context-engineering

# Install Python dependencies for visualization tools
pip install -r tools/requirements.txt

# Optional: Install Graphviz for ID graph generation
# macOS: brew install graphviz
# Ubuntu: sudo apt-get install graphviz
# Windows: https://graphviz.org/download/
```

## Your First GHM Product

### Step 1: Define Your Product Idea

Start with a clear problem statement:
- Who is your target user?
- What problem are they facing?
- How will your solution help?

### Step 2: Create Your PRD

1. Copy the PRD template:
   ```bash
   cp templates/product/product-PRD_template.md ~/development/products/my-product/my-product-PRD.md
   ```

2. Fill out the initial sections (v0.1):
   - Product vision
   - Target audience
   - Core features

### Step 3: Market Research (Gate 1)

Use the research phase templates to:
- Analyze competitors
- Validate market size
- Confirm revenue potential

**Gate 1 Criteria**: 
- Clear market need identified
- Revenue potential of $1K-$10K/month
- Competitive advantage defined

### Step 4: Technical Planning (Gate 2)

1. Choose your tech stack based on project requirements
2. Estimate infrastructure costs
3. Define architecture approach

**Gate 2 Criteria**:
- Clear architecture documented
- Infrastructure costs estimated
- Technical risks identified

### Step 5: Design Phase (Gate 3)

1. Create user journey maps (UJ-XXX IDs)
2. Design information architecture
3. Generate UI designs using your preferred tools

**Gate 3 Criteria**:
- User journeys documented with IDs
- Design system defined
- Key screens designed

### Step 6: Development (Gate 4)

1. **Set up your project structure**:
   ```bash
   # Copy GHM templates to your project
   cp -r templates/product/ my-product/
   cp -r templates/epics/ my-product/epics/
   cp -r templates/source_of_truth/ my-product/source_of_truth/
   ```

2. **Create your EPICs**:
   - Use EPIC templates from `templates/epics/`
   - Break down features into tasks with ID references
   - Prioritize MVP features

3. **Implement with ID traceability**:
   - Reference BR-XXX, API-XXX in commits
   - Update SoT files as you implement
   - Keep Session State current in EPICs

**Gate 4 Criteria**:
- All MVP features complete
- Tests passing (TEST-XXX validated)
- SoT files up to date

## Common Workflows

### Daily Development Flow

1. **Morning**: Review EPICs and plan day
2. **Development**: Implement features test-first
3. **Testing**: Run full test suite
4. **Evening**: Update progress in EPICs

### Using AI Assistants

- **Claude Code**: Primary development
- **Gemini**: Strategic reviews at gates
- **Specialized Agents**: Performance, testing, etc.

### Progressive Documentation

Instead of creating new documents:
1. Update existing PRD (v0.1 → v0.2 → etc.)
2. Evolve EPICs as you learn
3. Keep single source of truth

## Tips for Success

### Speed Optimization
- Use existing templates
- Leverage AI for boilerplate
- Focus on MVP features only

### Cost Management
- Start with free tiers
- Monitor usage daily
- Optimize before scaling

### Quality Balance
- "Good enough" for MVP
- Polish after revenue
- Iterate based on feedback

## Next Steps

1. **Join the Community**
   - Star the repository
   - Join discussions
   - Share your progress

2. **Build Your First Product**
   - Start small
   - Ship fast
   - Iterate often

3. **Contribute Back**
   - Share your templates
   - Document learnings
   - Help others

## Troubleshooting

### Common Issues

**Problem**: Development taking too long
- **Solution**: Cut features aggressively, focus on core value

**Problem**: Context window overload
- **Solution**: Use ID references instead of pasting full docs; keep EPICs focused

**Problem**: Failing gates
- **Solution**: Re-evaluate assumptions, check SoT files for completeness

### Getting Help

- GitHub Discussions for questions
- Issues for bugs
- Community Discord (coming soon)

## Resources

- [Complete Workflow Guide](../methodology/workflows/WORKFLOW_MASTER.md)
- [Template Library](../templates/)
- [Repository Organization](../methodology/guides/REPO_ORGANIZATION.md)

---

Ready to build? Pick an idea and start with Phase 1!