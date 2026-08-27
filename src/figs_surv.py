"""Shape S17 — time-to-event with censoring. Figures P234-P245.

Every figure here draws the same 800 patients (see survdata.py), so the
comparisons between them mean something: where two of these plots disagree,
the disagreement is about the plot, not about the data.

Run:  python3 src/figs_surv.py
"""
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
from figbase import DATA, ACC, AXIS, SURF, MUTE, D2, clean, save, F
import survlib as S
from survdata import cohort, LABEL, HORIZON

d = cohort()
G = {g: (d['group'] == g) for g in (0, 1)}
COL = {0: D2, 1: DATA}
ANY = (d['cause'] > 0).astype(int)
rng = np.random.default_rng(23)


def stepdraw(ax, ts, ys, **kw):
    ax.step(ts, ys, where='post', **kw)


def censor_ticks(ax, mask, ts, ys, colour):
    t = d['time'][mask][d['cause'][mask] == 0]
    if not len(t):
        return
    ax.plot(t, S.step_at(ts, ys, t), '|', ms=4.5, color=colour, mew=.9, alpha=.85)


# -------- P234  Kaplan-Meier curve -----------------------------------
chi2, p = S.logrank(d['time'], ANY, d['group'])
f, a = F(5.8, 3.8)
for g in (0, 1):
    m = G[g]
    ts, s, lo, hi = S.kaplan_meier(d['time'][m], ANY[m])
    a.fill_between(ts, lo, hi, step='post', color=COL[g], alpha=.14, lw=0)
    stepdraw(a, ts, s, color=COL[g], lw=2.0, label='%s  (n = %d)' % (LABEL[g], m.sum()))
    censor_ticks(a, m, ts, s, COL[g])
a.legend(frameon=False, fontsize=8, labelcolor=AXIS, loc='upper right')
a.text(.03, .10, 'log-rank χ² = %.0f on 1 df, p = %.1e\nticks are censored patients'
       % (chi2, p), transform=a.transAxes, color=MUTE, fontsize=7.4, va='bottom')
a.set_ylim(0, 1.02); a.set_xlim(0, HORIZON)
clean(a, 'Kaplan-Meier estimate of event-free survival (illustrative)',
      'Months since transplant', 'Probability event-free')
print('P234 %5.0f KB' % (save(f, 'P234') / 1024))

# -------- P235  number-at-risk table ---------------------------------
MARKS = np.arange(0, HORIZON + 1, 12)
fig = plt.figure(figsize=(5.8, 4.3)); fig.patch.set_alpha(0)
gs = fig.add_gridspec(2, 1, height_ratios=[3.1, 1], hspace=.06,
                      left=.235, right=.975, top=.925, bottom=.115)
ax = fig.add_subplot(gs[0]); ax.patch.set_alpha(0)
for g in (0, 1):
    m = G[g]
    ts, s, _, _ = S.kaplan_meier(d['time'][m], ANY[m])
    stepdraw(ax, ts, s, color=COL[g], lw=2.0, label=LABEL[g])
    censor_ticks(ax, m, ts, s, COL[g])
ax.legend(frameon=False, fontsize=8, labelcolor=AXIS, loc='upper right')
ax.set_ylim(0, 1.02); ax.set_xlim(-4, HORIZON + 1); ax.set_xticks(MARKS)
ax.set_xticklabels([])
clean(ax, 'The same curve, with the denominator underneath',
      None, 'Probability event-free')
tab = fig.add_subplot(gs[1]); tab.patch.set_alpha(0)
tab.set_xlim(-4, HORIZON + 1); tab.set_ylim(-0.5, 2.1)
for sp in tab.spines.values():
    sp.set_visible(False)
tab.set_yticks([1.0, 0.15])
tab.set_yticklabels([LABEL[1], LABEL[0]], fontsize=7.6)
for lbl, g in zip(tab.get_yticklabels(), (1, 0)):
    lbl.set_color(COL[g])
tab.set_xticks(MARKS)
tab.tick_params(colors=AXIS, labelsize=8, length=0)
tab.set_xlabel('Months since transplant', color=AXIS, fontsize=8.5)
tab.text(-4, 1.85, 'Number still at risk', color=MUTE, fontsize=7.6,
         ha='left', va='bottom')
