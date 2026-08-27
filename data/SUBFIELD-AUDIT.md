# Subfield audit — what the catalogue is missing

Radiation dosimetry was absent entirely, which suggested other subfields would be too. This is a
pass over the 17 areas named in the build brief, checked against `plots.csv` by figure vocabulary
(name + aliases + tools) rather than by subject tag, since a missing cluster has no tag to find it by.

**Nothing here has been added.** Counts are proposals.

---

## The structural evidence

Counting entries per subject tag finds the blind spots without needing to guess at vocabulary.
**14 of the 143 taxonomy tags have zero entries** and 22 more have three or fewer:

| Tag | Area | Entries |
|---|---|---:|
| `anaesthesia-icu` Anaesthesia & critical care | HM | 0 |
| `pharmacology-clin` Clinical pharmacology & pharmacokinetics | HM | 0 |
| `dentistry` Dentistry & oral health | HM | 0 |
| `endocrinology` Endocrinology & metabolism | HM | 0 |
| `nephrology-urology` Nephrology & urology | HM | 0 |
| `rheum-immunology` Rheumatology & clinical immunology | HM | 0 |
| `paediatrics` Paediatrics | HM | 0 |
| `geriatrics` Geriatrics & ageing | HM | 0 |
| `emergency` Emergency medicine | HM | 0 |
| `nutrition` Nutrition & dietetics | HM | 0 |
| `biotechnology` Biotechnology & bioengineering | LS | 0 |
| `forensics` Forensic science | SH | 0 |
| `philosophy` Philosophy & ethics | SH | 0 |
| `science-studies` Science & technology studies | SH | 0 |
| `respiratory` Respiratory medicine | HM | 1 |
| `gastro-hepatology`, `obgyn`, `nursing-midwifery` | HM | 1 each |
| `veterinary` | HM | 2 |
| `surgery` | HM | 2 |
| `civil-engineering`, `metrology`, `chem-inorganic`, `quantum` | PE | 2 each |
| `planetary`, `space-physics` | EE | 2 each |
| `archaeology`, `criminology` | SH | 2 each |

Ten of the fourteen empty tags are clinical. The catalogue's coverage of medicine is concentrated in
oncology, epidemiology, clinical trials and imaging, and thins to nothing across the specialties that
monitor a patient rather than analyse a cohort. That is the same failure mode as the missing
radiotherapy cluster.

---

## Field by field

Numbers in brackets are what is already present, then what is proposed.

### 1. Audiology & hearing — [0 present, ~8 proposed]

Nothing. No hit on audiogram, tympanogram, ABR, otoacoustic emission or speech audiometry.

Pure-tone audiogram (the inverted y-axis is a genuine reading trap) · Tympanogram · Speech
audiometry performance-intensity function · Auditory brainstem response waveform · DPOAE
"DP-gram" · Speech banana overlay · Acoustic reflex threshold chart · Loudness growth function.

### 2. Vision science & ophthalmology — [2 present, ~9 proposed]

Present: `P694` fundus photograph, `P695` OCT retinal scan — both images. Every *measurement*
figure of the field is absent.

Humphrey visual field grayscale and total-deviation plot · Goldmann kinetic perimetry chart ·
Snellen / logMAR acuity chart · Contrast sensitivity function curve · Electroretinogram waveform ·
Corneal topography map · OCT RNFL TSNIT thickness profile · Defocus curve · Amsler grid.

### 3. Sleep medicine — [2 present, ~6 proposed]

Present: `P725` actigraphy trace, `P726` polysomnogram / hypnogram. The circadian and
respiratory-event conventions are missing.

Double-plotted actogram (raster) · Overnight oximetry desaturation trace with AHI · Sleep-stage
transition diagram · Sleep EEG spectrogram / delta power decay · Multiple sleep latency test
summary · Phase response curve.

### 4. Anaesthesia & critical care monitoring — [0 present, ~9 proposed]

Empty tag, empty vocabulary. This is the largest single hole after radiotherapy, and like
radiotherapy it is almost entirely `origin = H`: an instrument emits a waveform and the display
renders it.

Capnogram (EtCO₂ waveform — its *shape* is the diagnosis) · Ventilator pressure–volume loop ·
Ventilator flow–volume loop · Arterial pressure waveform with pulse pressure variation ·
Depth-of-anaesthesia (BIS) trend · Train-of-four display · Context-sensitive half-time curve ·
ICU multi-parameter vitals chart · Thromboelastogram trace · Oxygen–haemoglobin dissociation curve
(shape `S30`, and a textbook characteristic curve that the catalogue has no version of).

