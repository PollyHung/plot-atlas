#!/usr/bin/env python3
"""Plot Atlas — static site generator.

Pre-renders one real HTML page per catalogue entry plus every listing page, so
that search engines see 812 documents rather than one hash-routed shell.

Run from anywhere:  python3 src/build.py
Output goes to the repository root, which is what GitHub Pages publishes.
"""
import csv, json, os, re, shutil, sys, html, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from content import ENTRIES as WRITTEN, CAPCOLS

CONF = json.load(open(os.path.join(ROOT, 'site.json')))
BASE = CONF['base_url'].rstrip('/')
SITE = CONF['site_name']

# ---------------------------------------------------------------- data load

def load_taxonomy():
    areas, areatags, tagname = {}, {}, {}
    for line in open(os.path.join(ROOT, 'data', 'taxonomy.txt')):
        line = line.strip()
        if line.startswith('AREA|'):
            _, c, n = line.split('|'); areas[c] = n; areatags[c] = []
        elif line.startswith('TAG|'):
            _, a, s, n = line.split('|'); areatags[a].append(s); tagname[s] = n
    return areas, areatags, tagname

AREAS, AREATAGS, TAGNAME = load_taxonomy()

SHAPES = {}
ROWS = list(csv.DictReader(open(os.path.join(ROOT, 'data', 'plots.csv'))))
for r in ROWS:
    SHAPES.setdefault(r['data_shape'], r['shape_label'])

ORIGIN = {'D': 'Data-driven', 'H': 'Hybrid instrument', 'L': 'Lab-only', 'C': 'Conceptual'}
ORIGDESC = {
    'D': 'Computable from a data table.',
    'H': 'An instrument emits a raw signal; software renders the figure.',
    'L': 'The figure is the physical experimental output. No input table exists.',
    'C': 'Drawn, not derived from data.'}
ORIGADJ = {'D': 'data-driven', 'H': 'instrument-rendered', 'L': 'lab-produced', 'C': 'conceptual'}
TIERLBL = {'universal': 'Universal', 'cross-domain': 'Cross-domain',
           'domain-signature': 'Domain signature', 'niche': 'Niche'}
RANK = {'universal': 0, 'cross-domain': 1, 'domain-signature': 2, 'niche': 3}


def slugify(name):
    s = name.lower().replace('&', 'and')
    s = re.sub(r"['‘’]", '', s)
    return re.sub(r'[^a-z0-9]+', '-', s).strip('-')


WRITTEN_BY_ID = {d['id']: d for d in WRITTEN}

# figures: fig/<id>.svg, or fig/<content-slug>.svg for the pilot set
FIGDIR = os.path.join(HERE, 'fig')


def read_fig(name):
    p = os.path.join(FIGDIR, name + '.svg')
    if not os.path.exists(p):
        return None
    s = open(p).read()
    s = s[s.index('<svg'):]
    s = re.sub(r'\s(width|height)="[\d.]+pt"', '', s, count=2)
    # the generated SVGs carry no accessible name of their own
    s = s.replace('<svg ', '<svg role="img" ', 1)
    return s


ENTRIES = []
for r in ROWS:
    w = WRITTEN_BY_ID.get(r['id'])
    e = dict(
        id=r['id'], name=r['name'], alias=r['aliases'], fam=r['family'],
        shape=r['data_shape'], shape_label=r['shape_label'], origin=r['origin_code'],
        tier=r['universality'], depth=r['depth_tier'],
        areas=[a for a in r['areas'].split(';') if a],
        tags=[t for t in r['subject_tags'].split(';') if t],
        tools=[t.strip() for t in r['tools'].split(';') if t.strip()],
        slug=slugify(r['name']))
    e['figname'] = r['id'] if os.path.exists(os.path.join(FIGDIR, r['id'] + '.svg')) else (
        w['slug'] if w and os.path.exists(os.path.join(FIGDIR, w['slug'] + '.svg')) else None)
    if w:
        for k in ('defn', 'read', 'hides', 'use', 'avoid', 'r', 'py', 'caps'):
            e[k] = w[k]
    ENTRIES.append(e)

BY_ID = {e['id']: e for e in ENTRIES}
BY_SLUG = {e['slug']: e for e in ENTRIES}
assert len(BY_SLUG) == len(ENTRIES), 'slug collision'

FAMS = sorted({e['fam'] for e in ENTRIES})
FAMSLUG = {f: slugify(f[4:]) for f in FAMS}


def in_shape(s):
    return [e for e in ENTRIES if e['shape'] == s]


def tier_sort(lst):
    return sorted(lst, key=lambda e: (RANK[e['tier']], e['id']))


# ---------------------------------------------------------------- helpers

def esc(s):
    return html.escape(s or '', quote=True)


def famname(f):
    return re.sub(r'^F\d+\s', '', f)


def trim(s, n=157):
    s = ' '.join(s.split())
    if len(s) <= n:
        return s
    cut = s[:n].rsplit(' ', 1)[0]
    return cut.rstrip(' ,;:—-') + '…'


