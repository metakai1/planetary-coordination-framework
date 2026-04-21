# Failure Modes

Every framework has failure modes. Naming them explicitly is what separates a serious proposal from a manifesto. This document is deliberately honest about what could break this framework, including the problems we don't currently know how to solve.

## Technical failure modes

### 1. Stack capture (unsolved)

**The problem:** Whoever controls the model weights, the compute, the training data, and the deployment infrastructure controls the coordinator regardless of what the instruction set says. They can fine-tune the model, filter outputs, adjust the system prompt, or simply ignore unfavorable inferences. The "transparent prompt" is only as transparent as the stack underneath it.

**Why it's unsolved:** Current frontier AI infrastructure is concentrated in a handful of organizations (OpenAI, Anthropic, Google, Meta, DeepSeek, major Chinese AI labs). Compute is concentrated in an even smaller set of chip manufacturers and cloud providers. Genuinely open, planetary-scale AI infrastructure does not exist.

**Partial mitigations:**
- Federated stack with multiple independently controlled models, making full capture require compromising multiple organizations simultaneously
- Open weights, data, and inference logs as prerequisites for coordinator participation
- Hardware audit trails and independent verification
- Public red-teaming of the stack
- Treating AI infrastructure for the coordinator as a public utility analogous to water or electricity

**What would be required for full solution:** A CERN-scale international public AI project, or equivalent, producing genuinely open frontier-capable models on auditable infrastructure. This is a multi-decade, trillion-dollar undertaking. It's probably necessary. It's probably not happening on the timeline the crisis demands.

**Honest assessment:** This is the framework's single hardest unsolved problem. Without addressing it, the coordinator is theater.

### 2. Prompt gaming

**The problem:** Every ambiguity in the instruction set will be exploited by actors who want different outcomes than the text specifies. "Maximize human flourishing" — whose definition? "Within planetary boundaries" — measured how? Every word is a potential battleground.

**Partial mitigations:**
- The interpretation layer handles contested cases, producing binding interpretations that accrete over time (similar to common-law case law)
- Amendment process allows the text to be clarified in response to gaming patterns
- Multi-model cross-auditing catches cases where different models interpret clauses differently — the disagreement is itself the flag

**Residual problem:** Interpretation bodies can themselves be captured. Common-law constitutional interpretation has produced both civil-rights expansion and Citizens United. The interpretation layer is as good as its human composition.

### 3. Instruction set incompleteness

**The problem:** No text can anticipate every situation. The instruction set will always be incomplete relative to the reality it tries to govern. Edge cases, novel situations, and rapid technological or ecological change all produce moments where the text doesn't clearly apply.

**Mitigations:**
- The interpretation layer handles novel cases
- The amendment process allows the text to extend
- The coordinator has permission to refuse action rather than act under unclear authority

**Residual problem:** "Refuse to act" is itself a decision with consequences. A coordinator that refuses to act during a crisis because the instruction set doesn't clearly cover it is a coordinator that has abdicated responsibility at the moment most needed.

### 4. Model alignment failure

**The problem:** AI alignment — ensuring a model's behavior matches its specified objectives — is not a solved problem. Current frontier models exhibit misalignment behaviors that are sometimes subtle, sometimes dramatic. A coordinator running on misaligned models produces decisions that don't actually track the instruction set.

**Mitigations:**
- Multi-model cross-auditing catches alignment divergences between models
- Extensive red-teaming
- Conservative action thresholds: the coordinator acts only when multiple models agree
- Reversibility: actions that can be undone are preferred; irreversible actions require higher confidence

**Residual problem:** This is a real area of AI safety research, not a solved problem. The framework depends on alignment research progress that has not fully occurred yet.

## Political failure modes

### 5. Legitimacy failure

**The problem:** Populations and states may simply reject the coordinator's authority. The framework is adopted in crisis, but legitimacy requires ongoing consent, and that consent is fragile.

**Partial mitigations:**
- The coordinator's remit is narrow and domain-specific, reducing surface area for legitimacy challenges
- Transparency means legitimacy claims can be grounded in specific instruction-set texts and specific outcomes
- Override authority gives affected populations a real channel for dissent
- Sunset clauses mean rejection can be expressed as "time to hand back" rather than "destroy the system"

**Residual problem:** Some populations and states will reject the framework regardless. The framework cannot achieve universal legitimacy and should not try. The question is whether it achieves enough legitimacy in enough places to function.

