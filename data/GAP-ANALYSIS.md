# Gap analysis — what the Observable glossary is missing

I pulled the notebook's full source from the Observable API. It defines **102 terms**, but ~38 of those are not plot types at all — `mean`, `median`, `ETL`, `cardinality`, `normalize`, `sample`, `scale`, `projection`, `clustering`, `data mining`, `NULL`, `pivot`. **The real plot count is about 64.**

This catalogue has **812**.

## What the 64 are, and what they are not

The Observable list is essentially the *Data Viz Catalogue* canon: the D3 / business-dashboard / infographic vocabulary. It is complete for that world and covers finance well (candlestick, OHLC, Kagi, point-and-figure). Against research publishing it has a shape problem — it contains **almost no plot that a scientist actually publishes**.

Absent from all 102 terms:

- **Clinical & epidemiology:** ROC curve, Kaplan-Meier curve, forest plot, funnel plot, Bland-Altman plot, epidemic curve, nomogram, decision curve analysis, PRISMA/CONSORT diagram, calibration plot
- **Genomics & omics:** volcano plot, Manhattan plot, MA plot, oncoprint, UMAP/t-SNE, GSEA enrichment plot, circos plot, sequence logo, sashimi plot, LocusZoom
- **Geoscience — the gap you spotted:** ternary plot, stereonet, rose diagram, Piper diagram, concordia diagram, Harker diagram, TAS diagram, stratigraphic column, Hovmoller diagram, Taylor diagram, skew-T log-P
- **Physics, chemistry, materials:** band structure, phase diagram, Pourbaix diagram, Arrhenius plot, cyclic voltammogram, XRD pattern, stress-strain curve, Nyquist plot, Bode plot, Ashby chart
- **Astronomy:** Hertzsprung-Russell diagram, light curve, colour-magnitude diagram, corner plot, all-sky projection
- **Statistics proper:** Q-Q plot, ECDF, ridgeline plot, raincloud plot, UpSet plot, coefficient plot, partial dependence plot, posterior/trace plot
- **The entire lab-only category:** western blots, gels, micrographs, flow cytometry, patch-clamp traces, fMRI maps, IVIS imaging — 0 of 102

## Structural additions beyond volume

1. **Origin classification.** Every entry is D / H / L / C. The Observable list has no concept of a figure that cannot be produced from a data table. Your western-blot and mouse-imaging requirement lands here, and the H (hybrid) class is the one most glossaries get wrong — a mass spectrum or an XRD pattern is neither hand-made nor plottable from a spreadsheet; an instrument emits a raw signal and software renders it.
2. **Subject ranking, not just subject listing.** Each plot carries ordered area + tag lists, so a page can say *"ternary plots: petrology first, soil science second, ecology third"* rather than an unordered tag soup.
3. **Alias coverage.** Same figure, different name by field: MA plot = Bland-Altman = Tukey mean-difference; rose diagram = wind rose = circular histogram; PCoA = MDS = classical scaling. These are the searches that fail on every existing glossary.
4. **Discriminating comparison.** Your requirement (4.1) — what a plot *cannot* show relative to alternatives from the same data — needs a "sibling" relation between entries. That is a data-model decision to make before building: e.g. box plot ↔ violin ↔ raincloud ↔ beeswarm all consume one grouped continuous variable and hide different things.

## Counts by family

| Family | Entries |
|---|---:|
| F01 Distributions | 28 |
| F02 Categorical comparison | 30 |
| F03 Correlation & bivariate | 21 |
| F04 Regression & diagnostics | 16 |
| F05 Part-to-whole & sets | 12 |
| F06 Time series & temporal | 32 |
| F07 Networks & hierarchies | 29 |
| F08 Maps & spatial | 28 |
| F09 Uncertainty & Bayesian | 17 |
| F10 ML & classifier evaluation | 20 |
| F11 Survival & time-to-event | 13 |
| F12 Meta-analysis & evidence | 20 |
| F13 Epidemiology & public health | 12 |
| F14 Genomics & transcriptomics | 38 |
| F15 Single-cell & spatial omics | 18 |
| F16 Structural & molecular | 23 |
| F17 Ecology & biodiversity | 21 |
| F18 Ordination & dim reduction | 21 |
| F19 Compositional & simplex | 18 |
| F20 Directional & circular | 17 |
| F21 Spectra & signals | 40 |
| F22 Physics, chem & materials | 49 |
| F23 Astronomy & space | 18 |
| F24 Earth, climate & hydrology | 54 |
| F26 Gels, blots & electrophoresis | 17 |
| F25 Lab imaging & microscopy | 41 |
| F27 Flow cytometry & plate assays | 32 |
| F28 Clinical & preclinical imaging | 19 |
| F29 Electrophysiology & neuroimaging | 22 |
| F30 Text, qualitative & humanities | 19 |
| F31 Social science & econometrics | 29 |
| F32 Business, finance & ops | 18 |
| F33 Conceptual & schematic | 20 |

| **Total** | **812** |

## Counts by origin class

| Class | Entries |
|---|---:|
| D — data-driven | 612 |
| H — hybrid instrument/software | 114 |
| L — lab-only physical output | 59 |
| C — conceptual/schematic | 27 |