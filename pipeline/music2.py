import numpy as np, wave, sys
sr=44100; V=int(sys.argv[3]) if len(sys.argv)>3 else 0
PR=[([[60,64,67,71],[57,60,64,67],[53,57,60,64],[55,59,62,65]],[36,33,29,31],100),([[57,60,64,67],[53,57,60,64],[60,64,67,71],[55,59,62,67]],[33,29,36,31],92),([[62,65,69,72],[67,71,74,77],[60,64,67,71],[57,60,64,69]],[38,31,36,33],108),([[64,67,71,74],[60,64,67,71],[62,65,69,72],[59,62,67,71]],[40,36,38,35],96),([[65,69,72,76],[62,65,69,72],[58,62,65,69],[60,64,67,70]],[41,38,34,36],104),([[59,62,66,69],[64,67,71,74],[57,61,64,69],[62,66,69,73]],[35,40,33,38],88)]
import math
bpm=PR[V%6][2]; beat=60/bpm; bars=math.ceil(float(sys.argv[2])/(4*beat))+1; dur=bars*4*beat
t=np.arange(int(sr*(dur+1.5)))/sr; out=np.zeros_like(t)
def n2f(n): return 440*2**((n-69)/12)
chords=[PR[V%6][0][i%4] for i in range(bars)]; bass=[PR[V%6][1][i%4] for i in range(bars)]
def add(sig,start):
    i=int(start*sr); out[i:i+len(sig)]+=sig[:len(out)-i]
def ep(f,L,amp):
    tt=np.arange(int(sr*L))/sr; env=np.exp(-tt*2.2)*(1-np.exp(-tt*80))
    return amp*env*(np.sin(2*np.pi*f*tt)+0.3*np.sin(2*np.pi*2*f*tt)*np.exp(-tt*5)+0.08*np.sin(2*np.pi*3*f*tt))
def pad(f,L,amp):
    tt=np.arange(int(sr*L))/sr; env=np.minimum(1,tt/0.6)*np.minimum(1,(L-tt)/0.5)
    s=sum(np.sin(2*np.pi*f*d*tt) for d in (0.997,1,1.003))/3
    return amp*env*s
for b,ch in enumerate(chords):
    s=b*4*beat
    for k,nn in enumerate(ch): add(pad(n2f(nn),4*beat,0.05),s)
    for hit in (0,1.5,2.5):  # EP rhythm
        for k,nn in enumerate(ch): add(ep(n2f(nn+12),1.2,0.045),s+hit*beat+k*0.012)
    tt=np.arange(int(sr*4*beat))/sr
    add(0.18*np.sin(2*np.pi*n2f(bass[b])*tt)*np.minimum(1,tt/0.02)*np.exp(-tt*0.4),s)
rng=np.random.default_rng(V+1)
for i in range(bars*4):
    s=i*beat
    tt=np.arange(int(sr*0.35))/sr; f=50+90*np.exp(-tt*25)
    add(0.5*np.sin(2*np.pi*np.cumsum(f)/sr)*np.exp(-tt*9),s) if i%2==0 else None
    if i%2==1:
        tt=np.arange(int(sr*0.2))/sr; add(0.12*rng.standard_normal(len(tt))*np.exp(-tt*25),s)
    for h in (0,0.5):
        tt=np.arange(int(sr*0.05))/sr; nz=rng.standard_normal(len(tt)); nz=np.diff(nz,prepend=0)
        add(0.04*nz*np.exp(-tt*80),s+h*beat+(0.03 if h else 0))
# simple reverb
ir_t=np.arange(int(sr*1.2))/sr; ir=rng.standard_normal(len(ir_t))*np.exp(-ir_t*4)*0.02; ir[0]=1
from numpy.fft import rfft,irfft
N=len(out)+len(ir); wet=irfft(rfft(out,N)*rfft(ir,N),N)[:len(out)]
mix=np.tanh(1.3*wet); L=float(sys.argv[2]); mix=mix[:int(sr*L)]
fade=np.ones_like(mix); fl=int(sr*1.2); fade[-fl:]=np.linspace(1,0,fl); fade[:int(sr*0.05)]=np.linspace(0,1,int(sr*0.05)); mix*=fade
mix=mix/np.abs(mix).max()*0.8
st=np.stack([mix,np.roll(mix,180)],1)
w=wave.open(sys.argv[1],'w'); w.setnchannels(2); w.setsampwidth(2); w.setframerate(sr); w.writeframes((st*32767).astype(np.int16).tobytes())