def description(e):
    """One meta description per entry.

    Written entries use their own definition sentence. The rest are described
    from the facts that are actually specific to them — aliases, data shape,
    how the figure is made, how many alternatives share its shape, the primary
    tool — rather than from a fixed sentence with the name slotted in.
    """
    if e.get('defn'):
        return trim(e['defn'])
    sibs = len(in_shape(e['shape'])) - 1
    alias = [a.strip() for a in e['alias'].split(';') if a.strip()]
    lead = e['name']
    if alias:
        lead += ' (' + alias[0] + ')'
    bits = ['%s: a %s figure drawn from %s.' % (lead, ORIGADJ[e['origin']],
                                                e['shape_label'][0].lower() + e['shape_label'][1:])]
    if sibs:
        bits.append('%d alternatives share that data shape.' % sibs)
    if e['tools'] and e['origin'] != 'L':
        bits.append('Drawn with %s.' % e['tools'][0].split(';')[0].strip())
    elif e['tools']:
        bits.append('Technique: %s.' % e['tools'][0].strip())
    return trim(' '.join(bits))


NAV = [('browse/', 'All plots'), ('shapes/', 'By data shape'), ('subjects/', 'By subject'),
       ('origins/', 'By origin'), ('families/', 'By family'), ('about/', 'About')]


def page(path, title, desc, body, extra_head='', nav_on='', og_type='website'):
    """Write one complete HTML document."""
    depth = path.count('/')
    root = '../' * depth
    canon = BASE + '/' + (path.rsplit('index.html', 1)[0])
    if path == '404.html':
        # Served for any missed URL under the site, so relative links would
        # resolve against the request path rather than this file's location.
        root = BASE + '/'
    nav = ''.join('<a href="%s%s"%s>%s</a>' % (root, href, ' class="on"' if href == nav_on else '', lbl)
                  for href, lbl in NAV)
    doc = f'''<!doctype html>
<html lang="en" data-root="{root}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{esc(canon)}">
<meta property="og:type" content="{og_type}">
<meta property="og:site_name" content="{esc(SITE)}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}">
<meta property="og:url" content="{esc(canon)}">
<meta name="twitter:card" content="summary">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Spectral:ital,wght@0,400;0,600;1,400&amp;family=IBM+Plex+Mono:wght@400;500&amp;family=IBM+Plex+Sans:wght@400;500;600&amp;display=swap">
<link rel="stylesheet" href="{root}assets/atlas.css">
<script>try{{var t=localStorage.getItem('atlas-theme');if(t&&t!=='system')document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}</script>
{extra_head}</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="top"><div class="topin">
 <a class="brand" href="{root}">Plot <span>Atlas</span></a>
 <nav class="main">{nav}</nav>
 <div class="search">
  <svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="M20 20l-4-4"/></svg>
  <input id="q" type="search" placeholder="Search {len(ENTRIES)} plots…" autocomplete="off" aria-label="Search plots">
  <div class="sugg" id="sugg"></div>
 </div>
 <button class="themebtn" id="themebtn" hidden>Theme</button>
</div></header>
<main id="main">
{body}
<footer>
<p><b>Plot Atlas</b> — {len(ENTRIES)} plot types, indexed by data shape.</p>
<p>Figures generated from synthetic data. <a href="{root}about/">What is finished and what is not</a> ·
<a href="{root}sitemap-page/">Site index</a></p>
</footer>
</main>
<script src="{root}assets/site.js" defer></script>
</body>
</html>
'''
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w').write(doc)
    PAGES.append(path)
    return len(doc)


PAGES = []


# ---------------------------------------------------------------- fragments

def pill(cls, txt):
    return '<span class="pill %s">%s</span>' % (cls, esc(txt))


def table(lst, root):
    if not lst:
        return '<p style="color:var(--muted)">Nothing matches those filters.</p>'
    out = ['<div class="tablewrap"><table><thead><tr><th>#</th><th>Plot</th><th>Shape</th>'
           '<th>Origin</th><th>Subject areas</th></tr></thead><tbody>']
    for e in lst:
        out.append(
            '<tr><td class="tid">%s</td><td class="tname">'
            '<span class="dot d-%s" title="%s"></span>'
            '<a href="%splot/%s/">%s</a>%s</td>'
            '<td><a href="%sshape/%s/" class="pill">%s</a></td>'
            '<td><span class="pill o-%s">%s</span></td>'
            '<td style="color:var(--muted);font-size:12.6px">%s</td></tr>' % (
                e['id'], e['depth'], e['depth'], root, e['slug'], esc(e['name']),
                ('<span class="al">%s</span>' % esc(e['alias'])) if e['alias'] else '',
                root, e['shape'], e['shape'], e['origin'], ORIGIN[e['origin']],
                ' · '.join(e['areas']) if e['areas'] else '—'))
    out.append('</tbody></table></div><div class="legend">'
               '<span><span class="dot d-deep"></span> deep entry</span>'
               '<span><span class="dot d-standard"></span> standard</span>'
               '<span><span class="dot d-stub"></span> stub</span></div>')
    return ''.join(out)


