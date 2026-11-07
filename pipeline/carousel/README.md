# Carousel format — one topic, nine networks

Still-image carousels in place of built video. Decided 3 November 2026.

## Why this exists

Valentin's call: three slides of advice plus one that carries the ask, no
music, no voiceover. Dropping the audio track removes two problems at once.

* **Licensing.** TikTok restricts business accounts to its Commercial Music
  Library; Meta's Sound Collection licence covers Meta products only and does
  not travel to TikTok, YouTube or the website. No audio, no question.
* **Scheduling.** Adding a platform's licensed track has to happen inside the
  app at posting time, which rules out Metricool auto-publish. Silent images
  schedule normally.

And the reader controls the pace, which is what he actually asked for: in a
video the renderer decides how long a line stays on screen; in a carousel the
reader swipes when they are ready.

## What the research changed

From the November 2026 brief:

* **Brand belongs in the first frame, not the last.** System1 x TikTok, 887
  short-form ads: brand attribution within 2 seconds gave +88% memory lift
  and +92% awareness lift. A bare logo on its own measured **-30%**. So the
  lion, the wordmark and the number are on slide 1 and on every slide after
  it, and the last slide is never a plain contact card.
* **A CTA present from the opening beat a CTA revealed later by +44%.**
  Hence the WhatsApp number in the footer throughout.
* **Up to four distinctive assets early roughly doubles brand recognition;
  past four, attention drops.** Ours are exactly four and never vary: the
  lion, the gold, Bricolage Grotesque, the escalation ladder.

## The nine networks, and what each one actually does

Checked 3 November 2026, not assumed. Four of these broke the naive plan.

| Network | Build | Why |
|---|---|---|
| Instagram, Facebook, Threads | `ro-feed` — 1080x1350, 4 slides | Swipeable. Tallest ratio the feed allows. |
| TikTok | `ro-tiktok` — 1080x1920, 4 slides | Photo post. Its own chrome covers the top tenth, the bottom quarter and a rail down the right. |
| LinkedIn | `en-feed` -> **PDF document post** | A multi-image post renders as a **grid**, not a swipe: all four land at once, ask included. The document post is the only native format there that swipes. |
| Bluesky | `en-feed` — 4 slides | Published guidance says a Bluesky post only becomes a swipeable carousel at **five** images. Its API rejects more than **four**. Both are true, so a swipeable Bluesky carousel is impossible through Metricool; the four English slides go out stacked. Captions cap at 300 characters. |
| Pinterest | `en-pin` — 1000x1500 | Pinterest **crops** anything wider than 2:3, so the 4:5 feed render would have been cut. |
| Google Business | `en-gbp` — 1200x1200, one frame | A listing, not a feed. Nobody swipes it, so the whole message sits in one image. |
| YouTube | — | Video only. |
| Twitch | — | Not an image-posting surface. |

Language follows the network rule: Romanian on Instagram, Facebook, Threads
and TikTok; English on LinkedIn, Bluesky, Pinterest and Google Business. The
English copy is rewritten, not translated — the LinkedIn reader is not the
same person as the Instagram reader.

## Running it

    python3 pipeline/carousel/build.py            # all six
    python3 pipeline/carousel/build.py en-pin     # one
    python3 pipeline/carousel/qa.py               # gates; exits non-zero on failure

The copy lives in `build.py` once and is shared across every size.

### Slide types

| type   | carries                                            |
|--------|----------------------------------------------------|
| `hook` | poster layout, lion watermark, kicker + headline   |
| `step` | step pill, hero figure, one sentence, optional note |
| `ask`  | step pill, hero figure, sentence, then the ask and the number |
| `solo` | the whole message in one frame; no ladder, no swipe cue |

## What the first live run taught us

Run on 3 November 2026, 20:45. Six of nine network targets published;
three failed, and the failures were worth more than the successes.

