# Progress

Written entries and generated figures, by data shape. Work goes one shape at a time so that the
sibling comparisons stay coherent — "what it hides" is written once against a shared set of
alternatives.

Regenerate the counts with:

```bash
python3 src/progress.py
```

<!-- BEGIN TABLE -->
| Shape | What it is | Entries | Written | Figures |
|---|---|---:|---:|---:|
| `S01` | One continuous variable | 43 | 0 | 4 |
| `S02` | One continuous variable, split by group | 12 | 12 | 12 |
| `S03` | Two continuous variables | 57 | 0 | 3 |
| `S04` | Paired or repeated measurements on the same units | 5 | 0 | 0 |
| `S05` | One summary value per category | 29 | 0 | 2 |
| `S06` | Parts of a whole | 11 | 0 | 2 |
| `S07` | Set membership and overlap | 3 | 0 | 1 |
| `S08` | Time series | 69 | 0 | 3 |
| `S09` | Compositional (parts constrained to sum to a whole) | 14 | 0 | 1 |
| `S10` | Directional or circular | 17 | 0 | 2 |
| `S11` | Many variables per observation (wide / high-dimensional) | 40 | 0 | 3 |
| `S12` | Pairwise matrix | 16 | 0 | 2 |
| `S13` | Nodes and edges | 25 | 0 | 0 |
| `S14` | Hierarchy | 15 | 0 | 0 |
| `S15` | Flows between states | 10 | 0 | 0 |
| `S16` | Values attached to geography | 63 | 0 | 0 |
| `S17` | Time-to-event with censoring | 11 | 0 | 1 |
| `S18` | Effect estimates with uncertainty | 26 | 0 | 1 |
| `S19` | Spectrum (intensity vs ordered index) | 40 | 0 | 1 |
| `S20` | Instrument trace (signal vs time) | 28 | 0 | 0 |
| `S21` | Image or raster grid | 18 | 0 | 0 |
| `S22` | Model output vs observed | 61 | 0 | 1 |
| `S23` | Values along genomic coordinate | 23 | 0 | 1 |
| `S24` | Posterior or simulation draws | 13 | 0 | 0 |
| `S25` | Surface over a two-dimensional domain | 11 | 0 | 1 |
| `S26` | Physical lab output (no input table) | 65 | 0 | 3 |
| `S27` | Schematic (no data) | 26 | 0 | 0 |
| `S28` | Text corpus | 12 | 0 | 0 |
| `S29` | Three-dimensional structure or spatial coordinates | 17 | 0 | 0 |
| `S30` | Characteristic curve (measured response vs a controlled variable) | 20 | 0 | 1 |
| `S31` | Reference chart or state-space diagram | 12 | 0 | 0 |
| | **Total** | **812** | **12** | **45** |
<!-- END TABLE -->

## Batch log

| Date | Batch | Result |
|---|---|---|
| 2026-08-27 | SEO migration | Replaced the single-file SPA with 895 pre-rendered pages. 812 entry pages at `/plot/<slug>/`, listing pages for every shape, subject area, origin class and family, `sitemap.xml`, `robots.txt`, `DefinedTerm` JSON-LD, 159 KB search index. Heaviest entry page 246 KB. Verified in a headless browser, light and dark, zero console errors. |

## Rules of a batch

A batch is: content for one data shape → figures for that shape → `python3 src/figs.py` →
`python3 src/build.py` → look at every new figure on screen → check page weight → commit.

- Never mark an entry written that has placeholder text. A stub that says it is a stub is fine;
  a stub pretending to be finished is not.
- Bullets average 8 words, nothing over ~15.
- `hides` is the mechanism, `avoid` is the situation where that loss bites. If a bullet appears in
  both, one of them is wrong.
- Verify every package name against the CRAN index list and the Bioconductor `VIEWS` file. CRAN
  serves removal notices with HTTP 200, so a status check is a false positive.

## Known defects carried forward

- **34 archived packages** are cited in `data/plots.csv` and flagged there. Replace them as each
  entry is reached.
- **Meta descriptions on the 800 unwritten entries** are composed from the entry's own
  classification (aliases, data shape, origin, sibling count, primary tool) rather than from a
  definition sentence, because no definition exists yet. Each one that gets written replaces its
  own description automatically.
- **`universality = universal` entries still carry area and tag values in `plots.csv`**, which
  contradicts the stated rule that universal plots are untagged. 68 entries are affected. Not
  changed — it touches the classification axes.
- **No `og:image`.** Social previews fall back to text. A baked-colour PNG set would fix it and is
  the same work as figure thumbnails.
