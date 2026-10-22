#!/bin/bash
# Full mechanical production for one week. Run from pipeline/ after week_plan.json, week_ro.json, week_en.json, week_valentin.json are written.
# usage: bash run_week.sh 2026-10-30   (first day of the batch)
set -e; cd "$(dirname "$0")"; W=$1
pip list 2>/dev/null | grep -qi numpy || pip install -q --break-system-packages numpy
npm ls -g playwright >/dev/null 2>&1 || npm i -g playwright >/dev/null 2>&1
for v in 0 1 2 3 4 5; do [ -f lm$v.wav ] || python3 music2.py lm$v.wav 22 $v; done
python3 - <<'PY'
import json,random
for lang in ('ro','en'):
    ps=json.load(open(f'week_{lang}.json')); random.seed(7)
    open(f'list_{lang}.txt','w').write(''.join(f"{p['id']} {i%6}\n" for i,p in enumerate(ps)))
PY
bash render2.sh week_ro.json list_ro.txt & bash render2.sh week_en.json list_en.txt & wait
D=../reels/week-$W; mkdir -p $D/thumbs; cp out/*.mp4 $D/; for f in out/*.thumb.jpg; do b=$(basename $f .thumb.jpg); cp $f $D/thumbs/$b.jpg; done
echo RENDERED $(ls out/*.mp4 | wc -l)
