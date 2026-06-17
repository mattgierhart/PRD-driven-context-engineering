# Design Tool Prompt Examples

> **Purpose**: Example prompts and workflow patterns for design tools (UX Pilot, Lovable, Figma)
> **Source**: Extracted during Phase 1 template purity cleanup (2026-01-10). Design components now live in SoT.DESIGN_COMPONENTS.md.
> **Use When**: Creating screen flows and design specifications during PRD v0.4

---

## UX Pilot Prompt Template

### Basic Structure

```
Create a [screen/component] for [product name] that:
- Serves [user persona] who wants to [user goal]
- Follows [design system] guidelines
- Includes [specific elements]
- Optimizes for [device/context]
- Achieves [success metric]

Style: [Design aesthetic]
Colors: [Color palette]
Typography: [Font choices]
Layout: [Grid/spacing approach]
```

### Example: Dashboard Screen

```
Create a dashboard screen for TaskFlow that:
- Serves busy project managers who want to see project status at a glance
- Follows Material Design 3 guidelines
- Includes status cards, recent activity feed, quick action buttons
- Optimizes for desktop (1920x1080) with mobile responsiveness
- Achieves task completion rate >90%

Style: Clean, professional, data-dense
Colors: Primary blue (#2563EB), neutral grays, success green (#10B981)
Typography: Inter for headings, system fonts for body
Layout: 12-column grid, 24px base spacing
```

### When to Use UX Pilot

**Best For**:
- Static mockups and wireframes
- Visual exploration of design concepts
- Rapid iteration on layouts
- Creating design system documentation

**Not Ideal For**:
- Interactive prototypes with complex state
- Production-ready code generation
- Detailed component specifications

---

## Lovable Prompt Template

### Basic Structure

```
Build a React component for [product name] that:
- Implements [specific functionality]
- Uses [design system/library]
- Handles [user interactions]
- Integrates with [APIs/data]
- Follows [coding standards]

Requirements:
- Responsive design
- Accessibility compliant
- Performance optimized
- Type-safe (TypeScript)
```

### Example: Task Card Component

```
Build a React component for TaskFlow that:
- Implements a task card with title, status, assignee, and due date
- Uses shadcn/ui components (Card, Badge, Avatar)
- Handles click to expand details, drag for reordering, status change on dropdown
- Integrates with /api/tasks endpoint for updates
- Follows Airbnb TypeScript style guide

Requirements:
- Responsive design (collapses to compact view on mobile)
- Accessibility compliant (ARIA labels, keyboard navigation)
- Performance optimized (React.memo, debounced API calls)
- Type-safe (Zod schema validation)
```

### When to Use Lovable

**Best For**:
- Production-ready React components
- Interactive functionality with state management
- API integration and data fetching
- Type-safe implementations

**Not Ideal For**:
- Initial visual exploration
- Design system creation
- Static mockups

---

## Figma Instructions Template

### Basic Structure

```
Design [screen/flow] with:
1. Create artboards for [breakpoints]
2. Use [design system/library]
3. Include [interactive states]
4. Prepare for [dev handoff format]
5. Export [asset specifications]
```

### Example: Onboarding Flow

```
Design user onboarding flow with:
1. Create artboards for desktop (1440px), tablet (768px), mobile (375px)
2. Use TaskFlow Design System (file: taskflow-ds.fig)
3. Include hover, active, disabled, loading states for all interactive elements
4. Prepare for dev handoff using Figma Dev Mode with CSS, React, Tailwind options
5. Export icons as SVG, images as WebP (2x resolution), spacing tokens as JSON
```

### When to Use Figma

**Best For**:
- Collaborative design with stakeholder review
- Design system creation and maintenance
- Detailed component specifications
- Asset export and developer handoff

**Not Ideal For**:
- Quick iteration (slower than AI tools)
- Code generation (manual process)
- Solo rapid prototyping

---

## Tool Selection Decision Framework

### Choose UX Pilot When...

- ✅ You need **visual concepts quickly**
- ✅ Exploring **multiple design directions**
- ✅ Creating **static mockups** for stakeholder review
- ✅ Building **design documentation**
- ✅ Working **solo** without design team

### Choose Lovable When...

- ✅ You need **production code** immediately
- ✅ Building **interactive components** with state
- ✅ Integrating with **APIs and backend**
- ✅ Implementing **specific functionality**
- ✅ **TypeScript/React** is your stack

### Choose Figma When...

- ✅ **Collaboration** with designers/stakeholders is critical
- ✅ Building a **design system** for reuse
- ✅ Need **pixel-perfect** control
- ✅ Creating **detailed specifications** for developers
- ✅ Working in a **team environment**

---

## Workflow Patterns

### Pattern 1: AI-First Rapid Prototyping

**Sequence**:
1. **UX Pilot** → Generate initial screen mockups
2. **Lovable** → Convert approved mockups to React components
3. **Manual refinement** → Polish edge cases and interactions

**When to Use**: Solo founders, MVPs, tight deadlines

**Pros**: Fast, integrated, minimal tooling
**Cons**: Less collaboration, harder to maintain design system

