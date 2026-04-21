# Vision

## The three-layer structure

The framework organizes all economic and governance activity into three layers, stacked hierarchically. Each layer has a distinct function, a distinct mechanism, and a distinct relationship to the layers above and below it.

```
┌─────────────────────────────────────────────────────────────┐
│ LAYER 1 — PLANETARY CONSTRAINTS                             │
│ Hard limits, constitutional, scientifically determined.     │
│ No layer below may violate.                                 │
├─────────────────────────────────────────────────────────────┤
│ LAYER 2 — COORDINATION                                      │
│ Transparent AI systems operating on public instruction set. │
│ Handles planetary commons, logistics at scale, redistribution. │
├─────────────────────────────────────────────────────────────┤
│ LAYER 3 — FREE MIDDLE                                       │
│ Local economies, culture, enterprise, daily life.           │
│ Markets operate here, bounded by the layers above.          │
└─────────────────────────────────────────────────────────────┘
```

The fundamental design principle is **subsidiarity**: decisions are made at the lowest layer capable of making them. The coordinator handles only what cannot be handled at the free-middle layer because of commons dynamics, cross-border externalities, or scale. Everything else is explicitly and constitutionally left free.

This is not a gradient. The layers have sharp boundaries, and those boundaries are themselves constitutional.

## Layer 1 — Planetary Constraints

### What it is

A small, explicit set of hard limits that no economic or political activity may violate. These are constitutional in the strongest sense: they are the frame within which everything else happens.

### Current candidate constraints

The exact set requires deliberation (see [OPEN_QUESTIONS.md](OPEN_QUESTIONS.md)), but the working list:

**Ecological:**
- Carbon budget consistent with maintained climate stability
- Biodiversity floor (species loss rate within background rate)
- Freshwater extraction within renewable replenishment
- Topsoil preservation and regeneration
- Ocean acidification and fisheries sustainability
- Nitrogen and phosphorus cycle limits

**Human:**
- Livelihood floor for every human: food, shelter, healthcare, education, basic dignity
- Freedom from arbitrary violence, imprisonment, or coercion
- Freedom of conscience, expression, and association within non-harm limits
- Right to leave (no citizen of any jurisdiction may be forced to remain)

These map substantially onto Kate Raworth's *Doughnut Economics* framework. The framework's novelty is in treating them as **hard constraints on every layer below**, not as aspirational goals to be balanced against economic growth.

### Who sets them

Scientific bodies with transparent methodology, not political bodies. The IPCC is the nearest existing analog — an international scientific consensus body that produces assessments trusted across ideological lines because its methodology is open and its authors are diverse. The framework proposes a broader version: an IPCC-equivalent for biodiversity (drawing on IPBES), for freshwater, for ocean systems, for livelihood indicators, and so on.

Scientific determination does not mean scientific infallibility. The bodies publish their methodology, their uncertainty ranges, and their dissenting minority views. The constraints are revised as evidence evolves. The point is not that scientists have magic authority; the point is that the methodology is *inspectable* in a way political negotiation is not.

### Why they are constitutional

Because the fundamental failure of the current system is that these constraints are negotiable. Carbon budgets are routinely violated when short-term political or economic interests require it. Livelihood floors are perpetually "unaffordable." Biodiversity is sacrificed piecemeal.

Making them constitutional means Layer 2 and Layer 3 activity that would violate them is not permitted, full stop. A firm cannot grow by depleting a commons. A nation cannot develop by exceeding its carbon share. A coordinator cannot optimize its way past a biodiversity floor. The constraints are inviolable from below.

## Layer 2 — Coordination

### What it is

A federated set of AI systems that handle the allocation, logistics, and coordination functions that markets handle badly at planetary scale. The coordinator operates on a **public, versioned, amendable instruction set** — analogous to a constitution, but written, updatable, and directly machine-readable.

### What it coordinates

Specifically and only:

- **Planetary commons management.** Allocating carbon budget across sectors and regions. Managing freshwater systems that cross borders. Biodiversity preservation. Ocean systems. Atmospheric systems.
- **Critical supply chains.** Food security, essential medicines, energy grids, rare earths, semiconductor capacity. The things civilization breaks without.
- **Pandemic and catastrophic risk.** Surveillance, response coordination, resource pre-positioning.
- **Externality pricing and redistribution.** Setting Pigouvian prices on unpriced commons costs. Collecting revenue into the planetary fund. Distributing the planetary dividend.
- **Cross-border financial flows.** Preventing tax havens, capital flight, and the erosion of national fiscal capacity by mobile capital. Because the coordinator is planetary, there is no "elsewhere" for capital to flee to.
- **AI governance itself.** Frontier model training, deployment, and oversight.
- **Planetary public goods.** Open scientific research infrastructure, coordination protocols, shared data commons.

### What it does not coordinate

Explicitly and constitutionally:

- Local economies
- Cultural production, art, media, religion
- Small and medium enterprise (below thresholds defined in [ECONOMICS.md](ECONOMICS.md))
- Personal life choices: what you eat, wear, believe, create, love
- Local governance: cities, regions, community institutions
- Education content and curriculum (infrastructure yes, curriculum no)
- Family and intimate life
- Most of what people actually experience as their daily lives

This is not a list of things the coordinator *currently* doesn't touch but might later. This is a constitutional scope limit. The coordinator's authority stops at the boundary of what can be handled at lower layers, and the boundary is enforced from above.

### How it operates

See [GOVERNANCE.md](GOVERNANCE.md) for mechanics. Briefly:

