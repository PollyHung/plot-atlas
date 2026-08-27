"""The one dataset behind every shape-S17 figure.

A registry of 800 patients followed after transplant, split into two cohorts by
age. The relapse hazard is **identical in both cohorts by construction** — same
Weibull shape and scale. Only the hazard of dying without relapsing differs,
and it differs a lot: older patients die of other causes far sooner.

That is what makes the cumulative-incidence entry's demonstration work. A
Kaplan-Meier estimate of relapse, which treats those deaths as censoring, is
estimating exp(-cumulative cause-specific hazard) and so must come out the same
in both cohorts. The proportion of patients who actually relapse cannot, because
in the older cohort most of them are dead first.

Nothing here is a measurement. The shapes are clinically ordinary; the numbers
are drawn from a fixed seed.
"""
import numpy as np

N = 400                     # per cohort
HORIZON = 60.0              # months of planned follow-up
WEIBULL_SHAPE = 1.4
WEIBULL_SCALE = 100.0       # months
NRM_HAZARD = {0: 0.025, 1: 0.002}   # death without relapse, per month
LABEL = {0: 'Age 60 and over', 1: 'Under 60'}
SEED = 11

_CACHE = {}


def cohort():
    """group (0/1), time (months), cause (0 censored, 1 relapse, 2 death)."""
    if _CACHE:
        return _CACHE
    rng = np.random.default_rng(SEED)
    g, t, c = [], [], []
    for grp in (0, 1):
        t_relapse = WEIBULL_SCALE * rng.weibull(WEIBULL_SHAPE, N)
        t_death = rng.exponential(1 / NRM_HAZARD[grp], N)
        t_cens = np.minimum(rng.exponential(190.0, N), HORIZON)
        obs = np.minimum(np.minimum(t_relapse, t_death), t_cens)
        cause = np.where((t_relapse <= t_death) & (t_relapse <= t_cens), 1,
                         np.where(t_death <= t_cens, 2, 0))
        g.append(np.full(N, grp)); t.append(obs); c.append(cause)
    d = dict(group=np.concatenate(g), time=np.concatenate(t),
             cause=np.concatenate(c).astype(int))

    # Per-patient response data for the swimmer and waterfall entries, drawn
    # for the same people so those figures describe the same cohort.
    rng2 = np.random.default_rng(SEED + 1)
    n = len(d['time'])
    # best percentage change in the sum of target lesion diameters
    base = rng2.normal(-18, 34, n)
    base[d['cause'] == 1] += 26          # relapsers respond less well
    d['best_change'] = np.clip(base, -100, 120)
    d['response_month'] = np.clip(rng2.gamma(2.0, 1.6, n), 0.6, None)
    _CACHE.update(d)
    return _CACHE


if __name__ == '__main__':
    import survlib
    d = cohort()
    print('n = %d, %d per cohort' % (len(d['time']), N))
    for g in (0, 1):
        m = d['group'] == g
        print('  cohort %d (%-15s) relapse %3d   death %3d   censored %3d'
              % (g, LABEL[g], (d['cause'][m] == 1).sum(),
                 (d['cause'][m] == 2).sum(), (d['cause'][m] == 0).sum()))
    print()
    for g in (0, 1):
        m = d['group'] == g
        kt, ks, _, _ = survlib.kaplan_meier(d['time'][m], (d['cause'][m] == 1).astype(int))
        ct, cif = survlib.aalen_johansen(d['time'][m], d['cause'][m], 1)
        print('  cohort %d   1 - KM(relapse) at 60 mo = %.3f    Aalen-Johansen CIF = %.3f'
              % (g, 1 - survlib.step_at(kt, ks, HORIZON), survlib.step_at(ct, cif, HORIZON)))
