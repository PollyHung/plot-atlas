const D = window.__ATLAS__, FIG = window.__FIGS__;
const E = D.entries, byId = Object.fromEntries(E.map(e=>[e.id,e]));
const esc = s => (s||'').replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const app = document.getElementById('app');
const TIERLBL={universal:'Universal',"cross-domain":'Cross-domain',"domain-signature":'Domain signature',niche:'Niche'};
const famName = f => f.replace(/^F\d+\s/,'');
const shapeOf = s => D.shapes[s] || s;
const groupBy = (arr,fn) => arr.reduce((m,x)=>((m[fn(x)]=m[fn(x)]||[]).push(x),m),{});
const count = (fn) => E.filter(fn).length;

const pill=(cls,txt)=>`<span class="pill ${cls}">${esc(txt)}</span>`;
const originPill=o=>pill('o-'+o, D.origin[o]);
const depthDot=d=>`<span class="dot d-${d}" title="${d}"></span>`;

/* ---------------- rows / tables ---------------- */
function table(list){
  if(!list.length) return `<p style="color:var(--muted)">Nothing matches those filters.</p>`;
  return `<div class="tablewrap"><table><thead><tr>
    <th>#</th><th>Plot</th><th>Shape</th><th>Origin</th><th>Subject areas</th></tr></thead><tbody>`
    + list.map(e=>`<tr>
      <td class="tid">${e.id}</td>
      <td class="tname">${depthDot(e.depth)}<a href="#/plot/${e.id}">${esc(e.name)}</a>
        ${e.alias?`<span class="al">${esc(e.alias)}</span>`:''}</td>
      <td><a href="#/shape/${e.shape}" class="pill">${e.shape}</a></td>
      <td>${originPill(e.origin)}</td>
      <td style="color:var(--muted);font-size:12.6px">${e.areas.length?e.areas.join(' · '):'—'}</td>
    </tr>`).join('') + `</tbody></table></div>
    <div class="legend"><span>${depthDot('deep')} deep entry</span>
    <span>${depthDot('standard')} standard</span><span>${depthDot('stub')} stub</span></div>`;
}

/* ---------------- views ---------------- */
function home(){
  const c=o=>count(e=>e.origin===o);
  return `<section class="hero">
    <p class="eyebrow">A reference atlas of scientific figures</p>
    <h1>Every plot, and what it hides</h1>
    <p class="lede">812 plot types across the sciences — indexed not by what they look like,
    but by the shape of the data that produces them, so you can see what you could have drawn instead.</p>
    <div class="counts">
      <div><b>812</b><span>plot types</span></div>
      <div><b>31</b><span>data shapes</span></div>
      <div><b>6</b><span>subject areas</span></div>
      <div><b>143</b><span>subject tags</span></div>
    </div>
  </section>
  <div class="doors">
    <a class="door" href="#/shapes"><h3>By data shape</h3>
      <p>Start from the table you have. Every plot that consumes the same structure is an
      alternative you could be drawing — that is where the comparisons live.</p></a>
    <a class="door" href="#/areas"><h3>By subject</h3>
      <p>Six areas and 143 nested tags, from clinical trials to geochronology. Basic plots are
      deliberately untagged so subject filters stay useful.</p></a>
    <a class="door" href="#/origins"><h3>By how it is made</h3>
      <p>${c('D')} computable from a data table, ${c('H')} rendered by instrument software,
      ${c('L')} produced physically in a lab, ${c('C')} drawn by hand.</p></a>
  </div>

  <section class="sec"><div class="sech"><span>Start here</span>
    <h2>Two of these groups have identical box plots</h2></div>
    <p class="intro">140 patients per arm, same biomarker. Their five-number summaries agree to within
    0.7&nbsp;ng/mL; a t-test gives p&nbsp;=&nbsp;0.98. One arm splits cleanly into responders and
    non-responders — and the box plot cannot show it.</p>
    <div class="fig">${FIG['hero']||''}</div>
    <p class="intro" style="margin-top:18px">This is what the atlas is for.
    <a href="#/shape/S02">See all twelve plots for this data shape →</a></p>
  </section>

  <section class="sec"><div class="sech"><span>The largest families</span><h2>Browse by function</h2></div>
    <div class="cards c3">${
      Object.entries(groupBy(E,e=>e.fam)).sort((a,b)=>b[1].length-a[1].length).slice(0,12)
      .map(([f,l])=>`<a class="card" href="#/browse?fam=${encodeURIComponent(f)}">
        <span class="cid">${f.slice(0,3)}</span><h4>${esc(famName(f))}</h4>
        <p>${l.length} plot types</p></a>`).join('')}</div>
  </section>`;
}

