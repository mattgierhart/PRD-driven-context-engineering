# [Product Name] Design Brief

## Authority, Template Usage, and Standards

- **Authority**: This document is governed by the processes and standards defined in [WORKFLOW-MASTER.md](../workflows/WORKFLOW-MASTER.md). All design activities must align with the established workflows.
- **Template Usage**: For detailed instructions on how to use this template, refer to the [Template Usage Guide](./README.md). This brief is a critical input for the Product Designer Agent and must be completed before any design work begins.
- **Standards**: All design outputs must adhere to the documentation and design standards outlined in [STANDARDS.md](../../STANDARDS.md). This includes naming conventions, design system usage, and accessibility requirements.

**Version**: 1.0
**Date**: [Date]
**Created By**: AURA Strategic Lead
**Product Stage**: Design Phase
**Related PRD**: v0.9 - v1.0

---

## Brand Identity & Voice

### Brand Personality
**Primary Traits**: [3-4 adjectives describing the brand]
**Secondary Traits**: [2-3 supporting characteristics]
**Voice Tone**: [Professional/Friendly/Technical/Casual]

### Visual Identity Direction
**Color Psychology**: [What colors convey the right message]
**Typography Strategy**: [Modern/Classic/Technical/Playful]
**Imagery Style**: [Photography/Illustrations/Icons approach]
**Overall Aesthetic**: [Clean/Bold/Minimal/Rich description]

---

## Target User Personas & Context

