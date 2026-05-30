# Double-Headed Growth — Geopolitical Intelligence Platform

A professional geopolitical intelligence and economic analytics platform visualizing findings from the research paper "Double-Headed Growth: Evaluating Russia's Sanction Evasion Networks, Asymmetric Geopolitical Re-Routing, and Banking Loopholes" by Makhzumul Islam Mahdi (2026).

## Run & Operate

- `streamlit run app.py --server.port 5000` — start the intelligence platform
- Required Python packages: `streamlit`, `plotly`, `pandas`, `networkx`, `numpy`
- No database required — all data is embedded from the research paper

## Stack

- Python 3.11
- Streamlit (multi-page app framework)
- Plotly (interactive charts, Sankey diagrams, geopolitical maps, network graphs)
- Pandas (data management)
- Dark theme via `.streamlit/config.toml`

## Where things live

- `app.py` — Home page (landing + KPI dashboard)
- `pages/01_Executive_Summary.py` → `pages/10_Research_Methodology.py` — 10 intelligence modules
- `.streamlit/config.toml` — Dark theme configuration (primaryColor: #C41E3A, dark background)
- `requirements.txt` — Python dependencies
- `README.md` — Platform documentation

## Architecture decisions

- Multi-page Streamlit app using the native `pages/` directory convention
- All research data embedded as Python data structures (no external DB needed)
- Custom HTML/CSS via `st.markdown(unsafe_allow_html=True)` for professional dark theme styling
- Plotly chosen for interactive Sankey diagrams, network graphs, and geo maps
- Color palette: Deep Blue (#1F6FEB), Black (#0D1117), Silver (#8B949E), Red (#C41E3A), Green (#3FB950)

## Product

10-page professional intelligence dashboard covering:
1. Executive Summary — KPIs and research overview
2. Sanctions Evasion Ecosystem — Network graph of 9 evasion nodes
3. CIS Banking Intelligence — Sankey capital flow diagrams
4. Shadow Fleet Intelligence — Maritime route map + vessel growth charts
5. Energy Revenue Analytics — Revenue trends, trade partners, forecasts to 2030
6. Luxury Goods Re-Routing — G-Wagon pipeline flow diagrams
7. Crypto Mining Dashboard — Siberian mining ecosystem and liquidity model
8. Macroeconomic Dashboard — GDP/inflation/interest rate analysis 2022–2030
9. Eurasian Financial Order — Geopolitical network map + ruble devaluation model
10. Research Methodology — Framework, 12 academic references, author profile

## User preferences

_Populate as you build — explicit user instructions worth remembering across sessions._

## Gotchas

- Always run Streamlit on port 5000 (Replit's configured port)
- Do not change `.streamlit/config.toml` server section — port and address are pre-configured
- Pages render in alphabetical order by filename; use numbered prefixes (01_, 02_) to control order

## Pointers

- See `README.md` for platform documentation and data sources
- Research data sourced from: BIS, CBR, CREA, EDB, Eurostat, NBKR, OFAC, CSIS, Reuters, FT, AUTOSTAT
