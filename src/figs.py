import numpy as np, matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Circle, Polygon
from scipy import stats
import os
DATA='#2a78d6'; ACC='#e34948'; AXIS='#52514e'; SURF='#fcfcfb'; MUTE='#8a8a85'
D2='#eb6834'
SENT={DATA:'var(--series-1)',ACC:'var(--accent)',AXIS:'var(--ink)',SURF:'var(--surface-1)',
      MUTE:'var(--muted)',D2:'var(--series-2)'}
rng=np.random.default_rng(7)
plt.rcParams.update({'font.size':8.5,'axes.titlesize':9.5})

def clean(ax,title=None,xl=None,yl=None,grid='y',spines=('left','bottom')):
    for s in ('top','right','left','bottom'):
        ax.spines[s].set_visible(s in spines)
        if s in spines: ax.spines[s].set_color(AXIS); ax.spines[s].set_linewidth(.8)
    ax.tick_params(colors=AXIS,labelsize=8,length=3,width=.8)
    if grid=='y': ax.yaxis.grid(True,color=AXIS,alpha=.16,lw=.7)
    elif grid=='x': ax.xaxis.grid(True,color=AXIS,alpha=.16,lw=.7)
    elif grid=='both': ax.grid(True,color=AXIS,alpha=.16,lw=.7)
    ax.set_axisbelow(True)
    if title: ax.set_title(title,color=AXIS,loc='left',pad=8)
    if xl: ax.set_xlabel(xl,color=AXIS,fontsize=8.5)
    if yl: ax.set_ylabel(yl,color=AXIS,fontsize=8.5)

def save(fig,name):
    fig.tight_layout()
    p=f'fig/{name}.svg'; fig.savefig(p,format='svg',transparent=True,dpi=140); plt.close(fig)
    s=open(p).read()
    for a,b in SENT.items(): s=s.replace(a,b).replace(a.upper(),b)
    open(p,'w').write(s)

def F(w=5.6,h=3.4):
    fig,ax=plt.subplots(figsize=(w,h)); fig.patch.set_alpha(0); ax.patch.set_alpha(0); return fig,ax

# ---------- distributions ----------
x=rng.normal(50,9,600)
f,a=F(); a.hist(x,bins=26,color=DATA,edgecolor=SURF,lw=.6); clean(a,'Histogram','Value','Count'); save(f,'P001')
f,a=F(); g=np.linspace(x.min(),x.max(),300); a.fill_between(g,stats.gaussian_kde(x)(g),color=DATA,alpha=.55,lw=0)
a.plot(g,stats.gaussian_kde(x)(g),color=DATA,lw=1.6); clean(a,'Density plot','Value','Density'); save(f,'P002')
f,a=F(); xs=np.sort(x); a.step(xs,np.arange(1,len(xs)+1)/len(xs),color=DATA,lw=1.8)
clean(a,'Empirical CDF','Value','Cumulative proportion'); save(f,'P015')
f,a=F(); stats.probplot(x,plot=None); (osm,osr),(sl,ic,r)=stats.probplot(x,dist='norm')
a.plot(osm,osr,'o',ms=3.4,mfc=DATA,mec=SURF,mew=.4,ls='none'); a.plot(osm,sl*osm+ic,color=ACC,lw=1.4)
clean(a,'Q–Q plot','Theoretical quantiles','Sample quantiles'); save(f,'P016')
f,a=F(5.6,3.8)
for i,mu in enumerate([46,50,54,58,62]):
    d=rng.normal(mu,6,400); gg=np.linspace(25,85,300); k=stats.gaussian_kde(d)(gg); k=k/k.max()*1.5
    a.fill_between(gg,i,i+k,color=DATA,alpha=.75,lw=.8,ec=SURF)
a.set_yticks(range(5)); a.set_yticklabels([f'Cohort {i+1}' for i in range(5)],color=AXIS)
clean(a,'Ridgeline plot','Value',None,grid='x'); save(f,'P014')

