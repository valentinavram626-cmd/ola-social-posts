#!/usr/bin/env python3
"""How much vertical room each topic's ask card actually uses, per language.

The budget comes from measurement, not from taste: on a 1080x1350 frame the
footer has to start at 1225 or earlier, or qa.py finds ink in the bottom
margin. bd = 52 top padding + content + 96 bottom padding, starting at 182,
so the content block has 892px.
"""
import subprocess, sys, re, pathlib
import topics, build

BUDGET = 892
D = pathlib.Path(__file__).parent
for t in topics.DAY:
    build.build(t["slug"], ["en-feed", "ro-feed"])
    line = []
    for job in ("ro-feed", "en-feed"):
        out = subprocess.run(["node", str(D / "measure.js"), job],
                             cwd=D, capture_output=True, text=True).stdout
        m = re.search(r"slide 4 .*content (\d+)\.\.(\d+)", out)
        h = int(m.group(2)) - int(m.group(1))
        line.append(f"{job} {h:4d} {'OK ' if h <= BUDGET else 'OVER +%d' % (h-BUDGET)}")
    print(f"  {t['slug']:20s} " + "   ".join(line))
