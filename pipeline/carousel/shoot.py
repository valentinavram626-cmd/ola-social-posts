"""Render every HTML file listed in <out>/_jobs.json to a PNG beside it."""
import json, pathlib, sys
from playwright.sync_api import sync_playwright

out = pathlib.Path(sys.argv[1])
jobs = json.loads((out / "_jobs.json").read_text(encoding="utf-8"))

with sync_playwright() as pw:
    b = pw.chromium.launch()
    for j in jobs:
        page = b.new_page(viewport={"width": j["w"], "height": j["h"]}, device_scale_factor=1)
        page.goto((out / f"{j['name']}.html").resolve().as_uri())
        page.wait_for_timeout(250)
        page.evaluate("document.fonts.ready")
        page.wait_for_timeout(250)
        page.screenshot(path=str(out / f"{j['name']}.png"))
        page.close()
        print("  ", j["name"])
    b.close()