def sech(eyebrow, h, tag='h1'):
    return '<div class="sech"><span>%s</span><%s>%s</%s></div>' % (esc(eyebrow), tag, esc(h), tag)


def crumb(root, *parts):
    bits = ['<a href="%s">Atlas</a>' % root]
    for p in parts:
        bits.append('<a href="%s%s">%s</a>' % (root, p[1], esc(p[0])) if len(p) > 1 else esc(p[0]))
    return '<div class="crumb">' + ' / '.join(bits) + '</div>'


# ---------------------------------------------------------------- entry page

def entry_page(e):
    root = '../../'
    sibs = [x for x in tier_sort(in_shape(e['shape'])) if x['id'] != e['id']]
    desc = description(e)
    fig = read_fig(e['figname']) if e['figname'] else None

    def ul(items, cls=''):
        return '<ul class="%s">%s</ul>' % (cls, ''.join('<li>%s</li>' % esc(i) for i in items))

    if e.get('defn'):
        body = (
            '<p class="lead">%s</p>'
            '<div class="dyad"><section><h4>How to read it</h4>%s</section>'
            '<section><h4 class="hh">What it hides</h4>%s</section></div>'
            '<div class="dyad"><section><h4>Reach for it when</h4>%s</section>'
            '<section><h4>Avoid it when</h4>%s</section></div>'
            '<div class="code"><div><span class="lang">R</span><pre><code>%s</code></pre></div>'
            '<div><span class="lang">Python</span><pre><code>%s</code></pre></div></div>' % (
                esc(e['defn']), ul(e['read']), ul(e['hides'], 'hide'),
                ul(e['use'], 'yes'), ul(e['avoid'], 'no'), esc(e['r']), esc(e['py'])))
    else:
        body = ('<p class="stubnote">Catalogued and classified, not yet written up — it is queued as a '
                '<b>%s</b> entry. Its data shape, origin, subject tags and tooling are complete; the '
                'reading guide and the comparison against its %d siblings are still to come.</p>' % (
                    e['depth'], len(sibs)))

    side = ['<aside class="side">',
            '<section><h4>Data shape</h4><p><a href="%sshape/%s/">%s — %s</a></p></section>' % (
                root, e['shape'], e['shape'], esc(e['shape_label'])),
            '<section><h4>How it is made</h4><p>%s</p></section>' % esc(ORIGDESC[e['origin']])]
    if e['areas']:
        side.append('<section><h4>Subject areas</h4><div class="list">%s</div></section>' % ''.join(
            '<a href="%sarea/%s/">%s</a>' % (root, a, esc(AREAS.get(a, a))) for a in e['areas']))
    else:
        side.append('<section><h4>Subject areas</h4><p style="color:var(--muted)">Universal — used across '
                    'every area, so deliberately untagged.</p></section>')
    if e['tags']:
        side.append('<section><h4>Subject tags</h4><div class="tagrow">%s</div></section>' % ''.join(
            '<a class="pill" href="%sbrowse/?tag=%s">%s</a>' % (root, t, esc(TAGNAME.get(t, t)))
            for t in e['tags']))
    side.append('<section><h4>%s</h4><div class="toollist">%s</div></section>' % (
        'Technique' if e['origin'] == 'L' else 'Tools', '<br>'.join(esc(t) for t in e['tools'])))
    if sibs:
        side.append('<section><h4>Alternatives from the same data</h4><div class="sibs">%s%s</div></section>' % (
            ''.join('<a href="%splot/%s/">%s</a>' % (root, s['slug'], esc(s['name'])) for s in sibs[:14]),
            ('<a href="%sshape/%s/" style="color:var(--series-1)">all %d →</a>' % (root, e['shape'], len(sibs)))
            if len(sibs) > 14 else ''))
    side.append('</aside>')

    aliases = [a.strip() for a in e['alias'].split(';') if a.strip()]
    ld = {
        '@context': 'https://schema.org',
        '@type': 'DefinedTerm',
        '@id': BASE + '/plot/' + e['slug'] + '/',
        'url': BASE + '/plot/' + e['slug'] + '/',
        'name': e['name'],
        'termCode': e['id'],
        'description': desc,
        'inDefinedTermSet': {'@type': 'DefinedTermSet', '@id': BASE + '/',
                             'name': SITE, 'url': BASE + '/'}}
    if aliases:
        ld['alternateName'] = aliases if len(aliases) > 1 else aliases[0]
    crumbs = {
        '@context': 'https://schema.org', '@type': 'BreadcrumbList',
        'itemListElement': [
            {'@type': 'ListItem', 'position': 1, 'name': SITE, 'item': BASE + '/'},
            {'@type': 'ListItem', 'position': 2, 'name': e['shape'] + ' ' + e['shape_label'],
             'item': BASE + '/shape/' + e['shape'] + '/'},
            {'@type': 'ListItem', 'position': 3, 'name': e['name']}]}
    head = ('<script type="application/ld+json">%s</script>\n'
            '<script type="application/ld+json">%s</script>\n' % (
                json.dumps(ld, ensure_ascii=False), json.dumps(crumbs, ensure_ascii=False)))

    figblock = ('<figure class="fig">%s<figcaption class="figcap">%s — generated from synthetic data.'
                '</figcaption></figure>' % (fig, esc(e['name']))) if fig else (
        '<div class="nofig">No figure generated for this entry yet</div>')

    body_html = (
        crumb(root, ('All plots', 'browse/'), (e['shape'] + ' ' + e['shape_label'], 'shape/%s/' % e['shape']), (e['id'],)) +
        '<div class="entry"><div>'
        '<div class="metarow">%s%s%s<a class="pill" href="%sfamily/%s/">%s</a></div>'
        '<h1>%s</h1>%s%s%s</div>%s</div>'
        '<div class="pagenav"><a href="%sshape/%s/">← all %d plots for shape %s</a>'
        '<a href="%sbrowse/">Browse everything →</a></div>' % (
            '<span class="pill o-%s">%s</span>' % (e['origin'], ORIGIN[e['origin']]),
            pill('', TIERLBL[e['tier']]),
            pill('', 'written') if e.get('defn') else pill('', 'planned: ' + e['depth']),
            root, FAMSLUG[e['fam']], esc(famname(e['fam'])),
            esc(e['name']),
            ('<p class="alias">%s</p>' % esc(e['alias'])) if e['alias'] else '',
            figblock, body, ''.join(side),
            root, e['shape'], len(sibs) + 1, e['shape'], root))

    title = '%s — what it shows and what it hides | %s' % (e['name'], SITE)
    return page('plot/%s/index.html' % e['slug'], title, desc, body_html, head, og_type='article')


