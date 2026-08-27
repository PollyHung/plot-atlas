# Plot Atlas

A reference catalogue of **823 plot types** used across the sciences, indexed by the *shape of the
data that produces them* rather than by what they look like — so that for any figure you can see
what you could have drawn instead, and what each option hides.

The site is **pre-rendered static HTML**: one real page per entry, no framework, no server, no
build tooling beyond Python and matplotlib.

---

## Deploy to GitHub Pages

1. Create a repository and push this folder.

   ```bash
   git remote add origin git@github.com:PollyHung/plot-atlas.git
   git push -u origin main
   ```

2. In the repo: **Settings → Pages → Build and deployment → Source: GitHub Actions.**
   The included workflow publishes on every push to `main`.

3. Live at `https://pollyhung.github.io/plot-atlas/`.

`site.json` holds the canonical base URL. It is used for `<link rel="canonical">`, Open Graph
`og:url`, the JSON-LD `@id`s and `sitemap.xml`. **Change it before deploying anywhere else, then
re-run the build** — every internal link is relative, so only these absolute URLs depend on it.

### Custom domain

Add a file named `CNAME` at the repo root containing one line:

```
atlas.love-death-and-maladies.org
```

Then at your DNS provider add a `CNAME` record pointing that subdomain at `pollyhung.github.io`.
For an apex domain use four `A` records instead: `185.199.108.153`, `185.199.109.153`,
`185.199.110.153`, `185.199.111.153`. Tick **Enforce HTTPS** in Settings → Pages once the
certificate is issued. Set `base_url` in `site.json` to the new domain and rebuild.

---

## How it is put together

```
site.json           canonical base URL and site name
data/
  plots.csv         the catalogue: 823 rows, the source of truth
  taxonomy.txt      6 subject areas, 145 nested tags
  *.md              catalogue, taxonomy, data model, gap analysis and subfield audit
src/
  build.py          the static site generator — writes every page
  content.py        written entries
  figs.py           generates every figure from synthetic data
  figs_rt.py        the radiotherapy and dosimetry figures
  figbase.py        shared palette, axis styling and sentinel-colour save
  atlas.css         stylesheet, copied to assets/ at build time
  site.js           client layer, copied to assets/ at build time
  fig/*.svg         generated figures
PROGRESS.md         what is written and illustrated, shape by shape
```

Everything else at the repository root is **generated** and should not be hand-edited:

```
index.html  about/  browse/  shapes/  subjects/  origins/  families/  sitemap-page/
plot/<slug>/        823 entry pages
plot/<ID>/          823 redirect stubs, kept so old links survive
shape/<Sxx>/  area/<XX>/  origin/<X>/  family/<slug>/
assets/             atlas.css, site.js, search-index.json
sitemap.xml  robots.txt  404.html
```

### Rebuild

```bash
pip install numpy scipy matplotlib
python3 src/figs.py     # regenerate figures into src/fig/ (only when figures change)
python3 src/figs_rt.py  # the radiotherapy set
python3 src/build.py    # regenerate the whole site
```

`build.py` deletes and rewrites the generated directories on every run, so a removed entry never
leaves a stale page behind.

### Local preview

```bash
python3 -m http.server 8712
```

---

## What the migration to static pages bought

The site used to be one 3.7 MB `index.html` with hash routing. A search engine saw a single
document; for a reference site whose value is being found by someone googling *"what is a ternary
plot"*, that was fatal.

| | Before | After |
|---|---|---|
| Indexable documents | 1 | 907 |
| Bytes to read one entry | 3.7 MB | 6.4 KB median, 246 KB heaviest |
| Search index loaded | whole bundle | 161 KB (30 KB gzipped) |
| Per-page `<title>` / description | no | yes |
| Structured data | none | `DefinedTerm` in a `DefinedTermSet`, plus `BreadcrumbList` |

Old `#/plot/P400` links redirect client-side to `/plot/ternary-plot/`, and `/plot/P400/` is kept as
a `noindex` stub whose canonical points at the slug URL.

### The figure-theming constraint

Figures are written with **CSS custom properties instead of literal colours**
(`fill="var(--series-1)"`), so one SVG set re-themes with light and dark mode rather than needing
two copies. **Those variables do not resolve through `<img src>`** — only when the SVG is inlined
in the document. So each entry page inlines its own figure, and listing pages carry none. Thumbnails,
if they are ever wanted, need separate baked-colour PNGs.

---

## The data model

Four independent axes, all present in `plots.csv`:

| Field | What it answers |
|---|---|
| `family` | *What kind of thing is this?* — 34 functional families, used for browsing |
| `data_shape` | *What could I use instead?* — 31 shapes; plots sharing one are substitutes |
| `origin_code` | *How is the figure physically made?* — `D` data-driven · `H` hybrid instrument · `L` lab-only · `C` conceptual |
| `universality` | *How broadly is it used?* — universal · cross-domain · domain-signature · niche |

`data_shape` is the spine. Siblings are derived from it rather than authored pair by pair, which is
what makes the comparison feature maintainable at 823 entries.

## Current state

See `PROGRESS.md` for the shape-by-shape table. In summary:

| | |
|---|---|
| Catalogued, classified and given their own page | **823 / 823** |
| Written up in full | **23** (shape S02, plus the radiotherapy family) |
| Figures generated | **56** |
| Deep tier planned | 168 · standard 431 · stub 224 |

Package references were checked against the live CRAN and Bioconductor indexes. **34 cited packages
are archived** and need substitutes — they are flagged in `data/plots.csv`.

Subject rankings are considered estimates, not measured publication frequencies.

## Licence

Figures are generated from synthetic data, never copied, so nothing here carries a third-party
image licence.
