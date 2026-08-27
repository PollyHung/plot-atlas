"""Check src/survlib.py against lifelines.

lifelines is a test-time dependency only — building the site does not need it.

    pip install lifelines
    python3 src/test_survlib.py
"""
import os, sys
import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import survlib
from survdata import cohort

rng = np.random.default_rng(5)
d = cohort()
fails = []


def check(name, got, want, tol=1e-6):
    ok = abs(got - want) < tol
    print('%-42s %12.6f  vs %12.6f   %s' % (name, got, want, 'ok' if ok else 'FAIL'))
    if not ok:
        fails.append(name)


try:
    from lifelines import KaplanMeierFitter, NelsonAalenFitter, CoxPHFitter
    from lifelines.statistics import logrank_test
    from lifelines.utils import restricted_mean_survival_time
except ImportError:
    sys.exit('lifelines not installed; skipping (pip install lifelines)')

for g in (0, 1):
    m = d['group'] == g
    t, e = d['time'][m], (d['cause'][m] > 0).astype(int)

    kmf = KaplanMeierFitter().fit(t, e)
    ts, s, _, _ = survlib.kaplan_meier(t, e)
    for x in (12, 24, 36, 60):
        check('KM group %d at %d months' % (g, x),
              survlib.step_at(ts, s, x), float(kmf.predict(x)), 1e-9)

    naf = NelsonAalenFitter().fit(t, e)
    ht, H, _ = survlib.nelson_aalen(t, e)
    for x in (24, 60):
        check('Nelson-Aalen group %d at %d' % (g, x),
              survlib.step_at(ht, H, x), float(naf.predict(x)), 1e-9)

    check('RMST group %d to 36 months' % g, survlib.rmst(t, e, 36),
          float(restricted_mean_survival_time(kmf, t=36)), 1e-6)

t, e, g = d['time'], (d['cause'] > 0).astype(int), d['group']
lr = logrank_test(t[g == 0], t[g == 1], e[g == 0], e[g == 1])
chi2, p = survlib.logrank(t, e, g)
check('log-rank chi2', chi2, float(lr.test_statistic), 1e-6)
check('log-rank p', p, float(lr.p_value), 1e-9)

import pandas as pd
df = pd.DataFrame({'T': t, 'E': e, 'x': g.astype(float)})
cph = CoxPHFitter().fit(df, 'T', 'E')
beta, se = survlib.cox_binary(t, e, g.astype(float))
check('Cox beta', beta, float(cph.params_['x']), 1e-6)
check('Cox se', se, float(cph.standard_errors_['x']), 1e-5)

# competing-risks CIF has no lifelines equivalent here; check its invariants
ct, cif1 = survlib.aalen_johansen(t, d['cause'], 1)
ct2, cif2 = survlib.aalen_johansen(t, d['cause'], 2)
kt, ks, _, _ = survlib.kaplan_meier(t, e)
tot = survlib.step_at(ct, cif1, 1e9) + survlib.step_at(ct2, cif2, 1e9)
check('CIF1 + CIF2 == 1 - KM(any event)', tot, 1 - survlib.step_at(kt, ks, 1e9), 1e-9)
check('CIF1 <= 1 - KM(cause 1 alone)', 1.0,
      1.0 if survlib.step_at(ct, cif1, 60) <=
      1 - survlib.step_at(*survlib.kaplan_meier(t, (d['cause'] == 1).astype(int))[:2], 60) + 1e-12
      else 0.0)

print()
print('FAILED: %s' % fails if fails else 'all checks passed')
sys.exit(1 if fails else 0)
