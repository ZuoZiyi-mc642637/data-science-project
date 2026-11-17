# Macao public facilities and older residents — ongoing six-person team project

**Research question:** Across Macao's 23 land statistical zones, is the share of residents aged 65+ associated with core-four facility density?

## Scope and attribution
Class M · Team01, CISC7204, University of Macau, 2026/27 Semester1. Population: 2021; facility snapshot retrieved by the team on 29 October2026. Core four: older-person services, pharmacies, clinics and parks/gardens. Extended seven adds Chinese pharmacies, health centres and hospitals for sensitivity analysis.

Team roles: Member A — coordination; Member B — minutes and liaison; Member C — data/indicators/statistical analysis; Member D — spatial processing and mapping; Member E — interpretation and quality review; Zuo Ziyi — presentation integration, slides, introductory video and delivery. The table originates from the team's analyst handover. This portfolio analysis script regenerates selected summaries from that derived table; it does not reconstruct the complete original GIS extraction pipeline.

## Data sources and use
- [DSEC population database](https://www.dsec.gov.mo/CensosWebDB/): 2021 population and older-resident totals.
- [DSCC thematic POI service](https://webmap.gis.gov.mo/arcgis/rest/services/WebMap/MacauMap_T_POI/MapServer): facility locations and categories.
- [IAM parks and gardens](https://data.gov.mo/Detail?id=12916045-4895-408c-bfe5-c923af422e12).
- [Statistical-zone boundaries](https://webmap.gis.gov.mo/arcgis/rest/services/ThematicMap/Zone/MapServer/0).

`zone_indicators.csv` is the team's derived aggregate table, shared with source attribution for this academic portfolio. Original publishers retain their data rights; consult the linked source's current reuse conditions. No blanket open-source licence is asserted for third-party data. This folder contains zone aggregates, not individual records. `elderly_count` means older-person service facilities; `elderly_65plus` means residents aged65+.

## Reproduce
From the repository root, install `python -m pip install -r requirements.txt`, then run `python macao/analysis.py`. The script reads the included frozen table and writes two PNGs and `statistics.json` to `macao/results/`. A Python3.11+ environment is recommended. No API keys or live downloads are required for this derived-table reproduction.

## Preliminary findings and limitations
The 23 land zones contain 977 core-four records (1,143 extended-seven records). Pearson r=0.411, two-sided p=0.051; Spearman rho=0.456, p=0.029. Report both: the primary Pearson result does not pass alpha=.05, and the exploratory rank association is positive. Neither result establishes causation or service adequacy. The five-year gap prevents a same-year supply–demand assessment. Zonal aggregation, facility capacity, access across boundaries and the land-area denominator limit interpretation. Large zones such as Coloane can influence density; maps are not the evidence used to estimate correlation. Further sensitivity work remains ongoing.

## Visual design review
- **Truthful:** dates, units, all 23 observations and both exact test results are stated; count bars start at zero. Category counts are facility records, not service capacity.
- **Functional:** scatterplot position compares two numeric variables; horizontal bars compare the four category counts.
- **Beautiful:** restrained high-contrast colours, readable labels and consistent spacing reduce visual clutter.
- **Insightful:** the scatterplot distinguishes linear and rank evidence; the category chart shows why the composite is dominated by clinics and pharmacies. Neither chart supports causal claims.

## Personal learning and AI assistance
Zuo Ziyi's contribution focuses on selecting evidence and translating team analysis into a coherent visual and spoken account, while keeping claims within the data. AI assistance (OpenAI Codex) was used to prepare this portfolio page, documentation and reproduction/plotting code. Team data and computed outputs remain the evidence; peer feedback is recorded only when actually received.

## Presentation work
Zuo Ziyi prepared the team progress slides and introductory video for course submission. Those files are not publicly distributed in this portfolio.

## Scatterplot zone key

Point labels use the following IDs from the frozen analysis table.

| Plot ID | Statistical zone name |
|---|---|
| 1 | 青洲區 |
| 2 | 台山區 |
| 3 | 黑沙環及祐漢區 |
| 4 | 黑沙環新填海區 |
| 5 | 望廈及水塘區 |
| 6 | 筷子基區 |
| 7 | 林茂塘區 |
| 8 | 高士德及雅廉訪區 |
| 9 | 新橋區 |
| 10 | 沙梨頭及大三巴區 |
| 11 | 荷蘭園區 |
| 12 | 東望洋區(松山區) |
| 13 | 新口岸區 |
| 14 | 外港及南灣湖新填海區 |
| 15 | 中區 |
| 16 | 下環區 |
| 17 | 南西灣及主教山區 |
| 18 | 海洋及小潭山區 |
| 19 | 氹仔中心區 |
| 20 | 大學及北安灣區 |
| 21 | 北安及大潭山區 |
| 22 | 氹仔舊城及馬場區 |
| 23 | 路環區 |