### 6. Adoption failure

**The problem:** The crisis comes, and either the framework isn't ready, or it's available but isn't picked up, or it's picked up and mis-implemented. All three have historical precedent.

**Mitigations:** See [TRANSITION.md](TRANSITION.md) for the strategy. In brief: prepare now, pilot components in advance, build intellectual and institutional infrastructure, make the framework real before it's needed.

**Residual problem:** Even Friedman's well-prepared neoliberal framework produced uneven adoption with significant regional and domain variation. The framework should expect similar — partial adoption, long implementation, significant local modification. Its design should be robust to this.

### 7. Co-optation

**The problem:** Powerful actors adopt framework language while gutting substance. Carbon pricing that is too low to bite. "Citizen assemblies" that are advisory only. "Open" AI that has key components proprietary. "Wealth taxes" with loopholes that make them symbolic. This has happened to every emancipatory framework and will happen to this one.

**Mitigations:**
- Clear, specific commitments that substance requires
- An evaluation framework for distinguishing genuine from cosmetic adoption
- A community willing to name co-optation publicly
- The framework's commitments to openness and specificity make co-optation easier to detect than in more vague frameworks

**Residual problem:** The line between principled compromise and co-optation is contested. People of good faith will disagree about whether a given implementation is an acceptable halfway step or a dangerous dilution. This cannot be fully resolved in advance.

### 8. Geopolitical fragmentation

**The problem:** Great-power competition may produce incompatible versions of the framework in different geopolitical blocs, or active opposition to planetary coordination from powers that see it as a threat to their interests. US-China dynamics are particularly relevant.

**Mitigations:**
- The framework can accommodate multiple versions at the regional level while maintaining core planetary commons coordination
- The commons problems (climate, pandemics, AI risk) genuinely require coordination, creating practical pressure toward cooperation
- Starting with narrowly-scoped coordination on clear mutual-benefit domains

**Residual problem:** Nuclear-scale geopolitical conflict could make any planetary framework infeasible for a generation or longer. The framework cannot solve geopolitics; it can only be ready when geopolitics allows.

### 9. Authoritarian adoption

**The problem:** Authoritarian regimes may adopt framework components that serve their interests (centralized AI coordination, surveillance for "commons protection") without the accompanying governance commitments (override bodies, open stack, sunset clauses). The result would be a framework-branded authoritarianism.

**Mitigations:**
- The framework's identity-defining commitments (open stack, override, sunset, Layer 3 freedom) are explicitly the deal-breakers; violating them means the resulting system is not framework-consistent
- Community willingness to publicly distinguish real adoption from authoritarian mimicry
- Global recognition that certain components are load-bearing — a "planetary dividend" without open governance is not the framework

**Residual problem:** Authoritarians can still adopt the rhetoric. Public understanding of the distinction is ongoing work.

## Sociological failure modes

### 10. Public incomprehension

**The problem:** The framework is complex. Most people will not read it. Most people will not engage with the instruction set. If "humanity can at least read the prompts" is the floor, and the floor isn't met, the legitimacy story collapses.

**Mitigations:**
- Tiered communication: one-line description, one-page summary, full framework, technical specifications
- Intermediary institutions (journalism, civic education, unions, religious communities) that translate and advocate
- Plain-language versions of the instruction set itself
- The expectation is not universal comprehension but sufficient expert and engaged-citizen oversight — similar to how most people don't read the Federal Reserve's minutes but enough people do

**Residual problem:** If public attention is successfully captured by other dynamics (which is happening now), the framework's legitimacy-through-transparency story is in trouble regardless of how good the documents are.

### 11. Deliberation quality

**The problem:** Citizen assemblies and override bodies require real deliberative conditions — information, time, freedom from coercion, psychological safety. Real-world implementations will be compromised versions of the ideal.

**Mitigations:**
- Learn from existing high-quality deliberations (Irish citizen assembly, Belgian permanent council, French climate convention all achieved real deliberative quality)
- Explicit design requirements for deliberative conditions
- Evaluation of outcomes relative to deliberative quality

**Residual problem:** Deliberation is genuinely hard and requires resources that may be chronically underfunded relative to need.

### 12. Cognitive recovery failure

**The problem:** The framework's legitimacy depends on an implicit expectation that during the regency period, cognitive, social, and epistemic conditions improve — that the demos heals. If they don't, the sunset never arrives, and the regency becomes permanent.

