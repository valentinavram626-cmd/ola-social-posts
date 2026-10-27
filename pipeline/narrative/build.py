#!/usr/bin/env python3
"""Build one narrative reel end to end.

    python3 build.py <slug> [--skip-voice] [--preview-only]

Steps
  1. voice      ElevenLabs take per phrase        -> build/<slug>/voice/NN.wav
  2. timeline   phrase + word timing, scene runs  -> build/<slug>/timeline.json
  3. audio      music + SFX in the pauses         -> build/<slug>/mix.wav
  4. render     canvas frames at 30 fps           -> build/<slug>/frames/
  5. composite  optional live-action opening      (stories/<slug>-open.mp4)
  6. encode                                       -> reels/narrative/<slug>.mp4 + .jpg

The opening plate is composited exactly the way ola-story-FINAL.mp4 was built:
base canvas frames, the live-action video on top with its alpha faded out over
3.0-3.4 s, and the transparent text-only PNG overlay on top of both so the
caption and the Ola chrome stay readable over the footage.
"""
import json, os, shutil, subprocess, sys, argparse

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..'))
OUT_DIR = os.path.join(REPO, 'reels', 'narrative')
FPS = 30
PLATE_END, PLATE_FADE = 3.4, 3.0      # live-action plate: full, then alpha fade 3.0 -> 3.4 s
MAX_TOTAL = 59.0


def run(cmd, **kw):
    print('+', ' '.join(str(c) for c in cmd))
    subprocess.run(cmd, check=True, **kw)


def probe(fn, entry='format=duration'):
    return subprocess.run(['ffprobe', '-v', 'error', '-show_entries', entry,
                           '-of', 'csv=p=0', fn], capture_output=True, text=True).stdout.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('slug')
    ap.add_argument('--skip-voice', action='store_true',
                    help='voice files are already in build/<slug>/voice/ (e.g. made via the MCP connector)')
    ap.add_argument('--preview-only', action='store_true', help='stop after stills')
    a = ap.parse_args()
    slug = a.slug

    story_path = os.path.join(HERE, 'stories', f'{slug}.json')
    if not os.path.exists(story_path):
        sys.exit(f'no story at {story_path}')
    build = os.path.join(HERE, 'build', slug)
    voice = os.path.join(build, 'voice')
    os.makedirs(voice, exist_ok=True)

    # 1 — voice
    if not a.skip_voice:
        run([sys.executable, os.path.join(HERE, 'voice.py'), slug, '--out', voice])
    missing = [i for i in range(len(json.load(open(story_path, encoding='utf8'))['phrases']))
               if not os.path.exists(os.path.join(voice, f'{i:02d}.wav'))]
    if missing:
        sys.exit(f'missing voice takes {missing} in {voice}')

    # 2 — timeline
    run([sys.executable, os.path.join(HERE, 'timeline.py'), slug,
         '--voice-dir', voice, '--build-dir', build])
    tl = json.load(open(os.path.join(build, 'timeline.json'), encoding='utf8'))
    assert tl['total'] <= MAX_TOTAL, f"{slug}: {tl['total']}s over the {MAX_TOTAL}s Story cap"

    # 3 — audio
    run([sys.executable, os.path.join(HERE, 'audio.py'), '--build-dir', build])

    if a.preview_only:
        run(['node', os.path.join(HERE, 'render.js'), build, 'preview',
             ','.join(str(round(p['start'] + 0.6, 1)) for p in tl['phrases'][::2])])
        print('preview stills in', os.path.join(build, 'prev'))
        return

    # 4 — canvas frames
    run(['node', os.path.join(HERE, 'render.js'), build, 'frames'])

    # 5 — optional live-action opening plate
    plate = os.path.join(HERE, 'stories', f'{slug}-open.mp4')
    frames = os.path.join(build, 'frames', 'f%05d.jpg')
    mix = os.path.join(build, 'mix.wav')
    os.makedirs(OUT_DIR, exist_ok=True)
    mp4 = os.path.join(OUT_DIR, f'{slug}.mp4')

    if os.path.exists(plate):
        run(['node', os.path.join(HERE, 'render.js'), build, 'textonly', str(PLATE_END)])
        txt = os.path.join(build, 'textonly', 't%05d.png')
        fc = (
            f'[1:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,'
            f'trim=0:{PLATE_END},setpts=PTS-STARTPTS,fps={FPS},format=yuva420p,'
            f'fade=t=out:st={PLATE_FADE}:d={PLATE_END - PLATE_FADE}:alpha=1[plate];'
            f'[0:v][plate]overlay=0:0:eof_action=pass[b];'
            f'[b][2:v]overlay=0:0:eof_action=pass[v]'
        )
        run(['ffmpeg', '-nostdin', '-y', '-v', 'warning',
             '-framerate', str(FPS), '-i', frames,
             '-i', plate,
             '-framerate', str(FPS), '-i', txt,
             '-i', mix,
             '-filter_complex', fc, '-map', '[v]', '-map', '3:a',
             '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18',
             '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', mp4])
    else:
        run(['ffmpeg', '-nostdin', '-y', '-v', 'warning',
             '-framerate', str(FPS), '-i', frames, '-i', mix,
             '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '18',
             '-c:a', 'aac', '-b:a', '192k', '-shortest', '-movflags', '+faststart', mp4])

    # 6 — poster: the Ola card if the story has one, otherwise 60 % in
    ola = next((s for s in tl['scenes'] if s['name'] == 'ola'), None)
    pt = (ola['start'] + 1.2) if ola else tl['total'] * 0.6
    jpg = os.path.join(OUT_DIR, f'{slug}.jpg')
    run(['ffmpeg', '-nostdin', '-y', '-v', 'error', '-ss', f'{pt:.2f}', '-i', mp4,
         '-frames:v', '1', '-q:v', '2', jpg])

    dur = float(probe(mp4))
    size = probe(mp4, 'stream=width,height').replace('\n', 'x').strip('x')
    assert dur <= MAX_TOTAL, f'{slug}: rendered {dur:.2f}s, over the {MAX_TOTAL}s Story cap'
    print(f'\n{slug}: {mp4}  {dur:.2f}s  {size}')
    print(f'{slug}: {jpg}')


if __name__ == '__main__':
    main()