function shapes(){
  const g=groupBy(E,e=>e.shape);
  const order=Object.keys(D.shapes).sort();
  return `<div class="crumb"><a href="#/">Atlas</a> / Data shapes</div>
  <div class="sech"><span>31 shapes</span><h2>Start from the data you have</h2></div>
  <p class="intro">A plot's data shape is the structure of its input table. Plots that share a shape are
  substitutes — they consume the same data and discard different parts of it. Four of these are not data
  shapes at all: lab output, schematics, text and 3-D structure have no input table, and group instead by
  what the figure is evidence of.</p>
  <div class="cards c3">${order.filter(s=>g[s]).map(s=>`<a class="card" href="#/shape/${s}">
    <span class="cid">${s}</span><h4>${esc(D.shapes[s])}</h4>
    <p>${g[s].length} plot${g[s].length>1?'s':''}</p></a>`).join('')}</div>`;
}

function shapePage(sid){
  const list=E.filter(e=>e.shape===sid);
  if(!list.length) return `<p>Unknown shape.</p>`;
  const rank={universal:0,'cross-domain':1,'domain-signature':2,niche:3};
  list.sort((a,b)=>rank[a.tier]-rank[b.tier]||a.id.localeCompare(b.id));
  let extra='';
  if(sid==='S02'){
    const caps=D.capcols, deep=list.filter(e=>e.caps);
    const mark={yes:['✓','y'],partial:['~','p'],no:['✕','n']};
    extra=`<section class="sec"><div class="sech"><span>The comparison</span>
      <h2>What each plot keeps and discards</h2></div>
      <div class="tablewrap"><table><thead><tr><th>Plot</th>
      ${caps.map(c=>`<th>${c[1]}</th>`).join('')}</tr></thead><tbody>
      ${deep.map(e=>`<tr><td class="tname"><a href="#/plot/${e.id}">${esc(e.name)}</a></td>
        ${caps.map(c=>{const m=mark[e.caps[c[0]]];
          return `<td style="text-align:center"><span class="pill o-${m[1]==='y'?'D':m[1]==='p'?'H':'C'}"
          style="border-radius:50%;width:22px;height:22px;display:inline-flex;align-items:center;justify-content:center">${m[0]}</span></td>`;
        }).join('')}</tr>`).join('')}
      </tbody></table></div>
      <div class="legend"><span>✓ shown</span><span>~ partial or indirect</span><span>✕ not shown</span></div>
      </section>`;
  }
  return `<div class="crumb"><a href="#/">Atlas</a> / <a href="#/shapes">Data shapes</a> / ${sid}</div>
  <div class="sech"><span>Shape ${sid} · ${list.length} plots</span><h2>${esc(D.shapes[sid])}</h2></div>
  ${sid==='S02'?`<p class="intro">One continuous measurement and one grouping column — the most
  common table in experimental science, and the one where the choice of plot does the most damage.</p>
  <div class="fig">${FIG['hero']||''}</div>`:''}
  ${extra}
  <section class="sec"><div class="sech"><span>All ${list.length}</span><h2>Plots for this shape</h2></div>
  ${table(list)}</section>`;
}

