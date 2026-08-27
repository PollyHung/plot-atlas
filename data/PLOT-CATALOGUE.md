# Data-Visualisation Atlas — Master Plot Catalogue

**812 plot types** · 33 families · 31 data shapes · 6 subject areas · 143 nested tags

Origin: **D** data-driven · **H** hybrid (instrument signal, software-rendered) · **L** lab-only (physical output) · **C** conceptual
Tier: **U** universal · **X** cross-domain · **S** domain-signature · **N** niche  ·  Depth: **●** deep · **◐** standard · **○** stub

## F01 Distributions  *(28)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P001 | **Histogram** | frequency histogram | S01 | D | U● | XM LS HM PE EE SH | ggplot2::geom_histogram; matplotlib.hist; seaborn.histplot; base::hist |
| P002 | **Density plot** | kernel density estimate; KDE plot | S01 | D | U● | XM LS HM SH | ggplot2::geom_density; seaborn.kdeplot; scipy.stats.gaussian_kde |
| P003 | **Frequency polygon** |  | S01 | D | S◐ | XM SH | ggplot2::geom_freqpoly |
| P004 | **Box-and-whisker plot** | box plot; Tukey box plot | S02 | D | U● | LS HM XM PE SH | ggplot2::geom_boxplot; seaborn.boxplot; base::boxplot |
| P005 | **Notched box plot** |  | S02 | D | S◐ | XM HM | ggplot2::geom_boxplot(notch=TRUE) |
| P006 | **Letter-value plot** | boxen plot | S02 | D | N○ | XM | seaborn.boxenplot; lvplot |
| P007 | **Violin plot** |  | S02 | D | U● | LS HM XM | ggplot2::geom_violin; seaborn.violinplot; scanpy.pl.violin |
| P008 | **Bean plot** |  | S02 | D | S◐ | XM LS | R::beanplot |
| P009 | **Sina plot** |  | S02 | D | S◐ | LS XM | ggforce::geom_sina |
| P010 | **Raincloud plot** |  | S02 | D | U● | LS HM SH | ggrain; PupillometryR; raincloudplots; ptitprince (py) |
| P011 | **Strip plot** | jitter plot | S02 | D | U● | LS HM XM | ggplot2::geom_jitter; seaborn.stripplot |
| P012 | **Wilkinson dot plot** |  | S02 | D | U● | XM SH | ggplot2::geom_dotplot |
| P013 | **Beeswarm plot** |  | S02 | D | U● | LS HM | ggbeeswarm; seaborn.swarmplot |
| P014 | **Ridgeline plot** | joy plot | S26 | D | U● | XM EE SH LS | ggridges; joypy |
| P015 | **Empirical CDF plot** | ECDF plot | S01 | D | U● | XM HM | ggplot2::stat_ecdf; seaborn.ecdfplot |
| P016 | **Q-Q plot** | quantile-quantile plot | S01 | D | U● | XM LS HM | base::qqnorm; statsmodels.qqplot; ggpubr::ggqqplot |
| P017 | **P-P plot** | probability-probability plot | S01 | D | N○ | XM | statsmodels.ProbPlot |
| P018 | **Normal probability plot** |  | S01 | D | S◐ | XM PE | base::qqnorm; scipy.stats.probplot |
| P019 | **Stem-and-leaf plot** |  | S01 | D | U● | XM SH | base::stem |
| P020 | **Rug plot** |  | S01 | D | U● | XM | ggplot2::geom_rug |
| P021 | **Marginal histogram plot** | scatter with marginals | S03 | D | U● | XM LS | ggExtra::ggMarginal; seaborn.jointplot |
| P022 | **Pareto chart** |  | S01 | D | S◐ | SH PE | qcc; ggQC; matplotlib |
| P023 | **Hanging rootogram** |  | S01 | D | N○ | XM | vcd::rootogram; countreg |
| P024 | **Bagplot** | bivariate boxplot | S03 | D | N○ | XM | aplpack::bagplot |
| P025 | **Spike histogram** |  | S01 | D | S◐ | XM HM | ggplot2; Hmisc |
| P026 | **Quantile dotplot** |  | S24 | D | S◐ | XM SH | ggdist::stat_dots |
| P027 | **Histogram with fitted distribution overlay** |  | S01 | D | S◐ | XM PE | fitdistrplus; ggplot2 |
| P028 | **Cumulative frequency curve** | ogive | S01 | D | S◐ | XM SH | ggplot2::stat_ecdf |

## F02 Categorical comparison  *(30)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P029 | **Bar chart** | column chart | S05 | D | U● | HM LS PE EE SH XM | ggplot2::geom_col; matplotlib.bar; seaborn.barplot |
| P030 | **Grouped bar chart** | multi-set bar chart; clustered bar | S05 | D | U● | HM LS SH | ggplot2::geom_col(position=dodge) |
| P031 | **Stacked bar chart** |  | S06 | D | U● | LS SH EE | ggplot2::geom_col(position=stack) |
| P032 | **100% stacked bar chart** | proportional stacked bar | S06 | D | U● | LS SH | ggplot2::geom_col(position=fill) |
| P033 | **Diverging bar chart** |  | S05 | D | S◐ | SH EE | ggplot2 |
| P034 | **Lollipop chart** |  | S05 | D | U● | SH LS | ggplot2::geom_segment+geom_point |
| P035 | **Cleveland dot plot** |  | S05 | D | U● | XM HM SH | ggplot2; lattice::dotplot |
| P036 | **Dumbbell plot** | DNA chart; connected dot plot | S04 | D | S◐ | SH HM | ggalt::geom_dumbbell |
| P037 | **Slope graph** | slope chart; bumps chart | S04 | D | S◐ | SH HM | CGPfunctions::newggslopegraph |
| P038 | **Bullet graph** |  | S05 | D | N○ | SH | plotly; R::bulletgraph |
| P039 | **Radar chart** | spider chart; star plot; web chart | S11 | D | X◐ | SH HM PE | fmsb; ggradar; plotly scatterpolar |
| P040 | **Nightingale rose chart** | polar area diagram; coxcomb | S05 | D | S◐ | HM SH | ggplot2::coord_polar |
| P041 | **Radial bar chart** | circular bar chart | S05 | D | N○ | SH | ggplot2::coord_polar |
| P042 | **Waterfall chart** |  | S05 | D | S◐ | SH | waterfalls; plotly |
| P043 | **Marimekko chart** | mekko chart; variable-width bar | S06 | D | S◐ | SH | ggmosaic |
| P044 | **Mosaic plot** |  | S05 | D | U● | XM SH HM | vcd::mosaic; ggmosaic |
| P045 | **Spine plot** | spinogram | S05 | D | N○ | XM | graphics::spineplot; vcd |
| P046 | **Heatmap (categorical matrix)** |  | S12 | D | U● | LS HM XM SH | pheatmap; ComplexHeatmap; seaborn.heatmap |
| P047 | **Bump chart** | rank-over-time chart | S08 | D | S◐ | SH | ggbump |
| P048 | **Small multiples** | trellis plot; facet grid; lattice plot | S05 | D | U● | ALL | ggplot2::facet_wrap; lattice; seaborn.FacetGrid |
| P049 | **Tally chart** |  | S05 | D | N○ | SH | manual |
| P050 | **Pictogram chart** | isotype chart | S05 | D | S◐ | SH HM | waffle; pywaffle |
| P051 | **Waffle chart** | square pie chart | S06 | D | S◐ | SH HM | waffle; pywaffle |
| P052 | **Span chart** | range bar chart | S04 | D | U● | SH EE | ggplot2::geom_linerange |
| P053 | **Population pyramid** | age-sex pyramid | S05 | D | S◐ | SH HM | apyramid; pyramid; plotly |
| P054 | **Likert plot** | diverging stacked bar | S06 | D | S◐ | SH HM | likert; HH::plot.likert; ggstats |
| P055 | **Equiplot** | equity gap plot | S05 | D | S◐ | HM SH | equiplot (Stata); ggplot2 |
| P056 | **Wrapped bar chart** |  | S05 | D | N○ | SH | ggplot2 |
| P057 | **Piled bar chart** |  | S05 | D | N○ | SH | ggplot2 |
| P058 | **Gauge chart** | speedometer chart; dial | S05 | D | S◐ | SH HM | plotly indicator; flexdashboard |

## F03 Correlation & bivariate  *(21)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P059 | **Scatter plot** | XY plot | S03 | D | U● | ALL | ggplot2::geom_point; matplotlib.scatter |
| P060 | **Bubble chart** | proportional-symbol scatter | S03 | D | U● | SH EE HM | ggplot2::geom_point(aes(size=)); plotly |
| P061 | **Connected scatter plot** |  | S04 | D | S◐ | SH EE | ggplot2::geom_path+geom_point |
| P062 | **Scatter plot matrix** | SPLOM; pairs plot | S11 | D | U● | XM LS | GGally::ggpairs; seaborn.pairplot; base::pairs |
| P063 | **Hexbin plot** | hexagonal binning | S25 | D | U● | XM LS EE | hexbin; ggplot2::geom_hex; matplotlib.hexbin |
| P064 | **2-D density plot** | bivariate KDE; contour density | S25 | D | U● | XM LS | ggplot2::geom_density_2d; seaborn.kdeplot |
| P065 | **Binned scatter plot** | binscatter | S03 | D | N○ | SH | binsreg; binscatter (Stata) |
| P066 | **Correlogram** | correlation matrix plot; corrplot | S12 | D | U● | XM LS SH | corrplot; ggcorrplot; corrr; seaborn.heatmap |
| P067 | **Bland-Altman plot** | difference plot; Tukey mean-difference plot; MA plot | S22 | D | S● | HM LS | blandr; BlandAltmanLeh; pyCompare |
| P068 | **Deming/Passing-Bablok regression plot** | method comparison plot | S22 | D | N○ | HM | mcr; deming |
| P069 | **Contour plot** |  | S25 | D | U● | PE EE XM | ggplot2::geom_contour; matplotlib.contour |
| P070 | **3-D surface plot** |  | S25 | D | U● | PE XM EE | plotly; rgl; matplotlib plot_surface |
| P071 | **Wireframe plot** | mesh plot | S25 | D | S◐ | PE XM | lattice::wireframe; matplotlib plot_wireframe |
| P072 | **Vector field plot** | quiver plot | S25 | D | S◐ | PE EE | matplotlib.quiver; ggquiver; metR |
| P073 | **Streamline plot** | streamplot | S25 | D | S◐ | PE EE | matplotlib.streamplot; metR |
| P074 | **Parallel coordinates plot** |  | S11 | D | U● | XM LS PE | GGally::ggparcoord; plotly; pandas parallel_coordinates |
| P075 | **Andrews curves** |  | S11 | D | N○ | XM | pandas.plotting.andrews_curves; andrews |
| P076 | **Chernoff faces** |  | S11 | D | S◐ | XM SH | aplpack::faces |
| P077 | **Star glyph plot** | glyph plot | S11 | D | N○ | XM | graphics::stars |
| P078 | **Table lens** | tableplot | S11 | D | N○ | XM | tabplot |
| P079 | **Heat scatter / density scatter** |  | S03 | D | S◐ | LS XM | LSD::heatscatter; matplotlib |

## F04 Regression & diagnostics  *(16)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P080 | **Regression line with confidence band** | fitted line plot | S22 | D | U● | ALL | ggplot2::geom_smooth |
| P081 | **LOESS / LOWESS smoother** |  | S22 | D | U● | XM SH EE | ggplot2::geom_smooth(method=loess); statsmodels.lowess |
| P082 | **Residual vs fitted plot** |  | S22 | D | S◐ | XM SH | base::plot.lm; ggfortify::autoplot; performance |
| P083 | **Scale-location plot** | spread-location plot | S22 | D | N○ | XM | base::plot.lm |
| P084 | **Cook's distance plot** |  | S22 | D | N○ | XM | base::plot.lm; car |
| P085 | **Leverage / influence plot** |  | S22 | D | N○ | XM | car::influencePlot |
| P086 | **Added-variable plot** | partial regression plot | S22 | D | S◐ | XM SH | car::avPlots |
| P087 | **Component+residual plot** | partial residual plot | S22 | D | N○ | XM | car::crPlots |
| P088 | **Marginal effects plot** | predicted values plot | S22 | D | S◐ | SH HM | marginaleffects; ggeffects; effects |
| P089 | **Interaction plot** | moderation plot; simple slopes plot | S22 | D | S◐ | SH HM | interactions; emmeans; sjPlot |
| P090 | **Coefficient plot** | dot-and-whisker plot | S18 | D | U● | SH HM | dotwhisker; coefplot; sjPlot::plot_model |
| P091 | **Nomogram** |  | S22 | D | S◐ | HM | rms::nomogram; regplot; DynNom |
| P092 | **Spline / GAM partial effect plot** |  | S22 | D | X◐ | XM HM EE | mgcv::plot.gam; gratia |
| P093 | **Regularisation path plot** | lasso trace plot | S24 | D | N○ | XM | glmnet::plot.glmnet |
| P094 | **Cross-validation error curve** |  | S22 | D | N○ | XM | glmnet::cv.glmnet; caret |
| P095 | **Caterpillar plot** | random effects plot | S18 | D | X◐ | XM SH HM | lattice::dotplot(ranef); sjPlot |