def redirect_stub(e):
    """Old /plot/P400/ URLs kept alive. GitHub Pages cannot serve a real 301,
    so this is a canonical-tagged, noindex refresh stub."""
    target = BASE + '/plot/' + e['slug'] + '/'
    path = 'plot/%s/index.html' % e['id']
    doc = f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>{esc(e['name'])} — moved</title>
<link rel="canonical" href="{esc(target)}">
<meta name="robots" content="noindex,follow">
<meta http-equiv="refresh" content="0; url=../{e['slug']}/">
</head>
<body>
<p>This entry now lives at <a href="../{e['slug']}/">{esc(e['name'])}</a>.</p>
<script>location.replace('../{e['slug']}/' + location.search + location.hash);</script>
</body>
</html>
'''
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    open(full, 'w').write(doc)


# ---------------------------------------------------------------- listings

def home():
    root = ''
    c = lambda o: sum(1 for e in ENTRIES if e['origin'] == o)
    fams = sorted(((f, [e for e in ENTRIES if e['fam'] == f]) for f in FAMS),
                  key=lambda x: -len(x[1]))[:12]
    hero = read_fig('hero-comparison')
    body = f'''<section class="hero">
<p class="eyebrow">A reference atlas of scientific figures</p>
<h1>Every plot, and what it hides</h1>
<p class="lede">{len(ENTRIES)} plot types across the sciences — indexed not by what they look like,
but by the shape of the data that produces them, so you can see what you could have drawn instead.</p>
<div class="counts">
 <div><b>{len(ENTRIES)}</b><span>plot types</span></div>
 <div><b>{len(SHAPES)}</b><span>data shapes</span></div>
 <div><b>{len(AREAS)}</b><span>subject areas</span></div>
 <div><b>{len(TAGNAME)}</b><span>subject tags</span></div>
</div></section>
<div class="doors">
 <a class="door" href="shapes/"><h3>By data shape</h3>
  <p>Start from the table you have. Every plot that consumes the same structure is an
  alternative you could be drawing — that is where the comparisons live.</p></a>
 <a class="door" href="subjects/"><h3>By subject</h3>
  <p>{len(AREAS)} areas and {len(TAGNAME)} nested tags, from clinical trials to geochronology. Basic plots are
  deliberately untagged so subject filters stay useful.</p></a>
 <a class="door" href="origins/"><h3>By how it is made</h3>
  <p>{c('D')} computable from a data table, {c('H')} rendered by instrument software,
  {c('L')} produced physically in a lab, {c('C')} drawn by hand.</p></a>