# ---------- categorical ----------
cats=['Alpha','Beta','Gamma','Delta','Epsilon']; v=[38,52,29,61,44]
f,a=F(); a.bar(cats,v,color=DATA,width=.62); clean(a,'Bar chart',None,'Count'); save(f,'P029')
f,a=F(); b=np.array([[18,22,12],[26,14,12],[9,11,9],[30,18,13],[20,15,9]])
bot=np.zeros(5)
for j,c in enumerate([DATA,D2,MUTE]):
    a.bar(cats,b[:,j],bottom=bot,color=c,width=.62,edgecolor=SURF,lw=1.4); bot+=b[:,j]
clean(a,'Stacked bar chart',None,'Count'); save(f,'P031')
f,a=F(5.6,3.8); ages=np.arange(0,90,5); m=np.exp(-(ages-30)**2/1400)*52+rng.normal(0,1.4,18)
w=np.exp(-(ages-34)**2/1600)*54+rng.normal(0,1.4,18)
a.barh(ages,-m,height=4,color=DATA); a.barh(ages,w,height=4,color=D2)
a.set_xticks([-40,-20,0,20,40]); a.set_xticklabels(['40','20','0','20','40'])
clean(a,'Population pyramid','Population (thousands)','Age',grid='x'); save(f,'P053')

# ---------- relationships ----------
n=400; xa=rng.normal(0,1,n); ya=.72*xa+rng.normal(0,.7,n)
f,a=F(); a.plot(xa,ya,'o',ms=3.6,mfc=DATA,mec=SURF,mew=.4,alpha=.8,ls='none')
clean(a,'Scatter plot','x','y'); save(f,'P059')
f,a=F(); xb=rng.normal(0,1,9000); yb=.6*xb+rng.normal(0,.8,9000)
hb=a.hexbin(xb,yb,gridsize=26,cmap='Blues',mincnt=1,linewidths=.2,rasterized=True)
clean(a,'Hexbin plot','x','y',grid=None); save(f,'P063')
f,a=F(4.6,4.0)
M=np.array([[1,.82,-.44,.21,.06],[.82,1,-.31,.35,-.12],[-.44,-.31,1,-.08,.52],
            [.21,.35,-.08,1,.18],[.06,-.12,.52,.18,1]])
im=a.imshow(M,cmap='RdBu_r',vmin=-1,vmax=1)
lab=['Age','BMI','HDL','SBP','CRP']
a.set_xticks(range(5)); a.set_xticklabels(lab,color=AXIS,rotation=45,ha='right')
a.set_yticks(range(5)); a.set_yticklabels(lab,color=AXIS)
for i in range(5):
    for j in range(5): a.text(j,i,f'{M[i,j]:.2f}',ha='center',va='center',fontsize=7,
        color=SURF if abs(M[i,j])>.55 else AXIS)
clean(a,'Correlogram',grid=None,spines=()); save(f,'P066')

# ---------- part to whole ----------
f,a=F(4.2,3.6); a.pie([34,26,21,12,7],labels=cats,colors=[DATA,D2,MUTE,'#1baf7a','#eda100'],
  wedgeprops=dict(edgecolor=SURF,lw=1.6),textprops=dict(color=AXIS,fontsize=8.5))
a.set_title('Pie chart',color=AXIS,loc='left',pad=8); save(f,'P096')
f,a=F(4.6,3.4)
from matplotlib.patches import Circle as C2
c1=C2((.36,.5),.30,color=DATA,alpha=.55); c2=C2((.60,.5),.30,color=D2,alpha=.55)
a.add_patch(c1); a.add_patch(c2)
a.text(.22,.5,'412',ha='center',color=AXIS,fontsize=10); a.text(.48,.5,'168',ha='center',color=SURF,fontsize=10)
a.text(.74,.5,'237',ha='center',color=AXIS,fontsize=10)
a.text(.30,.86,'RNA-seq',ha='center',color=AXIS,fontsize=9); a.text(.68,.86,'Proteomics',ha='center',color=AXIS,fontsize=9)
a.set_xlim(0,1); a.set_ylim(.1,.95); a.axis('off')
a.set_title('Venn diagram',color=AXIS,loc='left',pad=8); save(f,'P105')