### Primary Persona: [Name]
**Demographics**: [Age, location, profession]
**Tech Comfort Level**: [High/Medium/Low]
**Usage Context**: [When/where/how they'll use the product]
**Device Preferences**: [Desktop/Mobile/Tablet priority]
**Accessibility Needs**: [Any specific requirements]

### Secondary Persona: [Name]
**Demographics**: [Age, location, profession]
**Tech Comfort Level**: [High/Medium/Low]
**Usage Context**: [When/where/how they'll use the product]
**Device Preferences**: [Desktop/Mobile/Tablet priority]
**Accessibility Needs**: [Any specific requirements]

---

## User Journey Maps

### Core User Journey: [Primary Use Case]
```
Awareness → Interest → Trial → Value → Habit → Advocacy
    |         |         |       |       |        |
[Touchpoint] [Touchpoint] [Touchpoint] [Touchpoint] [Touchpoint] [Touchpoint]
[Emotion]    [Emotion]   [Emotion]   [Emotion]   [Emotion]   [Emotion]
[Pain Point] [Pain Point] [Pain Point] [Pain Point] [Pain Point] [Pain Point]
```

### Critical Moments
1. **First Impression** (0-30 seconds)
   - Goal: User understands value proposition
   - Key Elements: Hero section, clear messaging
   - Success Metric: Time to "aha" moment

2. **First Value** (First session)
   - Goal: User experiences core benefit
   - Key Elements: Onboarding, feature discovery
   - Success Metric: Task completion rate

3. **Habit Formation** (Days 2-7)
   - Goal: User returns and engages regularly
   - Key Elements: Notifications, progress tracking
   - Success Metric: Weekly retention rate

---

## Information Architecture

### Site Map
```
Landing Page
├── Product Features
├── Pricing
├── About/Company
└── Authentication
    ├── Dashboard/Home
    ├── [Core Feature 1]
    ├── [Core Feature 2]
    ├── [Core Feature 3]
    ├── Settings/Profile
    ├── Help/Support
    └── Account Management
```

### Navigation Strategy
**Primary Navigation**: [Top bar/Sidebar/Tab approach]
**Secondary Navigation**: [Breadcrumbs/Sub-menus/Context menus]
**Mobile Navigation**: [Hamburger/Bottom tabs/Drawer]

---

## Screen Definitions & Requirements

### Landing Page
**Primary Goal**: Convert visitors to users
**Key Elements**:
- Hero section with value proposition
- Social proof/testimonials
- Feature highlights
- Clear CTA placement
**User Actions**: Sign up, learn more, see pricing

### Dashboard/Home
**Primary Goal**: Quick access to core functionality
**Key Elements**:
- Status overview/metrics
- Quick actions
- Recent activity
- Navigation to features
**User Actions**: Navigate to features, view status, take action

### [Core Feature Screen 1]
**Primary Goal**: [Main user objective]
**Key Elements**:
- [Interface element 1]
- [Interface element 2]
- [Interface element 3]
**User Actions**: [Action 1], [Action 2], [Action 3]

### [Core Feature Screen 2]
**Primary Goal**: [Main user objective]
**Key Elements**:
- [Interface element 1]
- [Interface element 2]
- [Interface element 3]
**User Actions**: [Action 1], [Action 2], [Action 3]

---

## Design System Selection

### Component Library Strategy
**Recommendation**: [Tailwind UI/shadcn/ui/Material UI/Custom]
**Rationale**: [Why this choice fits the product]
**Customization Level**: [Minimal/Moderate/Extensive]

### Design Token Strategy
**Colors**: [Primary palette approach]
**Typography**: [Font selection criteria]
**Spacing**: [Grid system approach]
**Elevation**: [Shadow/depth strategy]

---

## Tool Integration Strategy

### UX Design Tool Chain
**Primary Tool**: [UX Pilot/Lovable/Figma/Sketch]
**Rationale**: [Why this tool best fits our workflow]
**Output Format**: [Code/Assets/Specifications]

### Design-to-Code Workflow
**Code Generation**: [Level of automation expected]
**Hand-off Process**: [How design transfers to development]
**Review Cycles**: [How many iterations planned]
**Quality Gates**: [What needs approval before development]

### Asset Management
**Icon Strategy**: [Library selection]
**Image Strategy**: [Source and optimization approach]
**Animation Strategy**: [Level of motion design]

---

## Success Metrics & Validation

### Design Success Metrics
**Usability**: Task completion rate >90%
**Efficiency**: Time to complete core task <2 minutes
**Satisfaction**: User satisfaction score >4.5/5
**Accessibility**: WCAG 2.1 AA compliance
**Performance**: Page load <2 seconds

### Design Validation Plan
**Phase 1**: Static mockup review with stakeholders
**Phase 2**: Interactive prototype testing with 5-10 users
**Phase 3**: Development integration validation
**Phase 4**: Pre-launch usability testing

---

## Technical Constraints & Considerations

### Platform Requirements
**Responsive Breakpoints**: [Mobile-first/Desktop-first approach]
**Browser Support**: [Minimum browser versions]
**Device Support**: [Touch/Mouse/Keyboard considerations]

### Performance Budget
**Bundle Size**: [Maximum JS/CSS size]
**Image Optimization**: [Format and compression strategy]
**Loading Strategy**: [Progressive loading approach]

### Integration Requirements
**APIs**: [How design accommodates data requirements]
**Real-time Updates**: [Live data integration needs]
**Offline Capability**: [Offline design considerations]

---

## Design Tool Prompts

### UX Pilot Prompt
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

### Lovable Prompt
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

### Figma Instructions
```
Design [screen/flow] with:
1. Create artboards for [breakpoints]
2. Use [design system/library]
3. Include [interactive states]
4. Prepare for [dev handoff format]
5. Export [asset specifications]
```

---

## Project Timeline & Handoffs

### Design Phase Timeline
**Week 1**: Initial mockups and wireframes
**Week 2**: High-fidelity designs and prototype
**Week 3**: Design system creation and documentation
**Week 4**: Development handoff and integration

### Handoff Requirements
**To Development**:
- [ ] All screens designed and approved
- [ ] Design system documented
- [ ] Assets exported and optimized
- [ ] Specifications documented
- [ ] Interactive prototype complete

**Quality Gates**:
- [ ] Stakeholder approval on designs
- [ ] User testing validation (if applicable)
- [ ] Technical feasibility confirmed
- [ ] Performance budget validated

---

## 📍 Design Components (DES-XXX IDs)

> **Purpose**: Each design component gets a unique ID for cross-referencing
> **ID Format**: DES-XXX (sequential numbering)
> **Usage**: Reference these IDs from EPICs, user journeys, and component implementations

### Navigation by Category

**Core Components** (DES-001 to DES-099):
- [DES-001](#des-001-hero-section) - Landing page hero section
- [DES-002](#des-002-navigation-bar) - Primary navigation

**Feature Components** (DES-101 to DES-199):
- [DES-101](#des-101-product-card) - Product display card
- [DES-102](#des-102-checkout-flow) - Checkout user interface

**Shared Components** (DES-201 to DES-299):
- [DES-201](#des-201-button-system) - Button component system
- [DES-202](#des-202-form-inputs) - Form input components

**Design Patterns** (DES-301 to DES-399):
- [DES-301](#des-301-loading-states) - Loading state patterns
- [DES-302](#des-302-error-states) - Error state patterns

---

## DES-001: Hero Section

**ID**: DES-001
**Category**: Core Component
**Platform**: Web | Mobile | Both
**Status**: Active | Deprecated | Planned
**Created**: YYYY-MM-DD
**Last Updated**: YYYY-MM-DD
**Designer**: {Name}

### Component Overview

**Purpose**: Primary landing page hero that communicates value proposition
**Location**: Landing page, above the fold
**Priority**: Critical (first impression)

### Design Specifications

**Dimensions**:
- Desktop: 1200px width × 600px height
- Mobile: 375px width × 500px height
- Tablet: 768px width × 550px height

### Related IDs

**Used in User Journeys**:
- [UJ-001](../source-of-truth/USER-JOURNEYS-template.md#uj-001) - First-time visitor onboarding

**Design System References**:
- [DES-201](#des-201-button-system) - Button components used in CTAs

**Implemented in EPICs**:
- [EPIC-03](../epics/EPIC-template.md) - Landing page development

### Version History

| Version | Date | Changes | Updated By |
|---------|------|---------|------------|
| 1.0 | YYYY-MM-DD | Initial design | {Name} |

---

## Cross-Reference Index

> **Auto-Generated Section**: Run `npm run codex:sync-registry` to rebuild

**Components by User Journey**:
- UJ-001 uses: DES-001 (hero), DES-002 (navigation)

**Components by Platform**:
- Web: DES-001, DES-002
- Mobile: DES-002
- Both: DES-201, DES-202 (shared components)

---

## Update Protocol

### When to Add New DES-XXX IDs

1. **New UI Component**: Distinct, reusable interface elements
2. **Design Pattern**: Recurring design solutions (loading, errors, empty states)
3. **Page Template**: Complete page layouts with multiple components
4. **Design Token Update**: Major changes to colors, typography, spacing

### Bidirectional Reference Checklist

When adding a new DES-XXX:
- [ ] Update USER-JOURNEYS.md "Design Components" section with this DES-XXX
- [ ] Update EPIC Section 3A "IDs Created This EPIC" table
- [ ] Update README.md "Active IDs" section if part of current work
- [ ] Create corresponding React component file in `src/components/`
- [ ] Add UXPilot export reference (if applicable)
- [ ] Document accessibility requirements
- [ ] Run `npm run codex:sync-registry` to update ID-REGISTRY.md

---

*This design brief serves as the single source of truth for all design decisions and guides the transition from PRD v1.0 to development phase.*