</div>
<section class="sec"><div class="sech"><span>Start here</span>
<h2>Two of these groups have identical box plots</h2></div>
<p class="intro">140 patients per arm, same biomarker. Their five-number summaries agree to within
0.7&nbsp;ng/mL; a t-test gives p&nbsp;=&nbsp;0.98. One arm splits cleanly into responders and
non-responders — and the box plot cannot show it.</p>
<figure class="fig">{hero or ''}</figure>
<p class="intro" style="margin-top:18px">This is what the atlas is for.
<a href="shape/S02/">See all twelve plots for this data shape →</a></p>
</section>
<section class="sec"><div class="sech"><span>The largest families</span><h2>Browse by function</h2></div>
<div class="cards c3">{''.join(
    '<a class="card" href="family/%s/"><span class="cid">%s</span><h4>%s</h4><p>%d plot types</p></a>'
    % (FAMSLUG[f], f[:3], esc(famname(f)), len(l)) for f, l in fams)}</div>
</section>'''
    return page('index.html', 'Plot Atlas — %d scientific plot types, indexed by data shape' % len(ENTRIES),
                'A reference catalogue of %d scientific plot types indexed by the shape of the data that '
                'produces them, so that for any figure you can see the alternatives and what each one hides.'
                % len(ENTRIES), body)


def shapes_index():
    root = '../'
    order = sorted(SHAPES)
    body = (crumb(root, ('Data shapes',)) +
            sech('%d shapes' % len(SHAPES), 'Start from the data you have') +
            '<p class="intro">A plot’s data shape is the structure of its input table. Plots that share a '
            'shape are substitutes — they consume the same data and discard different parts of it. Four of these '
            'are not data shapes at all: lab output, schematics, text and 3-D structure have no input table, and '
            'group instead by what the figure is evidence of.</p>' +
            '<div class="cards c3">%s</div>' % ''.join(
                '<a class="card" href="%sshape/%s/"><span class="cid">%s</span><h4>%s</h4>'
                '<p>%d plot%s</p></a>' % (root, s, s, esc(SHAPES[s]), len(in_shape(s)),
                                          's' if len(in_shape(s)) > 1 else '')
                for s in order))
    return page('shapes/index.html', 'The %d data shapes | %s' % (len(SHAPES), SITE),
                'Every plot in the atlas is keyed to the structure of its input table. %d shapes, from one '
                'continuous variable to time-to-event with censoring — plots sharing a shape are substitutes.'
                % len(SHAPES), body, nav_on='shapes/')


CAPMARK = {'yes': ('✓', 'D'), 'partial': ('~', 'H'), 'no': ('✕', 'C')}


def shape_page(sid):
    root = '../../'
    lst = tier_sort(in_shape(sid))
    label = SHAPES[sid]
    extra = ''
    if sid == 'S02':
        deep = [e for e in lst if e.get('caps')]
        extra = ('<section class="sec"><div class="sech"><span>The comparison</span>'
                 '<h2>What each plot keeps and discards</h2></div>'
                 '<div class="tablewrap"><table><thead><tr><th>Plot</th>%s</tr></thead><tbody>%s'
                 '</tbody></table></div><div class="legend"><span>✓ shown</span>'
                 '<span>~ partial or indirect</span><span>✕ not shown</span></div></section>' % (
                     ''.join('<th>%s</th>' % c[1] for c in CAPCOLS),
                     ''.join('<tr><td class="tname"><a href="%splot/%s/">%s</a></td>%s</tr>' % (
                         root, e['slug'], esc(e['name']),
                         ''.join('<td style="text-align:center"><span class="pill o-%s" style="border-radius:50%%;'
                                 'width:22px;height:22px;display:inline-flex;align-items:center;'
                                 'justify-content:center">%s</span></td>' % (
                                     CAPMARK[e['caps'][c[0]]][1], CAPMARK[e['caps'][c[0]]][0])
                                 for c in CAPCOLS)) for e in deep)))
    hero = ''
    if sid == 'S02':
        hero = ('<p class="intro">One continuous measurement and one grouping column — the most common table '
                'in experimental science, and the one where the choice of plot does the most damage.</p>'
                '<figure class="fig">%s</figure>' % (read_fig('hero-comparison') or ''))
    body = (crumb(root, ('Data shapes', 'shapes/'), (sid,)) +
            sech('Shape %s · %d plots' % (sid, len(lst)), label) + hero + extra +
            '<section class="sec"><div class="sech"><span>All %d</span><h2>Plots for this shape</h2></div>%s</section>'
            % (len(lst), table(lst, root)))
    names = ', '.join(e['name'] for e in lst[:6])
    return page('shape/%s/index.html' % sid, '%s — %d plots for this data shape | %s' % (label, len(lst), SITE),
                trim('%d plot types consume this data shape (%s): %s. They are substitutes, and each discards '
                     'something different.' % (len(lst), label[0].lower() + label[1:], names)),
                body, nav_on='shapes/')


def subjects_index():
    root = '../'
    body = (crumb(root, ('Subjects',)) +
            sech('%d areas · %d tags' % (len(AREAS), len(TAGNAME)), 'Browse by subject') +
            '<p class="intro">Grounded in the Nature subject ontology merged with the Elsevier journal '
            'taxonomy. Universal plots — histograms, scatter plots, box plots — carry no subject tags at all: '
            'tagging them everywhere would make every filter return the same results.</p>' +
            '<div class="cards">%s</div>' % ''.join(
                '<a class="card" href="%sarea/%s/"><span class="cid">%s</span><h4>%s</h4>'
                '<p>%d plots · %d tags</p></a>' % (
                    root, c, c, esc(n), sum(1 for e in ENTRIES if c in e['areas']), len(AREATAGS[c]))
                for c, n in AREAS.items()))
    return page('subjects/index.html', 'Plots by subject area | %s' % SITE,
                'Six subject areas and %d nested tags, from clinical trials to geochronology. Universal plots '
                'carry no subject tags so that every filter stays useful.' % len(TAGNAME), body, nav_on='subjects/')


def area_page(code):
    root = '../../'
    lst = tier_sort([e for e in ENTRIES if code in e['areas']])
    tc = {}
    for e in lst:
        for t in e['tags']:
            if t in AREATAGS[code]:
                tc[t] = tc.get(t, 0) + 1
    tags = sorted(tc.items(), key=lambda x: -x[1])
    body = (crumb(root, ('Subjects', 'subjects/'), (code,)) +
            sech('%s · %d plots' % (code, len(lst)), AREAS[code]) +
            (('<p class="intro">Most-used subject tags in this area:</p><div class="tagrow" '
              'style="margin-bottom:26px">%s</div>' % ''.join(
                  '<a class="pill" href="%sbrowse/?tag=%s">%s · %d</a>' % (root, t, esc(TAGNAME.get(t, t)), n)
                  for t, n in tags[:18])) if tags else '') +
            table(lst, root))
    return page('area/%s/index.html' % code, '%s — %d plot types | %s' % (AREAS[code], len(lst), SITE),
                trim('%d plot types tagged to %s, ranked by how broadly each is used. Commonest tags: %s.' % (
                    len(lst), AREAS[code], ', '.join(TAGNAME.get(t, t) for t, _ in tags[:4]))),
                body, nav_on='subjects/')


def origins_index():
    root = '../'
    body = (crumb(root, ('Origin',)) + sech('4 classes', 'How the figure is made') +
            '<p class="intro">Most glossaries assume every figure can be plotted from a spreadsheet. Most '
            'cannot. The hybrid class is the one usually missed — a mass spectrum or an MRI is neither '
            'hand-drawn nor plottable from a table; an instrument emits a raw signal and software renders it.</p>' +
            '<div class="cards">%s</div>' % ''.join(
                '<a class="card" href="%sorigin/%s/"><span class="cid">%s</span><h4>%s</h4><p>%d plots — %s</p></a>'
                % (root, c, c, esc(n), sum(1 for e in ENTRIES if e['origin'] == c), esc(ORIGDESC[c]))
                for c, n in ORIGIN.items()))
    return page('origins/index.html', 'Plots by how the figure is made | %s' % SITE,
                'Four origin classes: computable from a data table, rendered by instrument software, produced '
                'physically in a lab, or drawn by hand. The hybrid class is the one most glossaries miss.',
                body, nav_on='origins/')


def origin_page(code):
    root = '../../'
    lst = tier_sort([e for e in ENTRIES if e['origin'] == code])
    body = (crumb(root, ('Origin', 'origins/'), (code,)) +
            sech('%s · %d plots' % (code, len(lst)), ORIGIN[code]) +
            '<p class="intro">%s</p>' % esc(ORIGDESC[code]) + table(lst, root))
    return page('origin/%s/index.html' % code, '%s figures — %d plot types | %s' % (ORIGIN[code], len(lst), SITE),
                trim('%d plot types in the %s class. %s Examples: %s.' % (
                    len(lst), ORIGIN[code].lower(), ORIGDESC[code],
                    ', '.join(e['name'] for e in lst[:5]))), body, nav_on='origins/')


def families_index():
    root = '../'
    body = (crumb(root, ('Families',)) + sech('%d families' % len(FAMS), 'Browse by function') +
            '<p class="intro">Family answers <em>what kind of thing is this</em>, for navigation. Data shape '
            'answers <em>what could I use instead</em>, for deciding. They are deliberately different axes: a '
            'volcano plot is a genomics figure by family and a two-continuous-variable plot by shape.</p>' +
            '<div class="cards c3">%s</div>' % ''.join(
                '<a class="card" href="%sfamily/%s/"><span class="cid">%s</span><h4>%s</h4><p>%d plot types</p></a>'
                % (root, FAMSLUG[f], f[:3], esc(famname(f)), sum(1 for e in ENTRIES if e['fam'] == f))
                for f in FAMS))
    return page('families/index.html', 'Plots by family | %s' % SITE,
                '%d functional families, from distributions and regression diagnostics to genomics, '
                'geoscience and signal traces.' % len(FAMS), body, nav_on='families/')


def family_page(f):
    root = '../../'
    lst = tier_sort([e for e in ENTRIES if e['fam'] == f])
    body = (crumb(root, ('Families', 'families/'), (f[:3],)) +
            sech('%s · %d plots' % (f[:3], len(lst)), famname(f)) + table(lst, root))
    return page('family/%s/index.html' % FAMSLUG[f], '%s — %d plot types | %s' % (famname(f), len(lst), SITE),
                trim('%d plot types in the %s family: %s.' % (
                    len(lst), famname(f).lower(), ', '.join(e['name'] for e in lst[:6]))),
                body, nav_on='families/')


def browse_page():
    root = '../'
    body = (crumb(root, ('All plots',)) +
            sech('%d plot types' % len(ENTRIES), 'Browse everything') +
            '<div class="browse"><div class="facets" id="facets"></div><div><div id="results">' +
            '<div class="resbar"><b>%d</b><span style="color:var(--muted);font-size:13px">of %d</span></div>' % (
                len(ENTRIES), len(ENTRIES)) +
            table(sorted(ENTRIES, key=lambda e: e['id']), root) + '</div></div></div>')
    return page('browse/index.html', 'All %d plot types | %s' % (len(ENTRIES), SITE),
                'The complete catalogue of %d scientific plot types, filterable by data shape, subject area, '
                'how the figure is made and how broadly it is used.' % len(ENTRIES), body, nav_on='browse/')


def about_page():
    root = '../'
    n = lambda k: sum(1 for e in ENTRIES if e['depth'] == k)
    written = sum(1 for e in ENTRIES if e.get('defn'))
    figs = sum(1 for e in ENTRIES if e['figname'])
    body = (crumb(root, ('About',)) + sech('About', 'What this is, and what it is not yet') +
            f'''<div style="max-width:66ch;color:var(--ink-2)">