## F05 Part-to-whole & sets  *(12)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P096 | **Pie chart** |  | S06 | D | U● | SH HM | ggplot2::coord_polar; matplotlib.pie |
| P097 | **Donut chart** | doughnut chart; ring chart | S06 | D | U● | SH | plotly; ggplot2 |
| P098 | **Nested pie chart** | multi-level pie | S06 | D | N○ | SH | plotly |
| P099 | **Sunburst diagram** | radial treemap | S14 | D | S◐ | SH LS | plotly; sunburstR; d3 |
| P100 | **Treemap** |  | S14 | D | U● | SH EE LS | treemapify; squarify; plotly |
| P101 | **Voronoi treemap** |  | S16 | D | N○ | SH | voronoiTreemap; d3-voronoi-treemap |
| P102 | **Circle packing** | nested circles | S14 | D | S◐ | SH XM | packcircles; circlepackeR |
| P103 | **Icicle plot** | partition plot | S14 | D | S◐ | XM SH | plotly icicle; ggraph |
| P104 | **Proportional area chart** |  | S06 | D | N○ | SH | ggplot2 |
| P105 | **Venn diagram** |  | S07 | D | U● | LS HM XM | ggVennDiagram; VennDiagram; matplotlib-venn |
| P106 | **Euler diagram** | area-proportional Venn | S07 | D | S◐ | LS XM | eulerr; venneuler |
| P107 | **UpSet plot** | set intersection matrix plot | S07 | D | U● | LS HM XM | UpSetR; ComplexUpset; UpSetPlot (py) |

## F06 Time series & temporal  *(32)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P108 | **Line chart** | line graph | S08 | D | U● | ALL | ggplot2::geom_line; matplotlib.plot |
| P109 | **Multi-series line chart** |  | S08 | D | U● | ALL | ggplot2; plotly |
| P110 | **Area chart** |  | S08 | D | U● | SH EE | ggplot2::geom_area |
| P111 | **Stacked area chart** |  | S08 | D | U● | SH EE | ggplot2::geom_area(position=stack) |
| P112 | **Stream graph** | ThemeRiver | S08 | D | S◐ | SH LS | streamgraph; ggstream; d3 |
| P113 | **Step chart** | staircase plot | S08 | D | U● | XM SH | ggplot2::geom_step |
| P114 | **Sparkline** |  | S08 | D | S◐ | SH HM | sparkline; kableExtra |
| P115 | **Horizon chart** |  | S08 | D | S◐ | EE SH | latticeExtra::horizonplot; ggHoriPlot |
| P116 | **Calendar heatmap** |  | S12 | D | U● | SH HM EE | calendR; calmap; ggcal |
| P117 | **Cycle plot** | seasonal subseries plot | S08 | D | S◐ | SH EE | forecast::ggsubseriesplot; feasts |
| P118 | **Seasonal decomposition plot** | STL plot | S08 | D | S◐ | SH EE | stats::stl; statsmodels seasonal_decompose |
| P119 | **Autocorrelation plot** | ACF/PACF correlogram | S12 | D | U● | XM SH EE | stats::acf; statsmodels plot_acf; forecast::ggAcf |
| P120 | **Lag plot** |  | S08 | D | N○ | XM | stats::lag.plot; pandas lag_plot |
| P121 | **Control chart** | Shewhart chart; XmR; CUSUM; EWMA | S08 | D | X◐ | PE HM SH | qcc; SPC; qicharts2 |
| P122 | **Run chart** |  | S08 | D | S◐ | HM PE | qicharts2 |
| P123 | **Gantt chart** |  | S08 | D | U● | SH | ganttrify; plotly.timeline; DiagrammeR::mermaid |
| P124 | **Timeline** |  | S08 | D | U● | SH | vistime; timevis |
| P125 | **Spiral plot** | spiral heatmap | S12 | D | S◐ | EE HM | spiralize; d3 |
| P126 | **Jump plot** |  | S08 | D | N○ | SH | d3 |
| P127 | **Candlestick chart** | Japanese candlestick | S08 | D | N○ | SH | quantmod; mplfinance; plotly |
| P128 | **OHLC bar chart** | open-high-low-close chart | S08 | D | N○ | SH | quantmod; mplfinance |
| P129 | **Kagi chart** |  | S08 | D | N○ | SH | plotly |
| P130 | **Renko chart** |  | S08 | D | N○ | SH | mplfinance |
| P131 | **Point-and-figure chart** |  | S08 | D | N○ | SH | TTR::pointFigure |
| P132 | **Moving average overlay chart** |  | S08 | D | S◐ | SH EE | TTR; zoo::rollmean |
| P133 | **Recurrence plot** |  | S08 | D | X● | XM PE HM | nonlinearTseries; pyunicorn |
| P134 | **Hovmoller diagram** | time-latitude/longitude section | S25 | D | S● | EE | metR; xarray; NCL |
| P135 | **Lexis diagram** |  | S08 | D | S◐ | SH HM | LexisPlotR; Epi::Lexis |
| P136 | **Marey chart** | train schedule chart | S08 | D | S◐ | SH | d3 |
| P137 | **Fan chart** | forecast fan chart | S08 | D | S◐ | SH EE | fanplot; forecast::autoplot |
| P138 | **Waterfall plot (stacked traces)** | 3-D spectral waterfall | S19 | H | S◐ | PE | matplotlib; Origin |
| P139 | **Braided graph** |  | S08 | D | N○ | SH | d3 |

## F07 Networks & hierarchies  *(29)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P140 | **Node-link network diagram** | graph diagram; sociogram | S13 | D | U● | XM SH LS | igraph; ggraph; networkx; Gephi; Cytoscape |
| P141 | **Force-directed graph** |  | S13 | D | X◐ | XM LS SH | d3-force; networkD3; Gephi |
| P142 | **Adjacency matrix plot** |  | S13 | D | S◐ | XM LS | ggraph; seaborn.heatmap |
| P143 | **Arc diagram** |  | S13 | D | X◐ | XM SH LS | ggraph::geom_edge_arc; arcdiagram |
| P144 | **Chord diagram** | circular relationship diagram | S13 | D | U● | LS SH EE | circlize::chordDiagram; d3-chord |
| P145 | **Non-ribbon chord diagram** |  | S13 | D | N○ | XM | d3 |
| P146 | **Hive plot** |  | S13 | D | S◐ | LS XM | HiveR; jhive |
| P147 | **Sankey diagram** |  | S15 | D | U● | EE SH HM | networkD3; ggalluvial; plotly; SankeyMATIC |
| P148 | **Alluvial diagram** |  | S15 | D | U● | HM SH LS | ggalluvial; easyalluvial |
| P149 | **Parallel sets** | categorical parallel coordinates | S15 | D | S◐ | SH XM | ggforce::geom_parallel_sets; d3 |
| P150 | **Flow map** |  | S16 | D | S◐ | SH EE | flowmapblue; ggplot2+sf |
| P151 | **Dendrogram** | hierarchical clustering tree | S14 | D | U● | LS XM SH | stats::hclust; ggdendro; dendextend; scipy.cluster |
| P152 | **Tanglegram** |  | S04 | D | S◐ | LS | dendextend::tanglegram; ape::cophyloplot |
| P153 | **Phylogenetic tree** | cladogram; phylogram; unrooted tree | S14 | D | S◐ | LS | ggtree; ape; ETE3; iTOL; FigTree |
| P154 | **Time-scaled phylogeny** | phylodynamic tree; BEAST tree | S14 | D | S◐ | LS HM | ggtree; BEAST/TreeAnnotator; treeio |
| P155 | **Tree diagram** | hierarchy tree | S14 | D | S◐ | XM SH | ggraph; DiagrammeR |
| P156 | **Decision tree diagram** |  | S14 | D | U● | XM HM | rpart.plot; sklearn.tree.plot_tree; DiagrammeR |
| P157 | **Circos plot** | circular genome plot | S23 | D | S◐ | LS | circlize; Circos; pyCircos |
| P158 | **Ideogram / karyotype plot** |  | S23 | D | S◐ | LS HM | karyoploteR; RIdeogram; chromoMap |
| P159 | **Bipartite network plot** |  | S13 | D | S◐ | LS SH | bipartite; bipartiteD3; networkx |
| P160 | **Directed acyclic graph** | DAG; causal diagram | S27 | C | S◐ | HM SH | dagitty; ggdag; DiagrammeR |
| P161 | **Transmission tree** | outbreak transmission network | S13 | D | S◐ | HM LS | outbreaker2; epicontacts; TransPhylo |
| P162 | **Contact network** | contact tracing graph | S13 | D | N○ | HM | epicontacts; igraph |
| P163 | **Metabolic flux map** |  | S16 | D | S◐ | LS | Escher; COBRApy |
| P164 | **Pathway diagram** | KEGG map; Reactome diagram; SBGN map | S13 | H | S◐ | LS HM | pathview; ggkegg; CellDesigner; Cytoscape |
| P165 | **Gene regulatory network plot** |  | S13 | D | S◐ | LS | igraph; Cytoscape; SCENIC |
| P166 | **Protein-protein interaction network** |  | S13 | D | S◐ | LS | STRING; Cytoscape; igraph |
| P167 | **Enrichment map** | EMAP; functional network | S16 | D | S◐ | LS | enrichplot::emapplot; Cytoscape EnrichmentMap |
| P168 | **Gene-concept network** | cnetplot | S13 | D | N○ | LS | enrichplot::cnetplot |

## F08 Maps & spatial  *(28)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P169 | **Choropleth map** |  | S16 | D | U● | SH EE HM | sf+ggplot2; tmap; geopandas; leaflet |
| P170 | **Bivariate choropleth** |  | S16 | D | S◐ | SH EE | biscale; bivariatechoropleths |
| P171 | **Cartogram** | contiguous / non-contiguous / Dorling cartogram | S16 | D | S◐ | SH HM | cartogram; cartogramR; ScapeToad |
| P172 | **Dot density map** |  | S16 | D | S◐ | SH HM | sf; tmap |
| P173 | **Proportional symbol map** | bubble map; graduated symbol map | S16 | D | X◐ | SH EE HM | tmap; ggplot2+sf; leaflet |
| P174 | **Isopleth map** | isarithmic map; contour map | S16 | D | S◐ | EE | metR; gstat; matplotlib.contour |
| P175 | **Kernel density surface map** | hotspot map | S16 | D | S◐ | SH HM | spatstat; ggplot2::stat_density_2d |
| P176 | **Hexbin map** | tile grid map; tilegram | S16 | D | S◐ | SH | geogrid; tilegramsR; d3-hexbin |
| P177 | **Connection map** | great-circle map; desire line map | S16 | D | S◐ | SH EE | stplanr; ggplot2+sf; geosphere |
| P178 | **Origin-destination flow map** |  | S16 | D | S◐ | SH | stplanr; flowmapblue |
| P179 | **Isochrone map** | travel-time map | S16 | D | S◐ | SH HM | osrm; r5r; OpenRouteService |
| P180 | **Voronoi / Thiessen polygon map** |  | S16 | D | S◐ | EE SH | deldir; sf::st_voronoi |
| P181 | **LISA cluster map** | spatial autocorrelation map; Moran cluster map | S16 | D | X◐ | SH HM EE | spdep; rgeoda; GeoDa; PySAL |
| P182 | **Moran scatterplot** |  | S16 | D | S◐ | SH EE | spdep::moran.plot; PySAL |
| P183 | **Semivariogram** | variogram | S16 | D | S◐ | EE | gstat; geoR; scikit-gstat |
| P184 | **Kriging interpolation surface** |  | S16 | D | S◐ | EE | gstat; automap; PyKrige |
| P185 | **Spatial scan cluster map** | SaTScan cluster map | S16 | D | S◐ | HM | SaTScan; scanstatistics; smerc |
| P186 | **Standardised mortality/incidence ratio map** |  | S16 | D | S◐ | HM | SpatialEpi; INLA |
| P187 | **Satellite / raster imagery map** | true-colour composite | S16 | H | N○ | EE | terra; raster; rasterio; Google Earth Engine |
| P188 | **Spectral index map** | NDVI / EVI / NDWI map | S19 | H | S◐ | EE LS | terra; Google Earth Engine; rasterio |
| P189 | **Land cover classification map** |  | S16 | D | S◐ | EE | terra; randomForest; GEE |
| P190 | **Digital elevation model / hillshade** |  | S16 | H | S◐ | EE | terra; whitebox; rayshader |
| P191 | **Bathymetric map** |  | S16 | H | N○ | EE | marmap; GEBCO; oce |
| P192 | **Space-time cube** |  | S16 | D | S◐ | SH EE | stcube (ArcGIS); cubble |
| P193 | **Map projection comparison plot** |  | S16 | D | S◐ | EE SH | sf; proj; d3-geo |
| P194 | **Small-multiple map series** | map matrix | S16 | D | X◐ | EE SH HM | tmap::tm_facets; ggplot2::facet_wrap |
| P195 | **Synoptic weather chart** | surface pressure chart | S16 | H | N○ | EE | MetPy; NCL; GrADS |
| P196 | **Animal movement track map** | telemetry track | S16 | D | S◐ | LS | move; adehabitatLT; moveVis |