for row, g in enumerate((1, 0)):
    m = G[g]
    for x in MARKS:
        n = int((d['time'][m] >= x).sum())
        tab.text(x, 1.0 - row * .85, str(n), color=COL[g], fontsize=8,
                 ha='center', va='center')
print('P235 %5.0f KB' % (save(fig, 'P235', tight=False) / 1024))

# -------- P236  cumulative incidence — the demonstration -------------
# The relapse hazard is identical in the two cohorts by construction, so a
# Kaplan-Meier estimate of relapse must agree between them. The proportion who
# actually relapse cannot: in the older cohort most patients die first.
fig = plt.figure(figsize=(6.6, 4.0)); fig.patch.set_alpha(0)
gs = fig.add_gridspec(1, 2, wspace=.24, left=.085, right=.98, top=.80, bottom=.235)
km60, cif60 = {}, {}
for panel, (ttl, kind) in enumerate((
        ('1 − Kaplan-Meier, deaths treated as censoring', 'km'),
        ('Aalen-Johansen cumulative incidence', 'cif'))):
    ax = fig.add_subplot(gs[panel]); ax.patch.set_alpha(0)
    for g in (0, 1):
        m = G[g]
        if kind == 'km':
            ts, s, _, _ = S.kaplan_meier(d['time'][m], (d['cause'][m] == 1).astype(int))
            y = 1 - s
            km60[g] = S.step_at(ts, y, HORIZON)
        else:
            ts, y = S.aalen_johansen(d['time'][m], d['cause'][m], 1)
            cif60[g] = S.step_at(ts, y, HORIZON)
        stepdraw(ax, ts, y, color=COL[g], lw=2.1, label=LABEL[g],
                 alpha=.95 if kind == 'cif' else (1.0 if g == 1 else .8))
    ax.set_ylim(0, .52); ax.set_xlim(0, HORIZON)
    clean(ax, ttl, 'Months since transplant',
          'Probability of relapse' if panel == 0 else None)

axl, axr = fig.axes
h, lb = axl.get_legend_handles_labels()
fig.legend(h, lb, frameon=False, fontsize=8, labelcolor=AXIS, ncol=2,
           loc='lower center', bbox_to_anchor=(.5, .005))
axl.text(.97, .97, 'at 60 months the two cohorts\nagree to %.1f percentage points' %
         (100 * abs(km60[0] - km60[1])), transform=axl.transAxes,
         color=ACC, fontsize=7.6, ha='right', va='top')
axr.annotate('', xy=(HORIZON * .96, cif60[1]), xytext=(HORIZON * .96, cif60[0]),
             arrowprops=dict(arrowstyle='<->', color=ACC, lw=1.2))
axr.text(HORIZON * .55, .46, '%.0f%% of the older cohort actually relapse,\n%.0f%% of the younger'
         % (100 * cif60[0], 100 * cif60[1]),
         color=ACC, fontsize=7.6, ha='center', va='top')
fig.text(.5, .975, 'Same relapse hazard in both cohorts — only the competing mortality differs',
         color=AXIS, fontsize=9.5, ha='center', va='top')
print('P236 %5.0f KB  (1-KM %.3f / %.3f;  CIF %.3f / %.3f)'
      % (save(fig, 'P236', tight=False) / 1024, km60[0], km60[1], cif60[0], cif60[1]))

# -------- P237  Nelson-Aalen cumulative hazard -----------------------
f, a = F(5.8, 3.6)
for g in (0, 1):
    m = G[g]
    ts, H, se = S.nelson_aalen(d['time'][m], ANY[m])
    a.fill_between(ts, H - 1.96 * se, H + 1.96 * se, step='post',
                   color=COL[g], alpha=.14, lw=0)
    stepdraw(a, ts, H, color=COL[g], lw=2.0, label=LABEL[g])
a.legend(frameon=False, fontsize=8, labelcolor=AXIS, loc='upper left')
a.text(.03, .74, 'the slope at any point is the hazard rate',
       transform=a.transAxes, color=MUTE, fontsize=7.4)
a.set_xlim(0, HORIZON)
clean(a, 'Nelson-Aalen cumulative hazard (illustrative)',
      'Months since transplant', 'Cumulative hazard')
print('P237 %5.0f KB' % (save(f, 'P237') / 1024))

