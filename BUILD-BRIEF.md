# Build brief — Plot Atlas v2

Paste this into Claude Code from the root of the `plot-atlas` repo.

---

## What this repo is

A reference catalogue of scientific plot types, indexed by the **shape of the data that produces
them** rather than by appearance, so that for any figure a reader can see what they could have drawn
instead and what each option hides.

```
index.html          the entire site today — data, figures and code inlined (3.7 MB)
data/plots.csv      the catalogue: 812 rows, the source of truth
data/taxonomy.txt   6 subject areas, 143 nested tags
data/*.md           catalogue, taxonomy, data model, gap analysis
src/figs.py         figure generators (matplotlib → SVG)
src/content.py      written entries — currently 12, all of data shape S02
src/shell.html      page shell + stylesheet
src/app.js          router and views
src/build_site.py   assembles the data bundle
src/fig/*.svg       45 generated figures
```

Read `data/DATA-MODEL.md` first. It explains the four classification axes and why they exist.

**State today:** all 812 entries catalogued and classified; 12 written up; 45 figures.

---

## Three jobs, in this order

### 1. Fix SEO — this blocks everything else

The site is currently a single-file SPA with hash routing. Search engines see one page, not 812.
For a reference site whose whole value is being found by someone googling *"what is a ternary
plot"*, that is fatal. Fix it before there is more content to re-migrate.

**Required:**

- Static pre-render one real HTML page per entry at `/plot/<slug>/index.html`, where `<slug>` is a
  kebab-case name (`/plot/ternary-plot/`, `/plot/kaplan-meier-curve/`). Keep `/plot/P400/` as a
  301-style redirect stub so existing links survive.
- Static index pages for every shape, subject area, family and origin class.
- Per page: unique `<title>`, `<meta name="description">` written from the entry's own definition
  (not templated boilerplate), `<link rel="canonical">`, and Open Graph tags.
- `sitemap.xml` listing every page; `robots.txt` pointing at it.
- JSON-LD on each entry page. `DefinedTerm` within a `DefinedTermSet` is the right schema for a
  glossary; include `name`, `description`, `inDefinedTermSet`, and `termCode` (the plot ID).
- Keep search working client-side, but load a **small search index** (id, name, aliases, shape,
  origin — a few hundred KB) rather than the whole bundle.

**One trap to know about.** The figures use CSS custom properties instead of literal colours
(`fill="var(--series-1)"`) so a single SVG set re-themes with light and dark mode. **Those variables
do not resolve if the SVG is loaded via `<img src>`** — only when inlined in the document. So:
inline the entry's own figure on its page (one figure, ~100 KB, fine), and do not put figures on
listing pages. If you need thumbnails later, generate separate baked-colour PNGs for that purpose.

Target: each entry page under 300 KB. Verify a sample with a real headless browser, not by
reasoning about it.

Publishing stays GitHub Pages — no server, no framework, no build tooling beyond Python. The
existing Actions workflow should keep working.

### 2. Write the remaining entries

620 entries are `deep` or `standard` tier and unwritten; 224 are `stub` tier and only need a
definition. Work **one data shape at a time** — that is what makes the sibling comparisons coherent,
because you write "what it hides" once against a shared set of alternatives.

Follow `src/content.py` exactly. Every written entry has:

```python
defn   # one prose sentence — what it is, mechanically
read   # 3–4 bullets — how to read the marks
hides  # 2–3 bullets — what information is lost (the MECHANISM)
use    # 1–2 bullets — when to reach for it
avoid  # 1–2 bullets — when not to (the SITUATION)
r      # one runnable R line
py     # one runnable Python line
caps   # for deep entries: the capability matrix row
```

**Writing rules, learned from review:**

- Bullets average **8 words**. Nothing longer than ~15.
- `hides` and `avoid` must not restate each other. `hides` is the mechanism, `avoid` is the
  situation where that loss bites. If a bullet appears in both, one is wrong.
- No hedging, no "it is important to note", no restating the plot's name back at the reader.
- Every claim must be true of the plot as actually implemented, not as idealised.

**The strongest pattern in the site is proof, not assertion.** The S02 shape page does not claim
that box plots hide modality — it shows two groups whose box plots are pixel-identical (five-number
summaries within 0.7 ng/mL, t-test p = 0.98) where one is cleanly bimodal, built by fitting a beta
distribution's shape parameters to match the bimodal group's quartiles. Look for that opportunity in
every shape and take it when it exists. One engineered demonstration beats ten paragraphs.

### 3. Generate the remaining figures

767 entries have no figure. Conventions in `src/figs.py`, all non-negotiable:

- **One dataset per data shape.** Every plot within a shape draws the *same numbers* — that is what
  makes the comparison mean anything.
- Write with sentinel colours, then string-replace to `var(--series-1)`, `var(--accent)`,
  `var(--ink)`, `var(--surface-1)`, `var(--muted)`. Never literal hex in shipped SVG.
- **Rasterize dense mark layers** (`rasterized=True`, `dpi=140`). This took the Manhattan plot from
  956 KB to under 100 KB with vector axes intact. Any figure over ~250 KB needs this.
- Colour is only for identity. Where the axis already labels the groups, use one hue. If you do need
  a categorical palette, validate it — the `dataviz` skill ships a runnable validator, and slot 4 of
  the default palette puts yellow beside orange, which fails the all-pairs colour-blindness floor.
- **Lab-only figures are synthesisable.** Western blots and agarose gels in this repo are numpy
  Gaussian blobs + `gaussian_filter` + noise, rendered `cmap='gray_r'`. They look real, cost
  nothing, and carry no licence risk. Make them biologically coherent — the existing blot has a
  p-ERK time course that decays against a flat GAPDH loading control. Label them as illustrative.