## F09 Uncertainty & Bayesian  *(17)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P197 | **Error bars** | SD / SEM / 95% CI bars | S18 | D | U● | LS HM PE XM | ggplot2::geom_errorbar; matplotlib.errorbar |
| P198 | **Confidence ribbon** | confidence band | S18 | D | U● | ALL | ggplot2::geom_ribbon |
| P199 | **Prediction interval plot** |  | S18 | D | X◐ | XM SH EE | ggplot2; forecast |
| P200 | **Gradient interval / eye plot / half-eye plot** |  | S18 | D | S◐ | XM SH | ggdist::stat_halfeye |
| P201 | **Hypothetical outcome plot** | HOP; animated uncertainty | S24 | D | S◐ | XM SH | gganimate; ungeviz |
| P202 | **Posterior density plot** |  | S24 | D | X◐ | XM HM EE | bayesplot; ArviZ; tidybayes |
| P203 | **MCMC trace plot** |  | S24 | D | N○ | XM | bayesplot::mcmc_trace; ArviZ |
| P204 | **MCMC rank plot** | trank plot | S24 | D | N○ | XM | bayesplot::mcmc_rank_hist; ArviZ |
| P205 | **Corner plot** | MCMC pairs plot; triangle plot | S24 | D | X● | EE XM PE | corner.py; bayesplot::mcmc_pairs; GetDist |
| P206 | **Prior-posterior overlay plot** |  | S24 | D | S◐ | XM HM | bayesplot; brms |
| P207 | **Posterior predictive check plot** | PPC plot | S24 | D | N○ | XM | bayesplot::pp_check; ArviZ |
| P208 | **Tornado diagram** | one-way sensitivity plot | S18 | D | X● | HM SH PE | dampack; ggplot2 |
| P209 | **Cost-effectiveness plane** |  | S03 | D | N● | HM | BCEA; dampack; heemod |
| P210 | **Cost-effectiveness acceptability curve** | CEAC | S18 | D | N○ | HM | BCEA; dampack |
| P211 | **Expected value of information plot** | EVPI / EVPPI plot | S24 | D | N○ | HM | BCEA; voi |
| P212 | **Markov trace plot** | state occupancy plot | S24 | D | S◐ | HM | heemod; dampack |
| P213 | **Monte Carlo simulation fan** | scenario spaghetti plot | S24 | D | X◐ | SH EE HM | ggplot2; matplotlib |

## F10 ML & classifier evaluation  *(20)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P214 | **ROC curve** | receiver operating characteristic curve | S22 | D | U● | HM XM LS | pROC; ROCR; yardstick; sklearn.RocCurveDisplay |
| P215 | **Precision-recall curve** | PR curve | S22 | D | S● | XM LS | PRROC; yardstick; sklearn.PrecisionRecallDisplay |
| P216 | **Confusion matrix heatmap** |  | S12 | D | U● | XM HM | caret; sklearn.ConfusionMatrixDisplay; cvms |
| P217 | **Calibration plot** | reliability diagram | S22 | D | X● | HM XM EE | rms::val.prob; sklearn.CalibrationDisplay; probably |
| P218 | **Decision curve analysis** | net benefit curve | S22 | D | S● | HM | dcurves; rmda; dcurves (py) |
| P219 | **Lift chart / cumulative gains chart** |  | S22 | D | S◐ | SH XM | modelplotr; scikit-plot |
| P220 | **Learning curve** | sample-size curve | S22 | D | N○ | XM | sklearn.learning_curve; yardstick |
| P221 | **Training loss curve** | epoch curve; convergence plot | S22 | D | N● | XM | TensorBoard; keras history; wandb |
| P222 | **Validation curve** | hyperparameter sweep plot | S22 | D | N○ | XM | sklearn.validation_curve; Optuna |
| P223 | **Feature importance plot** | variable importance plot; VIP | S22 | D | U● | XM LS HM | vip; randomForest::varImpPlot; sklearn |
| P224 | **SHAP beeswarm plot** | SHAP summary plot | S22 | D | S● | XM HM | shap; shapviz; kernelshap |
| P225 | **SHAP dependence plot** |  | S22 | D | N○ | XM | shap; shapviz |
| P226 | **SHAP force / waterfall plot** |  | S22 | D | S◐ | XM HM | shap; shapviz |
| P227 | **Partial dependence plot** | PDP | S22 | D | S● | XM EE | pdp; DALEX; sklearn.PartialDependenceDisplay |
| P228 | **Individual conditional expectation plot** | ICE plot | S22 | D | N○ | XM | ICEbox; pdp; sklearn |
| P229 | **LIME explanation plot** |  | S22 | D | N○ | XM | lime; lime (py) |
| P230 | **Silhouette plot** |  | S11 | D | S◐ | XM LS | cluster::silhouette; factoextra; yellowbrick |
| P231 | **Elbow plot** | within-cluster SS plot | S11 | D | S◐ | XM LS | factoextra::fviz_nbclust; yellowbrick |
| P232 | **Saliency map / attention heatmap** | Grad-CAM overlay | S16 | H | S◐ | XM HM | pytorch-grad-cam; captum |
| P233 | **Embedding projection plot** | latent space scatter | S11 | D | S◐ | XM LS | umap-learn; Rtsne; TensorBoard Projector |

## F11 Survival & time-to-event  *(13)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P234 | **Kaplan-Meier curve** | survival curve; product-limit plot | S17 | D | U● | HM LS | survminer::ggsurvplot; survival; lifelines |
| P235 | **Number-at-risk table** |  | S17 | D | S◐ | HM | survminer; ggsurvfit |
| P236 | **Cumulative incidence function plot** | competing risks CIF | S17 | D | S● | HM | cmprsk; tidycmprsk; lifelines |
| P237 | **Nelson-Aalen cumulative hazard plot** |  | S17 | D | S◐ | HM PE | survival; lifelines |
| P238 | **Log-minus-log survival plot** | proportional hazards check | S17 | D | N○ | HM | survival |
| P239 | **Schoenfeld residual plot** |  | S17 | D | N● | HM | survival::cox.zph; survminer::ggcoxzph |
| P240 | **Swimmer plot** |  | S17 | D | S● | HM | swimplot; ggswim; swimmeR |
| P241 | **Spider plot (tumour response)** | tumour growth trajectory plot | S08 | D | N○ | HM | ggplot2; RECIST toolkits |
| P242 | **Waterfall plot (best tumour response)** | RECIST waterfall | S17 | D | N● | HM | ggplot2; waterfall |
| P243 | **Restricted mean survival time plot** | RMST plot | S17 | D | N○ | HM | survRM2 |
| P244 | **Landmark analysis plot** |  | S17 | D | N○ | HM | survival; ggsurvfit |
| P245 | **Weibull probability plot** |  | S17 | D | S● | PE HM | WeibullR; reliability (py) |
| P246 | **Bathtub curve** | hazard function over lifetime | S27 | C | N○ | PE | conceptual/illustrative |

## F12 Meta-analysis & evidence  *(20)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P247 | **Forest plot** |  | S18 | D | U● | HM SH | metafor::forest; meta; forestplot; PythonMeta |
| P248 | **Funnel plot (publication bias)** |  | S18 | D | N● | HM | metafor::funnel; meta::funnel |
| P249 | **Contour-enhanced funnel plot** |  | S18 | D | N○ | HM | metafor::funnel(level=) |
| P250 | **Radial plot (Galbraith)** |  | S18 | D | S◐ | HM EE | metafor::radial; IsoplotR |
| P251 | **L'Abbe plot** |  | S18 | D | N○ | HM | meta::labbe |
| P252 | **Baujat plot** | heterogeneity contribution plot | S18 | D | N○ | HM | metafor::baujat |
| P253 | **Network meta-analysis geometry plot** | network graph of comparisons | S13 | D | N● | HM | netmeta::netgraph |
| P254 | **League table heatmap (NMA)** |  | S18 | D | N○ | HM | netmeta; nmadata |
| P255 | **Rankogram / SUCRA plot** |  | S18 | D | N○ | HM | netmeta::rankogram |
| P256 | **Risk-of-bias traffic light plot** |  | S18 | D | N● | HM | robvis |
| P257 | **Risk-of-bias summary bar plot** |  | S18 | D | N○ | HM | robvis |
| P258 | **Meta-regression bubble plot** |  | S18 | D | S◐ | HM SH | metafor::regplot |
| P259 | **Cumulative meta-analysis plot** |  | S18 | D | N○ | HM | metafor::cumul |
| P260 | **Leave-one-out sensitivity plot** |  | S18 | D | N○ | HM | metafor::leave1out; meta::metainf |
| P261 | **Albatross plot** |  | S18 | D | N○ | HM | albatross (Stata); ggplot2 |
| P262 | **Doi plot / LFK index** |  | S18 | D | N○ | HM | MetaXL; metasens |
| P263 | **Effect direction plot** |  | S18 | D | S◐ | HM SH | ggplot2 |
| P264 | **PRISMA flow diagram** |  | S15 | D | S● | HM SH | PRISMA2020; PRISMAstatement; DiagrammeR |
| P265 | **CONSORT flow diagram** |  | S15 | D | N● | HM | consort; DiagrammeR |
| P266 | **Evidence gap map** |  | S16 | D | S◐ | HM SH | EPPI-Mapper; ggplot2 |

## F13 Epidemiology & public health  *(12)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P267 | **Epidemic curve** | epi curve | S08 | D | S● | HM | incidence2; EpiCurve; ggplot2 |
| P268 | **Compartmental model trajectory plot** | SIR/SEIR curve | S08 | D | S◐ | HM XM | deSolve; EpiModel; scipy.integrate |
| P269 | **Effective reproduction number plot** | Rt plot | S08 | D | N● | HM | EpiEstim; EpiNow2 |
| P270 | **Age-period-cohort plot** |  | S08 | D | S◐ | HM SH | Epi; apc |
| P271 | **Institutional funnel plot** | caterpillar/funnel for provider comparison | S18 | D | S◐ | HM | FunnelPlotR |
| P272 | **Care cascade plot** | treatment cascade | S15 | D | S◐ | HM | ggplot2 |
| P273 | **Dose-response curve** | concentration-response curve; IC50/EC50 curve | S22 | D | S● | LS HM | drc; nplr; GraphPad Prism; scipy |
| P274 | **Benchmark dose (BMD) plot** |  | S22 | D | S◐ | LS HM | bmd; BMDS (EPA); PROAST |
| P275 | **Life table survival plot** |  | S08 | D | S◐ | SH HM | demography; lifecontingencies |
| P276 | **Cohort component projection plot** |  | S08 | D | N○ | SH | popprojection; ggplot2 |
| P277 | **Attributable fraction plot** |  | S08 | D | N○ | HM | AF; ggplot2 |
| P278 | **Exposure-lag-response surface** | DLNM 3-D surface | S25 | D | S◐ | HM EE | dlnm |

## F14 Genomics & transcriptomics  *(38)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P279 | **Volcano plot** |  | S03 | D | S● | LS HM | EnhancedVolcano; ggplot2; ggVolcano |
| P280 | **MA plot (expression)** | mean-difference plot | S03 | D | N● | LS | DESeq2::plotMA; limma::plotMA |
| P281 | **Manhattan plot** |  | S23 | D | S● | LS HM | qqman; CMplot; ggmanh; manhattanly |
| P282 | **GWAS Q-Q plot** | lambda inflation plot | S01 | D | S◐ | LS HM | qqman::qq; CMplot |
| P283 | **Miami plot** | two-trait mirrored Manhattan | S23 | D | S◐ | LS HM | hudson; ggplot2 |
| P284 | **Circular Manhattan plot** |  | S23 | D | N○ | LS | CMplot |
| P285 | **LocusZoom plot** | regional association plot | S23 | D | S◐ | LS HM | locuszoomr; LocusZoom; gassocplot |
| P286 | **Linkage disequilibrium heatmap** | LD plot | S23 | D | N○ | LS | LDheatmap; Haploview; LDlinkR |
| P287 | **Clustered expression heatmap** | z-scored gene heatmap | S12 | D | U● | LS HM | pheatmap; ComplexHeatmap; scanpy.pl.heatmap |
| P288 | **GSEA enrichment plot** | running enrichment score plot | S05 | D | S● | LS | fgsea; clusterProfiler; GSEA desktop |
| P289 | **GO/pathway dot plot** |  | S13 | D | N○ | LS | clusterProfiler::dotplot; enrichplot |
| P290 | **Ridgeline enrichment plot** |  | S26 | D | N○ | LS | enrichplot::ridgeplot |
| P291 | **PCA plot of samples (RNA-seq QC)** |  | S11 | D | N○ | LS | DESeq2::plotPCA; PCAtools |
| P292 | **Sample-sample distance heatmap** |  | S12 | D | N○ | LS | DESeq2; pheatmap |
| P293 | **Sashimi plot** | splice junction plot | S23 | D | N● | LS | ggsashimi; IGV; rmats2sashimiplot |
| P294 | **Genome browser track plot** |  | S23 | H | N○ | LS | Gviz; IGV; pyGenomeTracks; UCSC Genome Browser |
| P295 | **Read coverage / pileup plot** |  | S23 | D | N○ | LS | Gviz; deepTools; IGV |
| P296 | **Metagene profile plot** | TSS/TES profile plot | S23 | D | S◐ | LS | deepTools plotProfile; ngs.plot |
| P297 | **Peak-centred heatmap** | ChIP/ATAC signal heatmap | S23 | D | N○ | LS | deepTools plotHeatmap; EnrichedHeatmap |
| P298 | **Peak annotation pie / bar plot** |  | S23 | D | N○ | LS | ChIPseeker |
| P299 | **Motif enrichment logo plot** |  | S23 | D | N○ | LS | HOMER; MEME; ggseqlogo |
| P300 | **Hi-C contact matrix heatmap** |  | S23 | D | N○ | LS | HiCExplorer; Juicebox; cooltools |
| P301 | **Hi-C arc / loop plot** |  | S23 | D | N○ | LS | pyGenomeTracks; Sushi |
| P302 | **Oncoprint** | mutation waterfall matrix | S12 | D | S● | HM LS | ComplexHeatmap::oncoPrint; maftools; cBioPortal |
| P303 | **Lollipop mutation plot** | protein domain mutation plot | S05 | D | S◐ | HM LS | maftools::lollipopPlot; g3viz; MutationMapper |
| P304 | **Mutational signature plot** | 96-trinucleotide context bar plot | S01 | D | S● | LS HM | MutationalPatterns; SigProfiler; sigminer |
| P305 | **Copy number profile plot** |  | S23 | D | S◐ | LS HM | CNVkit; GenVisR; copynumber |
| P306 | **Rainfall plot** | mutation density along genome | S23 | D | N○ | LS | maftools::rainfallPlot |
| P307 | **Fish plot** | clonal evolution plot; muller plot | S23 | D | S◐ | LS HM | fishplot; timescape; ggmuller |
| P308 | **Tumour mutational burden plot** |  | S01 | D | N○ | HM | maftools::tcgaCompare |
| P309 | **Synteny dot plot** | genome alignment dot plot | S23 | D | S◐ | LS | D-GENIES; MUMmer mummerplot; syntenyPlotteR |
| P310 | **Sequence logo** |  | S01 | D | S● | LS | ggseqlogo; WebLogo; seqLogo; logomaker |
| P311 | **Multiple sequence alignment plot** |  | S23 | D | S◐ | LS | ggmsa; Jalview; msa |
| P312 | **Haplotype network** |  | S13 | D | S◐ | LS | pegas::haploNet; PopART |
| P313 | **Admixture / STRUCTURE bar plot** | ancestry proportion plot | S23 | D | S◐ | LS SH | pophelper; ADMIXTURE; STRUCTURE |
| P314 | **Principal component ancestry plot** |  | S11 | D | N○ | LS | SNPRelate; PLINK; ggplot2 |
| P315 | **Karyotype / chromosome painting plot** |  | S23 | D | S◐ | LS | karyoploteR; RIdeogram |
| P316 | **Pedigree chart** | kinship diagram; family tree | S14 | D | S◐ | HM SH | kinship2; pedigreemm; Progeny |