# -------- P238  log-minus-log survival plot --------------------------
f, a = F(5.8, 3.6)
for g in (0, 1):
    m = G[g]
    ts, s, _, _ = S.kaplan_meier(d['time'][m], ANY[m])
    ok = (ts > 0) & (s > 0) & (s < 1)
    stepdraw(a, np.log(ts[ok]), np.log(-np.log(s[ok])), color=COL[g], lw=2.0, label=LABEL[g])
a.legend(frameon=False, fontsize=8, labelcolor=AXIS, loc='upper left')
gaps = {}
for tv in (3, 58):
    v = []
    for g in (0, 1):
        m = G[g]
        ts, sv, _, _ = S.kaplan_meier(d['time'][m], ANY[m])
        v.append(np.log(-np.log(S.step_at(ts, sv, tv))))
    gaps[tv] = v[0] - v[1]
for tv in (3, 58):
    a.annotate('', xy=(np.log(tv), -0.02), xytext=(np.log(tv), -gaps[tv] - 0.02),
               arrowprops=dict(arrowstyle='<->', color=ACC, lw=1.0))
a.text(.985, .05, 'parallel curves would mean proportional hazards.\n'
       'The vertical gap is log of the cumulative hazard ratio:\n'
       'it falls from %.2f at 3 months to %.2f at 58.' % (gaps[3], gaps[58]),
       transform=a.transAxes, color=ACC, fontsize=7.4, ha='right', va='bottom')
clean(a, 'Log-minus-log survival plot (illustrative)',
      'log(months)', 'log(−log Ŝ)')
print('P238 %5.0f KB' % (save(f, 'P238') / 1024))

# -------- P239  Schoenfeld residual plot -----------------------------
beta, se = S.cox_binary(d['time'], ANY, d['group'].astype(float))
et, sr = S.schoenfeld(d['time'], ANY, d['group'].astype(float), beta)
grid = np.linspace(et.min(), et.max(), 250)
trend = S.smooth(et, sr, grid, bw=6.0)
sl, ic, r, pv, _ = stats.linregress(et, sr)
f, a = F(5.8, 3.6)
a.plot(et, sr, 'o', ms=2.4, mfc=DATA, mec='none', alpha=.28, ls='none',
       rasterized=True)
a.axhline(beta, color=MUTE, lw=1.1, ls='--')
a.text(HORIZON * .99, beta + .12, r'fitted $\hat\beta$ = %.2f' % beta,
       color=MUTE, fontsize=7.4, ha='right')
a.plot(grid, trend, color=ACC, lw=2.0)
a.text(.985, .62, 'a binary covariate puts every residual in one of two bands —\n'
       'read the fitted curve, not the points. It rises from %.2f to %.2f\n'
       '(trend p = %.3f), so the hazard ratio is not constant.'
       % (trend[0], trend[-1], pv),
       transform=a.transAxes, color=ACC, fontsize=7.4, ha='right', va='top')
a.set_xlim(0, HORIZON)
clean(a, 'Scaled Schoenfeld residuals for the cohort term (illustrative)',
      'Months since transplant', r'Scaled residual (log hazard ratio)')
print('P239 %5.0f KB  (beta %.3f, trend slope p = %.2g)' % (save(f, 'P239') / 1024, beta, pv))

# -------- P240  swimmer plot -----------------------------------------
# stratify the sample so the figure shows all three endings, not just the
# patients who happened to be followed longest
pick = []
for c, k in ((1, 7), (2, 6), (0, 9)):
    idx = np.where(d['cause'] == c)[0]
    pick.extend(idx[np.linspace(0, len(idx) - 1, k).astype(int)])
pick = np.array(pick)
pick = pick[np.argsort(d['time'][pick])]
f, a = F(5.8, 4.2)
for row, i in enumerate(pick):
    a.barh(row, d['time'][i], height=.62, color=DATA, alpha=.32, lw=0)
    rm = min(d['response_month'][i], d['time'][i] * .9)
    a.plot([rm], [row], 'o', ms=4.2, mfc=DATA, mec=SURF, mew=.6, zorder=4)
    if d['cause'][i] == 1:
        a.plot([d['time'][i]], [row], 'X', ms=5.4, mfc=ACC, mec=SURF, mew=.5, zorder=4)
    elif d['cause'][i] == 2:
        a.plot([d['time'][i]], [row], 's', ms=4.4, mfc=AXIS, mec=SURF, mew=.5, zorder=4)
    else:
        a.annotate('', xy=(d['time'][i] + 2.6, row), xytext=(d['time'][i], row),
                   arrowprops=dict(arrowstyle='->', color=DATA, lw=1.1))
