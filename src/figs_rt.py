"""Radiotherapy and medical physics figures (P813–P823).

Every beam figure here comes from one dose model, so the percentage depth dose
curve really is a line through the isodose surface and the beam profile really
is a horizontal cut of it. All numbers are synthetic and illustrative: the
shapes are physically faithful, the values are not measurements.

Run:  python3 src/figs_rt.py
"""
import numpy as np
from scipy import optimize, ndimage, special
from scipy.interpolate import PchipInterpolator
from scipy.stats import norm as stats_norm
import matplotlib.pyplot as plt
from figbase import DATA, ACC, AXIS, SURF, MUTE, D2, clean, save, F

rng = np.random.default_rng(19)


# ====================================================================
#  One electron beam model, used by P813, P814, P817, P820
# ====================================================================
# R50, the depth of 50% dose, is close to E/2.33 in water and sets the whole
# horizontal scale. d_max moves deeper up to about 15 MeV and then comes back
# toward the surface — that non-monotonicity is the reading trap the entry
# warns about. The tail past the practical range is bremsstrahlung and grows
# with energy.
BEAM = {  # MeV: (d_max cm, surface dose %, bremsstrahlung tail %)
    7:  (1.6, 78, 0.6),
    9:  (2.1, 82, 1.0),
    15: (3.1, 90, 2.1),
    18: (3.0, 93, 2.9),
    25: (2.5, 96, 4.4),
}
_PDD_CACHE = {}


def _pdd_curve(E):
    """Monotone interpolant through the depths a physicist would quote:
    surface dose, d_max, the 80/50/20/10 % depths, and the practical range."""
    if E in _PDD_CACHE:
        return _PDD_CACHE[E]
    dmax, surf, brem = BEAM[E]
    r50 = E / 2.33
    rp = 1.271 * r50 - 0.23
    pts = [(0.0, float(surf)), (dmax, 100.0)]
    z80 = 0.86 * r50
    if z80 - dmax > 1.2:
        pts.append((dmax + 0.55 * (z80 - dmax), 97.0))
    pts += [(z80, 80.0), (r50, 50.0), (1.09 * r50, 20.0), (1.17 * r50, 10.0),
            (rp, brem + 2.0), (rp + 2.5, float(brem)), (32.0, brem * 0.7)]
    pts.sort()
    zs = np.array([p[0] for p in pts]); ds = np.array([p[1] for p in pts])
    f = PchipInterpolator(zs, ds, extrapolate=True)
    _PDD_CACHE[E] = f
    return f


def pdd(z, E):
    return np.clip(_pdd_curve(E)(np.asarray(z, dtype=float)), 0, None)


def oar(x, z, half_field=3.0):
    """Off-axis ratio. The penumbra widens with depth, which constricts the
    high isodose lines and makes the low ones bulge outward."""
    sig = 0.28 + 0.10 * np.asarray(z, dtype=float)
    return .5 * (special.erf((half_field - x) / (np.sqrt(2) * sig)) +
                 special.erf((half_field + x) / (np.sqrt(2) * sig)))


# -------- P813  percentage depth dose curve --------------------------
z = np.linspace(0, 16, 1200)
f, a = F(5.8, 3.8)
for E in sorted(BEAM):
    al = .34 + .66 * (E - 7) / 18
    a.plot(z, pdd(z, E), color=DATA, lw=1.8, alpha=al, label='%d MeV' % E)
    a.plot([BEAM[E][0]], [100], 'o', ms=3.8, mfc=ACC, mec=SURF, mew=.5, zorder=5)
a.axhline(50, color=MUTE, lw=.7, ls=':')
a.text(15.85, 52.5, 'R$_{50}$', color=MUTE, fontsize=7.4, ha='right')
leg = a.legend(frameon=False, fontsize=7.8, labelcolor=AXIS, loc='upper right',
               title='Electron energy', handlelength=1.6, borderaxespad=.2)
leg.get_title().set_color(AXIS); leg.get_title().set_fontsize(7.6)
a.text(.035, .30, 'red marks $d_{max}$ — it moves deeper\nto about 15 MeV, then back toward\nthe surface',
       transform=a.transAxes, color=ACC, fontsize=7.2, ha='left', va='top')
a.set_ylim(0, 108); a.set_xlim(0, 16)
clean(a, 'Percentage depth dose, electron beams (illustrative)',
      'Depth in water (cm)', 'Dose (% of maximum)')
