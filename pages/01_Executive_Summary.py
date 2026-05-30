import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

st.set_page_config(page_title="Executive Summary | Intelligence Platform", page_icon="📋", layout="wide")

st.markdown("""
<style>
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0D1117 0%, #161B22 100%); border-right: 1px solid #30363D; }
    .kpi-card { background:#161B22; border:1px solid #30363D; border-top:3px solid #C41E3A; border-radius:8px; padding:20px 16px; text-align:center; }
    .kpi-card:hover { border-top-color:#1F6FEB; }
    .kpi-value { font-size:1.9rem; font-weight:800; color:#E6EDF3; }
    .kpi-label { font-size:0.72rem; color:#8B949E; letter-spacing:0.08em; text-transform:uppercase; margin-top:6px; }
    .kpi-delta-up { color:#3FB950; font-size:0.78rem; }
    .kpi-delta-down { color:#C41E3A; font-size:0.78rem; }
    .section-header { color:#8B949E; font-size:0.7rem; letter-spacing:0.18em; text-transform:uppercase; border-bottom:1px solid #30363D; padding-bottom:6px; margin-bottom:16px; }
    .intel-card { background:#161B22; border:1px solid #30363D; border-left:3px solid #1F6FEB; border-radius:6px; padding:16px 18px; margin-bottom:10px; }
    .intel-card.red { border-left-color:#C41E3A; }
    .intel-card.green { border-left-color:#3FB950; }
    .page-title { color:#E6EDF3; font-size:1.6rem; font-weight:800; margin:0; }
    .page-subtitle { color:#8B949E; font-size:0.9rem; margin:4px 0 24px 0; }
</style>
""", unsafe_allow_html=True)

st.markdown('<span style="color:#C41E3A;font-size:0.7rem;letter-spacing:0.15em;font-weight:700;">MODULE 01</span>', unsafe_allow_html=True)
st.markdown('<div class="page-title">📋 Executive Summary</div>', unsafe_allow_html=True)
st.markdown('<div class="page-subtitle">Research Overview · Key Findings · Strategic Context · Intelligence Briefing</div>', unsafe_allow_html=True)

