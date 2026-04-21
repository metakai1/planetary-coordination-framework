# Typography

## Philosophy

The framework is speaking from the long tradition of serious civic documents, not from the feed. Typography reinforces this register at the pre-linguistic level: the shapes of the letters tell the viewer what kind of thing they're reading before the words are processed.

The default tech-manifesto stack (Inter/Manrope/grotesque everywhere) codes as *startup pitch*. We deliberately diverge.

## Typefaces

### Headlines — Instrument Serif

```
font-family: 'Instrument Serif', 'Cormorant Garamond', Georgia, serif;
```

**Why serif:** serifs signal *this is meant to be read and remembered, not scrolled past*. Serifs are the typography of books, constitutions, scholarly journals, and serious publications. Using a serif for the headline is the single strongest move to distinguish the framework from every other online manifesto.

**Why Instrument Serif specifically:** it has a quiet gravitas — neither the formal stiffness of Garamond nor the modern cleanliness of Fraunces. The italic has real drama; perfect for the emphasis word in compositions that use it. It was designed in 2022 by Rodrigo Fuenzalida and Jonny Pinhorn, released open-source via Google Fonts.

**Weights used:** Regular (400) for most headlines. Italic (400) for emphasis words. No bold — the serif's presence is sufficient.

### Body and subordinate text — Inter

```
font-family: 'Inter', -apple-system, sans-serif;
```

**Why Inter:** workhorse sans-serif with excellent screen legibility at small sizes. It's also ubiquitous, which is a feature here — subordinate text should disappear into readability, not call attention to itself. The serif headline is doing the work; the body text supports.

**Weights used:** 400 (regular) for body, 500 (medium) for emphasis, 600 (semibold) for subheads. 700 is generally too heavy for ivory-on-near-black.

### Metadata and code — JetBrains Mono

```
font-family: 'JetBrains Mono', 'IBM Plex Mono', monospace;
```

**Why monospace for metadata:** the engineering texture. The framework is positioned as something *built*, not *believed* — and monospace text signals engineering documentation, API reference, source. It also creates visual contrast with the serif and sans, producing the triadic typography system that gives compositions their technical-document feel.

**Used for:** URLs, corner labels, timestamps, version strings, small captions, technical metadata.

## Typographic scale

For 1080×1080 card format:

```
--size-hero:       140px / 0.9 line-height    /* the single largest element */
--size-headline:   88px / 0.95                /* standard headline */
--size-subhead:    32px / 1.3                 /* subline under headline */
--size-body:       20px / 1.5                 /* paragraph text */
--size-label:      13px / 1.4                 /* corner labels, metadata */
--size-caption:    11px / 1.4                 /* smallest legible */
```

For other formats, scale proportionally. The ratios matter more than the absolute sizes.

## Emphasis patterns

### The italic emphasis word

One word per headline may be italicized in verdigris, drawing the eye to the load-bearing concept. This is borrowed from the Resonant Blue signature move but adapted — use it sparingly, one per composition, never more.

Example: *Demand is a **commons.*** — with "commons" as the italic-verdigris emphasis.

### The letterspacing treatment

Small metadata labels use aggressive letterspacing for the *technical-document* register:

```
text-transform: uppercase;
letter-spacing: 0.25em;  /* to 0.35em for the smallest sizes */
font-weight: 500;
```

This is what makes corner labels read as "specification" rather than "headline."

## Rules

1. **Never use bold on headlines.** The serif's natural weight is sufficient. Bold serifs read as aggressive or desperate.
2. **Never use all-caps on headlines.** Only on small metadata labels. All-caps serif headlines read as Roman monuments or wedding invitations, neither of which is the register.
3. **Never use more than three typefaces in one composition.** The triadic system (Instrument Serif / Inter / JetBrains Mono) is the ceiling, not the target — many compositions use only two.
4. **Never use emoji, icons, or decorative symbols.** The composition's gravity comes from the typography and the palette. Adding emoji cheapens it immediately.
5. **Always let one element dominate.** Headline size should be at least 3× the next-largest text. Hierarchy is load-bearing.

## Font loading

Google Fonts for all three:

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
```

All three are open-source, free to use, and self-hostable if needed for reproduction without external dependencies.