print('P813 %5.0f KB' % (save(f, 'P813') / 1024))

# -------- P814  isodose curve ----------------------------------------
E = 15
zz = np.linspace(0, 11, 340)
xx = np.linspace(-7, 7, 400)
X, Z = np.meshgrid(xx, zz)
DOSE = pdd(Z, E) * oar(X, Z)
DOSE = DOSE / DOSE.max() * 100

f, a = F(5.6, 4.0)
levels = [10, 20, 30, 50, 70, 80, 90]
cs = a.contour(X, Z, DOSE, levels=levels, colors=DATA,
               linewidths=[.8, .8, .9, 1.2, 1.4, 1.6, 1.9])
# label on the distal end of each contour, where the segment runs horizontal
zc = np.linspace(0, 11, 4000)
axis_dose = pdd(zc, E) * oar(np.zeros_like(zc), zc) / DOSE.max() * 100
def _depth_of(level):
    k = np.argmax(zc > 3.1)
    return zc[k + np.argmin(np.abs(axis_dose[k:] - level))]
spots = [(-0.9, _depth_of(90)), (1.0, _depth_of(70)), (-1.0, _depth_of(50)),
         (1.0, _depth_of(30)), (-1.0, _depth_of(10))]
a.clabel(cs, fmt='%d%%', fontsize=7.2, colors=AXIS, inline_spacing=4, manual=spots)
a.axhline(0, color=AXIS, lw=1.1)
a.plot([-3, 3], [0, 0], color=ACC, lw=2.6, solid_capstyle='butt')
a.text(0, -0.48, '6 × 6 cm field at the surface', color=ACC, fontsize=7.4, ha='center')
a.annotate('high isodoses constrict,\nlow ones bulge — the\npenumbra widens with depth',
           xy=(4.2, 5.4), xytext=(4.7, 8.6), color=MUTE, fontsize=7.2, ha='left',
           va='center', arrowprops=dict(arrowstyle='->', color=MUTE, lw=.8))
a.set_xlim(-7, 7); a.set_ylim(11, -1.25)
clean(a, 'Isodose distribution, 15 MeV electrons (illustrative)',
      'Distance from central axis (cm)', 'Depth in water (cm)', grid=None)
print('P814 %5.0f KB' % (save(f, 'P814') / 1024))

# -------- P817  beam profile -----------------------------------------
d0 = BEAM[E][0]
ref = float(pdd(d0, E))
f, a = F(5.8, 3.5)
pen = []
for d, col, lbl in ((d0, DATA, 'at $d_{max}$ = %.1f cm' % d0), (6.0, D2, 'at 6.0 cm')):
    prof = float(pdd(d, E)) * oar(xx, d) / ref * 100
    a.plot(xx, prof, color=col, lw=1.9, label=lbl)
    right = xx > 0
    top = prof.max()
    x80 = xx[right][np.argmin(np.abs(prof[right] - .80 * top))]
    x20 = xx[right][np.argmin(np.abs(prof[right] - .20 * top))]
    pen.append(x20 - x80)
    for xv, fr in ((x80, .80), (x20, .20)):
        a.plot([xv], [fr * top], 'o', ms=3.4, mfc=ACC, mec=SURF, mew=.5, zorder=5)
a.text(-6.8, 116, '80–20 %% penumbra, marked in red\n  %.1f cm at $d_{max}$\n  %.1f cm at 6.0 cm'
       % (pen[0], pen[1]), color=ACC, fontsize=7.4, ha='left', va='top')
a.legend(frameon=False, fontsize=7.8, labelcolor=AXIS, loc='upper right')
a.set_ylim(0, 122); a.set_xlim(-7, 7)
clean(a, 'Beam profile, 15 MeV electrons (illustrative)',
      'Distance from central axis (cm)', 'Dose (% of $d_{max}$ on axis)')
print('P817 %5.0f KB  (penumbra %.2f / %.2f cm)' % (save(f, 'P817') / 1024, pen[0], pen[1]))


# ====================================================================
#  P815 / P816  dose-volume histogram — the engineered demonstration
# ====================================================================
# Two dose distributions built from the SAME multiset of voxel doses, so their
# dose-volume histograms are identical by construction. One puts the high dose
# in a single contiguous lump; the other spreads it as a rim. For a serial organ
# those are not the same plan, and the DVH cannot tell them apart.
N = 96
gy, gx = np.mgrid[0:N, 0:N]
cx = cy = (N - 1) / 2
rad = np.sqrt((gx - cx) ** 2 + (gy - cy) ** 2)
organ = rad < 40
nvox = int(organ.sum())

