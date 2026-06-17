#!/usr/bin/env python3
"""Refresh the screenshots embedded in README.md from the live HTML pages.

The shots below are the source of truth for what gets captured. When the HTML
templates gain real entries (or a new page is added to the library), re-run
this script so the visuals in README.md match reality.

Usage:
    python3 SoT/html/screenshot.py            # refresh every shot
    python3 SoT/html/screenshot.py atlas      # refresh shots whose name contains "atlas"
    python3 SoT/html/screenshot.py --list     # show configured shots and exit

Requires Playwright with Chromium:
    pip install playwright && python3 -m playwright install chromium
"""

import sys
from pathlib import Path

# (html file, css selector or None for the top of the page, output name)
# A selector captures just that element (e.g. one entry card); None captures
# the viewport — masthead, kicker, headline, and first content.
SHOTS = [
    ("index.html",                 None,              "atlas.png"),
    ("SoT.USER_JOURNEYS.html",     "#UJ-001",         "journey-map.png"),
    ("SoT.API_CONTRACTS.html",     "#API-001",        "api-contract.png"),
    ("SoT.DATA_MODEL.html",        "#DBT-001",        "data-model.png"),
    ("SoT.customer_feedback.html", "#CFD-001",        "feedback-card.png"),
    ("SoT.ADOPTION.html",          "#adoption-curve", "adoption-curve.png"),
]

VIEWPORT = {"width": 1280, "height": 880}
SCALE = 2  # device pixels per CSS pixel — keeps text crisp on GitHub


def main() -> int:
    base = Path(__file__).resolve().parent
    # Example mockups live under temp/ so they never ship with /prd-ce:init — the HTML
    # deliverable templates seed, their generated example renders do not.
    out_dir = base.parent.parent / "temp" / "sot-html-mockups"

    args = [a for a in sys.argv[1:]]
    if "--list" in args:
        for fname, sel, outname in SHOTS:
            print(f"{outname:22s} ← {fname}" + (f"  ({sel})" if sel else "  (page top)"))
        return 0

    name_filter = next((a for a in args if not a.startswith("-")), None)
    shots = [s for s in SHOTS if not name_filter or name_filter in s[2]]
    if not shots:
        print(f"no shot matches '{name_filter}' — try --list")
        return 1

    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright is not installed. Run:")
        print("  pip install playwright && python3 -m playwright install chromium")
        return 1

    out_dir.mkdir(parents=True, exist_ok=True)
    with sync_playwright() as pw:
        browser = pw.chromium.launch()
        page = browser.new_page(viewport=VIEWPORT, device_scale_factor=SCALE)
        for fname, sel, outname in shots:
            target = base / fname
            if not target.exists():
                print(f"SKIP {outname}: {fname} not found")
                continue
            page.goto(target.as_uri())
            page.wait_for_load_state("networkidle")
            dest = out_dir / outname
            if sel:
                page.locator(sel).screenshot(path=str(dest))
            else:
                page.screenshot(path=str(dest))
            print(f"OK   {dest.relative_to(base)}")
        browser.close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
