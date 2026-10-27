# Narrative reels — the story engine

One narrative reel a day, from one JSON file per story. Everything the reel is — the words,
the voice, the visuals, the sounds, the caption — comes out of `stories/<slug>.json`; nothing
is hand-built any more.

The reference reel this engine was generalised from is `reels/narrative/doi-romani.mp4`
("Doi români", 48.5 s). Same look, same sound design, same safe zone.

```
pipeline/narrative/
  stories/<slug>.json      the whole story (see "Writing a story")
  stories/<slug>-open.mp4  optional 5 s live-action opening plate (Higgsfield)
  build.py                 driver — one command per reel
  voice.py                 ElevenLabs narration, one take per phrase
  timeline.py              phrase + word timing from the real voice files, scene runs
  audio.py                 music + SFX, SFX only in the pauses
  render.js                canvas renderer (preview | frames | textonly | safe)
  page.html                the engine: scene primitives + kinetic captions
  build/<slug>/            working files (git-ignored)
→ reels/narrative/<slug>.mp4 + .jpg
```

## Build a reel

```bash
cd pipeline/narrative
ELEVENLABS_API_KEY=... python3 build.py cutia-de-pantofi
```

Steps, in order: voice → timeline → audio → frames → (optional live-action composite) → encode
→ poster. Roughly 6–8 minutes on 2 CPUs, most of it the ~1,600 canvas frames.

Useful flags and modes:

```bash
python3 build.py <slug> --skip-voice        # takes already in build/<slug>/voice/NN.wav
python3 build.py <slug> --preview-only      # stop after stills, for a quick look
node render.js build/<slug> preview 2,20,44 # stills at chosen seconds -> build/<slug>/prev/
node render.js build/<slug> safe            # assert no text leaves the safe zone
```

### Voice without an API key

If the session has the **ElevenLabs MCP connector** instead of a key (this is how the first
batch was made), generate the takes through it and drop them in `build/<slug>/voice/`:

* `creative_generate_speech`, one call per phrase, `generations_count=1`,
  `model_id=eleven_multilingual_v2`, `voice_id=4YZdCwbKGmetvWILgi8V` ("Valentin Voice").
* poll `creative_get_flow_run_status` until `all_completed`, take `content_url`,
* download and convert each one to `NN.wav`:

```bash
curl -sS -o NN.mp3 "<content_url>" </dev/null
ffmpeg -nostdin -y -i NN.mp3 -af \
 "silenceremove=start_periods=1:start_duration=0:start_threshold=-45dB:detection=peak,areverse,\
silenceremove=start_periods=1:start_duration=0:start_threshold=-45dB:detection=peak,areverse,\
loudnorm=I=-18:TP=-2" -ac 1 -ar 44100 NN.wav
```

In a bash loop over a file of URLs, read from a dedicated descriptor and keep stdin away from
the children, or the loop eats its own input:
`while read -r n url <&3; do … </dev/null; done 3< urls.txt`.

Then `python3 build.py <slug> --skip-voice`.

A story costs about 600 ElevenLabs credits (≈1 credit per character).

### Live-action opening

Drop a 5 s vertical clip at `stories/<slug>-open.mp4` and `build.py` composites it exactly the
way `ola-story-FINAL.mp4` was made: the canvas frames as the base, the clip on top with its
alpha faded out over 3.0 → 3.4 s, and the transparent text-only PNG overlay on top of both so
the caption and the Ola chrome stay readable over the footage. Without the file the reel opens
on the canvas and nothing else changes.

The clip is generated from the story's `opening_shot_prompt` in Higgsfield, which has to be
driven by a browser — it is not automatable from a headless session.

## Writing a story

```jsonc
{
  "slug": "cutia-de-pantofi",
  "title": "Ce spune cutia ta de bonuri despre tine",
  "phrases": ["...", "..."],            // 10–14 Romanian lines, ~600 characters in total
  "scene_plan": [                       // exactly one entry per phrase
    {"scene": "receipts", "args": {"box": true, "count": 7, "label": "cutia ta"},
     "warm": true, "sfx": "oops"}
  ],
  "question_card_text": ["Tu în ce", "categorie ești?"],
  "question_buttons": ["Plicuri", "Torpedou"],
  "brass": ["cutie", "cifrele"],        // extra words to set in brass in the caption
  "gaps": {"9": 1.4},                   // optional per-phrase pause override, seconds
  "opening_shot_prompt": "…",           // English, for Higgsfield
  "caption": "…",                       // Romanian, house style
  "hashtags": ["#bonuri", "…"]
}
```

* `warm: true` on a scene bathes the frame in the warm gold wash while it is on screen —
  use it on the good news, not the bad.
* `sfx` drops one comedy sound into the pause after that phrase:
  `oops tick thud ding pop sparkle uplift whoosh`.
* Numbers, `£`, `%` and the words in `brass` are set in brass automatically.
* Consecutive phrases with the same scene **and the same args** share one scene run, so the
  animation carries across them instead of restarting. Change an arg to restart it.

### Scene primitives

| scene | what it draws | args |
|---|---|---|
| `street` | people on a street, horizon, houses, a suitcase | `figures` (1–3), `houses`, `suitcase`, `bubble`, `labels[]` |
| `receipts` | receipts flying in and stacking (or landing in a heap) | `count`, `tidy` (false = mess), `box` (the shoebox), `warm`, `label` |
| `calendar` | calendar pages flipping | `count`, `label`, `sub` |
| `stairs` | ascending stairs/graph, a figure climbing, flag + confetti at the top | `steps`, `climb` (seconds), `label`, `amount` |
| `penalty` | amber penalty cards dropping in | `items[]` (1–3), `label` |
| `bignum` | one big typographic beat | `big`, `small`, `sub`, `size` |
| `question` | the on-screen question card (uses `question_card_text` / `question_buttons`) | — |
| `ola` | the Ola end card, lion + cities | — |
| `whatsapp` | the gold WhatsApp card + the consultation price | — |
| `plain` | caption only | — |

Data-driven text shrinks itself to fit, so a long `label` will not run out of the frame.

### Hard rules the code enforces

* **≤ 59 s.** Instagram rejects Story videos over 60 s. `timeline.py` asserts it before anything
  is rendered and `build.py` asserts it again on the finished file. Never speed the audio up —
  cut a phrase or shorten the wording. 13 phrases of ~50 characters lands around 53 s.
* **SFX never touch the voice.** `audio.py` places every sound inside a pause with a 0.15 s
  margin, truncates it if the pause is short, drops it if there is no room, and then asserts
  zero overlap at interval level *and* zero SFX energy under any voice interval.
* **Peak < 0.95.** Asserted on the mix.
* **Safe zone**: nothing right of x=850, below y=1440 or above y=170 — the whole composition is
  centred on x=455, not 540. `node render.js build/<slug> safe` walks the piece and fails with
  the offending timestamps.
* **The whoosh stays low-passed** (4th-order at 700 Hz). It was raw white noise once and hissed.

### Compliance

Every figure must be verified on GOV.UK the same night the reel is written; if it cannot be
verified, it does not go in the script. No guarantees, no "chartered", no invented clients or
testimonials, no promises of refunds. Prices exactly as on the site: first consultation £120
incl. VAT (30 min), financial consultation £420 incl. VAT (60 min). The WhatsApp line in
captions is `Scrie-ne pe WhatsApp la 0330 133 1886. Birouri în Luton și Birmingham.`
The on-screen disclaimer is drawn automatically over the end card.