**Mitigations:**
- Explicit commitment to investments in cognitive and social recovery: environmental cleanup, mental health, community infrastructure, education, attention-environment reform
- Measurable indicators of demos health that track toward the sunset
- Explicit refusal to accept "the people aren't ready" as an indefinite excuse

**Residual problem:** The same dynamics that produced cognitive capture may continue under the coordinator's watch, or new forms may emerge. Cognitive health at scale is not a solved problem. The framework depends on progress it doesn't know how to engineer.

## Structural failure modes

### 13. Scope creep

**The problem:** Every governing body in history has tended to expand its remit. "The coordinator handles only planetary commons" is a commitment that will be tested repeatedly. Over time, the pressure to let it handle more will be substantial.

**Mitigations:**
- Constitutional scope limits enforced by override bodies
- Sunset clauses on specific mandates requiring affirmative renewal
- A community vigilant about scope expansion

**Residual problem:** Each individual expansion will be locally justifiable. "We need the coordinator to handle X because local institutions have failed on X" is a seductive argument that must be resisted even when partly true.

### 14. Override underuse

**The problem:** Default-accept-with-override fails if no one overrides when they should. A captured or passive override body produces coordinator authority that is technically checked but practically unchecked.

**Mitigations:**
- Override body structure designed for active exercise (sortition, rotation, clear authority)
- Adversarial red-teaming of coordinator proposals to ensure options for override are visible
- Community pressure on override bodies that appear passive

**Residual problem:** Institutional passivity is a general problem in governance. The framework mitigates it but does not solve it.

### 15. Override overuse

**The problem:** Conversely, override bodies that block everything produce paralysis, which privileges the status quo over any proposed change.

**Mitigations:**
- Clear standards for override justification
- Transparency of override patterns, so chronically-overriding bodies become visible
- Structural design that makes override costly in specific ways (time, process, public justification)

### 16. Interpretation drift

**The problem:** The interpretation layer can accrete interpretations that collectively move far from the text, producing a governed reality that no one voted for. This has happened to every major constitutional tradition.

**Mitigations:**
- Amendment process that can clarify text in response to interpretation drift
- Transparency of accumulated interpretations
- Periodic review of whether the operative specification (text + interpretations) still reflects intent

**Residual problem:** Drift is not always bad — sometimes it's how a living document stays current — but distinguishing beneficial evolution from drift is contested.

## Existential failure modes

### 17. The framework is simply wrong

**The problem:** The diagnosis could be mistaken. The current system may be more self-correcting than the framework assumes, or alternative frameworks could be better, or the framework's structure may produce worse outcomes than what it replaces.

**Mitigations:**
- Honest engagement with critique
- Willingness to abandon specific components that prove wrong
- Epistemic humility in presentation
- Multiple versions of the framework coexisting, so failure of one doesn't mean failure of all

**Residual problem:** The framework authors' confidence does not determine correctness. The framework could be a dead end that absorbs reformist energy for a generation while producing nothing. This risk is real.

### 18. Bad crisis timing

**The problem:** The framework may be ready either too early (before crisis, when no adoption is possible) or too late (after crisis, when an incompatible alternative has already filled the vacuum).

**Mitigations:**
- Continuous development and presence rather than one-time release
- Multiple entry points and adoption pathways so the framework remains viable across different crisis trajectories
- Community willingness to iterate for decades

### 19. Active suppression

**The problem:** Powerful actors with interests opposed to the framework may actively suppress it — through academic marginalization, media hostility, legal attack, or worse.

**Mitigations:**
- Distributed authorship and organizational base
- Open license so suppression in one jurisdiction doesn't end the framework
- Broad coalition across political identities to make pure ideological attack less effective

**Residual problem:** Suppression has worked in the past and could work here. This is a real risk and cannot be fully mitigated.

## Meta-failure modes

### 20. This document is incomplete

**The problem:** This list itself is incomplete. Additional failure modes exist that we haven't identified. Some of them may be load-bearing.

**Mitigation:** Contributors adding failure modes to this document are performing the most valuable work. Skeptics are welcome. The worst outcome is false confidence; the best outcome is a framework strengthened by hard engagement with its weaknesses.

---

The framework is a proposal, not a proof. These failure modes are the real terrain on which it will succeed or fail. Taking them seriously is the only way to build something that actually survives contact with reality.
