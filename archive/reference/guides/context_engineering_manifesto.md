# The Context Engineering Manifesto

## Preamble
We have traveled from the rigid cadence of waterfall to the agile heartbeat and now into a third epoch: context engineering. Waterfall prized upfront certainty but ossified teams. Agile celebrated iteration yet often left knowledge scattered in tickets and chats. Context engineering fuses discipline with memory. It treats documentation, IDs, and governance as the dynamic substrate where humans and AI co-create.

## From Waterfall to Agile to Context Engineering
- **Waterfall** assumed that truth could be frozen; change arrived through painful change control. Teams lost momentum when reality diverged from early plans.
- **Agile** restored adaptability, but the artifacts of change—stories, docs, diagrams—fractured across tools, increasing onboarding time and decision drift.
- **Context engineering** preserves agility while restoring coherence. It establishes predictable navigation files, a Source-of-Truth (SoT) library, and temp spaces that channel experimentation into durable knowledge. The goal is not just faster delivery but a living memory that any teammate—human or AI—can enter without ceremony. 【F:README.md†L14-L83】

## Principles for Durable Momentum
1. **Single Source of Truth, Not Slideware**  
   Every concept earns a home in the SoT library, backed by durable IDs (`BR-XXX`, `UJ-XXX`, `API-XXX`). We treat duplication as a defect and harvest temporary work before archive. This discipline prevents drift and anchors decisions in one canonical place. 【F:README.md†L22-L83】

2. **3+1+SoT+Temp Stack as Dynamic Memory**  
   Navigation files (`CLAUDE.md`, PRD, README) orient newcomers in minutes, the active EPIC frames the current window of work, and SoT IDs provide precise recall. Temp areas exist only to accelerate synthesis into the graph. Together they form a predictable memory layout that AI can load and reason over with minimal tokens. 【F:README.md†L27-L71】

3. **Gate-Based Execution with Tests Upfront**  
   Progress is earned through gates that align quality, security, performance, and business rules. Tests, datasets, and benchmarks are declared early so that AI output is evaluated, not blindly trusted. IDs link journeys, rules, and feedback to the checks that guard them. 【F:README.md†L84-L120】

4. **Context Governance Over Context Window**  
   Authority flows from product README and SoT, with stable paths (`templates/product/`, `templates/epics/`, `templates/source_of_truth/`) that humans and automation can predict. Instead of overflowing prompts, we reference IDs that summon exactly the needed context. 【F:README.md†L72-L133】

## Documentation as Onboarding and Offboarding
Documentation is not a chore; it is the memory palace that lets teams pivot without losing fidelity. A new contributor lands in the README, follows links into SoT IDs, and sees the current EPIC deltas. Departing teammates leave behind structured references, not tribal knowledge. AI agents re-enter mid-stream and reconstruct state from the same anchors, enabling multi-agent collaboration without repetitive context dumps. 【F:README.md†L14-L71】

## AI as Contextual Partner
In context engineering, AI is not an isolated assistant but a member of the delivery system. By speaking the language of IDs, agents retrieve precise specs, compare feedback to journeys, and propose changes without rehydrating entire documents. The SoT graph becomes a long-term memory that keeps AI aligned with product truth, ensuring that recommendations serve the team's momentum rather than a single user's prompt. 【F:README.md†L46-L83】

## Consistency Through Structure: Iteration Over Reinvention
One of the greatest challenges with AI-assisted development is the tendency toward reinvention. Without persistent structure, each session begins as a blank slate—AI agents guess at conventions, recreate patterns that already exist, and produce inconsistent artifacts. Context engineering solves this by making iteration the path of least resistance.

1. **Anchored Identity**
   The ID system (`BR-XXX`, `UJ-XXX`, `API-XXX`) provides durable reference points that persist across sessions and agents. When an AI sees `BR-101`, it doesn't invent a new interpretation—it retrieves the canonical definition. This transforms AI from a stateless generator into a contextual collaborator that builds on established foundations.

2. **One Document, Many Versions**
   The "Progressive Documentation Protocol" mandates updating existing documents rather than spawning new ones. No `PRD-v2.md`, no `design_final_FINAL.md`. When AI operates under this rule, every change becomes an incremental refinement to a living artifact, not a parallel universe of conflicting truth.

3. **Session Continuity Protocol**
   Each EPIC's Section 0 captures "Where we left off"—the exact file, line, and next step. AI agents don't restart; they resume. The handoff marker (`<!-- HANDOFF -->`) serves as a breadcrumb for context-limited sessions, enabling work to continue across boundaries without information loss.

4. **SoT as Gravitational Center**
   Source-of-Truth files act as attractors that pull work toward consistency. When specs live in `SoT.*.md` files with stable paths, AI naturally references and extends them rather than generating competing definitions. The structure itself encodes the preference for iteration.

5. **Traceability as Memory**
   The `@implements BR-XXX` pattern in code creates bidirectional links between implementation and intent. AI reading existing code sees not just what was built, but why—enabling informed iteration rather than uninformed replacement.

This architecture addresses a fundamental asymmetry: humans remember context effortlessly across sessions, but AI starts fresh each time. Context engineering bridges this gap by externalizing memory into navigable structure, making consistency the default behavior rather than an afterthought.

## Call to Action
We reject both the stagnation of waterfall and the entropy of ungoverned agility. We embrace context engineering: a practice where documentation is alive, IDs are currency, gates safeguard value, and AI augments every contributor. Maintain the navigation files, tend the SoT, and let context—not heroics—power our progress. 【F:README.md†L27-L120】
