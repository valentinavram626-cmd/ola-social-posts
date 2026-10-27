# Halloween reel engine

Canvas-rendered 9:16 reels. No AI generation, no stock, no licensed audio —
every frame and every sample is produced here, so these cost zero credits
and carry no third-party rights.

    node render.js deadline.json      # -> fr-deadline/*.jpg  (30 fps)
    python3 bed.py                    # -> bed.wav  (original ambient bed)
    ffmpeg -framerate 30 -i fr-deadline/f%05d.jpg -i bed-n.wav \
           -c:v libx264 -crf 19 -pix_fmt yuv420p -c:a aac -shortest out.mp4

`hw.html` draws the background, the carved lantern, the embers and the
type. `<config>.json` holds `total`, `outdir`, `beats` and `end`.

Beat fields: `text`, `in`, `out`, `size`, `hi` (word drawn in brass),
`ember` (draw `hi` in pumpkin orange instead).

## Checks worth repeating

* Type must not orphan a word on its own line — measure at 860px max
  width and pick a size that breaks cleanly, or split the beat in two.
* Keep audible energy above 500 Hz: a bed that lives in the sub is
  inaudible on a phone speaker. Target about -23 dBFS RMS high-passed
  at 500 Hz.
* High-frequency RMS should sit near -55 dBFS. Anything an order of
  magnitude above that reads as hiss.

## Facts used in deadline.json

Verified against gov.uk and LITRG on 27 Oct 2026:
paper Self Assessment return for 2025/26 is due 23:59 on 31 Oct 2026;
online return and payment are due 31 Jan 2027; missing the paper
deadline but filing online by 31 Jan avoids the £100 penalty.
