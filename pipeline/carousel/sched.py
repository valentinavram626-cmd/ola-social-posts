#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Emit every Metricool payload for one publication day, in priority order.

Reads what is ACTUALLY staged on disk, so a post the gate held never appears.
Counts every caption with limits.check before it is emitted; a caption over its
network's limit raises here rather than failing silently at publication.
"""
import json, pathlib, sys
import topics
from alt import alt_for
from limits import check

DAY = sys.argv[1] if sys.argv[1:] else "2026-11-18"
MONTH = DAY[:7]
REPO = pathlib.Path(__file__).parent.parent.parent
RAW = "https://raw.githubusercontent.com/valentinavram626-cmd/ola-social-posts/main/posts/carousel"
TZ = "Europe/London"
SITE = "https://ola-accountancy.co.uk"
BOARD = "1038431695270727659"
BRAND = {"ola": "7561492", "bham": "8085549", "en": "8086748"}

def staged(slug, job):
    d = REPO / "posts" / "carousel" / f"{MONTH}-{slug}" / job
    return [f"{RAW}/{MONTH}-{slug}/{job}/{f.name}" for f in sorted(d.glob("*.jpg"))] if d.is_dir() else []

def pdf(slug):
    p = REPO / "posts" / "carousel" / f"{MONTH}-{slug}" / f"linkedin-{slug}.pdf"
    return f"{RAW}/{MONTH}-{slug}/linkedin-{slug}.pdf" if p.exists() else None

def cards(t, lang):
    body = t["RO"] if lang == "ro" else t["EN"]
    cta = t["CTA_RO"] if lang == "ro" else t["CTA_EN"]
    return list(body[:3]) + [cta]

TIMES = {
 ("ola","feed"):   ["08:00","11:00","13:30","17:00","19:30"],
 ("ola","li"):     ["08:30","11:30","14:00","17:30","20:00"],
 ("ola","bsky"):   ["09:00","11:15","13:45","17:15","19:45"],
 ("ola","pin"):    ["08:15","11:45","14:15","17:45","20:15"],
 ("ola","solo"):   ["10:00","15:30","21:00"],
 ("bham","feed"):  ["08:45","12:15","15:00","18:15","20:30"],
 ("bham","solo"):  ["10:30","16:30","19:00"],
 ("en","feed"):    ["09:30","12:45","16:00","18:45","21:15"],
 ("en","solo"):    ["11:30","17:30","20:45"],
}

out = []
def post(prio, label, brand, when, info):
    out.append(dict(prio=prio, label=label, blogId=BRAND[brand],
                    date=f"{DAY}T{when}:00+00:00", info=info))

def base(text, media, alts, providers, **nd):
    i = dict(autoPublish=True, draft=False, hasNotReadNotes=False, shortener=False,
             smartLinkData={"ids": []}, media=media, mediaAltText=alts,
             providers=[{"network": n} for n in providers],
             publicationDate={"dateTime": f"{DAY}T00:00:00", "timezone": TZ},
             text=text)
    i.update(nd)
    return i

for brand in ("ola", "bham", "en"):
    tops = [t for t in topics.DAY if t.get("brand", "ola") == brand]
    # ---- carousels
    n = 0
    for t in tops:
        slug = t["slug"]
        feedjob = "ro-feed" if brand == "ola" else "en-feed"
        tjob = "ro-tiktok" if brand == "ola" else "en-tiktok"
        lang = "ro" if brand == "ola" else "en"
        feed, tik = staged(slug, feedjob), staged(slug, tjob)
        if not (feed or tik):
            continue
        when = TIMES[(brand, "feed")][n]
        a_feed = alt_for(cards(t, lang))
        if brand == "ola" and feed:
            check(t["caption"], "instagram"); check(t["caption"], "facebook")
            post(1, f"{slug} IG+FB", brand, when, base(t["caption"], feed, a_feed,
                 ["instagram", "facebook"], instagramData={"type": "POST"}, facebookData={"type": "POST"}))
        elif feed:
            check(t["caption"], "instagram")
            post(1, f"{slug} IG+FB", brand, when, base(t["caption"], feed, a_feed,
                 ["instagram", "facebook"], instagramData={"type": "POST"}, facebookData={"type": "POST"}))
        if tik:
            check(t["caption"], "tiktok")
            post(1, f"{slug} TikTok", brand, when, base(t["caption"], tik, alt_for(cards(t, lang)),
                 ["tiktok"], tiktokData={"privacyOption": "PUBLIC_TO_EVERYONE"}))
        if brand == "ola" and feed:
            check(t["caption_threads"], "threads")
            post(2, f"{slug} Threads", brand, when, base(t["caption_threads"], feed, a_feed,
                 ["threads"], threadsData={"allowedCountryCodes": []}))
        # Stories: first frame of the 9:16 render, same time as its own feed post.
        # No text: a Story has no caption and it is the only network of the post.
        if brand in ("ola", "bham") and tik:
            post(3, f"{slug} Story", brand, when, base("", tik[:1], alt_for(cards(t, lang))[:1],
                 ["instagram", "facebook"], instagramData={"type": "STORY"}, facebookData={"type": "STORY"}))
        if brand == "ola":
            p = pdf(slug)
            if p:
                check(t["caption_li"], "linkedin")
                post(2, f"{slug} LinkedIn", brand, TIMES[("ola","li")][n],
                     base(t["caption_li"], [p], [a_feed[0]], ["linkedin"],
                          linkedinData={"documentTitle": t["title"][:95], "type": "post"}))
            bsky = staged(slug, "en-bsky")
            if bsky:
                check(t["caption_bsky"], "bluesky")
                a_en = alt_for(cards(t, "en"))
                post(2, f"{slug} Bluesky", brand, TIMES[("ola","bsky")][n],
                     base(t["caption_bsky"], bsky, a_en, ["bluesky"],
                          blueskyData={"postLanguages": ["en"]}))
            pin = staged(slug, "en-pin")
            if pin:
                check(t["caption_pin_desc"], "pinterest")
                check(t["caption_pin_title"], "pinterest_title")
                post(2, f"{slug} Pinterest", brand, TIMES[("ola","pin")][n],
                     base(t["caption_pin_desc"], pin[:1], [alt_for(cards(t, "en"))[0]], ["pinterest"],
                          pinterestData={"boardId": BOARD, "pinTitle": t["caption_pin_title"],
                                         "pinLink": SITE}))
        n += 1
    # ---- single-image posts
    m = 0
    for s in topics.SOLOS:
        if s.get("brand") != brand:
            continue
        lang = s.get("lang", "en")
        feed = staged(s["slug"], f"{lang}-solo-feed")
        tik = staged(s["slug"], f"{lang}-solo-tiktok")
        if not (feed or tik):
            continue
        when = TIMES[(brand, "solo")][m]
        a = alt_for([s["slide"]])
        if brand in ("ola", "bham") and feed:
            check(s["caption"], "instagram")
            post(4, f"{s['slug']} IG+FB", brand, when, base(s["caption"], feed, a,
                 ["instagram", "facebook"], instagramData={"type": "POST"}, facebookData={"type": "POST"}))
        if tik:
            check(s["caption"], "tiktok")
            post(4, f"{s['slug']} TikTok", brand, when, base(s["caption"], tik, a,
                 ["tiktok"], tiktokData={"privacyOption": "PUBLIC_TO_EVERYONE"}))
        m += 1

out.sort(key=lambda r: (r["prio"], r["blogId"], r["date"]))
pathlib.Path("sched.json").write_text(json.dumps(out, ensure_ascii=False, indent=1))
from collections import Counter
print("payloads:", len(out))
print(Counter((r["prio"], r["blogId"]) for r in out))
urls = sorted({u for r in out for u in r["info"]["media"]})
pathlib.Path("urls.txt").write_text("\n".join(urls))
print("distinct media urls:", len(urls))
for r in out:
    assert len(r["info"]["mediaAltText"]) == len(r["info"]["media"]), r["label"]
print("alt length matches media on every payload")