# ---------- time ----------
t=np.arange(120); s=np.cumsum(rng.normal(.16,1,120))+30
f,a=F(); a.plot(t,s,color=DATA,lw=1.8); clean(a,'Line chart','Time','Value'); save(f,'P108')
f,a=F(); ys=[np.abs(np.cumsum(rng.normal(0,1,120)))+6 for _ in range(3)]
a.stackplot(t,*ys,colors=[DATA,D2,MUTE],alpha=.9,edgecolor=SURF,lw=.5)
clean(a,'Stacked area chart','Time','Value'); save(f,'P111')

# ---------- model evaluation ----------
f,a=F(4.2,3.8)
sc=np.concatenate([rng.beta(2,5,500),rng.beta(5,2,500)]); yy=np.r_[np.zeros(500),np.ones(500)]
th=np.linspace(0,1,300); tpr=[(sc[yy==1]>=t_).mean() for t_ in th]; fpr=[(sc[yy==0]>=t_).mean() for t_ in th]
auc=np.trapezoid(tpr[::-1],np.array(fpr)[::-1])
a.plot([0,1],[0,1],ls='--',color=MUTE,lw=1)
a.plot(fpr,tpr,color=DATA,lw=2); a.fill_between(fpr,tpr,alpha=.12,color=DATA)
a.text(.55,.22,f'AUC = {auc:.2f}',color=AXIS,fontsize=9.5)
clean(a,'ROC curve','False positive rate','True positive rate',grid='both'); save(f,'P214')
f,a=F(4.2,3.6)
CM=np.array([[412,38],[57,293]])
a.imshow(CM,cmap='Blues')
for i in range(2):
    for j in range(2): a.text(j,i,CM[i,j],ha='center',va='center',
        color=SURF if CM[i,j]>250 else AXIS,fontsize=11)
a.set_xticks([0,1]); a.set_xticklabels(['Pred –','Pred +'],color=AXIS)
a.set_yticks([0,1]); a.set_yticklabels(['True –','True +'],color=AXIS)
clean(a,'Confusion matrix',grid=None,spines=()); save(f,'P216')

# ---------- survival ----------
f,a=F(5.6,3.6)
for i,(lam,lab_,col) in enumerate([(.011,'Treatment',DATA),(.021,'Control',D2)]):
    tt=np.arange(0,60); su=np.exp(-lam*tt)
    a.step(tt,su,where='post',color=col,lw=2,label=lab_)
    cens=np.arange(6,58,7); a.plot(cens,np.exp(-lam*cens),'|',ms=6,color=col)
a.legend(frameon=False,labelcolor=AXIS,fontsize=8.5); a.set_ylim(0,1.02)
clean(a,'Kaplan–Meier curve','Months from randomisation','Overall survival'); save(f,'P234')

# ---------- meta-analysis ----------
f,a=F(5.8,3.8)
st=['Ahmed 2019','Bianchi 2020','Chen 2021','Dubois 2022','Erikson 2023']
est=np.array([.72,.88,.61,.94,.79]); se=np.array([.14,.10,.20,.09,.12])
yv=np.arange(len(st))[::-1]
a.errorbar(est,yv,xerr=1.96*se,fmt='s',ms=6,color=DATA,ecolor=DATA,elinewidth=1.2,capsize=0)
pool=(est/se**2).sum()/(1/se**2).sum(); psе=np.sqrt(1/(1/se**2).sum())
a.add_patch(Polygon([[pool-1.96*psе,-1],[pool,-.72],[pool+1.96*psе,-1],[pool,-1.28]],color=ACC))
a.axvline(1,color=MUTE,ls='--',lw=1)
a.set_yticks(list(yv)+[-1]); a.set_yticklabels(st+['Pooled'],color=AXIS)
a.set_ylim(-1.7,len(st)-.3)
clean(a,'Forest plot','Risk ratio',None,grid='x'); save(f,'P247')

