#!/usr/bin/env python3
"""
Render all cards in memetics/cards/*.html to memetics/cards/*.png.

Usage:
    python render-all.py

Requires: playwright with chromium installed.
    pip install playwright
    playwright install chromium
"""

from pathlib import Path
from playwright.sync_api import sync_playwright

CARDS_DIR = Path(__file__).parent / "cards"


def render_card(page, html_path: Path, out_path: Path):
    page.goto(f"file://{html_path.resolve()}")
    page.wait_for_load_state("networkidle")
    page.wait_for_timeout(2000)  # extra time for web fonts to settle
    canvas = page.locator(".canvas")
    canvas.screenshot(path=str(out_path))


def main():
    html_files = sorted(CARDS_DIR.glob("*.html"))
    print(f"rendering {len(html_files)} cards at 2x resolution...")

    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            viewport={"width": 1180, "height": 1180},
            device_scale_factor=2,  # retina-sharp output
        )
        page = context.new_page()

        for html_path in html_files:
            png_path = html_path.with_suffix(".png")
            render_card(page, html_path, png_path)
            print(f"  {html_path.name} → {png_path.name}")

        browser.close()

    print(f"\ndone. {len(html_files)} PNGs written to {CARDS_DIR}")


if __name__ == "__main__":
    main()