vals = np.sort(18 + 44 * (np.linspace(0, 1, nvox) ** 2.3) + rng.normal(0, 0.6, nvox))

keyA = -((gx - (cx - 17)) ** 2 + (gy - (cy - 17)) ** 2)   # one contiguous hot lump
keyB = rad                                                 # hot rim, cool core
doseA = np.full((N, N), np.nan)
doseB = np.full((N, N), np.nan)
for key, out in ((keyA, doseA), (keyB, doseB)):
    order = np.argsort(key[organ])
    slot = np.empty(nvox, dtype=int)
    slot[order] = np.arange(nvox)
    out[organ] = vals[slot]

edges = np.linspace(0, 70, 281)
centres = (edges[:-1] + edges[1:]) / 2


def cumulative_dvh(dmap):
    v = dmap[np.isfinite(dmap)]
    h, _ = np.histogram(v, bins=edges)
    return 100 * (h[::-1].cumsum()[::-1]) / v.size


cumA = cumulative_dvh(doseA)
cumB = cumulative_dvh(doseB)
maxdiff = float(np.abs(cumA - cumB).max())

fig = plt.figure(figsize=(6.4, 4.9)); fig.patch.set_alpha(0)
gs = fig.add_gridspec(2, 3, width_ratios=[1, 1, .055], height_ratios=[.92, 1.20],
                      hspace=.32, wspace=.09, left=.105, right=.945,
                      top=.945, bottom=.105)
im = None
for j, (dmap, ttl) in enumerate(((doseA, 'Plan A — one contiguous hot lump'),
                                 (doseB, 'Plan B — hot rim, cool core'))):
    ax = fig.add_subplot(gs[0, j]); ax.patch.set_alpha(0)
    im = ax.imshow(dmap, cmap='YlGnBu', vmin=16, vmax=64, interpolation='nearest',
                   rasterized=True)
    ax.contour(dmap, levels=[45, 55], colors=AXIS, linewidths=.75)
    ax.set_xticks([]); ax.set_yticks([])
    for s in ax.spines.values():
        s.set_color(AXIS); s.set_linewidth(.8)
    ax.set_title(ttl, color=AXIS, fontsize=8.3, loc='left', pad=5)
cax = fig.add_subplot(gs[0, 2])
cb = fig.colorbar(im, cax=cax)
cb.set_label('Dose (Gy)', color=AXIS, fontsize=7.3, labelpad=3)
cb.ax.tick_params(colors=AXIS, labelsize=6.8)
cb.outline.set_edgecolor(AXIS); cb.outline.set_linewidth(.6)

ax = fig.add_subplot(gs[1, 0:3]); ax.patch.set_alpha(0)
ax.plot(centres, cumA, color=DATA, lw=3.4, label='Plan A')
ax.plot(centres, cumB, color=ACC, lw=1.4, ls=(0, (4, 4)), label='Plan B')
ax.set_ylim(0, 104); ax.set_xlim(0, 70)
clean(ax, 'Cumulative dose–volume histogram — the two plans coincide',
      'Dose (Gy)', 'Volume receiving ≥ dose (%)')
ax.legend(frameon=False, fontsize=7.8, labelcolor=AXIS, loc='lower left')
ax.text(.985, .94, 'largest gap between the two curves: %.2f %% of volume' % maxdiff,
        transform=ax.transAxes, color=MUTE, fontsize=7.4, ha='right', va='top')
print('P815 %5.0f KB  (max DVH difference %.3f %%)'
      % (save(fig, 'P815', tight=False) / 1024, maxdiff))

# -------- P816  differential DVH -------------------------------------
target_vals = rng.normal(60, 1.1, 4000)
f, a = F(5.8, 3.4)
bins = np.linspace(0, 70, 71)
a.hist(vals, bins=bins, color=DATA, alpha=.85, edgecolor=SURF, lw=.4,
       label='Organ at risk — broad, heterogeneous', density=True)
a.hist(target_vals, bins=bins, color=D2, alpha=.85, edgecolor=SURF, lw=.4,
       label='Target — one narrow spike, uniform dose', density=True)