c1, c2, c3, c4, c5, c6 = st.columns(6)
kpis = [
    ("1,500+", "Shadow Fleet Vessels", "▲ 9× growth since 2022", "down"),
    ("$3.5B", "CIS Remittance Peak", "Kyrgyzstan from Russia", "up"),
    ("€231B", "EU Energy Spend on Russia", "Despite official ban", "down"),
    ("€567M", "Feb 2026 Refinery Exports", "Single month laundering", "down"),
    ("$1.01B", "Armenia Banking Profit", "From $180M pre-sanctions", "up"),
    ("$31B", "Kyrgyzstan Crypto Volume", "Exceeds nominal GDP", "down"),
]
for col, (val, label, delta, direction) in zip([c1,c2,c3,c4,c5,c6], kpis):
    delta_class = "kpi-delta-up" if direction == "up" else "kpi-delta-down"
    with col:
        st.markdown(f"""<div class="kpi-card">
            <div class="kpi-value">{val}</div>
            <div class="kpi-label">{label}</div>
            <div class="{delta_class}">{delta}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col_left, col_right = st.columns([3, 2])

with col_left:
    st.markdown('<div class="section-header">ABSTRACT — RESEARCH OVERVIEW</div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="background:#161B22; border:1px solid #30363D; border-radius:8px; padding:20px; line-height:1.8; color:#C9D1D9; font-size:0.88rem;">
    Banning Russia's access to SWIFT banking and luxury goods, Western countries hoped the Russian economy
    would crumble. By 2026, Russia has survived by using various strategies — a model termed
    <strong style="color:#E6EDF3;">"Double-Headed Growth."</strong>
    <br><br>
    This study identifies main structural vulnerabilities in Eurasia through which Russia circumvents the
    global blockade. The research documents how <strong style="color:#E6EDF3;">capital and liquidity behave like water</strong>
    — when primary channels are blocked, money finds alternative pathways.
    <br><br>
    The two heads of Russia's dual economy are:<br>
    <strong style="color:#1F6FEB;">HEAD 1:</strong> Internal capital rationing via state-directed ruble injections into domestic industry.<br>
    <strong style="color:#C41E3A;">HEAD 2:</strong> An adaptive grey economy with cross-border Eurasian financial pipelines.
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="section-header">THE DOUBLE-HEADED GROWTH MODEL</div>', unsafe_allow_html=True)

    fig = go.Figure()
    heads = ["State Head\n(Domestic)", "Grey Economy Head\n(International)"]
    values = [55, 45]
    colors = ["#1F6FEB", "#C41E3A"]
    fig.add_trace(go.Bar(
        x=heads, y=values,
        marker_color=colors,
        text=[f"{v}% Economic Weight" for v in values],
        textposition="outside",
        textfont=dict(color="#E6EDF3", size=11),
    ))
    fig.update_layout(
        plot_bgcolor="#0D1117", paper_bgcolor="#161B22",
        font=dict(color="#E6EDF3", family="sans-serif"),
        title=dict(text="Economic Weight Split: Domestic vs Grey Economy", font=dict(size=13, color="#E6EDF3"), x=0),
        yaxis=dict(showgrid=True, gridcolor="#21262D", ticksuffix="%", color="#8B949E"),
        xaxis=dict(color="#8B949E"),
        showlegend=False,
        margin=dict(l=10, r=10, t=50, b=10),
        height=280,
    )
    st.plotly_chart(fig, use_container_width=True)

with col_right:
    st.markdown('<div class="section-header">MAIN FINDINGS</div>', unsafe_allow_html=True)
    findings_list = [
        ("🏦", "CIS Card Tourism", "red", "Russian citizens maintain international purchasing power via Bakai Bank, Evocabank, and VTB Belarus — bypassing international card bans entirely."),
        ("🏴‍☠️", "Shadow Fleet", "red", "1,500+ vessels under flags of convenience ship crude oil outside G7 price cap enforcement. Fleet grew 9× since 2022."),
        ("🔐", "Unrecognized Territories", "red", "South Ossetia, Abkhazia & Transnistria act as zero-risk financial cut-outs with zero BIS oversight — funds flow invisibly."),
        ("🚗", "Luxury Re-Routing", "red", "G-Wagons, Porsches, BMWs re-enter Russia via Chinese middlemen who reclassify new vehicles as 'pre-owned' at border zones."),
        ("⛏️", "Crypto Mining", "red", "State-backed Siberian crypto mining converts cheap energy into alternative liquidity — funded with foreign cryptocurrency purchases."),
        ("📈", "Ruble Resilience", "green", "Despite sanctions, the ruble stabilized via capital controls. Central Bank now targets 8–10% rate by 2027 toward sustainable recovery."),
    ]
    for icon, title, card_type, desc in findings_list:
        st.markdown(f"""<div class="intel-card {card_type}">
            <h4 style="color:#E6EDF3; font-size:0.88rem; margin:0 0 5px 0;">{icon} {title}</h4>
            <p style="color:#8B949E; font-size:0.8rem; margin:0; line-height:1.5;">{desc}</p>
        </div>""", unsafe_allow_html=True)

st.markdown("---")
st.markdown('<div class="section-header">KEY CONCLUSIONS</div>', unsafe_allow_html=True)
conc_cols = st.columns(3)
conclusions = [
    ("🌐", "Financial Containment Fails", "#1F6FEB",
     "Traditional financial models assumed SWIFT bans would cause immediate collapse. Empirical data to 2026 proves this is impossible for a major economic power with vast resources and borders."),
    ("⚖️", "Sanctions Paradox", "#D29922",
     "Sanctions forced Russia to overhaul its economic architecture. Rather than depression, they triggered 'militarised Keynesianism' — a domestic industrial boom at full capacity with record wages."),
    ("🔄", "New Eurasian Order", "#C41E3A",
     "Russia created a parallel financial world via South Ossetia, CIS pipelines, and direct CNY clearing. This alternative system is stable and demonstrates a model for any sanctioned great power."),
]
for col, (icon, title, color, text) in zip(conc_cols, conclusions):
    with col:
        st.markdown(f"""
        <div style="background:#161B22; border:1px solid #30363D; border-top:3px solid {color};
             border-radius:8px; padding:20px; height:180px;">
            <div style="font-size:1.5rem; margin-bottom:10px;">{icon}</div>
            <div style="color:#E6EDF3; font-weight:700; font-size:0.9rem; margin-bottom:8px;">{title}</div>
            <div style="color:#8B949E; font-size:0.8rem; line-height:1.6;">{text}</div>
        </div>""", unsafe_allow_html=True)

st.markdown('<div style="text-align:center; color:#484F58; font-size:0.75rem; padding:20px 0 4px 0; border-top:1px solid #21262D; margin-top:32px;">Double-Headed Growth Intelligence Platform · Makhzumul Islam Mahdi · 2026</div>', unsafe_allow_html=True)
