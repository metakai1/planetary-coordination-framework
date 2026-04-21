# Governance

This document specifies how Layer 2 — the coordination layer — actually operates. It is the mechanical core of the framework.

The design goal is **legibility**. Not trust in any actor, but a system where every decision can be traced to an explicit, public specification that anyone can read, and where deviation from that specification requires explicit, public justification.

## The instruction set

### What it is

A public, versioned, amendable document that specifies what the coordinator should optimize for, what constraints it must respect, and how it should handle contested cases. Think of it as a constitution that is also directly executable — the same text that humans debate is the input the coordinator operates on.

### Structure

The instruction set has three tiers:

**Tier 1 — Constraints.** The planetary hard limits from Layer 1. Binding, non-negotiable, amendable only through the heaviest deliberation process. The coordinator treats violations of Tier 1 as impossible — it will refuse any proposal that would cross a Tier 1 line.

**Tier 2 — Objectives.** What the coordinator is trying to achieve within the constraints. Human flourishing, equity, intergenerational fairness, resilience, ecological regeneration. These are weighted, tradeable against each other, and amendable through normal deliberation.

**Tier 3 — Mechanics.** Specific rules, thresholds, and procedures. How externality prices are calculated. How the planetary dividend is distributed. How size thresholds for firm obligations are set. Amendable through lighter process; these are expected to evolve frequently.

### Versioning and amendment

The instruction set lives in a public, version-controlled system (git or equivalent). Every change is tracked, attributed, and justified. The amendment process follows a defined RFC (Request for Comments) procedure — see [CONTRIBUTING.md](CONTRIBUTING.md).

Amendments to Tier 1 require the heaviest process: extended deliberation, multiple rounds of citizen assembly review, scientific body input, and broad ratification. This is deliberately slow because the constraints are load-bearing.

Amendments to Tier 2 and Tier 3 use lighter processes calibrated to their stakes.

### Interpretation

Every instruction set will have ambiguities. Every ambiguity will be exploited by actors who want different outcomes than the text specifies. This is not a failure mode to be eliminated; it is an inherent feature of textual specification that must be managed.

The framework handles this through an **interpretation layer** — a body (part human, part AI-assisted, fully transparent) that resolves contested clauses and whose interpretations become part of the operative instruction set. This is structurally similar to common-law courts: the text plus the accumulated body of interpretations is what actually governs.

The interpretation layer's decisions are themselves public, reasoned, and subject to challenge. It does not produce final authority — it produces *reviewable* authority.

## The coordinator stack

### What it is

Not a single AI system. A federated set of AI systems, operating in parallel, cross-auditing each other's proposals, deployed on open infrastructure.

### Why federated

A single coordinator is a single point of failure, capture, and control. A federated stack is robust against capture of any individual node. It also allows diversity: different approaches, different model architectures, different training methodologies, with the instruction set as the shared ground truth that all must respect.

National or regional bodies may contribute models. Scientific institutions may contribute models. Open-source communities may contribute models. All submitted models run against the same instruction set; their proposals are compared; consensus proposals proceed, dissenting proposals become part of the debate.

### Stack requirements

For a model to be part of the coordinator stack, it must satisfy:

- **Open weights.** The model parameters are public.
- **Open training data provenance.** What was it trained on, and how.
- **Open inference logs.** Every decision, every proposal, every input and output is logged publicly (with privacy-preserving transformations where necessary for individual-level data).
- **Open evaluation.** Benchmarks, red-team results, alignment audits are all public.
- **Hardware audit trail.** The compute substrate is identified and auditable; decisions cannot be made on secret hardware whose provenance is unknown.

This is a very high bar. Current frontier AI systems meet none of these requirements. Meeting them requires treating compute, models, and AI infrastructure as public utilities rather than private assets. This is itself a major structural change and is discussed in [FAILURE_MODES.md](FAILURE_MODES.md) as the "stack capture" problem — currently the framework's hardest unsolved problem.

### Cross-auditing

Every significant proposal is checked by multiple models in the stack. Disagreements are logged and flagged for human review. The stack cannot reach consensus through collusion because the models come from different contributors and are run on different infrastructure.

This is similar in spirit to how scientific peer review functions — not by producing perfect results, but by requiring claims to survive independent scrutiny.

## Default-accept with override

### The mechanic

The coordinator produces proposals based on the instruction set. A designated human body then either:

- **Accepts** the proposal, which is the default. No action required. Proposal proceeds.
- **Overrides** the proposal, which requires an affirmative decision, a public justification, and a record.

The asymmetry is deliberate. Under current systems, beneficial actions (pricing externalities, redistributing surplus, enforcing commons limits) require mobilizing majorities against entrenched resistance, while inaction is the default and favors the status quo. Under this framework, the default is the coordinator's recommendation based on the transparent instruction set, and *deviation from it* is what must be justified.

This inverts the burden of proof in the direction the current system most needs it inverted.

### Who can override

Override authority lives in bodies structured to be difficult to capture:

