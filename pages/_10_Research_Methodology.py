import streamlit as st

st.set_page_config(page_title="Research Methodology | Intelligence Platform", page_icon="📖", layout="wide")

st.markdown("""
<style>
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0D1117 0%, #161B22 100%); border-right: 1px solid #30363D; }
    .section-header { color:#8B949E; font-size:0.7rem; letter-spacing:0.18em; text-transform:uppercase; border-bottom:1px solid #30363D; padding-bottom:6px; margin-bottom:16px; }
    .ref-card { background:#161B22; border:1px solid #30363D; border-left:3px solid #1F6FEB; border-radius:6px; padding:14px 16px; margin-bottom:8px; }
    .ref-num { color:#8B949E; font-size:0.72rem; font-weight:700; }
    .ref-title { color:#E6EDF3; font-size:0.85rem; font-weight:600; margin:3px 0; }
    .ref-source { color:#8B949E; font-size:0.78rem; }
</style>
""", unsafe_allow_html=True)

st.markdown('<span style="color:#C41E3A;font-size:0.7rem;letter-spacing:0.15em;font-weight:700;">MODULE 10</span>', unsafe_allow_html=True)
st.markdown('<h1 style="color:#E6EDF3; font-size:1.6rem; font-weight:800; margin:0;">📖 Research Methodology & Publication</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#8B949E; font-size:0.9rem; margin:4px 0 24px 0;">Research Framework · Data Sources · Methodology · Academic References · Author Profile</p>', unsafe_allow_html=True)

col_meta, col_ids = st.columns(2)

with col_meta:
    st.markdown('<div class="section-header">PUBLICATION METADATA</div>', unsafe_allow_html=True)
    pub_meta = [
        ("Title", "Double-Headed Growth: Evaluating Russia's Sanction Evasion Networks, Asymmetric Geopolitical Re-Routing, and Banking Loopholes"),
        ("Author", "Makhzumul Islam Mahdi"),
        ("Year of Study", "2026"),
        ("Email", "makhzumulislammahdi@gmail.com"),
        ("Classification", "Unclassified Academic Research"),
        ("Data Period", "2022–2026 (Empirical) + 2027–2030 (CBR Forecast)"),
        ("Primary Domain", "International Economics, Geopolitical Finance, Sanctions Studies"),
        ("Methodology", "Empirical Case Studies + Macroeconomic Modeling + Network Analysis"),
    ]
    for k, v in pub_meta:
        st.markdown(f"""<div style="display:flex; gap:12px; padding:9px 0; border-bottom:1px solid #21262D;">
            <span style="color:#8B949E; font-size:0.8rem; min-width:130px;">{k}</span>
            <span style="color:#E6EDF3; font-size:0.8rem;">{v}</span>
        </div>""", unsafe_allow_html=True)