## F15 Single-cell & spatial omics  *(18)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P317 | **t-SNE embedding plot** |  | S11 | D | S● | LS | Rtsne; Seurat::DimPlot; scanpy.pl.tsne |
| P318 | **UMAP embedding plot** |  | S11 | D | S● | LS | umap; Seurat::DimPlot; scanpy.pl.umap |
| P319 | **Feature plot** | expression-on-embedding plot | S11 | D | N○ | LS | Seurat::FeaturePlot; scanpy.pl.umap(color=) |
| P320 | **Single-cell dot plot** | marker gene dot plot | S12 | D | N○ | LS | Seurat::DotPlot; scanpy.pl.dotplot |
| P321 | **Stacked violin plot** |  | S02 | D | N○ | LS | scanpy.pl.stacked_violin; Seurat::VlnPlot |
| P322 | **QC violin panel** | nFeature / nCount / percent.mt plot | S02 | D | N○ | LS | Seurat::VlnPlot; scanpy.pl.violin |
| P323 | **Knee plot** | barcode rank plot | S24 | D | N○ | LS | DropletUtils::barcodeRanks; CellRanger |
| P324 | **Pseudotime trajectory plot** |  | S08 | D | S● | LS | monocle3; slingshot; scanpy PAGA |
| P325 | **RNA velocity stream plot** |  | S08 | D | S◐ | LS | scVelo; velocyto |
| P326 | **PAGA graph** |  | S11 | D | N○ | LS | scanpy.pl.paga |
| P327 | **Cell-cell communication circle plot** |  | S11 | D | S◐ | LS | CellChat; CellPhoneDB; LIANA |
| P328 | **Cell type proportion stacked bar** |  | S06 | D | N○ | LS | ggplot2; scanpy |
| P329 | **Spatial feature plot** | spot-level expression overlay | S21 | H | N○ | LS | Seurat::SpatialFeaturePlot; squidpy; Giotto |
| P330 | **Spatial domain / niche map** |  | S16 | D | N○ | LS | squidpy; BayesSpace; SpaGCN |
| P331 | **Deconvolution proportion pie map** |  | S16 | D | N○ | LS | SPOTlight; CARD; cell2location |
| P332 | **Mass cytometry (CyTOF) heatmap** |  | S12 | D | S◐ | LS | CATALYST; diffcyt |
| P333 | **FlowSOM minimum spanning tree** |  | S11 | D | N○ | LS | FlowSOM; CATALYST |
| P334 | **viSNE / opt-SNE plot** |  | S11 | D | N○ | LS | Cytobank; CATALYST |

## F16 Structural & molecular  *(23)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P335 | **Ramachandran plot** |  | S29 | D | S● | LS | bio3d; MolProbity; PyMOL; Biopython |
| P336 | **Protein structure cartoon** | ribbon diagram | S29 | D | N○ | LS | PyMOL; ChimeraX; VMD; NGLview; Mol* |
| P337 | **Surface / electrostatic potential map** |  | S16 | D | S◐ | LS | APBS; PyMOL; ChimeraX |
| P338 | **Molecular docking pose figure** |  | S29 | D | S◐ | LS | AutoDock Vina; PyMOL; Maestro |
| P339 | **2-D ligand interaction diagram** |  | S29 | D | N○ | LS | LigPlot+; PoseView; Maestro; ProLIF |
| P340 | **Cryo-EM density map figure** |  | S16 | H | N○ | LS | ChimeraX; RELION; cryoSPARC |
| P341 | **Predicted aligned error plot** | PAE plot | S29 | D | S● | LS | AlphaFold; ColabFold |
| P342 | **pLDDT-coloured structure** |  | S29 | D | N○ | LS | AlphaFold; PyMOL |
| P343 | **Residue contact map** |  | S16 | D | N○ | LS | bio3d; MDAnalysis |
| P344 | **RMSD / RMSF trajectory plot** |  | S29 | D | S◐ | LS | MDAnalysis; GROMACS; bio3d |
| P345 | **Free energy landscape plot** | FEL; funnel plot (folding) | S18 | D | S◐ | LS PE | MDAnalysis; PLUMED; matplotlib |
| P346 | **Protein domain architecture diagram** |  | S29 | D | S◐ | LS | drawProteins; Pfam; InterPro; gggenes |
| P347 | **ORTEP thermal ellipsoid plot** |  | S29 | D | S◐ | PE | ORTEP-3; Mercury; Olex2 |
| P348 | **Unit cell packing diagram** |  | S29 | D | N○ | PE | Mercury; VESTA; Diamond |
| P349 | **Electron density difference map** |  | S29 | D | S◐ | PE LS | VESTA; Coot; PyMOL |
| P350 | **Michaelis-Menten plot** |  | S22 | D | S● | LS | drc; GraphPad Prism; scipy |
| P351 | **Lineweaver-Burk plot** | double reciprocal plot | S22 | D | N○ | LS | ggplot2; GraphPad Prism |
| P352 | **Eadie-Hofstee plot** |  | S22 | D | N○ | LS | ggplot2 |
| P353 | **Hanes-Woolf plot** |  | S22 | D | N○ | LS | ggplot2 |
| P354 | **Scatchard plot** |  | S22 | D | S◐ | LS | ggplot2; GraphPad Prism |
| P355 | **Hill plot** |  | S22 | D | S◐ | LS | drc; GraphPad Prism |
| P356 | **Binding isotherm / saturation curve** |  | S22 | D | S◐ | LS | drc; GraphPad Prism |
| P357 | **Van Krevelen diagram** |  | S03 | D | X◐ | EE LS PE | MetaboAnalyst; ggplot2; iFOAM |

## F17 Ecology & biodiversity  *(21)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P358 | **Taxonomic relative abundance bar plot** | microbiome composition bar plot | S06 | D | S◐ | LS EE | phyloseq; microbiome; microViz; QIIME2 |
| P359 | **Krona chart** | hierarchical taxonomy sunburst | S14 | D | S◐ | LS | Krona; KronaTools |
| P360 | **Alpha diversity plot** | Shannon/Simpson box plot | S01 | D | S◐ | LS EE | phyloseq::plot_richness; vegan |
| P361 | **Beta diversity ordination** | PCoA/NMDS of Bray-Curtis | S11 | D | S◐ | LS EE | vegan; phyloseq::ordinate |
| P362 | **Rarefaction curve** |  | S01 | D | S● | LS EE | vegan::rarecurve; iNEXT |
| P363 | **Species accumulation curve** |  | S01 | D | S◐ | LS EE | vegan::specaccum; iNEXT |
| P364 | **Rank-abundance curve** | Whittaker plot; dominance-diversity curve | S01 | D | S◐ | LS EE | BiodiversityR; vegan::radfit |
| P365 | **LEfSe cladogram** | linear discriminant analysis effect size plot | S14 | D | N○ | LS | LEfSe; microbiomeMarker |
| P366 | **Differential abundance bubble plot** |  | S05 | D | N○ | LS | ggplot2; ANCOM-BC |
| P367 | **Species distribution model suitability map** |  | S16 | D | S◐ | LS EE | dismo; MaxEnt; ENMeval; terra |
| P368 | **Species richness map** |  | S16 | D | S◐ | LS EE | terra; letsR |
| P369 | **Food web / trophic network diagram** |  | S13 | D | N○ | LS | igraph; cheddar; Foodweb |
| P370 | **Ecological niche overlap plot** |  | S05 | D | S◐ | LS | ecospat; hypervolume |
| P371 | **Population dynamics / abundance time series** |  | S08 | D | S◐ | LS EE | ggplot2; popbio |
| P372 | **Leslie matrix / life-cycle graph** |  | S05 | D | N○ | LS | popbio; DiagrammeR |
| P373 | **Mark-recapture survival plot** |  | S05 | D | S◐ | LS | RMark; marked |
| P374 | **Home range / utilisation distribution map** | kernel UD; MCP | S16 | D | S◐ | LS | adehabitatHR; amt; move |
| P375 | **Ethogram** | behaviour time budget plot | S05 | D | N○ | LS | BORIS; ggplot2 |
| P376 | **Phenology / growing season plot** |  | S08 | D | S◐ | LS EE | phenopix; ggplot2 |
| P377 | **Growth curve (organismal / OD600)** |  | S22 | D | S◐ | LS | growthcurver; growthrates; ggplot2 |
| P378 | **Bacterial growth-phase plot** | lag/log/stationary curve | S22 | D | N○ | LS | growthcurver; ggplot2 |

## F18 Ordination & dim reduction  *(21)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P379 | **PCA scores plot** |  | S11 | D | U● | ALL | prcomp; factoextra; sklearn.PCA; PCAtools |
| P380 | **PCA biplot** |  | S11 | D | X◐ | LS EE SH | ggbiplot; factoextra::fviz_pca_biplot |
| P381 | **Scree plot** | eigenvalue plot | S11 | D | U● | XM SH LS | factoextra::fviz_eig; psych |
| P382 | **Loadings plot** |  | S11 | D | S◐ | LS PE | factoextra; pca3d |
| P383 | **Parallel analysis plot** |  | S11 | D | S◐ | SH | psych::fa.parallel |
| P384 | **PLS-DA / OPLS-DA scores plot** |  | S11 | D | S◐ | LS PE | ropls; mixOmics; MetaboAnalyst |
| P385 | **VIP score plot** |  | S11 | D | N○ | LS | mixOmics; ropls |
| P386 | **LDA / discriminant plot** |  | S11 | D | S◐ | XM LS | MASS::lda; sklearn.LDA |
| P387 | **Correspondence analysis biplot** |  | S11 | D | S◐ | SH LS | ca; FactoMineR::CA |
| P388 | **Multiple correspondence analysis plot** | MCA | S11 | D | S◐ | SH | FactoMineR::MCA; factoextra |
| P389 | **Multidimensional scaling plot** | MDS; PCoA; classical scaling | S11 | D | X◐ | LS SH XM | cmdscale; vegan; sklearn.MDS |
| P390 | **NMDS ordination plot** | non-metric MDS | S11 | D | S● | LS EE | vegan::metaMDS |
| P391 | **Shepard / stress plot** |  | S11 | D | S◐ | LS XM | vegan::stressplot |
| P392 | **Canonical correspondence analysis triplot** | CCA triplot | S11 | D | S◐ | LS EE | vegan::cca |
| P393 | **Redundancy analysis plot** | RDA | S11 | D | S◐ | LS EE | vegan::rda |
| P394 | **Procrustes plot** |  | S11 | D | S◐ | LS | vegan::procrustes; geomorph |
| P395 | **Self-organising map plot** | Kohonen map | S16 | D | S◐ | XM EE | kohonen; minisom |
| P396 | **SEM path diagram** | structural equation model diagram | S11 | D | S◐ | SH LS | semPlot; lavaanPlot; DiagrammeR |
| P397 | **Psychometric network plot** | Gaussian graphical model plot | S13 | D | S◐ | SH HM | qgraph; bootnet |
| P398 | **Geometric morphometrics shape plot** | Procrustes/PCA shape space; wireframe deformation | S11 | D | S◐ | LS SH | geomorph; Morpho; MorphoJ |
| P399 | **Thin-plate spline deformation grid** |  | S11 | D | S◐ | LS SH | geomorph; Morpho |

## F19 Compositional & simplex  *(18)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P400 | **Ternary plot** | triangle plot; simplex plot; de Finetti diagram | S09 | D | X● | EE PE LS SH | Ternary (CRAN); ggtern; plotly; python-ternary; mpltern |
| P401 | **Ternary contour / heatmap plot** |  | S09 | D | S◐ | EE PE | Ternary; ggtern; mpltern |
| P402 | **Quaternary plot** | tetrahedral / 3-simplex plot | S09 | D | S◐ | PE EE | Ternary; plotly 3D |
| P403 | **Soil texture triangle** | USDA texture triangle | S09 | D | S● | EE | soiltexture (CRAN); ggtern; soil_texture (py) |
| P404 | **QAPF diagram** | Streckeisen diagram | S09 | D | N○ | EE | GCDkit; ggtern; Ternary |
| P405 | **AFM diagram** | alkali-FeO-MgO diagram | S09 | D | S◐ | EE | GCDkit; ggtern |
| P406 | **TAS diagram** | total alkali-silica diagram | S09 | D | N● | EE | GCDkit; tas (R); ggplot2 |
| P407 | **Harker diagram** | oxide vs SiO2 variation diagram | S03 | D | N○ | EE | GCDkit; ggplot2 |
| P408 | **Spider diagram** | normalised multi-element plot | S03 | D | N○ | EE | GCDkit; ggplot2 |
| P409 | **REE chondrite-normalised plot** | rare earth element pattern | S03 | D | N○ | EE | GCDkit; ggplot2 |
| P410 | **Pearce discrimination diagram** | tectonic discrimination diagram | S03 | D | S◐ | EE | GCDkit; ggtern |
| P411 | **Piper diagram** | Piper trilinear diagram | S09 | D | S● | EE | hydrogeo; smwrGraphs; WQChartPy |
| P412 | **Stiff diagram** |  | S09 | D | N○ | EE | hydrogeo; WQChartPy |
| P413 | **Schoeller diagram** |  | S09 | D | N○ | EE | WQChartPy; smwrGraphs |
| P414 | **Durov diagram** |  | S09 | D | N○ | EE | WQChartPy |
| P415 | **Gibbs diagram (water chemistry)** |  | S09 | D | S◐ | EE | WQChartPy; ggplot2 |
| P416 | **Compositional log-ratio biplot** | CLR/ILR biplot | S09 | D | X● | XM LS EE | compositions; robCompositions; scikit-bio |
| P417 | **De Finetti diagram (genotype frequencies)** | Hardy-Weinberg ternary plot | S09 | D | S◐ | LS | HardyWeinberg; ggtern |