* **TikTok refuses PNG.** *"The 'image/png' type is not allowed, use
  'image/jpeg' or 'image/webp'."* Every frame now also ships as JPEG at
  quality 92 with no chroma subsampling, and JPEG is what gets posted
  everywhere — one format beats a per-network exception.
* **Bluesky caps a post at four images.** *"array too big (maximum 4,
  got 5)."* The five-slide build existed because published guidance says
  the carousel starts at five. Both facts are correct and they contradict
  each other in practice: through the API, a swipeable Bluesky carousel
  cannot be made. The five-slide job was deleted rather than left broken.
* **Threads returned "Media container not created by unknown cause"** on
  the same images Facebook and Instagram accepted. Meta gives nothing to
  work with here; retried with JPEG.

The lesson worth keeping: platform documentation told us what the feeds
*display*, and only a live post told us what the APIs *accept*. Those are
different questions, and the second one is the one that decides what ships.

## limits.py — no caption is ever scheduled without being counted

**`from limits import check` then `check(caption, network)` before every
single `createScheduledPost` and `updateScheduledPost`.** It raises rather
than returns, so a caption over the limit cannot quietly go through.

Set by Valentin on 6 November 2026 after the same fault broke three platforms
in three days — and not one of the error messages mentioned length:

| Date | Network | Caption | Limit | What the platform said |
|---|---|---|---|---|
| 4-5 Nov | Threads | 638, 755 | 500 | `Media container not created by unknown cause` |
| 6 Nov | Pinterest | 921, 929, 941, 1046 | 800 | `Code: 400 - Invalid request` + the first 75 characters quoted back |
| 6 Nov | Instagram, TikTok | 2277 | 2200 | held before it could fail |

Every one of those reads like a problem with the media or the words. None of
them is. The images in the Threads failures published perfectly to Facebook
and Instagram from the same post, in the same second.

**The Instagram/TikTok case is the one to remember.** Those captions started
at 1998 characters — comfortably inside the limit. Four Gatekeeper repair
rounds grew them to 2277. The repair loop broke posts that were fine, because
nothing measured the caption after an edit. So `check()` goes **after every
edit**, not only after the first draft.

The limits, for reading rather than for copying — use the table in the file:
Instagram 2200, Facebook 63206, Threads 500, TikTok 2200, LinkedIn 3000,
Bluesky 300, Pinterest 800 description and 100 title, Google Business 1500.
A Story has no caption of its own, so length does not apply to it.

`limits.report()` returns a line per caption with its count, for the
"Lungimi" section of a run report. Put the numbers in the report: a claim
that the lengths were checked is worth nothing next to the counts.

## preflight.py — run it before anything leaves the machine

`python3 preflight.py` exits non-zero and nothing is pushed or scheduled.

Every check in it exists because the mistake it catches was actually made, and
in every case **the mistake was reported as success**. That is the pattern the
file exists to break: a claim that something is fine is worth nothing unless a
check that *could* have failed was run and did not.

| Check | The day it was earned |
|---|---|
| IDENTITIES | 3 Nov — five people's handles, their contact dates and their tax subjects sat in a public repo for six days |
| LOSS | 5 Nov — rewriting one topic silently deleted its Google Business card, because the edit replaced a span of text without checking what was inside it |
| FORMAT | 5 Nov — a content card carried its own CTA and the closing card repeated it, almost word for word |
| SCOPE | 3 Nov — a post nearly went out calling an England-only payment universal |
| SOURCES | every figure needs a primary source and the date it was read |
| ALT | 5 Nov — a whole day published with `mediaAltText` null on every image |

The order of a run is: write the copy → `build.py` → `qa.py` (the visual gate) →
**`preflight.py`** (the content gate) → push → schedule. A failure at any gate
stops everything after it.

### Alt text cannot be forgotten any more

`alt.py` derives one alt string per frame from the card that is already
written, so a frame cannot exist without alt text. That is deliberately not a
reminder in a checklist: a reminder is something to forget, and this was
forgotten on the first day it mattered. `alt_for(cards)` returns a list the
same length as the media list, and preflight checks that it is.

