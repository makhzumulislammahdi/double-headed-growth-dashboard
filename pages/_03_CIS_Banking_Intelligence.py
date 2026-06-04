import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="CIS Banking Intelligence | Intelligence Platform", page_icon="🏦", layout="wide")

st.markdown("""
<style>
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0D1117 0%, #161B22 100%); border-right: 1px solid #30363D; }
    .section-header { color:#8B949E; font-size:0.7rem; letter-spacing:0.18em; text-transform:uppercase; border-bottom:1px solid #30363D; padding-bottom:6px; margin-bottom:16px; }
    .kpi-card { background:#161B22; border:1px solid #30363D; border-top:3px solid #C41E3A; border-radius:8px; padding:20px 16px; text-align:center; }
    .kpi-value { font-size:1.7rem; font-weight:800; color:#E6EDF3; }
    .kpi-label { font-size:0.72rem; color:#8B949E; letter-spacing:0.08em; text-transform:uppercase; margin-top:6px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<span style="color:#C41E3A;font-size:0.7rem;letter-spacing:0.15em;font-weight:700;">MODULE 03</span>', unsafe_allow_html=True)
st.markdown('<h1 style="color:#E6EDF3; font-size:1.6rem; font-weight:800; margin:0;">🏦 CIS Banking Network Intelligence</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#8B949E; font-size:0.9rem; margin:4px 0 24px 0;">Capital Flow Architecture · Sankey Analysis · Money Movement Intelligence · Banking Node Profiles</p>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
kpis = [
    ("$3.5B", "Kyrgyzstan Remittances", "#C41E3A"),
    ("$1.01B", "Armenia Banking Profit", "#1F6FEB"),
    ("$31B", "Kyrgyz Crypto Volume", "#D29922"),
    ("3 Nodes", "Active CIS Gateways", "#3FB950"),
]
for col, (val, label, color) in zip([c1,c2,c3,c4], kpis):
    with col:
        st.markdown(f"""<div class="kpi-card" style="border-top-color:{color}">
            <div class="kpi-value">{val}</div>
            <div class="kpi-label">{label}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-header">MULTI-CHANNEL CAPITAL TRANSMISSION — SANKEY DIAGRAM</div>', unsafe_allow_html=True)

labels = [
    "Sanctioned Russian Rubles",   # 0
    "SPFS Messaging Rail",          # 1
    "Bakai Bank (Kyrgyzstan)",      # 2
    "Evocabank (Armenia)",          # 3
    "VTB Belarus",                  # 4
    "CIS Correspondent Layer",      # 5
    "Chinese Regional Banks",       # 6
    "RUB-CNY Clearing Matrix",      # 7
    "International Retail Payments",# 8
    "Foreign Exchange (FX)",        # 9
    "Cross-Border Trade",           # 10
    "Global Procurement",           # 11
]

source = [0, 0, 0, 0, 1, 1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 10]
target = [1, 2, 3, 4, 5, 6, 9, 8, 10, 6, 7, 7, 11, 11, 11, 11]
value  = [50, 20, 15, 15, 25, 25, 20, 15, 15, 15, 10, 20, 30, 15, 20, 15]

colors_node = [
    "#C41E3A","#8B949E","#3FB950","#3FB950","#3FB950",
    "#1F6FEB","#1F6FEB","#D29922","#D29922","#D29922","#D29922","#E6EDF3"
]
colors_link = [
    "rgba(196,30,58,0.35)","rgba(196,30,58,0.35)","rgba(196,30,58,0.35)","rgba(196,30,58,0.35)",
    "rgba(31,111,235,0.35)","rgba(31,111,235,0.35)",
    "rgba(63,185,80,0.35)","rgba(63,185,80,0.35)","rgba(63,185,80,0.35)",
    "rgba(31,111,235,0.35)","rgba(31,111,235,0.35)",
    "rgba(210,153,34,0.35)","rgba(210,153,34,0.35)","rgba(210,153,34,0.35)",
    "rgba(230,237,243,0.35)","rgba(230,237,243,0.35)",
]

fig_sankey = go.Figure(go.Sankey(
    arrangement="snap",
    node=dict(
        pad=20, thickness=20,
        line=dict(color="#30363D", width=0.5),
        label=labels,
        color=colors_node,
        hovertemplate="%{label}<extra></extra>",
    ),
    link=dict(
        source=source, target=target, value=value,
        color=colors_link,
    )
))
fig_sankey.update_layout(
    plot_bgcolor="#0D1117", paper_bgcolor="#161B22",
    font=dict(color="#E6EDF3", size=11),
    title=dict(text="Russia → CIS Banks → Global Payments: Capital Flow Architecture", font=dict(size=13, color="#E6EDF3"), x=0),
    margin=dict(l=10, r=10, t=50, b=10),
    height=480,
)
st.plotly_chart(fig_sankey, use_container_width=True)

st.markdown("---")
col_l, col_r = st.columns(2)

with col_l:
    st.markdown('<div class="section-header">CIS BANKING GROWTH — REMITTANCE INFLOWS</div>', unsafe_allow_html=True)
    df_remit = pd.DataFrame({
        "Country": ["Kyrgyzstan", "Kyrgyzstan", "Armenia", "Armenia"],
        "Period": ["Pre-Sanctions (2021)", "Peak 2025-2026", "Pre-Sanctions (2021)", "Peak 2025-2026"],
        "Value_USD_B": [1.17, 3.25, 0.18, 1.01],
        "Metric": ["Money Inflows from Russia", "Money Inflows from Russia", "Banking Sector Profit", "Banking Sector Profit"],
    })
    colors_map = {"Pre-Sanctions (2021)": "#484F58", "Peak 2025-2026": "#C41E3A"}
    fig_bar = go.Figure()
    for period, color in colors_map.items():
        subset = df_remit[df_remit["Period"] == period]
        fig_bar.add_trace(go.Bar(
            name=period,
            x=subset["Country"] + " — " + subset["Metric"],
            y=subset["Value_USD_B"],
            marker_color=color,
            text=[f"${v}B" for v in subset["Value_USD_B"]],
            textposition="outside",
            textfont=dict(color="#E6EDF3", size=10),
        ))
    fig_bar.update_layout(
        plot_bgcolor="#0D1117", paper_bgcolor="#161B22",
        font=dict(color="#E6EDF3"), barmode="group",
        yaxis=dict(showgrid=True, gridcolor="#21262D", tickprefix="$", ticksuffix="B", color="#8B949E"),
        xaxis=dict(color="#8B949E", tickfont=dict(size=9)),
        legend=dict(font=dict(color="#8B949E", size=10), bgcolor="#161B22", bordercolor="#30363D"),
        margin=dict(l=10, r=10, t=10, b=10), height=300,
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with col_r:
    st.markdown('<div class="section-header">CAPITAL TRANSMISSION ARCHITECTURE — STAGE FLOW</div>', unsafe_allow_html=True)
    stages = [
        ("#C41E3A", "STAGE 1A — Bakai Bank (Kyrgyzstan)", "Retail access & foreign account onboarding. RUB deposits swapped into FX via local agents. Provides working Visa cards loaded with rubles for international e-commerce and travel."),
        ("#3FB950", "STAGE 1B — Evocabank (Armenia)", "Digital wealth parking & retail settlement. Cross-border retail payment clearing. Consumers park savings and make international payments with compliance coverage."),
        ("#1F6FEB", "STAGE 1C — VTB Belarus (BLR VTB)", "High-volume untraceable ruble transfers under unified economic agreements. Direct currency bridge invisible to Western financial tracking networks."),
        ("#D29922", "STAGE 2 — CIS Correspondent Layer", "Consolidation of intermediary financial flows. Integrated with smaller regional Chinese financial cards and banks for corporate-level capital aggregation."),
        ("#8B949E", "STAGE 3 — RUB-CNY Clearing Matrix", "Direct ruble-to-yuan clearing. Removes Western intermediary dependency. Closed-loop settlement bypassing all Western clearinghouses."),
    ]
    for color, title, desc in stages:
        st.markdown(f"""<div style="background:#161B22; border:1px solid #30363D; border-left:3px solid {color};
             border-radius:6px; padding:12px 14px; margin-bottom:8px;">
            <div style="color:{color}; font-size:0.68rem; font-weight:700; letter-spacing:0.08em;">{title}</div>
            <div style="color:#8B949E; font-size:0.78rem; line-height:1.5; margin-top:4px;">{desc}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("---")
st.markdown('<div class="section-header">UNRECOGNIZED TERRITORY BANKING NETWORK</div>', unsafe_allow_html=True)
ter_cols = st.columns(3)
territories = [
    ("South Ossetia", "#8B949E", "MRB Bank / TSMRBank",
     "Operates without BIS oversight. SPFS messaging rails route funds without digital footprint. U.S. Treasury confirmed secret correspondent account with North Korea's Foreign Trade Bank. Assets remain 100% offshore, outside Western tracking."),
    ("Abkhazia", "#8B949E", "Local Commercial Banks",
     "Physical banknotes finance limited trade completely hidden from Western monitors. Foreign exchange cash stored in secret accounts. Funds fuel imports from foreign countries. Confirmed zero-risk operation despite U.S. blacklisting."),
    ("Transnistria", "#8B949E", "Shell Company Accounts",
     "Breakaway region (legally part of Moldova) hosts shell companies that resemble European nodes on customs papers and bank wire forms. Compliance systems clear funds without red flags. European machinery and microchips transported into Russia via unguarded borders."),
]
for col, (name, color, bank, desc) in zip(ter_cols, territories):
    with col:
        st.markdown(f"""<div style="background:#161B22; border:1px solid #30363D; border-top:3px solid {color};
             border-radius:8px; padding:16px;">
            <div style="color:#484F58; font-size:0.65rem; font-weight:700; letter-spacing:0.1em; margin-bottom:4px;">JURISDICTIONAL BLACK BOX</div>
            <div style="color:#E6EDF3; font-size:0.95rem; font-weight:700; margin-bottom:4px;">🏴 {name}</div>
            <div style="color:#D29922; font-size:0.78rem; margin-bottom:10px;">{bank}</div>
            <div style="color:#8B949E; font-size:0.78rem; line-height:1.55;">{desc}</div>
        </div>""", unsafe_allow_html=True)

st.markdown('<div style="text-align:center; color:#484F58; font-size:0.75rem; padding:20px 0 4px 0; border-top:1px solid #21262D; margin-top:32px;">Double-Headed Growth Intelligence Platform · Module 03 · CIS Banking Intelligence</div>', unsafe_allow_html=True)
