#!/usr/bin/env python3
"""
Planetary Coordination Framework — Card Generator

Generates the memetics/cards/*.html files from a single card-config list.
This ensures visual consistency across the series and makes bulk revisions
cheap (change one place, regenerate everything).

Each card has a few parameters that vary:
  - number, slug, classification, corner labels
  - eyebrow (optional — hero cards omit it)
  - headline with emphasis word and optional ochre period
  - second-voice (optional sans-serif imperative)
  - tag-line (optional italic serif coda)
  - headline_size and verdigris accent position (tuned per card)

Everything else comes from brand/cards.css.
"""

from pathlib import Path
from textwrap import dedent

CARDS_DIR = Path(__file__).parent / "cards"
CSS_PATH = "../brand/cards.css"  # relative to the card HTML file

# ─── Card template ─────────────────────────────────────────────────────────
# Uses the shared cards.css for all brand styling. Only card-specific
# overrides go in the inline <style>.

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>PCF · Card {num} · {slug_title}</title>
<!--
  Planetary Coordination Framework — Card {num_padded}
  "{headline_plain}"
  1080 × 1080 · Uses shared brand/cards.css
-->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Instrument+Serif:ital@0;1&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{css_path}">
<style>
  /* Card-specific overrides */
  .headline {{
    font-size: {headline_size}px;
    {extra_headline_css}
  }}
  .bloom-verdigris-accent {{
    top: {va_top};
    left: {va_left};
    {va_extra}
  }}
  {extra_css}
</style>
</head>
<body>
<div class="canvas">

  <div class="bloom bloom-warm-primary"></div>
  <div class="bloom bloom-ochre"></div>
  <div class="bloom bloom-ochre-2"></div>
  <div class="bloom bloom-warm-accent"></div>
  <div class="bloom-verdigris-accent"></div>

  <div class="spine"></div>
  <div class="spine-numeral">{num_padded}</div>

  <div class="hairline top"></div>
  <div class="hairline bottom"></div>

  <div class="corner-label tl">{corner_tl}</div>
  <div class="corner-label tr">Edition 2026.1</div>
  <div class="corner-label bl">{corner_bl}</div>
  <div class="corner-label br">{corner_br}</div>

  <div class="content">

    <div class="header">
      <div class="mark">
        <div class="mark-dot"></div>
        <div class="mark-name">Planetary Coordination Framework</div>
      </div>
      <div class="classification">Exit Capitalism</div>
    </div>

    <div class="headline-block">
      {eyebrow_html}
      <h1 class="headline">{headline_html}</h1>
      {second_voice_html}
      {tag_line_html}
    </div>

    <div class="footer">
      <div class="{footer_left_class}">{footer_left}</div>
      <div class="url">
        <span class="arrow">→</span>exitcapitalism<span class="path">.link</span>
      </div>
    </div>

  </div>

  <div class="noise"></div>

