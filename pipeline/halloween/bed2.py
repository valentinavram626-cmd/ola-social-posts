#!/usr/bin/env python3
"""Original ambient bed for the Halloween reel.

Everything here is synthesised from scratch (numpy oscillators + filtered
noise), so there is no third-party audio and nothing to licence.
Deliberately restrained: a low minor drone, a slow pulse, soft ember
crackle and three brass-ish bell taps that land on the beat changes.
"""
import numpy as np
from scipy.signal import butter, lfilter
from scipy.io import wavfile

SR = 48000
DUR = 27.0
N = int(SR * DUR)
t = np.arange(N) / SR
rng = np.random.default_rng(20261031)


def lp(x, hz, order=4):
    b, a = butter(order, hz / (SR / 2), btype="low")
    return lfilter(b, a, x)


def bp(x, lo, hi, order=4):
    b, a = butter(order, [lo / (SR / 2), hi / (SR / 2)], btype="band")
    return lfilter(b, a, x)


def adsr(n, a, d, s_lvl, r):
    """Simple ADSR as a sample-accurate envelope."""
    a, d, r = int(a * SR), int(d * SR), int(r * SR)
    s = max(0, n - a - d - r)
    return np.concatenate([
        np.linspace(0, 1, a, endpoint=False),
        np.linspace(1, s_lvl, d, endpoint=False),
        np.full(s, s_lvl),
        np.linspace(s_lvl, 0, r),
    ])[:n]


# ---- 1. drone: A minor-ish stack, slightly detuned for movement ----
drone = np.zeros(N)
for f, g in [(55.0, 0.50), (82.5, 0.26), (110.0, 0.20), (164.8, 0.09), (220.0, 0.05)]:
    det = 1 + 0.0016 * np.sin(2 * np.pi * 0.07 * t + f)
    drone += g * np.sin(2 * np.pi * f * det * t)
# slow breathing so it never sits still
drone *= 0.72 + 0.28 * np.sin(2 * np.pi * 0.085 * t - 1.1)
drone = lp(drone, 900)

# ---- 2. heartbeat pulse, 72 bpm, felt more than heard ----
pulse = np.zeros(N)
bpm, beat = 72.0, 60.0 / 72.0
k = 0
while k * beat < DUR - 0.5:
    i = int(k * beat * SR)
    ln = int(0.30 * SR)
    env = np.exp(-np.linspace(0, 7, ln))
    tone = np.sin(2 * np.pi * 48 * np.arange(ln) / SR)
    amp = 0.38 if k % 2 == 0 else 0.22
    pulse[i:i + ln] += amp * tone * env
    k += 1
pulse = lp(pulse, 220)

# ---- 3. ember crackle: sparse filtered-noise ticks ----
crack = np.zeros(N)
for _ in range(70):
    i = rng.integers(0, N - 2400)
    ln = int(rng.integers(140, 900))
    env = np.exp(-np.linspace(0, rng.uniform(5, 11), ln))
    crack[i:i + ln] += rng.standard_normal(ln) * env * rng.uniform(0.05, 0.22)
crack = bp(crack, 1800, 5200) * 0.30

# ---- 4. air: very quiet filtered noise so the mix has a floor ----
air = bp(rng.standard_normal(N), 260, 2200) * 0.020

# ---- 5. bell taps on the key beat changes ----
bells = np.zeros(N)
for when, g in [(0.4, 0.26), (4.3, 0.30), (9.7, 0.30), (15.1, 0.30), (20.5, 0.26), (23.8, 0.34)]:
    i = int(when * SR)
    ln = min(int(3.2 * SR), N - i)
    if ln <= 0:
        continue
    tt = np.arange(ln) / SR
    v = np.zeros(ln)
    # inharmonic partials -> struck metal rather than a sine
    for f, a, dec in [(523.3, 1.0, 2.2), (1046.5, 0.42, 3.1),
                      (1398.0, 0.21, 4.0), (2093.0, 0.12, 5.2)]:
        v += a * np.sin(2 * np.pi * f * tt) * np.exp(-tt * dec)
    v *= adsr(ln, 0.004, 0.05, 0.75, 1.4)
    bells[i:i + ln] += v * g

# ---- 6. mid pad so phone speakers have something to reproduce ----
# Phone speakers roll off hard below ~500 Hz, so a bed that lives in the
# sub is a bed nobody hears. This sits in the vocal band on purpose.
pad = np.zeros(N)
for f, g in [(392.0, 0.30), (466.2, 0.26), (587.3, 0.22), (783.9, 0.14)]:
    vib = 1 + 0.0022 * np.sin(2 * np.pi * 0.19 * t + f)
    pad += g * np.sin(2 * np.pi * f * vib * t)
pad *= 0.55 + 0.45 * np.sin(2 * np.pi * 0.062 * t - 0.4)
pad = bp(pad, 240, 1800) * 0.9

# Balance by audibility, not by level: the low end is felt, the mid is heard.
mix = (0.16 * drone + 0.13 * pulse + 0.34 * pad
       + 0.70 * crack + 0.55 * bells + air)

# trim the inaudible sub and tilt a little brightness back in
mix = mix - lp(mix, 42)                       # high-pass ~42 Hz
mix = mix + 0.10 * bp(mix, 1500, 4200)        # presence tilt, kept below hiss

# gentle duck under the end card so the CTA reads clean
duck = np.ones(N)
s = int(23.8 * SR)
duck[s:] = np.linspace(1.0, 0.70, N - s)
mix *= duck

# fade in / out
fi, fo = int(1.2 * SR), int(1.6 * SR)
mix[:fi] *= np.linspace(0, 1, fi)
mix[-fo:] *= np.linspace(1, 0, fo)

# normalise to about -17 LUFS-ish by peak, leaving headroom
mix /= (np.abs(mix).max() + 1e-9)
mix *= 0.56

st = np.stack([mix, mix], axis=1)
wavfile.write("bed2.wav", SR, (st * 32767).astype(np.int16))
print(f"bed2.wav written: {DUR}s, peak {np.abs(mix).max():.3f}")