<p>A catalogue of {len(ENTRIES)} plot types used across the sciences, classified four ways: by function
({len(FAMS)} families), by the shape of the data that produces them ({len(SHAPES)} shapes), by how the figure is
physically made (4 origin classes), and by subject ({len(AREAS)} areas, {len(TAGNAME)} nested tags).</p>
<p>The organising idea is the <a href="{root}shapes/">data shape</a>. Two plots are alternatives if they
consume the same table. That relation is authored once per shape rather than once per pair, and it
supports the question people actually arrive with — <em>I have this kind of data, what could I draw?</em></p>
<h3 style="font-size:1.15rem;margin:26px 0 8px">Current state</h3>
<p>All {len(ENTRIES)} entries are catalogued, classified and searchable, and each has its own page.
Written depth follows three tiers: <b>{n('deep')} deep</b>, <b>{n('standard')} standard</b>,
<b>{n('stub')} stub</b>. <b>{written}</b> entries are fully written; <b>{figs}</b> have a generated figure.
The remaining {len(ENTRIES) - written} pages carry their classification, tooling and alternatives, and say
plainly that the written guidance is still missing.</p>
<p>Every figure is generated from synthetic data by script, never copied, so nothing here carries a
licence restriction. The colour palette is validated for colour-vision deficiency in both themes.</p>
<h3 style="font-size:1.15rem;margin:26px 0 8px">Known gaps</h3>
<p>Most entries have no figure yet. Most have no written guidance yet. Meta descriptions on unwritten
entries are composed from the entry's own classification rather than from a definition sentence, because
the definition has not been written. Package references were checked against the live CRAN and
Bioconductor indexes, but 34 cited packages are archived and need substitutes. Subject rankings are
estimates, not measured publication frequencies.</p>
<h3 style="font-size:1.15rem;margin:26px 0 8px">How it is built</h3>
<p>The site is pre-rendered by a Python script into static HTML — one file per entry, no framework and no
server. <a href="{root}sitemap-page/">Every page is listed here</a>.</p>
</div>''')
    return page('about/index.html', 'About the Plot Atlas — what is finished and what is not',
                'What the Plot Atlas covers, how the four classification axes work, and an honest account of '
                'what is written, what is illustrated and what is still only catalogued.', body, nav_on='about/')


def sitemap_page():
    root = '../'
    groups = {}
    for e in sorted(ENTRIES, key=lambda x: x['name']):
        groups.setdefault(e['name'][0].upper(), []).append(e)
    body = (crumb(root, ('Site index',)) + sech('Every page', 'Site index') +
            '<p class="intro">One link per catalogue entry, alphabetically, plus every listing page. '
            'The machine-readable version is <a href="%ssitemap.xml">sitemap.xml</a>.</p>' % root +
            '<section class="sec"><div class="sech"><span>Listings</span><h2>Indexes</h2></div>'
            '<div class="tocgrid">%s%s%s%s</div></section>' % (
                ''.join('<a href="%sshape/%s/">%s — %s</a>' % (root, s, s, esc(SHAPES[s])) for s in sorted(SHAPES)),
                ''.join('<a href="%sarea/%s/">%s</a>' % (root, c, esc(n)) for c, n in AREAS.items()),
                ''.join('<a href="%sorigin/%s/">%s</a>' % (root, c, esc(n)) for c, n in ORIGIN.items()),
                ''.join('<a href="%sfamily/%s/">%s</a>' % (root, FAMSLUG[f], esc(famname(f))) for f in FAMS)) +
            ''.join('<section class="sec"><div class="sech"><span>%s</span><h2>%d entries</h2></div>'
                    '<div class="sitemapcols">%s</div></section>' % (
                        letter, len(lst), ''.join('<a href="%splot/%s/">%s</a>' % (root, e['slug'], esc(e['name']))
                                                  for e in lst))
                    for letter, lst in sorted(groups.items())))
    return page('sitemap-page/index.html', 'Site index — every page in the atlas | %s' % SITE,
                'A human-readable index of every page in the Plot Atlas: %d entry pages plus all shape, '
                'subject, origin and family listings.' % len(ENTRIES), body)


def not_found():
    return page('404.html', 'Page not found | %s' % SITE, 'That page does not exist in the Plot Atlas.',
                '<div class="sech"><span>404</span><h1>That page is not here</h1></div>'
                '<p class="intro">The atlas moved from hash routes to real pages. If you followed an old link '
                'it should have redirected; if it did not, try the '
                '<a href="%s/browse/">full catalogue</a> or the <a href="%s/sitemap-page/">site index</a>.</p>'
                % (BASE, BASE))


# ---------------------------------------------------------------- assets

def search_index():
    fam_list = FAMS
    fam_ix = {f: i for i, f in enumerate(fam_list)}
    data = {
        'fam': fam_list,
        'shapes': SHAPES,
        'areas': AREAS,
        'tags': TAGNAME,
        'origin': ORIGIN,
        'e': [{'i': e['id'], 's': e['slug'], 'n': e['name'], 'a': e['alias'],
               'sh': e['shape'], 'o': e['origin'], 'f': fam_ix[e['fam']],
               't': e['tier'], 'd': e['depth'], 'ar': e['areas'], 'tg': e['tags']}
              for e in ENTRIES]}
    p = os.path.join(ROOT, 'assets', 'search-index.json')
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(data, open(p, 'w'), ensure_ascii=False, separators=(',', ':'))
    return os.path.getsize(p)


def sitemap_xml():
    today = datetime.date.today().isoformat()
    urls = []
    for path in PAGES:
        if path == '404.html':
            continue
        loc = BASE + '/' + path.replace('index.html', '')
        pri = '1.0' if path == 'index.html' else ('0.8' if path.startswith('plot/') else '0.6')
        urls.append('<url><loc>%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>' % (loc, today, pri))
    xml = ('<?xml version="1.0" encoding="UTF-8"?>\n<urlset '
           'xmlns="http://www.sitemap.org/schemas/sitemap/0.9">\n' + '\n'.join(urls) + '\n</urlset>\n')
    xml = xml.replace('www.sitemap.org', 'www.sitemaps.org')
    open(os.path.join(ROOT, 'sitemap.xml'), 'w').write(xml)
    open(os.path.join(ROOT, 'robots.txt'), 'w').write(
        'User-agent: *\nAllow: /\n\nSitemap: %s/sitemap.xml\n' % BASE)
    return len(urls)


# ---------------------------------------------------------------- main

def clean():
    for d in ('plot', 'shape', 'area', 'origin', 'family', 'shapes', 'subjects', 'origins',
              'families', 'browse', 'about', 'sitemap-page', 'assets'):
        p = os.path.join(ROOT, d)
        if os.path.isdir(p):
            shutil.rmtree(p)


def main():
    clean()
    os.makedirs(os.path.join(ROOT, 'assets'), exist_ok=True)
    shutil.copy(os.path.join(HERE, 'atlas.css'), os.path.join(ROOT, 'assets', 'atlas.css'))
    shutil.copy(os.path.join(HERE, 'site.js'), os.path.join(ROOT, 'assets', 'site.js'))
    open(os.path.join(ROOT, 'assets', '.nojekyll'), 'w').write('')
    open(os.path.join(ROOT, '.nojekyll'), 'w').write('')

    home()
    biggest = (0, '')
    for e in ENTRIES:
        n = entry_page(e)
        redirect_stub(e)
        if n > biggest[0]:
            biggest = (n, e['slug'])
    shapes_index()
    for s in sorted(SHAPES):
        shape_page(s)
    subjects_index()
    for c in AREAS:
        area_page(c)
    origins_index()
    for c in ORIGIN:
        origin_page(c)
    families_index()
    for f in FAMS:
        family_page(f)
    browse_page()
    about_page()
    sitemap_page()
    not_found()

    idx = search_index()
    n = sitemap_xml()
    print('pages          %d' % len(PAGES))
    print('redirect stubs %d' % len(ENTRIES))
    print('sitemap urls   %d' % n)
    print('search index   %.0f KB' % (idx / 1024))
    print('heaviest page  %.0f KB  (plot/%s/)' % (biggest[0] / 1024, biggest[1]))


if __name__ == '__main__':
    main()
