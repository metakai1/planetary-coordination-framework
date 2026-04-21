# Memetics

Visual and linguistic assets for propagating the framework.

## Contents

```
memetics/
├── README.md               This file
├── cards/                  1080×1080 square format (feed-ready)
│   ├── 01-*.html           HTML source (edit these)
│   ├── 01-*.png            Rendered output (do not edit)
│   └── ...
├── posters/                Portrait 2:3 (print-ready) — not yet built
├── banners/                Landscape 16:9 (headers, LinkedIn) — not yet built
├── stencils/               High-contrast SVG (real-world use) — not yet built
├── brand/
│   ├── colors.md           Palette spec and rules
│   ├── typography.md       Typeface spec and scale
│   ├── voice.md            Language and tone rules
│   └── cards.css           Shared CSS for all cards
├── generate-cards.py       Card generator from config
└── render-all.py           HTML → PNG rendering pipeline
```

## Working with the cards

### To edit an existing card's text or structure

Edit `generate-cards.py` — find the card in the `CARDS` list, modify the
relevant fields, then:

```bash
python generate-cards.py    # regenerate HTML
python render-all.py        # re-render PNGs
```

The cards regenerate from config, so edits are cheap and consistent.

Note: Cards 01 and 02 are the reference implementations and have inline CSS.
Cards 03+ use the shared `brand/cards.css`. If you want to modify the base
visual language, edit `brand/cards.css` and cards 03+ update automatically.
Cards 01 and 02 need manual editing.

### To add a new card

Append a new dict to the `CARDS` list in `generate-cards.py`. Minimum fields:

```python
{
    'num': 11,
    'slug': 'short-kebab-case-identifier',
    'headline_plain': 'The full line as plain text, for filename/title.',
    'headline_size': 120,              # px, scale to fit the line
    'headline_html': 'The line with <span class="emphasis">emphasis</span>.',
    'eyebrow': 'Source or context',    # optional
    'second_voice': 'Sans imperative', # optional
    'tag_line': 'Italic serif coda',   # optional
    'corner_tl': 'Card category',
    'corner_bl': 'Section · §N',
    'corner_br': 'Domain · Area',
    'footer_left': 'CC0 · Public domain',
},
```

Then regenerate. See existing entries for the full parameter surface,
especially `va_top` / `va_left` for positioning the verdigris glow behind
the emphasis word.

### Dependencies

```bash
pip install playwright
playwright install chromium
```

## Brand rules (the short version)

**Palette:** warm near-black ground, ivory/ochre atmospheric warmth, verdigris
as signature accent only. No pure white, no pure black, no green atmosphere.
One ochre element per composition, maximum. See `brand/colors.md`.

**Typography:** Instrument Serif for headlines, Inter for subordinate, JetBrains
Mono for metadata. No bold on serifs. No all-caps headlines. No emoji.
See `brand/typography.md`.

**Voice:** Declarative. Short. No exclamation marks. No hashtags in-image.
Specific nouns. Never explain the meme. See `brand/voice.md`.

**Series signature:** verdigris spine + italic numeral on the left, hairlines
framing top and bottom, corner metadata labels, `exitcapitalism.link` footer.
Present on every card.

## License

All content in this directory is released under CC0 1.0 (public domain).
Fork, remix, print, stencil, post on walls.