## F20 Directional & circular  *(17)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P418 | **Rose diagram** | circular histogram; polar rose | S10 | D | S● | EE LS | circular; Directional; openair; matplotlib polar |
| P419 | **Wind rose** |  | S10 | D | S● | EE PE | openair::windRose; plotly barpolar; windrose (py) |
| P420 | **Wave / current rose** |  | S10 | D | N○ | EE | openair; oce |
| P421 | **Pollution rose** |  | S10 | D | S◐ | EE | openair::pollutionRose |
| P422 | **Polar plot** | polar coordinate scatter/line | S10 | D | S◐ | EE PE | openair::polarPlot; matplotlib polar |
| P423 | **Stereonet** | equal-area (Schmidt) net; Wulff net; lower-hemisphere projection | S10 | D | S● | EE | mplstereonet; RFOC; Stereonet (Allmendinger); OpenStereo |
| P424 | **Pole figure** | crystallographic texture plot | S10 | D | S● | PE | MTEX; pymatgen; orix |
| P425 | **Inverse pole figure** | IPF map | S10 | D | S◐ | PE | MTEX; orix |
| P426 | **Orientation distribution function plot** | ODF section plot | S10 | D | S◐ | PE | MTEX |
| P427 | **Focal mechanism beachball plot** | fault plane solution | S10 | D | N● | EE | obspy.imaging.beachball; RFOC; pyrocko |
| P428 | **Circular density plot** |  | S10 | D | S◐ | LS EE | circular; bpnreg |
| P429 | **Actogram** | double-plotted actogram | S20 | H | S◐ | LS HM | ActogramJ; ClockLab; GGIR; actogram (py) |
| P430 | **Circadian phase / acrophase plot** | cosinor plot | S10 | D | S◐ | LS HM | cosinor; cosinor2; CircaCompare |
| P431 | **Phase portrait** | phase plane plot | S10 | D | X◐ | PE XM LS | phaseR; matplotlib |
| P432 | **Poincare plot (HRV)** | return map | S10 | D | S◐ | HM | RHRV; neurokit2 |
| P433 | **Circular dendrogram** | fan tree | S10 | D | S◐ | LS | ggtree(layout=circular); dendextend; iTOL |
| P434 | **Compass / orientation vector plot** |  | S10 | D | S◐ | EE LS | circular; oce |

## F21 Spectra & signals  *(40)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P435 | **Optical absorption spectrum** | UV-Vis spectrum | S19 | H | S◐ | PE LS | hyperSpec; ChemoSpec; Origin |
| P436 | **Fluorescence emission/excitation spectrum** |  | S19 | H | S◐ | PE LS | hyperSpec; Origin |
| P437 | **Excitation-emission matrix contour** | EEM plot | S19 | H | S◐ | EE PE | eemR; staRdom; drEEM |
| P438 | **Infrared / FTIR spectrum** |  | S19 | H | S◐ | PE LS | hyperSpec; ChemoSpec; OPUS |
| P439 | **Raman spectrum** |  | S19 | H | S◐ | PE LS | hyperSpec; ramanspy; LabSpec |
| P440 | **Circular dichroism spectrum** |  | S19 | H | S◐ | LS | CDPro; DichroWeb; Origin |
| P441 | **1-D NMR spectrum** |  | S19 | H | S◐ | PE LS | TopSpin; MestReNova; nmrglue; rDolphin |
| P442 | **2-D NMR contour plot** | COSY; HSQC; HMBC; NOESY | S25 | H | S◐ | PE LS | NMRPipe; nmrglue; CcpNmr; MestReNova |
| P443 | **Mass spectrum** | m/z vs intensity plot | S19 | H | S● | PE LS | MSnbase; pyOpenMS; Xcalibur; mzR |
| P444 | **MS/MS annotated fragment spectrum** |  | S19 | H | S◐ | LS PE | MSnbase; Skyline; pyOpenMS |
| P445 | **Mirror plot (spectral match)** | butterfly spectrum plot | S19 | D | S◐ | LS | MSnbase; matchms; Spectra |
| P446 | **Total ion chromatogram** | TIC | S19 | H | S◐ | PE LS | xcms; MSnbase; Xcalibur |
| P447 | **Extracted ion chromatogram** | EIC / XIC | S19 | H | S◐ | LS PE | xcms; Skyline |
| P448 | **HPLC / GC chromatogram** |  | S19 | H | S◐ | PE LS | chromatographR; Chromeleon; Empower |
| P449 | **X-ray diffraction pattern** | powder XRD diffractogram | S10 | H | S● | PE EE | powdR; GSAS-II; xrayutilities; HighScore |
| P450 | **Rietveld refinement plot** | observed-calculated-difference plot | S19 | H | S◐ | PE | GSAS-II; FullProf; TOPAS |
| P451 | **Small-angle scattering curve** | SAXS/SANS I(q) plot | S19 | H | S◐ | PE LS | ATSAS; SasView; BioXTAS RAW |
| P452 | **Kratky plot** |  | S19 | D | S◐ | LS PE | ATSAS; BioXTAS RAW |
| P453 | **Guinier plot** |  | S19 | D | S◐ | PE LS | ATSAS; SasView |
| P454 | **Pair distance distribution function** | P(r) plot | S19 | D | S◐ | LS PE | ATSAS GNOM |
| P455 | **XPS spectrum with peak deconvolution** |  | S19 | H | S◐ | PE | CasaXPS; XPSPEAK; lmfit |
| P456 | **EDS / EDX spectrum** |  | S19 | H | S◐ | PE EE | HyperSpy; Aztec; Esprit |
| P457 | **EELS spectrum** |  | S19 | H | S◐ | PE | HyperSpy; DigitalMicrograph |
| P458 | **XAS / EXAFS / XANES spectrum** |  | S19 | H | S◐ | PE | Athena/Artemis (Demeter); Larch |
| P459 | **Mossbauer spectrum** |  | S19 | H | S◐ | PE EE | Recoil; MossA |
| P460 | **EPR / ESR spectrum** |  | S19 | H | S◐ | PE LS | EasySpin; SpinFit |
| P461 | **Spectrogram** | time-frequency plot; sonogram | S21 | D | X● | PE LS SH | signal; librosa; seewave; scipy.signal |
| P462 | **Power spectral density plot** | PSD; periodogram | S19 | D | X◐ | PE EE XM | signal; scipy.signal.welch; stats::spec.pgram |
| P463 | **Lomb-Scargle periodogram** |  | S19 | D | S◐ | EE LS | astropy.timeseries; lomb |
| P464 | **Wavelet scalogram** | wavelet power spectrum | S19 | D | X● | EE LS PE | WaveletComp; biwavelet; PyWavelets |
| P465 | **Coherence plot** | magnitude-squared coherence | S19 | D | S◐ | PE LS | signal; scipy.signal.coherence; MNE |
| P466 | **Bode plot** | magnitude and phase vs frequency | S03 | D | S● | PE | control (R/py); MATLAB; scipy.signal.bode |
| P467 | **Nyquist plot (control)** |  | S03 | D | N○ | PE | python-control; MATLAB |
| P468 | **Nichols chart** |  | S03 | D | N○ | PE | python-control; MATLAB |
| P469 | **Root locus plot** |  | S03 | D | N○ | PE | python-control; MATLAB |
| P470 | **Pole-zero plot** |  | S03 | D | S◐ | PE | python-control; scipy.signal |
| P471 | **Smith chart** |  | S31 | D | S◐ | PE | scikit-rf; MATLAB RF Toolbox |
| P472 | **Constellation diagram** |  | S03 | D | N○ | PE | scikit-dsp-comm; GNU Radio |
| P473 | **Eye diagram** |  | S20 | H | S◐ | PE | GNU Radio; oscilloscope |
| P474 | **Campbell diagram** |  | S03 | D | N○ | PE | MATLAB; ANSYS |

## F22 Physics, chem & materials  *(49)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P475 | **Phase diagram (thermodynamic)** | P-T; binary/ternary phase diagram | S31 | D | S● | PE EE | pycalphad; Thermo-Calc; pymatgen; FactSage |
| P476 | **Pourbaix diagram** | E-pH diagram | S31 | D | S● | PE | pymatgen; HSC Chemistry |
| P477 | **Ellingham diagram** |  | S31 | D | S◐ | PE | HSC Chemistry; ggplot2 |
| P478 | **Electronic band structure plot** |  | S29 | D | S● | PE | pymatgen; sumo; VASPKIT; ASE |
| P479 | **Density of states plot** | DOS / PDOS | S19 | D | S◐ | PE | pymatgen; sumo; VASPKIT |
| P480 | **Fermi surface plot** |  | S29 | D | N○ | PE | IFermi; XCrySDen; FermiSurfer |
| P481 | **Brillouin zone diagram** |  | S29 | D | S◐ | PE | seekpath; XCrySDen |
| P482 | **Reaction coordinate diagram** | potential energy surface profile | S03 | D | S◐ | PE | matplotlib; ChemDraw; energydiagram (py) |
| P483 | **Molecular orbital diagram** |  | S27 | C | S◐ | PE | ChemDraw; hand-drawn |
| P484 | **Jablonski diagram** |  | S27 | C | S◐ | PE LS | ChemDraw; TikZ |
| P485 | **Feynman diagram** |  | S27 | C | S◐ | PE | TikZ-Feynman; JaxoDraw; FeynGame |
| P486 | **Energy level diagram** | term scheme; Grotrian diagram | S27 | C | S◐ | PE | TikZ; matplotlib |
| P487 | **Arrhenius plot** | ln k vs 1/T | S03 | D | S◐ | PE LS | ggplot2; scipy |
| P488 | **Eyring plot** |  | S03 | D | N○ | PE | ggplot2; scipy |
| P489 | **Van 't Hoff plot** |  | S03 | D | S◐ | PE | ggplot2; scipy |
| P490 | **Tafel plot** |  | S30 | D | N○ | PE | ggplot2; EC-Lab |
| P491 | **Cyclic voltammogram** | CV curve | S30 | H | N● | PE | EC-Lab; NOVA; echem (py); cyclicvoltammetry |
| P492 | **Electrochemical impedance Nyquist plot** | EIS Nyquist plot | S30 | H | S◐ | PE | impedance.py; ZView; EC-Lab |
| P493 | **Galvanostatic charge-discharge curve** |  | S30 | H | S◐ | PE | EC-Lab; BioLogic; navani |
| P494 | **Differential capacity plot** | dQ/dV plot | S30 | D | N○ | PE | navani; ggplot2 |
| P495 | **Ragone plot** | energy vs power density | S01 | D | N○ | PE | ggplot2; matplotlib |
| P496 | **Stress-strain curve** |  | S30 | H | S● | PE | Instron Bluehill; MATLAB; ggplot2 |
| P497 | **S-N curve** | Wohler curve; fatigue curve | S30 | D | S◐ | PE | ggplot2; fatpack |
| P498 | **Creep curve** |  | S30 | H | N○ | PE | Origin; ggplot2 |
| P499 | **Nanoindentation load-displacement curve** |  | S30 | H | S◐ | PE | Hysitron TriboScan; NanoIndent |
| P500 | **TGA thermogram** | thermogravimetric curve | S19 | H | S◐ | PE | TA Universal Analysis; Origin |
| P501 | **DSC thermogram** | differential scanning calorimetry curve | S19 | H | S◐ | PE LS | TA Universal Analysis; Origin; NanoAnalyze |
| P502 | **DMA curve** | storage/loss modulus vs temperature | S30 | H | S◐ | PE | TA Universal Analysis |
| P503 | **Rheogram** | flow curve; viscosity curve | S30 | H | S◐ | PE | RheoCompass; TRIOS |
| P504 | **BET adsorption isotherm** |  | S30 | H | S◐ | PE | pyGAPS; ASAP software |
| P505 | **Langmuir / Freundlich isotherm fit** |  | S30 | D | S◐ | PE EE | pyGAPS; ggplot2; drc |
| P506 | **Breakthrough curve** |  | S30 | H | S◐ | PE EE | ggplot2; CXTFIT |
| P507 | **Psychrometric chart** |  | S31 | D | S◐ | PE | psychrolib; CoolProp; HAsPsychroChart |
| P508 | **Mollier diagram** | h-s diagram | S31 | D | S◐ | PE | CoolProp; pyromat |
| P509 | **T-s and P-v diagrams** |  | S31 | D | N○ | PE | CoolProp; pyromat |
| P510 | **Moody chart** |  | S31 | D | S◐ | PE | fluids (py); ggplot2 |
| P511 | **Pump / fan performance curve** |  | S30 | D | S◐ | PE | fluids (py); ggplot2 |
| P512 | **Magnetic hysteresis loop** | B-H loop; M-H curve | S30 | H | S◐ | PE | VSM/SQUID software; Origin |
| P513 | **I-V curve (semiconductor)** | current-voltage characteristic | S30 | H | S◐ | PE | Keithley; LabVIEW; matplotlib |
| P514 | **J-V curve (solar cell)** | photovoltaic characteristic with fill factor | S30 | H | S◐ | PE | pvlib; Origin |
| P515 | **EQE / IPCE spectrum** |  | S30 | H | S◐ | PE | Origin; matplotlib |
| P516 | **Ashby chart** | material property selection map | S31 | D | S● | PE | CES EduPack/Granta; ggplot2 |
| P517 | **Chart of nuclides** | Segre chart | S31 | D | N○ | PE | nuclear-chart tools; matplotlib |
| P518 | **Dalitz plot** |  | S03 | D | N○ | PE | ROOT; matplotlib |
| P519 | **Invariant mass histogram** | bump hunt plot | S01 | D | N○ | PE | ROOT; matplotlib; hist (py) |
| P520 | **Brazil band plot** | exclusion limit plot | S03 | D | N○ | PE | ROOT; pyhf |
| P521 | **Ray diagram** |  | S27 | C | N○ | PE | TikZ; raytracing (py) |
| P522 | **Beam profile map** | intensity cross-section | S30 | H | N○ | PE | BeamGage; matplotlib |
| P523 | **Interferogram** |  | S21 | H | S◐ | PE | Zygo MetroPro; matplotlib |

