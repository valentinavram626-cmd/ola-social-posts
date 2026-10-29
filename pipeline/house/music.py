#!/usr/bin/env python3
"""Original score for the house format.

Written to the profile measured from Valentin's own professionally edited
reference clip, because that is the only target that matters:

    voice/music band 300-3400 Hz   about -17 dBFS
    everything below 120 Hz        at least 15 dB under that
    above 500 Hz                   about -18 to -20 dBFS
    level range across the clip    8-12 dB, so it develops

The reels this replaces had their strongest tones at 43-55 Hz and sat at
-25 dBFS above 500 Hz: inaudible on a phone. Everything here is synthesised
from oscillators and filtered noise, so there is nothing to licence.

Usage: music.py <seconds> <out.wav> [key] [seed]
"""
import sys
import numpy as np
from scipy.signal import butter, lfilter
from scipy.io import wavfile

SR = 48000


def lp(x, hz, o=4):
    b, a = butter(o, hz / (SR / 2), btype="low")
    return lfilter(b, a, x)


def hp(x, hz, o=4):
    b, a = butter(o, hz / (SR / 2), btype="high")
    return lfilter(b, a, x)


def bp(x, lo, hi, o=4):
    b, a = butter(o, [lo / (SR / 2), hi / (SR / 2)], btype="band")
    return lfilter(b, a, x)


def note(semitones_from_a4, octave_shift=0):
    return 440.0 * (2 ** ((semitones_from_a4 + 12 * octave_shift) / 12))


# A natural minor, degrees as semitone offsets from A
SCALE = [0, 2, 3, 5, 7, 8, 10]
# i - VI - III - VII, the workhorse progression: melancholy but moving
PROG = [
    [0, 3, 7],      # Am
    [-4, 0, 3],     # F
    [3, 7, 10],     # C
    [-2, 2, 5],     # G
]


def adsr(n, a, d, s, r):
    a, d, r = int(a * SR), int(d * SR), int(r * SR)
    sus = max(0, n - a - d - r)
    return np.concatenate([
        np.linspace(0, 1, a, endpoint=False),
        np.linspace(1, s, d, endpoint=False),
        np.full(sus, s),
        np.linspace(s, 0, r),
    ])[:n]