a.set_yticks([]); a.set_xlim(0, HORIZON + 5); a.set_ylim(-1, len(pick))
handles = [plt.Line2D([], [], ls='none', marker=mk, ms=ms, mfc=c, mec=SURF, mew=.5, label=l)
           for mk, ms, c, l in (('o', 4.2, DATA, 'response'), ('X', 5.4, ACC, 'relapse'),
                                ('s', 4.4, AXIS, 'death'))]
handles.append(plt.Line2D([], [], color=DATA, lw=1.4, label='→ still in follow-up'))
a.legend(handles=handles, frameon=False, fontsize=7.6, labelcolor=AXIS,
         loc='lower center', bbox_to_anchor=(.5, 1.005), ncol=4,
         columnspacing=1.4, handletextpad=.4)
clean(a, None, 'Months since transplant', None, grid='x')
a.set_title('Swimmer plot — one bar per patient (illustrative)', color=AXIS,
            loc='left', pad=26)
print('P240 %5.0f KB  (%d patients)' % (save(f, 'P240') / 1024, len(pick)))

# -------- P242  waterfall plot (best tumour response) ----------------
sel = np.where(G[1])[0][:74]
ch = np.sort(d['best_change'][sel])[::-1]
f, a = F(5.8, 3.6)
a.bar(np.arange(len(ch)), ch, width=.86, color=DATA, lw=0)
a.axhline(20, color=ACC, lw=1.0, ls='--')
a.axhline(-30, color=ACC, lw=1.0, ls='--')
a.text(len(ch) - .5, 23, 'progressive disease  ≥ +20 %', color=ACC, fontsize=7.2, ha='right')
a.text(-.5, -40, 'partial response  ≤ −30 %', color=ACC, fontsize=7.2, ha='left')
a.axhline(0, color=AXIS, lw=.9)
a.set_xticks([]); a.set_xlim(-1, len(ch))
a.set_ylim(min(-100, ch.min() - 8), max(80, ch.max() + 8))
a.text(.985, .93, 'one bar per patient, sorted — not a time series',
       transform=a.transAxes, color=MUTE, fontsize=7.4, ha='right', va='top')
clean(a, 'Waterfall plot of best tumour response (illustrative)',
      'Patients, ordered by response', 'Best change in target lesion sum (%)')
print('P242 %5.0f KB  (%d patients)' % (save(f, 'P242') / 1024, len(ch)))

# -------- P243  restricted mean survival time ------------------------
TAU = 36.0
f, a = F(5.8, 3.7)
r, curves = {}, {}
grid = np.linspace(0, TAU, 1200)
for g in (0, 1):
    m = G[g]
    ts, s, _, _ = S.kaplan_meier(d['time'][m], ANY[m])
    curves[g] = S.step_at(ts, s, grid)
    r[g] = S.rmst(d['time'][m], ANY[m], TAU)
    stepdraw(a, ts, s, color=COL[g], lw=2.0,
             label='%s — RMST %.1f months' % (LABEL[g], r[g]))
# the area between the two curves up to tau IS the difference in RMST
a.fill_between(grid, curves[0], curves[1], color=DATA, alpha=.16, lw=0)
a.axvline(TAU, color=MUTE, lw=1.0, ls=':')
a.text(TAU - .8, 1.0, 'τ = %d months' % TAU, color=MUTE, fontsize=7.4, ha='right', va='top')
a.legend(frameon=False, fontsize=7.8, labelcolor=AXIS, loc='lower left')
a.text(.985, .90, 'the shaded area between the curves is\nthe difference: %.1f months of event-free\nlife over the first %d months'
       % (r[1] - r[0], TAU), transform=a.transAxes, color=ACC, fontsize=7.6,
       ha='right', va='top')
a.set_ylim(0, 1.02); a.set_xlim(0, HORIZON)
clean(a, 'Restricted mean survival time (illustrative)',
      'Months since transplant', 'Probability event-free')
