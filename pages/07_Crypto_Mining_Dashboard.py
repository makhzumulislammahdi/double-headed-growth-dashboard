import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(page_title="Crypto Mining Dashboard | Intelligence Platform", page_icon="⛏️", layout="wide")

st.markdown("""
<style>
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0D1117 0%, #161B22 100%); border-right: 1px solid #30363D; }
    .section-header { color:#8B949E; font-size:0.7rem; letter-spacing:0.18em; text-transform:uppercase; border-bottom:1px solid #30363D; padding-bottom:6px; margin-bottom:16px; }
    .kpi-card { background:#161B22; border:1px solid #30363D; border-top:3px solid #C41E3A; border-radius:8px; padding:20px 16px; text-align:center; }
    .kpi-value { font-size:1.7rem; font-weight:800; color:#E6EDF3; }
    .kpi-label { font-size:0.72rem; color:#8B949E; letter-spacing:0.08em; text-transform:uppercase; margin-top:6px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<span style="color:#C41E3A;font-size:0.7rem;letter-spacing:0.15em;font-weight:700;">MODULE 07</span>', unsafe_allow_html=True)
st.markdown('<h1 style="color:#E6EDF3; font-size:1.6rem; font-weight:800; margin:0;">⛏️ Crypto Mining & Alternative Liquidity</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#8B949E; font-size:0.9rem; margin:4px 0 24px 0;">Siberian Mining Operations · Digital Asset Infrastructure · Alternative Liquidity Generation · State-Backed Crypto Networks</p>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
kpis = [
    ("$31B", "Kyrgyzstan Crypto Volume", "#D29922"),
    ("#2 Global", "Russia Mining Power Rank", "#C41E3A"),
    ("-40°C", "Siberian Winter Advantage", "#1F6FEB"),
    ("~12¢", "Russia Energy Cost/kWh", "#3FB950"),
]
for col, (val, label, color) in zip([c1, c2, c3, c4], kpis):
    with col:
        st.markdown(f"""<div class="kpi-card" style="border-top-color:{color}">
            <div class="kpi-value" style="font-size:1.5rem;">{val}</div>
            <div class="kpi-label">{label}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col_net, col_model = st.columns([2, 3])

with col_net:
    st.markdown('<div class="section-header">SIBERIAN CRYPTO ECOSYSTEM — OPERATION NODES</div>', unsafe_allow_html=True)
    nodes_crypto = {
        "Siberian Mining\nFarms": (0, 0, "#C41E3A", 35),
        "Cheap State\nEnergy": (-1.5, 1.2, "#1F6FEB", 24),
        "Sub-Zero\nTemperature": (-1.5, -1.2, "#1F6FEB", 20),
        "Bitcoin /\nCrypto": (1.8, 0.6, "#D29922", 28),
        "Foreign Currency\nPurchase": (1.8, -0.6, "#D29922", 22),
        "Kyrgyzstan\nCrypto Hub": (3.2, 0, "#3FB950", 24),
        "Alternative\nLiquidity Pool": (0, -2.2, "#3FB950", 22),
        "Chinese\nExchange Nodes": (3.2, -1.5, "#8B949E", 18),
    }
    edges_crypto = [
        ("Cheap State\nEnergy", "Siberian Mining\nFarms"),
        ("Sub-Zero\nTemperature", "Siberian Mining\nFarms"),
        ("Siberian Mining\nFarms", "Bitcoin /\nCrypto"),
        ("Siberian Mining\nFarms", "Foreign Currency\nPurchase"),
        ("Bitcoin /\nCrypto", "Kyrgyzstan\nCrypto Hub"),
        ("Foreign Currency\nPurchase", "Alternative\nLiquidity Pool"),
        ("Kyrgyzstan\nCrypto Hub", "Alternative\nLiquidity Pool"),
        ("Kyrgyzstan\nCrypto Hub", "Chinese\nExchange Nodes"),
        ("Alternative\nLiquidity Pool", "Chinese\nExchange Nodes"),
    ]
    fig_net = go.Figure()
    for src, tgt in edges_crypto:
        x0, y0 = nodes_crypto[src][:2]
        x1, y1 = nodes_crypto[tgt][:2]
        fig_net.add_trace(go.Scatter(
            x=[x0, x1, None], y=[y0, y1, None],
            mode="lines", line=dict(width=1.5, color="rgba(196,30,58,0.4)"),
            hoverinfo="skip", showlegend=False,
        ))
    for name, (x, y, color, size) in nodes_crypto.items():
        fig_net.add_trace(go.Scatter(
            x=[x], y=[y], mode="markers+text",
            marker=dict(size=size, color=color, line=dict(width=1.5, color="#E6EDF3")),
            text=[name], textposition="top center",
            textfont=dict(color="#E6EDF3", size=9),
            hovertemplate=f"<b>{name.replace(chr(10), ' ')}</b><extra></extra>",
            showlegend=False,
        ))
    fig_net.update_layout(
        plot_bgcolor="#0D1117", paper_bgcolor="#161B22",
        font=dict(color="#E6EDF3"),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-2.5, 4.5]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-3.2, 2.5]),
        margin=dict(l=10, r=10, t=10, b=10), height=400,
    )
    st.plotly_chart(fig_net, use_container_width=True)

