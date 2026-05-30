import streamlit as st

st.set_page_config(
    page_title="Double-Headed Growth | Intelligence Platform",
    page_icon="🔱",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Sidebar branding */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0D1117 0%, #161B22 100%);
        border-right: 1px solid #30363D;
    }
    [data-testid="stSidebar"] .stMarkdown h1,
    [data-testid="stSidebar"] .stMarkdown h2,
    [data-testid="stSidebar"] .stMarkdown h3 {
        color: #E6EDF3;
    }
    /* Header */
    .main-header {
        background: linear-gradient(135deg, #0D1117 0%, #1A2332 50%, #0D1117 100%);
        border: 1px solid #C41E3A;
        border-radius: 8px;
        padding: 32px 40px;
        margin-bottom: 32px;
        text-align: center;
    }
    .main-header h1 {
        font-size: 2.4rem;
        font-weight: 800;
        color: #E6EDF3;
        letter-spacing: 0.02em;
        margin: 0;
    }
    .main-header p {
        color: #8B949E;
        font-size: 1rem;
        margin-top: 8px;
    }
    .classification-badge {
        display: inline-block;
        background: #C41E3A;
        color: white;
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 0.15em;
        padding: 3px 10px;
        border-radius: 3px;
        margin-bottom: 12px;
    }
    /* KPI Cards */
    .kpi-card {
        background: #161B22;
        border: 1px solid #30363D;
        border-top: 3px solid #C41E3A;
        border-radius: 8px;
        padding: 20px 16px;
        text-align: center;
        transition: border-color 0.2s;
    }
    .kpi-card:hover { border-top-color: #1F6FEB; }
    .kpi-value {
        font-size: 1.9rem;
        font-weight: 800;
        color: #E6EDF3;
        line-height: 1.1;
    }
    .kpi-label {
        font-size: 0.75rem;
        color: #8B949E;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-top: 6px;
    }
    .kpi-delta-up { color: #3FB950; font-size: 0.8rem; }
    .kpi-delta-down { color: #C41E3A; font-size: 0.8rem; }
    /* Section headers */
    .section-header {
        color: #8B949E;
        font-size: 0.7rem;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        border-bottom: 1px solid #30363D;
        padding-bottom: 6px;
        margin-bottom: 16px;
    }
    /* Intelligence cards */
    .intel-card {
        background: #161B22;
        border: 1px solid #30363D;
        border-left: 3px solid #1F6FEB;
        border-radius: 6px;
        padding: 16px 18px;
        margin-bottom: 12px;
    }
    .intel-card.red { border-left-color: #C41E3A; }
    .intel-card.green { border-left-color: #3FB950; }
    .intel-card.yellow { border-left-color: #D29922; }
    .intel-card h4 { color: #E6EDF3; font-size: 0.9rem; margin: 0 0 6px 0; }
    .intel-card p { color: #8B949E; font-size: 0.82rem; margin: 0; line-height: 1.5; }
    /* Footer */
    .platform-footer {
        text-align: center;
        color: #484F58;
        font-size: 0.75rem;
        padding: 24px 0 8px 0;
        border-top: 1px solid #21262D;
        margin-top: 40px;
    }
    /* Divider */
    hr { border-color: #21262D; }
    /* Metric override */
    [data-testid="stMetric"] {
        background: #161B22;
        border: 1px solid #30363D;
        border-radius: 8px;
        padding: 14px 16px;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="main-header">
    <div class="classification-badge">INTELLIGENCE PLATFORM — UNCLASSIFIED RESEARCH</div>
    <h1>🔱 DOUBLE-HEADED GROWTH</h1>
    <p>Russia Sanctions Evasion Networks · Asymmetric Geopolitical Re-Routing · Banking Loopholes</p>
    <p style="color:#484F58; font-size:0.8rem; margin-top:4px;">
        Research by Makhzumul Islam Mahdi · ORCID: 0009-0007-1769-7771 · Published 2026
    </p>
</div>
""", unsafe_allow_html=True)

col1, col2, col3, col4, col5, col6 = st.columns(6)
with col1:
    st.markdown("""<div class="kpi-card">
        <div class="kpi-value">1,500+</div>
        <div class="kpi-label">Shadow Fleet Vessels</div>
        <div class="kpi-delta-down">▲ 9× since 2022</div>
    </div>""", unsafe_allow_html=True)
with col2:
    st.markdown("""<div class="kpi-card">
        <div class="kpi-value">3</div>
        <div class="kpi-label">CIS Banking Nodes</div>
        <div class="kpi-delta-up">Active pipelines</div>
    </div>""", unsafe_allow_html=True)
with col3:
    st.markdown("""<div class="kpi-card">
        <div class="kpi-value">€1.075T</div>
        <div class="kpi-label">Energy Revenue</div>
        <div class="kpi-delta-up">Since 2022</div>
    </div>""", unsafe_allow_html=True)
with col4:
    st.markdown("""<div class="kpi-card">
        <div class="kpi-value">0.4%</div>
        <div class="kpi-label">GDP Growth 2026</div>
        <div class="kpi-delta-down">▼ from 4.9% peak</div>
    </div>""", unsafe_allow_html=True)
with col5:
    st.markdown("""<div class="kpi-card">
        <div class="kpi-value">5.2%</div>
        <div class="kpi-label">CPI Inflation 2026</div>
        <div class="kpi-delta-up">▼ from 11.9% peak</div>
    </div>""", unsafe_allow_html=True)
with col6:
    st.markdown("""<div class="kpi-card">
        <div class="kpi-value">14.5%</div>
        <div class="kpi-label">Key Interest Rate</div>
        <div class="kpi-delta-down">▼ from 21% peak</div>
    </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col_a, col_b = st.columns([3, 2])
with col_a:
    st.markdown('<div class="section-header">PLATFORM OVERVIEW</div>', unsafe_allow_html=True)
    st.markdown("""
    This platform visualizes findings from the research paper **"Double-Headed Growth: Evaluating Russia's
    Sanction Evasion Networks, Asymmetric Geopolitical Re-Routing, and Banking Loopholes"** (2026).

    The study documents how Russia has survived comprehensive Western sanctions by developing a
    parallel financial ecosystem — the **"Double-Headed Growth"** model — consisting of two interdependent
    economic engines: state-directed domestic capital rationing and an adaptive grey economy operating
    through Eurasian networks.

    Use the **sidebar** to navigate between intelligence modules.
    """)
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown('<div class="section-header">KEY FINDINGS</div>', unsafe_allow_html=True)
    findings = [
        ("🏦", "CIS Card Tourism", "Russian citizens evade card bans via Bakai Bank (Kyrgyzstan), Evocabank (Armenia), and VTB Belarus, maintaining international purchasing capacity."),
        ("🏴‍☠️", "Shadow Fleet Operations", "1,500+ uninsured tankers registered under flags of convenience ship crude to Turkey and India for 'refining laundering' back to Europe."),
        ("🔐", "Unrecognized Territory Loopholes", "South Ossetia, Abkhazia, and Transnistria operate as zero-risk financial cut-outs outside Western compliance jurisdiction."),
        ("🚗", "Luxury Goods Re-Routing", "European luxury vehicles (G-Wagon, Porsche, BMW) reach Russia via China through customs reclassification as 'pre-owned' cars."),
        ("⛏️", "Siberian Crypto Mining", "State-backed crypto mining in Siberia generates alternative liquidity using cheap energy and sub-zero temperatures."),
        ("🇨🇳", "Chinese Yuan Clearing", "Direct RUB-CNY clearing matrices bypass USD/SWIFT dependency, enabling high-volume trade settlement."),
    ]
    for icon, title, desc in findings:
        st.markdown(f"""<div class="intel-card">
            <h4>{icon} {title}</h4>
            <p>{desc}</p>
        </div>""", unsafe_allow_html=True)

with col_b:
    st.markdown('<div class="section-header">INTELLIGENCE MODULES</div>', unsafe_allow_html=True)
    modules_data = [
        ("01", "Executive Summary", "KPI overview and research context"),
        ("02", "Sanctions Ecosystem", "Network graph of evasion nodes"),
        ("03", "CIS Banking Intelligence", "Sankey diagrams, capital flows"),
        ("04", "Shadow Fleet Center", "Maritime routes and vessel data"),
        ("05", "Energy Revenue Analytics", "Revenue trends and forecasts"),
        ("06", "Luxury Goods Re-Routing", "Supply chain flow diagrams"),
        ("07", "Crypto Mining Dashboard", "Digital asset infrastructure"),
        ("08", "Macroeconomic Analysis", "GDP, inflation, 2030 forecasts"),
        ("09", "Eurasian Financial Order", "Geopolitical network mapping"),
        ("10", "Research Methodology", "Framework, sources, references"),
    ]
    for num, name, desc in modules_data:
        st.markdown(f"""
        <div style="display:flex; align-items:center; padding:10px 14px; background:#161B22;
             border:1px solid #30363D; border-radius:6px; margin-bottom:8px; gap:12px;">
            <div style="font-size:0.7rem; color:#C41E3A; font-weight:700; min-width:24px;">{num}</div>
            <div>
                <div style="color:#E6EDF3; font-size:0.88rem; font-weight:600;">{name}</div>
                <div style="color:#8B949E; font-size:0.75rem;">{desc}</div>
            </div>
        </div>""", unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">RESEARCH METADATA</div>', unsafe_allow_html=True)
    meta = {
        "Author": "Makhzumul Islam Mahdi",
        "Year": "2026",
        "Classification": "Unclassified Research",
        "Data Period": "2022–2026 (Forecast to 2030)",
        "Primary Sources": "BIS, CREA, EDB, Bank of Russia",
        "Methodology": "Empirical case studies + macro modeling",
    }
    for k, v in meta.items():
        st.markdown(f"""
        <div style="display:flex; justify-content:space-between; padding:7px 0;
             border-bottom:1px solid #21262D;">
            <span style="color:#8B949E; font-size:0.8rem;">{k}</span>
            <span style="color:#E6EDF3; font-size:0.8rem; font-weight:500;">{v}</span>
        </div>""", unsafe_allow_html=True)

st.markdown('<div class="platform-footer">Double-Headed Growth Intelligence Platform · Research by Makhzumul Islam Mahdi · 2026 · For Academic and Policy Research Purposes Only</div>', unsafe_allow_html=True)
