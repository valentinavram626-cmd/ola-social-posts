# OLA CONTENT STUDIO — WRITER BRIEF — posts for Wednesday 25 November 2026

You are ONE writer for ONE set. You write copy only. You do NOT push to git and you do NOT schedule.

## THE RENDERER AND THE FIELD NAMES

Renderer: /home/claude/ola-social-posts/pipeline/carousel/solo.py
Read its docstring first. Five post kinds, each with exactly these fields:

  tip    slot, hero, sub, cta
  acq    slot, hero, sub, cta
  edu    slot, hero, sub, cta
  joke   slot, setup, punch, hook, cta
  quote  slot, line, attrib

A post is a dict; your set is a JSON array of them. Example:

  {"id":"ola-ro-01-tip","kind":"tip","sizes":["feed","story"],
   "slot":"Gandul zilei",
   "hero":"...","sub":"...","cta":"..."}

## LENGTH LIMITS — COUNT THEM IN CODE, NEVER BY EYE

  hero  <= 78      sub <= 175
  setup <= 62      punch <= 52      hook <= 125
  line  <= 130

The frame has no scrollbar. Over-length copy runs into the lion or off the bottom
edge and the render STILL EXITS 0. Write a python one-liner that asserts every
field of every post before you render.

`<em>text</em>` inside `hero` prints that fragment in gold. Use it on the figure,
and on AT MOST FOUR posts in your set. Gold on every frame is gold on none.

## THE FIVE SLOTS AND WHAT THEY ARE FOR

**Thought of the day / Gandul zilei** — NOT a tax tip. A short motivational thought
about business and work, OR a concrete example of something Ola does well, OR
something genuinely good that happened in the UK in the last 24 hours (only if you
can verify it at primary source — you cannot search, so use the motivational or Ola
angle). No figure needed.

**Come to Ola Accountancy / Vino la Ola Accountancy** — the acquisition slot.
Opens on WHAT THE READER GAINS by being with us: one fixed monthly fee, we handle
the handover and write the professional clearance letter, the free 30 minutes,
someone who actually answers. A deadline may appear in the body as reassurance —
we watch the dates so you do not have to — NEVER as the opening threat.
**NO PENALTY FIGURE IN `hero` OR `punch`, EVER.** On our own account a penalty
figure reads as though WE issue it. Nothing that reads as a warning. We are
inviting someone in, not frightening them.

**Financial education with Ola Accountancy / Educatie financiara cu Ola Accountancy**
— every figure and every exclusion stays, but write the way a good teacher explains
something to someone they like. A sentence that opens a door, not a line off a form.
Warmth and rhythm, varied sentence lengths, no jargon.

**Joke of the day / Gluma zilei** and **Joke of the evening / Gluma serii** — two
DIFFERENT labels, never the same one twice. They must be genuinely funny: the reader
recognises themselves or someone they know, in ONE beat, with no accounting knowledge
needed to get the laugh. The accounting point lands underneath, in `hook`. Everyday
business life is the richest source: the bag of receipts, "I'll do it next week", the
client who never pays, the phone ringing on 30 January. A joke that needs explaining
is replaced, not explained.

**Evening quote / Citatul serii** — a REAL quotation from a named philosopher or
thinker, `attrib` is the author's name alone, printed on the frame.
  - Only a quotation whose wording AND author you are certain of. An invented or
    misattributed quote is the same failure as an invented figure.
  - Authors long dead and in the public domain only. No living author.
  - It must speak to work, time, patience, discipline, money or building something.
  - Romanian sets carry the quotation translated faithfully into Romanian.
  - Your assigned author is in your own instructions. Do not use another.

## THE TWO WRITING RULES

**1. The first line may not lean on a name the reader does not know.** The scheme
name is the answer, not the hook. The first line carries the figure and what the
reader gets or loses; the scheme is named in the body.
  Not: "NHS Healthy Start. 4.65 a week from the 10th week of pregnancy."
  But: "9.30 a week for every child under one, and most parents never claim it."
Applies to `hero`, `punch`, `line`, the caption's opening sentence and the TikTok title.

**2. Ask for the save IN THE CAPTION, NEVER ON THE FRAME.** One line, immediately
before the disclaimer. VARY THE WORDING across your set. Ask for a SAVE when the post
carries a figure or date the reader will need again, a SHARE when the post is clearly
about somebody other than the reader. Never both in one caption. NEVER ask for a like.