a.legend(frameon=False, fontsize=7.8, labelcolor=AXIS, loc='upper left')
a.set_xlim(0, 70)
clean(a, 'Differential dose–volume histogram (illustrative)',
      'Dose (Gy)', 'Fraction of volume per 1 Gy bin')
print('P816 %5.0f KB' % (save(f, 'P816') / 1024))


# ====================================================================
#  P818 / P819  Bragg peak and spread-out Bragg peak
# ====================================================================
def bragg(zg, R0, spread=0.010):
    """Depth dose for a near-monoenergetic proton beam. The (R0-z)^-0.435 form
    is the standard analytic approximation; the Gaussian smear is range
    straggling plus the beam's own energy spread, which together set the finite
    width of the peak."""
    dz = zg[1] - zg[0]
    gap = R0 - zg
    d = np.where(gap > 0, np.maximum(gap, dz / 2) ** -0.435, 0.0)
    sig = np.hypot(0.012 * R0 ** 0.935, spread * R0 * 1.77)
    d = ndimage.gaussian_filter1d(d, sig / dz)
    return d + 0.09 * (zg < R0)          # small plateau from nuclear reactions


zp = np.linspace(0, 22, 1800)
f, a = F(5.8, 3.6)
b = bragg(zp, 16.0); b = b / b.max() * 100
a.plot(zp, b, color=DATA, lw=1.9, label='Protons, ≈150 MeV')
e18 = pdd(zp, 18); e18 = e18 / e18.max() * 100
a.plot(zp, e18, color=MUTE, lw=1.3, ls='--', label='18 MeV electrons, for contrast')
pk = zp[np.argmax(b)]
a.annotate('Bragg peak', xy=(pk - .4, 86), xytext=(pk - 6.6, 96), color=ACC,
           fontsize=7.8, va='center',
           arrowprops=dict(arrowstyle='->', color=ACC, lw=1))
a.annotate('sharp distal fall-off —\nalmost no exit dose', xy=(pk + 1.0, 5),
           xytext=(pk + 1.8, 44), color=ACC, fontsize=7.8,
           arrowprops=dict(arrowstyle='->', color=ACC, lw=1))
a.legend(frameon=False, fontsize=7.8, labelcolor=AXIS, loc='upper left',
         bbox_to_anchor=(.01, .76))
a.set_ylim(0, 112); a.set_xlim(0, 22)
clean(a, 'Bragg peak curve (illustrative)', 'Depth in water (cm)', 'Relative dose (%)')
print('P818 %5.0f KB' % (save(f, 'P818') / 1024))

# -------- P819  spread-out Bragg peak --------------------------------
ranges = np.linspace(9.4, 15.9, 44)
COMP = np.column_stack([bragg(zp, R) for R in ranges])
lo, hi = 9.7, 15.6
flat = (zp > lo) & (zp < hi)
w, _ = optimize.nnls(COMP[flat], np.ones(flat.sum()))
sobp = COMP.dot(w)
scale = 100 / sobp[flat].mean()
plateau = sobp[flat] * scale
ripple = 100 * (plateau.max() - plateau.min()) / plateau.mean() / 2

f, a = F(5.8, 3.6)
a.axvspan(lo, hi, color=DATA, alpha=.08, lw=0)
for k in range(len(ranges)):
    a.plot(zp, COMP[:, k] * w[k] * scale, color=MUTE, lw=.55, alpha=.38)
a.plot(zp, sobp * scale, color=DATA, lw=2.2)
a.text((lo + hi) / 2, 113, 'target depth', color=AXIS, fontsize=7.6, ha='center')
a.annotate('plateau flat to ±%.1f %%' % ripple, xy=((lo + hi) / 2, 100),
           xytext=((lo + hi) / 2, 72), color=MUTE, fontsize=7.4, ha='center',
           arrowprops=dict(arrowstyle='->', color=MUTE, lw=.8))
a.annotate('the %d component peaks,\neach with its own weight' % len(ranges),
           xy=(14.6, 9), xytext=(3.4, 30), color=MUTE, fontsize=7.4,
           arrowprops=dict(arrowstyle='->', color=MUTE, lw=.8))
a.annotate('entrance dose is the price\nof the flat plateau', xy=(0.5, 61),
           xytext=(0.5, 112), color=ACC, fontsize=7.4, va='top', ha='left',
           arrowprops=dict(arrowstyle='->', color=ACC, lw=.9))
