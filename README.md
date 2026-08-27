# Plot Atlas

A reference catalogue of **812 plot types** used across the sciences, indexed by the *shape of the
data that produces them* rather than by what they look like — so that for any figure you can see
what you could have drawn instead, and what each option hides.

The whole site is a **single `index.html`**. No build step, no dependencies, no framework.

---

## Deploy to GitHub Pages

1. Create a repository and push this folder.

   ```bash
   git init && git add . && git commit -m "Plot Atlas"
   git branch -M main
   git remote add origin git@github.com:<you>/plot-atlas.git
   git push -u origin main
   ```

2. In the repo: **Settings → Pages → Build and deployment → Source: GitHub Actions.**
   The included workflow publishes on every push to `main`.

   *(Or skip Actions entirely: set Source to "Deploy from a branch", pick `main` / root.
   A single `index.html` needs nothing else.)*

3. Live at `https://<you>.github.io/plot-atlas/`.

### Custom domain

Add a file named `CNAME` at the repo root containing one line:

```
atlas.love-death-and-maladies.org
```

Then at your DNS provider add a `CNAME` record pointing that subdomain at `<you>.github.io`.
For an apex domain (`love-death-and-maladies.org` with no subdomain) use four `A` records instead:
`185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`.
Tick **Enforce HTTPS** in Settings → Pages once the certificate is issued.

---

## How it is put together

```
index.html          the entire site — data, figures and code inlined
data/
  plots.csv         the catalogue: 812 rows, the source of truth
  taxonomy.txt      6 subject areas, 143 nested tags
  *.md              catalogue, taxonomy, data model and gap analysis as documents
src/
  figs.py           generates every figure from synthetic data
  content.py        written entries (currently the 12 of shape S02)
  shell.html        page shell + stylesheet
  app.js            router and views
  build_site.py     prepares the data bundle
  fig/*.svg         generated figures
```

### Rebuild

```bash
pip install numpy scipy matplotlib
cd src
python figs.py          # regenerate figures
python build_site.py    # rebuild the data bundle
# then re-inline: see the assembly step at the bottom of build_site.py
```

Figures are written with **CSS custom properties instead of literal colours**
(`fill="var(--series-1)"`), so they re-theme with the page rather than needing a light and a dark
copy. The palette is validated for colour-vision deficiency in both themes.

---

## The data model

Four independent axes, all present in `plots.csv`:

| Field | What it answers |
|---|---|
| `family` | *What kind of thing is this?* — 33 functional families, used for browsing |
| `data_shape` | *What could I use instead?* — 31 shapes; plots sharing one are substitutes |
| `origin_code` | *How is the figure physically made?* — `D` data-driven · `H` hybrid instrument · `L` lab-only · `C` conceptual |
| `universality` | *How broadly is it used?* — universal · cross-domain · domain-signature · niche |

`data_shape` is the spine. Siblings are derived from it rather than authored pair by pair, which is
what makes the comparison feature maintainable at 812 entries.

Universal plots (histogram, scatter, box) carry **no subject tags at all** — tagging them under every
area would make every subject filter useless. They surface through the Foundations route instead.

## Current state

| | |
|---|---|
| Catalogued and classified | **812 / 812** |
| Written up in full | **12** (shape S02) |
| Figures generated | **45** |
| Deep tier planned | 168 · standard 420 · stub 224 |

Package references were checked against the live CRAN and Bioconductor indexes. **34 cited packages
are archived** and need substitutes — they are flagged in `data/plots.csv`.

Subject rankings are considered estimates, not measured publication frequencies.

## Licence

Figures are generated from synthetic data, never copied, so nothing here carries a third-party
image licence.
