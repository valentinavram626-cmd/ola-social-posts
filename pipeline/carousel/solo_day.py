#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build, gate and stage every single-image post for one publication day.

    python3 solo_day.py 2026-11-18

Mirrors day.py for topics.SOLOS: render -> qa.py in place -> stage to
posts/carousel/<YYYY-MM>-<slug>/. One frame per job, so there is no
LinkedIn PDF and nothing to swipe.
"""
import shutil, subprocess, sys, pathlib, json
import topics, build

D = pathlib.Path(__file__).parent
REPO = D.parent.parent
MONTH = (sys.argv[1] if sys.argv[1:] else "2026-11-18")[:7]

results = {}
for s in topics.SOLOS:
    slug = s["slug"]
    print(f"\n=== {slug}")
    want = set(build.jobs_for_solo(s))
    for d in D.glob("*-out"):
        if d.name[:-4] not in want:
            shutil.rmtree(d, ignore_errors=True)
    try:
        build.build_solo(slug)
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
        for f in sorted(jd.glob("*.jpg")):
            shutil.copy2(f, tgt / f.name)
    results[slug] = ("OK", str(dest.relative_to(REPO)))
    print("  staged →", dest.relative_to(REPO))

print("\n================ SOLO SUMMARY")
for slug, (state, detail) in results.items():
    print(f"  {state:12s} {slug:30s} {detail}")
ok = [s for s, (st, _) in results.items() if st == "OK"]
print(f"\n  {len(ok)} of {len(topics.SOLOS)} single-image posts passed the gate.")
(D / "solo-result.json").write_text(json.dumps(results, indent=2, ensure_ascii=False))
sys.exit(0 if ok else 1)
