#!/usr/bin/env python3
"""Quality gates for the house format.

The first version of the frozen-frame test downscaled to 96x171 before
differencing, which washed out slow bokeh drift and reported a clip as
static when 10% of its pixels were still changing twice a second. It read
the house reference the same way. Measured at 540x960 instead, with
"frozen" defined as under 1% of pixels moving, it agrees with the eye.
"""
import sys, subprocess
import numpy as np
from scipy.signal import butter, lfilter

SR = 48000


def frozen_runs(path, fps=6, w=540, h=960, moved_pct=1.0):
    raw = subprocess.run(["ffmpeg", "-nostdin", "-v", "quiet", "-i", path,
                          "-vf", f"fps={fps},scale={w}:{h}",
                          "-f", "rawvideo", "-pix_fmt", "gray", "-"],
                         capture_output=True).stdout
    n = len(raw) // (w * h)
    d = np.frombuffer(raw[:n * w * h], dtype=np.uint8).reshape(n, h, w).astype(np.int16)
    moving = np.array([100 * (np.abs(d[i] - d[i - 1]) > 4).mean() for i in range(1, n)])
    frozen = moving < moved_pct
    longest = run = 0
    for f in frozen:
        run = run + 1 if f else 0
        longest = max(longest, run)
    return longest / fps, float(moving.min()), float(moving.mean())


def audio(path):
    x = np.frombuffer(subprocess.run(
        ["ffmpeg", "-nostdin", "-v", "quiet", "-i", path,
         "-af", "pan=mono|c0=0.5*c0+0.5*c1", "-ar", str(SR), "-f", "f32le", "-"],
        capture_output=True).stdout, dtype=np.float32)

    def f(kind, *a):
        wn = [v / (SR / 2) for v in a] if len(a) > 1 else a[0] / (SR / 2)
        b, a2 = butter(4, wn, btype=kind)
        return lfilter(b, a2, x)

    db = lambda v: 20 * np.log10(v + 1e-12)
    w = int(SR)
    env = np.array([np.sqrt((x[i:i + w] ** 2).mean()) for i in range(0, len(x) - w, w)])
    return (db(np.sqrt((f('band', 300, 3400) ** 2).mean())),
            db(np.sqrt((f('low', 120) ** 2).mean())),
            db(np.sqrt((f('high', 500) ** 2).mean())),
            float(np.sqrt((f('high', 5000) ** 2).mean())),
            db(env.max()) - db(env.min()))


hdr = f"{'clip':10} {'dur':>6} {'frozen':>8} {'min mov':>8} | {'300-3400':>9} {'<120':>7} {'>500':>7} {'HF':>8} {'range':>7}  verdict"
print(hdr)
print("-" * len(hdr))
for p in sys.argv[1:]:
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                "-of", "csv=p=0:nk=1", p], capture_output=True, text=True).stdout.strip())
    fr, mn, mean = frozen_runs(p)
    b, lo, hi, hf, rng = audio(p)
    ok = (fr <= 2.0 and -22 <= b <= -14 and lo <= b - 13 and hf < 0.004)
    print(f"{p.split('/')[-1][:10]:10} {dur:5.1f}s {fr:7.2f}s {mn:7.1f}% | "
          f"{b:9.1f} {lo:7.1f} {hi:7.1f} {hf:8.5f} {rng:6.1f}dB  {'PASS' if ok else 'CHECK'}")
