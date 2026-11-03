# Carousel format — 3 + 1

Still-image carousels in place of built video. Decided 3 November 2026.

## Why this exists

Valentin's call: three slides of advice plus a fourth that carries the ask,
no music, no voiceover. Two problems disappear with the audio track:

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

From the November 2026 brief (see `departments/reports/`):

* **Brand belongs in the first frame, not the last.** System1 x TikTok, 887
  short-form ads: correct brand attribution within 2 seconds gave +88% memory
  lift and +92% awareness lift. A bare logo on its own measured **-30%**.
  So the lion, the wordmark and the number are on slide 1 and on every slide
  after it, and slide 4 is never a plain contact card.
* **A CTA present from the opening beat a CTA revealed later by +44%**
  (TikTok creative data). Hence the WhatsApp number in the footer throughout.
* **Up to four distinctive assets early roughly doubles brand recognition;
  past four, attention drops.** Ours are exactly four and never vary: the
  lion, the gold, Bricolage Grotesque, the escalation ladder.

## The house device

The ladder under the header — one segment per slide, filled as you advance.
It makes an escalating sequence legible at a glance and is identical on every
carousel. One repeatable structural device is what the accounts that work in
this niche have (Erika Kullberg reads fine print; we show the ladder).

## Running it

    node pipeline/carousel/render.js c1        # reads c1.json, writes c1-out/

Slides are 1080 x 1350 (4:5) — the tallest ratio the feed allows, so the post
occupies the most screen. A 1080 x 1920 variant is needed for TikTok photo
posts; not built yet.

### Slide types

| type   | carries                                        |
|--------|------------------------------------------------|
| `hook` | poster layout, lion watermark, kicker + headline |
| `step` | step pill, hero figure, one sentence, optional note |
| `ask`  | step pill, hero figure, sentence, then the ask and the number |

## Gates — run them, do not assume

* Contrast of every text colour on the background, WCAG. All five pairs in
  the first carousel cleared 4.5:1; the lowest was the muted note at 6.6:1.
* No ink in the outer 58px of any edge.
* Every figure verified on GOV.UK the same week, URL recorded in the post's
  notes.

A claim that could not be verified gets dropped, not softened. The first
carousel lost "£100 even if you owe no tax" for exactly that reason: it is
widely repeated and probably right, but it is not on the GOV.UK penalties
page, so it is not on a slide.