## F23 Astronomy & space  *(18)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P524 | **Hertzsprung-Russell diagram** | HR diagram | S03 | D | N● | EE | astropy; matplotlib; TOPCAT |
| P525 | **Colour-magnitude diagram** | CMD | S03 | D | N○ | EE | astropy; TOPCAT |
| P526 | **Colour-colour diagram** |  | S03 | D | N○ | EE | astropy; TOPCAT |
| P527 | **Light curve** |  | S08 | D | N● | EE | lightkurve; astropy; juliet |
| P528 | **Phase-folded light curve** |  | S08 | D | N○ | EE | lightkurve; astropy |
| P529 | **Transit light curve with model fit** |  | S08 | D | S◐ | EE | batman; exoplanet; juliet |
| P530 | **Radial velocity curve** |  | S08 | D | S◐ | EE | RadVel; exoplanet |
| P531 | **Spectral energy distribution** | SED plot | S19 | D | N○ | EE | astropy; CIGALE; sedpy |
| P532 | **All-sky projection map** | Mollweide/Aitoff/HEALPix map | S16 | D | S● | EE | healpy; astropy; Aladin |
| P533 | **Hubble diagram** |  | S08 | D | N○ | EE | astropy; matplotlib |
| P534 | **Galaxy rotation curve** |  | S08 | D | N○ | EE | matplotlib; GALPY |
| P535 | **Position-velocity diagram** |  | S03 | D | N○ | EE | CASA; spectral-cube |
| P536 | **Channel map** | velocity channel mosaic | S16 | D | N○ | EE | CASA; spectral-cube; astropy |
| P537 | **Butterfly diagram (sunspots)** |  | S08 | D | N○ | EE | SunPy; matplotlib |
| P538 | **Dynamic spectrum (radio)** |  | S19 | H | S◐ | EE | SunPy; PRESTO |
| P539 | **Sky survey mosaic / cutout figure** |  | S05 | H | N○ | EE | astropy; Aladin; DS9 |
| P540 | **Particle collision event display** |  | S26 | H | N○ | PE | ROOT; iSpy; Atlantis |
| P541 | **Power spectrum of CMB** |  | S19 | D | N○ | EE | CAMB; healpy |

## F24 Earth, climate & hydrology  *(54)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P542 | **Stratigraphic column** | lithologic log; graphic log | S01 | D | S● | EE | StratigrapheR; SedLog; TikZ |
| P543 | **Well log plot** | wireline log; composite log | S03 | H | S◐ | EE | welly; lasio; Techlog; Petrel |
| P544 | **Seismogram** | waveform record | S20 | H | N● | EE | obspy; SAC |
| P545 | **Record section plot** |  | S03 | D | N○ | EE | obspy; pyrocko |
| P546 | **Seismic reflection section** |  | S03 | H | N○ | EE | OpendTect; segyio; Petrel |
| P547 | **Gutenberg-Richter plot** | frequency-magnitude distribution | S01 | D | S◐ | EE | obspy; ggplot2 |
| P548 | **Seismic hazard curve** |  | S03 | D | N○ | EE | OpenQuake; ggplot2 |
| P549 | **ShakeMap** | ground motion intensity map | S16 | D | N○ | EE | USGS ShakeMap; terra |
| P550 | **Geological cross-section** |  | S27 | H | N○ | EE | GeoScene3D; Move; Illustrator |
| P551 | **Fence diagram** |  | S25 | D | S◐ | EE | RockWorks; Leapfrog |
| P552 | **Isopach map** | thickness contour map | S16 | D | S◐ | EE | gstat; Surfer; Petrel |
| P553 | **Concordia diagram** | U-Pb Wetherill/Tera-Wasserburg plot | S03 | D | N● | EE | IsoplotR; Isoplot; DensityPlotter |
| P554 | **Isochron diagram** | Rb-Sr / Sm-Nd isochron | S03 | D | N○ | EE | IsoplotR; Isoplot |
| P555 | **Ar-Ar age spectrum plot** | plateau age plot | S19 | D | N○ | EE | IsoplotR; ArArCALC |
| P556 | **Detrital zircon KDE plot** | age distribution KDE/PDP | S01 | D | S◐ | EE | provenance; detzrcr; DensityPlotter |
| P557 | **Fission-track length distribution plot** |  | S01 | D | N○ | EE | IsoplotR; HeFTy |
| P558 | **Time-temperature history plot** | thermal history envelope | S03 | D | N○ | EE | HeFTy; QTQt |
| P559 | **Pollen diagram** |  | S03 | D | S● | EE | rioja; riojaPlot; Tilia; C2 |
| P560 | **Microfossil stratigraphic diagram** | diatom/foraminifera diagram | S03 | D | S◐ | EE | rioja; C2 |
| P561 | **Age-depth model plot** |  | S03 | D | S◐ | EE | rbacon; Bchron; clam |
| P562 | **Tree-ring chronology plot** | dendrochronology series plot | S03 | D | S◐ | EE LS | dplR; dendroTools |
| P563 | **Skeleton plot (dendrochronology)** |  | S03 | D | N○ | EE | dplR |
| P564 | **Ice core isotope depth profile** |  | S03 | D | S◐ | EE | ggplot2; PaleoSpec |
| P565 | **Stable isotope cross plot** | d18O vs d13C plot | S03 | D | S◐ | EE LS | ggplot2; isotope R packages |
| P566 | **Keeling plot** |  | S03 | D | S◐ | EE | ggplot2; SIBER |
| P567 | **Isotope mixing model plot** | SIBER/MixSIAR biplot | S11 | D | S◐ | LS EE | SIBER; MixSIAR; simmr |
| P568 | **Climate stripes** | warming stripes | S08 | D | N○ | EE | ggplot2; #ShowYourStripes |
| P569 | **Climate spiral** |  | S08 | D | N○ | EE | gganimate; matplotlib |
| P570 | **Temperature anomaly time series** |  | S08 | D | N○ | EE | ggplot2; xarray |
| P571 | **Taylor diagram** | model skill diagram | S22 | D | S● | EE XM | plotrix::taylor.diagram; openair; SkillMetrics |
| P572 | **Target diagram** |  | S22 | D | S◐ | EE | SkillMetrics |
| P573 | **Koppen climate classification map** |  | S31 | D | S◐ | EE | kgc; terra |
| P574 | **Climograph** | Walter-Lieth diagram; ombrothermic diagram | S03 | D | S◐ | EE | climatol; ggplot2 |
| P575 | **Skew-T log-P diagram** | atmospheric sounding plot | S03 | H | N● | EE | MetPy; SHARPpy |
| P576 | **Tephigram** |  | S03 | D | N○ | EE | MetPy; tephi (py) |
| P577 | **Emagram / Stuve diagram** |  | S03 | D | N○ | EE | MetPy |
| P578 | **Hydrograph** | streamflow time series | S08 | D | N● | EE | hydroTSM; ggplot2 |
| P579 | **Flow duration curve** |  | S01 | D | N○ | EE | hydroTSM; hydrostats |
| P580 | **Rating curve** | stage-discharge curve | S22 | D | N○ | EE | bdrc; ggplot2 |
| P581 | **Unit hydrograph** |  | S08 | D | N○ | EE | topmodel; ggplot2 |
| P582 | **Double mass curve** |  | S08 | D | S◐ | EE | ggplot2 |
| P583 | **IDF curve** | intensity-duration-frequency curve | S01 | D | S◐ | EE | IDF; ggplot2 |
| P584 | **Flood frequency curve** |  | S01 | D | S◐ | EE | lmomRFA; ggplot2 |
| P585 | **Grain size distribution curve** | particle size cumulative curve | S01 | D | S● | EE PE | G2Sd; GRADISTAT; ggplot2 |
| P586 | **Hjulstrom / Shields diagram** |  | S31 | D | N○ | EE | ggplot2 |
| P587 | **T-S diagram** | temperature-salinity diagram | S03 | D | N● | EE | oce; gsw; matplotlib |
| P588 | **CTD profile plot** | depth profile of T/S/O2 | S03 | H | N○ | EE | oce; python-ctd |
| P589 | **Depth-time section** | oceanographic section plot | S08 | D | N○ | EE | oce; xarray |
| P590 | **Tidal harmonic / tide curve plot** |  | S08 | D | N○ | EE | TideHarmonics; oce; UTide |
| P591 | **Sea-ice extent time series** |  | S08 | D | S◐ | EE | xarray; ggplot2 |
| P592 | **Soil profile diagram** | soil horizon description plot | S27 | H | N○ | EE | aqp; ggplot2 |
| P593 | **Water balance diagram** |  | S05 | D | N○ | EE | SPEI; ggplot2 |
| P594 | **Emissions / scenario pathway plot** | RCP/SSP pathway plot | S13 | D | S◐ | EE SH | ggplot2; pyam |
| P595 | **Land use change Sankey** |  | S15 | D | S◐ | EE | networkD3; ggalluvial |

## F26 Gels, blots & electrophoresis  *(17)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P596 | **Western blot** | immunoblot | S26 | L | S● | LS HM | WET LAB: SDS-PAGE + transfer + antibody + ECL/near-IR detection. Imagers: ChemiDoc, LI-COR Odyssey, iBright. Quantify: ImageJ/Fiji, Image Lab, Empiria Studio |
| P597 | **Southern blot** |  | S26 | L | S◐ | LS | WET LAB: DNA restriction digest + transfer + labelled probe hybridisation |
| P598 | **Northern blot** |  | S26 | L | S◐ | LS | WET LAB: denaturing RNA gel + transfer + probe hybridisation |
| P599 | **Far-western blot** |  | S26 | L | S◐ | LS | WET LAB: protein-protein interaction detection on membrane |
| P600 | **Dot blot / slot blot** |  | S26 | L | S◐ | LS | WET LAB: direct spotting onto membrane + probe |
| P601 | **Agarose gel electrophoresis image** |  | S26 | L | S● | LS | WET LAB: agarose gel + EtBr/SYBR + UV/blue-light transilluminator. Quantify: ImageJ, Image Lab |
| P602 | **SDS-PAGE stained gel** | Coomassie / silver stain gel | S26 | L | S◐ | LS | WET LAB: polyacrylamide gel + protein stain |
| P603 | **Native PAGE / Blue-native PAGE** |  | S26 | L | S◐ | LS | WET LAB: non-denaturing electrophoresis |
| P604 | **2-D gel electrophoresis** | IEF x SDS-PAGE gel | S26 | L | N○ | LS | WET LAB + analysis software: Delta2D, PDQuest, Melanie |
| P605 | **Zymogram** | zymography gel | S26 | L | S◐ | LS | WET LAB: substrate-embedded gel + activity staining |
| P606 | **EMSA** | electrophoretic mobility shift assay; gel shift | S26 | L | S◐ | LS | WET LAB: labelled probe + protein binding + native gel |
| P607 | **Pulsed-field gel electrophoresis** | PFGE | S26 | L | S◐ | LS | WET LAB: alternating-field electrophoresis |
| P608 | **Comet assay image** | single cell gel electrophoresis | S26 | L | S◐ | LS HM | WET LAB + scoring: OpenComet, CometScore, CaspLab |
| P609 | **Autoradiograph** |  | S26 | L | S◐ | LS | WET LAB: radiolabel + film/phosphor screen (Typhoon, Amersham) |
| P610 | **Sanger sequencing chromatogram** | electropherogram trace | S20 | H | S◐ | LS HM | Instrument output. View/analyse: Chromas, SnapGene, sangerseqR, ApE |
| P611 | **Bioanalyzer / TapeStation trace** | virtual gel + electropherogram | S20 | H | S◐ | LS | Agilent 2100 Expert; TapeStation Analysis; bioanalyzeR |
| P612 | **Capillary electrophoresis electropherogram** |  | S20 | H | S◐ | LS PE | Instrument software; Fragman; Fragment Analyzer |