function areas(){
  return `<div class="crumb"><a href="#/">Atlas</a> / Subjects</div>
  <div class="sech"><span>6 areas · 143 tags</span><h2>Browse by subject</h2></div>
  <p class="intro">Grounded in the Nature subject ontology merged with the Elsevier journal taxonomy.
  Universal plots — histograms, scatter plots, box plots — carry no subject tags at all: tagging them
  everywhere would make every filter return the same results.</p>
  <div class="cards">${Object.entries(D.areas).map(([c,n])=>{
    const k=count(e=>e.areas.includes(c));
    return `<a class="card" href="#/area/${c}"><span class="cid">${c}</span>
      <h4>${esc(n)}</h4><p>${k} plots · ${D.areatags[c].length} tags</p></a>`}).join('')}</div>`;
}

function areaPage(code){
  const list=E.filter(e=>e.areas.includes(code));
  const tagCount={};
  list.forEach(e=>e.tags.forEach(t=>{if(D.areatags[code].includes(t))tagCount[t]=(tagCount[t]||0)+1}));
  const tags=Object.entries(tagCount).sort((a,b)=>b[1]-a[1]);
  return `<div class="crumb"><a href="#/">Atlas</a> / <a href="#/areas">Subjects</a> / ${code}</div>
  <div class="sech"><span>${code} · ${list.length} plots</span><h2>${esc(D.areas[code])}</h2></div>
  ${tags.length?`<p class="intro">Most-used subject tags in this area:</p>
  <div class="tagrow" style="margin-bottom:26px">${tags.slice(0,18).map(([t,n])=>
    `<a class="pill" href="#/browse?tag=${t}">${esc(D.tags[t]||t)} · ${n}</a>`).join('')}</div>`:''}
  ${table(list)}`;
}

function origins(){
  return `<div class="crumb"><a href="#/">Atlas</a> / Origin</div>
  <div class="sech"><span>4 classes</span><h2>How the figure is made</h2></div>
  <p class="intro">Most glossaries assume every figure can be plotted from a spreadsheet. Most cannot.
  The hybrid class is the one usually missed — a mass spectrum or an MRI is neither hand-drawn nor
  plottable from a table; an instrument emits a raw signal and software renders it.</p>
  <div class="cards">${Object.entries(D.origin).map(([c,n])=>
    `<a class="card" href="#/browse?origin=${c}"><span class="cid">${c}</span><h4>${esc(n)}</h4>
     <p>${count(e=>e.origin===c)} plots — ${esc(D.origdesc[c])}</p></a>`).join('')}</div>`;
}

