# Data model — the structural layer

The catalogue is no longer a flat list. Three new fields turn it into something a site can reason with.

## 1. `data_shape` — the spine

Every entry is keyed to the **structure of its input table**, not to its appearance. Siblings then fall out automatically: two plots are alternatives if they consume the same shape. This is authored once per shape instead of once per pair, and it powers the entry point the Observable glossary cannot have — *"I have this kind of data, what can I plot?"*

31 shapes cover all 823 entries.

| Shape | Meaning | Entries |
|---|---|---:|
| `S01` | One continuous variable | 45 |
| `S02` | One continuous variable, split by group | 12 |
| `S03` | Two continuous variables | 57 |
| `S04` | Paired or repeated measurements on the same units | 5 |
| `S05` | One summary value per category | 29 |
| `S06` | Parts of a whole | 11 |
| `S07` | Set membership and overlap | 3 |
| `S08` | Time series | 70 |
| `S09` | Compositional (parts constrained to sum to a whole) | 14 |
| `S10` | Directional or circular | 17 |
| `S11` | Many variables per observation (wide / high-dimensional) | 40 |
| `S12` | Pairwise matrix | 16 |
| `S13` | Nodes and edges | 25 |
| `S14` | Hierarchy | 15 |
| `S15` | Flows between states | 10 |
| `S16` | Values attached to geography | 63 |
| `S17` | Time-to-event with censoring | 11 |
| `S18` | Effect estimates with uncertainty | 26 |
| `S19` | Spectrum (intensity vs ordered index) | 40 |
| `S20` | Instrument trace (signal vs time) | 28 |
| `S21` | Image or raster grid | 18 |
| `S22` | Model output vs observed | 63 |
| `S23` | Values along genomic coordinate | 23 |
| `S24` | Posterior or simulation draws | 13 |
| `S25` | Surface over a two-dimensional domain | 13 |
| `S26` | Physical lab output (no input table) | 65 |
| `S27` | Schematic (no data) | 26 |
| `S28` | Text corpus | 12 |
| `S29` | Three-dimensional structure or spatial coordinates | 17 |
| `S30` | Characteristic curve (measured response vs a controlled variable) | 24 |
| `S31` | Reference chart or state-space diagram | 12 |

Four of these are deliberately *not* data shapes — `S26` physical lab output, `S27` schematic, `S28` text corpus, `S29` three-dimensional structure. Entries there have no input table, so their siblings group by **what the figure is evidence of** rather than by table structure. That is the honest way to handle a western blot: its alternatives are ELISA and targeted mass spectrometry, not other scatter plots.

### A correction worth recording

The first pass grouped lollipop charts, Cleveland dot plots, dumbbell plots and slope graphs with box and violin plots — all "a value and a category". That is wrong and it would have poisoned the comparison feature. A box plot shows a **distribution** within each group; a Cleveland dot plot shows **one summary number** per category. They answer different questions and are not substitutes. They now sit in `S05` and `S04`.

The physical sciences also needed two shapes that no general-purpose glossary has:

- **`S30` characteristic curve** — a measured response against a variable *you* controlled: stress-strain, I-V, cyclic voltammogram, rheogram, BET isotherm. The x-axis is an experimental setting, not an observation.
- **`S31` reference chart** — a state-space diagram you read against, rather than plot your data into: Moody chart, psychrometric chart, Pourbaix diagram, Ashby chart, phase diagram. These are *maps of possibility*, and calling them "scatter plots" would be a category error.

---

## 2. `universality` — solving the tag-pollution problem

If a histogram carries all six area tags, every subject filter returns histograms and the filter stops being useful. So breadth is a tier, not a tag set.

| Tier | Entries | Tagging rule |
|---|---:|---|
| `universal` | 68 | **No subject tags at all.** Surfaced as a "Foundations" entry point instead. |
| `cross-domain` | 28 | 3+ areas, ranked. |
| `domain-signature` | 470 | 1–2 areas. The plot that says "this is an X paper" — volcano, Kaplan-Meier, ternary. |
| `niche` | 257 | One subfield, unambiguous — concordia diagram, Dalitz plot, Krona chart. |

Ranking is only a genuine judgement call for the 28 cross-domain entries. Everything else is either untagged or obvious, which matches how you wanted this handled.

---

## 3. `depth_tier` — the writing budget

