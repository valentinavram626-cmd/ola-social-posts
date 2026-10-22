import sys,subprocess,wave,json,numpy as np
from faster_whisper import WhisperModel
m=WhisperModel('medium',device='cpu',compute_type='int8')
D="/mnt/user-data/uploads/Marketing Department Ola/Video Photo Ola/"
out={}
for k in sys.argv[1:]:
    subprocess.run(['ffmpeg','-v','error','-y','-i',D+k+'.mp4','-vn','-ac','1','-ar','16000','a.wav'])
    w=wave.open('a.wav');a=np.frombuffer(w.readframes(w.getnframes()),dtype=np.int16).astype(np.float32)/32768
    segs,_=m.transcribe(a,language='ro',beam_size=3,vad_filter=True)
    out[k]=[(round(s.start,2),round(s.end,2),s.text.strip()) for s in segs]
    for s in out[k]: print(k[-9:],s)
json.dump(out,open('segs.json','w'),ensure_ascii=False)
