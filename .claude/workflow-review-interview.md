# Comprehensive Skills Workflow Review — CPO-Level Interview Prompt

**Purpose**: Conduct a holistic review of all PRD lifecycle skills (v0.1-v1.0) through the lens of 20 years of Chief Product Officer experience. Extract principles and stage-appropriate decision frameworks that should inform every skill, then systematically improve the skills to reflect mature product development judgment.

**Context**: Recent work on `prd-v05-technical-stack-selection` revealed a critical flaw: the skill contained a premature cost optimization bias that conflicts with real product development practice. This interview is designed to:
1. Understand the user's core principles about stage-appropriate decision-making
2. Map those principles across the entire lifecycle (v0.1 through v1.0)
3. Identify similar hidden biases or assumptions in other skills
4. Create a unified framework that keeps all skills in sync with mature product judgment

**Interview Structure**: 7 sections, designed to flow naturally. Allow 60-90 minutes for comprehensive coverage.

---

## SECTION 1: Stage-Appropriate Decision-Making (15 min)

**Opening context**: In the recent tech stack skill update, we discovered that cost optimization during MVP creates distorted incentives. You corrected this by noting: "Use more expensive stack to get it live quicker and build a user base, then optimize with cheaper parts." This is about *stage-appropriate* decision frameworks.

### 1.1 Define the Product Stages You Use

**Question**: "Walk me through the stages you use to think about product development. For example, do you think about it as MVP → PMF → Series A → Scale? Or different stages? What are the defining characteristics of each stage that matter for decision-making?"

**What we're looking for**:
- How you define stage transitions
- What metrics or milestones define each stage
- How decision-making should fundamentally shift between stages
- Whether there are substages (e.g., "Pre-launch MVP" vs. "post-launch MVP with users")

### 1.2 Cost vs. Velocity Trade-off by Stage

**Question**: "For each stage you described, what should be the optimization priority? For example, MVP might be: velocity (speed to market) > quality > cost. Series A might be: quality > cost > velocity. Is that how you think about it, or different?"

**Follow-up**: "Give me an example of a technology decision where you chose the more expensive option in early stage because it was faster to market. What was the outcome?"

**What we're looking for**:
- Your personal conviction about when to optimize vs. when to pay for velocity
- How you weight speed, quality, and cost at each stage
- Real examples that show the principle in practice
- Any exceptions or nuances (e.g., "cost matters even in MVP if you're bootstrap-funded")

### 1.3 Post-PMF Cost Optimization

**Question**: "Once a product reaches PMF and you decide to scale, how should cost optimization work? Do you have a process for revisiting tech decisions? When do you *not* optimize costs (e.g., when does the expensive solution stay even post-PMF)?"

**What we're looking for**:
- How to structure the transition from MVP to cost-aware scaling
- What decisions get revisited vs. which ones are locked in
- When vendor lock-in is acceptable vs. problematic
- How to balance optimization with stability

---

## SECTION 2: Quality Attributes by Stage (15 min)

**Opening context**: Beyond cost, other quality attributes (performance, reliability, security, maintainability) should also be stage-appropriate. A startup MVP doesn't need 99.99% uptime, but a fintech product does.

### 2.1 Risk and Compliance by Stage

**Question**: "In the PRD lifecycle, we have RISK- entries that constrain technology decisions. How should risk assessment differ between stages? For example, should an MVP in healthcare or finance have the same compliance rigor as a post-PMF scaling product?"

**Follow-up**: "Give me an example where you took a risk in MVP that you addressed later, and where you didn't take that risk."

**What we're looking for**:
- Which risks are non-negotiable from day one (e.g., user data privacy) vs. which can be deferred
- How to distinguish between "we'll fix this post-PMF" vs. "this breaks the product if we ignore it"
- Your judgment on which constraints are real vs. which are overcautious

### 2.2 Performance, Reliability, and Maintainability Expectations

**Question**: "How should expectations for performance, uptime, and code quality evolve across stages? For instance, MVP code might be messy but fast to ship; should the tech stack skill guide people toward 'clean code' or 'shipping code'? When do you invest in maintainability?"

**What we're looking for**:
- Your philosophy on technical debt: when is it acceptable, when is it dangerous
- How to structure MVP decisions so they don't create tech debt nightmares later
- When to refactor vs. when to live with messiness