- The coordinator **proposes** allocations and actions based on the public instruction set.
- Human bodies **ratify by default**; override requires explicit, public justification.
- Multiple independent AI systems cross-audit each other.
- The entire stack (model weights, training data, inference logs, hardware provenance) is open and auditable.
- The instruction set is a living document, amendable through a defined deliberation process.

### Why AI

The coordination function has to live somewhere. Historically it has lived in markets (which fail at this scale), central committees (which concentrate power dangerously), or technocratic elites (which become the new oligarchy).

An AI coordinator operating on a public instruction set is different in kind: its objective function is **inspectable**. You don't have to trust any human or institution; you read the document. Disagreement about outcomes becomes disagreement about the document, which is a tractable argument conducted in public.

This does not require believing AI is wise, aligned, or benevolent. It requires believing AI is *legible* — that its operation, unlike the operation of opaque human institutions, can be traced to an explicit specification. That legibility is the whole point.

### Why time-limited

The coordinator's authority is explicitly bounded in time. It exists to hold the planetary commons stable during the transition period — the decades during which the social fabric rebuilds, cognitive and epistemic conditions improve, and human institutions regain the functional capacity to resume direct self-governance.

This is the **regency model**. A regent rules on behalf of a sovereign who is not yet fit to rule, with explicit provisions for handback. The coordinator is not the end state. The end state is a population capable of democratic self-governance across planetary scales — which does not currently exist and cannot be assumed to emerge without deliberate work.

See [GOVERNANCE.md](GOVERNANCE.md) for the sunset mechanics.

## Layer 3 — Free Middle

### What it is

Everything the coordinator does not handle. The economic and social life people actually live.

### What happens here

- Local and regional economies operating through markets, cooperatives, mutual aid, barter, or whatever local actors choose
- Small and medium enterprise, competing, innovating, failing, succeeding
- Cultural production: art, music, literature, film, fashion, cuisine, sport
- Religion and spiritual practice
- Education in its substantive content (schools, universities, apprenticeships, self-directed learning)
- Science as practiced by working scientists (the coordinator funds infrastructure; researchers do research)
- Community institutions, civic organizations, neighborhood life
- Family, friendship, intimacy, care
- Experimentation — political, technological, social, aesthetic

### Why a free middle at all

Three reasons.

**First, markets genuinely work at this scale.** Coordinating diverse preferences at small scale, rewarding local knowledge, handling variety — these are things prices do well. The critique of markets in this framework is specifically about their failure at planetary scale in the presence of unpriced externalities, not a general critique.

**Second, humans need autonomy.** A framework that optimizes every aspect of life for some global objective function, however well-intentioned, is the utopian horror scenario. Leaving a large domain of life uncoordinated — where people can choose badly, fail, experiment, disagree, build weird things — is not a concession to market ideology. It is a positive commitment to human freedom.

**Third, resilience comes from variety.** A monoculture fails catastrophically when the environment shifts. A diverse ecosystem of local and regional economies, cultural forms, and institutional experiments produces the variation from which adaptation is drawn. The free middle is where the next good ideas come from.

### What's different from current capitalism in the middle layer

Markets here are *bounded* in ways they aren't currently:

- They pay the externality prices set by Layer 2. Carbon is priced. Attention extraction is priced. Labor displacement externalities are priced.
- They operate with a **livelihood floor** already in place for all participants, so "no" is a real option for workers and consumers in a way it currently isn't. This alone transforms labor-market dynamics.
- Above certain size thresholds, firms take on public-interest obligations proportional to their scale (see [ECONOMICS.md](ECONOMICS.md)).
- Essential goods (food, shelter, healthcare, education, energy up to a threshold) are substantially decommodified via Layer 2 provision, leaving Layer 3 markets to handle above-baseline and discretionary activity.

This is a market economy, but one that cannot eat its own preconditions.

## The relationship between layers

The layers do not interact symmetrically.

**Downward:** Layer 1 constrains Layer 2 absolutely. Layer 2 constrains Layer 3 through pricing, provisioning, and size-threshold obligations — but does not directly manage Layer 3 activity.

**Upward:** Layer 3 generates signals (production, preferences, needs, failures) that feed into Layer 2's coordination. Layer 2's outputs and the effectiveness of Layer 1's constraints feed back into the deliberation process that revises both.

**Lateral within Layer 3:** Normal market, community, and political dynamics. Subsidiarity all the way down within this layer — regions and localities handle their own affairs.

## The meme question

A framework needs a name and a compressed form that travels. The working repo name is `planetary-coordination-framework`. The memeable wrapper is an [open question](OPEN_QUESTIONS.md) — candidates include:

- *Commons Capitalism* (markets work, but touching a commons costs you)
- *Open Civilization*
- *The Readable Constitution*
- *Regency Economics*
- *Planet-first, People-second, Profit-third* (ordered because any other order destroys the first two)
- *Hard Floor, Soft Ceiling, Free Middle*

Naming by committee on day one is usually bad. The name should emerge from the community that forms around the project. This document uses the descriptive label.

## What this vision asks of you

If you're reading this to decide whether to contribute, here is what the framework assumes you're willing to grant:

- That abundance is technically possible at planetary scale with current and near-term technology, and that scarcity is substantially a coordination problem, not a resource problem.
- That the free-market framework, whatever its past merits, is no longer self-correcting and is producing outcomes opposite to its theorized ones.
- That structural intervention is required and cannot be waited for — the crisis is coming whether or not we're ready.
- That AI, operating transparently on a public instruction set, is a more legitimate coordinator than any human elite — not because it's wiser, but because it's inspectable.
- That the goal is not permanent AI governance but a bounded regency during a transition period, with handback to a healed human polity as the end state.

If you can grant these, the rest is engineering and deliberation. The framework is open for both.
