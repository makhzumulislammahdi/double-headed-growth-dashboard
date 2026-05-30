import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(page_title="Sanctions Ecosystem | Intelligence Platform", page_icon="🕸️", layout="wide")

st.markdown("""
<style>
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0D1117 0%, #161B22 100%); border-right: 1px solid #30363D; }
    .section-header { color:#8B949E; font-size:0.7rem; letter-spacing:0.18em; text-transform:uppercase; border-bottom:1px solid #30363D; padding-bottom:6px; margin-bottom:16px; }
    .node-card { background:#161B22; border:1px solid #30363D; border-radius:6px; padding:14px; margin-bottom:8px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<span style="color:#C41E3A;font-size:0.7rem;letter-spacing:0.15em;font-weight:700;">MODULE 02</span>', unsafe_allow_html=True)
st.markdown('<h1 style="color:#E6EDF3; font-size:1.6rem; font-weight:800; margin:0;">🕸️ Russia Sanctions Evasion Ecosystem</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#8B949E; font-size:0.9rem; margin:4px 0 24px 0;">Network Intelligence · Node Analysis · Relationship Mapping · Evasion Pathways</p>', unsafe_allow_html=True)

# Network graph data
nodes = {
    "Russia": (0, 0, "#C41E3A", 40, "Central node. Source of sanctioned capital seeking international routes."),
    "China": (2.5, 1.5, "#1F6FEB", 32, "Primary trade partner. Provides CNY clearing, luxury goods conduit, and technology supply chains."),
    "Turkey": (1.5, -2, "#D29922", 28, "Energy transit hub. Tupras refinery launders Russian crude into 'Turkish' fuel for EU re-export."),
    "India": (3, -1, "#1F6FEB", 28, "Major crude buyer. Jamnagar refinery converts Russian oil sold back to Europe at premium prices."),
    "Kyrgyzstan": (-2.5, 1.5, "#3FB950", 24, "CIS gateway. Bakai Bank enables card tourism; crypto volume ($31B) exceeds national GDP."),
    "Armenia": (-2, -1, "#3FB950", 22, "Retail banking node. Evocabank provides cross-border retail payment clearing with strict compliance."),
    "Belarus": (-1, 2.5, "#3FB950", 22, "Sovereign bridge. VTB Belarus enables high-volume untraceable ruble transfers."),
    "South Ossetia": (-3, -0.5, "#8B949E", 18, "Unrecognized territory. SPFS messaging rails provide zero-risk financial cut-out outside BIS oversight."),
    "Abkhazia": (-3.2, 0.8, "#8B949E", 16, "Unrecognized territory. Physical banknotes fund limited trade outside all Western monitors."),
    "Transnistria": (-1.8, -2.5, "#8B949E", 16, "Shell company hub. Simulates European nodes to pass compliance checks, rerouting goods into Russia."),
}

edge_list = [
    ("Russia", "China", 5, "Direct CNY clearing + luxury goods pipeline"),
    ("Russia", "Turkey", 5, "Crude oil transit → refining laundering"),
    ("Russia", "India", 5, "Discounted crude → re-export to EU"),
    ("Russia", "Kyrgyzstan", 4, "Card tourism + crypto mining networks"),
    ("Russia", "Armenia", 4, "Evocabank retail payment clearing"),
    ("Russia", "Belarus", 4, "VTB sovereign ruble bridge"),
    ("Russia", "South Ossetia", 3, "SPFS financial messaging cut-out"),
    ("Russia", "Abkhazia", 3, "Physical cash flows, fuel imports"),
    ("Russia", "Transnistria", 3, "Shell company trade rerouting"),
    ("Turkey", "India", 3, "Refined product coordination"),
    ("China", "Kyrgyzstan", 2, "Regional Chinese bank integration"),
    ("China", "Belarus", 2, "Trade settlement cooperation"),
]

fig = go.Figure()

# Draw edges
for src, tgt, weight, desc in edge_list:
    x0, y0 = nodes[src][:2]
    x1, y1 = nodes[tgt][:2]
    fig.add_trace(go.Scatter(
        x=[x0, x1, None], y=[y0, y1, None],
        mode="lines",
        line=dict(width=weight * 0.8, color="rgba(196,30,58,0.35)"),
        hoverinfo="skip",
        showlegend=False,
    ))

# Draw nodes
for name, (x, y, color, size, tooltip) in nodes.items():
    fig.add_trace(go.Scatter(
        x=[x], y=[y],
        mode="markers+text",
        marker=dict(size=size, color=color, line=dict(width=2, color="#E6EDF3"),
                    symbol="circle"),
        text=[name],
        textposition="top center",
        textfont=dict(color="#E6EDF3", size=11),
        hovertemplate=f"<b>{name}</b><br>{tooltip}<extra></extra>",
        name=name,
        showlegend=False,
    ))

fig.update_layout(
    plot_bgcolor="#0D1117", paper_bgcolor="#161B22",
    font=dict(color="#E6EDF3"),
    title=dict(text="Russia Sanctions Evasion Network — Node Relationship Map", font=dict(size=14, color="#E6EDF3"), x=0),
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-4.5, 4.5]),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-3.5, 3.5]),
    margin=dict(l=10, r=10, t=50, b=10),
    height=520,
)
st.plotly_chart(fig, use_container_width=True)

st.markdown("---")
st.markdown('<div class="section-header">NODE INTELLIGENCE PROFILES</div>', unsafe_allow_html=True)

row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)

node_profiles = [
    ("#1F6FEB", "🇨🇳 China", "PRIMARY TRADE PARTNER", "Provides direct RUB-CNY clearing matrix, eliminating USD dependency. Thousands of Chinese middlemen reclassify European luxury vehicles as 'pre-owned' at border zones. Regional Chinese banks integrate with CIS correspondent accounts to settle high-risk trade."),
    ("#D29922", "🇹🇷 Turkey", "ENERGY TRANSIT HUB", "Tupras refinery processes Russian crude, relabeling it as 'Turkish' diesel and jet fuel. In February 2026 alone, exported €567M in reprocessed Russian energy products to sanctioning EU countries."),
    ("#1F6FEB", "🇮🇳 India", "CRUDE OIL BUYER", "Jamnagar refinery (Reliance Industries) purchases Russian crude at discount, refines it, and sells refined products back to EU nations at premium prices — completing the laundering loop."),
    ("#3FB950", "🇰🇬 Kyrgyzstan", "CIS CARD GATEWAY", "Bakai Bank enables card tourism: Russian citizens open foreign accounts via agents, load rubles, and access international payment systems. Crypto & virtual asset volume reached $31B — exceeding national GDP."),
    ("#3FB950", "🇦🇲 Armenia", "RETAIL BANKING NODE", "Evocabank serves as digital wealth parking and cross-border retail payment clearing. National banking sector profit grew from $180M to $1.01B (AMD 421.3B) driven by Russian capital inflows."),
    ("#3FB950", "🇧🇾 Belarus", "SOVEREIGN RUBLE BRIDGE", "VTB Bank (BLR) operates as a direct currency bridge under unified economic agreements. Enables high-volume untraceable ruble transfers, invisible to Western tracking networks."),
    ("#8B949E", "🏴 South Ossetia", "JURISDICTIONAL BLACK BOX", "TSMRBank/MRB Bank operates outside BIS jurisdiction. No international compliance oversight. SPFS messaging rails route funds without digital footprint on international monitors. Confirmed by U.S. Treasury documents."),
    ("#8B949E", "🏴 Abkhazia", "PHYSICAL CASH CORRIDOR", "Local commercial banks serve as hiding places for foreign exchange cash. Physical banknotes finance limited trade outside all Western monitoring systems. Foreign exchange cash moves in secret accounts."),
    ("#8B949E", "🏴 Transnistria", "SHELL COMPANY HUB", "Breakaway region (legally Moldova) hosts shell companies that resemble European nodes on customs papers and bank wire forms. European machinery, microchips transported into Russia via unguarded borders."),
]

all_rows = [row1, row2, row3]
for i, (cols) in enumerate(all_rows):
    for j, col in enumerate(cols):
        idx = i * 3 + j
        color, name, role, desc = node_profiles[idx]
        with col:
            st.markdown(f"""<div style="background:#161B22; border:1px solid #30363D; border-top:3px solid {color};
                 border-radius:8px; padding:16px; height:200px; overflow:hidden;">
                <div style="color:{color}; font-size:0.65rem; font-weight:700; letter-spacing:0.1em; margin-bottom:4px;">{role}</div>
                <div style="color:#E6EDF3; font-size:0.92rem; font-weight:700; margin-bottom:8px;">{name}</div>
                <div style="color:#8B949E; font-size:0.78rem; line-height:1.55;">{desc}</div>
            </div>""", unsafe_allow_html=True)

st.markdown('<div style="text-align:center; color:#484F58; font-size:0.75rem; padding:20px 0 4px 0; border-top:1px solid #21262D; margin-top:32px;">Double-Headed Growth Intelligence Platform · Module 02 · Sanctions Evasion Ecosystem</div>', unsafe_allow_html=True)