# ---------- omics ----------
f,a=F(5.2,4.0)
lfc=rng.normal(0,1.1,4000); pv=-np.log10(np.clip(rng.beta(1,14,4000),1e-12,1))
hit=(np.abs(lfc)>1)&(pv>2.2)
a.plot(lfc[~hit],pv[~hit],'o',ms=2.6,mfc=MUTE,mec='none',alpha=.45,ls='none',rasterized=True)
a.plot(lfc[hit],pv[hit],'o',ms=3.2,mfc=DATA,mec='none',alpha=.85,ls='none',rasterized=True)
a.axhline(2.2,color=ACC,ls='--',lw=.9); a.axvline(1,color=ACC,ls='--',lw=.9); a.axvline(-1,color=ACC,ls='--',lw=.9)
clean(a,'Volcano plot','log₂ fold change','−log₁₀ p'); save(f,'P279')
f,a=F(6.6,3.2)
pos=[];val=[];cols=[]
off=0
for c in range(1,15):
    L=int(600*(1-c*0.03)); p=np.arange(L)+off
    vv=-np.log10(rng.beta(1,9,L))
    if c in (3,8): vv[L//2-8:L//2+8]+=rng.uniform(3.5,8.5,16)
    pos+=list(p); val+=list(vv); cols+=[DATA if c%2 else MUTE]*L; off+=L+40
a.scatter(pos,val,s=2.2,c=cols,linewidths=0,rasterized=True)
a.axhline(7.3,color=ACC,ls='--',lw=.9)
a.set_xticks([]); clean(a,'Manhattan plot','Chromosome','−log₁₀ p',grid='y'); save(f,'P281')
f,a=F(4.8,4.0)
cl=[rng.normal([0,0],.7,(180,2)),rng.normal([4.2,1.6],.6,(150,2)),
    rng.normal([1.4,4.4],.8,(160,2)),rng.normal([5.2,5.0],.5,(90,2))]
for c,col in zip(cl,[DATA,D2,'#1baf7a','#eda100']):
    a.plot(c[:,0],c[:,1],'o',ms=3,mfc=col,mec='none',alpha=.8,ls='none',rasterized=True)
a.set_xticks([]); a.set_yticks([])
clean(a,'UMAP embedding','UMAP 1','UMAP 2',grid=None); save(f,'P318')

# ---------- ordination ----------
f,a=F(4.8,4.0)
g1=rng.multivariate_normal([-1.6,.4],[[.6,.2],[.2,.4]],70)
g2=rng.multivariate_normal([1.5,-.5],[[.7,-.15],[-.15,.5]],70)
a.plot(g1[:,0],g1[:,1],'o',ms=4,mfc=DATA,mec=SURF,mew=.4,ls='none',label='Case')
a.plot(g2[:,0],g2[:,1],'o',ms=4,mfc=D2,mec=SURF,mew=.4,ls='none',label='Control')
for vx,vy,nm in [(1.5,.6,'CRP'),(-1.2,1.1,'HDL'),(.9,-1.4,'BMI')]:
    a.annotate('',xy=(vx,vy),xytext=(0,0),arrowprops=dict(arrowstyle='->',color=ACC,lw=1.2))
    a.text(vx*1.12,vy*1.12,nm,color=ACC,fontsize=8)
a.legend(frameon=False,labelcolor=AXIS,fontsize=8.5,loc='lower left')
clean(a,'PCA biplot','PC1 (41%)','PC2 (18%)'); save(f,'P380')
f,a=F(4.6,3.2); ev=np.array([41,18,11,7.5,5.2,3.8,2.6,2.0,1.5,1.1])
a.bar(range(1,11),ev,color=DATA,width=.6); a.plot(range(1,11),ev,color=ACC,lw=1.4,marker='o',ms=4)
clean(a,'Scree plot','Component','Variance explained (%)'); save(f,'P381')

# ---------- ternary ----------
f,a=F(5.0,4.4)
def tern(A,B,C):
    t=A+B+C; A,B,C=A/t,B/t,C/t
    return .5*(2*B+C)/(A+B+C), (np.sqrt(3)/2)*C/(A+B+C)
V=[(0,0),(1,0),(.5,np.sqrt(3)/2)]
a.add_patch(Polygon(V,closed=True,fill=False,edgecolor=AXIS,lw=1.1))
for k in range(1,5):
    fr=k/5
    p1=tern(1-fr,fr,0); p2=tern(1-fr,0,fr); a.plot([p1[0],p2[0]],[p1[1],p2[1]],color=AXIS,alpha=.14,lw=.7)
    p1=tern(0,1-fr,fr); p2=tern(fr,1-fr,0); a.plot([p1[0],p2[0]],[p1[1],p2[1]],color=AXIS,alpha=.14,lw=.7)
    p1=tern(fr,0,1-fr); p2=tern(0,fr,1-fr); a.plot([p1[0],p2[0]],[p1[1],p2[1]],color=AXIS,alpha=.14,lw=.7)
for mu,col,lb in [((.62,.25,.13),DATA,'Basalt'),((.24,.55,.21),D2,'Andesite')]:
    s_=rng.dirichlet(np.array(mu)*46,60)
    px,py=tern(s_[:,0],s_[:,1],s_[:,2])
    a.plot(px,py,'o',ms=4,mfc=col,mec=SURF,mew=.4,ls='none',label=lb)
a.text(-.03,-.05,'Qz',color=AXIS,fontsize=9); a.text(1.0,-.05,'Alk',color=AXIS,fontsize=9)
a.text(.48,.90,'Pl',color=AXIS,fontsize=9)
a.legend(frameon=False,labelcolor=AXIS,fontsize=8.5,loc='upper right')
a.set_xlim(-.09,1.09); a.set_ylim(-.10,.96); a.axis('off')
a.set_title('Ternary plot',color=AXIS,loc='left',pad=8); save(f,'P400')

# ---------- directional ----------
fig=plt.figure(figsize=(4.4,4.0)); fig.patch.set_alpha(0)
a=fig.add_subplot(111,projection='polar'); a.patch.set_alpha(0)
th=np.linspace(0,2*np.pi,17)[:-1]
r=np.abs(np.cos(th-.7))*9+rng.uniform(0,2.4,16)
a.bar(th,r,width=2*np.pi/16*.92,color=DATA,edgecolor=SURF,lw=.6)
a.set_theta_zero_location('N'); a.set_theta_direction(-1)
a.tick_params(colors=AXIS,labelsize=8); a.grid(color=AXIS,alpha=.18,lw=.7)
a.set_yticklabels([]); a.set_title('Rose diagram',color=AXIS,loc='left',pad=12); save(fig,'P418')

# ---------- spectra ----------
f,a=F(6.0,3.2)
mz=np.linspace(200,1400,4000); sp=np.zeros_like(mz)
for pk,h in [(287,.28),(401,.62),(516,1.0),(644,.45),(788,.71),(902,.33),(1055,.24),(1190,.15)]:
    sp+=h*np.exp(-(mz-pk)**2/2.2)
sp+=rng.uniform(0,.012,len(mz))
a.plot(mz,sp,color=DATA,lw=.9,rasterized=True); a.set_ylim(0,1.12)
clean(a,'Mass spectrum','m/z','Relative intensity'); save(f,'P443')
f,a=F(6.0,3.2)
tt=np.linspace(10,80,4000); pat=np.zeros_like(tt)
for pk,h in [(21.4,.5),(26.6,1.0),(36.5,.30),(39.4,.24),(42.4,.20),(50.1,.28),(59.9,.16),(68.1,.12)]:
    pat+=h*np.exp(-(tt-pk)**2/0.06)
pat+=.02+.012*np.exp(-(tt-24)**2/300)+rng.normal(0,.004,len(tt))
a.plot(tt,pat,color=DATA,lw=.9,rasterized=True)
clean(a,'X-ray diffraction pattern','2θ (degrees)','Intensity'); save(f,'P449')

# ---------- characteristic curve ----------
f,a=F(5.4,3.6)
e=np.linspace(0,.22,600)
s_=np.where(e<.004,e*52000,208+ (1-np.exp(-(e-.004)*38))*310 - np.clip((e-.17),0,None)*2400)
a.plot(e,s_,color=DATA,lw=2)
a.plot([0,.03],[0,.03*52000],color=ACC,ls='--',lw=1)
a.annotate('yield',xy=(.012,208),xytext=(.045,150),color=ACC,fontsize=8.5,
  arrowprops=dict(arrowstyle='->',color=ACC,lw=1))
a.set_ylim(0,580)
clean(a,'Stress–strain curve','Strain','Stress (MPa)'); save(f,'P496')

# ---------- astronomy ----------
f,a=F(4.6,4.2)
T=np.concatenate([rng.normal(5400,1400,500),rng.normal(4200,600,90),rng.normal(9500,2000,60)])
L=np.concatenate([(T[:500]/5772)**5.2*rng.lognormal(0,.28,500),
                  rng.lognormal(4.4,.5,90), rng.lognormal(-4.6,.6,60)])
a.scatter(T,L,s=4.6,c=DATA,alpha=.65,linewidths=0,rasterized=True)
a.set_xscale('log'); a.set_yscale('log'); a.invert_xaxis()
clean(a,'Hertzsprung–Russell diagram','Effective temperature (K)','Luminosity (L☉)',grid='both'); save(f,'P524')
f,a=F(6.0,3.0)
tt=np.linspace(0,10,3000); fl=np.ones_like(tt)+rng.normal(0,.0016,3000)
for c in (2.1,5.4,8.7):
    fl-=0.021*np.exp(-((tt-c)/0.16)**8)
a.plot(tt,fl,color=DATA,lw=.8,rasterized=True)
clean(a,'Transit light curve','Time (days)','Normalised flux'); save(f,'P527')

# ---------- LAB: western blot & agarose gel (synthetic images) ----------
def blot(bands,shape=(150,420),blur=7.0,noise=.035,seed=3):
    r2=np.random.default_rng(seed); img=np.zeros(shape)
    for (cx,cy,w,h,inten) in bands:
        Y,X=np.mgrid[0:shape[0],0:shape[1]]
        img+=inten*np.exp(-(((X-cx)/w)**2+((Y-cy)/h)**2))
    from scipy.ndimage import gaussian_filter
    img=gaussian_filter(img,blur*.35)
    img+=r2.normal(0,noise,shape)
    return np.clip(img,0,1.35)

f,a=F(5.6,3.0)
lanes=[60,140,220,300,380]; ints=[1.0,.92,.55,.28,.13]
bands=[(cx,52,20,7.5,i) for cx,i in zip(lanes,ints)]
bands+=[(cx,110,21,7.0,.78) for cx in lanes]   # loading control
a.imshow(blot(bands),cmap='gray_r',vmin=0,vmax=1.25,aspect='auto')
a.set_xticks(lanes); a.set_xticklabels(['0','1','5','15','30'],color=AXIS)
a.set_yticks([52,110]); a.set_yticklabels(['p-ERK\n44 kDa','GAPDH\n37 kDa'],color=AXIS,fontsize=8)
a.set_xlabel('Minutes of stimulation',color=AXIS,fontsize=8.5)
for s in ('top','right','left','bottom'): a.spines[s].set_visible(False)
a.tick_params(length=0)
a.set_title('Western blot',color=AXIS,loc='left',pad=8); save(f,'P596')

f,a=F(5.0,3.6)
lanes=[46,110,174,238,302]
gb=[]
for j,cx in enumerate(lanes):
    if j==0: gb+=[(cx,y,17,4.0,.9) for y in (26,50,74,98,122,150,182)]  # ladder
    else:
        gb.append((cx,62+j*4,19,6.0,1.0))
        if j in (2,3): gb.append((cx,118,18,5.2,.42))
a.imshow(blot(gb,shape=(210,350),blur=6,noise=.03,seed=11),cmap='gray_r',vmin=0,vmax=1.2,aspect='auto')
a.set_xticks(lanes); a.set_xticklabels(['L','WT','KO1','KO2','NTC'],color=AXIS)
a.set_yticks([]); a.tick_params(length=0)
for s in ('top','right','left','bottom'): a.spines[s].set_visible(False)
a.set_title('Agarose gel electrophoresis',color=AXIS,loc='left',pad=8); save(f,'P601')
print('figures:',len([x for x in os.listdir('fig') if x.endswith('.svg')]))