## The format, set 5 November 2026

**Four cards. Three of content, then the ask on its own. Every network, no
exceptions.** Valentin set this after looking at the 4 November run.

What was wrong with five:

* The fourth card carried its own call to action AND the fifth repeated it,
  on the VAT carousel almost word for word — *"Te apropii de prag? Scrie-ne
  și urmărim împreună cele 12 luni"* then *"Aproape de prag? Scrie-ne și
  verificăm împreună ultimele 12 luni"*. Two asks back to back read as a
  sales pitch, not as help.
* Bluesky caps a post at four images, so Bluesky alone needed a different
  shape and a CTA thread reply to carry the fifth card. Four everywhere
  removes the special case: **the Bluesky CTA reply is gone.**
* The `ask` card type is retired. It now renders as a plain `step`, so an
  older topics.py still builds, without its CTA block. **A content card
  carries no call to action.**

His second instruction, the same day: **write it for someone who has never
read anything about accounting.** The VAT carousel was the example — *"Ieșirea
din TVA · £88.000 · Poți cere anularea dacă te aștepți să stai sub £88.000"*.
Every word of that is correct and none of it is usable. Rewritten as *"Ai
vândut de peste £90.000? Trebuie să te înregistrezi la TVA. Se numără cât ai
vândut, nu cât ți-a rămas."* Same facts, same sources, no jargon. Card 3 still
has to answer **who does NOT have to** — that rule is unchanged.

Three cards is less room, so the third card has to earn its place: it holds
the exclusion, which is the most useful line in the whole carousel.

## What the second live run taught us

Run on 4 November 2026 for publication on the 5th. Four of five carousels
shipped; 29 Metricool entries accepted, one rejection, fixed in the same run.

* **Pinterest needs `pinLink`, not just `boardId` and `pinTitle`.**
  *"Pinterest data requires 'boardId', 'pinTitle', and 'pinLink'."* The tool
  description names only the first two as required. Send the website URL.
* **Bluesky's 300 characters have to carry three things, not one.** The four
  brand tags are 85 characters and the compliance disclaimer is another 65,
  which leaves about 150 for the message. Write the Bluesky body to that
  budget from the start rather than trimming it afterwards.
* **A Metricool thread reply is forced to exactly one hour after its parent**,
  as the first run found. Confirmed again: every `descendants` entry landed at
  parent + 60 minutes regardless of the date supplied.
* **The `ask` card is the one that overflows at 4:5.** On a 1080x1350 frame the
  body block has 892px before the footer is pushed out of the frame, and a
  three-line sentence plus a two-line ask comes to 931px. `probe.py` measures
  it per topic; use it before rendering a full day. The fix is shorter copy —
  never smaller type.
* **The template had no slot for the compliance disclaimer**, which is why it
  was missing from every item rather than from some of them. `cta` and `solo`
  slides now take a `disc` field. When a check finds the same fault in all five
  items at once, suspect the template.
* **A reviewer's objection is not a source, and neither is a page that is
  silent.** A compliance reviewer asked for the VAT deregistration test to say
  "the next 12 months". Two GOV.UK pages do not mention a period, so the change
  was declined — correctly, on that evidence. The reviewer then cited VAT
  Notice 700/11 section 3.2, which states it outright. Verified, and adopted.
  Check the notices, not only the guidance pages.

## What the third live run taught us

Run on 5 November 2026 for publication on the 6th. Four of five carousels
shipped; 29 Metricool entries accepted, one rejection, fixed in the same run.

* **TikTok requires a `title` in `tiktokData`.** *"Error processing post
  information: TikTok title is required"* — on a photo post, with the caption
  already in `text`. The tool description does not list it as required and the
  earlier runs never hit it, because earlier runs sent video. Send a short
  Romanian title as well as the caption.
