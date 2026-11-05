#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build one topic's carousel for every connected platform, in the right language and ratio.

    python3 build.py <topic-slug>              # every job for that topic
    python3 build.py <topic-slug> en-pin       # one job

The copy lives in topics.py once and is shared across every size. Each platform
gets the size its feed actually wants and the language Valentin's network rule
assigns to it:
  Romanian  — Instagram, Facebook, Threads, TikTok
  English   — LinkedIn, Bluesky, Pinterest, Google Business

Outputs land in <job>-out/ so qa.py can gate them in place. The day driver
(day.py) moves them to out/<slug>/<job>/ only after the gate passes.
"""
import json, shutil, subprocess, sys, pathlib
import topics

D = pathlib.Path(__file__).parent


def cards(t, lang):
    """The four frames of a carousel: three of content, then the ask on its own.

    Set by Valentin on 5 Nov 2026, replacing the old five-card set. Two things
    were wrong with five: the fourth card carried its own call to action AND the
    fifth repeated it almost word for word, and Bluesky's API caps a post at four
    images, so Bluesky alone needed a different shape. Four cards everywhere, the
    ask only on the last, is one format for every network with nothing special-cased.

    A topic that still supplies four content cards is truncated rather than
    rejected, so an older topics.py renders instead of failing the night's run.
    """
    body, cta = (t["RO"], t["CTA_RO"]) if lang == "ro" else (t["EN"], t["CTA_EN"])
    return list(body[:3]) + [cta]


def jobs_for(t):
    """Every render this topic needs, keyed by the network it serves."""
    j = {
      "ro-feed":   (cards(t, "ro"), 1080, 1350, "ro"),  # Instagram, Facebook, Threads
      "ro-tiktok": (cards(t, "ro"), 1080, 1920, "ro"),  # TikTok photo post
      "en-feed":   (cards(t, "en"), 1080, 1350, "en"),  # LinkedIn, published as a PDF
      "en-pin":    (cards(t, "en"), 1000, 1500, "en"),  # Pinterest crops wider than 2:3

      # Four cards is exactly Bluesky's ceiling, so it now takes the same set as
      # everyone else and the CTA thread reply it used to need is gone.
      "en-bsky":   (cards(t, "en"), 1080, 1350, "en"),
    }
    # Google Business is a listing with nothing to swipe: one frame, whole
    # message, and only on the single topic chosen for it that day.
    if t.get("GBP"):
        j["en-gbp"] = (t["GBP"], 1200, 1200, "en")
    return j


def build(slug, only=None):
    t = topics.BY_SLUG[slug]
    JOBS = jobs_for(t)
    keys = only or list(JOBS)
    from PIL import Image

    for key in keys:
        slides, w, h, lang = JOBS[key]
        out = D / f"{key}-out"
        shutil.rmtree(out, ignore_errors=True)       # never gate a stale frame

        (D / f"{key}.json").write_text(json.dumps(
            {"id": key, "w": w, "h": h, "lang": lang, "slides": slides},
            ensure_ascii=False, indent=2))
        r = subprocess.run(["node", str(D / "render.js"), key], cwd=D,
                           capture_output=True, text=True)

        # TikTok refuses image/png ("use 'image/jpeg' or 'image/webp'"), so every
        # frame also ships as JPEG and that is what gets posted everywhere. One
        # format across all networks beats a per-network exception.
        for png in sorted(out.glob("*.png")):
            Image.open(png).convert("RGB").save(
                png.with_suffix(".jpg"), quality=92, optimize=True, subsampling=0)

        n = len(list(out.glob("*.jpg")))
        print(f"  {key:10s} {w}x{h:<5d} {r.stdout.strip() or r.stderr.strip()[:120]}  (+{n} jpg)")
        if n != len(slides):
            raise SystemExit(f"FAIL {slug}/{key}: expected {len(slides)} frames, got {n}")


def stale_dirs(slug):
    """Job dirs left over from another topic, which qa.py would otherwise gate."""
    want = set(jobs_for(topics.BY_SLUG[slug]))
    return [d for d in D.glob("*-out") if d.name[:-4] not in want]


if __name__ == "__main__":
    if not sys.argv[1:]:
        raise SystemExit("usage: build.py <topic-slug> [job ...]\n  slugs: "
                         + ", ".join(topics.BY_SLUG))
    slug, rest = sys.argv[1], sys.argv[2:]
    for d in stale_dirs(slug):
        shutil.rmtree(d, ignore_errors=True)
    print(topics.BY_SLUG[slug]["title"])
    build(slug, rest or None)
