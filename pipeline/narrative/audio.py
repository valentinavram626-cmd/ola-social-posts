#!/usr/bin/env python3
"""Build the mix for one narrative story.

    python3 audio.py --build-dir build/<slug>

Voice + original synthesized music + SFX.  Two rules that must never be broken:
  * SFX live ONLY inside the pauses between phrases — asserted at interval and
    at sample level, so nothing can ever talk over Valentin.
  * the whoosh is heavily low-passed (dark, no sibilance).  It used to be raw
    white noise and it hissed; do not take the filter out.
"""
import json, wave, math, os, subprocess, argparse
import numpy as np

sr = 44100
PAD = 0.15          # safety margin around every spoken phrase
PEAK_MAX = 0.95


def rd(fn):
    out = subprocess.run(['ffmpeg', '-nostdin', '-v', 'error', '-i', fn,
                          '-f', 'f32le', '-ac', '1', '-ar', str(sr), '-'],
                         capture_output=True).stdout
    return np.frombuffer(out, dtype=np.float32)


def put(buf, sig, t, gain=1.0):
    i = int(t * sr)
    if i < 0:
        sig = sig[-i:]; i = 0
    n = min(len(sig), len(buf) - i)
    if n > 0:
        buf[i:i + n] += sig[:n] * gain


def envl(n, a, r):
    e = np.ones(n); A = int(a * sr); R = int(r * sr)
    if A > 0: e[:A] = np.linspace(0, 1, A)
    if R > 0: e[-R:] *= np.linspace(1, 0, R)
    return e


def n2f(n):
    return 440 * 2 ** ((n - 69) / 12)


def tone(f, n, kind='pad'):
    t = np.arange(n) / sr
    if kind == 'pad':
        s = (np.sin(2 * np.pi * f * t) + 0.45 * np.sin(2 * np.pi * f * 2 * t + 0.3)
             + 0.2 * np.sin(2 * np.pi * f * 3 * t))
        s *= (1 + 0.06 * np.sin(2 * np.pi * 0.5 * t))
        return s / 1.65
    if kind == 'bell':
        return ((np.sin(2 * np.pi * f * t) + 0.4 * np.sin(2 * np.pi * f * 2.01 * t)
                 + 0.2 * np.sin(2 * np.pi * f * 3.0 * t)) * np.exp(-t * 2.4))
    return (np.sin(2 * np.pi * f * t) + 0.3 * np.sin(2 * np.pi * f * 2 * t)) * np.exp(-t * 6)


def lp(x, hz):
    try:
        from scipy.signal import butter, lfilter
        b, a = butter(4, hz / (sr / 2))
        return lfilter(b, a, x)
    except Exception:
        al = math.exp(-2 * math.pi * hz / sr); z = 0.0
        out = np.empty_like(x)
        for i in range(len(x)):
            z = al * z + (1 - al) * x[i]; out[i] = z
        return out


