#!/usr/bin/env python3
"""Gates for the carousel set. Measured, never eyeballed.

Two of these exist because the first build failed them:

  * en-bsky slide 5 had a three-line sentence, the centred content overflowed
    the frame, and the footer was pushed into the bottom margin. Shorten the
    copy; do not quietly shrink the type.
  * ro-tiktok put the footer at 84% of frame height, inside the area TikTok
    covers with the caption, and ran the swipe cue to 92% width, under the
    action rail. Tall frames need their own padding, not the feed's.
"""
from PIL import Image
import numpy as np, glob, os, sys

def lum(c):
    c = np.array(c[:3]) / 255.0
    c = np.where(c <= 0.03928, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126*c[0] + 0.7152*c[1] + 0.0722*c[2]

def ratio(a, b):
    la, lb = lum(a), lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)

PAIRS = {"white on ink": ((255,255,255), (10,14,24)),
         "gold on ink":  ((240,176,62),  (10,14,24)),
         "body on ink":  ((228,233,242), (10,14,24)),
         "note on ink":  ((140,152,174), (10,14,24)),
         "ink on WhatsApp": ((7,33,15),  (37,211,102))}

fails = []
print("CONTRAST")
for k, (f, b) in PAIRS.items():
    r = ratio(f, b)
    ok = r >= 4.5
    print(f"  {k:18s} {r:5.1f}:1  {'pass' if ok else 'FAIL'}")
    if not ok: fails.append(f"contrast {k}")

print("\nFRAMES")
print(f"  {'job':11s} {'n':>2s} {'size':11s} {'KB':>5s}  margins    platform-safe")
# Read the jobs off the disk rather than from a list. A hardcoded table goes
# stale the moment a job is added, and it goes stale SILENTLY: en-tiktok and the
# four solo renders arrived on 13 November 2026 and a fixed list would have
# gated none of them while still printing a clean pass.
for job in sorted(d[:-4] for d in os.listdir('.') if d.endswith('-out')):
    for f in sorted(glob.glob(f'{job}-out/*.png')):
        im = Image.open(f); W, H = im.size
        a = np.array(im.convert('L')).astype(int); bg = int(np.median(a))
        M = max(40, int(W * 0.05))
        edges = {'top': a[:M,:], 'bot': a[-M:,:], 'L': a[:,:M], 'R': a[:,-M:]}
        bad = [k for k, v in edges.items() if (np.abs(v-bg) > 60).mean() > 0.004]

        note = '—'
        if H / W > 1.5:                       # a 9:16 photo post
            # Only bright pixels count here. What matters is whether the
            # platform's chrome would cover something the viewer needs to
            # read; a dim background glow or the watermark behind the
            # headline can sit under the action rail without losing anything.
            lit = (a > 150)
            rows = lit.mean(axis=1)
            cols = lit.mean(axis=0)
            spill = []
            if rows[:int(H*0.10)].max()  > 0.02: spill.append('top')
            if rows[int(H*0.75):].max()  > 0.02: spill.append('caption')
            if cols[int(W*0.88):].max()  > 0.02: spill.append('rail')
            note = 'clear' if not spill else 'UNDER ' + ','.join(spill)
            if spill: fails.append(f"{job} {os.path.basename(f)} {note}")
        if bad: fails.append(f"{job} {os.path.basename(f)} ink in {','.join(bad)}")
        print(f"  {job:11s} {os.path.basename(f)[:2]:>2s} {W}x{H:<6d} "
              f"{os.path.getsize(f)/1024:5.0f}  "
              f"{'ok' if not bad else 'INK:'+','.join(bad):10s} {note}")

print("\nFAILURES:", len(fails))
for x in fails: print("  -", x)
sys.exit(1 if fails else 0)