- **Sortition-based citizen assemblies.** Randomly selected from the affected population, with time, information, and deliberative conditions sufficient for real decision-making. This model has real precedent — Ireland's citizen assembly on abortion, French climate convention, Belgian permanent citizen councils.
- **Multiple concurring bodies.** Major overrides may require agreement from multiple independent bodies — a citizen assembly, a scientific panel, an elder or tradition-holder council for affected communities.
- **Rotation.** No individual serves on an override body for more than a defined term, reducing capture risk.
- **Transparency of deliberation.** Discussions are public unless deliberately protected for specific reasons (e.g., safety of participants).

The exact structure requires deliberation (see [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md)), but the principle is clear: override authority does not live in elected politicians operating through existing party structures, because those structures have demonstrably been captured. It lives in harder-to-capture bodies with explicitly different selection mechanisms.

### What override actually does

An override does not reprogram the coordinator. It blocks a specific proposal and triggers a process. If the override reveals a flaw in the instruction set, that flaw is debated and potentially amended. If it reveals a failure in the coordinator's reasoning, that failure is analyzed and the coordinator is updated. If it reveals a contested value judgment where reasonable humans disagree, the decision goes to broader deliberation.

The override is the system's error-correction mechanism. It is expected to be used.

### What prevents override abuse

The same structural features that make override bodies hard to capture also make capricious override costly: overrides are public, justified, recorded, and reviewable. An override body that repeatedly blocks sound proposals for bad reasons becomes visible and loses legitimacy. A pattern of self-serving overrides is a signal that the override body itself needs restructuring.

## The sunset clause

### The principle

The coordinator's authority is time-limited and domain-limited. It exists to hold planetary commons stable and manage civilization-scale coordination during a transition period — roughly, the decades during which epistemic, social, and cognitive conditions heal sufficiently for humans to resume direct self-governance at planetary scale.

This is not a promise that the coordinator will be shut off in 30 years. It is a structural commitment: authority is justified by specific current conditions, and as those conditions change, authority is transferred back to human institutions.

### How sunset works mechanically

**Scope can shrink.** As specific problems become solvable at lower layers — through improved institutions, healed social fabric, local capability — the coordinator's remit shrinks to exclude them. The instruction set specifies triggers for this shrinkage.

**Authority can degrade to advisory.** The coordinator may continue operating but with reduced authority — from proposing-with-default-accept to proposing-with-default-review, to purely advisory. This is a softer transition than binary on/off.

**Specific mandates sunset.** Individual clauses in the instruction set can have expiration dates, with renewal requiring affirmative deliberation rather than defaulting to continuation.

### Why sunset matters

Because every transitional authority in history has attempted to become permanent. Lenin's "temporary" revolutionary dictatorship. Military juntas. Emergency powers extended indefinitely. The temptation for any governing body to prolong its own authority is universal and must be structurally countered, not trusted against.

Built-in sunset with affirmative renewal, combined with the instruction set's transparency, reduces (though does not eliminate) this risk. Everyone can see whether the coordinator is still needed for a given function. Everyone can argue against renewal. The default is contraction, not expansion.

## The interpretation layer in detail

Because this is the piece most likely to be misunderstood as a loophole.

### What it does

When an instruction set clause is contested in application — when two reasonable readings produce different outcomes, when a novel situation isn't clearly covered, when an edge case exposes ambiguity — the interpretation layer produces a binding interpretation that becomes part of the operative specification.

Over time, this produces an accreting body of interpretation, similar to common-law case law. The *text plus interpretations* is what actually governs, not the text alone.

### Who interprets

Human bodies with AI assistance, structured similarly to override bodies: sortition-selected, rotating, transparent, with public reasoning. Not judges in the existing sense, because existing judiciaries have been captured in most jurisdictions. New institutions, built from scratch.

AI assistance here is specifically useful because the interpretation layer has to handle large volumes of contested cases while maintaining consistency. AI can surface prior interpretations, flag inconsistencies, and draft reasoning, but the binding decision is human.

### Why not just fix the text

Because text cannot anticipate every application. This is true of every legal and constitutional tradition that has ever existed. The choice is between acknowledging interpretation as a first-class process and trying to hide it. Hiding it means interpretation happens anyway, opaquely, by whoever has informal power. Acknowledging it means interpretation is public, reasoned, and contestable.

The instruction set can be improved in response to patterns of interpretation. If a clause is chronically producing disputes, that's a signal to rewrite the clause. The interpretation layer and the amendment process feed each other.

## Failure modes

This is not a perfect system. Several failure modes are known and discussed in [FAILURE_MODES.md](FAILURE_MODES.md):

- **Stack capture.** Whoever controls the compute, weights, and deployment pipeline controls the system regardless of what the instruction set says. Partial solutions exist; no complete solution is currently known.
- **Prompt gaming.** Every ambiguity in the instruction set will be exploited. The interpretation layer helps but does not eliminate this.
- **Override capture.** Override bodies can themselves be captured over time. Rotation, sortition, and multiple-body concurrence help but don't eliminate this.
- **Legitimacy.** Nations and populations may simply reject the system's authority, particularly in its early phases.
- **Scope creep.** Despite the sunset clause, governance bodies tend to expand their remit over time.

These are named honestly rather than solved. The framework is a starting point for addressing them, not a claim to have.