| Tier | Entries | Gets |
|---|---:|---|
| `deep` | 168 | Definition · how to read it · **what it hides vs its siblings** · ranked subjects · packages with runnable code · generated image |
| `standard` | 431 | Definition · how to read it · subjects · packages · image |
| `stub` | 224 | Definition · tags · one tool pointer |

All 823 are findable and correctly tagged from day one. Depth follows demand, and any stub can be promoted later without restructuring.

---

## Sibling groups (the tight ones)

These are the shapes where "which one should I use" is a real and frequently-asked question. The loose shapes — 70 time-series entries, 63 geographic — are correct but too broad to read as a menu; there, siblings are ranked by universality so the general options surface first.

**`S02` — One continuous variable, split by group**

  Box-and-whisker plot · Violin plot · Raincloud plot · Strip plot · Wilkinson dot plot · Beeswarm plot · Notched box plot · Bean plot · Sina plot · Letter-value plot · Stacked violin plot · QC violin panel

**`S04` — Paired or repeated measurements on the same units**

  Span chart · Dumbbell plot · Slope graph · Connected scatter plot · Tanglegram

**`S07` — Set membership and overlap**

  Venn diagram · UpSet plot · Euler diagram

**`S09` — Compositional (parts constrained to sum to a whole)**

  Ternary plot · Compositional log-ratio biplot · Ternary contour / heatmap plot · Quaternary plot · Soil texture triangle · AFM diagram · Piper diagram · Gibbs diagram (water chemistry) · De Finetti diagram (genotype frequencies) · QAPF diagram · TAS diagram · Stiff diagram · Schoeller diagram · Durov diagram

**`S17` — Time-to-event with censoring**

  Kaplan-Meier curve · Number-at-risk table · Cumulative incidence function plot · Nelson-Aalen cumulative hazard plot · Swimmer plot · Weibull probability plot · Log-minus-log survival plot · Schoenfeld residual plot · Waterfall plot (best tumour response) · Restricted mean survival time plot · Landmark analysis plot

**`S06` — Parts of a whole**

  Stacked bar chart · 100% stacked bar chart · Pie chart · Donut chart · Marimekko chart · Waffle chart · Likert plot · Taxonomic relative abundance bar plot · Nested pie chart · Proportional area chart · Cell type proportion stacked bar

**`S30` — Characteristic curve (measured response vs a controlled variable)**

  Electrochemical impedance Nyquist plot · Galvanostatic charge-discharge curve · Stress-strain curve · S-N curve · Nanoindentation load-displacement curve · DMA curve · Rheogram · BET adsorption isotherm · Langmuir / Freundlich isotherm fit · Breakthrough curve · Pump / fan performance curve · Magnetic hysteresis loop · I-V curve (semiconductor) · J-V curve (solar cell) · EQE / IPCE spectrum · Tafel plot · Cyclic voltammogram · Differential capacity plot · Creep curve · Beam profile map · Percentage depth dose curve · Radiation beam profile · Bragg peak curve · Spread-out Bragg peak

**`S31` — Reference chart or state-space diagram**

  Smith chart · Phase diagram (thermodynamic) · Pourbaix diagram · Ellingham diagram · Psychrometric chart · Mollier diagram · Moody chart · Ashby chart · Koppen climate classification map · T-s and P-v diagrams · Chart of nuclides · Hjulstrom / Shields diagram

---

## Schema

```
id              P001–P823
name            canonical name
aliases         other field-specific names for the same figure
family          F01–F34, functional grouping (navigation)
data_shape      S01–S31, structure of the input table (siblings)
origin_code     D data-driven | H hybrid instrument | L lab-only | C conceptual
universality    universal | cross-domain | domain-signature | niche
depth_tier      deep | standard | stub
areas           ranked area codes (empty for universal)
subject_tags    ranked nested tags (empty for universal)
tools           packages / technique
sibling_count   derived: other entries sharing data_shape
```

A new family, `F34 Radiotherapy & dosimetry`, was added with the eleven radiation dosimetry
entries. Scattering them between `F22 Physics, chem & materials` and `F28 Clinical & preclinical
imaging` would have split one clinical subfield across two families for no gain. This is the only
structural change made when the dosimetry entries went in; reversing it is one column in the CSV.

`family` and `data_shape` are deliberately different axes. Family answers *"what kind of thing is this"* for browsing; shape answers *"what could I use instead"* for deciding. A volcano plot is family F14 Genomics but shape S03 two-continuous — which is exactly why it sits next to a scatter plot in the comparison view and next to a Manhattan plot in the navigation.