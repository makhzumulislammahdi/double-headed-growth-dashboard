import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(page_title="Energy Revenue Analytics | Intelligence Platform", page_icon="⚡", layout="wide")

st.markdown("""
<style>
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0D1117 0%, #161B22 100%); border-right: 1px solid #30363D; }
    .section-header { color:#8B949E; font-size:0.7rem; letter-spacing:0.18em; text-transform:uppercase; border-bottom:1px solid #30363D; padding-bottom:6px; margin-bottom:16px; }
    .kpi-card { background:#161B22; border:1px solid #30363D; border-top:3px solid #C41E3A; border-radius:8px; padding:20px 16px; text-align:center; }
    .kpi-value { font-size:1.7rem; font-weight:800; color:#E6EDF3; }
    .kpi-label { font-size:0.72rem; color:#8B949E; letter-spacing:0.08em; text-transform:uppercase; margin-top:6px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<span style="color:#C41E3A;font-size:0.7rem;letter-spacing:0.15em;font-weight:700;">MODULE 05</span>', unsafe_allow_html=True)
st.markdown('<h1 style="color:#E6EDF3; font-size:1.6rem; font-weight:800; margin:0;">⚡ Energy Revenue Analytics</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#8B949E; font-size:0.9rem; margin:4px 0 24px 0;">Fossil Fuel Export Intelligence · Revenue Trends · Trade Partner Analysis · 2030 Forecast Models</p>', unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns(4)
kpis_top = [
    ("€1.075T", "Total Fossil Revenue Since 2022", "#C41E3A"),
    ("€231B", "EU Share of Russian Energy", "#D29922"),
    ("€567M", "Feb 2026 Refinery Laundering", "#1F6FEB"),
    ("93%", "Hungary Oil Dependency 2025", "#C41E3A"),
]
for col, (val, label, color) in zip([c1,c2,c3,c4], kpis_top):
    with col:
        st.markdown(f"""<div class="kpi-card" style="border-top-color:{color}">
            <div class="kpi-value">{val}</div>
            <div class="kpi-label">{label}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="section-header">ANNUAL ENERGY EXPORT REVENUE (2022–2026) — €BILLION</div>', unsafe_allow_html=True)
    years = [2022, 2023, 2024, 2025, 2026]
    total_rev = [328, 265, 230, 195, 175]
    eu_rev = [85, 65, 52, 41, 38]
    non_eu = [243, 200, 178, 154, 137]
    fig_rev = go.Figure()
    fig_rev.add_trace(go.Bar(name="Non-EU Revenue (CNY/USD)", x=years, y=non_eu,
                             marker_color="#1F6FEB", text=[f"€{v}B" for v in non_eu],
                             textposition="inside", textfont=dict(color="white", size=9)))
    fig_rev.add_trace(go.Bar(name="EU Revenue (via refining laundering)", x=years, y=eu_rev,
                             marker_color="#C41E3A", text=[f"€{v}B" for v in eu_rev],
                             textposition="inside", textfont=dict(color="white", size=9)))
    fig_rev.add_trace(go.Scatter(name="Total Revenue", x=years, y=total_rev,
                                 mode="lines+markers", line=dict(color="#D29922", width=2),
                                 marker=dict(color="#D29922", size=7),
                                 yaxis="y2"))
    fig_rev.update_layout(
        plot_bgcolor="#0D1117", paper_bgcolor="#161B22",
        font=dict(color="#E6EDF3"), barmode="stack",
        yaxis=dict(color="#8B949E", showgrid=True, gridcolor="#21262D",
                   title="€ Billion", tickprefix="€", ticksuffix="B"),
        yaxis2=dict(overlaying="y", side="right", color="#D29922",
                    title="Total (€B)", showgrid=False),
        xaxis=dict(color="#8B949E"),
        legend=dict(font=dict(color="#8B949E", size=9), bgcolor="#161B22", bordercolor="#30363D"),
        margin=dict(l=10, r=10, t=10, b=10), height=320,
    )
    st.plotly_chart(fig_rev, use_container_width=True)

with col2:
    st.markdown('<div class="section-header">ENERGY TRADE PARTNERS — MARKET SHARE 2026</div>', unsafe_allow_html=True)
    partners = ["China", "India", "Turkey", "Belarus", "Hungary", "Serbia", "Other CIS", "Other"]
    shares = [32, 22, 15, 8, 6, 4, 7, 6]
    colors_pie = ["#1F6FEB", "#3FB950", "#D29922", "#3FB950", "#C41E3A", "#C41E3A", "#8B949E", "#484F58"]
    fig_pie = go.Figure(go.Pie(
        labels=partners, values=shares,
        marker=dict(colors=colors_pie, line=dict(color="#0D1117", width=2)),
        textfont=dict(color="#E6EDF3", size=11),
        hovertemplate="<b>%{label}</b><br>%{value}% market share<extra></extra>",
        hole=0.4,
    ))
    fig_pie.update_layout(
        paper_bgcolor="#161B22",
        font=dict(color="#E6EDF3"),
        legend=dict(font=dict(color="#8B949E", size=10), bgcolor="#161B22"),
        margin=dict(l=10, r=10, t=10, b=10), height=320,
        annotations=[dict(text="Trade<br>Partners", x=0.5, y=0.5,
                          font=dict(size=12, color="#E6EDF3"), showarrow=False)],
    )
    st.plotly_chart(fig_pie, use_container_width=True)

st.markdown("---")
col3, col4 = st.columns(2)

with col3:
    st.markdown('<div class="section-header">ENERGY REVENUE FORECAST 2026–2030 (€BILLION)</div>', unsafe_allow_html=True)
    years_f = [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
    actual = [328, 265, 230, 195, 175, None, None, None, None]
    forecast = [None, None, None, None, 175, 168, 163, 158, 155]
    fig_fore = go.Figure()
    fig_fore.add_trace(go.Scatter(x=years_f, y=actual, mode="lines+markers",
                                   name="Actual Revenue", line=dict(color="#1F6FEB", width=3),
                                   marker=dict(size=7, color="#1F6FEB"), connectgaps=False))
    fig_fore.add_trace(go.Scatter(x=years_f, y=forecast, mode="lines+markers",
                                   name="Forecast", line=dict(color="#C41E3A", width=2, dash="dash"),
                                   marker=dict(size=7, color="#C41E3A"), connectgaps=False))
    fig_fore.add_vrect(x0=2026, x1=2030, fillcolor="rgba(196,30,58,0.05)",
                        line_width=0, annotation_text="FORECAST PERIOD",
                        annotation_font=dict(color="#8B949E", size=9))
    fig_fore.update_layout(
        plot_bgcolor="#0D1117", paper_bgcolor="#161B22",
        font=dict(color="#E6EDF3"),
        yaxis=dict(color="#8B949E", showgrid=True, gridcolor="#21262D",
                   tickprefix="€", ticksuffix="B"),
        xaxis=dict(color="#8B949E", showgrid=False),
        legend=dict(font=dict(color="#8B949E", size=10), bgcolor="#161B22"),
        margin=dict(l=10, r=10, t=10, b=10), height=280,
    )
    st.plotly_chart(fig_fore, use_container_width=True)

with col4:
    st.markdown('<div class="section-header">MONTHLY REFINERY LAUNDERING — 2025–2026 (€MILLION)</div>', unsafe_allow_html=True)
    months = ["Aug'25","Sep'25","Oct'25","Nov'25","Dec'25","Jan'26","Feb'26"]
    refinery_exports = [420, 445, 480, 510, 495, 530, 567]
    colors_m = ["#484F58"] * 6 + ["#C41E3A"]
    fig_monthly = go.Figure(go.Bar(
        x=months, y=refinery_exports,
        marker_color=colors_m,
        text=[f"€{v}M" for v in refinery_exports],
        textposition="outside",
        textfont=dict(color="#E6EDF3", size=10),
        hovertemplate="<b>%{x}</b><br>€%{y}M<extra></extra>",
    ))
    fig_monthly.add_annotation(x="Feb'26", y=567, text="Peak: €567M",
                                showarrow=True, arrowhead=2, arrowcolor="#C41E3A",
                                font=dict(color="#C41E3A", size=10),
                                ax=-60, ay=-30)
    fig_monthly.update_layout(
        plot_bgcolor="#0D1117", paper_bgcolor="#161B22",
        font=dict(color="#E6EDF3"),
        yaxis=dict(color="#8B949E", showgrid=True, gridcolor="#21262D",
                   tickprefix="€", ticksuffix="M"),
        xaxis=dict(color="#8B949E"),
        margin=dict(l=10, r=10, t=10, b=10), height=280,
        showlegend=False,
    )
    st.plotly_chart(fig_monthly, use_container_width=True)

st.markdown("---")
st.markdown('<div class="section-header">ENERGY REVENUE INTELLIGENCE COMMENTARY</div>', unsafe_allow_html=True)
commentary_cols = st.columns(3)
commentary = [
    ("#1F6FEB", "€1.075 Trillion Milestone",
     "Since the start of the conflict, Russia has earned over €1.075 trillion in fossil fuel revenue. EU countries — despite official bans — account for €231 billion of this total, purchasing refined Russian energy via Turkish and Indian intermediaries."),
    ("#D29922", "The Refining Laundering Loop",
     "Russia exports crude to Turkey (Tupras) and India (Jamnagar/Reliance). These refineries convert it into diesel and jet fuel legally reclassified as 'Turkish' or 'Indian' product. In February 2026 alone, €567M of this product was sold back to sanctioning EU states."),
    ("#3FB950", "Rebel Buyers Sustain Revenue",
     "Hungary (93% dependency), Serbia (TurkStream), and other EU members continue direct Russian energy imports through pipeline exemptions and back-channel agreements. This structural dependency makes energy revenue effectively uncollapsible via unilateral bans."),
]
for col, (color, title, text) in zip(commentary_cols, commentary):
    with col:
        st.markdown(f"""<div style="background:#161B22; border:1px solid #30363D; border-top:3px solid {color};
             border-radius:8px; padding:18px; min-height:170px;">
            <div style="color:#E6EDF3; font-weight:700; font-size:0.9rem; margin-bottom:10px;">{title}</div>
            <div style="color:#8B949E; font-size:0.8rem; line-height:1.65;">{text}</div>
        </div>""", unsafe_allow_html=True)

st.markdown('<div style="text-align:center; color:#484F58; font-size:0.75rem; padding:20px 0 4px 0; border-top:1px solid #21262D; margin-top:32px;">Double-Headed Growth Intelligence Platform · Module 05 · Energy Revenue Analytics · Source: CREA, Eurostat, Bank of Russia</div>', unsafe_allow_html=True)