## EVIDENCE — YOU DO NOT SEARCH

Every figure, date, threshold and condition comes from the bank entries you are handed
(your own JSON file). You do NOT open gov.uk. You do NOT search the web. A figure that
is not in your entry does not go on a frame. There is no card 2 to qualify a frame that
gets the nation, the band or the start date wrong.

**WHO DOES NOT GET IT GOES IN `sub`.** Every entry's `scope.excluded` is populated.
A post that states an entitlement without its exclusion overstates and does not ship.
A headline promising an amount MUST have the exclusion under it.

**THE NATION DOES NOT GO IN THE HERO.** If the scheme covers the whole UK, name no
nation at all. If it does not, the nation goes in `sub`. Read `scope.nation`.

## WRITE IT FOR SOMEONE WHO HAS NEVER HEARD OF ACCOUNTING

Name what the reader actually does: "you sold", "you add up your sales", "you tell
HMRC". Not "taxable turnover", "the look-back test", "comes into force". A term the
reader may not know is explained the first time or dropped. Say what it is NOT where
people get it wrong. One idea per frame. Accuracy is never traded for simplicity.

**SIMPLE IS NOT FLAT.** The first line is a person talking, not a notice. One concrete
person, one concrete number. Write the exclusions as help, not as a disclaimer. Keep
the ordinary word. Cut what nobody asked for. Read every frame aloud as if you were
the accountant saying it to a client across a desk; anything you would not say that
way is rewritten. Labels are parallel and neutral — "Excluded" is a label, "Not you"
is a verdict on the reader, and a verdict on the reader never goes on a frame.

## COMPLIANCE — NON-NEGOTIABLE

No guarantees. Never the word "chartered". No tax-avoidance suggestion. No client
details, no invented statistics, no testimonials. **The first consultation is FREE and
lasts 30 MINUTES** — never put a price on it. The financial consultation with the CEO
is GBP 420 incl. VAT, 60 minutes. No opinion on anybody's immigration or residency
situation — explaining a public fact is allowed, telling a reader what THEY should do
about THEIR status is not, and if you are unsure it crosses the line.

## THE SEASONAL WINDOW FOR 25 NOVEMBER 2026

Open and worth writing against: Black Friday is Friday 27 November and Cyber Monday
30 November (retail takings, record keeping, what is and is not a business expense);
the first Sunday of Advent is 29 November; Romania's national day is 1 December;
St Andrew's Day is 30 November; the Christmas run-up (staff parties, gifts, paying
staff early); winter proper; and underneath all of it the 31 January Self Assessment
deadline, now about nine weeks away. A seasonal joke must tie the occasion to a real
accounting point, not put a hat on the logo.

## THE CAPTIONS FILE

A JSON object keyed by post id. Each value:
  {"caption": "...", "ask": "...", "title": "..."}
  caption — the body. Opens on a hook, not a scheme name. No save/share ask inside it.
  ask     — the single save-or-share line, varied across your set.
  title   — a short TikTok / Pinterest title, same hook rule, under 90 characters.
Hashtags are added later by the orchestrator; do not put them in the caption.
Do not put the disclaimer in the caption; the orchestrator appends it.

## WHAT YOU DELIVER

1. /home/claude/ola-social-posts/night/2026-11-25/specs-<SET>.json   (the array)
2. /home/claude/ola-social-posts/night/2026-11-25/captions-<SET>.json (the object)
3. Assert every length limit IN CODE. Fix anything over. Re-assert.
4. Render:  cd /home/claude/ola-social-posts/pipeline/carousel
            python3 solo.py ../../night/2026-11-25/specs-<SET>.json ../../posts/2026-11-25/
5. **OPEN AT LEAST FOUR OF THE RENDERED IMAGES WITH THE Read TOOL AND LOOK AT THEM.**
   A render that exits 0 can still be unreadable. Only the eye catches copy that
   collides with the lion or runs off the bottom. If copy is tight, shorten and re-render.
6. Report back: the ids you wrote, one line each on what the post says, the longest
   field length per post, which four posts carry gold, and what you saw in the images.

Load the `ola-copywriter` skill if it is available to you.