## F25 Lab imaging & microscopy  *(41)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P613 | **Brightfield micrograph** |  | S26 | L | S● | LS HM | MICROSCOPE. Process: Fiji/ImageJ, QuPath, CellProfiler |
| P614 | **Phase contrast micrograph** |  | S26 | L | S◐ | LS | MICROSCOPE. Process: Fiji, CellProfiler |
| P615 | **DIC micrograph** | Nomarski differential interference contrast | S26 | L | S◐ | LS | MICROSCOPE. Process: Fiji |
| P616 | **Darkfield micrograph** |  | S26 | L | N○ | LS | MICROSCOPE |
| P617 | **Immunofluorescence micrograph** | multi-channel merge; IF image | S26 | L | S● | LS HM | MICROSCOPE + antibodies. Process: Fiji, CellProfiler, QuPath, napari |
| P618 | **Confocal micrograph** | z-stack; orthogonal view; max projection | S26 | L | S◐ | LS | CONFOCAL. Process: Fiji, Imaris, Huygens, napari |
| P619 | **Super-resolution micrograph** | STORM; PALM; STED; SIM | S26 | L | S◐ | LS | SR MICROSCOPE. Reconstruct: ThunderSTORM, Picasso, SMAP |
| P620 | **Kymograph** |  | S21 | H | S◐ | LS | Derived from time-lapse. Fiji KymographBuilder, KymoResliceWide |
| P621 | **Time-lapse montage** | frame series figure | S26 | L | S◐ | LS | LIVE IMAGING. Assemble: Fiji, Imaris |
| P622 | **FRAP recovery curve** |  | S20 | H | S◐ | LS | Confocal bleach + quantify: Fiji, easyFRAP, simFRAP |
| P623 | **FRET efficiency image / ratio map** |  | S16 | H | S◐ | LS | Fiji FRET plugins; PixFRET; FLIMfit |
| P624 | **Calcium imaging trace + heatmap** | dF/F trace array | S20 | H | N○ | LS | Suite2p; CaImAn; Fiji |
| P625 | **Light-sheet volumetric render** |  | S26 | L | S◐ | LS | LIGHT-SHEET. Render: Imaris, napari, Vaa3D, arivis |
| P626 | **Transmission electron micrograph** | TEM image | S26 | L | S◐ | LS PE | TEM. Process: Fiji, DigitalMicrograph |
| P627 | **Scanning electron micrograph** | SEM image | S26 | L | X◐ | PE LS EE | SEM. Process: Fiji, ImageJ |
| P628 | **Cryo-EM micrograph & 2-D class averages** |  | S26 | L | N○ | LS | CRYO-EM. Process: RELION, cryoSPARC, cisTEM |
| P629 | **Immunogold electron micrograph** |  | S26 | L | N○ | LS | TEM + gold-conjugated antibody |
| P630 | **Correlative light-EM figure** | CLEM | S26 | L | N○ | LS | CLEM workflow. Align: Fiji ec-CLEM |
| P631 | **AFM height map** | atomic force micrograph | S16 | H | S● | PE LS | Gwyddion; NanoScope Analysis; pySPM |
| P632 | **STM image** | scanning tunnelling micrograph | S26 | H | S◐ | PE | Gwyddion; WSxM; SpectraFox |
| P633 | **EBSD orientation map** | IPF map from EBSD | S16 | H | S● | PE EE | MTEX; Aztec Crystal; OIM Analysis; orix |
| P634 | **Cathodoluminescence image** |  | S26 | L | S◐ | EE PE | SEM-CL. Process: Fiji |
| P635 | **Metallographic micrograph** |  | S26 | L | N○ | PE | Polish + etch + optical microscope. Quantify: Fiji |
| P636 | **Fractography image** |  | S26 | L | S◐ | PE | SEM of fracture surface |
| P637 | **Histology micrograph** | H&E stained section | S26 | L | S● | HM LS | HISTOLOGY. Analyse: QuPath, Fiji, HALO |
| P638 | **Special stain micrograph** | Masson trichrome; PAS; Congo red; Oil Red O | S26 | L | S◐ | HM LS | HISTOLOGY. Quantify: QuPath, Fiji colour deconvolution |
| P639 | **Immunohistochemistry micrograph** | IHC; DAB staining | S26 | L | S◐ | HM LS | IHC. Score: QuPath, HALO, Aperio |
| P640 | **In situ hybridisation image** | ISH; FISH; RNAscope | S26 | L | S◐ | LS HM | ISH protocols. Analyse: HALO, QuPath, Fiji |
| P641 | **Tissue microarray panel** | TMA figure | S26 | L | S◐ | HM | TMA + scanner. Analyse: QuPath, TMAJ |
| P642 | **Whole-slide image** | digital pathology scan | S26 | L | N○ | HM | Slide scanner. View/analyse: QuPath, OpenSlide, ASAP |
| P643 | **Chromosome spread / karyotype image** |  | S26 | L | S◐ | LS HM | Metaphase spread + banding. Software: Ikaros, CytoVision |
| P644 | **Spectral karyotyping image** | SKY; M-FISH | S19 | L | S◐ | HM LS | SKY imaging system |
| P645 | **Multiplexed tissue imaging figure** | CODEX; imaging mass cytometry; MIBI | S21 | H | S◐ | LS HM | steinbock; napari; QuPath; MCD Viewer |
| P646 | **TLC plate image** | thin-layer chromatography plate | S26 | L | S◐ | PE LS | WET LAB: TLC + visualisation (UV, stain) |
| P647 | **Crystal habit photograph** |  | S26 | L | S◐ | PE EE | Optical/stereo microscope photography |
| P648 | **Schlieren / shadowgraph image** |  | S26 | L | N○ | PE | Schlieren optical setup + high-speed camera |
| P649 | **PIV vector field** | particle image velocimetry | S21 | H | S● | PE | PIVlab; OpenPIV; DaVis |
| P650 | **Thermal / infrared camera image** |  | S21 | H | X◐ | PE EE HM | FLIR Tools; ThermImageJ |
| P651 | **High-speed camera frame sequence** |  | S26 | L | S◐ | PE LS | High-speed camera. Assemble: Fiji |
| P652 | **Ultrasonic C-scan / NDT map** |  | S16 | H | S◐ | PE | NDT software; Fiji |
| P653 | **Industrial CT slice / 3-D render** | micro-CT of materials | S21 | H | S◐ | PE EE | Dragonfly; Avizo; 3D Slicer; Fiji |

## F27 Flow cytometry & plate assays  *(32)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P654 | **Flow cytometry dot plot** | bivariate FCM plot with gates | S03 | H | S● | LS HM | FlowJo; FCS Express; flowCore; CytoExploreR |
| P655 | **Flow cytometry histogram** | single-parameter FCM histogram | S01 | H | S◐ | LS HM | FlowJo; FCS Express; flowCore |
| P656 | **Flow cytometry contour / density plot** |  | S01 | H | N○ | LS | FlowJo; ggcyto |
| P657 | **Gating strategy figure** | gating hierarchy/tree | S14 | H | S◐ | LS HM | FlowJo; openCyto |
| P658 | **Backgating plot** |  | S26 | H | N○ | LS | FlowJo |
| P659 | **Cell cycle histogram** | PI/DAPI DNA content with model fit | S01 | H | S◐ | LS | ModFit LT; FlowJo Cell Cycle; flowPloidy |
| P660 | **CFSE proliferation histogram** | division peak modelling | S01 | H | N○ | LS | FlowJo Proliferation; FCS Express |
| P661 | **ELISA standard curve** | 4-parameter logistic fit | S22 | D | S◐ | LS HM | drc; GraphPad Prism; nplr; MyAssays |
| P662 | **ELISpot plate image + spot counts** |  | S26 | H | S◐ | LS HM | ImmunoSpot; AID EliSpot; CTL |
| P663 | **qPCR amplification curve** |  | S20 | H | S● | LS | Instrument software (QuantStudio, LightCycler); pcr; qpcR |
| P664 | **qPCR melt curve** | dissociation / derivative plot | S20 | H | N○ | LS | Instrument software; MeltR |
| P665 | **ddPCR droplet plot** | 1-D/2-D droplet amplitude plot | S26 | H | S◐ | LS HM | QuantaSoft; ddpcr; twoddpcr |
| P666 | **Plate heatmap** | 96/384-well plate map | S16 | D | S◐ | LS | platetools; ggplot2 |
| P667 | **Drug synergy isobologram** |  | S22 | D | S◐ | LS HM | synergyfinder; CompuSyn |
| P668 | **Drug synergy surface** | Bliss/Loewe/HSA/ZIP synergy landscape | S22 | D | S◐ | LS HM | SynergyFinder; synergyfinder (R) |
| P669 | **Colony formation assay image** | clonogenic assay plate | S26 | L | S◐ | LS | WET LAB: stain + plate scan. Count: ColonyArea, OpenCFU, Fiji |
| P670 | **Scratch / wound healing assay montage** |  | S26 | L | S◐ | LS | Live imaging (IncuCyte). Quantify: Fiji Wound Healing Tool |
| P671 | **Transwell migration / invasion image** |  | S26 | L | N○ | LS | WET LAB: stained membrane micrograph. Count: Fiji |
| P672 | **Spheroid / organoid growth image series** |  | S26 | L | S◐ | LS | Live imaging. Quantify: Fiji, INSIDIA, OrganoSeg |
| P673 | **Zone of inhibition plate** | Kirby-Bauer disc diffusion plate | S26 | L | S◐ | LS HM | WET LAB: agar plate photograph. Measure: calipers, Fiji, ADAGIO |
| P674 | **MIC microdilution plate image** |  | S26 | L | S◐ | LS HM | WET LAB: broth microdilution plate read |
| P675 | **Antibiogram heatmap** | resistance profile heatmap | S12 | D | S◐ | HM LS | ComplexHeatmap; AMR (R); WHONET |
| P676 | **Plaque assay plate** |  | S26 | L | N○ | LS | WET LAB: viral plaque plate. Count: Fiji, Viridot |
| P677 | **Haemagglutination assay plate** |  | S26 | L | S◐ | LS HM | WET LAB: V-bottom plate read |
| P678 | **SPR sensorgram** | surface plasmon resonance trace | S20 | H | S● | LS | Biacore Evaluation; Scrubber |
| P679 | **BLI sensorgram** | bio-layer interferometry trace | S20 | H | N○ | LS | Octet Data Analysis |
| P680 | **ITC thermogram + binding isotherm** |  | S19 | H | S● | LS PE | NanoAnalyze; Origin ITC; MicroCal PEAQ |
| P681 | **Thermal shift melt curve** | DSF; Thermofluor | S20 | H | S◐ | LS | Protein Thermal Shift; MoltenProt; DSFworld |
| P682 | **MST binding curve** | microscale thermophoresis | S26 | H | N○ | LS | MO.Affinity Analysis |
| P683 | **Seahorse OCR/ECAR trace** | extracellular flux plot | S20 | H | S◐ | LS | Wave (Agilent); ggplot2 |
| P684 | **xCELLigence impedance trace** | real-time cell analysis curve | S20 | H | S◐ | LS | RTCA Software |
| P685 | **Microelectrode array raster / activity map** |  | S20 | H | N○ | LS | Axion AxIS; MEA-Tools; Multi Channel Analyzer |

## F28 Clinical & preclinical imaging  *(19)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P686 | **Radiograph** | plain X-ray film | S26 | L | S◐ | HM | X-RAY MACHINE. View: PACS, Horos, 3D Slicer |
| P687 | **CT slice / MPR / 3-D volume render** |  | S21 | H | N○ | HM | 3D Slicer; Horos; OsiriX; ITK-SNAP |
| P688 | **MRI image** | T1 / T2 / FLAIR / DWI sequence | S21 | H | S◐ | HM LS | FSL; SPM; 3D Slicer; ITK-SNAP; freesurfer |
| P689 | **Ultrasound image / echocardiogram** |  | S26 | L | S◐ | HM | ULTRASOUND MACHINE. Analyse: EchoPAC, ImageJ |
| P690 | **Doppler flow image / spectral Doppler trace** |  | S19 | L | S◐ | HM | Ultrasound system |
| P691 | **Angiogram** | coronary/cerebral angiography | S26 | L | S◐ | HM | Catheter lab imaging + QCA software |
| P692 | **PET / SPECT uptake image** |  | S21 | H | S◐ | HM | 3D Slicer; PMOD; MIM |
| P693 | **PET time-activity curve / SUV plot** |  | S08 | D | S◐ | HM | PMOD; kinfitr |
| P694 | **Fundus photograph** |  | S26 | L | S◐ | HM | Fundus camera. Analyse: EyeQ, ImageJ |
| P695 | **OCT retinal scan** |  | S21 | H | S◐ | HM | OCT device; OCTExplorer |
| P696 | **Endoscopy / colonoscopy image** |  | S26 | L | S◐ | HM | Endoscopy tower |
| P697 | **Dermoscopy image** |  | S26 | L | S◐ | HM | Dermatoscope |
| P698 | **In vivo bioluminescence / fluorescence image** | IVIS image | S26 | L | S● | LS HM | IVIS Spectrum + Living Image software; Bruker In-Vivo Xtreme |
| P699 | **Micro-CT reconstruction** | small-animal CT; bone microarchitecture | S21 | H | S◐ | LS HM | 3D Slicer; Dragonfly; CTAn; BoneJ |
| P700 | **Small-animal MRI / preclinical MRI** |  | S21 | H | S◐ | LS | Bruker ParaVision; FSL |
| P701 | **Behavioural tracking heatmap** | open field / EPM occupancy map | S21 | H | S◐ | LS | EthoVision XT; ANY-maze; DeepLabCut; ezTrack |
| P702 | **Pose estimation trace** | DeepLabCut / SLEAP keypoint trajectory | S08 | H | S◐ | LS | DeepLabCut; SLEAP; DeepEthogram |
| P703 | **Gait analysis / motion capture stick figure** |  | S29 | H | S◐ | HM LS | Vicon Nexus; OpenSim; CatWalk |
| P704 | **Camera trap detection timeline / image** |  | S08 | H | S◐ | LS | camtrapR; Wildlife Insights; MegaDetector |