def build(dur, key_shift=0, seed=7):
    rng = np.random.default_rng(seed)
    n = int(SR * dur)
    t = np.arange(n) / SR

    bpm = 90.0
    beat = 60.0 / bpm
    bar = beat * 4

    pad = np.zeros(n)
    pluck = np.zeros(n)
    bass = np.zeros(n)
    pulse = np.zeros(n)

    n_bars = int(np.ceil(dur / bar))

    for b in range(n_bars):
        chord = PROG[b % len(PROG)]
        t0 = b * bar
        i0 = int(t0 * SR)
        ln = min(int(bar * SR * 1.06), n - i0)
        if ln <= 0:
            break
        tt = np.arange(ln) / SR

        # --- pad: the chord, sat in the band a phone reproduces ---
        env = adsr(ln, 0.35, 0.5, 0.75, 0.6)
        voice = np.zeros(ln)
        for j, deg in enumerate(chord):
            f = note(deg + key_shift, 0)          # around 440 Hz, mid-range on purpose
            det = 1 + 0.0018 * np.sin(2 * np.pi * (0.11 + 0.03 * j) * tt)
            voice += (0.52 / (j + 1.35)) * np.sin(2 * np.pi * f * det * tt)
            voice += (0.17 / (j + 1.35)) * np.sin(2 * np.pi * f * 2 * det * tt)
        pad[i0:i0 + ln] += bp(voice, 220, 2600) * env

        # --- bass: root, deliberately quiet and high-passed later ---
        fb = note(chord[0] + key_shift, -2)
        benv = adsr(ln, 0.02, 0.25, 0.55, 0.5)
        bass[i0:i0 + ln] += np.sin(2 * np.pi * fb * tt) * benv

    # --- melody: chord tones, a simple rhythmic motif that repeats and lifts ---
    motif = [0, 2, 4, 2, 5, 4, 2, 0]          # indices into the scale
    step = beat / 2
    k = 0
    while k * step < dur - 0.4:
        bar_i = int((k * step) // bar)
        chord = PROG[bar_i % len(PROG)]
        deg = SCALE[motif[k % len(motif)] % len(SCALE)]
        octave = 1 if (k // len(motif)) % 2 else 0
        f = note(chord[0] + deg + key_shift, octave)
        i0 = int(k * step * SR)
        ln = min(int(0.55 * SR), n - i0)
        if ln > 0:
            tt = np.arange(ln) / SR
            e = np.exp(-tt * 7.5)
            v = (np.sin(2 * np.pi * f * tt)
                 + 0.34 * np.sin(2 * np.pi * f * 2 * tt)
                 + 0.14 * np.sin(2 * np.pi * f * 3.01 * tt))
            # every other note softer, so the motif has a shape
            amp = 1.0 if k % 2 == 0 else 0.62
            pluck[i0:i0 + ln] += v * e * amp
        k += 1

    # --- pulse: a transient on each beat. Transients are what read as rhythm ---
    k = 0
    while k * beat < dur:
        i0 = int(k * beat * SR)
        ln = min(int(0.09 * SR), n - i0)
        if ln > 0:
            e = np.exp(-np.linspace(0, 9, ln))
            pulse[i0:i0 + ln] += rng.standard_normal(ln) * e * (0.9 if k % 4 == 0 else 0.45)
        k += 1
    pulse = bp(pulse, 1200, 5000)

    # --- arrangement: sparse in, full in the middle, settle at the end ---
    k = t / dur
    rise = np.clip(k / 0.30, 0, 1)                       # first third builds
    fall = 1 - np.clip((k - 0.80) / 0.20, 0, 1) * 0.45   # last fifth eases back
    shape = rise * fall

    mix = (0.52 * pad * (0.55 + 0.45 * shape)
           + 0.40 * pluck * shape
           + 0.26 * pulse * np.clip((k - 0.12) / 0.2, 0, 1) * fall
           + 0.30 * bass)

    # Keep the bottom where a phone can ignore it without the mix falling apart.
    mix = hp(mix, 150)
    mix += 0.30 * bp(mix, 900, 3200)      # lift presence, the band phones favour

    fi, fo = int(0.5 * SR), int(1.1 * SR)
    mix[:fi] *= np.linspace(0, 1, fi)
    mix[-fo:] *= np.linspace(1, 0, fo)

    # Calibrate on BAND energy, not on peak, and never with a loudness
    # normaliser: loudnorm flattened an 8 dB arc to 3.5 dB in testing, which
    # removes the development the arrangement exists for.
    target_dbfs = -17.5                      # the reference clip's music band
    cur = np.sqrt((bp(mix, 300, 3400) ** 2).mean())
    gain = (10 ** (target_dbfs / 20)) / (cur + 1e-12)
    mix = mix * gain
    peak = np.abs(mix).max()
    if peak > 0.94:                          # headroom, no limiter, no pumping
        mix = mix * (0.94 / peak)
    return mix.astype(np.float32)


def main():
    dur = float(sys.argv[1])
    out = sys.argv[2]
    key = int(sys.argv[3]) if len(sys.argv) > 3 else 0
    seed = int(sys.argv[4]) if len(sys.argv) > 4 else 7
    m = build(dur, key, seed)
    st = np.stack([m, m], axis=1)
    wavfile.write(out, SR, (st * 32767).astype(np.int16))

    db = lambda v: 20 * np.log10(v + 1e-12)
    w = int(SR * 1.0)
    env = np.array([np.sqrt((m[i:i + w] ** 2).mean()) for i in range(0, len(m) - w, w)])
    print(f"{out}: {dur:.1f}s")
    print(f"  300-3400Hz {db(np.sqrt((bp(m,300,3400)**2).mean())):6.1f} dBFS   (target ~ -17)")
    print(f"  <120Hz     {db(np.sqrt((lp(m,120)**2).mean())):6.1f} dBFS   (target >=15 dB under)")
    print(f"  >500Hz     {db(np.sqrt((hp(m,500)**2).mean())):6.1f} dBFS   (target -18..-20)")
    print(f"  range      {db(env.max())-db(env.min()):6.1f} dB      (target 8-12)")


if __name__ == "__main__":
    main()