- Render every figure and **look at it** before shipping. Two bugs in the current set were invisible
  in code and obvious on screen: a beeswarm that came out as vertical stripes, and a control
  distribution with a spurious waist that undercut the page's entire argument.

---

## New material to add: radiotherapy and medical physics

The catalogue has **zero** entries for radiation dosimetry — checked against `plots.csv` for depth
dose, isodose, dose-volume, DVH, Bragg, TCP and NTCP. All absent. This is a whole clinical subfield
with its own distinctive figure vocabulary, and it was found by accident in a GAMSAT physics paper.

Add these entries. Continue IDs from P813. Add two new subject tags under area `HM` in
`data/taxonomy.txt`: `medical-physics` and `radiation-oncology`.

| Name | Aliases | Shape | Origin | Notes for the writer |
|---|---|---|---|---|
| Percentage depth dose curve | PDD curve; depth dose curve | S30 | H | Dose on the central axis as a % of maximum, against depth. Higher electron energy pushes the useful range deeper but raises exit dose. The *shape* — build-up region, d<sub>max</sub>, sharp fall-off — is the whole clinical point. Hides everything off the central axis. |
| Isodose curve | isodose distribution; isodose plot | S25 | H | Contours of equal % dose over depth × distance from the central axis. Shows field flatness, penumbra width and how the high-dose region conforms to the target. The companion to PDD: PDD is one line through this surface. |
| Dose–volume histogram | DVH; cumulative DVH | S01 | D | Fraction of an organ's volume receiving at least a given dose — an inverse ECDF. Collapses all spatial information: two very different dose distributions can share a DVH. That is exactly the "identical summary, different truth" pattern this site exists to show — build the demonstration. |
| Differential dose–volume histogram | differential DVH | S01 | D | The density form of the above. |
| Beam profile | lateral dose profile; cross-plane profile | S30 | H | Dose against off-axis distance at fixed depth. Flatness, symmetry, penumbra. |
| Bragg peak curve | proton depth dose | S30 | H | Depth dose for protons and heavier ions — the sharp distal peak that motivates particle therapy. Contrast directly with the electron PDD entry. |
| Spread-out Bragg peak | SOBP | S30 | D | Weighted superposition of Bragg peaks producing a uniform dose plateau across the target. |
| Gamma index map | gamma analysis map | S25 | D | 2-D pass/fail comparison of planned against delivered dose, combining a dose-difference and distance-to-agreement criterion. Standard QA output. |
| Tumour control probability curve | TCP curve | S22 | D | Sigmoid probability of control against delivered dose. |
| Normal tissue complication probability curve | NTCP curve | S22 | D | The paired sigmoid for toxicity. TCP and NTCP are almost always shown together — the therapeutic window is the gap between them, so draw them on one axis. |
| Linac output constancy chart | machine QA chart | S08 | D | A control chart applied to daily linac output. Cross-reference the existing control chart entry. |

Two figures are worth building carefully because they carry the family: a **PDD curve** with several
electron energies on one axis (7, 9, 15, 18, 25 MeV — build-up, d<sub>max</sub> shifting deeper,
bremsstrahlung tail), and an **isodose contour plot** for a single energy showing the 90% to 10%
lines with visible penumbra.

---

## Also do: an audit for other missing subfields

Medical physics was missing entirely, which means other subfields probably are too. Before writing
content, spend one pass looking for whole clusters that are absent rather than individual plots.
Check at least: audiology and vision science, sleep medicine, anaesthesia monitoring, pharmacometrics
and PK/PD, veterinary imaging, dentistry, food science and sensory analysis, sports biomechanics,
metallurgy and welding, mining and mineral processing, textile science, acoustics, HVAC and building
performance, transport engineering, actuarial science, and psychometrics beyond IRT.

Report what you find before adding it, with a count. Do not silently expand the catalogue.

---

## Working method

This is far more than one session of work. Do it in batches and keep the repo deployable at all
times.

1. Do the SEO migration first, in one batch, and verify it.
2. Then work shape by shape. A batch is: content for one shape + figures for that shape + rebuild +
   visual check + commit.
3. Maintain `PROGRESS.md` at the repo root: a table of shapes with entries written, figures made,
   and date. Update it every batch. This is how the work survives across sessions.
4. Never mark an entry written that has placeholder text. A stub that says it is a stub is fine;
   a stub pretending to be finished is not.

## Verification, every batch

- Rebuild and open the site in a headless browser. Zero console errors.
- Screenshot at least one entry page in **both light and dark themes**. The figures must re-theme.
  A colour defined only inside a media query is the classic failure and renders one theme's text on
  the other theme's background.
- Check page weight on the heaviest new page.
- **Verify every package name you cite.** CRAN serves removal notices with **HTTP 200**, so a status
  check is a false positive. Check against the index list at
  `cran.r-project.org/web/packages/available_packages_by_name.html` plus the Bioconductor `VIEWS`
  file. 34 packages already cited in `plots.csv` are archived and flagged — replace them as you
  reach their entries.

## Things not to change without asking

- The four classification axes and the data-shape spine. Siblings derive from shape; do not author
  them pairwise.
- Universal-tier plots carry **no subject tags**. Tagging histograms under all six areas makes every
  subject filter useless.
- The typography and palette: Spectral for display, IBM Plex Sans for body, IBM Plex Mono for data
  and code; cool instrument neutrals, blue series, red reserved for "what it hides".
- The honesty of the About page. It states what is finished and what is not. Keep it accurate as the
  numbers change.