## F29 Electrophysiology & neuroimaging  *(22)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P705 | **Patch-clamp trace** | whole-cell current/voltage recording | S20 | H | S● | LS | Clampfit/pCLAMP; Stimfit; Igor NeuroMatic |
| P706 | **Patch-clamp I-V relationship** |  | S03 | D | S◐ | LS | Clampfit; ggplot2 |
| P707 | **Spike raster plot** |  | S08 | D | N● | LS | Elephant; Neo; MATLAB; ggplot2 |
| P708 | **Peri-stimulus time histogram** | PSTH | S01 | D | N○ | LS | Elephant; MATLAB; ggplot2 |
| P709 | **Local field potential trace** |  | S20 | H | N○ | LS | Neo; MNE; SpikeInterface |
| P710 | **Spike sorting cluster plot** | waveform + PCA cluster plot | S20 | D | N○ | LS | SpikeInterface; Kilosort/Phy; MountainSort |
| P711 | **EEG multichannel trace** |  | S20 | H | S● | HM LS | MNE-Python; EEGLAB; FieldTrip; Brainstorm |
| P712 | **EEG topographic scalp map** | topoplot | S20 | D | S◐ | LS HM | MNE-Python; EEGLAB; eegUtils |
| P713 | **ERP waveform plot** | event-related potential plot | S20 | D | S◐ | SH LS | MNE-Python; ERPLAB; eegUtils |
| P714 | **Time-frequency / ERSP plot** |  | S20 | D | S◐ | LS SH | MNE-Python; EEGLAB; FieldTrip |
| P715 | **MEG source localisation map** |  | S16 | D | S◐ | LS HM | MNE-Python; Brainstorm; FieldTrip |
| P716 | **fMRI statistical parametric map** | activation map; SPM overlay | S21 | D | X● | SH HM LS | SPM; FSL; AFNI; nilearn; fMRIPrep |
| P717 | **Glass brain plot** |  | S21 | D | S◐ | SH LS | nilearn; SPM |
| P718 | **Cortical surface render** | inflated surface map | S29 | D | S◐ | LS SH | FreeSurfer; Connectome Workbench; pysurfer |
| P719 | **Cortical thickness / morphometry map** |  | S21 | D | S◐ | HM LS | FreeSurfer; CAT12; ANTs |
| P720 | **DTI tractography render** | fibre tract visualisation | S29 | D | S● | LS HM | MRtrix3; DSI Studio; TrackVis; DIPY |
| P721 | **Brain connectivity matrix** | connectome matrix | S12 | D | S◐ | LS SH | BCT; nilearn; netplotbrain |
| P722 | **Connectogram** | circular brain connectivity plot | S13 | D | S◐ | LS | circlize; BrainNet Viewer; MNE |
| P723 | **ECG trace** | electrocardiogram | S20 | H | N○ | HM | neurokit2; wfdb; instrument printout |
| P724 | **EMG trace** | electromyogram | S20 | H | S◐ | HM LS | neurokit2; biosppy; Delsys |
| P725 | **Actigraphy / accelerometer trace** |  | S20 | H | S◐ | HM | GGIR; ActiLife; accelerometry |
| P726 | **Polysomnogram / hypnogram** |  | S20 | H | S◐ | HM | YASA; sleep scoring software |

## F30 Text, qualitative & humanities  *(19)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P727 | **Word cloud** | tag cloud | S28 | D | S◐ | SH | wordcloud2; wordcloud; python wordcloud |
| P728 | **Word tree** |  | S28 | D | S◐ | SH | Voyant Tools; d3 |
| P729 | **Concordance / KWIC display** | keyword in context | S28 | D | S◐ | SH | quanteda::kwic; AntConc; NLTK |
| P730 | **Lexical dispersion plot** |  | S28 | D | S◐ | SH | quanteda::textplot_xray; NLTK dispersion_plot |
| P731 | **Keyness plot** |  | S28 | D | S◐ | SH | quanteda::textstat_keyness |
| P732 | **Topic model visualisation** | LDAvis intertopic distance map | S16 | D | S● | SH XM | LDAvis; pyLDAvis; BERTopic |
| P733 | **Topic prevalence over time plot** |  | S28 | D | S◐ | SH | stm; BERTopic |
| P734 | **Semantic / text network plot** |  | S28 | D | S◐ | SH | quanteda; igraph; textnets |
| P735 | **Sentiment arc** | narrative arc plot | S28 | D | S◐ | SH | syuzhet; sentimentr |
| P736 | **Stylometry bootstrap consensus tree** |  | S28 | D | S◐ | SH | stylo |
| P737 | **Character co-occurrence network** |  | S28 | D | S◐ | SH | igraph; Gephi |
| P738 | **Sequence index plot** | life-course sequence plot | S08 | D | S● | SH | TraMineR; seqHMM |
| P739 | **State distribution plot** | chronogram | S08 | D | S◐ | SH | TraMineR |
| P740 | **Qualitative code matrix / code map** |  | S16 | D | S◐ | SH | NVivo; MAXQDA; ATLAS.ti |
| P741 | **Discourse network plot** |  | S28 | D | S◐ | SH | Discourse Network Analyzer; rDNA |
| P742 | **Manuscript stemma** | textual transmission tree | S28 | D | S◐ | SH | stemmaweb; PhyloBayes |
| P743 | **Piano roll / score visualisation** |  | S16 | D | N○ | SH | music21; librosa |
| P744 | **Historical network map** | Palladio-style spatial network | S16 | D | S◐ | SH | Palladio; Gephi; ggplot2+sf |
| P745 | **Archaeological site plan / harris matrix** |  | S27 | C | N○ | SH | Harris Matrix Composer; QGIS |

## F31 Social science & econometrics  *(29)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P746 | **Lorenz curve** |  | S01 | D | S● | SH | ineq; gglorenz; ggplot2 |
| P747 | **Concentration / Gini plot** |  | S01 | D | S◐ | SH HM | ineq; rineq |
| P748 | **Growth incidence curve** |  | S01 | D | N○ | SH | ggplot2 |
| P749 | **Impulse response function plot** | IRF plot | S22 | D | S◐ | SH | vars; statsmodels VAR |
| P750 | **Forecast error variance decomposition plot** |  | S22 | D | N○ | SH | vars; statsmodels |
| P751 | **Event study plot** | dynamic treatment effect plot | S22 | D | S● | SH HM | fixest::iplot; did; eventstudyr |
| P752 | **Difference-in-differences plot** | parallel trends plot | S22 | D | S◐ | SH HM | did; fixest; ggplot2 |
| P753 | **Regression discontinuity plot** | RD plot | S22 | D | S● | SH | rdrobust::rdplot; rddensity |
| P754 | **McCrary density test plot** |  | S22 | D | N○ | SH | rddensity; rdd |
| P755 | **Synthetic control gap plot** |  | S22 | D | S◐ | SH | Synth; tidysynth; gsynth |
| P756 | **Love plot** | covariate balance plot | S22 | D | S● | HM SH | cobalt::love.plot; MatchIt |
| P757 | **Propensity score overlap plot** | common support plot | S22 | D | S◐ | HM SH | cobalt; MatchIt; WeightIt |
| P758 | **E-value / sensitivity contour plot** |  | S22 | D | N○ | HM | EValue; sensemakr |
| P759 | **Item characteristic curve** | IRT trace line | S20 | D | S● | SH HM | mirt; ltm; catR |
| P760 | **Test information function plot** |  | S22 | D | S◐ | SH | mirt |
| P761 | **Wright map** | person-item map | S16 | D | S◐ | SH | WrightMap; eRm |
| P762 | **Differential item functioning plot** |  | S22 | D | S◐ | SH | difR; lordif |
| P763 | **Conjoint AMCE plot** |  | S22 | D | S◐ | SH | cregg; cjoint |
| P764 | **Blockmodel image matrix** |  | S13 | D | S◐ | SH XM | sna; blockmodeling |
| P765 | **Sociogram** |  | S13 | D | S◐ | SH | igraph; RSiena; Gephi |
| P766 | **Migration flow chord / circular plot** |  | S13 | D | S◐ | SH | circlize; migest |
| P767 | **Survey-weighted estimate plot** | design-based CI plot | S03 | D | S◐ | SH HM | survey; srvyr; ggsurvey |
| P768 | **Co-citation network map** |  | S16 | D | S◐ | XM SH | bibliometrix; VOSviewer; CiteSpace |
| P769 | **Co-authorship / collaboration map** |  | S16 | D | N○ | XM | VOSviewer; bibliometrix |
| P770 | **Keyword co-occurrence map** |  | S16 | D | N○ | XM | VOSviewer; bibliometrix |
| P771 | **Bradford's law plot** |  | S01 | D | N○ | XM | bibliometrix |
| P772 | **Lotka's law plot** |  | S01 | D | N○ | XM | bibliometrix |
| P773 | **Citation burst plot** |  | S22 | D | N○ | XM | CiteSpace |
| P774 | **Three-fields Sankey (bibliometrix)** |  | S15 | D | N○ | XM | bibliometrix |

## F32 Business, finance & ops  *(18)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P775 | **Funnel chart** | conversion funnel | S15 | D | S◐ | SH | plotly; ggplot2 |
| P776 | **Cohort retention heatmap** |  | S12 | D | S◐ | SH | ggplot2; pandas |
| P777 | **RFM segmentation heatmap** |  | S12 | D | N○ | SH | ggplot2 |
| P778 | **BCG growth-share matrix** |  | S08 | D | N○ | SH | ggplot2 |
| P779 | **Efficient frontier plot** |  | S03 | D | N○ | SH | PortfolioAnalytics; PyPortfolioOpt |
| P780 | **Drawdown chart** | underwater plot | S08 | D | N○ | SH | PerformanceAnalytics; quantstats |
| P781 | **Risk-return scatter** |  | S03 | D | N○ | SH | PerformanceAnalytics |
| P782 | **Correlation network (assets)** |  | S13 | D | S◐ | SH XM | igraph; corrplot |
| P783 | **Value-at-risk distribution plot** |  | S01 | D | N○ | SH | PerformanceAnalytics; quantstats |
| P784 | **Yield curve plot** | term structure plot | S08 | D | S● | SH | ggplot2; YieldCurve |
| P785 | **Order book depth chart** |  | S08 | D | N○ | SH | plotly; matplotlib |
| P786 | **Cumulative flow diagram** |  | S15 | D | S◐ | SH | ggplot2; Jira |
| P787 | **Burndown / burnup chart** |  | S08 | D | N○ | SH | ggplot2; Jira |
| P788 | **Value stream map** |  | S16 | C | N○ | SH | Visio; Lucidchart |
| P789 | **Queueing / capacity utilisation plot** |  | S16 | D | S◐ | SH PE | queueing; simmer |
| P790 | **Supply chain network map** |  | S16 | D | S◐ | SH | igraph; sf |
| P791 | **Pareto/ABC inventory curve** |  | S08 | D | N○ | SH | ggplot2 |
| P792 | **KPI card / big number tile** |  | S05 | D | S◐ | SH HM | flexdashboard; Shiny; Tableau |

## F33 Conceptual & schematic  *(20)*

| # | Plot | Also known as | Shape | Origin | Tier | Areas | Tools |
|---|---|---|:--:|:--:|:--:|---|---|
| P793 | **Flow chart** | process flow diagram | S27 | C | U● | ALL | DiagrammeR; mermaid; Graphviz; draw.io |
| P794 | **Mind map** | concept map | S27 | C | N○ | SH | XMind; mermaid; Graphviz |
| P795 | **Ishikawa diagram** | fishbone; cause-and-effect diagram | S27 | C | S◐ | SH PE | qcc::cause.and.effect; Visio |
| P796 | **Organisational chart** | organogram | S14 | C | N○ | SH | DiagrammeR; mermaid |
| P797 | **Entity-relationship diagram** | ERD | S27 | C | N○ | XM | mermaid; dbdiagram; Graphviz |
| P798 | **UML class / sequence diagram** |  | S27 | C | N○ | XM | PlantUML; mermaid |
| P799 | **Experimental design schematic** | study workflow figure | S27 | C | S◐ | LS HM | BioRender; Illustrator; Inkscape |
| P800 | **Mechanism / signalling pathway cartoon** |  | S27 | C | S◐ | LS HM | BioRender; Illustrator; ChemDraw |
| P801 | **Reaction scheme** | arrow-pushing mechanism diagram | S27 | C | N○ | PE | ChemDraw; MarvinSketch; RDKit |
| P802 | **Retrosynthesis tree** |  | S14 | C | N○ | PE | ChemDraw; ASKCOS |
| P803 | **Anatomical / physiological diagram** |  | S27 | C | S◐ | HM | BioRender; Servier Medical Art |
| P804 | **Causal loop diagram** | system dynamics diagram | S27 | C | S◐ | SH EE | Vensim; Stella; DiagrammeR |
| P805 | **Logic model / theory of change** |  | S27 | C | S◐ | SH HM | DiagrammeR; Visio |
| P806 | **Conceptual framework diagram** |  | S27 | C | S◐ | SH | DiagrammeR; Illustrator |
| P807 | **SWOT / 2x2 matrix** |  | S27 | C | N○ | SH | ggplot2; Visio |
| P808 | **Circuit diagram** | schematic | S27 | C | N○ | PE | KiCad; CircuiTikZ; Fritzing |
| P809 | **Engineering drawing / CAD orthographic view** |  | S27 | C | S◐ | PE | SolidWorks; AutoCAD; FreeCAD |
| P810 | **Free-body diagram** |  | S27 | C | S◐ | PE | TikZ; Illustrator |
| P811 | **Bertin reorderable matrix** |  | S12 | D | S◐ | XM SH | seriation; Bertifier |
| P812 | **Storyline / narrative chart** |  | S08 | D | S◐ | SH | d3; storyline packages |