### 5. Pharmacometrics and PK/PD — [4 loosely present, ~9 proposed]

Present but incidental: `P273` dose–response curve, `P355` Hill plot, `P268` compartmental model
trajectory, `P208` tornado diagram. None of the figures that constitute a population-PK report exist.

Concentration–time profile (linear and semi-log — the semi-log is what makes the compartments
readable) · Visual predictive check · Goodness-of-fit panel (DV vs PRED / IPRED, CWRES vs time) ·
Covariate effect forest plot · Emax model fit · AUC trapezoidal diagram · Therapeutic window band
plot · Spaghetti plot of individual profiles · Bioequivalence 90% confidence interval plot.

### 6. Veterinary imaging — [2 present, ~4 proposed — and the framing is wrong]

`P698` and `P700` are preclinical small-animal imaging, not clinical veterinary work. But
veterinary radiology genuinely does reuse `P686` radiograph, `P688` MRI and `P689` ultrasound —
there is no distinct figure vocabulary to add. **Recommend not adding a veterinary imaging cluster.**
What *is* distinctive is production animal science, which is a different thing:

Lactation curve · Growth / body condition score chart · Egg production curve · Herd epidemic curve.

### 7. Dentistry — [0 present, ~7 proposed]

Empty. Dental imaging has its own geometry conventions that a general radiograph entry does not cover.

Panoramic radiograph (OPG) · Bitewing and periapical radiograph · Periodontal charting grid ·
Odontogram · Cephalometric tracing and analysis · Dental CBCT slice · DMFT index bar chart.

### 8. Food science and sensory analysis — [0 present, ~9 proposed]

The one hit for "spider" is `P241`, an oncology tumour-response plot. Sensory science has a large
and distinctive figure set, none of it here.

Quantitative descriptive analysis spider profile · External and internal preference map · Penalty
(just-about-right) analysis plot · Texture profile analysis curve (`S30`) · Shelf-life survival
curve · Triangle-test power / d′ chart · Time–intensity curve · Napping / projective mapping plot ·
CIELAB a*b* colour plot.

### 9. Sports biomechanics — [5 loosely present, ~8 proposed]

Present: `P039` radar chart, `P432` Poincaré HRV, `P703` gait stick figure, `P724` EMG trace,
`P725` actigraphy. The waveform conventions that biomechanics actually publishes are absent.

Ground reaction force–time curve · Joint angle waveform over the gait cycle with an SD band ·
Force–velocity / power–velocity profile · Blood lactate threshold curve · VO₂ kinetics and
incremental test plot · Critical power hyperbola · Plantar pressure map · SPM1D statistical
parametric map of a waveform.

### 10. Metallurgy and welding — [4 present, ~9 proposed]

Present: `P475` phase diagram, `P477` Ellingham, `P516` Ashby, `P585` grain size distribution.
The transformation and weld-specific charts are missing, and they are the ones a metallurgist reads
daily.

TTT (isothermal transformation) diagram · CCT (continuous cooling) diagram · Schaeffler / WRC-1992
constitution diagram · Jominy hardenability curve · Hardness traverse across a weld · Charpy
ductile–brittle transition curve · da/dN vs ΔK (Paris law) plot · Weld macrograph (`origin = L`,
synthesisable) · Larson–Miller creep parameter plot.

### 11. Mining and mineral processing — [1 present, ~8 proposed]

`P183` semivariogram is the only real hit (the "recovery curve" match was `P622`, FRAP). Resource
estimation and processing are both absent.

Grade–tonnage curve · Grade–recovery curve · Partition (Tromp) curve · Comminution size-distribution
/ P80 curve · Flotation kinetics curve · Block model cross-section · Nested pit shell plot ·
Reconciliation (F1/F2) chart.

### 12. Textile science — [0 present, ~7 proposed]

Nothing. The only hit was a tractography render.

Fibre diameter distribution histogram · Kawabata KES fabric-hand profile · Fabric drape diagram ·
Uster yarn evenness diagram and imperfection chart · Single-fibre stress–strain curve (`S30`) ·
Moisture regain isotherm · Pilling / colour-fastness grey-scale grading chart.

### 13. Acoustics — [0 present, ~9 proposed]

Every apparent hit was a false positive: `P138`/`P226`/`P242` are three unrelated "waterfall" plots
and `P749` is the econometric impulse response function. Acoustics is a completely absent field.