---

## SECTION 3: Decision Framework Principles (15 min)

**Opening context**: The tech stack skill uses a decision framework: Reuse → Vendor-fit → Non-vendor alternatives → Build custom. This is essentially "reuse first, buy if you can't reuse, build only as last resort."

### 3.1 Build vs. Buy vs. Reuse Philosophy

**Question**: "Do you agree with the principle: Reuse first (lowest risk), then Buy (proven solutions), then Build (only if it's a differentiator)? Or do you have a different framework?"

**Follow-up**: "Give me an example where you broke this rule and built something commoditized, or where you bought something and regretted it."

**What we're looking for**:
- Whether the Reuse → Buy → Build hierarchy holds across all product stages
- How to identify true differentiators vs. false differentiators (resume-driven development)
- Your instinct on when to trust vendors vs. build control

### 3.2 Applying Frameworks Across the Lifecycle

**Question**: "The PRD lifecycle has stages v0.1 (Problem), v0.3 (Design), v0.5 (Risk), v0.6 (Architecture), v0.7 (Build), v0.8 (Release), v0.9 (Launch), v1.0 (Scale). For each stage, what framework should guide decision-making? Should a v0.1 problem definition framework be different from v0.7 build execution framework?"

**What we're looking for**:
- How different skills should have stage-appropriate guidance
- Whether to have separate frameworks or unified principles with stage-specific application
- Any patterns that repeat across stages

---

## SECTION 4: Hidden Biases and Assumptions (10 min)

**Opening context**: The tech stack skill had a hidden bias: "estimate costs at 10x scale." This created wrong incentives. We want to surface other biases.

### 4.1 Biases to Audit

**Question**: "Looking at the skills workflow (problem definition, requirements, risk discovery, tech stack, architecture, build, release, launch, scale), what biases or assumptions do you think exist? For example:
- Are they too optimistic about what MVP should accomplish?
- Are they too cost-conscious too early?
- Are they too focused on greenfield vs. brownfield?
- Are they biased toward certain industries (SaaS, B2B, venture-backed)?
- Are they biased toward certain team sizes or maturity?

What would you change?"

**What we're looking for**:
- Blind spots in the current methodology
- Assumptions that don't hold across different product contexts (B2B vs. B2C, startup vs. enterprise, different industries)
- Any patterns where the skill gives wrong advice to certain audiences

### 4.2 Context-Dependent Judgment

**Question**: "Are there situations where the 'normal' framework breaks down? For example:
- Regulated industries (healthcare, finance, government)?
- Open-source vs. commercial products?
- Bootstrap-funded vs. VC-backed?
- Consumer vs. enterprise?
- Build-in-public vs. stealth?

How should the skills adapt for these contexts?"

**What we're looking for**:
- When to apply standard frameworks vs. when to override them
- Which frameworks are truly universal vs. which are startup-SaaS assumptions
- How to make skills flexible without becoming prescriptive

---

## SECTION 5: Workflow Integration and Cascade (10 min)

**Opening context**: The lifecycle is sequential (v0.1 → v0.3 → v0.5 → ...), but each stage should inform downstream stages. For example, risks discovered in v0.5 should constrain tech selections in v0.6.

### 5.1 Cross-Stage Consistency

**Question**: "Looking at how decisions cascade downstream:
- Should a v0.3 feature definition constrain what we can decide in v0.6 architecture? When?
- Should v0.5 risk discovery cause us to revisit v0.3 features? How do you know when it should?
- Should v0.7 build execution surface problems that require going back to v0.6 architecture or v0.5 risk discovery? How often is this normal vs. a sign of bad upstream work?

In your experience, what's the healthy frequency of backpropagation vs. sign of dysfunction?"

**What we're looking for**:
- Your mental model of how upstream work constrains downstream decisions
- How much rework is acceptable/expected vs. a sign of poor process
- Whether the skills are designed to surface conflicts early or if they emerge later

### 5.2 Handoff Quality

**Question**: "When one stage hands off to the next, what makes a good handoff? For example, what does v0.5 Risk Discovery need to hand off to v0.6 Architecture such that Architecture can work independently without re-doing risk work? What do you want to see in that handoff document?"

**What we're looking for**:
- Your standards for "done"ness
- What downstream teams should NOT have to rethink
- How to prevent rediscovery and repetition

