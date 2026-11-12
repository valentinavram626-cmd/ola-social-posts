#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Write what the checkers read, and the captions.md that ships with each post.

Two different bundles on purpose:
  verify/<slug>-claims.md   card text + source URLs, no reasoning — so the
                            fact and scope checkers test the claim instead of
                            agreeing with an argument for it
  verify/<slug>-images.md   rendered frame paths + source URLs, nothing else —
                            for the verifier that never saw the drafting
"""
import pathlib, re, html
import topics, captions

D = pathlib.Path(__file__).parent
REPO = D.parent.parent
V = pathlib.Path("/home/claude/verify"); V.mkdir(exist_ok=True)
MONTH = "2026-11"
PUBLISH = "13 November 2026"


def flat(s):
    return html.unescape(re.sub(r"<[^>]+>", "", str(s))).strip()


def card_lines(cards, label):
    out = [f"### {label}"]
    for i, c in enumerate(cards, 1):
        bits = []
        for k in ("kicker", "step", "h1", "fig", "say", "note", "ask", "phone", "disc"):
            if c.get(k):
                bits.append(f"  {k}: {flat(c[k])}")
        if c.get("rows"):
            for r in c["rows"]:
                bits.append(f"  row: {flat(r[0])} — {flat(r[1])}")
        out.append(f"CARD {i:02d} [{c['type']}]\n" + "\n".join(bits))
    return "\n\n".join(out)


for t in topics.DAY:
    slug = t["slug"]
    post = REPO / "posts" / "carousel" / f"{MONTH}-{slug}"

    # ---- captions.md, shipped with the images
    cap = [f"# Textele postării — {t['title']}", "",
           "Limba urmează regula rețelelor: română pe Instagram, Facebook, Threads",
           "și TikTok; engleză pe LinkedIn, Bluesky, Pinterest și Google Business.",
           "", "---", "", "## RO — Instagram, Facebook, Threads, TikTok", "",
           captions.ro_caption(slug), "", "---", "",
           "## EN — LinkedIn  (postat ca document PDF, nu ca imagini multiple)", "",
           captions.li_caption(slug), "", "---", "",
           f"## EN — Bluesky  (limită 300 de caractere; aici {len(captions.bsky_caption(slug))})", "",
           captions.bsky_caption(slug), "", "---", "",
           "## EN — Pinterest  (descriere pin)", "",
           f"**Titlu:** {captions.C[slug]['pin_title']}", "",
           captions.pin_caption(slug)]
    if "gbp" in captions.C[slug]:
        cap += ["", "---", "", "## EN — Google Business  (o singură imagine)", "",
                captions.gbp_caption(slug)]
    cap += ["", "---", "", "## Surse primare", ""]
    for what, url, read in t["SOURCES"]:
        cap.append(f"- {what}\n  {url}  (citit {read})")
    (post / "captions.md").write_text("\n".join(cap) + "\n")

    # ---- claims bundle for the fact and scope checkers
    claims = [f"# {t['title']}", "",
              f"Carousel for publication on {PUBLISH}. Below is every word that",
              "appears on the cards, and the primary-source URLs the drafter used.", "",
              card_lines(t["RO"] + [t["CTA_RO"]], "Romanian cards (Instagram, Facebook, Threads, TikTok)"), "",
              card_lines(t["EN"] + [t["CTA_EN"]], "English cards (LinkedIn, Bluesky, Pinterest)")]
    if t.get("GBP"):
        claims += ["", card_lines(t["GBP"], "English single frame (Google Business)")]
    claims += ["", "### Captions that ship with the images", "",
               "RO:\n" + captions.ro_caption(slug), "",
               "EN LinkedIn:\n" + captions.li_caption(slug), "",
               "EN Bluesky:\n" + captions.bsky_caption(slug), "",
               "EN Pinterest:\n" + captions.pin_caption(slug)]
    if "gbp" in captions.C[slug]:
        claims += ["", "EN Google Business:\n" + captions.gbp_caption(slug)]
    claims += ["", "### SCOPE as the drafter answered it", ""]
    for k in ("nation", "category", "excluded", "from_when"):
        claims.append(f"- {k}: {(t.get('SCOPE') or {}).get(k, '(MISSING)')}")
    claims += ["", "### Sources cited by the drafter", ""]
    for what, url, read in t["SOURCES"]:
        claims.append(f"- {url}  (read {read})\n  covers: {what}")
    (V / f"{slug}-claims.md").write_text("\n".join(claims) + "\n")

    # ---- images bundle for the independent verifier
    imgs = [f"# Rendered frames — {slug}", "",
            "Read the images. Check the words that are actually on them against the",
            "sources below. Report per carousel: SHIP, or HOLD with the reason.", ""]
    for jd in sorted(post.glob("*/")):
        if not jd.is_dir():
            continue
        for f in sorted(jd.glob("*.jpg")):
            imgs.append(str(f))
    imgs += ["", "### Primary sources", ""]
    for what, url, read in t["SOURCES"]:
        imgs.append(f"- {url}\n  covers: {what}")
    (V / f"{slug}-images.md").write_text("\n".join(imgs) + "\n")

print("captions.md written into each post folder; verify/ bundles written")
for f in sorted(V.iterdir()):
    print(" ", f.name, f.stat().st_size, "bytes")