One-third-octave band spectrum · Sound level time history (L<sub>Aeq</sub>, L<sub>90</sub>) ·
Reverberation time decay curve (Schroeder integration) · Noise contour map (L<sub>den</sub>) ·
Directivity polar plot (`S10`) · Equal-loudness contour chart · Sound transmission class plot ·
NC / RC room criteria curves · Modulation transfer / STI matrix.

### 14. HVAC and building performance — [2 present, ~7 proposed]

Present: `P507` psychrometric chart, `P508` Mollier diagram. `P147` Sankey and `P510` Moody chart are
generic entries that building services reuse rather than building-specific figures.

Energy signature / degree-day regression plot · Load duration curve · PMV–PPD thermal comfort chart ·
Adaptive comfort band chart · Daylight factor false-colour floor plan · Sun path diagram ·
Annual end-use energy stacked bar.

### 15. Transport engineering — [4 present, ~8 proposed]

Present: `P136` Marey chart, `P177` connection map, `P178` OD flow map, `P179` isochrone map — all
spatial. Traffic flow theory has none of its own figures here.

Fundamental diagram of traffic flow (speed–flow–density) · Time–space vehicle trajectory diagram ·
Cumulative arrival–departure queueing diagram · Level-of-service band chart · Travel-time
reliability distribution · Collision diagram · 24-hour traffic count profile · Macroscopic
fundamental diagram.

### 16. Actuarial science — [3 present, ~8 proposed]

Present: `P135` Lexis diagram, `P186` SMR map, `P275` life table survival plot — demography, not
insurance. General insurance reserving is absent entirely.

Loss development (run-off) triangle heat map · Chain-ladder development factor plot · Mortality
improvement heat map (Lee–Carter) · Lapse / persistency curve by duration · Exposure curve · Loss
distribution with VaR and TVaR annotated · Solvency capital waterfall · Claim development lag scatter.

### 17. Psychometrics beyond IRT — [9 present, ~6 proposed — the weakest case]

Present: `P759` item characteristic curve, `P760` test information function, `P761` Wright map,
`P762` DIF plot, plus `P381` scree, `P396` SEM path diagram, `P067` Bland–Altman, `P214` ROC. This
is the one field on the list that is **not** a missing cluster; it is a field with gaps.

Test characteristic curve · Category response curves for polytomous items · CFA standardised
loading diagram · Parallel analysis plot · Infit–outfit person fit map · Norm / percentile
conversion chart.

---

## Summary

| Field | Present | Proposed | Verdict |
|---|---:|---:|---|
| Acoustics | 0 | 9 | whole field absent |
| Anaesthesia & critical care | 0 | 9 | whole field absent |
| Audiology & hearing | 0 | 8 | whole field absent |
| Dentistry | 0 | 7 | whole field absent |
| Food science & sensory | 0 | 9 | whole field absent |
| Textile science | 0 | 7 | whole field absent |
| Mining & mineral processing | 1 | 8 | whole field absent |
| Vision science & ophthalmology | 2 | 9 | imaging only, no measurement figures |
| Metallurgy & welding | 4 | 9 | reference charts only, no process charts |
| Pharmacometrics / PK-PD | 4 | 9 | incidental hits, no report vocabulary |
| Transport engineering | 4 | 8 | spatial only, no flow theory |
| Actuarial science | 3 | 8 | demography only, no reserving |
| Sports biomechanics | 5 | 8 | traces only, no waveform conventions |
| HVAC & building performance | 2 | 7 | reference charts only |
| Sleep medicine | 2 | 6 | partial |
| Psychometrics beyond IRT | 9 | 6 | gaps, not a cluster |
| Veterinary imaging | 2 | 4 | **do not add as imaging** — reuses radiology; add animal science instead |
| **Total** | | **~131** | |

Adding all of it, together with the 11 radiotherapy entries, would take the catalogue from 812 to
roughly 954.

Two observations that should shape the decision rather than the list itself:

**The gap has a direction.** Fields disappear when the figure is a *monitoring waveform* or an
*instrument display* rather than an analysis of a data table. Anaesthesia, audiology, acoustics and
radiotherapy are all mostly `origin = H`. The catalogue's `H` class holds 114 of 812 entries and is
dominated by imaging and spectroscopy. This is the class that a general-purpose glossary cannot
reach, and it is where this catalogue's remaining distinctiveness lies.

**Engineering practice is under-represented relative to engineering research.** Metallurgy has its
thermodynamic reference charts but not its heat-treatment charts; HVAC has its psychrometrics but not
its energy signatures; transport has its maps but not its fundamental diagram. Everything present is
what appears in a paper; everything missing is what appears in an engineering report or on a shop floor.

*(Written 2026-08-27, against `plots.csv` at 812 rows.)*