a.set_ylim(0, 120); a.set_xlim(0, 20)
clean(a, 'Spread-out Bragg peak — %d weighted beams (illustrative)' % len(ranges),
      'Depth in water (cm)', 'Dose (% of plateau)')
print('P819 %5.0f KB  (ripple ±%.2f %%)' % (save(f, 'P819') / 1024, ripple))


# ====================================================================
#  P820  gamma index map
# ====================================================================
# Reference is the 15 MeV plane above. Evaluated is the same delivery with a
# 1.4 mm setup shift, a 1.5 % output gain and detector noise — errors small
# enough to pass everywhere except where the dose gradient is steep.
gz = np.linspace(0.4, 9.2, 90)
gx_ = np.linspace(-6.0, 6.0, 110)
GX, GZ = np.meshgrid(gx_, gz)
RAW = pdd(GZ, 15) * oar(GX, GZ)
norm = RAW.max()
REF = RAW / norm * 100
EVAL = (pdd(GZ + 0.12, 15) * oar(GX - 0.07, GZ + 0.12)) / norm * 100 * 1.015
EVAL = EVAL + rng.normal(0, 0.30, EVAL.shape)

dta, dd = 0.2, 3.0                      # 2 mm distance-to-agreement, 3 % dose
step_x = gx_[1] - gx_[0]; step_z = gz[1] - gz[0]
win_x = int(np.ceil(3 * dta / step_x)); win_z = int(np.ceil(3 * dta / step_z))
gamma = np.full(REF.shape, np.nan)
for i in range(REF.shape[0]):
    for j in range(REF.shape[1]):
        if REF[i, j] < 10:              # low-dose threshold, as in clinical QA
            continue
        i0, i1 = max(0, i - win_z), min(REF.shape[0], i + win_z + 1)
        j0, j1 = max(0, j - win_x), min(REF.shape[1], j + win_x + 1)
        r2 = (((gz[i0:i1] - gz[i]) ** 2)[:, None] +
              ((gx_[j0:j1] - gx_[j]) ** 2)[None, :]) / dta ** 2
        d2 = ((EVAL[i0:i1, j0:j1] - REF[i, j]) / dd) ** 2
        gamma[i, j] = np.sqrt(np.min(r2 + d2))

# the mean must run over evaluated points only — the sub-threshold
# cells are NaN, and counting them as failures understates the rate
_g = gamma[np.isfinite(gamma)]
passing = 100 * np.mean(_g <= 1)
f, a = F(5.8, 3.8)
cmap = plt.get_cmap('RdYlBu_r').copy()
cmap.set_bad(alpha=0)
im = a.imshow(gamma, cmap=cmap, vmin=0, vmax=2, origin='upper',
              extent=[gx_[0], gx_[-1], gz[-1], gz[0]], aspect='auto',
              interpolation='nearest', rasterized=True)
a.contour(gx_, gz, np.nan_to_num(gamma), levels=[1.0], colors=AXIS, linewidths=1.0)
cb = f.colorbar(im, ax=a, pad=.02, fraction=.045)
cb.set_label('γ  (3 % / 2 mm)', color=AXIS, fontsize=8)
cb.ax.tick_params(colors=AXIS, labelsize=7.5)
cb.outline.set_edgecolor(AXIS); cb.outline.set_linewidth(.6)
a.text(.02, .06, 'blank = below the 10 % dose threshold', transform=a.transAxes,
       color=MUTE, fontsize=7.2)
a.set_ylim(gz[-1], gz[0]); a.set_xlim(gx_[0], gx_[-1])
clean(a, 'Gamma index map — %.1f %% pass, against a 95 %% criterion' % passing,
      'Distance from central axis (cm)', 'Depth in water (cm)', grid=None)
print('P820 %5.0f KB  (%.1f %% pass)' % (save(f, 'P820') / 1024, passing))


# ====================================================================
#  P821 / P822  TCP and NTCP
# ====================================================================
d = np.linspace(30, 100, 800)
D50, g50 = 61.0, 2.6
tcp = 1 / (1 + (D50 / d) ** (4 * g50))
TD50, mm = 86.0, 0.13
ntcp = stats_norm.cdf((d - TD50) / (mm * TD50))

