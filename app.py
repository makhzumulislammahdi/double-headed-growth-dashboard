import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="DOUBLE-HEADED GROWTH | Geopolitical Intelligence Platform",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ══════════════════════════════════════════════════════════════════════
# GLOBAL CSS — Cyberpunk Intelligence Platform
# ══════════════════════════════════════════════════════════════════════
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&family=Inter:wght@300;400;600;700&display=swap');

html { scroll-behavior: smooth; }

/* BASE */
.stApp { background-color: #050B18 !important; font-family: 'Inter', sans-serif; color: #C8D8E8; }
.main .block-container { padding: 0 2rem 4rem 2rem !important; max-width: 100% !important; }

/* CYBER GRID BACKGROUND */
.stApp::before {
    content: '';
    position: fixed; top: 0; left: 0;
    width: 100vw; height: 100vh;
    background-image:
        linear-gradient(rgba(0,212,255,0.022) 1px, transparent 1px),
        linear-gradient(90deg, rgba(0,212,255,0.022) 1px, transparent 1px);
    background-size: 60px 60px;
    pointer-events: none; z-index: 0;
}

/* SIDEBAR */
[data-testid="stSidebar"] { background: #020814 !important; border-right: 1px solid rgba(0,212,255,0.18) !important; }
[data-testid="stSidebarNav"] { display: none !important; }
[data-testid="stSidebar"] .stMarkdown { padding: 0 !important; }
[data-testid="stSidebar"] .stMarkdown p { margin: 0; }

/* HIDE STREAMLIT CHROME */
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }

/* CUSTOM SCROLLBAR */
::-webkit-scrollbar { width: 3px; background: #020814; }
::-webkit-scrollbar-thumb { background: rgba(0,212,255,0.35); border-radius: 2px; }

/* ── NAV SIDEBAR ─────────────────────────────────── */
.nav-brand {
    font-family: 'Orbitron', monospace;
    font-size: 0.82rem; font-weight: 900;
    color: #00D4FF; letter-spacing: 0.06em;
    text-align: center; padding: 24px 16px 6px 16px;
    text-shadow: 0 0 18px rgba(0,212,255,0.7);
}
.nav-sub {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.6rem; color: #FF4444;
    letter-spacing: 0.22em; text-align: center;
    padding-bottom: 16px;
    border-bottom: 1px solid rgba(0,212,255,0.1);
    margin-bottom: 8px;
    animation: blink 3s infinite;
}
@keyframes blink { 0%,100%{opacity:1} 50%{opacity:0.5} }
.nav-link {
    display: block; padding: 9px 14px;
    color: #4A6A80; font-size: 0.75rem;
    font-family: 'Share Tech Mono', monospace;
    text-decoration: none !important;
    border-radius: 4px;
    border: 1px solid transparent;
    letter-spacing: 0.03em;
    transition: all 0.2s;
    margin: 2px 8px;
}
.nav-link:hover {
    color: #00D4FF !important; background: rgba(0,212,255,0.07);
    border-color: rgba(0,212,255,0.18);
    text-decoration: none !important;
    box-shadow: 0 0 12px rgba(0,212,255,0.06);
}
.nav-num { color: #FF4444; margin-right: 8px; font-size: 0.6rem; }
.nav-divider { border-top: 1px solid rgba(0,212,255,0.07); margin: 6px 12px; }
.status-row { display:flex; align-items:center; gap:8px; padding: 4px 16px; margin-bottom:4px; }
.dot { width:6px; height:6px; border-radius:50%; flex-shrink:0; }
.dot-green { background:#00FF90; box-shadow:0 0 6px #00FF90; animation:pulse 2s infinite; }
.dot-amber { background:#FFB800; box-shadow:0 0 6px #FFB800; animation:pulse 2.5s infinite; }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:0.3} }
.status-lbl { font-family:'Share Tech Mono',monospace; font-size:0.62rem; color:#2A4050; }

/* ── HERO ─────────────────────────────────────────── */
.hero {
    background: linear-gradient(160deg, #020B22 0%, #050B18 45%, #020916 80%, #020814 100%);
    border-bottom: 1px solid rgba(0,212,255,0.15);
    padding: 88px 60px 72px 60px;
    text-align: center;
    position: relative; overflow: hidden;
    margin: 0 -2rem 56px -2rem;
}
.hero::before {
    content: '';
    position: absolute; top: 0; left: 0;
    width: 100%; height: 100%;
    background: radial-gradient(ellipse at 50% 50%, rgba(0,212,255,0.055) 0%, transparent 70%);
    pointer-events: none;
}
.hero::after {
    content: '';
    position: absolute; bottom: 0; left: 0; right: 0;
    height: 1px;
    background: linear-gradient(90deg, transparent, #00D4FF, transparent);
}
.hero-badge {
    font-family: 'Share Tech Mono', monospace;
    font-size: 0.6rem; letter-spacing: 0.35em;
    background: rgba(255,45,45,0.1);
    border: 1px solid rgba(255,68,68,0.45);
    color: #FF5555; padding: 4px 16px;
    border-radius: 2px; display: inline-block;
    margin-bottom: 28px; animation: blink 3s infinite;
}
.hero-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(2.4rem, 4.5vw, 4.2rem);
    font-weight: 900;
    color: #FFFFFF;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    line-height: 1.1; margin: 0 0 6px 0;
    text-shadow: 0 0 50px rgba(0,212,255,0.45), 0 0 100px rgba(0,212,255,0.15);
}
.hero-title .accent { color: #00D4FF; }
.hero-line {
    width: 220px; height: 1px;
    background: linear-gradient(90deg, transparent, #00D4FF, transparent);
    margin: 20px auto;
}
.hero-subtitle {
    font-size: 1.0rem; color: #6A8FA8;
    max-width: 680px; margin: 0 auto 10px auto;
    line-height: 1.75; font-style: italic;
}
.hero-author {
    font-family: 'Share Tech Mono', monospace;
    color: #00D4FF; font-size: 0.88rem;
    letter-spacing: 0.1em; margin-top: 6px;
}
.hero-orcid {
    font-family: 'Share Tech Mono', monospace;
    color: #2A5A70; font-size: 0.72rem; margin-top: 4px;
}
.hero-stats-row {
    display: flex; justify-content: center;
    gap: 48px; flex-wrap: wrap;
    margin-top: 44px;
    padding-top: 36px;
    border-top: 1px solid rgba(0,212,255,0.1);
}
.hero-stat { text-align: center; }
.hero-stat-val {
    font-family: 'Orbitron', monospace;
    font-size: 1.55rem; font-weight: 700;
    color: #00D4FF;
    text-shadow: 0 0 18px rgba(0,212,255,0.7);
}
.hero-stat-lbl {
    font-size: 0.65rem; color: #2A4A60;
    letter-spacing: 0.12em; text-transform: uppercase;
    margin-top: 5px;
}

/* ── SECTION ──────────────────────────────────────── */
.section-wrap { margin-bottom: 64px; }
.section-header { margin-bottom: 28px; padding-bottom: 20px; border-bottom: 1px solid rgba(0,212,255,0.1); }
.section-tag {
    font-family: 'Share Tech Mono', monospace;
    color: #00D4FF; font-size: 0.62rem;
    letter-spacing: 0.28em; margin-bottom: 8px;
}
.section-title {
    font-family: 'Orbitron', monospace;
    font-size: clamp(1.2rem, 2.2vw, 1.7rem);
    font-weight: 700; color: #E8F4FF;
    text-transform: uppercase; letter-spacing: 0.04em;
    margin: 0 0 10px 0;
}
.section-summary { color: #4A6A80; font-size: 0.85rem; line-height: 1.75; max-width: 820px; }

/* ── KPI CARDS ────────────────────────────────────── */
.kpi-wrap {
    background: rgba(0,212,255,0.035);
    border: 1px solid rgba(0,212,255,0.15);
    border-radius: 8px; padding: 22px 16px;
    text-align: center; position: relative;
    overflow: hidden; transition: all 0.3s;
}
.kpi-wrap::before {
    content: ''; position: absolute;
    top: 0; left: 0; right: 0; height: 2px;
    background: linear-gradient(90deg, transparent, #00D4FF, transparent);
}
.kpi-wrap:hover {
    border-color: rgba(0,212,255,0.45);
    box-shadow: 0 0 28px rgba(0,212,255,0.09), 0 0 1px rgba(0,212,255,0.4);
    transform: translateY(-2px);
}
.kpi-v {
    font-family: 'Orbitron', monospace;
    font-size: 1.65rem; font-weight: 700;
    color: #00D4FF; line-height: 1.1;
    text-shadow: 0 0 16px rgba(0,212,255,0.65);
}
.kpi-l {
    font-size: 0.63rem; color: #2A4050;
    letter-spacing: 0.14em; text-transform: uppercase;
    margin-top: 6px;
}
.kpi-d { font-size: 0.72rem; margin-top: 5px; }
.kpi-d.up { color: #00FF90; } .kpi-d.dn { color: #FF5555; }
.kpi-wrap.red::before { background: linear-gradient(90deg, transparent, #FF4444, transparent); }
.kpi-wrap.red { border-color: rgba(255,68,68,0.18); }
.kpi-wrap.red .kpi-v { color: #FF6666; text-shadow: 0 0 16px rgba(255,68,68,0.6); }
.kpi-wrap.amber::before { background: linear-gradient(90deg, transparent, #FFB800, transparent); }
.kpi-wrap.amber .kpi-v { color: #FFB800; text-shadow: 0 0 16px rgba(255,184,0,0.6); }
.kpi-wrap.green::before { background: linear-gradient(90deg, transparent, #00FF90, transparent); }
.kpi-wrap.green .kpi-v { color: #00FF90; text-shadow: 0 0 16px rgba(0,255,144,0.6); }

/* ── INTEL CARDS ──────────────────────────────────── */
.ic {
    background: rgba(0,8,20,0.7);
    border: 1px solid rgba(0,212,255,0.1);
    border-left: 3px solid #00D4FF;
    border-radius: 0 6px 6px 0;
    padding: 14px 16px; margin-bottom: 10px;
    transition: all 0.2s;
}
.ic:hover { background: rgba(0,212,255,0.04); border-left-color: #00FFE7; }
.ic.r { border-left-color: #FF4444; }
.ic.r:hover { background: rgba(255,68,68,0.04); border-left-color: #FF6666; }
.ic.g { border-left-color: #00FF90; }
.ic.a { border-left-color: #FFB800; }
.ic h5 { color: #E8F4FF; font-size: 0.83rem; font-weight: 600; margin: 0 0 4px 0; }
.ic p { color: #3A5A70; font-size: 0.76rem; line-height: 1.55; margin: 0; }

/* ── GLASS CARD ───────────────────────────────────── */
.gc {
    background: rgba(0,212,255,0.03);
    border: 1px solid rgba(0,212,255,0.12);
    border-radius: 8px; padding: 20px;
    margin-bottom: 12px; transition: all 0.3s;
}
.gc:hover { border-color: rgba(0,212,255,0.3); box-shadow: 0 0 20px rgba(0,212,255,0.06); }

/* ── SEPARATOR ────────────────────────────────────── */
.sep { display:flex; align-items:center; gap:12px; margin: 56px 0 48px 0; }
.sep-line { flex:1; height:1px; background: rgba(0,212,255,0.09); }
.sep-diamond {
    width:6px; height:6px;
    background: #00D4FF; transform: rotate(45deg);
    box-shadow: 0 0 10px rgba(0,212,255,0.9);
    flex-shrink: 0;
}

/* ── STAGE/FLOW STEPS ─────────────────────────────── */
.flow-step {
    background: rgba(0,10,28,0.8);
    border: 1px solid rgba(0,212,255,0.15);
    border-radius: 6px; padding: 16px 12px;
    text-align: center; height: 100%;
    transition: all 0.2s;
}
.flow-step:hover { border-color: rgba(0,212,255,0.4); box-shadow: 0 0 16px rgba(0,212,255,0.07); }
.flow-arrow { font-size:1.2rem; color: rgba(0,212,255,0.35); display:flex; align-items:center; justify-content:center; height:100%; }

/* ── REF CARD ─────────────────────────────────────── */
.ref-card {
    background: rgba(0,8,20,0.7);
    border: 1px solid rgba(0,212,255,0.1);
    border-left: 3px solid #1A7AFF;
    border-radius: 0 6px 6px 0;
    padding: 12px 16px; margin-bottom: 8px;
}
.ref-num { font-family:'Share Tech Mono',monospace; color:#3A5A70; font-size:0.68rem; }
.ref-title { color: #C8D8E8; font-size:0.82rem; font-weight:600; margin:3px 0; }
.ref-src { color: #2A4050; font-size:0.73rem; }

/* ── FOOTER ───────────────────────────────────────── */
.platform-footer {
    text-align:center; padding: 32px 0 16px 0;
    border-top: 1px solid rgba(0,212,255,0.09);
    margin-top: 48px;
}
.footer-title { font-family:'Orbitron',monospace; color:#00D4FF; font-size:0.85rem; letter-spacing:0.06em; }
.footer-sub { color:#1A3040; font-size:0.72rem; margin-top:8px; font-family:'Share Tech Mono',monospace; }

/* ── DATA TABLE OVERRIDE ──────────────────────────── */
[data-testid="stDataFrame"] { border-radius:8px; overflow:hidden; }
</style>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# CHART THEME HELPER
# ══════════════════════════════════════════════════════════════════════
PAPER = "rgba(5,11,24,0.85)"
PLOT_BG = "rgba(0,0,0,0)"
FC = "#C8D8E8"
GRID = "rgba(0,212,255,0.07)"
CYAN = "#00D4FF"
GREEN = "#00FF90"
RED = "#FF4444"
AMBER = "#FFB800"
BLUE = "#1A7AFF"
GREY = "#2A4050"

def cl(**kw):
    base = dict(
        plot_bgcolor=PLOT_BG, paper_bgcolor=PAPER,
        font=dict(color=FC, family="sans-serif"),
        margin=dict(l=10, r=10, t=45, b=10),
        legend=dict(font=dict(color="#6A8FA8", size=9), bgcolor=PAPER, bordercolor=GRID),
    )
    base.update(kw)
    return base

# ══════════════════════════════════════════════════════════════════════
# SIDEBAR NAVIGATION
# ══════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div class="nav-brand">⚡ DHG PLATFORM</div>
    <div class="nav-sub">▸ UNCLASSIFIED RESEARCH ◂</div>
    """, unsafe_allow_html=True)

    nav_items = [
        ("#hero", "01", "HERO / OVERVIEW"),
        ("#exec", "02", "EXECUTIVE SUMMARY"),
        ("#ecosystem", "03", "SANCTIONS ECOSYSTEM"),
        ("#banking", "04", "BANKING NETWORKS"),
        ("#fleet", "05", "SHADOW FLEET"),
        ("#energy", "06", "ENERGY REVENUE"),
        ("#luxury", "07", "LUXURY RE-ROUTING"),
        ("#crypto", "08", "CRYPTO MINING"),
        ("#macro", "09", "MACROECONOMICS"),
        ("#eurasian", "10", "EURASIAN ORDER"),
        ("#methodology", "11", "METHODOLOGY"),
    ]
    for href, num, label in nav_items:
        st.markdown(f'<a href="{href}" class="nav-link"><span class="nav-num">{num}</span>{label}</a>',
                    unsafe_allow_html=True)

    st.markdown('<div class="nav-divider"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div style="padding:10px 16px 4px 16px;">
        <div class="status-row"><div class="dot dot-green"></div><div class="status-lbl">PLATFORM ACTIVE</div></div>
        <div class="status-row"><div class="dot dot-green"></div><div class="status-lbl">DATA: 2022–2026</div></div>
        <div class="status-row"><div class="dot dot-amber"></div><div class="status-lbl">FORECAST: 2027–2030</div></div>
    </div>
    <div class="nav-divider"></div>
    <div style="padding:10px 16px 20px 16px; font-family:'Share Tech Mono',monospace; font-size:0.58rem; color:#1A3040; line-height:1.8;">
        AUTHOR: M.I. MAHDI<br>
        ORCID: 0009-0007-1769-7771<br>
        YEAR: 2026<br>
        DOMAIN: GEOPOLITICAL FINANCE
    </div>
    """, unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# HERO SECTION
# ══════════════════════════════════════════════════════════════════════
st.markdown('<span id="hero"></span>', unsafe_allow_html=True)
st.markdown("""
<div class="hero">
    <div class="hero-badge">▸ GEOPOLITICAL INTELLIGENCE REPORT — MAKHZUMUL ISLAM MAHDI — 2026 ◂</div>
    <div class="hero-title">DOUBLE-<span class="accent">HEADED</span><br>GROWTH</div>
    <div class="hero-line"></div>
    <div class="hero-subtitle">
        Evaluating Russia's Sanction Evasion Networks, Asymmetric Geopolitical Re-Routing, and Banking Loopholes
    </div>
    <div class="hero-author">MAKHZUMUL ISLAM MAHDI</div>
    <div class="hero-orcid">ORCID: 0009-0007-1769-7771 &nbsp;·&nbsp; WOS: OOO-0072-2025 &nbsp;·&nbsp; FIGSHARE: /authors/Makhzumul_Mahdi/22543814</div>
    <div class="hero-stats-row">
        <div class="hero-stat"><div class="hero-stat-val">1,500+</div><div class="hero-stat-lbl">Shadow Fleet Vessels</div></div>
        <div class="hero-stat"><div class="hero-stat-val">€1.075T</div><div class="hero-stat-lbl">Energy Revenue Since 2022</div></div>
        <div class="hero-stat"><div class="hero-stat-val">9×</div><div class="hero-stat-lbl">Fleet Growth Factor</div></div>
        <div class="hero-stat"><div class="hero-stat-val">$31B</div><div class="hero-stat-lbl">Kyrgyzstan Crypto Volume</div></div>
        <div class="hero-stat"><div class="hero-stat-val">€231B</div><div class="hero-stat-lbl">EU Energy Spend on Russia</div></div>
    </div>
</div>
""", unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# EXECUTIVE SUMMARY
# ══════════════════════════════════════════════════════════════════════
st.markdown('<span id="exec"></span>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <div class="section-tag">▸ MODULE 01 — INTELLIGENCE BRIEFING</div>
    <div class="section-title">Executive Summary</div>
    <div class="section-summary">
        When a large economy is completely blocked from global financial networks, capital behaves like water — it finds new paths.
        This platform documents how Russia's "Double-Headed Growth" model creates two parallel economic engines to sustain state and civilian activity despite comprehensive Western sanctions.
    </div>
</div>
""", unsafe_allow_html=True)

k1, k2, k3, k4, k5, k6 = st.columns(6)
kpi_data = [
    ("1,500+", "Shadow Fleet Vessels", "▲ 9× since 2022", "dn", "red"),
    ("$3.5B", "CIS Remittance Peak", "Kyrgyzstan via Russia", "up", ""),
    ("€231B", "EU Energy Spend", "Despite official ban", "dn", "red"),
    ("0.4%", "GDP Growth 2026", "▼ from 4.9% peak", "dn", "amber"),
    ("5.2%", "CPI Inflation 2026", "▼ from 11.9% shock", "up", ""),
    ("14.5%", "Key Interest Rate", "▼ from 21% peak", "up", "green"),
]
for col, (v, l, d, dclass, card_cls) in zip([k1,k2,k3,k4,k5,k6], kpi_data):
    with col:
        st.markdown(f'<div class="kpi-wrap {card_cls}"><div class="kpi-v">{v}</div><div class="kpi-l">{l}</div><div class="kpi-d {dclass}">{d}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
col_abs, col_find = st.columns([3, 2])

with col_abs:
    st.markdown("""
    <div class="gc">
        <div style="font-family:'Share Tech Mono',monospace; color:#00D4FF; font-size:0.65rem; letter-spacing:0.2em; margin-bottom:14px;">▸ ABSTRACT</div>
        <div style="color:#7A9AB5; font-size:0.87rem; line-height:1.85;">
        Banning Russia from SWIFT and luxury goods, Western powers expected economic collapse. By 2026, Russia has instead constructed a
        <strong style="color:#E8F4FF;">"Double-Headed Growth"</strong> parallel financial architecture — surviving through two self-contained monetary engines.
        <br><br>
        <strong style="color:#00D4FF;">HEAD 1 — STATE ENGINE:</strong> The Ministry of Finance collects energy revenues in CNY/USD while disbursing all government spending in rubles. When foreign earnings fall, the ruble depreciates — maintaining budget stability at civilian expense through structural inflation.
        <br><br>
        <strong style="color:#FF5555;">HEAD 2 — GREY ENGINE:</strong> Private brokers and CIS networks create parallel financial pipelines — card tourism via Bakai Bank, shadow vessels, Siberian crypto mining, and Chinese middleman luxury channels — sustaining civilian consumption outside Western compliance.
        </div>
    </div>
    """, unsafe_allow_html=True)

    ec1, ec2 = st.columns(2)
    with ec1:
        fig_heads = go.Figure(go.Bar(
            x=["State Engine\n(Domestic)", "Grey Engine\n(International)"],
            y=[55, 45],
            marker_color=[BLUE, RED],
            text=["55%", "45%"],
            textposition="outside",
            textfont=dict(color=FC, size=11),
        ))
        fig_heads.update_layout(**cl(
            title=dict(text="Double-Headed Economic Weight Split", font=dict(size=11, color="#6A8FA8"), x=0),
            yaxis=dict(showgrid=True, gridcolor=GRID, ticksuffix="%", color="#4A6A80"),
            xaxis=dict(color="#4A6A80"), showlegend=False,
            height=240, margin=dict(l=10,r=10,t=40,b=10),
        ))
        st.plotly_chart(fig_heads, use_container_width=True)

    with ec2:
        phases_y = ["2022\nShock", "2023\nBoom", "2024\nPeak", "2025\nCool", "2026\nStall", "2030\nTarget"]
        phases_v = [-1.2, 3.6, 4.9, 1.0, 0.4, 2.5]
        colors_p = [RED if v < 0 else (AMBER if v < 1.5 else CYAN) for v in phases_v]
        colors_p[-1] = GREEN
        fig_ph = go.Figure(go.Bar(x=phases_y, y=phases_v, marker_color=colors_p,
                                   text=[f"{v}%" for v in phases_v], textposition="outside",
                                   textfont=dict(color=FC, size=9)))
        fig_ph.add_hline(y=0, line_color=GREY, line_width=1)
        fig_ph.update_layout(**cl(
            title=dict(text="GDP Growth Phases (% Real)", font=dict(size=11, color="#6A8FA8"), x=0),
            yaxis=dict(showgrid=True, gridcolor=GRID, ticksuffix="%", color="#4A6A80"),
            xaxis=dict(color="#4A6A80"), showlegend=False,
            height=240, margin=dict(l=10,r=10,t=40,b=10),
        ))
        st.plotly_chart(fig_ph, use_container_width=True)

with col_find:
    st.markdown('<div style="font-family:\'Share Tech Mono\',monospace; color:#00D4FF; font-size:0.62rem; letter-spacing:0.22em; margin-bottom:14px;">▸ KEY FINDINGS</div>', unsafe_allow_html=True)
    findings = [
        ("r", "🏦 CIS Card Tourism", "Russian citizens maintain international purchasing power via Bakai Bank (Kyrgyzstan), Evocabank (Armenia), and VTB Belarus — bypassing all international card bans."),
        ("r", "🏴‍☠️ Shadow Fleet 9× Growth", "1,500+ tankers under flags of convenience route crude to Turkey and India for refining laundering. EU nations buy back the same energy at premium prices."),
        ("r", "🔐 Unrecognized Territory Loopholes", "South Ossetia, Abkhazia & Transnistria operate as zero-BIS-oversight financial cut-outs. Funds flow invisibly outside all Western compliance frameworks."),
        ("r", "🚗 Luxury Goods Via China", "G-Wagons, Porsches, BMW X7s reclassified as 'pre-owned' by Chinese customs and routed to Russian showrooms. VPN systems fool European brand servers."),
        ("r", "⛏️ Siberian Crypto Mining", "State-backed operations leverage sub-zero temperatures and $0.03/kWh energy. Kyrgyzstan crypto volume ($31B) exceeds national GDP as liquidity gateway."),
        ("g", "📈 Ruble Devaluation Cushion", "CBR targets 8–10% interest rate by 2027. Sustainable 2.5% GDP growth projected for 2030 as alternative Eurasian financial architecture institutionalizes."),
    ]
    for card_cls, title, desc in findings:
        st.markdown(f'<div class="ic {card_cls}"><h5>{title}</h5><p>{desc}</p></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# SANCTIONS ECOSYSTEM
# ══════════════════════════════════════════════════════════════════════
st.markdown('<div class="sep"><div class="sep-line"></div><div class="sep-diamond"></div><div class="sep-line"></div></div>', unsafe_allow_html=True)
st.markdown('<span id="ecosystem"></span>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <div class="section-tag">▸ MODULE 02 — NETWORK INTELLIGENCE</div>
    <div class="section-title">Russia Sanctions Evasion Ecosystem</div>
    <div class="section-summary">
        Russia is connected to nine primary evasion nodes through financial, energy, trade, and informal networks.
        Each node represents a structural vulnerability in the Western sanctions architecture — a loophole that capital and trade flows exploit continuously.
    </div>
</div>
""", unsafe_allow_html=True)

nodes = {
    "RUSSIA": (0, 0, RED, 42, "Central node of the alternative Eurasian financial order."),
    "CHINA": (2.6, 1.4, BLUE, 32, "CNY clearing, luxury goods conduit, technology supply."),
    "TURKEY": (1.4, -2.1, AMBER, 28, "Energy transit, TurkStream, refining laundering."),
    "INDIA": (3.1, -0.8, BLUE, 26, "Crude oil buyer, Jamnagar refinery, EU re-export."),
    "KYRGYZSTAN": (-2.6, 1.5, GREEN, 22, "Card tourism, Bakai Bank, $31B crypto volume."),
    "ARMENIA": (-2.2, -0.9, GREEN, 20, "Evocabank retail clearing, $1.01B banking profit."),
    "BELARUS": (-1.0, 2.5, GREEN, 20, "VTB sovereign bridge, untraceable ruble transfers."),
    "S. OSSETIA": (-3.1, -0.4, GREY, 16, "SPFS cut-out, zero BIS oversight, MRB Bank."),
    "ABKHAZIA": (-3.2, 0.9, GREY, 14, "Physical cash corridor, unmonitored fuel imports."),
    "TRANSNISTRIA": (-1.8, -2.6, GREY, 14, "Shell company hub, European node mimicry."),
}
edges = [
    ("RUSSIA","CHINA",5,"CNY Direct Clearing + Luxury Goods Pipeline"),
    ("RUSSIA","TURKEY",4,"TurkStream + Crude Oil Transit"),
    ("RUSSIA","INDIA",4,"Discounted Crude → EU Re-export"),
    ("RUSSIA","KYRGYZSTAN",3,"Card Tourism + Crypto Hub"),
    ("RUSSIA","ARMENIA",3,"Evocabank Retail Pipeline"),
    ("RUSSIA","BELARUS",3,"VTB Sovereign Ruble Bridge"),
    ("RUSSIA","S. OSSETIA",2,"SPFS Financial Messaging"),
    ("RUSSIA","ABKHAZIA",2,"Physical Cash Corridor"),
    ("RUSSIA","TRANSNISTRIA",2,"Shell Company Trade Routing"),
    ("TURKEY","INDIA",2,"Refinery Coordination"),
    ("CHINA","KYRGYZSTAN",1.5,"Regional Bank Integration"),
]

fig_net = go.Figure()
for src, tgt, w, lbl in edges:
    x0, y0 = nodes[src][:2]
    x1, y1 = nodes[tgt][:2]
    fig_net.add_trace(go.Scatter(
        x=[x0,x1,None], y=[y0,y1,None], mode="lines",
        line=dict(width=w*0.7, color="rgba(0,212,255,0.18)"),
        hoverinfo="skip", showlegend=False,
    ))
for name, (x, y, color, size, tip) in nodes.items():
    fig_net.add_trace(go.Scatter(
        x=[x], y=[y], mode="markers+text",
        marker=dict(size=size, color=color, line=dict(width=2, color="#E8F4FF"),
                    symbol="circle"),
        text=[name], textposition="top center",
        textfont=dict(color="#C8D8E8", size=9, family="Share Tech Mono"),
        hovertemplate=f"<b>{name}</b><br>{tip}<extra></extra>",
        showlegend=False,
    ))
fig_net.update_layout(**cl(
    title=dict(text="Russia Sanctions Evasion Network — 10-Node Relationship Map", font=dict(size=12, color="#6A8FA8"), x=0),
    xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-4.5,4.5]),
    yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-3.8,3.5]),
    height=500, margin=dict(l=10,r=10,t=45,b=10),
))
st.plotly_chart(fig_net, use_container_width=True)

n1, n2, n3 = st.columns(3)
node_profiles = [
    (BLUE, "🇨🇳 China — Primary Trade Partner", "CNY clearing eliminates USD/SWIFT dependency. Thousands of Chinese middlemen reclassify European luxury vehicles as 'pre-owned' at border zones. Regional banks integrate with CIS accounts to settle high-risk trade outside Western clearinghouses."),
    (AMBER, "🇹🇷 Turkey — Energy Transit Hub", "Tupras refinery converts Russian crude into 'Turkish' diesel and jet fuel. In February 2026 alone, €567M was exported to sanctioning EU countries. TurkStream pipeline delivers gas through Serbia to the broader Balkans."),
    (BLUE, "🇮🇳 India — Crude Buyer & Re-exporter", "Jamnagar (Reliance) purchases Russian crude at discount, refines it, sells to EU nations at premium. The 'refining laundering' loop makes Russian energy legally 'Indian' by the time it re-enters sanctioning countries."),
    (GREEN, "🇰🇬 Kyrgyzstan — CIS Card Gateway", "Bakai Bank enables card tourism. Russian citizens open foreign accounts via local agents, load rubles, and access international Visa/Mastercard networks. Crypto & virtual asset volume: $31B — exceeds national GDP."),
    (GREEN, "🇦🇲 Armenia — Retail Banking Node", "Evocabank: digital wealth parking + cross-border retail payment clearing. National banking sector profit: $1.01B (from $180M pre-sanctions) — a 5× increase driven entirely by Russian capital inflows."),
    (GREY, "🏴 Unrecognized Territories", "South Ossetia (MRB Bank/TSMRBank), Abkhazia, and Transnistria operate as 'Jurisdictional Black Boxes.' No BIS oversight, no Western compliance. U.S. Treasury confirmed TSMRBank's secret North Korea correspondent account."),
]
for row_cols in [[n1,n2,n3]]:
    for col, (color, title, desc) in zip(row_cols, node_profiles[:3]):
        with col:
            st.markdown(f'<div class="gc" style="border-top:2px solid {color};"><div style="color:{color};font-size:0.72rem;font-weight:700;margin-bottom:8px;">{title}</div><div style="color:#3A5A70;font-size:0.77rem;line-height:1.6;">{desc}</div></div>', unsafe_allow_html=True)
n4, n5, n6 = st.columns(3)
for col, (color, title, desc) in zip([n4,n5,n6], node_profiles[3:]):
    with col:
        st.markdown(f'<div class="gc" style="border-top:2px solid {color};"><div style="color:{color};font-size:0.72rem;font-weight:700;margin-bottom:8px;">{title}</div><div style="color:#3A5A70;font-size:0.77rem;line-height:1.6;">{desc}</div></div>', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# CIS BANKING NETWORKS
# ══════════════════════════════════════════════════════════════════════
st.markdown('<div class="sep"><div class="sep-line"></div><div class="sep-diamond"></div><div class="sep-line"></div></div>', unsafe_allow_html=True)
st.markdown('<span id="banking"></span>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <div class="section-tag">▸ MODULE 03 — CAPITAL FLOW INTELLIGENCE</div>
    <div class="section-title">CIS Banking Network Intelligence</div>
    <div class="section-summary">
        Russia → CIS Banks → Global Payments. A multi-stage capital transmission architecture routes sanctioned rubles through retail gateways, sovereign bridges, and corporate aggregation layers — terminating in a closed RUB-CNY clearing matrix invisible to Western networks.
    </div>
</div>
""", unsafe_allow_html=True)

bk1, bk2, bk3, bk4 = st.columns(4)
for col, (v, l, c) in zip([bk1,bk2,bk3,bk4], [
    ("$3.5B","Kyrgyzstan Remittances",""), ("$1.01B","Armenia Banking Profit","green"),
    ("$31B","Kyrgyz Crypto Volume","red"), ("3","Active CIS Gateways","amber"),
]):
    with col:
        st.markdown(f'<div class="kpi-wrap {c}"><div class="kpi-v">{v}</div><div class="kpi-l">{l}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
bkcol1, bkcol2 = st.columns([3, 2])

with bkcol1:
    labels = ["Sanctioned Russian Rubles","SPFS Messaging Rail","Bakai Bank (Kyrgyzstan)",
              "Evocabank (Armenia)","VTB Belarus","CIS Correspondent Layer","Chinese Regional Banks",
              "RUB-CNY Clearing Matrix","International Retail Payments","Foreign Exchange (FX)","Global Procurement"]
    src  = [0,0,0,0,1,1,2,3,4,5,5,6,7,8,9,10]
    tgt  = [1,2,3,4,5,6,9,8,10,6,7,7,11 if False else 10,10,10,10]
    val  = [50,20,15,15,25,25,20,15,15,15,10,20,30,15,20,15]
    # Rebuild with correct indices
    labels2 = ["Sanctioned RUB","SPFS Rail","Bakai Bank\n(Kyrgyzstan)","Evocabank\n(Armenia)",
               "VTB Belarus","CIS Correspondent\nLayer","Chinese\nRegional Banks",
               "RUB-CNY\nClearing Matrix","Intl Retail\nPayments","Foreign\nExchange","Global\nProcurement"]
    src2  = [0,0,0,0,1,1,2,3,4,5,5,6,7,8,9]
    tgt2  = [1,2,3,4,5,6,9,8,10,6,7,7,10,10,10]
    val2  = [50,20,15,15,25,25,20,15,15,15,10,20,15,20,15]
    node_colors2 = [RED,"#5C7A8A",GREEN,GREEN,GREEN,BLUE,BLUE,AMBER,AMBER,AMBER,"#E8F4FF"]
    link_colors2 = [
        "rgba(255,68,68,0.25)","rgba(255,68,68,0.25)","rgba(255,68,68,0.25)","rgba(255,68,68,0.25)",
        "rgba(0,212,255,0.2)","rgba(0,212,255,0.2)",
        "rgba(0,255,144,0.2)","rgba(0,255,144,0.2)","rgba(0,255,144,0.2)",
        "rgba(0,212,255,0.2)","rgba(0,212,255,0.2)",
        "rgba(255,184,0,0.2)","rgba(255,184,0,0.2)","rgba(255,184,0,0.2)","rgba(255,184,0,0.2)",
    ]
    fig_sankey = go.Figure(go.Sankey(
        arrangement="snap",
        node=dict(pad=18, thickness=18,
                  line=dict(color="#1A2A3A", width=0.5),
                  label=labels2, color=node_colors2,
                  hovertemplate="%{label}<extra></extra>"),
        link=dict(source=src2, target=tgt2, value=val2, color=link_colors2),
    ))
    fig_sankey.update_layout(**cl(
        title=dict(text="Russia → CIS Banks → Global Payments: Capital Flow Architecture", font=dict(size=11, color="#6A8FA8"), x=0),
        height=420, margin=dict(l=10,r=10,t=40,b=10),
    ))
    st.plotly_chart(fig_sankey, use_container_width=True)

with bkcol2:
    st.markdown('<div style="font-family:\'Share Tech Mono\',monospace; color:#00D4FF; font-size:0.62rem; letter-spacing:0.22em; margin-bottom:14px;">▸ TRANSMISSION STAGES</div>', unsafe_allow_html=True)
    stages = [
        (RED, "STAGE 1A — Bakai Bank", "Kyrgyzstan. Retail access & foreign account onboarding. RUB deposits swapped into FX. Working Visa cards for international e-commerce."),
        (GREEN, "STAGE 1B — Evocabank", "Armenia. Digital wealth parking & cross-border retail settlement. Strict compliance coverage. $1.01B national banking profit."),
        (BLUE, "STAGE 1C — VTB Belarus", "Unified economic agreements. High-volume untraceable ruble transfers. Invisible to Western financial tracking networks."),
        (AMBER, "STAGE 2 — CIS Correspondent Layer", "Consolidation of intermediary capital flows. Integration with smaller regional Chinese financial cards and banks."),
        (GREY, "STAGE 3 — RUB-CNY Clearing Matrix", "Direct ruble-to-yuan closed-loop settlement. Removes all Western intermediary dependency. Zero SWIFT footprint."),
    ]
    for color, title, desc in stages:
        st.markdown(f'''<div style="background:rgba(0,8,20,0.7); border:1px solid rgba(0,212,255,0.09);
             border-left:3px solid {color}; border-radius:0 6px 6px 0;
             padding:12px 14px; margin-bottom:8px;">
            <div style="color:{color};font-size:0.65rem;font-weight:700;letter-spacing:0.08em;margin-bottom:4px;">{title}</div>
            <div style="color:#3A5A70;font-size:0.76rem;line-height:1.5;">{desc}</div>
        </div>''', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    df_remit = pd.DataFrame({
        "Country / Metric": ["Kyrgyzstan — Remittances (Pre-2022)", "Kyrgyzstan — Remittances (2025–26)",
                             "Armenia — Banking Profit (Pre-2022)", "Armenia — Banking Profit (2025–26)"],
        "Value ($B)": [1.17, 3.25, 0.18, 1.01],
    })
    fig_remit = go.Figure(go.Bar(
        x=df_remit["Country / Metric"], y=df_remit["Value ($B)"],
        marker_color=[GREY, RED, GREY, GREEN],
        text=[f"${v}B" for v in df_remit["Value ($B)"]],
        textposition="outside", textfont=dict(color=FC, size=9),
    ))
    fig_remit.update_layout(**cl(
        yaxis=dict(showgrid=True, gridcolor=GRID, tickprefix="$", ticksuffix="B", color="#4A6A80"),
        xaxis=dict(color="#4A6A80", tickfont=dict(size=7)), showlegend=False,
        height=220, margin=dict(l=10,r=10,t=10,b=10),
        title=dict(text="CIS Banking Growth: Pre-Sanctions vs 2025–26", font=dict(size=10, color="#6A8FA8"), x=0),
    ))
    st.plotly_chart(fig_remit, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════
# SHADOW FLEET
# ══════════════════════════════════════════════════════════════════════
st.markdown('<div class="sep"><div class="sep-line"></div><div class="sep-diamond"></div><div class="sep-line"></div></div>', unsafe_allow_html=True)
st.markdown('<span id="fleet"></span>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <div class="section-tag">▸ MODULE 04 — MARITIME INTELLIGENCE</div>
    <div class="section-title">Shadow Fleet Intelligence Center</div>
    <div class="section-summary">
        Russia operates 1,500+ shadow tankers registered under flags of convenience — a fleet that grew 9× since 2022.
        Crude is routed to Turkey and India where it is refined and legally re-exported to the EU nations that banned it, at premium prices.
    </div>
</div>
""", unsafe_allow_html=True)

sf1, sf2, sf3, sf4, sf5 = st.columns(5)
for col, (v, l, c) in zip([sf1,sf2,sf3,sf4,sf5], [
    ("1,500+","Shadow Vessels","red"), ("9×","Fleet Growth Since 2022","amber"),
    ("€1.075T","Total Energy Revenue",""), ("€231B","EU Purchases Despite Ban","red"),
    ("€567M","Feb 2026 Refinery Exports","amber"),
]):
    with col:
        st.markdown(f'<div class="kpi-wrap {c}"><div class="kpi-v">{v}</div><div class="kpi-l">{l}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
sfmap_col, sfinfo_col = st.columns([3, 2])

with sfmap_col:
    locs = {
        "Russia (Novorossiysk)":(44.7,37.8), "Russia (Primorsk)":(60.0,28.5),
        "Turkey (Tupras)":(41.0,29.0), "India (Jamnagar)":(22.5,70.1),
        "China (Shanghai)":(31.2,121.5), "EU France":(48.9,2.3),
        "EU Belgium":(50.8,4.4), "Hungary":(47.5,19.0), "Serbia":(44.8,20.5),
        "Liberia (Flag)":(6.3,-10.8), "Panama (Flag)":(9.0,-79.5),
    }
    routes = [
        ("Russia (Novorossiysk)","Turkey (Tupras)", RED, 3, "Crude → Tupras Refinery"),
        ("Russia (Primorsk)","India (Jamnagar)", RED, 3, "Discounted Crude → Jamnagar"),
        ("Turkey (Tupras)","EU France", AMBER, 2, "'Turkish' Fuel → EU"),
        ("Turkey (Tupras)","EU Belgium", AMBER, 2, "'Turkish' Fuel → EU"),
        ("India (Jamnagar)","EU France", BLUE, 2, "'Indian' Fuel → EU"),
        ("Russia (Primorsk)","China (Shanghai)", CYAN, 2, "China Supply"),
        ("Turkey (Tupras)","Serbia", AMBER, 1.5, "TurkStream Region"),
    ]
    fig_map = go.Figure()
    for src, tgt, color, w, lbl in routes:
        lat0,lon0 = locs[src]
        lat1,lon1 = locs[tgt]
        fig_map.add_trace(go.Scattergeo(lat=[lat0,lat1],lon=[lon0,lon1],mode="lines",
                                         line=dict(width=w,color=color),
                                         hoverinfo="text",text=lbl,showlegend=False))
    nc = {
        "Russia":RED,"Turkey":AMBER,"India":BLUE,"EU":GREEN,
        "China":BLUE,"Hungary":AMBER,"Serbia":AMBER,"Liberia":GREY,"Panama":GREY,
    }
    for name,(lat,lon) in locs.items():
        key = name.split(" ")[0]
        fig_map.add_trace(go.Scattergeo(
            lat=[lat],lon=[lon],mode="markers+text",
            marker=dict(size=9 if "Russia" in name else 7, color=nc.get(key,GREY),
                        line=dict(width=1,color="#E8F4FF")),
            text=[name.split(" (")[0]], textposition="top right",
            textfont=dict(color="#C8D8E8",size=8),
            hovertemplate=f"<b>{name}</b><extra></extra>",showlegend=False,
        ))
    fig_map.update_layout(
        geo=dict(showland=True,landcolor="#0A1828",showocean=True,oceancolor="#020B18",
                 showcoastlines=True,coastlinecolor=GREY,showcountries=True,countrycolor="#1A2A3A",
                 showframe=False,projection_type="natural earth",bgcolor="#050B18",showlakes=False),
        paper_bgcolor=PAPER, font=dict(color=FC),
        margin=dict(l=0,r=0,t=10,b=0), height=420,
    )
    st.plotly_chart(fig_map, use_container_width=True)

with sfinfo_col:
    st.markdown('<div style="font-family:\'Share Tech Mono\',monospace; color:#00D4FF; font-size:0.62rem; letter-spacing:0.22em; margin-bottom:14px;">▸ OPERATION BRIEF</div>', unsafe_allow_html=True)
    for color, title, desc in [
        (RED, "Ghost Fleet Operation", "Russia invested billions acquiring 1,500+ shadow tankers — older oil vessels that bypass Western tracking. By late 2025, the fleet grew 9× and delivered billions in crude via EU waters without Western insurance."),
        (AMBER, "The Registration Trick", "Tankers registered under 'Flags of Convenience' in Liberia, Panama, and the Marshall Islands. Non-aligned nations with zero Western compliance obligations. G7 oil price cap effectively nullified."),
        (BLUE, "Refining Laundering", "Russian crude → Turkey (Tupras) and India (Jamnagar). Converted to diesel and jet fuel that becomes legally 'Turkish' or 'Indian'. In February 2026: €567M exported back to sanctioning EU states in a single month."),
        (GREEN, "Rebel Buyers", "Hungary: 93% Russian oil dependency in 2025 (from 61% in 2021). Serbia: TurkStream gas contract renewed through March 2026. EU nations like France and Belgium confirmed buying back refined Russian energy."),
    ]:
        st.markdown(f'''<div class="ic" style="border-left-color:{color}">
            <h5 style="color:{color};">{title}</h5><p>{desc}</p></div>''', unsafe_allow_html=True)

    years_f = [2021,2022,2023,2024,2025,2026]
    fleet_v = [165,400,750,1100,1400,1500]
    fig_fl = go.Figure()
    fig_fl.add_trace(go.Scatter(x=years_f, y=fleet_v, mode="lines+markers",
                                 line=dict(color=RED,width=2.5),
                                 marker=dict(color=RED,size=7,line=dict(color="#E8F4FF",width=1)),
                                 fill="tozeroy", fillcolor="rgba(255,68,68,0.06)"))
    fig_fl.update_layout(**cl(
        yaxis=dict(showgrid=True,gridcolor=GRID,color="#4A6A80",title="Vessels"),
        xaxis=dict(color="#4A6A80",showgrid=False), showlegend=False,
        height=200, margin=dict(l=10,r=10,t=10,b=10),
    ))
    st.plotly_chart(fig_fl, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════
# ENERGY REVENUE
# ══════════════════════════════════════════════════════════════════════
st.markdown('<div class="sep"><div class="sep-line"></div><div class="sep-diamond"></div><div class="sep-line"></div></div>', unsafe_allow_html=True)
st.markdown('<span id="energy"></span>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <div class="section-tag">▸ MODULE 05 — ENERGY REVENUE ANALYTICS</div>
    <div class="section-title">Energy Revenue Intelligence</div>
    <div class="section-summary">
        Russia earned €1.075 trillion in fossil fuel revenue since 2022. EU countries, despite official bans, account for €231 billion
        of this total — purchasing refined Russian energy via Turkish and Indian intermediaries. Energy demand overrides sanctions politics.
    </div>
</div>
""", unsafe_allow_html=True)

en1, en2 = st.columns(2)
with en1:
    yrs = [2022,2023,2024,2025,2026,2027,2028,2029,2030]
    non_eu = [243,200,178,154,137,130,125,122,120]
    eu_rev = [85,65,52,41,38,36,35,34,33]
    forecast_start = 5
    fig_en = go.Figure()
    fig_en.add_trace(go.Bar(name="Non-EU Revenue",x=yrs[:forecast_start],y=non_eu[:forecast_start],marker_color=CYAN,opacity=0.8))
    fig_en.add_trace(go.Bar(name="EU Revenue (refinery laundering)",x=yrs[:forecast_start],y=eu_rev[:forecast_start],marker_color=RED,opacity=0.8))
    fig_en.add_trace(go.Bar(name="Non-EU (Forecast)",x=yrs[forecast_start-1:],y=non_eu[forecast_start-1:],marker_color=CYAN,opacity=0.3,marker_pattern_shape="/"))
    fig_en.add_trace(go.Bar(name="EU (Forecast)",x=yrs[forecast_start-1:],y=eu_rev[forecast_start-1:],marker_color=RED,opacity=0.3,marker_pattern_shape="/"))
    fig_en.update_layout(**cl(
        title=dict(text="Annual Energy Export Revenue (€B) — Actual + Forecast to 2030", font=dict(size=11, color="#6A8FA8"), x=0),
        barmode="stack",
        yaxis=dict(showgrid=True,gridcolor=GRID,tickprefix="€",ticksuffix="B",color="#4A6A80"),
        xaxis=dict(color="#4A6A80",dtick=1), height=320,
    ))
    st.plotly_chart(fig_en, use_container_width=True)

with en2:
    partners = ["China","India","Turkey","Belarus","Hungary","Serbia","Other CIS","Other"]
    shares = [32,22,15,8,6,4,7,6]
    colors_pie = [BLUE,GREEN,AMBER,GREEN,RED,RED,GREY,"#1A3040"]
    fig_pie = go.Figure(go.Pie(
        labels=partners, values=shares,
        marker=dict(colors=colors_pie, line=dict(color="#050B18",width=2)),
        textfont=dict(color=FC, size=10),
        hovertemplate="<b>%{label}</b><br>%{value}% market share<extra></extra>",
        hole=0.42,
    ))
    fig_pie.update_layout(**cl(
        title=dict(text="Energy Trade Partner Market Share — 2026", font=dict(size=11, color="#6A8FA8"), x=0),
        height=320,
        annotations=[dict(text="Trade<br>Mix", x=0.5, y=0.5, font=dict(size=11,color=FC), showarrow=False)],
    ))
    st.plotly_chart(fig_pie, use_container_width=True)

months_m = ["Aug'25","Sep'25","Oct'25","Nov'25","Dec'25","Jan'26","Feb'26"]
monthly_v = [420,445,480,510,495,530,567]
col_colors = [GREY]*6 + [RED]
fig_monthly = go.Figure(go.Bar(
    x=months_m, y=monthly_v, marker_color=col_colors,
    text=[f"€{v}M" for v in monthly_v], textposition="outside", textfont=dict(color=FC, size=10),
))
fig_monthly.add_annotation(x="Feb'26", y=567, text="▲ PEAK: €567M — SINGLE MONTH",
                             showarrow=True, arrowhead=2, arrowcolor=RED,
                             font=dict(color=RED, size=10), ax=-80, ay=-35)
fig_monthly.update_layout(**cl(
    title=dict(text="Monthly Refinery Laundering Flow — EU Receipts (€M)", font=dict(size=11,color="#6A8FA8"), x=0),
    yaxis=dict(showgrid=True,gridcolor=GRID,tickprefix="€",ticksuffix="M",color="#4A6A80"),
    xaxis=dict(color="#4A6A80"), showlegend=False, height=240,
))
st.plotly_chart(fig_monthly, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════
# LUXURY GOODS RE-ROUTING
# ══════════════════════════════════════════════════════════════════════
st.markdown('<div class="sep"><div class="sep-line"></div><div class="sep-diamond"></div><div class="sep-line"></div></div>', unsafe_allow_html=True)
st.markdown('<span id="luxury"></span>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <div class="section-tag">▸ MODULE 06 — SUPPLY CHAIN INTELLIGENCE</div>
    <div class="section-title">Luxury Goods Re-Routing Network</div>
    <div class="section-summary">
        European luxury vehicles — the G-Wagon, Porsche 911, BMW X7, Audi EV — continuously fill Russian showrooms.
        New factory vehicles sold to China are reclassified as 'pre-owned' at Chinese border zones, then transit Eurasian customs with zero compliance risk.
        VPN systems rented from Dubai and Istanbul fool European servers into providing cloud updates.
    </div>
</div>
""", unsafe_allow_html=True)

flow_cols = st.columns(7)
flow_steps = [
    (BLUE,"🏭","STAGE 1","Austria\n(Magna Steyr, Graz)","Single factory worldwide. No alternate source."),
    (None,"→","","",""),
    (AMBER,"🇨🇳","STAGE 2","China\n'Asian Market'","Sold to qualified buyers. Fully legal export."),
    (None,"→","","",""),
    (AMBER,"🔄","STAGE 3","Chinese Border\nZone","Reclassified as 'pre-owned / used car' by Chinese customs."),
    (None,"→","","",""),
    (RED,"🇷🇺","STAGE 4","Russia\nShowrooms","Zero compliance risk. VPN fools European brand servers."),
]
for col, (color, icon, stage, loc, desc) in zip(flow_cols, flow_steps):
    with col:
        if color is None:
            st.markdown(f'<div class="flow-arrow">{icon}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'''<div class="flow-step" style="border-top:2px solid {color};">
                <div style="font-size:1.4rem;margin-bottom:6px;">{icon}</div>
                <div style="color:{color};font-size:0.6rem;font-weight:700;letter-spacing:0.1em;margin-bottom:4px;">{stage}</div>
                <div style="color:#E8F4FF;font-size:0.75rem;font-weight:600;margin-bottom:6px;white-space:pre-line;">{loc}</div>
                <div style="color:#2A4050;font-size:0.7rem;line-height:1.4;">{desc}</div>
            </div>''', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
lux1, lux2 = st.columns(2)

with lux1:
    yrs_lux = [2022,2023,2024,2025,2026]
    gwagon = [120,890,2100,3400,2800]
    porsche = [80,540,1200,2100,1900]
    bmw_x7 = [200,1200,2800,4200,3700]
    fig_lux = go.Figure()
    fig_lux.add_trace(go.Bar(name="Mercedes G-Wagon",x=yrs_lux,y=gwagon,marker_color=RED))
    fig_lux.add_trace(go.Bar(name="Porsche 911/Cayenne",x=yrs_lux,y=porsche,marker_color=AMBER))
    fig_lux.add_trace(go.Bar(name="BMW X7 / Audi EV",x=yrs_lux,y=bmw_x7,marker_color=CYAN))
    fig_lux.update_layout(**cl(
        title=dict(text="Luxury Vehicles Re-Routed via Chinese Middlemen (Est. Units)", font=dict(size=11,color="#6A8FA8"), x=0),
        barmode="group",
        yaxis=dict(showgrid=True,gridcolor=GRID,color="#4A6A80",title="Units"),
        xaxis=dict(color="#4A6A80"), height=300,
    ))
    st.plotly_chart(fig_lux, use_container_width=True)

with lux2:
    lux_labels = ["Austria / Germany","China (Official Sale)","Chinese Border Zone","Central Asian Transit","Russia Showrooms","Russia Private Buyers"]
    lux_src = [0,1,0,1,2,2,3,3,4]
    lux_tgt = [1,1,1,1,3,3,4,5,4]
    lux_src2 = [0,0,1,1,2,2,3]
    lux_tgt2 = [2,2,3,3,4,5,4]
    lux_val2 = [40,35,45,30,35,10,25]
    lux_node_c = [BLUE,BLUE,AMBER,GREY,RED,RED]
    lux_link_c = ["rgba(26,122,255,0.3)","rgba(26,122,255,0.3)","rgba(255,184,0,0.3)","rgba(255,184,0,0.3)","rgba(255,68,68,0.3)","rgba(255,68,68,0.3)","rgba(255,68,68,0.3)"]
    fig_lsankey = go.Figure(go.Sankey(
        node=dict(pad=14,thickness=16,label=lux_labels,color=lux_node_c,
                  line=dict(color="#1A2A3A",width=0.5),hovertemplate="%{label}<extra></extra>"),
        link=dict(source=lux_src2,target=lux_tgt2,value=lux_val2,color=lux_link_c),
    ))
    fig_lsankey.update_layout(**cl(
        title=dict(text="Luxury Vehicle Supply Chain — Sankey Flow", font=dict(size=11,color="#6A8FA8"), x=0),
        height=300, margin=dict(l=10,r=10,t=40,b=10),
    ))
    st.plotly_chart(fig_lsankey, use_container_width=True)

vpn1, vpn2, vpn3 = st.columns(3)
for col, (icon, title, color, text) in zip([vpn1,vpn2,vpn3], [
    ("🔑","The Software Block",RED,"European manufacturers encode geofencing into vehicle systems. Without European server approval, modern luxury vehicles cannot receive OTA updates, warranty activation, or navigation services in unauthorized markets."),
    ("🌐","The VPN Solution",AMBER,"Russian dealerships rent VPN access from trusted hubs — Dubai and Istanbul. Vehicle computers connect through these VPNs, fooling European central servers into treating Russian locations as authorized European service centers."),
    ("✅","Result: Total Nullification",GREEN,"Cloud updates deploy normally. Warranties activate. Navigation, ADAS, and OTA features function as if the vehicle is in Germany. Commercial VPN infrastructure completely neutralizes a billion-dollar software blockade."),
]):
    with col:
        st.markdown(f'''<div class="gc" style="border-top:2px solid {color}; min-height:180px;">
            <div style="font-size:1.3rem;margin-bottom:8px;">{icon}</div>
            <div style="color:{color};font-weight:700;font-size:0.85rem;margin-bottom:10px;">{title}</div>
            <div style="color:#3A5A70;font-size:0.78rem;line-height:1.65;">{text}</div>
        </div>''', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# CRYPTO MINING
# ══════════════════════════════════════════════════════════════════════
st.markdown('<div class="sep"><div class="sep-line"></div><div class="sep-diamond"></div><div class="sep-line"></div></div>', unsafe_allow_html=True)
st.markdown('<span id="crypto"></span>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <div class="section-tag">▸ MODULE 07 — DIGITAL ASSET INTELLIGENCE</div>
    <div class="section-title">Crypto Mining & Alternative Liquidity</div>
    <div class="section-summary">
        Russia converts cheap Siberian energy and sub-zero temperatures into an insurmountable crypto mining cost advantage.
        State-backed operations generate Bitcoin funded with foreign debt. Kyrgyzstan acts as the $31B liquidity gateway — exceeding national GDP — routing digital assets outside all Western financial monitoring.
    </div>
</div>
""", unsafe_allow_html=True)

cr1, cr2, cr3, cr4 = st.columns(4)
for col, (v, l, c) in zip([cr1,cr2,cr3,cr4], [
    ("$31B","Kyrgyzstan Crypto Volume","red"), ("#2 Global","Russia Mining Rank","amber"),
    ("-40°C","Siberian Cooling Advantage",""), ("$0.03","Energy Cost per kWh","green"),
]):
    with col:
        st.markdown(f'<div class="kpi-wrap {c}"><div class="kpi-v">{v}</div><div class="kpi-l">{l}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
crnet_col, crmod_col = st.columns([2, 3])

with crnet_col:
    crypto_nodes = {
        "Siberian\nMining Farms":(0,0,RED,34),
        "Cheap State\nEnergy":(-1.6,1.2,BLUE,22),
        "Sub-Zero\nClimate":(-1.6,-1.2,BLUE,20),
        "Bitcoin &\nCrypto":(1.8,0.7,AMBER,28),
        "Foreign Currency\nPurchase":(1.8,-0.7,AMBER,20),
        "Kyrgyzstan\nCrypto Hub":(3.2,0,GREEN,24),
        "Alternative\nLiquidity":(0,-2.2,GREEN,20),
        "Chinese\nExchanges":(3.2,-1.5,GREY,16),
    }
    crypto_edges = [
        ("Cheap State\nEnergy","Siberian\nMining Farms"),
        ("Sub-Zero\nClimate","Siberian\nMining Farms"),
        ("Siberian\nMining Farms","Bitcoin &\nCrypto"),
        ("Siberian\nMining Farms","Foreign Currency\nPurchase"),
        ("Bitcoin &\nCrypto","Kyrgyzstan\nCrypto Hub"),
        ("Foreign Currency\nPurchase","Alternative\nLiquidity"),
        ("Kyrgyzstan\nCrypto Hub","Alternative\nLiquidity"),
        ("Kyrgyzstan\nCrypto Hub","Chinese\nExchanges"),
    ]
    fig_cn = go.Figure()
    for s, t in crypto_edges:
        x0,y0 = crypto_nodes[s][:2]
        x1,y1 = crypto_nodes[t][:2]
        fig_cn.add_trace(go.Scatter(x=[x0,x1,None],y=[y0,y1,None],mode="lines",
                                     line=dict(width=1.5,color="rgba(0,212,255,0.2)"),
                                     hoverinfo="skip",showlegend=False))
    for name,(x,y,color,size) in crypto_nodes.items():
        fig_cn.add_trace(go.Scatter(
            x=[x],y=[y],mode="markers+text",
            marker=dict(size=size,color=color,line=dict(width=1.5,color="#E8F4FF")),
            text=[name],textposition="top center",
            textfont=dict(color="#C8D8E8",size=8),
            hovertemplate=f"<b>{name.replace(chr(10),' ')}</b><extra></extra>",showlegend=False,
        ))
    fig_cn.update_layout(**cl(
        xaxis=dict(showgrid=False,zeroline=False,showticklabels=False,range=[-2.8,4.5]),
        yaxis=dict(showgrid=False,zeroline=False,showticklabels=False,range=[-3.2,2.5]),
        height=380, margin=dict(l=10,r=10,t=10,b=10),
        title=dict(text="Siberian Crypto Liquidity Ecosystem", font=dict(size=11,color="#6A8FA8"), x=0),
    ))
    st.plotly_chart(fig_cn, use_container_width=True)

with crmod_col:
    qs = ["Q1'22","Q2'22","Q3'22","Q4'22","Q1'23","Q2'23","Q3'23","Q4'23",
          "Q1'24","Q2'24","Q3'24","Q4'24","Q1'25","Q2'25","Q3'25","Q4'25","Q1'26"]
    mining_idx = [2.0,3.2,5.1,7.8,10.2,12.5,14.8,16.2,17.5,18.8,19.4,20.1,21.3,22.0,22.8,23.5,24.1]
    kyrgyz_vol = [0.5,0.8,1.2,2.1,3.5,5.2,8.4,11.2,14.8,17.5,20.1,22.8,25.2,27.4,29.1,30.5,31.0]
    fig_cg = go.Figure()
    fig_cg.add_trace(go.Scatter(x=qs,y=mining_idx,mode="lines",name="Siberian Mining Power Index",
                                 line=dict(color=RED,width=2.5),fill="tozeroy",fillcolor="rgba(255,68,68,0.06)"))
    fig_cg.add_trace(go.Scatter(x=qs,y=kyrgyz_vol,mode="lines",name="Kyrgyzstan Crypto Volume ($B)",
                                 line=dict(color=AMBER,width=2.5),yaxis="y2"))
    fig_cg.update_layout(**cl(
        title=dict(text="Mining Power Index vs Kyrgyzstan Crypto Volume — Q1 2022 to Q1 2026", font=dict(size=11,color="#6A8FA8"), x=0),
        yaxis=dict(color=RED,showgrid=True,gridcolor=GRID,title="Mining Power Index"),
        yaxis2=dict(overlaying="y",side="right",color=AMBER,title="Volume ($B)",showgrid=False),
        xaxis=dict(color="#4A6A80",tickfont=dict(size=8)),
        height=230,
    ))
    st.plotly_chart(fig_cg, use_container_width=True)

    countries_e = ["Germany","UK","USA","China","Kazakhstan","Russia\n(Siberia)"]
    cost_e = [0.38,0.32,0.17,0.08,0.05,0.03]
    col_e = [GREY,GREY,GREY,BLUE,AMBER,RED]
    fig_ce = go.Figure(go.Bar(
        x=countries_e, y=cost_e, marker_color=col_e,
        text=[f"${v:.2f}" for v in cost_e], textposition="outside", textfont=dict(color=FC,size=9),
    ))
    fig_ce.update_layout(**cl(
        title=dict(text="Energy Cost per kWh — Global Mining Comparison", font=dict(size=11,color="#6A8FA8"), x=0),
        yaxis=dict(showgrid=True,gridcolor=GRID,tickprefix="$",color="#4A6A80"),
        xaxis=dict(color="#4A6A80"), showlegend=False, height=230,
    ))
    st.plotly_chart(fig_ce, use_container_width=True)

cr_mech = st.columns(4)
mechs = [
    ("❄️","Temperature Advantage",BLUE,"Sub-zero Siberian winters provide free cooling for ASIC rigs. Cooling = 30–40% of global mining overhead — eliminated entirely. Creates an insurmountable structural cost moat vs. Western competitors."),
    ("⚡","Cheap State Energy",AMBER,"Russia's subsidized infrastructure provides $0.03/kWh — 10× cheaper than Germany, 5× cheaper than USA. Mining profitability structurally guaranteed regardless of Bitcoin price fluctuations."),
    ("🏛️","State Financing",RED,"Operations funded directly via foreign debt — purchased cryptocurrencies as collateral. State backing removes private capital risk, enabling industrial-scale mining impossible for private actors in sanctioned markets."),
    ("🔄","The Liquidity Loop",GREEN,"Mined Bitcoin converts to foreign currency via Kyrgyzstan ($31B hub, exceeding national GDP). A perpetual autonomous liquidity engine operating entirely outside Western financial monitoring and international compliance."),
]
for col, (icon, title, color, text) in zip(cr_mech, mechs):
    with col:
        st.markdown(f'''<div class="gc" style="border-top:2px solid {color}; min-height:190px;">
            <div style="font-size:1.2rem;margin-bottom:8px;">{icon}</div>
            <div style="color:{color};font-weight:700;font-size:0.85rem;margin-bottom:8px;">{title}</div>
            <div style="color:#3A5A70;font-size:0.77rem;line-height:1.6;">{text}</div>
        </div>''', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# MACROECONOMIC DASHBOARD
# ══════════════════════════════════════════════════════════════════════
st.markdown('<div class="sep"><div class="sep-line"></div><div class="sep-diamond"></div><div class="sep-line"></div></div>', unsafe_allow_html=True)
st.markdown('<span id="macro"></span>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <div class="section-tag">▸ MODULE 08 — MACROECONOMIC INTELLIGENCE</div>
    <div class="section-title">Macroeconomic Dashboard</div>
    <div class="section-summary">
        From sanctions shock (−1.2% GDP, 11.9% inflation in 2022) to war economy boom (4.9% GDP peak in 2024) to physical limit stabilization (0.4% GDP in 2026).
        The CBR targets 8–10% interest rates and 2.5% sustainable GDP growth by 2030 as the alternative Eurasian financial architecture institutionalizes.
    </div>
</div>
""", unsafe_allow_html=True)

mc1, mc2, mc3, mc4 = st.columns(4)
for col, (v,l,c) in zip([mc1,mc2,mc3,mc4],[
    ("0.4%","GDP Growth 2026","amber"), ("5.2%","CPI Inflation 2026",""),
    ("14.5%","Key Interest Rate 2026","red"), ("2.5%","Projected GDP 2030","green"),
]):
    with col:
        st.markdown(f'<div class="kpi-wrap {c}"><div class="kpi-v">{v}</div><div class="kpi-l">{l}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

yrs_m = [2022,2023,2024,2025,2026,2027,2028,2029,2030]
gdp_m = [-1.2,3.6,4.9,1.0,0.4,1.4,1.9,2.4,2.5]
cpi_m = [11.9,7.4,5.9,5.6,5.2,4.0,4.0,4.0,4.0]
rate_m = [20.0,16.0,18.0,21.0,14.5,10.5,8.5,8.0,8.0]

fig_macro = go.Figure()
fig_macro.add_trace(go.Scatter(
    x=yrs_m[:5], y=gdp_m[:5], mode="lines+markers", name="GDP Growth (Actual)",
    line=dict(color=CYAN,width=3), marker=dict(size=8,color=CYAN,line=dict(color="#E8F4FF",width=1)),
))
fig_macro.add_trace(go.Scatter(
    x=yrs_m[4:], y=gdp_m[4:], mode="lines+markers", name="GDP Growth (Forecast)",
    line=dict(color=CYAN,width=2,dash="dash"), marker=dict(size=7,color=CYAN),
))
fig_macro.add_trace(go.Scatter(
    x=yrs_m[:5], y=cpi_m[:5], mode="lines+markers", name="CPI Inflation (Actual)",
    line=dict(color=RED,width=3), marker=dict(size=8,color=RED,line=dict(color="#E8F4FF",width=1)),
    yaxis="y2",
))
fig_macro.add_trace(go.Scatter(
    x=yrs_m[4:], y=cpi_m[4:], mode="lines+markers", name="CPI Inflation (Forecast)",
    line=dict(color=RED,width=2,dash="dash"), marker=dict(size=7,color=RED), yaxis="y2",
))
fig_macro.add_trace(go.Bar(
    x=yrs_m, y=rate_m, name="Key Interest Rate (%)",
    marker_color="rgba(255,184,0,0.2)", marker_line=dict(color=AMBER,width=1),
    yaxis="y2", opacity=0.7,
))
fig_macro.add_vrect(x0=2026.4,x1=2030.4,fillcolor="rgba(0,212,255,0.015)",
                     line_width=0.5,line_color=GRID,
                     annotation_text="CBR FORECAST PERIOD 2027–2030",
                     annotation_font=dict(color="#4A6A80",size=8))
for x, y, label, color in [(2024,4.9,"PEAK GDP 4.9%",CYAN),(2022,11.9,"SANCTIONS SHOCK 11.9%",RED)]:
    yr_ref = "y" if label.startswith("PEAK") else "y2"
    fig_macro.add_annotation(x=x,y=y,text=label,showarrow=True,arrowhead=2,
                               arrowcolor=color,font=dict(color=color,size=9),
                               ax=35,ay=-30,yref=yr_ref)
fig_macro.update_layout(**cl(
    title=dict(text="GDP Growth / CPI Inflation / Key Interest Rate — 2022–2030 (Actual + CBR Forecast)", font=dict(size=12,color="#6A8FA8"), x=0),
    yaxis=dict(color=CYAN,showgrid=True,gridcolor=GRID,title="GDP Growth (%)",ticksuffix="%",zeroline=True,zerolinecolor=GREY),
    yaxis2=dict(overlaying="y",side="right",color=RED,title="CPI / Interest Rate (%)",ticksuffix="%",showgrid=False),
    xaxis=dict(color="#4A6A80",dtick=1,showgrid=False),
    legend=dict(orientation="h",yanchor="bottom",y=1.02,font=dict(size=9,color="#6A8FA8"),bgcolor=PAPER),
    height=400,
))
st.plotly_chart(fig_macro, use_container_width=True)

df_macro = pd.DataFrame({
    "Year": yrs_m,
    "GDP Growth (%)": gdp_m,
    "CPI Inflation (%)": cpi_m,
    "Key Rate (%)": rate_m,
    "Status": ["Actual"]*5 + ["CBR Forecast"]*4,
})

def style_gdp(v):
    if isinstance(v, float):
        if v < 0: return "color: #FF5555"
        elif v < 1.5: return "color: #FFB800"
        return "color: #00FF90"
    return ""

def style_cpi(v):
    if isinstance(v, float):
        if v > 10: return "color: #FF5555"
        elif v > 6: return "color: #FFB800"
        return "color: #00FF90"
    return ""

st.dataframe(
    df_macro.style
        .map(style_gdp, subset=["GDP Growth (%)"])
        .map(style_cpi, subset=["CPI Inflation (%)"])
        .set_properties(**{"background-color": "#0A1828", "color": "#C8D8E8", "border": "1px solid rgba(0,212,255,0.1)"})
        .set_table_styles([
            {"selector": "th", "props": [("background-color","rgba(0,212,255,0.08)"),
                                          ("color","#00D4FF"),("font-family","monospace"),
                                          ("font-size","0.72rem"),("letter-spacing","0.08em")]},
        ]),
    use_container_width=True, hide_index=True,
)

st.markdown("<br>", unsafe_allow_html=True)
mphase1, mphase2, mphase3 = st.columns(3)
for col, (color, title, metrics, text) in zip([mphase1,mphase2,mphase3], [
    (RED,"2022: Sanctions Shock","−1.2% GDP | 11.9% CPI","SWIFT ban + $300B reserve freeze + FDI collapse. Classical models predicted system failure. Emergency capital controls and SPFS activation prevented collapse. Ruble devaluation cushion transferred shock to civilian purchasing power."),
    (AMBER,"2023–2024: War Economy Boom","3.6% → 4.9% GDP","Militarised Keynesianism: state-directed ruble injections into domestic factories created full employment and record nominal wages. Industrial sector reached capacity. 4.9% growth in 2024 exceeded all Western analyst projections."),
    (CYAN,"2026–2030: Institutionalization","0.4% → 2.5% GDP Target","Physical labor/machine limit hit in 2026. CBR dropped rate from 21% to 14.5%. Technology ceiling from microchip restrictions limits real GDP to 0.4%. Gradual rate easing toward 8–10% targets sustainable recovery."),
]):
    with col:
        st.markdown(f'''<div class="gc" style="border-top:2px solid {color}; min-height:180px;">
            <div style="color:{color};font-size:0.65rem;font-weight:700;letter-spacing:0.1em;margin-bottom:4px;">{metrics}</div>
            <div style="color:#E8F4FF;font-weight:700;font-size:0.88rem;margin-bottom:10px;">{title}</div>
            <div style="color:#3A5A70;font-size:0.78rem;line-height:1.65;">{text}</div>
        </div>''', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# EURASIAN FINANCIAL ORDER
# ══════════════════════════════════════════════════════════════════════
st.markdown('<div class="sep"><div class="sep-line"></div><div class="sep-diamond"></div><div class="sep-line"></div></div>', unsafe_allow_html=True)
st.markdown('<span id="eurasian"></span>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <div class="section-tag">▸ MODULE 09 — STRATEGIC GEOPOLITICAL INTELLIGENCE</div>
    <div class="section-title">The New Eurasian Financial Order</div>
    <div class="section-summary">
        Russia did not merely survive — it built a parallel financial world with South Ossetia, CIS card pipelines, and direct CNY clearing channels.
        European nations paid enormous political capital to isolate Russia, then purchased the same energy back from Indian and Turkish refineries at a premium.
        Global trade fragmentation makes top-down financial containment completely ineffective.
    </div>
</div>
""", unsafe_allow_html=True)

eu1, eu2, eu3, eu4 = st.columns(4)
for col, (v,l,c) in zip([eu1,eu2,eu3,eu4],[
    ("SPFS","Russian SWIFT Alternative","red"), ("CNY","Primary Reserve Replacement","amber"),
    ("6","Alternative Corridors Mapped",""), ("Irreversible","Fragmentation Assessment","red"),
]):
    with col:
        st.markdown(f'<div class="kpi-wrap {c}"><div class="kpi-v" style="font-size:1.2rem;">{v}</div><div class="kpi-l">{l}</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
geo_col, geo_info = st.columns([3, 2])

with geo_col:
    geo_nodes = {
        "Russia":(55.75,37.62,RED,20),
        "China":(39.9,116.4,BLUE,18),
        "India":(28.6,77.2,BLUE,14),
        "Turkey":(41.0,28.9,AMBER,14),
        "Kazakhstan":(51.2,71.5,GREEN,12),
        "Kyrgyzstan":(42.87,74.59,GREEN,12),
        "Armenia":(40.18,44.51,GREEN,10),
        "Belarus":(53.9,27.57,GREEN,10),
        "UAE":(25.2,55.3,GREY,10),
        "Serbia":(44.8,20.5,AMBER,9),
        "Hungary":(47.5,19.0,AMBER,9),
    }
    geo_routes = [
        ("Russia","China",BLUE,4,"CNY Direct Clearing"),
        ("Russia","Turkey",AMBER,3,"TurkStream + Energy"),
        ("Russia","India",BLUE,3,"Crude Oil Supply"),
        ("Russia","Kazakhstan",GREEN,3,"EAEU Corridor"),
        ("Russia","Belarus",GREEN,3,"Union State"),
        ("Russia","Kyrgyzstan",GREEN,2,"Card Tourism + Crypto"),
        ("Russia","Armenia",GREEN,2,"Evocabank Pipeline"),
        ("Russia","UAE",GREY,2,"VPN / Gold Hub"),
        ("Turkey","Serbia",AMBER,2,"TurkStream"),
        ("China","Kyrgyzstan",GREEN,1.5,"Regional Bank Integration"),
    ]
    fig_geo = go.Figure()
    for src,tgt,color,w,lbl in geo_routes:
        lat0,lon0 = geo_nodes[src][:2]
        lat1,lon1 = geo_nodes[tgt][:2]
        fig_geo.add_trace(go.Scattergeo(lat=[lat0,lat1],lon=[lon0,lon1],mode="lines",
                                         line=dict(width=w,color=color),
                                         hoverinfo="text",text=lbl,showlegend=False))
    for name,(lat,lon,color,size) in geo_nodes.items():
        fig_geo.add_trace(go.Scattergeo(
            lat=[lat],lon=[lon],mode="markers+text",
            marker=dict(size=size,color=color,line=dict(width=1.5,color="#E8F4FF")),
            text=[name],textposition="top right",textfont=dict(color="#C8D8E8",size=8),
            hovertemplate=f"<b>{name}</b><extra></extra>",showlegend=False,
        ))
    fig_geo.update_layout(
        geo=dict(showland=True,landcolor="#0A1828",showocean=True,oceancolor="#020B18",
                 showcoastlines=True,coastlinecolor="#1A2A3A",showcountries=True,countrycolor="#0D1E30",
                 showframe=False,projection_type="natural earth",bgcolor="#050B18",
                 center=dict(lat=42,lon=62),projection_scale=2.8,showlakes=False),
        paper_bgcolor=PAPER, font=dict(color=FC),
        margin=dict(l=0,r=0,t=10,b=0), height=450,
    )
    st.plotly_chart(fig_geo, use_container_width=True)

with geo_info:
    for (color, title, desc) in [
        (BLUE,"🇨🇳 Russia–China CNY Axis","Direct ruble-to-yuan clearing eliminates USD/SWIFT dependency. Thousands of Chinese intermediaries enable luxury goods, technology, and industrial supply outside Western compliance."),
        (AMBER,"🇹🇷 Russia–Turkey Energy Bridge","TurkStream + Tupras refinery creates the refining laundering loop. Turkey remains NATO member, creating unprecedented enforcement complexity for Western policymakers."),
        (GREEN,"🇰🇬 CIS Card Pipeline Network","Kyrgyzstan + Armenia + Belarus: three-node retail banking gateway maintaining full international purchasing capability for ordinary Russian citizens."),
        (GREY,"🏴 Unrecognized Territory Network","South Ossetia + Abkhazia + Transnistria: zero-BIS-oversight cut-outs. Funds flow invisibly, financing trade outside all international compliance frameworks."),
        (RED,"⛏️ Digital Asset Corridor","Siberian mining + Kyrgyzstan hub ($31B) = fully autonomous liquidity generation engine outside the dollar system and all Western monitoring."),
    ]:
        st.markdown(f'<div class="ic" style="border-left-color:{color}"><h5 style="color:{color};">{title}</h5><p>{desc}</p></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
rub_col1, rub_col2 = st.columns(2)
with rub_col1:
    st.markdown("""
    <div class="gc">
        <div style="font-family:'Share Tech Mono',monospace; color:#00D4FF; font-size:0.62rem; letter-spacing:0.2em; margin-bottom:14px;">▸ THE RUBLE DEVALUATION CUSHION — FISCAL STABILIZER MODEL</div>
        <div style="color:#5A7A8A; font-size:0.85rem; line-height:1.85;">
        Russia's fiscal architecture exploits a <strong style="color:#E8F4FF;">currency conversion arbitrage model</strong>:
        <br><br>
        <strong style="color:#00D4FF;">REVENUE:</strong> Energy export taxes collected in CNY/USD (foreign reserve currencies)<br>
        <strong style="color:#FF5555;">EXPENDITURE:</strong> All government spending — defense, wages, procurement — paid in RUB<br><br>
        <strong style="color:#FFB800;">THE MECHANISM:</strong> If foreign inflows fall, the CBR allows ruble depreciation.
        Domestic budget value in rubles increases even as foreign asset value decreases — maintaining fiscal stability.<br><br>
        <strong style="color:#FF5555;">THE COST:</strong> The devaluation bonus is a transfer of purchasing power from civilians
        to the state — manifesting as structural inflation. A hidden tax on the population.
        </div>
    </div>
    """, unsafe_allow_html=True)

with rub_col2:
    yrs_rub = [2022,2023,2024,2025,2026,2027,2028,2029,2030]
    rub_rate = [70,90,88,92,88,82,78,75,72]
    pwr_idx = [100,88,84,82,80,83,85,87,89]
    fig_rub = go.Figure()
    fig_rub.add_trace(go.Scatter(x=yrs_rub,y=rub_rate,mode="lines+markers",name="USD/RUB Rate",
                                  line=dict(color=RED,width=2.5),marker=dict(size=7)))
    fig_rub.add_trace(go.Scatter(x=yrs_rub,y=pwr_idx,mode="lines+markers",name="Purchasing Power Index (2022=100)",
                                  line=dict(color=CYAN,width=2.5,dash="dot"),marker=dict(size=7),yaxis="y2"))
    fig_rub.update_layout(**cl(
        title=dict(text="Ruble Rate vs Civilian Purchasing Power — 2022–2030", font=dict(size=11,color="#6A8FA8"), x=0),
        yaxis=dict(color=RED,showgrid=True,gridcolor=GRID,title="RUB per USD"),
        yaxis2=dict(overlaying="y",side="right",color=CYAN,title="Purchasing Power",showgrid=False),
        xaxis=dict(color="#4A6A80",showgrid=False), height=300,
    ))
    st.plotly_chart(fig_rub, use_container_width=True)

# ══════════════════════════════════════════════════════════════════════
# RESEARCH METHODOLOGY
# ══════════════════════════════════════════════════════════════════════
st.markdown('<div class="sep"><div class="sep-line"></div><div class="sep-diamond"></div><div class="sep-line"></div></div>', unsafe_allow_html=True)
st.markdown('<span id="methodology"></span>', unsafe_allow_html=True)
st.markdown("""
<div class="section-header">
    <div class="section-tag">▸ MODULE 10 — RESEARCH METHODOLOGY & PUBLICATION</div>
    <div class="section-title">Research Framework & Academic References</div>
    <div class="section-summary">
        Empirical case studies combined with macroeconomic modeling. Data period: 2022–2026 (actual) + 2027–2030 (CBR official baseline projections).
        12 primary sources from BIS, CBR, CREA, EDB, Eurostat, NBKR, OFAC, CSIS, Reuters, FT, and AUTOSTAT.
    </div>
</div>
""", unsafe_allow_html=True)

meth1, meth2 = st.columns(2)
with meth1:
    st.markdown('<div style="font-family:\'Share Tech Mono\',monospace; color:#00D4FF; font-size:0.62rem; letter-spacing:0.22em; margin-bottom:14px;">▸ PUBLICATION METADATA</div>', unsafe_allow_html=True)
    meta = [
        ("Title","Double-Headed Growth: Evaluating Russia's Sanction Evasion Networks, Asymmetric Geopolitical Re-Routing, and Banking Loopholes"),
        ("Author","Makhzumul Islam Mahdi"),
        ("Year","2026"),
        ("ORCID","0009-0007-1769-7771"),
        ("WoS ResearcherID","OOO-0072-2025"),
        ("Figshare","/authors/Makhzumul_Mahdi/22543814"),
        ("Domain","International Economics · Geopolitical Finance · Sanctions Studies"),
        ("Methodology","Empirical Case Studies + Macroeconomic Modeling + Network Analysis"),
        ("Data Period","2022–2026 (Empirical) + 2027–2030 (CBR Projections)"),
        ("Classification","Unclassified Academic Research"),
    ]
    for k, v in meta:
        st.markdown(f'<div style="display:flex;gap:12px;padding:8px 0;border-bottom:1px solid rgba(0,212,255,0.07);"><span style="color:#2A4050;font-size:0.78rem;min-width:130px;font-family:\'Share Tech Mono\',monospace;">{k}</span><span style="color:#C8D8E8;font-size:0.78rem;">{v}</span></div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div style="font-family:\'Share Tech Mono\',monospace; color:#00D4FF; font-size:0.62rem; letter-spacing:0.22em; margin-bottom:14px; margin-top:8px;">▸ COINED CONCEPTS</div>', unsafe_allow_html=True)
    for (color, term, defn) in [
        (RED,"Double-Headed Growth","A large sanctioned economy develops two parallel monetary engines: state-directed domestic capital rationing and an adaptive grey economy. Neither head can function without the other."),
        (AMBER,"Card Tourism","Russian citizens open foreign bank accounts via CIS agents to maintain international payment card access — circumventing international card bans through legal account ownership in non-sanctioned jurisdictions."),
        (CYAN,"Refining Laundering","Converting sanctioned crude oil into 'neutral' refined products via third-country refineries for legal re-export to the same nations that imposed the original ban — at premium prices."),
    ]:
        st.markdown(f'<div class="gc" style="border-top:2px solid {color}; margin-bottom:8px;"><div style="color:{color};font-weight:700;font-size:0.82rem;margin-bottom:5px;">{term}</div><div style="color:#3A5A70;font-size:0.76rem;line-height:1.55;">{defn}</div></div>', unsafe_allow_html=True)

with meth2:
    st.markdown('<div style="font-family:\'Share Tech Mono\',monospace; color:#00D4FF; font-size:0.62rem; letter-spacing:0.22em; margin-bottom:14px;">▸ ACADEMIC REFERENCES</div>', unsafe_allow_html=True)
    refs = [
        ("01",CYAN,"Bank for International Settlements (BIS)","BIS Quarterly Review and Cross-Border Banking Statistics","Basel: BIS, 2025"),
        ("02",RED,"Bank of Russia (CBR)","Development of the Financial Messaging System (SPFS)","Moscow: CBR, 2025"),
        ("03",RED,"Bank of Russia (CBR)","Macroeconomic Baseline Projections and Key Interest Rate Reports","Moscow: CBR, 2026"),
        ("04",GREEN,"CREA — Centre for Research on Energy and Clean Air","Russia Fossil Fuel Tracker and Refining Loophole Analysis","Helsinki: CREA, 2026"),
        ("05",GREEN,"Central Bank of Armenia (CBA)","Financial Stability Report","Yerevan: CBA, 2026"),
        ("06",AMBER,"Eurasian Development Bank (EDB)","Macroeconomic Review: Structural Changes in CIS Banking and Remittance Flows","Almaty: EDB, 2026"),
        ("07",CYAN,"Eurostat Trade Database","International Trade in Goods Statistics and Eurasian Transit Flows","Brussels: European Commission, 2025"),
        ("08",GREEN,"National Bank of Kyrgyz Republic (NBKR)","International Settlement Dynamics and Financial Statistics","Bishkek: NBKR, 2026"),
        ("09",RED,"U.S. Dept of Treasury — OFAC","Treasury Sanctions Russian Financial Networks Facilitating Procurement Platforms","Washington D.C.: OFAC, 2024"),
        ("10",CYAN,"Center for Strategic & International Studies (CSIS)","FinTech Sanctions Circumvention and Cross-Border Banking Networks in Eurasia","Washington D.C.: CSIS, 2025"),
        ("11",GREY,"Reuters Investigations","Russian Parallel Imports and Maritime Sanctions Evasion Networks","Reuters Global Investigations, 2025"),
        ("12",GREY,"Financial Times","Shadow Fleet Logistics and Russian Energy Re-Routing Mechanisms","London: FT, 2025"),
    ]
    for num, color, author, title, source in refs:
        st.markdown(f'''<div style="background:rgba(0,8,20,0.7); border:1px solid rgba(0,212,255,0.08);
             border-left:3px solid {color}; border-radius:0 6px 6px 0;
             padding:10px 14px; margin-bottom:7px;">
            <div style="font-family:'Share Tech Mono',monospace; color:#2A4050; font-size:0.65rem;">[{num}] {author}</div>
            <div style="color:#C8D8E8; font-size:0.8rem; font-weight:600; margin:2px 0;">{title}</div>
            <div style="color:#1A3040; font-size:0.72rem;">{source}</div>
        </div>''', unsafe_allow_html=True)

# ══════════════════════════════════════════════════════════════════════
# FOOTER
# ══════════════════════════════════════════════════════════════════════
st.markdown("""
<div class="platform-footer">
    <div class="footer-title">⚡ DOUBLE-HEADED GROWTH INTELLIGENCE PLATFORM</div>
    <div class="footer-sub">
        RESEARCH BY MAKHZUMUL ISLAM MAHDI · ORCID: 0009-0007-1769-7771 · YEAR: 2026<br>
        FOR ACADEMIC AND POLICY RESEARCH PURPOSES ONLY · DATA: 2022–2026 EMPIRICAL + 2027–2030 CBR PROJECTIONS<br>
        SOURCES: BIS · CBR · CREA · EDB · EUROSTAT · NBKR · OFAC · CSIS · REUTERS · FT · AUTOSTAT
    </div>
</div>
""", unsafe_allow_html=True)
