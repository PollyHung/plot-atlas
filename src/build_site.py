import csv, json, os, re, html
from content import ENTRIES as DEEP, CAPCOLS

# ---------- taxonomy ----------
AREA={}; TAGS={}; TAGNAME={}
for line in open('../taxonomy.txt'):
    line=line.strip()
    if line.startswith('AREA|'): _,c,n=line.split('|'); AREA[c]=n; TAGS[c]=[]
    elif line.startswith('TAG|'):
        _,a,s,n=line.split('|'); TAGS[a].append(s); TAGNAME[s]=n

SHAPES=json.load(open('../atlas.json'))['shapes']
SHAPES.pop('S04',None)
SHAPES['S04']='Paired or repeated measurements on the same units'
SHAPES['S05']='One summary value per category'
SHAPES['S30']='Characteristic curve (measured response vs a controlled variable)'
SHAPES['S31']='Reference chart or state-space diagram'

rows=list(csv.DictReader(open('../plots.csv')))
DEEPMAP={d['id']:d for d in DEEP}
SLUG={d['id']:d['slug'] for d in DEEP}

figs={}
for fn in os.listdir('fig'):
    if not fn.endswith('.svg'): continue
    key=fn[:-4]
    s=open('fig/'+fn).read(); s=s[s.index('<svg'):]
    s=re.sub(r'\s(width|height)="[\d.]+pt"','',s,count=2)
    figs[key]=s
FIG={}
for pid,slug in SLUG.items():
    if slug in figs: FIG[pid]=figs[slug]
for k,v in figs.items():
    if re.fullmatch(r'P\d{3}',k): FIG[k]=v

ENT=[]
for r in rows:
    d=DEEPMAP.get(r['id'])
    e=dict(id=r['id'],name=r['name'],alias=r['aliases'],fam=r['family'],
           shape=r['data_shape'],origin=r['origin_code'],tier=r['universality'],
           depth=r['depth_tier'],
           areas=[a for a in r['areas'].split(';') if a],
           tags=[t for t in r['subject_tags'].split(';') if t],
           tools=[t.strip() for t in r['tools'].split(';') if t.strip()],
           fig=r['id'] in FIG)
    if d:
        e.update(defn=d['defn'],read=d['read'],hides=d['hides'],use=d['use'],
                 avoid=d['avoid'],r=d['r'],py=d['py'],caps=d['caps'])
    ENT.append(e)

ORIGIN={'D':'Data-driven','H':'Hybrid instrument','L':'Lab-only','C':'Conceptual'}
ORIGDESC={'D':'Computable from a data table.',
 'H':'An instrument emits a raw signal; software renders the figure.',
 'L':'The figure is the physical experimental output. No input table exists.',
 'C':'Drawn, not derived from data.'}

DATA=dict(entries=ENT,shapes=SHAPES,areas=AREA,tags=TAGNAME,areatags=TAGS,
          origin=ORIGIN,origdesc=ORIGDESC,capcols=CAPCOLS)
json.dump(DATA,open('atlas-data.json','w'))
print('entries',len(ENT),'figures',len(FIG),
      'data %.0f KB'%(os.path.getsize('atlas-data.json')/1024))