* **Threads now has its own post and its own caption.** `th_caption()` in
  `captions.py`, asserted under 500 characters including the four brand tags,
  which are 85 of them. The 500-character cap is the whole explanation for
  *"Media container not created by unknown cause"* — a message that points at
  the images and has nothing to do with them. Read back from the planner, the
  four Threads captions measured 441, 453, 456 and 482.
* **Bluesky carries the full brand disclaimer, not a shortened one.** The
  300-character cap is answered by shorter copy, exactly as qa.py's frame
  overflow is answered by shorter copy. Swapping the long disclaimer back in
  pushed two captions over and they were rewritten until the gate passed.
* **A checker's objection is not a source, and neither is a checker's fix.**
  Five carousels came back HOLD. Every objection that changed a card was
  re-verified at primary source first — and the biggest one survived: CIS340
  Appendix C excludes only "the supply of security guards" and the *running*
  of site facilities, while erecting CCTV posts, fitting security shutters and
  putting up site hoardings are inside the scheme. The card had said "site
  security is outside CIS", which would have told a subcontractor doing exactly
  that work that he need not register.
* **Check the second language.** The trading allowance fix — gov.uk says "your
  employer or the employer of your spouse or civil partner", not "partner" —
  landed in English and not in Romanian on the first pass. The independent
  verifier caught it on the rendered frame, not in the source. A fix is not
  done until it is on every frame it was supposed to reach.
* **A topic can be held for a wording decision, not only for a wrong figure.**
  Child Benefit's figures were all verified. It was held because the exclusion
  that actually decides the claim for this audience is the residence condition,
  and writing that on a card touches the regulated immigration boundary. The
  standing rule is that an unsure sentence crosses the line, so it waits for
  Valentin rather than being improvised overnight.

## What the third live run taught us

Run on 7 November 2026 for publication on the 8th. Five of five carousels shipped;
36 Metricool entries accepted, one rejection, fixed in the same run.

* **A TikTok photo post needs a `title` in `tiktokData`.** The first attempt came
  back `Error processing post information: TikTok title is required`. The tool
  description lists `title` among the optional fields, so nothing warned us. Every
  TikTok post now carries a short Romanian title, separate from the caption.
* **The LinkedIn `documentTitle` is published text, so the language rule applies
  to it.** The first LinkedIn post of the day went up with the Romanian topic
  title on an English post. Caught on read-back and corrected with
  `updateScheduledPost`; the remaining four were built with English titles. Worth
  remembering that `updateScheduledPost` changes the post's id and keeps its uuid,
  so the read-back shows one entry, not two.
* **Metricool re-hosts `media` URLs on its own CDN at scheduling time.** Every
  accepted post came back with `static.metricool.com` paths, which is the cheapest
  proof that the raw GitHub URLs resolved and that the push was actually live.
* **The planner read-back does not fit in one call.** `getScheduledPosts` for a
  whole day of 36 entries exceeds the tool's response limit; it has to be read in
  windows and the counts added up. Reading it is still the only thing that turns
  "scheduled" from a claim into a fact.
* **A verifier reading only the images will flag the footer phone number on cards
  1-3 as CTA creep.** It is the template, set deliberately in this README, and
  `preflight.py`'s FORMAT check passes because it tests the `ask` and `phone`
  fields on the cards rather than the rendered footer. Tell the next verifier up
  front, or it costs a round trip. The gate's docstring says "no ask or phone
  anywhere but the last", which overstates what it enforces.
* **A compliance fix can break a length limit.** Two topics needed their own
  disclaimers — an accountant is not the adviser for an energy rebate or for
  employment status — and the first wording blew the Threads, Bluesky, Pinterest
  and feed caps on both. Short disclaimers on every network, with the fuller
  boundary wording in the long-form bodies, is what fits. `limits.py` caught all
  ten; nothing was judged by eye.

## Scope: what we post about

Widened on 3 November 2026 at Valentin's direction. Not only accounting:

- tax and accounting (Self Assessment, MTD, VAT, CIS, payroll, companies)
- good news and citizens' rights in the UK — benefits, rebates, new laws
  that help people, consumer protections, cost-of-living support