f, a = F(5.8, 3.4)
a.plot(d, 100 * tcp, color=DATA, lw=2.1)
a.plot([D50], [50], 'o', ms=4.6, mfc=ACC, mec=SURF, mew=.6, zorder=5)
a.annotate('D$_{50}$ = %.0f Gy,  γ$_{50}$ = %.1f' % (D50, g50), xy=(D50 - .7, 50),
           xytext=(37, 68), color=ACC, fontsize=7.8, va='center',
           arrowprops=dict(arrowstyle='->', color=ACC, lw=1))
a.text(.985, .06, 'a fitted model, not measured points', transform=a.transAxes,
       color=MUTE, fontsize=7.4, ha='right')
a.set_ylim(0, 104); a.set_xlim(30, 100)
clean(a, 'Tumour control probability (model, illustrative)',
      'Total dose (Gy)', 'Probability of control (%)')
print('P821 %5.0f KB' % (save(f, 'P821') / 1024))

pplus = tcp * (1 - ntcp)
opt = d[np.argmax(pplus)]
f, a = F(5.8, 3.5)
win = (tcp > .5) & (ntcp < .05)
if win.any():
    a.axvspan(d[win][0], d[win][-1], color=DATA, alpha=.10, lw=0)
    a.text((d[win][0] + d[win][-1]) / 2, 100,
           'therapeutic window\n%.0f–%.0f Gy' % (d[win][0], d[win][-1]),
           color=AXIS, fontsize=7.6, ha='center', va='top')
a.plot(d, 100 * tcp, color=DATA, lw=2.1, label='TCP — tumour control')
a.plot(d, 100 * ntcp, color=D2, lw=2.1, label='NTCP — complication')
a.plot(d, 100 * pplus, color=MUTE, lw=1.4, ls='--', label='P+ = TCP (1 − NTCP)')
a.plot([opt], [100 * pplus.max()], 'o', ms=4.4, mfc=ACC, mec=SURF, mew=.6, zorder=5)
a.annotate('P+ peaks at %.0f Gy' % opt, xy=(opt + .5, 100 * pplus.max()),
           xytext=(opt + 7, 100 * pplus.max() - 20), color=ACC, fontsize=7.6,
           arrowprops=dict(arrowstyle='->', color=ACC, lw=1))
a.legend(frameon=False, fontsize=7.7, labelcolor=AXIS, loc='center left',
         bbox_to_anchor=(.01, .38))
a.set_ylim(0, 106); a.set_xlim(30, 100)
clean(a, 'TCP and NTCP on one axis (model, illustrative)',
      'Total dose (Gy)', 'Probability (%)')
print('P822 %5.0f KB  (window %.0f–%.0f Gy, P+ peak %.0f Gy)'
      % (save(f, 'P822') / 1024, d[win][0], d[win][-1], opt))


# ====================================================================
#  P823  linac output constancy chart
# ====================================================================
nd = 130
day = np.arange(nd)
out = 100 * rng.normal(0, 0.0035, nd)
out[62:105] += np.linspace(0, 2.6, 43)         # slow drift out of tolerance
out[105:] += 0.15                              # after recalibration
f, a = F(5.9, 3.4)
a.plot(day, out, color=DATA, lw=1.0, marker='o', ms=2.6, mfc=DATA, mec=SURF, mew=.3)
bad = np.abs(out) > 2
a.plot(day[bad], out[bad], 'o', ms=6.2, mfc='none', mec=ACC, mew=1.2, zorder=5)
for lim, col, ls, lbl in ((2, MUTE, '--', 'tolerance ±2 %'),
                          (3, ACC, '-', 'action ±3 %')):
    a.axhline(lim, color=col, lw=1.0, ls=ls)
    a.axhline(-lim, color=col, lw=1.0, ls=ls)
    a.text(nd - 1, lim + .14, lbl, color=col, fontsize=7.2, ha='right')
a.axhline(0, color=AXIS, lw=.8)
a.axvline(104.5, color=AXIS, lw=.9, ls=':')
a.text(106, -3.9, 'recalibration', color=AXIS, fontsize=7.6, ha='left')
a.text(2, -3.9, '%d readings over tolerance before it' % int(bad.sum()),
       color=ACC, fontsize=7.6, ha='left')
a.set_ylim(-4.6, 4.6); a.set_xlim(-3, nd + 1)
clean(a, 'Linac output constancy, 6 MV photons (illustrative)',
      'Working day', 'Deviation from baseline (%)')
print('P823 %5.0f KB  (%d readings out of tolerance)'
      % (save(f, 'P823') / 1024, int(bad.sum())))