/* ---------------- browse with facets ---------------- */
let F={q:'',origin:new Set(),area:new Set(),tier:new Set(),shape:new Set(),fam:'',tag:''};
function browse(params){
  if(params){
    F={q:'',origin:new Set(),area:new Set(),tier:new Set(),shape:new Set(),fam:'',tag:''};
    if(params.get('origin')) F.origin.add(params.get('origin'));
    if(params.get('area')) F.area.add(params.get('area'));
    if(params.get('shape')) F.shape.add(params.get('shape'));
    if(params.get('fam')) F.fam=params.get('fam');
    if(params.get('tag')) F.tag=params.get('tag');
  }
  return `<div class="crumb"><a href="#/">Atlas</a> / All plots</div>
  <div class="sech"><span>812 plot types</span><h2>Browse everything</h2></div>
  <div class="browse"><div class="facets" id="facets"></div><div><div id="results"></div></div></div>`;
}
function applyFilters(){
  const q=F.q.toLowerCase();
  return E.filter(e=>{
    if(F.origin.size&&!F.origin.has(e.origin))return false;
    if(F.tier.size&&!F.tier.has(e.tier))return false;
    if(F.shape.size&&!F.shape.has(e.shape))return false;
    if(F.area.size&&!e.areas.some(a=>F.area.has(a)))return false;
    if(F.fam&&e.fam!==F.fam)return false;
    if(F.tag&&!e.tags.includes(F.tag))return false;
    if(q&&!(e.name+' '+e.alias+' '+e.fam+' '+e.tools.join(' ')).toLowerCase().includes(q))return false;
    return true;
  });
}
function renderFacets(){
  const box=document.getElementById('facets'); if(!box)return;
  const mk=(title,items,set,key)=>`<div class="facet"><h4>${title}</h4>${items.map(([v,l,n])=>
    `<label><input type="checkbox" data-k="${key}" value="${v}" ${set.has(v)?'checked':''}>
     <span>${esc(l)}</span><span class="cnt">${n}</span></label>`).join('')}</div>`;
  const shapeItems=Object.keys(D.shapes).sort().filter(s=>count(e=>e.shape===s))
    .map(s=>[s,s+' '+D.shapes[s].replace(/\s*\(.*/,''),count(e=>e.shape===s)]);
  box.innerHTML =
    mk('Origin',Object.entries(D.origin).map(([c,n])=>[c,n,count(e=>e.origin===c)]),F.origin,'origin')+
    mk('Subject area',Object.entries(D.areas).map(([c,n])=>[c,n,count(e=>e.areas.includes(c))]),F.area,'area')+
    mk('Breadth',Object.entries(TIERLBL).map(([c,n])=>[c,n,count(e=>e.tier===c)]),F.tier,'tier')+
    mk('Data shape',shapeItems,F.shape,'shape');
  box.querySelectorAll('input').forEach(i=>i.onchange=()=>{
    const s=F[i.dataset.k]; i.checked?s.add(i.value):s.delete(i.value); renderResults();
  });
}
function renderResults(){
  const box=document.getElementById('results'); if(!box)return;
  const list=applyFilters();
  const active=(F.fam?1:0)+(F.tag?1:0)+F.origin.size+F.area.size+F.tier.size+F.shape.size+(F.q?1:0);
  box.innerHTML=`<div class="resbar"><b>${list.length}</b>
    <span style="color:var(--muted);font-size:13px">of 812${F.fam?' · '+esc(famName(F.fam)):''}${F.tag?' · '+esc(D.tags[F.tag]||F.tag):''}</span>
    ${active?'<button id="clr">Clear filters</button>':''}</div>`+table(list);
  const c=document.getElementById('clr');
  if(c)c.onclick=()=>{F={q:'',origin:new Set(),area:new Set(),tier:new Set(),shape:new Set(),fam:'',tag:''};
    document.getElementById('q').value=''; renderFacets(); renderResults();};
}

/* ---------------- entry page ---------------- */
function plotPage(id){
  const e=byId[id]; if(!e) return `<p>Not found.</p>`;
  const sibs=E.filter(x=>x.shape===e.shape&&x.id!==e.id)
    .sort((a,b)=>({universal:0,'cross-domain':1,'domain-signature':2,niche:3})[a.tier]
                -({universal:0,'cross-domain':1,'domain-signature':2,niche:3})[b.tier]);
  const ul=(items,cls='')=>`<ul class="${cls}">${items.map(i=>`<li>${esc(i)}</li>`).join('')}</ul>`;
  const body = e.defn ? `
    <p class="lead">${esc(e.defn)}</p>
    <div class="dyad">
      <section><h4>How to read it</h4>${ul(e.read)}</section>
      <section><h4 class="hh">What it hides</h4>${ul(e.hides,'hide')}</section>
    </div>
    <div class="dyad">
      <section><h4>Reach for it when</h4>${ul(e.use,'yes')}</section>
      <section><h4>Avoid it when</h4>${ul(e.avoid,'no')}</section>
    </div>
    <div class="code">
      <div><span class="lang">R</span><pre><code>${esc(e.r)}</code></pre></div>
      <div><span class="lang">Python</span><pre><code>${esc(e.py)}</code></pre></div>
    </div>`
   : `<p class="stubnote">Catalogued and classified, not yet written up — it is queued as a
      <b>${e.depth}</b> entry. Its data shape, origin, subject tags and tooling are complete; the
      reading guide and the comparison against its ${sibs.length} siblings are still to come.</p>`;
  return `<div class="crumb"><a href="#/">Atlas</a> / <a href="#/browse">All plots</a> /
    <a href="#/shape/${e.shape}">${e.shape}</a> / ${e.id}</div>
  <div class="entry"><div>
    <div class="metarow">${pill('','')/*sp*/&&''}${originPill(e.origin)}
      ${pill('',TIERLBL[e.tier])}${e.defn?pill('','written'):pill('','planned: '+e.depth)}
      <a class="pill" href="#/browse?fam=${encodeURIComponent(e.fam)}">${esc(famName(e.fam))}</a></div>
    <h1>${esc(e.name)}</h1>
    ${e.alias?`<p class="alias">${esc(e.alias)}</p>`:''}
    ${FIG[e.id]?`<div class="fig">${FIG[e.id]}</div>`
      :`<div class="nofig">No figure generated for this entry yet</div>`}
    ${body}
  </div>
  <aside class="side">
    <section><h4>Data shape</h4>
      <p><a href="#/shape/${e.shape}">${e.shape} — ${esc(D.shapes[e.shape])}</a></p></section>
    <section><h4>How it is made</h4><p>${esc(D.origdesc[e.origin])}</p></section>
    ${e.areas.length?`<section><h4>Subject areas</h4><div class="list">${
      e.areas.map(a=>`<a href="#/area/${a}">${esc(D.areas[a]||a)}</a>`).join('')}</div></section>`
      :`<section><h4>Subject areas</h4><p style="color:var(--muted)">Universal — used across every
        area, so deliberately untagged.</p></section>`}
    ${e.tags.length?`<section><h4>Subject tags</h4><div class="tagrow">${
      e.tags.map(t=>`<a class="pill" href="#/browse?tag=${t}">${esc(D.tags[t]||t)}</a>`).join('')}</div></section>`:''}
    <section><h4>${e.origin==='L'?'Technique':'Tools'}</h4>
      <div class="toollist">${e.tools.map(t=>esc(t)).join('<br>')}</div></section>
    ${sibs.length?`<section><h4>Alternatives from the same data</h4><div class="sibs">${
      sibs.slice(0,14).map(s=>`<a href="#/plot/${s.id}">${esc(s.name)}</a>`).join('')}
      ${sibs.length>14?`<a href="#/shape/${e.shape}" style="color:var(--series-1)">all ${sibs.length} →</a>`:''}
      </div></section>`:''}
  </aside></div>`;
}

function about(){
  return `<div class="crumb"><a href="#/">Atlas</a> / About</div>
  <div class="sech"><span>About</span><h2>What this is, and what it is not yet</h2></div>
  <div style="max-width:66ch;color:var(--ink-2)">
  <p>A catalogue of 812 plot types used across the sciences, classified four ways: by function
  (33 families), by the shape of the data that produces them (31 shapes), by how the figure is
  physically made (4 origin classes), and by subject (6 areas, 143 nested tags).</p>
  <p>The organising idea is the <a href="#/shapes">data shape</a>. Two plots are alternatives if they
  consume the same table. That relation is authored once per shape rather than once per pair, and it
  supports the question people actually arrive with — <em>I have this kind of data, what could I draw?</em></p>
  <h3 style="font-size:1.15rem;margin:26px 0 8px">Current state</h3>
  <p>All 812 entries are catalogued, classified and searchable. Written depth follows three tiers:
  <b>${count(e=>e.depth==='deep')} deep</b>, <b>${count(e=>e.depth==='standard')} standard</b>,
  <b>${count(e=>e.depth==='stub')} stub</b>. Twelve entries — the ${'S02'} shape — are fully written and
  illustrated as the reference format. ${Object.keys(FIG).length-1} figures have been generated so far.</p>
  <p>Every figure is generated from synthetic data by script, never copied, so nothing here carries a
  licence restriction. The colour palette is validated for colour-vision deficiency in both themes.</p>
  <h3 style="font-size:1.15rem;margin:26px 0 8px">Known gaps</h3>
  <p>Most entries have no figure yet. Most have no written guidance yet. Package references were checked
  against the live CRAN and Bioconductor indexes, but 34 cited packages are archived and need
  substitutes. Subject rankings are considered estimates, not measured frequencies.</p>
  </div>`;
}

/* ---------------- router ---------------- */
function route(){
  const h=location.hash.slice(2)||'';
  const [path,qs]=h.split('?');
  const p=path.split('/').filter(Boolean);
  const params=new URLSearchParams(qs||'');
  let html='', isBrowse=false;
  if(!p.length) html=home();
  else if(p[0]==='browse'){html=browse(params); isBrowse=true;}
  else if(p[0]==='shapes') html=shapes();
  else if(p[0]==='shape') html=shapePage(p[1]);
  else if(p[0]==='areas') html=areas();
  else if(p[0]==='area') html=areaPage(p[1]);
  else if(p[0]==='origins') html=origins();
  else if(p[0]==='plot') html=plotPage(p[1]);
  else if(p[0]==='about') html=about();
  else html=`<div class="crumb"><a href="#/">Atlas</a></div><p>Page not found.</p>`;
  app.innerHTML=html+`<footer><p><b>Plot Atlas</b> — 812 plot types, indexed by data shape.</p>
    <p>Figures generated from synthetic data. <a href="#/about">What is finished and what is not</a>.</p></footer>`;
  if(isBrowse){renderFacets();renderResults();}
  document.querySelectorAll('#nav a').forEach(a=>a.classList.toggle('on',a.getAttribute('href')==='#/'+p[0]));
  window.scrollTo(0,0);
}
window.addEventListener('hashchange',route);

/* ---------------- search ---------------- */
const qEl=document.getElementById('q'), sg=document.getElementById('sugg');
let sel=-1, hits=[];
qEl.addEventListener('input',()=>{
  const v=qEl.value.trim().toLowerCase();
  if(location.hash.startsWith('#/browse')){F.q=qEl.value.trim();renderResults();}
  if(v.length<2){sg.classList.remove('open');return;}
  hits=E.filter(e=>(e.name+' '+e.alias).toLowerCase().includes(v)).slice(0,12);
  sel=-1;
  sg.innerHTML=hits.map((e,i)=>`<a href="#/plot/${e.id}" data-i="${i}">
    <span class="sid">${e.id}</span>${esc(e.name)}<span class="sm">${e.shape} · ${D.origin[e.origin]}</span></a>`).join('')
    +`<a href="#/browse" style="color:var(--series-1)">See all results in browse →</a>`;
  sg.classList.add('open');
});
qEl.addEventListener('keydown',ev=>{
  const links=[...sg.querySelectorAll('a')];
  if(ev.key==='ArrowDown'){ev.preventDefault();sel=Math.min(sel+1,links.length-1);}
  else if(ev.key==='ArrowUp'){ev.preventDefault();sel=Math.max(sel-1,0);}
  else if(ev.key==='Enter'&&sel>=0){ev.preventDefault();links[sel].click();sg.classList.remove('open');qEl.blur();return;}
  else if(ev.key==='Escape'){sg.classList.remove('open');qEl.blur();return;}
  else return;
  links.forEach((l,i)=>l.classList.toggle('sel',i===sel));
});
document.addEventListener('click',e=>{if(!sg.contains(e.target)&&e.target!==qEl)sg.classList.remove('open')});
sg.addEventListener('click',()=>sg.classList.remove('open'));
route();
