# Colors

The Planetary Coordination Framework brand palette.

## Philosophy

The palette is chosen to evade three visual traps that kill serious ideas:

1. **ESG / corporate-sustainability green** — the flattened-leaf color used by every oil company's greenwashing department
2. **Matrix / hacker green** — the saturated cyber-aesthetic that reads as juvenile
3. **Silicon Valley blue-on-white** — the startup register that codes as "pitch deck"

Instead: **verdigris on near-black**, with warm ivory for primary text and ochre used sparingly as counterpoint. The reference is not startup, not nonprofit, not protest. The reference is the **civic document, the restored library, the scientific atlas, the weathered monument.** Things that have earned their presence through time.

## Core palette

### Ground

```
--ground-deep:     #0d1412    /* near-black with faint cool-green undertone */
--ground-shadow:   #151d1a    /* one step up, for subtle layering */
```

Not pure black. Pure black on screen reads as cheap or OLED-optimized; a slightly tinted near-black reads as deliberately chosen.

### Signature — Verdigris

```
--verdigris:       #5a9b8e    /* primary signature, the earned attention color */
--verdigris-deep:  #3d6d64    /* for shadows, hover states, secondary emphasis */
--verdigris-glow:  #6fb8a8    /* for glow effects, highlights */
```

The color of copper that has weathered for a century. The Statue of Liberty. Old cathedral roofs. Public monuments that have outlasted the societies that built them. The color carries an argument: **things endure, things transform, meaning accrues through time**. Perfect for a framework about commons, stewardship, and inheritance.

Use verdigris as the attention color — the one element per composition that the eye is meant to land on.

### Text — Ivory

```
--ivory:           #e8e2d4    /* primary text, warm off-white */
--ivory-dim:       #b8b2a5    /* secondary text */
--gray-cool:       #7a8280    /* tertiary, metadata */
--gray-dim:        #4a524f    /* almost invisible, for texture */
```

Pure white on dark backgrounds reads as *tech product*. Warm ivory reads as *document*, *parchment*, *considered object*. This is the single most important palette decision after the ground color.

### Counterpoint — Ochre

```
--ochre:           #c9965a    /* warm accent, use sparingly */
--ochre-deep:      #8a6640    /* for darker warm notes */
```

The aged-brass counterpoint. Keeps the composition from going cold-and-sterile. **Rule: one ochre element per composition, maximum.** The rarity is what gives it power.

## Supporting utility colors

```
--line-subtle:     rgba(232, 226, 212, 0.08)   /* ivory at 8% for hairlines */
--line-verdigris:  rgba(90, 155, 142, 0.24)    /* verdigris at 24% for rings/borders */
--glow-verdigris:  rgba(90, 155, 142, 0.4)     /* for blur glows */
--noise-opacity:   0.035                         /* for the grain overlay */
```

## Usage rules

1. **Verdigris is earned.** One dominant verdigris element per composition. Every additional verdigris use dilutes the one that matters.
2. **Ochre is rare.** Maximum one ochre element per composition, often zero. When present, it balances the composition against the cool greens.
3. **Ivory is the workhorse.** All primary and secondary text is ivory or ivory-dim. White is never used.
4. **Ground is deliberate.** The near-black has a tint. Pure `#000000` is never used.
5. **Noise is mandatory.** Every composition has the grain overlay at ~3.5% opacity. This is what keeps the flat colors from reading as digital slop.

## What this palette communicates

- **Seriousness without pomposity** — the ivory-on-near-black library register, not the white-on-black tech register
- **Ecology without greenwashing** — verdigris is a green you have to earn, not a fresh-leaf green applied at marketing request
- **Temporal depth** — every color choice references materials that accrue meaning over time (copper patina, parchment, aged brass, weathered stone)
- **Craft** — the grain, the restraint, the deliberate palette discipline all signal that care was taken

## Inspiration references

- Penguin Great Ideas book covers
- Old scientific atlases (Haeckel's *Kunstformen der Natur*, the original *Audubon* plates)
- The Statue of Liberty's surface after a century of weathering
- The patina on an old brass sextant
- The interior of the Rose Reading Room at NYPL
- 1920s restored bookplates
- The typographic tradition of civic documents — constitutions, treaties, manifestos that have survived