- residency and rights **information only** (see the boundary below)

His words: *"daca ne informam cum trebuie este imposibil sa gresim."* The
second half of that sentence is the whole job. The near-miss that proves it:
he asked for a post about "the £100 fuel allowance". The payment is real,
but it is called the **Household Energy Payment**, it applies in **England
only**, only to **council tax bands A-D**, only on a **main home**,
automatically only for **direct debit payers**, and only **from January
2027**. Four of those five facts would have been missed.

So every claim must answer four questions before it ships:

1. **Which nation** — England, Scotland, Wales, Northern Ireland, or all of
   the UK. Never "everyone" unless it is literally everyone.
2. **Which category** — income band, council tax band, age, status.
3. **Who does NOT get it.** Mandatory, and usually the most useful line in
   the post. For this audience the common case is someone renting a room
   where the landlord pays council tax: excluded from a great deal, and
   nobody tells them.
4. **From when**, and whether it is automatic or has to be claimed.

A post that says "you get £100" is worse than no post. A post that tells the
reader whether *they* get it is the product.

### Hard boundary: immigration and residency

Giving immigration advice in the UK is regulated. The line is **"offering an
opinion on someone's individual immigration situation"**, which requires
authorisation from the Immigration Advice Authority (formerly OISC).
Penalties of up to £15,000 apply to unauthorised advice. Ola is not
authorised.

Allowed: explaining publicly available facts, describing how a scheme works,
pointing at the GOV.UK page. Not allowed: telling a reader what *they*
should do about *their* status, in a post or in a comment reply. If a
sentence might cross the line, it crosses the line.

## Who runs this

`Ola Content Studio` — a scheduled task, every evening at 19:37 London,
building the next day's five carousels. It runs the evening before on
purpose: the checks need a night of margin to be worth anything.

It spawns separate sub-agents to check its own work — fact checker, scope
checker, compliance reviewer, and an independent verifier that never saw the
drafting and reads the rendered images against the sources. **Any HOLD means
that carousel is not scheduled at all.** Four good posts beat five with one
wrong figure.

## Hashtags

`build.py` holds them. Four brand tags go on every post in either language,
because a brand tag is a name and is never translated:

    #OlaAccountancy #ValentinTheAccountant
    #OlaAccountancyLuton #OlaAccountancyBirmingham

Topical tags follow and change per post and per language.

## Gates — run them, do not assume

`qa.py` measures and exits non-zero on any failure:

* Contrast of every text colour on the background, WCAG. All five pairs clear
  4.5:1; the lowest is the muted note at 6.6:1.
* No ink within 5% of any edge.
* For 9:16 only: no **bright** content in the top tenth, the bottom quarter,
  or the right 12%. Dim background — the glow, the watermark behind the
  headline — may sit under the chrome, because nothing is lost there.

Two of those checks exist because the first build failed them, and both
failures are worth remembering:

* **en-bsky slide 5** had a three-line sentence. The centred content
  overflowed the frame, `overflow:hidden` clipped the bottom, and the footer
  was pushed into the margin. Shorten the copy; do not quietly shrink type.
* **ro-tiktok** put the footer at 84% of frame height, inside TikTok's
  caption area, and ran the swipe cue to 92% width, under the action rail.
  The first attempt at a fix added 500px of bottom padding to both the body
  and the footer, which pushed the column to 1972px inside a 1920px frame —
  so the padding was clipped away again and nothing moved. Measuring the
  computed box in the browser found it; guessing twice did not.

A figure that cannot be verified gets dropped, not softened. The first
carousel lost "£100 even if you owe no tax" for exactly that reason: widely
repeated and probably right, but not on the GOV.UK penalties page.

## What the fourth live run taught us

Run on 6 November 2026 for publication on the 7th. Five of five carousels
shipped; 36 Metricool entries accepted, none rejected.