---

## SECTION 6: Skill-by-Skill Feedback (20 min)

**Opening context**: We're going to walk through each skill (v0.1-v1.0) quickly and gather your judgment on whether the skill is asking the right questions and using stage-appropriate frameworks.

### For each skill listed below:

**Template question**: "[Skill name]. What's the purpose of this stage in the lifecycle? What are we trying to accomplish? Is the current skill design (brief overview provided below) accomplishing that well, or does it miss something important? What would you change?"

**v0.1 Problem Discovery**
- Current: Identifies user jobs-to-be-done, pain points, and market opportunity
- Question: "Are we asking the right discovery questions? What would a 20-year CPO add here?"

**v0.3 Feature Requirements & Prioritization**
- Current: Maps features to user needs, scores by importance/impact, prioritizes MVP scope
- Question: "How do we decide what goes in MVP vs. post-launch? What criteria should we use? How should we know when we have 'enough' features?"

**v0.5 Risk Discovery & Constraint Identification**
- Current: Identifies technical/market/business risks, compliance needs, constraints
- Question: "What are we *missing* in risk discovery? What risks do products actually hit that we don't surface?"

**v0.5 Technical Stack Selection**
- Current: Chooses Reuse/Buy/Build for each capability layer (already improved based on your feedback)
- Question: "Beyond the cost optimization feedback you already gave, are there other blind spots here?"

**v0.6 Architecture Design**
- Current: Maps requirements to system components, defines interfaces, documents non-functional requirements
- Question: "Is the skill helping architects make the right trade-offs? What's missing?"

**v0.6 Technical Specification (API/Data/...)**
- Current: Defines detailed API specs, data models, etc.
- Question: "When should technical specs be detailed vs. lightweight for MVP? How do you know?"

**v0.7 Build Execution (EPIC/Task breakdown)**
- Current: Breaks work into EPICs and tasks, aligns to lifecycle, creates test/deployment plans
- Question: "How should build execution differ between MVP rush and 'normal' development? What tells you when you need to cut corners vs. invest in quality?"

**v0.8 Release & Quality Assurance**
- Current: Defines test coverage, deployment strategy, rollback plans, monitoring
- Question: "MVP vs. production: how risky should releases be? When do you invest in observability vs. ship with minimal monitoring?"

**v0.9 Launch & Go-to-Market**
- Current: GTM strategy, user acquisition, feedback loops, metrics
- Question: "How do you know when a product is ready to launch? What tells you you're moving too fast vs. too slow?"

**v1.0 Scale & Optimization**
- Current: Growth roadmap, cost optimization, technical debt paydown, hiring
- Question: "What should this stage focus on? How do you prioritize between new features, efficiency, and stabilization?"

**What we're looking for**:
- Which skills are most important (where bad work cascades)
- Which skills are over-engineered vs. under-engineered
- Which skills are missing context about stage-appropriate judgment

---

## SECTION 7: Synthesizing Principles (5 min)

**Closing question**: "Looking across all of this, what are the 3-5 core principles about product development that should infuse every skill? What's the mental model that ties it all together?"

**What we're looking for**:
- Your personal philosophy distilled to its essence
- The principles that, if embedded in skills, would make them work better
- Anything we missed in the previous sections

---

## INTERVIEW OUTPUT & NEXT STEPS

**How to use this interview:**

1. **Conduct the interview** (60-90 min) with the user, either in this context window or a new one
2. **Capture responses** verbatim where possible; note context and examples
3. **Synthesize findings** into a "CPO Principles" document
4. **Audit each skill** against those principles
5. **Update skills** systematically, starting with highest-impact stages

**Success criteria:**
- Every skill reflects stage-appropriate decision-making (MVP ≠ Scale)
- Hidden biases are surfaced and corrected
- Handoffs between stages are clear and prevent rework
- Skills are accessible to different product contexts (not just venture-backed SaaS)
- User's 20 years of judgment is embedded in the methodology

---

## Time Budget

- Section 1: 15 min
- Section 2: 15 min
- Section 3: 15 min
- Section 4: 10 min
- Section 5: 10 min
- Section 6: 20 min (2 min per skill × 10 skills)
- Section 7: 5 min
- **Total: ~90 minutes**

Can be conducted in one sitting or broken into 2-3 sessions of 30 min each.
