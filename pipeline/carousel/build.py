#!/usr/bin/env python3
"""Build one carousel for every connected platform, in the right language and ratio.

The copy lives here once. Each platform gets the size its feed actually wants
and the language Valentin's network rule assigns to it:
  Romanian  — Instagram, Facebook, Threads, TikTok
  English   — LinkedIn, Bluesky, Pinterest, Google Business
"""
import json, subprocess, sys, pathlib

D = pathlib.Path(__file__).parent
PHONE = "0330 133 1886"

# ---------------------------------------------------------------- Romanian
RO = [
  dict(type="hook",
       kicker="Self Assessment · termen 31 ianuarie 2027",
       h1="Ratezi <em>31 ianuarie</em>?",
       say="Penalizările HMRC nu vin o singură dată. Cresc în trepte, lună după lună."),
  dict(type="step", step="Din prima zi", fig="<cur>£</cur>100",
       say="Penalizarea inițială, imediat ce declarația a întârziat."),
  dict(type="step", step="După 3 luni", fig="<cur>£</cur>10<small> / zi</small>",
       say="Se adaugă <b>în fiecare zi</b>, până la maximum £900.",
       note="Cu tot cu primii £100, ajungi la £1.000."),
  dict(type="ask", step="După 6 luni", fig="+5%",
       say="din taxa datorată — sau <b>£300</b>, care e mai mare. Iar la 12 luni se aplică încă o dată.",
       ask="Nu lăsa pe ultima săptămână. Scrie-ne și verificăm împreună dacă ai termen de depus.",
       phone=PHONE),
]

# ---------------------------------------------------------------- English
# Rewritten for a different reader, not translated: LinkedIn and Google
# bring people who are searching, not scrolling.
EN = [
  dict(type="hook",
       kicker="Self Assessment · deadline 31 January 2027",
       h1="Miss <em>31 January</em>?",
       say="HMRC penalties don't arrive once. They escalate, month after month."),
  dict(type="step", step="From day one", fig="<cur>£</cur>100",
       say="The initial penalty, the moment your return is late."),
  dict(type="step", step="After 3 months", fig="<cur>£</cur>10<small> / day</small>",
       say="Added <b>every single day</b>, up to a maximum of £900.",
       note="With the first £100, that is £1,000."),
  dict(type="ask", step="After 6 months", fig="+5%",
       say="of the tax due — or <b>£300</b>, whichever is greater. At 12 months it applies again.",
       ask="Not sure whether you need to file? Send us a message and we will check it with you.",
       phone=PHONE),
]

# Bluesky stacks four images and only turns a post into a real swipeable
# carousel at five, so the fifth slide carries the late-payment penalties —
# information the four-slide version leaves to the caption.
EN5 = EN[:3] + [
  dict(type="step", step="After 6 months", fig="+5%",
       say="of the tax due — or <b>£300</b>, whichever is greater. At 12 months it applies again."),
  dict(type="ask", step="Paying late", fig="5%<small> × 3</small>",
       say="A separate set of penalties on unpaid tax: 5% at 30 days, 6 months and 12 months.",
       ask="Not sure where you stand? Send us a message and we will check it with you.",
       phone=PHONE),
]

# Google Business is a listing, not a feed — nobody swipes it. One frame.
GBP = [
  dict(type="solo",
       kicker="Self Assessment · deadline 31 January 2027",
       h1="Filing late costs more every month.",
       rows=[["<cur>£</cur>100", "from the first day your return is late"],
             ["<cur>£</cur>10/day", "after 3 months, up to £900"],
             ["+5%",              "after 6 months, or £300 if greater"]],
       ask="Luton and Birmingham. Message us and we will check whether you need to file.",
       phone=PHONE),
]

JOBS = {
  # key            slides  w     h     note
  "ro-feed":   (RO,  1080, 1350, "ro"),   # Instagram, Facebook, Threads
  "ro-tiktok": (RO,  1080, 1920, "ro"),   # TikTok photo post
  "en-feed":   (EN,  1080, 1350, "en"),   # LinkedIn (also the PDF source)
  "en-bsky":   (EN5, 1080, 1350, "en"),   # Bluesky — five, so it becomes a carousel
  "en-pin":    (EN,  1000, 1500, "en"),   # Pinterest crops anything wider than 2:3
  "en-gbp":    (GBP, 1200, 1200, "en"),   # Google Business — one frame
}

only = sys.argv[1:] or list(JOBS)
for key in only:
    slides, w, h, lang = JOBS[key]
    (D / f"{key}.json").write_text(json.dumps(
        {"id": key, "w": w, "h": h, "lang": lang, "slides": slides},
        ensure_ascii=False, indent=2))
    r = subprocess.run(["node", str(D / "render.js"), key], cwd=D,
                       capture_output=True, text=True)
    print(f"{key:10s} {w}x{h}  {r.stdout.strip() or r.stderr.strip()[:120]}")
