#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build, gate and stage every topic for one publication day.

    python3 day.py 2026-11-05

For each topic in topics.DAY:
  1. build.py renders every size into <job>-out/
  2. qa.py gates them IN PLACE and exits non-zero on any failure
  3. only on a pass are the frames staged to posts/carousel/<YYYY-MM>-<slug>/

A topic whose gate fails is left unstaged and reported. It does not ship.
Nothing here schedules anything; staging only puts the frames where the push
can reach them.
"""
import shutil, subprocess, sys, pathlib, json
import topics, build

D = pathlib.Path(__file__).parent
REPO = D.parent.parent
DAY_ARG = sys.argv[1] if sys.argv[1:] else None
MONTH = (DAY_ARG or "2026-11-05")[:7]

results = {}
for t in topics.DAY:
    slug = t["slug"]
    print(f"\n=== {slug} — {t['title']}")
    for d in build.stale_dirs(slug):
        shutil.rmtree(d, ignore_errors=True)
    try:
        build.build(slug)
    except SystemExit as e:
        results[slug] = ("BUILD FAILED", str(e)); print(" ", e); continue

    g = subprocess.run([sys.executable, str(D / "qa.py")], cwd=D,
                       capture_output=True, text=True)
    if g.returncode != 0:
        tail = [l for l in g.stdout.splitlines() if l.startswith("  - ")]
        results[slug] = ("GATE FAILED", "; ".join(tail) or g.stdout[-400:])
        print("  GATE FAILED:", "; ".join(tail))
        continue

    dest = REPO / "posts" / "carousel" / f"{MONTH}-{slug}"
    shutil.rmtree(dest, ignore_errors=True)
    dest.mkdir(parents=True)
    for jd in sorted(D.glob("*-out")):
        job = jd.name[:-4]
        tgt = dest / job; tgt.mkdir()
        for f in sorted(jd.glob("*.jpg")):          # JPEG is what gets posted
            shutil.copy2(f, tgt / f.name)

    # LinkedIn renders a multi-image post as a static grid; a PDF document post
    # is the only native format there that swipes. Built from the English feed
    # frames, in order.
    from PIL import Image
    ims = [Image.open(f).convert("RGB")
           for f in sorted((dest / "en-feed").glob("*.jpg"))]
    pdf = dest / f"linkedin-{slug}.pdf"
    ims[0].save(pdf, save_all=True, append_images=ims[1:], resolution=96.0)

    results[slug] = ("OK", f"{dest.relative_to(REPO)}  (+{pdf.name})")
    print("  staged →", dest.relative_to(REPO), "and", pdf.name)

print("\n================ DAY SUMMARY")
for slug, (state, detail) in results.items():
    print(f"  {state:12s} {slug:20s} {detail}")
ok = [s for s, (st, _) in results.items() if st == "OK"]
print(f"\n  {len(ok)} of {len(topics.DAY)} carousels passed the gate.")
(D / "day-result.json").write_text(json.dumps(results, indent=2, ensure_ascii=False))
sys.exit(0 if ok else 1)
