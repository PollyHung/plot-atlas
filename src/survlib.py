"""Survival estimators, written out in numpy so the figure scripts need nothing
beyond numpy, scipy and matplotlib.

Each one is checked against lifelines in `src/test_survlib.py`; lifelines is a
test-time dependency only and is not needed to build the site.
"""
import numpy as np
from scipy import stats


def _tied(t):
    """Yield (time, slice) for each distinct time, in ascending order."""
    i = 0
    while i < len(t):
        j = i
        while j < len(t) and t[j] == t[i]:
            j += 1
        yield t[i], i, j
        i = j


def kaplan_meier(time, event):
    """Product-limit estimate with a Greenwood standard error.

    Returns (t, S, lower, upper) as step functions starting at (0, 1)."""
    o = np.argsort(time, kind='mergesort')
    t, e = np.asarray(time)[o], np.asarray(event)[o].astype(int)
    n = len(t)
    ts, surv, var = [0.0], [1.0], [0.0]
    cur, cum = 1.0, 0.0
    for tv, i, j in _tied(t):
        d = int(e[i:j].sum())
        if d:
            cur *= 1 - d / n
            cum += d / (n * (n - d)) if n > d else 0.0
            ts.append(tv); surv.append(cur); var.append(cum)
        n -= (j - i)
    ts, surv, var = np.array(ts), np.array(surv), np.array(var)
    se = surv * np.sqrt(var)
    return ts, surv, np.clip(surv - 1.96 * se, 0, 1), np.clip(surv + 1.96 * se, 0, 1)


def nelson_aalen(time, event):
    """Cumulative hazard, with its standard error."""
    o = np.argsort(time, kind='mergesort')
    t, e = np.asarray(time)[o], np.asarray(event)[o].astype(int)
    n = len(t)
    ts, H, var = [0.0], [0.0], [0.0]
    h, v = 0.0, 0.0
    for tv, i, j in _tied(t):
        d = int(e[i:j].sum())
        if d:
            h += d / n
            v += d / n ** 2
            ts.append(tv); H.append(h); var.append(v)
        n -= (j - i)
    return np.array(ts), np.array(H), np.sqrt(np.array(var))


def aalen_johansen(time, cause, k=1):
    """Cumulative incidence of cause k in the presence of the competing causes.

    Unlike 1 - Kaplan-Meier this weights each cause-k event by the probability
    of still being event-free, so it cannot exceed the observed proportion."""
    o = np.argsort(time, kind='mergesort')
    t, c = np.asarray(time)[o], np.asarray(cause)[o].astype(int)
    n = len(t)
    surv, cif = 1.0, 0.0
    ts, vals = [0.0], [0.0]
    for tv, i, j in _tied(t):
        dk = int((c[i:j] == k).sum())
        dall = int((c[i:j] > 0).sum())
        if dall:
            cif += surv * dk / n
            surv *= 1 - dall / n
            ts.append(tv); vals.append(cif)
        n -= (j - i)
    return np.array(ts), np.array(vals)


def step_at(ts, ys, x):
    """Value of a right-continuous step function at x."""
    return ys[np.searchsorted(ts, x, side='right') - 1]


def logrank(time, event, group):
    """Two-sample log-rank test. Returns (chi2, p)."""
    time = np.asarray(time); event = np.asarray(event).astype(int)
    group = np.asarray(group).astype(int)
    o = np.argsort(time, kind='mergesort')
    t, e, g = time[o], event[o], group[o]
    n1, n = int((g == 1).sum()), len(t)
    O1 = E1 = V = 0.0
    for tv, i, j in _tied(t):
        d = int(e[i:j].sum())
        if d and n > 1:
            d1 = int(e[i:j][g[i:j] == 1].sum())
            E1 += d * n1 / n
            V += d * (n1 / n) * (1 - n1 / n) * (n - d) / (n - 1)
            O1 += d1
        n1 -= int((g[i:j] == 1).sum()); n -= (j - i)
    chi2 = (O1 - E1) ** 2 / V if V > 0 else 0.0
    return chi2, float(stats.chi2.sf(chi2, 1))


def cox_binary(time, event, x):
    """Cox model with a single covariate, Breslow ties. Returns (beta, se)."""
    time = np.asarray(time); event = np.asarray(event).astype(int); x = np.asarray(x, float)
    o = np.argsort(time, kind='mergesort')
    t, e, x = time[o], event[o], x[o]

    def score_info(b):
        w = np.exp(b * x)
        U = I = 0.0
        n = len(t)
        for tv, i, j in _tied(t):
            d = int(e[i:j].sum())
            if d:
                ww = w[i:]
                s0 = ww.sum(); s1 = (ww * x[i:]).sum(); s2 = (ww * x[i:] ** 2).sum()
                U += x[i:j][e[i:j] == 1].sum() - d * s1 / s0
                I += d * (s2 / s0 - (s1 / s0) ** 2)
        return U, I

    b = 0.0
    for _ in range(40):
        U, I = score_info(b)
        if I <= 0:
            break
        step = U / I
        b += step
        if abs(step) < 1e-9:
            break
    _, I = score_info(b)
    return b, (1 / np.sqrt(I) if I > 0 else np.nan)


def schoenfeld(time, event, x, beta):
    """Scaled Schoenfeld residuals (Grambsch-Therneau).

    A trend in these against time is evidence that the hazard ratio is not
    constant, which is the assumption a Cox model rests on."""
    time = np.asarray(time); event = np.asarray(event).astype(int); x = np.asarray(x, float)
    o = np.argsort(time, kind='mergesort')
    t, e, x = time[o], event[o], x[o]
    w = np.exp(beta * x)
    ets, raw, vs = [], [], []
    for tv, i, j in _tied(t):
        if not e[i:j].sum():
            continue
        ww = w[i:]
        s0 = ww.sum(); s1 = (ww * x[i:]).sum(); s2 = (ww * x[i:] ** 2).sum()
        xbar = s1 / s0
        v = s2 / s0 - xbar ** 2
        for xi in x[i:j][e[i:j] == 1]:
            ets.append(tv); raw.append(xi - xbar); vs.append(v)
    ets, raw, vs = np.array(ets), np.array(raw), np.array(vs)
    d = len(ets)
    scaled = beta + raw * d / vs.sum()
    return ets, scaled


def rmst(time, event, horizon):
    """Restricted mean survival time: the area under the Kaplan-Meier curve up
    to `horizon`. The units are the units of time, which is the point of it."""
    ts, s, _, _ = kaplan_meier(time, event)
    keep = ts <= horizon
    tt = np.append(ts[keep], horizon)
    ss = np.append(s[keep], s[keep][-1])
    return float(np.sum(np.diff(tt) * ss[:-1]))


def smooth(x, y, grid, bw):
    """Gaussian kernel smoother — used for the Schoenfeld trend line."""
    out = np.empty_like(grid)
    for i, g in enumerate(grid):
        w = np.exp(-0.5 * ((x - g) / bw) ** 2)
        out[i] = np.sum(w * y) / np.sum(w)
    return out
