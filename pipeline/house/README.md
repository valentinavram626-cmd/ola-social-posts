# House format

Built 29 Oct 2026, after Valentin rejected the 15-a-day slide format:
"prefer 5 bune pe zi decat 15 proaste."

Every number below was measured, not guessed. The targets come from his own
professionally edited clip in `reels/reference/`.

## Pieces

* `house.html` — canvas renderer. Three modes: `full` (background + type),
  `bgonly` (background alone, where footage plays elsewhere in the timeline),
  `textonly` (transparent captions to overlay on footage).
* `render.js` — drives it frame by frame. Emits PNG with alpha in textonly
  mode, JPEG otherwise.
* `music.py` — original score. Chord bed, melodic motif, beat transients,
  arranged to build and settle.
* `qa.py` — the gates. Run before anything reaches Valentin.

## What the renderer does, and why

The background is a bokeh field — large soft discs at varying depth, drifting,
with a travelling light and film grain over the top. Radial gradients stand in
for lens blur. Without it the frame reads as a slide; with it, it reads as a
shot. The whole composition also pushes in slowly across the clip, so no frame
is ever truly still.

Captions follow the reference exactly: phrase-sized, about one change every
1.6 s, all caps in Anton, white with a hard dark outline so they survive any
background, centred at about 62% of frame height, one keyword per clip in the
accent colour.

## Audio targets, measured from the reference

    music/voice band 300-3400 Hz   -17 to -21 dBFS
    below 120 Hz                   at least 15 dB under that
    above 500 Hz                   -18 to -21 dBFS
    level range across the clip    8-12 dB

The reels this replaced had their strongest tones at 43-55 Hz and sat 9.5 dB
louder below 120 Hz than in their own music band — inaudible on a phone.

`music.py` calibrates on band energy, never with a loudness normaliser:
loudnorm flattened an 8 dB arc to 3.5 dB in testing, removing the development
the arrangement exists for.

## Gate calibration, and one mistake worth recording

The first frozen-frame test downscaled to 96x171 before differencing. That
washed out slow bokeh drift and reported clips as static while 10% of their
pixels were still changing twice a second — it failed the house reference too.
Measured at 540x960, with "frozen" meaning under 1% of pixels moving, it agrees
with the eye.

Two thresholds are conditional, not absolute:

* High-frequency energy above 5 kHz. A music-only clip sits near 0.002-0.004;
  anything higher is hiss. A clip carrying speech sits near 0.011-0.015,
  because consonants live up there. Valentin's own recorded voice measures
  0.011 at the same speech level; the ElevenLabs clone measures 0.017-0.019,
  so it gets a 3.5 dB shelf off the top. Matching the reference exactly would
  take 26 dB and leave the voice muffled — that is the wrong thing to chase,
  since the reference was a lapel mic outdoors.
* Longest frozen interval. Two seconds is the rule for built clips. Continuous
  footage carries much longer gaps: the reference holds 7.7 s between caption
  changes and never loses the viewer, because the image itself keeps moving.

## Measuring audio

Always downmix with `pan=mono|c0=0.5*c0+0.5*c1`. Plain `-ac 1` sums the
channels without attenuation, adds about 3 dB and can clip the measurement.
