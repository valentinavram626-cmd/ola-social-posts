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
