#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""The footer has to be INSIDE the frame. Measured in the browser, not guessed.

qa.py's bottom-margin test looks for ink too close to the edge, so a footer
pushed clean out of the frame passes it: there is no ink down there at all.
That blind spot was written up on 8 November and was still open on 10 November,
when the independent verifier found two English cards whose footer had been
pushed off a 1080x1350 frame (ftTop 1388 and 1324 against a 1225 budget) after
both qa.py and an ad-hoc ink check had passed them.

An ink check cannot close this. The footer's position is a layout fact, so it
is read from the layout: render.js already exposes it and measure.js already
prints it. This asserts on it.

    python3 footer.py            # every topic in topics.DAY, every job

The budget is the footer's own height. On a 1350-frame the body block ends at
1225 and the footer occupies the remaining 125px, which is where probe.py's
892px content budget comes from. Same 125px applies at every size, because the
footer strip does not scale with the frame.
"""
import math, pathlib, re, subprocess, sys
import topics, build

D = pathlib.Path(__file__).parent
# The footer strip is laid out in the same CSS at every size, so its height
# scales with the frame's WIDTH, not with a flat constant: 125px at 1080 wide,
# and 116px on Pinterest's 1000-wide render. A flat 125 flags all 16 en-pin
# frames of a healthy day, which is a gate that cries wolf rather than a gate.
# Two footer variants exist, and they are not the same height. A slide inside a
# carousel carries the "swipe ->" cue; a single-frame post does not, because
# there is nothing to swipe to (carousel.html: `const solo = (n===1)`). Measured
# on 13 November 2026: 125px with the cue, 124px without, on a 1080-wide frame.
# One constant for both made every single-frame render fail by exactly 1px, and
# the 1200-wide Google Business post passed only because floor() rounded its way.
FOOTER_CAROUSEL_AT_1080 = 125
FOOTER_SINGLE_AT_1080 = 124
LINE = re.compile(r"slide (\d+) +frame (\d+).*?ftTop (\d+)")

def measure(jobs, slug):
    """Measure every frame of one post's renders against the footer budget."""
    for job, (slides, W, _H, _lang) in jobs.items():
        out = subprocess.run(["node", str(D / "measure.js"), job],
                             cwd=D, capture_output=True, text=True).stdout
        rows = LINE.findall(out)
        if not rows:
            fails.append(f"{slug}/{job}: measure.js returned nothing")
            continue
        single = len(slides) == 1
        base = FOOTER_SINGLE_AT_1080 if single else FOOTER_CAROUSEL_AT_1080
        need = math.floor(base * W / 1080)
        for slide, H, ft in rows:
            H, ft = int(H), int(ft)
            globals()["n"] += 1
            room = H - ft
            if room < need:
                fails.append(
                    f"{slug}/{job} slide {slide}: footer starts at {ft} in a {H} frame "
                    f"— {room}px left, needs {need}. "
                    + ("FOOTER IS OFF-FRAME." if room <= 0 else "Footer is clipped."))


fails, n = [], 0

# The single-image posts, added 13 November 2026, are measured here too. They are
# the frames most likely to fail it: one frame carries the whole message, and the
# footer variant without the swipe cue is a pixel shorter, which is the bug that
# made every single-frame render fail by exactly one pixel before this file
# modelled both.
for s in topics.SOLOS:
    build.build_solo(s["slug"])
    measure(build.jobs_for_solo(s), s["slug"])

for t in topics.DAY:
    slug = t["slug"]
    build.build(slug)                      # every job this topic needs
    for job in build.jobs_for(t):
        out = subprocess.run(["node", str(D / "measure.js"), job],
                             cwd=D, capture_output=True, text=True).stdout
        rows = LINE.findall(out)
        if not rows:
            fails.append(f"{slug}/{job}: measure.js returned nothing")
            continue
        # Read the width and the frame count from the job itself rather than a
        # hardcoded table: a table goes stale the moment a job is added, and it
        # fails with KeyError instead of saying what it does not know.
        slides, W, _H, _lang = build.jobs_for(t)[job]
        single = len(slides) == 1
        # floor, not round: a frame cannot be asked for a fraction of a pixel.
        # The 1200-wide Google Business solo footer measures 138, and round()
        # asks for 139, which fails a frame that is demonstrably intact.
        base = FOOTER_SINGLE_AT_1080 if single else FOOTER_CAROUSEL_AT_1080
        need = math.floor(base * W / 1080)
        for slide, H, ft in rows:
            H, ft = int(H), int(ft)
            n += 1
            room = H - ft
            if room < need:
                fails.append(
                    f"{slug}/{job} slide {slide}: footer starts at {ft} in a {H} frame "
                    f"— {room}px left, needs {need}. "
                    + ("FOOTER IS OFF-FRAME." if room <= 0 else "Footer is clipped."))

print(f"\nfooter gate: {n} frames measured, {len(fails)} failure(s)")
for f in fails:
    print("  -", f)
sys.exit(1 if fails else 0)
