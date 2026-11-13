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
    if lang == "ro":
        # The Birmingham and En brands publish in English only, so they carry no
        # RO block. Asking for one is a bug in the caller, not a missing field:
        # say which topic and which brand rather than raising KeyError('RO').
        if "RO" not in t:
            raise SystemExit(f"FAIL {t['slug']}: brand '{t.get('brand','ola')}' "
                             f"publishes in English only and has no RO cards")
        body, cta = t["RO"], t["CTA_RO"]
    else:
        body, cta = t["EN"], t["CTA_EN"]
    return list(body[:3]) + [cta]


# Which renders each Metricool brand actually needs. Set 13 November 2026, when
# Valentin opened two further brands. Rendering a size no connected account can
# publish is pure cost, so each brand gets only its own:
#
#   ola   (7561492) — Instagram, Facebook, Threads, TikTok, LinkedIn, Bluesky,
#                     Pinterest, Google Business. Romanian feeds + English ones.
#   bham  (8085549) — Facebook, Instagram, TikTok. ENGLISH only.
#   en    (8086748) — TikTok only, as Valentin connected it. ENGLISH only.
#
# A topic with no "brand" key is the Ola brand, so every topic written before
# this change keeps rendering exactly as it did.
BRAND_JOBS = {
    "ola":  ("ro-feed", "ro-tiktok", "en-feed", "en-pin", "en-bsky"),
    "bham": ("en-feed", "en-tiktok"),
    "en":   ("en-tiktok",),
}


def jobs_for(t):
    """Every render this topic needs, keyed by the network it serves."""
    # Size and language of every render this pipeline knows how to make. Added
    # 13 Nov 2026: en-tiktok, because the two new ENGLISH-only brands both have
    # TikTok and the Romanian ro-tiktok render cannot serve them.
    SPEC = {
      "ro-feed":   (1080, 1350, "ro"),  # Instagram, Facebook, Threads
      "ro-tiktok": (1080, 1920, "ro"),  # TikTok photo post
      "en-feed":   (1080, 1350, "en"),  # LinkedIn, published as a PDF
      "en-pin":    (1000, 1500, "en"),  # Pinterest crops wider than 2:3
      # Four cards is exactly Bluesky's ceiling, so it now takes the same set as
      # everyone else and the CTA thread reply it used to need is gone.
      "en-bsky":   (1080, 1350, "en"),
      "en-tiktok": (1080, 1920, "en"),  # Birmingham and En brands
    }

    # Choose the brand's jobs FIRST, then render only those. Building them all
    # and filtering afterwards asked an English-only topic for Romanian cards
    # and failed on a brand that is working exactly as intended.
    brand = t.get("brand", "ola")
    j = {k: (cards(t, SPEC[k][2]), *SPEC[k]) for k in BRAND_JOBS[brand]}

    # Google Business is a listing with nothing to swipe: one frame, whole
    # message, and only on the single topic chosen for it that day. The Ola
    # brand is the only one with a Google Business listing connected.
    if brand == "ola" and t.get("GBP"):
        j["en-gbp"] = (t["GBP"], 1200, 1200, "en")
    return j


# --------------------------------------------------------------- single image
# Three single-image posts a brand, a day, set by Valentin on 13 November 2026:
# one problem, one answer, one frame, Ola branded. The `solo` slide type already
# existed for the Google Business listing, so this reuses it rather than
# inventing a second look — a reader who sees a solo post and a carousel on the
# same feed should see the same firm.
#
# Sizes are the feeds these actually reach, no more: 4:5 for an Instagram or
# Facebook feed, 9:16 for TikTok. The 1200x1200 Google Business frame stays
# where it is, on the carousel topic that carries GBP.
SOLO_JOBS = {
    "solo-feed":   (1080, 1350),   # Instagram, Facebook
    "solo-tiktok": (1080, 1920),   # TikTok
}


def jobs_for_solo(s):
    """Every render one single-image post needs, keyed like a carousel job."""
    lang = s.get("lang", "en")
    return {f"{lang}-{k}": ([s["slide"]], w, h, lang)
            for k, (w, h) in SOLO_JOBS.items()}


def _render(JOBS, keys=None):
    """Render each named job to <job>-out/. Shared by carousels and solo posts."""
    from PIL import Image
    for key in (keys or list(JOBS)):
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
        print(f"  {key:12s} {w}x{h:<5d} {r.stdout.strip() or r.stderr.strip()[:120]}  (+{n} jpg)")
        if n != len(slides):
            raise SystemExit(f"FAIL {key}: expected {len(slides)} frames, got {n}")


def build_solo(slug, only=None):
    """Render one single-image post from topics.SOLOS."""
    s = topics.SOLO_BY_SLUG[slug]
    _render(jobs_for_solo(s), only)


def build(slug, only=None):
    t = topics.BY_SLUG[slug]
    _render(jobs_for(t), only)


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