def build(build_dir):
    TL = json.load(open(os.path.join(build_dir, 'timeline.json'), encoding='utf8'))
    PH, SC, TOTAL = TL['phrases'], TL['scenes'], TL['total']
    N = int(TOTAL * sr)

    # ---- voice (peak-normalised per phrase so takes of different level sit evenly)
    voice = np.zeros(N, dtype=np.float32)
    for p in PH:
        v = rd(p['voice'])
        pk = float(np.abs(v).max()) or 1.0
        put(voice, v * (0.9 / pk), p['start'])

    # ---- music: C–G–Am–F pad with a soft pulse, resolving to C at the end card
    CH = [[60, 64, 67], [55, 59, 62], [57, 60, 64], [53, 57, 60]]
    music = np.zeros(N, dtype=np.float32)
    bar, t, k = 3.2, 0.0, 0
    RESOLVE = SC[-1]['start']
    while t < TOTAL:
        ch = CH[k % 4] if t < RESOLVE - 0.2 else CH[0]
        n = int(bar * sr * 1.3)
        for i, nn in enumerate(ch):
            s = tone(n2f(nn - 12 if i == 0 else nn), n) * envl(n, 0.9, 1.4) * (0.15 if i == 0 else 0.10)
            put(music, s, t)
        for b in (0, bar / 2):
            put(music, tone(n2f(ch[0]), int(0.6 * sr), 'pluck') * 0.05, t + b)
        t += bar; k += 1
    for j, nn in enumerate([72, 76, 79, 84, 88, 91]):
        put(music, tone(n2f(nn), int(2.5 * sr), 'bell') * 0.05, RESOLVE + 0.1 + j * 0.2)
    music = lp(music, 1600).astype(np.float32)

    # ---- SFX bank
    rng = np.random.default_rng(7)

    def whoosh(d=0.45, gain=0.22):
        n = int(d * sr); tt = np.arange(n) / sr
        noise = lp(rng.standard_normal(n), 700)          # dark: keep it this way
        noise /= (np.abs(noise).max() + 1e-9)
        return (noise * envl(n, 0.18, 0.3) * (gain * 0.18) * np.sin(np.pi * tt / d)).astype(np.float32)

    def tick(gain=0.12, f=1800, d=0.05):
        n = int(d * sr); tt = np.arange(n) / sr
        return (np.sin(2 * np.pi * f * tt) * np.exp(-tt * 90) * gain).astype(np.float32)

    def thud(gain=0.4):
        n = int(0.3 * sr); tt = np.arange(n) / sr
        return (np.sin(2 * np.pi * (110 - 60 * tt) * tt) * np.exp(-tt * 11) * gain).astype(np.float32)

    def ding(gain=0.35, note=88, d=1.2):
        return (tone(n2f(note), int(d * sr), 'bell') * gain).astype(np.float32)

    def sparkle(gain=0.22):
        out = np.zeros(int(0.9 * sr), dtype=np.float32)
        for j, nn in enumerate([84, 88, 91, 96]):
            put(out, tone(n2f(nn), int(0.5 * sr), 'bell') * gain, j * 0.09)
        return out

    def pop(gain=0.3):
        n = int(0.12 * sr); tt = np.arange(n) / sr
        return (np.sin(2 * np.pi * (520 - 300 * tt) * tt) * np.exp(-tt * 40) * gain).astype(np.float32)

    def oops(gain=0.3):
        out = np.zeros(int(0.5 * sr), dtype=np.float32)
        put(out, tone(n2f(69), int(0.35 * sr), 'pluck') * gain, 0.0)
        put(out, tone(n2f(64), int(0.4 * sr), 'pluck') * gain, 0.16)
        return out

    def uplift(gain=0.3):                       # small rising two-note "ta-daa"
        out = np.zeros(int(0.8 * sr), dtype=np.float32)
        put(out, tone(n2f(72), int(0.5 * sr), 'bell') * gain, 0.0)
        put(out, tone(n2f(79), int(0.7 * sr), 'bell') * gain, 0.18)
        return out

    ONE = {'tick': tick, 'thud': thud, 'ding': ding, 'pop': pop, 'oops': oops,
           'sparkle': sparkle, 'uplift': uplift, 'whoosh': whoosh}

    gaps = {}
    for i, p in enumerate(PH):
        gs = p['end'] + PAD
        ge = (PH[i + 1]['start'] - PAD) if i + 1 < len(PH) else TOTAL
        gaps[i] = (gs, ge)
    intervals = [(p['start'] - PAD, p['end'] + PAD) for p in PH]

    sfx = np.zeros(N, dtype=np.float32)
    placed = []

    def place(name, sig, i, offset=0.0, align='start'):
        """Put sig inside the pause after phrase i.  Truncated with a fast fade if
        it does not fit, dropped if the pause is too short."""
        gs, ge = gaps[i]
        ge -= 0.01                      # never butt right up against the next phrase
        if ge - gs < 0.12:
            placed.append((name, i, None, 'dropped: no gap')); return
        d = len(sig) / sr
        t0 = max(gs, gs + offset if align == 'start' else ge - d - offset)
        avail = ge - t0
        if avail < 0.08:
            placed.append((name, i, None, 'dropped: no room')); return
        if d > avail:
            n = int(avail * sr); sig = sig[:n] * envl(n, 0, min(0.06, avail / 2)); d = avail
        put(sfx, sig, t0); placed.append((name, i, round(t0, 3), round(t0 + d, 3)))

    # per-scene signature sounds, in the pause after the scene's first phrase
    for j, s in enumerate(SC):
        i0, name = s['from'], s['name']
        if j > 0 and i0 > 0:                     # scene change: whoosh landing on the cut
            place('whoosh', whoosh(), i0 - 1, 0.0, 'end')
        if name == 'receipts':
            for q in range(5): place('tick-receipt', tick(), i0, 0.05 + q * 0.11)
        elif name == 'calendar':
            for q in range(6): place('tick-month', tick(0.09, 1400), i0, 0.02 + q * 0.09)
        elif name == 'stairs':
            place('sparkle', sparkle(), i0, 0.0)
        elif name == 'penalty':
            place('thud', thud(), i0, 0.05); place('thud', thud(0.3), i0, 0.45)
        elif name == 'bignum':
            place('ding', ding(), i0, 0.05)
        elif name == 'question':
            place('pop', pop(), i0, 0.05); place('pop', pop(0.25), i0, 0.4)
        elif name == 'ola':
            place('pop-lion', pop(0.35), i0, 0.1)
        elif name == 'whatsapp':
            place('whoosh-end', whoosh(0.8, 0.16), i0, 0.1)

    # per-phrase overrides from the story's scene_plan ("sfx": "oops")
    for p in PH:
        tag = p.get('sfx')
        if tag and tag in ONE:
            place(tag, ONE[tag](), p['i'], 0.1)

    # ---- verification: no SFX anywhere near the voice
    print(f"{'sfx':14}{'after':>6}{'start':>9}{'end':>9}")
    overlaps = 0
    for name, i, a, b in placed:
        print(f'{name:14}{i:>6}{str(a):>9}{str(b):>9}')
        if a is None:
            continue
        for (vs, ve) in intervals:
            if a < ve and b > vs:
                overlaps += 1; print('   OVERLAP with voice', vs, ve)
    assert overlaps == 0, f'{overlaps} SFX overlap the voice'
    mask = np.zeros(N, dtype=bool)
    for (vs, ve) in intervals:
        mask[int(max(0, vs) * sr):int(min(TOTAL, ve) * sr)] = True
    assert float(np.abs(sfx[mask]).max()) == 0.0, 'SFX energy found under voice'
    print('overlap check: OK (0 overlaps, 0 SFX energy under voice)')

    # ---- mix: music ducks to 0.4 under speech and lifts back in the pauses
    duck = np.ones(N, dtype=np.float32)
    for p in PH:
        duck[int(max(0, p['start'] - 0.25) * sr):int(min(TOTAL, p['end'] + 0.3) * sr)] = 0.4
    kn = int(0.25 * sr)
    duck = np.convolve(duck, np.ones(kn) / kn, mode='same')
    mix = voice * 0.95 + music * duck * 0.9 + sfx * 0.8
    mix = np.tanh(mix * 1.1)
    mix[-int(1.2 * sr):] *= np.linspace(1, 0, int(1.2 * sr))
    peak = float(np.abs(mix).max())
    assert peak < PEAK_MAX, f'mix peak {peak:.3f} >= {PEAK_MAX}'
    st = np.stack([mix, mix], axis=1)
    out = os.path.join(build_dir, 'mix.wav')
    with wave.open(out, 'w') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr)
        w.writeframes((np.clip(st, -1, 1) * 32767).astype(np.int16).tobytes())
    print(f'mix.wav {TOTAL}s; peak {peak:.3f}')
    return out


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--build-dir', required=True)
    build(ap.parse_args().build_dir)