print('P243 %5.0f KB  (RMST %.1f vs %.1f)' % (save(f, 'P243') / 1024, r[0], r[1]))

# -------- P244  landmark analysis ------------------------------------
LM = 12.0
f, a = F(5.8, 3.7)
for g in (0, 1):
    m = G[g]
    ts, s, _, _ = S.kaplan_meier(d['time'][m], ANY[m])
    stepdraw(a, ts, s, color=COL[g], lw=1.1, alpha=.35)
    alive = m & (d['time'] > LM)
    lt, ls_, _, _ = S.kaplan_meier(d['time'][alive] - LM, ANY[alive])
    stepdraw(a, lt + LM, ls_, color=COL[g], lw=2.1,
             label='%s — %d event-free at the landmark' % (LABEL[g], alive.sum()))
a.axvline(LM, color=ACC, lw=1.2, ls='--')
a.text(LM + 1.2, .30, 'landmark at %d months' % LM, color=ACC, fontsize=7.6)
a.legend(frameon=False, fontsize=7.8, labelcolor=AXIS, loc='lower left')
a.text(.985, .97, 'faint: the whole cohort from time zero\nbold: restarted among those still event-free',
       transform=a.transAxes, color=MUTE, fontsize=7.4, ha='right', va='top')
a.set_ylim(0, 1.02); a.set_xlim(0, HORIZON)
clean(a, 'Landmark analysis (illustrative)',
      'Months since transplant', 'Probability event-free')
print('P244 %5.0f KB' % (save(f, 'P244') / 1024))

# -------- P245  Weibull probability plot -----------------------------
# Two ways to put the same relapse times on Weibull paper. The median-rank
# method uses the 183 observed relapses and silently discards the 375 patients
# who died or were still event-free; the Kaplan-Meier method keeps them. The
# generating model had shape 1.40 and scale 100 months, so we can say which
# one is wrong and by how much.
rel = np.sort(d['time'][d['cause'] == 1])
n = len(rel)
F_med = (np.arange(1, n + 1) - 0.3) / (n + 0.4)
x_naive, y_naive = np.log(rel), np.log(-np.log(1 - F_med))
sl_n, ic_n, r_n, _, _ = stats.linregress(x_naive, y_naive)

kt, ks, _, _ = S.kaplan_meier(d['time'], (d['cause'] == 1).astype(int))
ok = (kt > 0) & (ks < 1) & (ks > 0)
x_km, y_km = np.log(kt[ok]), np.log(-np.log(ks[ok]))
sl_k, ic_k, r_k, _, _ = stats.linregress(x_km, y_km)

f, a = F(5.8, 3.7)
a.plot(x_naive, y_naive, 'o', ms=3.2, mfc=D2, mec=SURF, mew=.3, ls='none',
       label='median ranks, observed relapses only', rasterized=True)
a.plot(x_km, y_km, 'o', ms=3.2, mfc=DATA, mec=SURF, mew=.3, ls='none',
       label='Kaplan-Meier, censored patients kept', rasterized=True)
xs = np.linspace(min(x_naive.min(), x_km.min()), max(x_naive.max(), x_km.max()), 20)
a.plot(xs, sl_n * xs + ic_n, color=D2, lw=1.5)
a.plot(xs, sl_k * xs + ic_k, color=DATA, lw=1.5)
a.legend(frameon=False, fontsize=7.6, labelcolor=AXIS, loc='upper left')
a.text(.985, .06,
       'true model: shape 1.40, scale 100 months\n'
       'events only:  shape %.2f, scale %3.0f months\n'
       'Kaplan-Meier: shape %.2f, scale %3.0f months'
       % (sl_n, np.exp(-ic_n / sl_n), sl_k, np.exp(-ic_k / sl_k)),
       transform=a.transAxes, color=ACC, fontsize=7.4, ha='right', va='bottom')
a.set_ylim(-7.7, 2.6)
clean(a, 'Weibull probability plot of time to relapse (illustrative)',
      'log(months to relapse)', 'log(−log Ŝ)')
print('P245 %5.0f KB  (naive shape %.2f scale %.0f;  KM shape %.2f scale %.0f;  true 1.40 / 100)'
      % (save(f, 'P245') / 1024, sl_n, np.exp(-ic_n / sl_n), sl_k, np.exp(-ic_k / sl_k)))
