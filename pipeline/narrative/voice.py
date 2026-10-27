#!/usr/bin/env python3
"""Generate the narration for one story with Valentin's cloned ElevenLabs voice.

    ELEVENLABS_API_KEY=... python3 voice.py <slug> [--out DIR]

Writes <out>/00.wav .. NN.wav — mono 44.1 kHz, silence-trimmed, loudness
normalised to I=-18 TP=-2, which is what timeline.py and audio.py expect.

If no API key is available (e.g. the session only has the ElevenLabs MCP
connector), generate the takes through the connector instead, download the
mp3s and run them through CONVERT below by hand; build.py --skip-voice then
picks them up from the same folder.
"""
import json, os, subprocess, sys, argparse, urllib.request, urllib.error

HERE = os.path.dirname(os.path.abspath(__file__))
API = 'https://api.elevenlabs.io/v1'
VOICE_ID = '4YZdCwbKGmetvWILgi8V'        # "Valentin Voice"
MODEL = 'eleven_multilingual_v2'         # the model that speaks Romanian

# Trim the silence ElevenLabs leaves at both ends, then normalise.  Keep this in
# sync with the command in README.md — timings depend on it.
CONVERT = ('silenceremove=start_periods=1:start_duration=0:start_threshold=-45dB:detection=peak,'
           'areverse,'
           'silenceremove=start_periods=1:start_duration=0:start_threshold=-45dB:detection=peak,'
           'areverse,loudnorm=I=-18:TP=-2')


def convert(src, dst):
    subprocess.run(['ffmpeg', '-nostdin', '-y', '-v', 'error', '-i', src,
                    '-af', CONVERT, '-ac', '1', '-ar', '44100', dst], check=True)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('slug')
    ap.add_argument('--out', default=None)
    ap.add_argument('--voice-id', default=VOICE_ID)
    a = ap.parse_args()

    key = os.environ.get('ELEVENLABS_API_KEY')
    if not key:
        sys.exit('ELEVENLABS_API_KEY not set — generate via the MCP connector instead '
                 '(see the docstring) and run build.py --skip-voice')

    story = json.load(open(os.path.join(HERE, 'stories', f'{a.slug}.json'), encoding='utf8'))
    out = a.out or os.path.join(HERE, 'build', a.slug, 'voice')
    os.makedirs(out, exist_ok=True)

    chars = 0
    for i, text in enumerate(story['phrases']):
        body = json.dumps({'text': text, 'model_id': MODEL,
                           'voice_settings': {'stability': 0.45, 'similarity_boost': 0.8,
                                              'style': 0.25, 'use_speaker_boost': True}}).encode()
        req = urllib.request.Request(f'{API}/text-to-speech/{a.voice_id}', data=body,
                                     headers={'xi-api-key': key, 'Content-Type': 'application/json',
                                              'Accept': 'audio/mpeg'})
        try:
            with urllib.request.urlopen(req, timeout=180) as f:
                mp3 = f.read()
        except urllib.error.HTTPError as e:
            sys.exit(f'phrase {i} failed: {e.code} {e.read()[:300].decode("utf8", "ignore")}')
        tmp = os.path.join(out, f'{i:02d}.mp3')
        open(tmp, 'wb').write(mp3)
        convert(tmp, os.path.join(out, f'{i:02d}.wav'))
        os.remove(tmp)
        chars += len(text)
        print(f'  {i:02d}  {text[:56]}')
    print(f'{a.slug}: {len(story["phrases"])} takes in {out}/, ~{chars} characters')


if __name__ == '__main__':
    main()
