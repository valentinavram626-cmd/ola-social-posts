import json, re, sys, os
sys.path.insert(0,'pipeline/carousel')
from alt import alt_for
from limits import fits

D='2026-11-25'
RAW=f'https://raw.githubusercontent.com/valentinavram626-cmd/ola-social-posts/main/posts/{D}/'
HELD={'en-05-edu'}

specs=json.load(open(f'night/{D}/all-specs.json'))
caps =json.load(open(f'night/{D}/all-captions.json'))

DISC={'ro':'Informații generale. Pentru situația ta, vorbește cu un contabil.',
      'en':'General information. For your own situation, speak to an accountant.'}
TAGS={'ola':'#OlaAccountancy #ValentinTheAccountant #OlaAccountancyLuton #OlaAccountancyBirmingham',
      'bham':'#OlaAccountancyBirmingham #OlaAccountancy #BirminghamBusiness #WestMidlands #SmallBusinessUK',
      'en':'#OlaAccountancy #UKTax #LimitedCompany #SelfAssessment #SmallBusinessUK'}

def alt1(p):
    card={'type':'solo','kicker':p.get('slot'),
          'h1':p.get('hero') or p.get('punch') or p.get('line')}
    return alt_for([card])

def body(setname,pid,lang,tagkey,withtags=True):
    c=caps[setname][pid]
    parts=[c['caption'].strip(), c['ask'].strip(), DISC[lang]]
    t='\n\n'.join(parts)
    if withtags: t=t+'\n\n'+TAGS[tagkey]
    return t

# ---------- hand preflight (preflight.py is dead: needs retired `topics`) ----------
problems=[]
PHONE=re.compile(r'\b0(?!330 133 1886)\d[\d \-]{7,}')
EMAIL=re.compile(r'[\w.+-]+@[\w-]+\.[\w.]+')
HANDLE=re.compile(r'(?<![\w#])@[A-Za-z0-9_.]{2,}')
for s,arr in specs.items():
    for p in arr:
        blob=' '.join(str(v) for v in p.values())
        cc=caps[s].get(p['id'],{})
        blob+=' '+' '.join(str(v) for v in cc.values())
        for rx,name in ((PHONE,'phone'),(EMAIL,'email'),(HANDLE,'handle')):
            m=rx.search(blob)
            if m: problems.append(f"{p['id']} {name}: {m.group(0)[:40]}")
        if p['kind']=='edu':
            sub=re.sub('<[^>]+>','',p.get('sub',''))
            if len(sub)<40: problems.append(f"{p['id']} sub too thin for an exclusion")
print('HAND-PREFLIGHT:', 'CLEAN' if not problems else problems)

# ---------- the plan ----------
plan=[]   # dicts: brand, blogId, networks[], time, pid, media, alt, text, extra
OLA,BHAM,EN=7561492,8085549,8086748
ola_feed_times=['07:40','09:20','10:50','12:10','13:40','15:10','16:30','18:00','19:20','21:10']
bham_times   =['08:05','09:45','11:05','12:35','14:05','15:35','17:00','18:20','19:40','21:20']
en_times     =['08:35','10:15','11:40','13:05','14:35','16:05','17:25','18:50','20:10','21:50']
threads_t=['08:10','11:20','14:10','18:30','21:30']
li_t     =['08:30','11:35','14:25','18:45','20:40']
bs_t     =['09:00','11:50','14:40','19:00','20:55']
pin_t    =['08:15','12:25','15:25','18:10','21:40']

ro=[p for p in specs['ola-ro']]
oe=[p for p in specs['ola-en']]
bh=[p for p in specs['bham']]
en=[p for p in specs['en']]

def add(brand,blog,nets,t,pid,media,alt,text,extra=None):
    plan.append(dict(brand=brand,blogId=str(blog),networks=nets,time=t,pid=pid,
                     media=media,alt=alt,text=text,extra=extra or {}))

# ola IG+FB feed (RO) + Stories at the same minute
for p,t in zip(ro,ola_feed_times):
    feed=RAW+p['id']+'-feed.png'; story=RAW+p['id']+'-story.jpg'
    add('ola',OLA,['instagram','facebook'],t,p['id'],[feed],alt1(p),
        body('ola-ro',p['id'],'ro','ola'))
    add('ola',OLA,['instagram','facebook'],t,p['id']+'-story',[story],alt1(p),'',
        {'story':True})
# ola TikTok (RO) story frame
for p,t in zip(ro,ola_feed_times):
    add('ola',OLA,['tiktok'],t,p['id']+'-tt',[RAW+p['id']+'-story.jpg'],alt1(p),
        body('ola-ro',p['id'],'ro','ola'),{'title':caps['ola-ro'][p['id']]['title']})
