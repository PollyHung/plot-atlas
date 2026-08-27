#!/usr/bin/env python3
"""Rewrite the counts table in PROGRESS.md from the actual data.

Only the block between the TABLE markers is touched; the batch log and the
notes below it are hand-maintained.
"""
import csv, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from content import ENTRIES as WRITTEN

rows = list(csv.DictReader(open(os.path.join(ROOT, 'data', 'plots.csv'))))
written = {d['id'] for d in WRITTEN}
altslug = {d['id']: d['slug'] for d in WRITTEN}
figs = {f[:-4] for f in os.listdir(os.path.join(HERE, 'fig')) if f.endswith('.svg')}

tot, wr, fg, label = defaultdict(int), defaultdict(int), defaultdict(int), {}
for r in rows:
    s = r['data_shape']
    tot[s] += 1
    label[s] = r['shape_label']
    if r['id'] in written:
        wr[s] += 1
    if r['id'] in figs or altslug.get(r['id']) in figs:
        fg[s] += 1

lines = ['| Shape | What it is | Entries | Written | Figures |', '|---|---|---:|---:|---:|']
for s in sorted(tot):
    lines.append('| `%s` | %s | %d | %d | %d |' % (s, label[s], tot[s], wr[s], fg[s]))
lines.append('| | **Total** | **%d** | **%d** | **%d** |'
             % (sum(tot.values()), sum(wr.values()), sum(fg.values())))
table = '\n'.join(lines)

p = os.path.join(ROOT, 'PROGRESS.md')
doc = open(p).read()
a, b = '<!-- BEGIN TABLE -->', '<!-- END TABLE -->'
doc = doc[:doc.index(a) + len(a)] + '\n' + table + '\n' + doc[doc.index(b):]
open(p, 'w').write(doc)
print('%d entries · %d written · %d figures' % (sum(tot.values()), sum(wr.values()), sum(fg.values())))