with col_model:
    st.markdown('<div class="section-header">CRYPTO LIQUIDITY GENERATION MODEL — 2022–2026</div>', unsafe_allow_html=True)
    months_c = ["Q1'22","Q2'22","Q3'22","Q4'22","Q1'23","Q2'23","Q3'23","Q4'23",
                "Q1'24","Q2'24","Q3'24","Q4'24","Q1'25","Q2'25","Q3'25","Q4'25","Q1'26"]
    mining_power = [2.0, 3.2, 5.1, 7.8, 10.2, 12.5, 14.8, 16.2,
                    17.5, 18.8, 19.4, 20.1, 21.3, 22.0, 22.8, 23.5, 24.1]
    kyrgyz_vol = [0.5, 0.8, 1.2, 2.1, 3.5, 5.2, 8.4, 11.2,
                  14.8, 17.5, 20.1, 22.8, 25.2, 27.4, 29.1, 30.5, 31.0]
    fig_crypto = go.Figure()
    fig_crypto.add_trace(go.Scatter(x=months_c, y=mining_power, mode="lines",
                                     name="Siberian Mining Power (EH/s proxy)",
                                     line=dict(color="#C41E3A", width=2.5),
                                     fill="tozeroy", fillcolor="rgba(196,30,58,0.08)"))
    fig_crypto.add_trace(go.Scatter(x=months_c, y=kyrgyz_vol, mode="lines",
                                     name="Kyrgyzstan Crypto Volume ($B)",
                                     line=dict(color="#D29922", width=2.5),
                                     yaxis="y2"))
    fig_crypto.update_layout(
        plot_bgcolor="#0D1117", paper_bgcolor="#161B22",
        font=dict(color="#E6EDF3"),
        yaxis=dict(color="#C41E3A", showgrid=True, gridcolor="#21262D", title="Mining Power Index"),
        yaxis2=dict(overlaying="y", side="right", color="#D29922",
                    title="Volume ($B)", showgrid=False),
        xaxis=dict(color="#8B949E", showgrid=False, tickfont=dict(size=9)),
        legend=dict(font=dict(color="#8B949E", size=10), bgcolor="#161B22", bordercolor="#30363D"),
        margin=dict(l=10, r=10, t=10, b=10), height=240,
    )
    st.plotly_chart(fig_crypto, use_container_width=True)

    st.markdown('<div class="section-header">ENERGY COST ADVANTAGE — GLOBAL COMPARISON</div>', unsafe_allow_html=True)
    countries_e = ["Germany", "UK", "USA", "China", "Kazakhstan", "Russia (Siberia)"]
    cost_kwh = [0.38, 0.32, 0.17, 0.08, 0.05, 0.03]
    colors_e = ["#484F58","#484F58","#484F58","#8B949E","#D29922","#C41E3A"]
    fig_energy = go.Figure(go.Bar(
        x=countries_e, y=cost_kwh,
        marker_color=colors_e,
        text=[f"${v:.2f}/kWh" for v in cost_kwh],
        textposition="outside", textfont=dict(color="#E6EDF3", size=9),
        hovertemplate="<b>%{x}</b><br>$%{y:.2f}/kWh<extra></extra>",
    ))
    fig_energy.update_layout(
        plot_bgcolor="#0D1117", paper_bgcolor="#161B22",
        font=dict(color="#E6EDF3"),
        yaxis=dict(color="#8B949E", showgrid=True, gridcolor="#21262D",
                   tickprefix="$", ticksuffix="/kWh"),
        xaxis=dict(color="#8B949E"),
        margin=dict(l=10, r=10, t=10, b=10), height=200,
        showlegend=False,
    )
    st.plotly_chart(fig_energy, use_container_width=True)

st.markdown("---")
st.markdown('<div class="section-header">MECHANISM ANALYSIS — HOW SIBERIAN CRYPTO GENERATES STATE LIQUIDITY</div>', unsafe_allow_html=True)
mech_cols = st.columns(4)
mechanisms = [
    ("❄️", "Temperature Advantage", "#1F6FEB", "Sub-zero Siberian winters provide free cooling for ASIC mining rigs. Cooling represents ~30-40% of global mining overhead costs — eliminated entirely in Siberia. This alone creates an insurmountable cost moat vs. Western competitors."),
    ("⚡", "Cheap Energy", "#D29922", "Russia's state-subsidized energy infrastructure provides electricity at ~$0.03/kWh — 10× cheaper than Germany, 5× cheaper than the US. Mining profitability is structurally guaranteed regardless of Bitcoin price fluctuations."),
    ("🏛️", "State Backing", "#C41E3A", "Operations are financed directly with foreign debt — purchased cryptocurrencies act as collateral. State backing removes private capital risk and enables industrial-scale operations impossible for private actors in sanctioned markets."),
    ("🔄", "Liquidity Loop", "#3FB950", "Mined Bitcoin converts into foreign currency via Kyrgyzstan's crypto hub ($31B volume, exceeds national GDP). This creates a perpetual liquidity generation engine that is entirely outside Western financial monitoring."),
]
for col, (icon, title, color, text) in zip(mech_cols, mechanisms):
    with col:
        st.markdown(f"""<div style="background:#161B22; border:1px solid #30363D; border-top:3px solid {color};
             border-radius:8px; padding:16px; min-height:200px;">
            <div style="font-size:1.3rem; margin-bottom:8px;">{icon}</div>
            <div style="color:#E6EDF3; font-weight:700; font-size:0.88rem; margin-bottom:8px;">{title}</div>
            <div style="color:#8B949E; font-size:0.78rem; line-height:1.6;">{text}</div>
        </div>""", unsafe_allow_html=True)

st.markdown('<div style="text-align:center; color:#484F58; font-size:0.75rem; padding:20px 0 4px 0; border-top:1px solid #21262D; margin-top:32px;">Double-Headed Growth Intelligence Platform · Module 07 · Crypto Mining & Alternative Liquidity</div>', unsafe_allow_html=True)