---

### Pattern 2: Figma-Led Design System

**Sequence**:
1. **Figma** → Create design system and component library
2. **Figma Dev Mode** → Export specifications to developers
3. **Manual coding** → Implement components following specs
4. **Lovable** (optional) → Generate boilerplate from specs

**When to Use**: Teams, long-term products, brand-critical work

**Pros**: Collaboration, consistency, reusability
**Cons**: Slower, more coordination overhead

---

### Pattern 3: Hybrid Approach

**Sequence**:
1. **UX Pilot** → Quick wireframes for user flow validation
2. **Figma** → Refine approved flows into design system
3. **Lovable** → Generate production components from Figma specs
4. **Iteration** → Update Figma, regenerate code

**When to Use**: Small teams, moderate timelines, quality focus

**Pros**: Balanced speed and quality
**Cons**: Requires tool-switching, some redundancy

---

## Common Pitfalls

### ❌ Anti-Pattern: Over-Designing Before Validation

**Mistake**: Spending weeks in Figma perfecting designs before user testing

**Problem**: Wasted effort on features users don't need or understand

**Fix**: Use UX Pilot for quick mockups → test with 5 users → refine in Figma

---

### ❌ Anti-Pattern: Code-First Without Design Thinking

**Mistake**: Jumping straight to Lovable without considering user flows

**Problem**: Functional but poorly designed interfaces

**Fix**: Map user journeys (UJ-XXX) first → then generate UI

---

### ❌ Anti-Pattern: Tool Mismatch

**Mistake**: Using Figma for solo rapid prototyping when UX Pilot would be faster

**Problem**: Slow iteration, context switching overhead

**Fix**: Match tool to context (see Decision Framework above)

---

## Prompt Engineering Tips

### For Better UX Pilot Results

1. **Be specific about constraints**: Screen size, device, accessibility
2. **Reference existing patterns**: "Similar to Stripe dashboard layout"
3. **Include success metrics**: "Optimizes for task completion rate"
4. **Specify design system**: "Follows Material Design" vs. "Custom minimal"

### For Better Lovable Results

1. **Provide type definitions**: Include TypeScript interfaces in prompt
2. **Specify libraries**: "Use shadcn/ui" vs. "Use raw Tailwind"
3. **Include edge cases**: Loading states, errors, empty states
4. **Reference API contracts**: Link to API-XXX entries for data shape

### For Better Figma Workflows

1. **Use components and variants**: Don't duplicate, reuse
2. **Name layers descriptively**: "btn-primary-hover" not "Rectangle 47"
3. **Organize with frames**: Group related elements logically
4. **Use auto-layout**: Makes responsive design easier

---

## Integration with PRD Lifecycle

### v0.4 User Journeys

**Tools Used**: Primarily UX Pilot for wireframes, Figma for flow diagrams

**Output**: Screen flows (SCR-XXX), user journey maps (UJ-XXX)

**Handoff**: Design specs → v0.5 Red Team Review

### v0.5 Red Team Review

**Tools Used**: Figma for stakeholder review, UX Pilot for quick iterations

**Output**: Revised mockups, risk mitigation designs

**Handoff**: Validated designs → v0.6 Architecture

### v0.6 Architecture & Technical Specification

**Tools Used**: Figma for component specs, Lovable for initial implementation

**Output**: Design system (DES-XXX), component library

**Handoff**: Design system → v0.7 Build Execution

---

## Example Prompts by PRD Stage

### v0.4: Initial Screen Flow

```
UX Pilot:
Create a mobile-first task creation screen for TaskFlow that:
- Serves UJ-101 (Quick Task Entry) user journey
- Includes title input, priority selector, assignee picker, due date
- Follows iOS Human Interface Guidelines
- Optimizes for one-handed use
- Achieves task creation in <30 seconds
```

### v0.6: Component Specification

```
Lovable:
Build a TaskCard React component that:
- Implements FEA-012 (Task Management) feature
- Uses shadcn/ui Card, Badge, Avatar components
- Handles API-045 (GET /tasks/:id) for data fetching
- Includes hover, loading, error states per DES-101 design system
- Follows BR-023 (task status validation) business rule

TypeScript interface:
interface Task {
  id: string
  title: string
  status: 'todo' | 'in_progress' | 'done'
  assignee: User
  dueDate: Date
}
```

---

## Usage Guide

### When Creating Design Components (SoT.DESIGN_COMPONENTS.md)

1. **Don't** embed these prompts in the design components file
2. **Do** reference this file: "See `.claude/skills/prd-v04-screen-flow-definition/references/design-tool-examples.md` for tool usage patterns"
3. **Do** customize prompts based on product-specific design system and constraints
4. **Do** link to UJ-XXX, FEA-XXX, API-XXX IDs for context

### When Executing Screen Flow Work

1. Read this reference file to understand tool options
2. Choose tool based on Decision Framework
3. Customize prompt templates with product-specific details
4. Generate screens and iterate
5. Document results as SCR-XXX entries

---

*End of design-tool-examples.md - Reference for prd-v04-screen-flow-definition skill*