with col_ids:
    st.markdown('<div class="section-header">RESEARCHER IDENTIFIERS</div>', unsafe_allow_html=True)
    ids = [
        ("ORCID", "https://orcid.org/0009-0007-1769-7771", "#3FB950"),
        ("WoS ResearcherID", "https://www.webofscience.com/wos/author/record/OOO-0072-2025", "#1F6FEB"),
        ("Figshare", "https://figshare.com/authors/Makhzumul_Mahdi/22543814", "#D29922"),
    ]
    for label, url, color in ids:
        st.markdown(f"""<div style="background:#161B22; border:1px solid #30363D; border-left:3px solid {color};
             border-radius:6px; padding:14px 16px; margin-bottom:10px;">
            <div style="color:{color}; font-size:0.7rem; font-weight:700; letter-spacing:0.1em; margin-bottom:4px;">{label}</div>
            <div style="color:#8B949E; font-size:0.78rem; word-break:break-all;">{url}</div>
        </div>""", unsafe_allow_html=True)

    st.markdown('<div class="section-header" style="margin-top:16px;">KEY CONCEPTS COINED</div>', unsafe_allow_html=True)
    concepts = [
        ("Double-Headed Growth", "#C41E3A", "A large sanctioned economy naturally develops two parallel monetary engines: state-directed domestic capital rationing and an adaptive grey economy."),
        ("Card Tourism", "#D29922", "Practice of Russian citizens opening foreign bank accounts via agents in CIS countries to maintain international payment card access."),
        ("Refining Laundering", "#1F6FEB", "Process of converting sanctioned crude oil into 'neutral' refined products via third-country refineries for re-export to sanctioning nations."),
    ]
    for term, color, definition in concepts:
        st.markdown(f"""<div style="background:#161B22; border:1px solid #30363D; border-top:2px solid {color};
             border-radius:6px; padding:12px 14px; margin-bottom:8px;">
            <div style="color:{color}; font-weight:700; font-size:0.85rem; margin-bottom:4px;">{term}</div>
            <div style="color:#8B949E; font-size:0.78rem; line-height:1.5;">{definition}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("---")
col_framework, col_method = st.columns(2)

with col_framework:
    st.markdown('<div class="section-header">RESEARCH FRAMEWORK</div>', unsafe_allow_html=True)
    framework_steps = [
        ("1", "#C41E3A", "Literature Review", "Examined classical financial models on capital controls, SWIFT network effects, and 'Weaponized Interdependence' theory — identifying the gap in micro-economic analysis of specific evasion mechanisms."),
        ("2", "#D29922", "Mathematical Formalization", "Developed the Ruble Devaluation Framework: a mathematical model of how Russia exploits currency conversion arbitrage to maintain domestic fiscal stability despite foreign currency income reduction."),
        ("3", "#1F6FEB", "Empirical Case Studies", "Section 4 examines four detailed case studies: (a) CIS Card Tourism networks, (b) Unrecognized Territory banking loopholes, (c) Shadow vessel and ghost energy financing, (d) High-end consumer re-routing via Chinese conduits."),
        ("4", "#3FB950", "Macroeconomic Trend Analysis", "Empirical data from 2022 to present, extended with CBR official baseline projections to 2030. Analyzed GDP growth, CPI, and key interest rate trajectories across four economic phases."),
        ("5", "#8B949E", "Policy Analysis & Conclusions", "Evaluated the systemic implications of financial fragmentation, the failure of unilateral blockades against systemic global suppliers, and the stabilization trajectory of the alternative Eurasian financial order."),
    ]
    for num, color, title, desc in framework_steps:
        st.markdown(f"""<div style="display:flex; gap:12px; background:#161B22; border:1px solid #30363D;
             border-radius:8px; padding:14px; margin-bottom:8px;">
            <div style="min-width:28px; height:28px; background:{color}; border-radius:50%; display:flex;
                 align-items:center; justify-content:center; font-size:0.78rem; font-weight:700;
                 color:white; flex-shrink:0;">{num}</div>
            <div>
                <div style="color:#E6EDF3; font-weight:600; font-size:0.85rem; margin-bottom:4px;">{title}</div>
                <div style="color:#8B949E; font-size:0.78rem; line-height:1.5;">{desc}</div>
            </div>
        </div>""", unsafe_allow_html=True)

with col_method:
    st.markdown('<div class="section-header">PRIMARY DATA SOURCES</div>', unsafe_allow_html=True)
    sources = [
        ("BIS", "Bank for International Settlements", "Cross-border banking statistics, quarterly review data, BIS oversight frameworks"),
        ("CBR", "Central Bank of Russia", "SPFS development data, macroeconomic baseline projections, key interest rate reports"),
        ("CREA", "Centre for Research on Energy and Clean Air", "Russia fossil fuel tracker, refining loophole analysis, shadow fleet tracking"),
        ("EDB", "Eurasian Development Bank", "CIS banking and remittance flow data, structural macroeconomic reviews"),
        ("Eurostat", "European Commission", "International trade goods statistics, Eurasian transit flows, VIN activation logs"),
        ("NBKR", "National Bank of Kyrgyz Republic", "International settlement dynamics, financial statistics"),
        ("OFAC", "U.S. Dept of Treasury", "Sanctions network documentation, TSMRBank/MRB Bank correspondence records"),
        ("CSIS", "Center for Strategic & International Studies", "FinTech sanctions circumvention, cross-border banking networks in Eurasia"),
        ("Reuters / FT", "Investigative Journalism", "Russian parallel imports, maritime sanctions evasion networks, shadow fleet logistics"),
        ("AUTOSTAT", "Analytical Agency AUTOSTAT", "VIN activation logs, vehicle registration metrics, luxury import tracking (2021-2026)"),
    ]
    for abbr, name, desc in sources:
        st.markdown(f"""<div style="background:#161B22; border:1px solid #30363D; border-radius:6px;
             padding:10px 14px; margin-bottom:6px; display:flex; gap:12px; align-items:flex-start;">
            <div style="min-width:52px; background:#21262D; border-radius:4px; padding:4px 6px;
                 text-align:center; color:#E6EDF3; font-size:0.68rem; font-weight:700; flex-shrink:0;">{abbr}</div>
            <div>
                <div style="color:#E6EDF3; font-size:0.8rem; font-weight:600;">{name}</div>
                <div style="color:#8B949E; font-size:0.73rem; margin-top:2px;">{desc}</div>
            </div>
        </div>""", unsafe_allow_html=True)

st.markdown("---")
st.markdown('<div class="section-header">ACADEMIC REFERENCES</div>', unsafe_allow_html=True)
references = [
    ("1", "Bank for International Settlements (BIS)", "BIS Quarterly Review and Cross-Border Banking Statistics", "Basel: BIS, 2025", "#1F6FEB"),
    ("2", "Bank of Russia (CBR)", "Development of the Financial Messaging System (SPFS)", "Moscow: Central Bank of the Russian Federation, 2025", "#C41E3A"),
    ("3", "Bank of Russia (CBR)", "Macroeconomic Baseline Projections and Key Interest Rate Reports", "Moscow: CBR, 2026", "#C41E3A"),
    ("4", "CREA (Centre for Research on Energy and Clean Air)", "Russia Fossil Fuel Tracker and Refining Loophole Analysis", "Helsinki: CREA, 2026", "#3FB950"),
    ("5", "Central Bank of Armenia (CBA)", "Financial Stability Report", "Yerevan: CBA, 2026", "#3FB950"),
    ("6", "Eurasian Development Bank (EDB)", "Macroeconomic Review: Structural Changes in CIS Banking and Remittance Flows", "Almaty: EDB, 2026", "#D29922"),
    ("7", "Eurostat Trade Database", "International Trade in Goods Statistics and Eurasian Transit Flows", "Brussels: European Commission, 2025", "#1F6FEB"),
    ("8", "National Bank of the Kyrgyz Republic (NBKR)", "International Settlement Dynamics and Financial Statistics", "Bishkek: NBKR, 2026", "#3FB950"),
    ("9", "U.S. Department of the Treasury (OFAC)", "Treasury Sanctions Russian Financial Networks Facilitating Procurement Platforms", "Washington D.C.: OFAC, 2024", "#C41E3A"),
    ("10", "CSIS", "FinTech Sanctions Circumvention and Cross-Border Banking Networks in Eurasia", "Washington D.C.: CSIS, 2025", "#1F6FEB"),
    ("11", "Reuters Investigations", "Russian Parallel Imports and Maritime Sanctions Evasion Networks", "Reuters Global Investigations Desk, 2025", "#8B949E"),
    ("12", "Financial Times", "Shadow Fleet Logistics and Russian Energy Re-Routing Mechanisms", "London: Financial Times, 2025", "#8B949E"),
]
ref_cols = st.columns(2)
for i, (num, author, title, source, color) in enumerate(references):
    with ref_cols[i % 2]:
        st.markdown(f"""<div class="ref-card" style="border-left-color:{color};">
            <div class="ref-num">[{num}] {author}</div>
            <div class="ref-title">{title}</div>
            <div class="ref-source">{source}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("""
<div style="background:#161B22; border:1px solid #30363D; border-radius:8px; padding:20px; margin-top:16px; text-align:center;">
    <div style="color:#E6EDF3; font-weight:700; font-size:1rem; margin-bottom:8px;">🔱 Double-Headed Growth Intelligence Platform</div>
    <div style="color:#8B949E; font-size:0.82rem; line-height:1.8;">
        Research by <strong style="color:#E6EDF3;">Makhzumul Islam Mahdi</strong> · 
        ORCID: <strong style="color:#3FB950;">0009-0007-1769-7771</strong><br>
        Platform designed to meet professional intelligence publication standards comparable to CSIS, Atlantic Council, and World Bank data platforms.<br>
        <em style="color:#484F58;">For academic and policy research purposes only. Data period: 2022–2026 empirical; 2027–2030 CBR forecast projections.</em>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div style="text-align:center; color:#484F58; font-size:0.75rem; padding:20px 0 4px 0; border-top:1px solid #21262D; margin-top:32px;">Double-Headed Growth Intelligence Platform · Module 10 · Research Methodology & Academic References</div>', unsafe_allow_html=True)
