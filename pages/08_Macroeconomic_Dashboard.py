import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import numpy as np

st.set_page_config(page_title="Macroeconomic Dashboard | Intelligence Platform", page_icon="📊", layout="wide")

st.markdown("""
<style>
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0D1117 0%, #161B22 100%); border-right: 1px solid #30363D; }
    .section-header { color:#8B949E; font-size:0.7rem; letter-spacing:0.18em; text-transform:uppercase; border-bottom:1px solid #30363D; padding-bottom:6px; margin-bottom:16px; }
    .kpi-card { background:#161B22; border:1px solid #30363D; border-top:3px solid #C41E3A; border-radius:8px; padding:20px 16px; text-align:center; }
    .kpi-value { font-size:1.7rem; font-weight:800; color:#E6EDF3; }
    .kpi-label { font-size:0.72rem; color:#8B949E; letter-spacing:0.08em; text-transform:uppercase; margin-top:6px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<span style="color:#C41E3A;font-size:0.7rem;letter-spacing:0.15em;font-weight:700;">MODULE 08</span>', unsafe_allow_html=True)
st.markdown('<h1 style="color:#E6EDF3; font-size:1.6rem; font-weight:800; margin:0;">📊 Macroeconomic Dashboard</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#8B949E; font-size:0.9rem; margin:4px 0 24px 0;">GDP Growth Analysis · Inflation Trends · Interest Rate Policy · 2030 Economic Forecasts</p>', unsafe_allow_html=True)

# Data from the paper
years_all = [2022, 2023, 2024, 2025, 2026, 2027, 2028, 2029, 2030]
gdp = [-1.2, 3.6, 4.9, 1.0, 0.4, 1.4, 1.9, 2.4, 2.5]
cpi = [11.9, 7.4, 5.9, 5.6, 5.2, 4.0, 4.0, 4.0, 4.0]
interest_rate = [20.0, 16.0, 18.0, 21.0, 14.5, 10.5, 8.5, 8.0, 8.0]

actual_cut = 5  # Up to and including 2026 index

c1, c2, c3, c4 = st.columns(4)
kpis = [
    ("0.4%", "GDP Growth 2026", "#D29922"),
    ("5.2%", "CPI Inflation 2026", "#1F6FEB"),
    ("14.5%", "Key Interest Rate 2026", "#C41E3A"),
    ("2.5%", "Projected GDP 2030", "#3FB950"),
]
for col, (val, label, color) in zip([c1, c2, c3, c4], kpis):
    with col:
        st.markdown(f"""<div class="kpi-card" style="border-top-color:{color}">
            <div class="kpi-value">{val}</div>
            <div class="kpi-label">{label}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-header">GDP GROWTH & INFLATION — 2022 TO 2030 (WITH FORECAST)</div>', unsafe_allow_html=True)

fig_main = go.Figure()

# GDP actual
fig_main.add_trace(go.Scatter(
    x=years_all[:actual_cut], y=gdp[:actual_cut],
    mode="lines+markers",
    name="GDP Growth (Actual)",
    line=dict(color="#1F6FEB", width=3),
    marker=dict(size=8, color="#1F6FEB", line=dict(color="#E6EDF3", width=1)),
))
# GDP forecast
fig_main.add_trace(go.Scatter(
    x=years_all[actual_cut-1:], y=gdp[actual_cut-1:],
    mode="lines+markers",
    name="GDP Growth (Forecast)",
    line=dict(color="#1F6FEB", width=2, dash="dash"),
    marker=dict(size=7, color="#1F6FEB"),
))
# CPI actual
fig_main.add_trace(go.Scatter(
    x=years_all[:actual_cut], y=cpi[:actual_cut],
    mode="lines+markers",
    name="CPI Inflation (Actual)",
    line=dict(color="#C41E3A", width=3),
    marker=dict(size=8, color="#C41E3A", line=dict(color="#E6EDF3", width=1)),
    yaxis="y2",
))
# CPI forecast
fig_main.add_trace(go.Scatter(
    x=years_all[actual_cut-1:], y=cpi[actual_cut-1:],
    mode="lines+markers",
    name="CPI Inflation (Forecast)",
    line=dict(color="#C41E3A", width=2, dash="dash"),
    marker=dict(size=7, color="#C41E3A"),
    yaxis="y2",
))
# Interest rate
fig_main.add_trace(go.Bar(
    x=years_all, y=interest_rate,
    name="Key Interest Rate (%)",
    marker_color="rgba(210,153,34,0.3)",
    marker_line=dict(color="#D29922", width=1),
    yaxis="y2",
    opacity=0.6,
))

fig_main.add_vrect(x0=2026.4, x1=2030.4, fillcolor="rgba(255,255,255,0.02)",
                   line_width=0.5, line_color="#30363D",
                   annotation_text="FORECAST PERIOD (CBR Projections)",
                   annotation_font=dict(color="#8B949E", size=9),
                   annotation_position="top left")

# Annotations
fig_main.add_annotation(x=2024, y=4.9, text="Peak Growth\n4.9%", showarrow=True,
                          arrowhead=2, arrowcolor="#1F6FEB", font=dict(color="#1F6FEB", size=9),
                          ax=30, ay=-30)
fig_main.add_annotation(x=2022, y=11.9, text="Sanctions Shock\n11.9%", showarrow=True,
                          arrowhead=2, arrowcolor="#C41E3A", font=dict(color="#C41E3A", size=9),
                          yref="y2", ax=40, ay=-20)

fig_main.update_layout(
    plot_bgcolor="#0D1117", paper_bgcolor="#161B22",
    font=dict(color="#E6EDF3"),
    yaxis=dict(color="#1F6FEB", showgrid=True, gridcolor="#21262D",
               title="GDP Growth (%)", ticksuffix="%", zeroline=True, zerolinecolor="#30363D"),
    yaxis2=dict(overlaying="y", side="right", color="#C41E3A",
                title="CPI / Interest Rate (%)", showgrid=False, ticksuffix="%"),
    xaxis=dict(color="#8B949E", showgrid=False, dtick=1),
    legend=dict(font=dict(color="#8B949E", size=9), bgcolor="#161B22", bordercolor="#30363D",
                orientation="h", yanchor="bottom", y=1.02),
    margin=dict(l=10, r=10, t=40, b=10), height=380,
)
st.plotly_chart(fig_main, use_container_width=True)

st.markdown("---")

# Data table
st.markdown('<div class="section-header">FULL MACROECONOMIC DATA TABLE (2022–2030)</div>', unsafe_allow_html=True)
df_table = pd.DataFrame({
    "Year": years_all,
    "GDP Growth (%)": gdp,
    "CPI Inflation (%)": cpi,
    "Key Interest Rate (%)": interest_rate,
    "Status": ["Actual"]*5 + ["Forecast (CBR)"]*4
})

def color_gdp(val):
    if isinstance(val, float):
        if val < 0: return "color: #C41E3A"
        elif val < 1.5: return "color: #D29922"
        else: return "color: #3FB950"
    return ""

def color_cpi(val):
    if isinstance(val, float):
        if val > 10: return "color: #C41E3A"
        elif val > 6: return "color: #D29922"
        else: return "color: #3FB950"
    return ""

st.dataframe(
    df_table.style
        .applymap(color_gdp, subset=["GDP Growth (%)"])
        .applymap(color_cpi, subset=["CPI Inflation (%)"])
        .set_properties(**{"background-color": "#161B22", "color": "#E6EDF3",
                           "border": "1px solid #30363D"})
        .set_table_styles([
            {"selector": "th", "props": [("background-color", "#21262D"),
                                          ("color", "#8B949E"),
                                          ("font-size", "0.75rem"),
                                          ("letter-spacing", "0.08em")]},
            {"selector": "td", "props": [("font-size", "0.85rem")]},
        ]),
    use_container_width=True, hide_index=True
)

st.markdown("<br>", unsafe_allow_html=True)
col_phases = st.columns(3)
phases = [
    ("#C41E3A", "2022: Sanctions Shock", "-1.2% GDP | 11.9% CPI",
     "SWIFT ban, $300B reserve freeze, FDI collapse. Classic financial model predicted system collapse. Economy contracted but avoided collapse via emergency capital controls and SPFS activation."),
    ("#D29922", "2023–2024: War Economy Boom", "3.6% → 4.9% GDP",
     "Militarised Keynesianism: state-directed ruble injections into domestic factories created full employment boom. Record nominal wages. Industrial sector at full capacity. 4.9% growth exceeded all Western projections."),
    ("#1F6FEB", "2026: Physical Limit Hit", "0.4% GDP | 14.5% Rate",
     "Economy reached labor and machine shortages. 21% emergency rate cooled markets; compromised to 14.5%. Technology ceiling from microchip restrictions slightly reduced real GDP. Now transitioning from crisis-avoidance to institutional stability."),
]
for col, (color, title, metrics, text) in zip(col_phases, phases):
    with col:
        st.markdown(f"""<div style="background:#161B22; border:1px solid #30363D; border-top:3px solid {color};
             border-radius:8px; padding:18px; min-height:180px;">
            <div style="color:{color}; font-size:0.68rem; font-weight:700; letter-spacing:0.1em; margin-bottom:4px;">{metrics}</div>
            <div style="color:#E6EDF3; font-weight:700; font-size:0.9rem; margin-bottom:10px;">{title}</div>
            <div style="color:#8B949E; font-size:0.78rem; line-height:1.65;">{text}</div>
        </div>""", unsafe_allow_html=True)

st.markdown('<div style="text-align:center; color:#484F58; font-size:0.75rem; padding:20px 0 4px 0; border-top:1px solid #21262D; margin-top:32px;">Double-Headed Growth Intelligence Platform · Module 08 · Macroeconomic Dashboard · Source: Bank of Russia, CBR Baseline Projections 2026</div>', unsafe_allow_html=True)
