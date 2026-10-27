#!/usr/bin/env python3
"""Build timeline.json for one narrative story.

    python3 timeline.py <slug> [--voice-dir DIR] [--build-dir DIR]

Reads stories/<slug>.json + the generated voice files (NN.wav, one per phrase),
measures the real spoken length of every phrase and lays the story out on a
timeline: phrase starts/ends, per-word timings for the kinetic caption, and the
scene runs that drive the canvas.  Hard-asserts the Story cap (<= 59 s).
"""
import json, os, re, subprocess, sys, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
MAX_TOTAL = 59.0
MIN_PHRASES, MAX_PHRASES = 10, 14

# A pause is reserved after every phrase; the SFX live only inside these.
DEFAULT_GAP = 0.85
# A scene change needs a little more air, and some scenes need to breathe.
GAP_BEFORE_SCENE = {'bignum': 1.15, 'question': 1.0, 'penalty': 1.0, 'ola': 1.0}
TAIL = 3.4            # seconds of end card after the last phrase

# Words that always get the brass treatment, plus anything with a digit or £.
BRASS_ALWAYS = {
    'Ola', 'WhatsApp', 'HMRC', 'MTD', 'CIS', 'TVA', 'VAT', 'Ltd',
    'ianuarie', 'Ianuarie', 'aprilie', 'Aprilie', 'octombrie', 'Octombrie',
}


def dur(fn: str) -> float:
    out = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
                          '-of', 'csv=p=0', fn], capture_output=True, text=True).stdout.strip()
    if not out:
        raise SystemExit(f'ffprobe could not read {fn}')
    return float(out)


def core(tok: str) -> str:
    return tok.strip('.,!?„”"…:;()')


def build(slug: str, voice_dir: str, build_dir: str) -> dict:
    story = json.load(open(os.path.join(HERE, 'stories', f'{slug}.json'), encoding='utf8'))
    phrases, plan = story['phrases'], story['scene_plan']
    assert MIN_PHRASES <= len(phrases) <= MAX_PHRASES, \
        f'{slug}: {len(phrases)} phrases, expected {MIN_PHRASES}-{MAX_PHRASES}'
    assert len(plan) == len(phrases), \
        f'{slug}: scene_plan has {len(plan)} entries for {len(phrases)} phrases'

    brass = BRASS_ALWAYS | set(story.get('brass', []))
    brass_lc = {b.lower() for b in brass}
    gaps = {int(k): float(v) for k, v in story.get('gaps', {}).items()}

    P = []
    for i, text in enumerate(phrases):
        fn = os.path.join(voice_dir, f'{i:02d}.wav')
        if not os.path.exists(fn):
            raise SystemExit(f'missing voice file {fn} — run the voice step first')
        P.append({'i': i, 'text': text, 'voice': os.path.abspath(fn), 'dur': round(dur(fn), 3)})

    t = 0.8
    for i, p in enumerate(P):
        p['start'] = round(t, 3)
        p['end'] = round(t + p['dur'], 3)
        toks = p['text'].split()
        # crude but stable per-word timing: weight by length, pay extra at punctuation
        w = [len(core(x)) + (2.2 if x[-1] in '.!?”…' else (1.0 if x[-1] in ',:;' else 0)) for x in toks]
        tot = sum(w) or 1
        acc = 0.0
        words = []
        for x, wi in zip(toks, w):
            s = t + p['dur'] * acc / tot
            acc += wi
            e = t + p['dur'] * acc / tot
            c = core(x)
            is_brass = (c in brass) or (c.lower() in brass_lc) or bool(re.search(r'[\d£%]', c))
            words.append({'w': x, 's': round(s, 3), 'e': round(e, 3), 'brass': is_brass})
        p['words'] = words
        p['scene'] = plan[i]['scene']
        if plan[i].get('sfx'):
            p['sfx'] = plan[i]['sfx']          # one-off comedy sound in the pause after this phrase
        nxt = plan[i + 1]['scene'] if i + 1 < len(plan) else None
        gap = gaps.get(i, GAP_BEFORE_SCENE.get(nxt, DEFAULT_GAP) if nxt else 0.0)
        p['gap'] = round(gap, 3)
        t = p['end'] + gap

    TOTAL = round(t + TAIL, 2)
    assert TOTAL <= MAX_TOTAL, (
        f'{slug}: {TOTAL}s exceeds the {MAX_TOTAL}s Story cap — cut a phrase or '
        f'shorten the wording (never speed the audio up)')

    # merge consecutive phrases that share a scene into scene runs
    scenes = []
    for i, p in enumerate(P):
        entry = plan[i]
        same = (scenes and scenes[-1]['name'] == entry['scene']
                and scenes[-1]['args'] == entry.get('args', {}))
        if same:
            scenes[-1]['to'] = i
        else:
            scenes.append({'name': entry['scene'], 'args': entry.get('args', {}),
                           'warm': bool(entry.get('warm')), 'from': i, 'to': i})
    for j, s in enumerate(scenes):
        s['start'] = round(max(0.0, P[s['from']]['start'] - 0.35), 3)
        s['end'] = round(P[scenes[j + 1]['from']]['start'] - 0.35 if j + 1 < len(scenes) else TOTAL, 3)

    q = story.get('question_card_text') or []
    if isinstance(q, str):
        q = [q]
    tl = {
        'slug': slug,
        'title': story.get('title', slug),
        'phrases': P,
        'scenes': scenes,
        'total': TOTAL,
        'question': {'text': q, 'buttons': story.get('question_buttons', ['Da', 'Nu'])},
        'voice_dir': os.path.abspath(voice_dir),
    }
    os.makedirs(build_dir, exist_ok=True)
    json.dump(tl, open(os.path.join(build_dir, 'timeline.json'), 'w', encoding='utf8'),
              ensure_ascii=False, indent=1)
    return tl


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('slug')
    ap.add_argument('--voice-dir', default=None)
    ap.add_argument('--build-dir', default=None)
    a = ap.parse_args()
    build_dir = a.build_dir or os.path.join(HERE, 'build', a.slug)
    voice_dir = a.voice_dir or os.path.join(build_dir, 'voice')
    tl = build(a.slug, voice_dir, build_dir)
    print(f"{a.slug}: {len(tl['phrases'])} phrases, total {tl['total']}s "
          f"({len(tl['scenes'])} scene runs)")
    for p in tl['phrases']:
        print(f"  {p['i']:>2} {p['start']:>6.2f}-{p['end']:>6.2f} [{p['scene']:<9}] {p['text'][:52]}")


if __name__ == '__main__':
    main()
