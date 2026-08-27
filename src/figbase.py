"""Shared figure machinery: palette, axis styling, and the sentinel-colour save.

Figures are drawn with literal sentinel colours and string-replaced to CSS custom
properties on save, so one SVG set re-themes with the page instead of needing a
light copy and a dark copy. Those variables only resolve when the SVG is inlined
in the document — never through <img src>.
"""
import os
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = os.path.dirname(os.path.abspath(__file__))
FIGDIR = os.path.join(HERE, 'fig')

DATA = '#2a78d6'; ACC = '#e34948'; AXIS = '#52514e'; SURF = '#fcfcfb'; MUTE = '#8a8a85'
D2 = '#eb6834'
SENT = {DATA: 'var(--series-1)', ACC: 'var(--accent)', AXIS: 'var(--ink)',
        SURF: 'var(--surface-1)', MUTE: 'var(--muted)', D2: 'var(--series-2)'}

rng = np.random.default_rng(7)
plt.rcParams.update({'font.size': 8.5, 'axes.titlesize': 9.5})


def clean(ax, title=None, xl=None, yl=None, grid='y', spines=('left', 'bottom')):
    for s in ('top', 'right', 'left', 'bottom'):
        ax.spines[s].set_visible(s in spines)
        if s in spines:
            ax.spines[s].set_color(AXIS); ax.spines[s].set_linewidth(.8)
    ax.tick_params(colors=AXIS, labelsize=8, length=3, width=.8)
    if grid == 'y':
        ax.yaxis.grid(True, color=AXIS, alpha=.16, lw=.7)
    elif grid == 'x':
        ax.xaxis.grid(True, color=AXIS, alpha=.16, lw=.7)
    elif grid == 'both':
        ax.grid(True, color=AXIS, alpha=.16, lw=.7)
    ax.set_axisbelow(True)
    if title:
        ax.set_title(title, color=AXIS, loc='left', pad=8)
    if xl:
        ax.set_xlabel(xl, color=AXIS, fontsize=8.5)
    if yl:
        ax.set_ylabel(yl, color=AXIS, fontsize=8.5)


def save(fig, name, tight=True):
    if tight:
        fig.tight_layout()
    os.makedirs(FIGDIR, exist_ok=True)
    p = os.path.join(FIGDIR, name + '.svg')
    fig.savefig(p, format='svg', transparent=True, dpi=140)
    plt.close(fig)
    s = open(p).read()
    for a, b in SENT.items():
        s = s.replace(a, b).replace(a.upper(), b)
    open(p, 'w').write(s)
    return os.path.getsize(p)


def F(w=5.6, h=3.4):
    fig, ax = plt.subplots(figsize=(w, h))
    fig.patch.set_alpha(0)
    ax.patch.set_alpha(0)
    return fig, ax
