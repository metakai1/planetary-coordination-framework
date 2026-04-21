#!/usr/bin/env python3
"""
Render posters to high-resolution PNGs suitable for print.

For 8.5" × 11" letter at 300 DPI:
  design size 850 × 1100 × 3x device scale = 2550 × 3300 px

This is exactly 300 DPI when printed at letter size. Inkjet printers
typically handle 300 DPI well. 600 DPI (6x scale) would be marginally
sharper but files get huge and the difference isn't visible at viewing
distance on glossy photo paper.
"""

from pathlib import Path
from playwright.sync_api import sync_playwright

POSTERS_DIR = Path(__file__).parent


def render_poster(html_path: Path, out_path: Path):
    """Render a poster at 3x resolution (300 DPI for letter size)."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        context = browser.new_context(
            viewport={"width": 950, "height": 1200},
            device_scale_factor=3,  # 3x for 300 DPI print output
        )
        page = context.new_page()
        page.goto(f"file://{html_path.resolve()}")
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(2500)  # fonts + QR image
        canvas = page.locator(".canvas")
        canvas.screenshot(path=str(out_path))
        browser.close()


def main():
    html_files = sorted(POSTERS_DIR.glob("*.html"))
    print(f"rendering {len(html_files)} posters at 300 DPI (3x scale)...")

    for html_path in html_files:
        png_path = html_path.with_suffix(".png")
        render_poster(html_path, png_path)
        print(f"  {html_path.name} → {png_path.name}")

    print(f"\ndone. PNGs written to {POSTERS_DIR}")
    print("for print: open in any image viewer, print at letter size, 'actual size' / no scaling")


if __name__ == "__main__":
    main()