</div>
</body>
</html>
'''


def render_card(card):
    """Render one card config to HTML."""
    num_padded = f"{card['num']:02d}"

    # Eyebrow is optional — hero/declarative cards often omit it
    if card.get('eyebrow'):
        eyebrow_html = f'<div class="eyebrow">{card["eyebrow"]}</div>'
    else:
        eyebrow_html = ''

    # Second voice (sans imperative) is optional
    if card.get('second_voice'):
        second_voice_html = f'<div class="second-voice">{card["second_voice"]}</div>'
    else:
        second_voice_html = ''

    # Tag line (italic serif coda) is optional
    if card.get('tag_line'):
        tag_line_html = f'<div class="tag-line">{card["tag_line"]}</div>'
    else:
        tag_line_html = ''

    # Footer-left can be either italic attribution or mono label
    if card.get('footer_left_style') == 'attribution':
        footer_left_class = 'attribution'
    else:
        footer_left_class = 'footer-left'

    html = TEMPLATE.format(
        num=card['num'],
        num_padded=num_padded,
        slug_title=card['slug'].replace('-', ' ').title(),
        headline_plain=card['headline_plain'],
        css_path=CSS_PATH,
        headline_size=card.get('headline_size', 152),
        extra_headline_css=card.get('extra_headline_css', ''),
        va_top=card.get('va_top', '56%'),
        va_left=card.get('va_left', '32%'),
        va_extra=card.get('va_extra', ''),
        extra_css=card.get('extra_css', ''),
        corner_tl=card['corner_tl'],
        corner_bl=card['corner_bl'],
        corner_br=card['corner_br'],
        classification=card['classification'],
        eyebrow_html=eyebrow_html,
        headline_html=card['headline_html'],
        second_voice_html=second_voice_html,
        tag_line_html=tag_line_html,
        footer_left=card.get('footer_left', 'CC0 · Public domain'),
        footer_left_class=footer_left_class,
    )
    return html


# ─── Card configurations ───────────────────────────────────────────────────
#
# Each card is tuned individually. The emphasis word, headline size, and
# verdigris glow position are all chosen to match the specific typography
# and meaning of that card.

CARDS = [
    # ─── 03 · "Your customers are a commons." ──────────────────────────
    # Business-audience cousin of Card 01. Same insight, different register.
    # The word "customers" is the hook — business language doing anti-business
    # work. This is the card for the HN / Substack / econ Twitter crowd.
    {
        'num': 3,
        'slug': 'your-customers-are-a-commons',
        'headline_plain': 'Your customers are a commons.',
        'headline_size': 128,
        'headline_html': 'Your customers<br>are a <span class="emphasis">commons.</span>',
        'eyebrow': 'Aggregate demand externality',
        'second_voice': 'Your competitors are depleting it.',
        'tag_line': 'So are you.',
        'classification': 'Observation',
        'corner_tl': 'Observation',
        'corner_bl': 'Externalities · §3',
        'corner_br': 'Domain · Commerce',
        'footer_left': 'CC0 · Public domain',
        'va_top': '52%',
        'va_left': '28%',
    },

    # ─── 04 · "Scarcity is a distribution problem." ────────────────────
    # The post-scarcity reframe, compressed. Four words do all the work.
    # Emphasis on "distribution" because that's the load-bearing word —
    # the claim that what looks like scarcity is actually a coordination failure.
    {
        'num': 4,
        'slug': 'scarcity-is-a-distribution-problem',
        'headline_plain': 'Scarcity is a distribution problem.',
        'headline_size': 130,
        'headline_html': 'Scarcity is a<br><span class="emphasis">distribution</span><br>problem.',
        'extra_headline_css': 'line-height: 0.9;',
        'eyebrow': 'Post-scarcity premise',
        'second_voice': 'Production already works.',
        'tag_line': 'Distribution is where the system fails.',
        'classification': 'Premise',
        'corner_tl': 'Premise',
        'corner_bl': 'Post-Scarcity · §1',
        'corner_br': 'Domain · Framework',
        'footer_left': 'CC0 · Public domain',
        'va_top': '44%',
        'va_left': '38%',
    },

    # ─── 05 · "Hard floor. Soft ceiling. Free middle." ─────────────────
    # The three-layer structure compressed into a slogan. Each phrase is
    # its own line. The emphasis is on "Free" in the middle — the word that
    # makes this read as an expansion of liberty, not a constraint on it.
    {
        'num': 5,
        'slug': 'hard-floor-soft-ceiling-free-middle',
        'headline_plain': 'Hard floor. Soft ceiling. Free middle.',
        'headline_size': 104,
        'headline_html': 'Hard floor.<br>Soft ceiling.<br><span class="emphasis">Free</span> middle.',
        'extra_headline_css': 'line-height: 1.02;',
        'eyebrow': 'The three-layer structure',
        'second_voice': 'Constraints above. Freedom below.',
        'tag_line': 'Coordination only where markets fail.',
        'classification': 'Structure',
        'corner_tl': 'Structure',
        'corner_bl': 'Framework · §2',
        'corner_br': 'Domain · Architecture',
        'footer_left': 'CC0 · Public domain',
        'va_top': '58%',
        'va_left': '22%',
    },

    # ─── 06 · "The calculation problem was solved. Privately." ─────────
    # Insider signal for the Hayek-literate. The first sentence says
    # "socialism's impossibility argument is obsolete." The second says
    # "and we can tell because Amazon and Walmart run planned economies
    # internally." Deeply compressed; only lands if you know the reference.
    {
        'num': 6,
        'slug': 'calculation-problem-solved-privately',
        'headline_plain': 'The calculation problem was solved. Privately.',
        'headline_size': 94,
        'headline_html': 'The calculation<br>problem was solved.<br><span class="emphasis">Privately.</span>',
        'extra_headline_css': 'line-height: 1.02;',
        'eyebrow': 'After Hayek, 1945 · After Walmart, 2020',
        'second_voice': 'Amazon plans. Walmart plans. The PLA plans.',
        'tag_line': 'The question is only who owns the planning.',
        'classification': 'Argument',
        'corner_tl': 'Argument',
        'corner_bl': 'Calculation · §2',
        'corner_br': 'Domain · Theory',
        'footer_left': 'CC0 · Public domain',
        'va_top': '66%',
        'va_left': '28%',
    },

    # ─── 07 · "Planet first. People second. Profit third." ─────────────
    # The priority ordering as the hook. The rhyming tricolon does the work.
    # Emphasis on "Planet" — the first one, the one that reorders everything.
    # The tag line is the logical justification — the order matters because
    # any other order destroys the prior terms.
    {
        'num': 7,
        'slug': 'planet-people-profit',
        'headline_plain': 'Planet first. People second. Profit third.',
        'headline_size': 100,
        'headline_html': '<span class="emphasis">Planet</span> first.<br>People second.<br>Profit third<span class="period">.</span>',
        'extra_headline_css': 'line-height: 1.04;',
        'eyebrow': 'The priority ordering',
        'second_voice': 'In that order. Any other order destroys the first two.',
        'classification': 'Ordering',
        'corner_tl': 'Ordering',
        'corner_bl': 'Priorities · §1',
        'corner_br': 'Domain · Ethics',
        'footer_left': 'CC0 · Public domain',
        'va_top': '36%',
        'va_left': '20%',
    },

    # ─── 08 · "Markets at planetary scale is a category error." ────────
    # For the wonks. Short argument: the tool doesn't match the problem
    # it's being applied to. Emphasis on "category error" — philosophical
    # precision. This is the card for the thoughtful critic who wants to
    # understand the framework's actual claim.
    {
        'num': 8,
        'slug': 'markets-at-planetary-scale-category-error',
        'headline_plain': 'Markets at planetary scale is a category error.',
        'headline_size': 90,
        'headline_html': 'Markets at<br>planetary scale<br>is a <span class="emphasis">category error.</span>',
        'extra_headline_css': 'line-height: 1.02;',
        'eyebrow': 'The structural critique',
        'second_voice': 'Good tools. Wrong scale. Wrong problem.',
        'tag_line': 'Preserve markets. Bound them.',
        'classification': 'Argument',
        'corner_tl': 'Argument',
        'corner_bl': 'Scale · §2',
        'corner_br': 'Domain · Theory',
        'footer_left': 'CC0 · Public domain',
        'va_top': '68%',
        'va_left': '28%',
    },

    # ─── 09 · "Freedom to say no is the only freedom that matters." ────
    # The livelihood-floor pitch, disguised as a meditation on freedom.
    # This is the card that speaks to workers, to anyone trapped in a
    # coercive arrangement. Emphasis on "no" — the single word that
    # carries the whole move. Short, declarative, universal.
    {
        'num': 9,
        'slug': 'freedom-to-say-no',
        'headline_plain': 'Freedom to say no is the only freedom that matters.',
        'headline_size': 88,
        'headline_html': 'Freedom<br>to say <span class="emphasis">no</span><br>is the only freedom<br>that matters.',
        'extra_headline_css': 'line-height: 1.02;',
        'eyebrow': 'The livelihood floor',
        'second_voice': 'Guarantee survival. Labor becomes free.',
        'tag_line': 'The exit option is the only real negotiation.',
        'classification': 'Principle',
        'corner_tl': 'Principle',
        'corner_bl': 'Livelihood · §3',
        'corner_br': 'Domain · Labor',
        'footer_left': 'CC0 · Public domain',
        'va_top': '44%',
        'va_left': '22%',
    },

    # ─── 10 · "Before it exits you." ────────────────────────────────────
    # Dark variant of the hero. References the Hemenway Falk dynamic:
    # if firms race each other off the demand cliff, then capitalism
    # eventually exits its own customers. So exit it first. Two small
    # serif italics, one period. Meme-ready. Would work well as a sticker.
    {
        'num': 10,
        'slug': 'before-it-exits-you',
        'headline_plain': 'Exit capitalism. Before it exits you.',
        'headline_size': 130,
        'headline_html': '<span class="emphasis">Exit</span> capitalism.<br>Before it<br>exits you<span class="period">.</span>',
        'extra_headline_css': 'line-height: 0.98;',
        'second_voice': 'The AI layoff trap is already running.',
        'tag_line': 'Every round of automation eats demand at the next round.',
        'classification': 'Directive',
        'corner_tl': 'Directive',
        'corner_bl': 'AI Layoff Trap · §3',
        'corner_br': 'Domain · Labor',
        'footer_left': 'CC0 · Public domain',
        'va_top': '30%',
        'va_left': '16%',
    },
]


if __name__ == '__main__':
    CARDS_DIR.mkdir(exist_ok=True)
    for card in CARDS:
        num_padded = f"{card['num']:02d}"
        filename = f"{num_padded}-{card['slug']}.html"
        out_path = CARDS_DIR / filename
        html = render_card(card)
        out_path.write_text(html)
        print(f"wrote: {out_path}")
    print(f"\n{len(CARDS)} cards generated.")