**The report could not be written.** `add_repo` is not available in this
session, so `valentinavram626-cmd/ola-ops-reports` could not be attached and
`SAFETY.md` could not be read. The exact error from the GitHub tool was:

    Access denied: repository "valentinavram626-cmd/ola-ops-reports" is not
    configured for this session. Allowed repositories:
    valentinavram626-cmd/ola-social-posts, valentinavram626-cmd/ola-next. If
    the add_repo tool (mcp__claude-code-remote__add_repo) is available in this
    session, ask the user whether to add this repository to it [...] if
    add_repo is not available, this repository cannot be added to this session.

The run carried on under the doctrine as summarised in the task prompt, and
the report was printed in full in the run output instead. This is the single
most important line of the day: two runs in three days have now been unable to
leave a report where it belongs.

* **`assert_lengths()` had three holes, and every one of them was a limit the
  repo already knew.** It measured Bluesky, Threads and Google Business, and
  never measured Pinterest (800), Instagram (2200), TikTok (2200) or LinkedIn
  (3000) — the exact limits in `limits.py` and the exact failures in its own
  table. Twelve Pinterest descriptions were over, one at 1046. `cis-20-30`'s
  Romanian caption was still sitting at 2281 against Instagram's 2200, which is
  the 6 November failure, still in the file two days later. A check that is
  never run cannot fail, and a check that cannot fail is not a check.
* **A checker's objection is still not a source — and this time four of five
  survived re-verification.** The independent verifier, the scope checker and
  the fact checker between them produced eight objections that changed a card.
  Each was read at primary source before the card was touched. The one that was
  declined was declined on evidence: the verifier reported the WhatsApp number
  in the footer of every content card as a format breach on 30 frames, but that
  footer is the brand template set on 3 November and recorded in this README,
  and `preflight.py`'s FORMAT check — which tests for an `ask` or `phone` field
  on a content card — passes. See "To settle" below.
* **The fix has to reach the long captions too, not just the cards.** The
  compliance reviewer's two FIXes landed on the Cold Weather and Consumer
  Rights CTA cards in the same edit round. Both carousels then went to the
  scheduler with the long Instagram, TikTok and LinkedIn captions still ending
  "vorbește cu un contabil" on a DWP benefit and a consumer-law question, and
  the Consumer Rights caption still asking "Vrei să știi ce drepturi ai?" —
  the exact headline compliance had asked to remove. Caught at the scheduling
  step by reading the caption rather than trusting the card. `ro_caption`,
  `li_caption`, `th_caption`, `bsky_caption` and `pin_caption` now take a
  per-topic `disc_ro` / `disc_en` override so a non-tax topic cannot send a
  reader to an accountant.
* **A carousel can be wrong by being incomplete.** The limited-company set said
  "three deadlines, not one". There are four: the confirmation statement runs on
  its own 12-month review period, is filed within 14 days of it closing, is
  filed even when nothing has changed, and a miss can get the company struck
  off. Late accounts cost money; this one costs the company. The scope checker
  found it and gov.uk confirmed it.
* **Card 1 has to survive card 2.** "Every business mile is 55p off your profit"
  is false from mile 10,001, and card 2 said so one swipe later. The hook now
  reads "worth up to 55p". Two separate checkers flagged it independently,
  which is usually the sign that a reader would have too.
* **Check the categorical word.** "No company is excused: you file after a loss
  and even if it never traded" was wrong — a company dormant for Corporation
  Tax is excused the return once HMRC has been told. "No", "every", "always"
  and "all" are where a card goes wrong without any figure being wrong.

### To settle

**The footer on content cards.** The 3 November brand rule puts the lion, the
wordmark and the WhatsApp number on slide 1 and every slide after it, on the
evidence that a CTA present from the opening beat a CTA revealed later by +44%.
The 5 November format rule says a content card carries no call to action and no
WhatsApp button. On the rendered frames, cards 1-3 carry the number and a
WhatsApp glyph in the footer strip, and card 4 carries the ask sentence and the
number in a green pill. Both readings are defensible and the studio did not
change the template overnight. Valentin's call.