# ola Threads (RO) 5
th=['ola-ro-01-tip','ola-ro-02-acq','ola-ro-03-acq','ola-ro-08-joke','ola-ro-10-quote']
for pid,t in zip(th,threads_t):
    p=next(x for x in ro if x['id']==pid)
    c=caps['ola-ro'][pid]
    txt=c['caption'].strip()+'\n\n'+c['ask'].strip()+'\n\n'+DISC['ro']
    add('ola',OLA,['threads'],t,pid+'-th',[RAW+pid+'-feed.png'],alt1(p),txt)
# ola LinkedIn / Bluesky / Pinterest (EN set)
for p,t in zip(oe,li_t):
    add('ola',OLA,['linkedin'],t,p['id']+'-li',[RAW+p['id']+'-feed.png'],alt1(p),
        body('ola-en',p['id'],'en','ola'))
for p,t in zip(oe,bs_t):
    add('ola',OLA,['bluesky'],t,p['id']+'-bs',[RAW+p['id']+'-feed.png'],alt1(p),
        caps['ola-en'][p['id']]['bluesky'].strip())
for p,t in zip(oe,pin_t):
    c=caps['ola-en'][p['id']]
    add('ola',OLA,['pinterest'],t,p['id']+'-pin',[RAW+p['id']+'-feed.png'],alt1(p),
        c['caption'].strip()+'\n\n'+c['ask'].strip()+'\n\n'+DISC['en'],
        {'pin':{'boardId':'1038431695270727659','pinTitle':c['title'][:95],
                'pinLink':'https://ola-accountancy.co.uk/'}})
# ola Google Business — ONE
gp=next(x for x in oe if x['id']=='ola-en-02-acq')
add('ola',OLA,['gmb'],'09:40','ola-en-02-acq-gmb',[RAW+gp['id']+'-feed.png'],alt1(gp),
    caps['ola-en']['ola-en-02-acq']['gmb'].strip()+'\n\n'+DISC['en'],{'gmb':True})

# bham IG+FB + Stories + TikTok
for p,t in zip(bh,bham_times):
    feed=RAW+p['id']+'-feed.png'; story=RAW+p['id']+'-story.jpg'
    add('bham',BHAM,['instagram','facebook'],t,p['id'],[feed],alt1(p),
        body('bham',p['id'],'en','bham'))
    add('bham',BHAM,['instagram','facebook'],t,p['id']+'-story',[story],alt1(p),'',{'story':True})
    add('bham',BHAM,['tiktok'],t,p['id']+'-tt',[story],alt1(p),
        body('bham',p['id'],'en','bham'),{'title':caps['bham'][p['id']]['title']})

# en TikTok only, held post skipped
for p,t in zip(en,en_times):
    if p['id'] in HELD: continue
    add('en',EN,['tiktok'],t,p['id']+'-tt',[RAW+p['id']+'-story.jpg'],alt1(p),
        body('en',p['id'],'en','en'),{'title':caps['en'][p['id']]['title']})

# ---------- GATES ----------
bad=[(i['pid'],u) for i in plan for u in i['media']
     if 'tiktok' in i['networks'] and not u.lower().endswith(('.jpg','.jpeg'))]
assert not bad, bad
print('TIKTOK JPEG GATE: pass (%d tiktok posts)' % sum(1 for i in plan if 'tiktok' in i['networks']))

NETLIM={'instagram':2200,'facebook':63206,'threads':500,'tiktok':2200,'bluesky':300,
        'pinterest':800,'linkedin':3000,'gmb':1500}
over=[]
for i in plan:
    if i['extra'].get('story') and not i['text']: continue
    for nw in i['networks']:
        L=NETLIM[nw]
        if len(i['text'])>L: over.append((i['pid'],nw,len(i['text']),L))
    if i['extra'].get('pin') and len(i['extra']['pin']['pinTitle'])>100:
        over.append((i['pid'],'pinTitle',len(i['extra']['pin']['pinTitle']),100))
print('CAPTION LIMITS:', 'pass' if not over else over)
for i in plan:
    assert len(i['alt'])==len(i['media']), i['pid']
print('ALT TEXT: pass (one per media on all %d posts)' % len(plan))

json.dump(plan,open(f'night/{D}/plan.json','w'),ensure_ascii=False,indent=1)
from collections import Counter
c=Counter()
for i in plan:
    for nw in i['networks']:
        key=(i['brand'],'story' if i['extra'].get('story') else nw)
        c[key]+=1
print('\nMANIFEST (brand, network -> count to schedule)')
for k in sorted(c): print('  ',k,c[k])
print('TOTAL METRICOOL POSTS:',len(plan))
