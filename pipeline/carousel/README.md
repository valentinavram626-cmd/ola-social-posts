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
