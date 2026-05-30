import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Eurasian Financial Order | Intelligence Platform", page_icon="🌐", layout="wide")

st.markdown("""
<style>
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0D1117 0%, #161B22 100%); border-right: 1px solid #30363D; }
    .section-header { color:#8B949E; font-size:0.7rem; letter-spacing:0.18em; text-transform:uppercase; border-bottom:1px solid #30363D; padding-bottom:6px; margin-bottom:16px; }
    .kpi-card { background:#161B22; border:1px solid #30363D; border-top:3px solid #C41E3A; border-radius:8px; padding:20px 16px; text-align:center; }
    .kpi-value { font-size:1.5rem; font-weight:800; color:#E6EDF3; }
    .kpi-label { font-size:0.72rem; color:#8B949E; letter-spacing:0.08em; text-transform:uppercase; margin-top:6px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<span style="color:#C41E3A;font-size:0.7rem;letter-spacing:0.15em;font-weight:700;">MODULE 09</span>', unsafe_allow_html=True)
st.markdown('<h1 style="color:#E6EDF3; font-size:1.6rem; font-weight:800; margin:0;">🌐 The New Eurasian Financial Order</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#8B949E; font-size:0.9rem; margin:4px 0 24px 0;">Strategic Intelligence · Alternative Financial Architecture · De-Dollarization · Multipolar Monetary System</p>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
kpis = [
    ("SPFS", "Russian Alternative to SWIFT", "#C41E3A"),
    ("CNY", "Primary Reserve Currency Alternative", "#D29922"),
    ("6 Nodes", "Alternative Financial Corridors", "#1F6FEB"),
    ("Irreversible", "Financial Fragmentation Assessment", "#C41E3A"),
]
for col, (val, label, color) in zip([c1, c2, c3, c4], kpis):
    with col:
        st.markdown(f"""<div class="kpi-card" style="border-top-color:{color}">
            <div class="kpi-value" style="font-size:1.2rem;">{val}</div>
            <div class="kpi-label">{label}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col_geo, col_analysis = st.columns([3, 2])

with col_geo:
    st.markdown('<div class="section-header">EURASIAN ALTERNATIVE FINANCIAL ARCHITECTURE — GEOPOLITICAL MAP</div>', unsafe_allow_html=True)

    key_nodes = {
        "Russia": (55.75, 37.62, "#C41E3A", 20, "Hub of alternative Eurasian financial order. SPFS messaging system. State capital rationing."),
        "China": (39.9, 116.4, "#1F6FEB", 18, "CNY clearing provider. Luxury goods conduit. Technology supply. Strategic partner."),
        "India": (28.6, 77.2, "#1F6FEB", 14, "Energy import hub. Crude oil buyer. Refining intermediary for EU re-export."),
        "Turkey": (41.0, 28.9, "#D29922", 14, "Energy transit and refining hub. NATO member bypassing sanctions. TurkStream gas corridor."),
        "Kazakhstan": (51.2, 71.5, "#3FB950", 12, "Eurasian Economic Union transit hub. Land border corridor for goods."),
        "Kyrgyzstan": (42.87, 74.59, "#3FB950", 12, "CIS card gateway. Crypto hub. EAEU member."),
        "Armenia": (40.18, 44.51, "#3FB950", 10, "Evocabank retail clearing. Banking sector boom."),
        "Belarus": (53.9, 27.57, "#3FB950", 10, "VTB sovereign bridge. Druzhba pipeline partner."),
        "UAE (Dubai)": (25.2, 55.3, "#8B949E", 10, "VPN infrastructure hub. Trade facilitation. Gold market access."),
        "Serbia": (44.8, 20.5, "#D29922", 9, "TurkStream gas receiver. Non-EU energy partner."),
        "Hungary": (47.5, 19.0, "#D29922", 9, "93% Russian oil dependency. Druzhba pipeline exception."),
    }

    corridors = [
        ("Russia", "China", "#1F6FEB", 4, "CNY Direct Clearing"),
        ("Russia", "Turkey", "#D29922", 3, "TurkStream + Energy Transit"),
        ("Russia", "India", "#1F6FEB", 3, "Crude Oil Supply"),
        ("Russia", "Kazakhstan", "#3FB950", 3, "EAEU Corridor"),
        ("Russia", "Belarus", "#3FB950", 3, "Union State Integration"),
        ("Russia", "Kyrgyzstan", "#3FB950", 2, "Card Tourism + Crypto"),
        ("Russia", "Armenia", "#3FB950", 2, "Evocabank Pipeline"),
        ("China", "Kyrgyzstan", "#3FB950", 2, "Regional Bank Integration"),
        ("Turkey", "Serbia", "#D29922", 2, "TurkStream Extension"),
        ("Russia", "UAE (Dubai)", "#8B949E", 2, "Gold/VPN Infrastructure"),
    ]

    fig_geo = go.Figure()
    for src, tgt, color, width, label in corridors:
        lat0, lon0 = key_nodes[src][:2]
        lat1, lon1 = key_nodes[tgt][:2]
        fig_geo.add_trace(go.Scattergeo(
            lat=[lat0, lat1], lon=[lon0, lon1],
            mode="lines",
            line=dict(width=width, color=color),
            hoverinfo="text", text=label,
            showlegend=False,
        ))

    for name, (lat, lon, color, size, tooltip) in key_nodes.items():
        fig_geo.add_trace(go.Scattergeo(
            lat=[lat], lon=[lon],
            mode="markers+text",
            marker=dict(size=size, color=color, line=dict(width=1.5, color="#E6EDF3")),
            text=[name.split(" (")[0]],
            textposition="top right",
            textfont=dict(color="#E6EDF3", size=9),
            hovertemplate=f"<b>{name}</b><br>{tooltip}<extra></extra>",
            showlegend=False,
        ))

    fig_geo.update_layout(
        geo=dict(
            showland=True, landcolor="#161B22",
            showocean=True, oceancolor="#0D1117",
            showcoastlines=True, coastlinecolor="#30363D",
            showcountries=True, countrycolor="#21262D",
            showframe=False,
            projection_type="natural earth",
            bgcolor="#0D1117",
            center=dict(lat=40, lon=60),
            projection_scale=2.5,
            showlakes=False,
        ),
        paper_bgcolor="#161B22",
        font=dict(color="#E6EDF3"),
        margin=dict(l=0, r=0, t=10, b=0),
        height=480,
    )
    st.plotly_chart(fig_geo, use_container_width=True)

with col_analysis:
    st.markdown('<div class="section-header">ALTERNATIVE FINANCIAL CORRIDORS</div>', unsafe_allow_html=True)
    corridors_info = [
        ("#1F6FEB", "🇨🇳 Russia–China CNY Axis", "Direct ruble-to-yuan clearing eliminates USD/SWIFT dependency. Thousands of Chinese intermediaries enable luxury goods, technology, and industrial supply chains outside Western compliance."),
        ("#D29922", "🇹🇷 Russia–Turkey Energy Bridge", "TurkStream pipeline + Tupras refinery creates 'refining laundering' loop. Turkey remains NATO member, creating unprecedented sanctions complexity for Western enforcement."),
        ("#3FB950", "🇰🇬 CIS Card Pipeline Network", "Kyrgyzstan, Armenia, Belarus form a three-node retail banking gateway. Ordinary Russian citizens maintain full international purchasing capability via these nodes."),
        ("#8B949E", "🏴 Unrecognized Territory Network", "South Ossetia + Abkhazia + Transnistria operate as zero-risk financial cut-outs. Outside BIS jurisdiction, invisible to Western compliance, enabling high-risk capital flows."),
        ("#C41E3A", "⛏️ Digital Asset Corridor", "Siberian crypto mining + Kyrgyzstan hub ($31B volume) creates a fully autonomous liquidity generation engine outside the dollar system."),
        ("#3FB950", "🇦🇪 UAE Infrastructure Hub", "Dubai provides VPN infrastructure, gold market access, and neutral trade facilitation — enabling luxury goods and financial flows while maintaining Western diplomatic relationships."),
    ]
    for color, title, desc in corridors_info:
        st.markdown(f"""<div style="background:#161B22; border:1px solid #30363D; border-left:3px solid {color};
             border-radius:6px; padding:11px 13px; margin-bottom:8px;">
            <div style="color:{color}; font-size:0.7rem; font-weight:700; margin-bottom:3px;">{title}</div>
            <div style="color:#8B949E; font-size:0.76rem; line-height:1.5;">{desc}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("---")
st.markdown('<div class="section-header">THE RUBLE DEVALUATION CUSHION — FISCAL STABILIZER MODEL</div>', unsafe_allow_html=True)
col_rub1, col_rub2 = st.columns(2)

with col_rub1:
    st.markdown("""
    <div style="background:#161B22; border:1px solid #30363D; border-radius:8px; padding:20px; line-height:1.8; color:#C9D1D9; font-size:0.85rem;">
    <div style="color:#E6EDF3; font-weight:700; margin-bottom:12px;">The Ruble Devaluation Arbitrage Model</div>
    Russia's fiscal architecture exploits a <strong style="color:#D29922;">currency conversion arbitrage</strong>:
    <br><br>
    <strong style="color:#1F6FEB;">Revenue Collection:</strong> Energy export taxes collected in CNY/USD (foreign reserve currencies)<br>
    <strong style="color:#C41E3A;">Expenditure:</strong> All government spending — defense, wages, procurement — paid in RUB<br><br>
    <strong style="color:#3FB950;">The Mechanism:</strong> If foreign currency inflows drop, the Central Bank allows the ruble to
    depreciate. Domestic budget value in rubles increases even as foreign asset value decreases.
    <br><br>
    <strong style="color:#D29922;">The Cost:</strong> Devaluation bonus is a transfer of purchasing power from the civilian population
    to the state — manifesting as structural inflation (currently 5.2% CPI).
    </div>
    """, unsafe_allow_html=True)

with col_rub2:
    years_rub = [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
    rub_rate = [70, 90, 88, 92, 88, 82, 78, 75, 72]
    purchasing_power = [100, 88, 84, 82, 80, 83, 85, 87, 89]
    fig_rub = go.Figure()
    fig_rub.add_trace(go.Scatter(x=years_rub, y=rub_rate, mode="lines+markers",
                                  name="USD/RUB Exchange Rate",
                                  line=dict(color="#C41E3A", width=2.5),
                                  marker=dict(size=7)))
    fig_rub.add_trace(go.Scatter(x=years_rub, y=purchasing_power, mode="lines+markers",
                                  name="Civilian Purchasing Power Index (2022=100)",
                                  line=dict(color="#1F6FEB", width=2.5, dash="dot"),
                                  marker=dict(size=7), yaxis="y2"))
    fig_rub.update_layout(
        plot_bgcolor="#0D1117", paper_bgcolor="#161B22",
        font=dict(color="#E6EDF3"),
        yaxis=dict(color="#C41E3A", showgrid=True, gridcolor="#21262D", title="RUB per USD"),
        yaxis2=dict(overlaying="y", side="right", color="#1F6FEB",
                    title="Purchasing Power Index", showgrid=False),
        xaxis=dict(color="#8B949E", showgrid=False),
        legend=dict(font=dict(color="#8B949E", size=9), bgcolor="#161B22"),
        margin=dict(l=10, r=10, t=10, b=10), height=300,
    )
    st.plotly_chart(fig_rub, use_container_width=True)

st.markdown('<div style="text-align:center; color:#484F58; font-size:0.75rem; padding:20px 0 4px 0; border-top:1px solid #21262D; margin-top:32px;">Double-Headed Growth Intelligence Platform · Module 09 · Eurasian Financial Order</div>', unsafe_allow_html=True)
