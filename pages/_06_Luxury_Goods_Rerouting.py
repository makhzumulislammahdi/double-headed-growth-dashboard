import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Luxury Goods Re-Routing | Intelligence Platform", page_icon="🚗", layout="wide")

st.markdown("""
<style>
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0D1117 0%, #161B22 100%); border-right: 1px solid #30363D; }
    .section-header { color:#8B949E; font-size:0.7rem; letter-spacing:0.18em; text-transform:uppercase; border-bottom:1px solid #30363D; padding-bottom:6px; margin-bottom:16px; }
    .kpi-card { background:#161B22; border:1px solid #30363D; border-top:3px solid #C41E3A; border-radius:8px; padding:20px 16px; text-align:center; }
    .kpi-value { font-size:1.7rem; font-weight:800; color:#E6EDF3; }
    .kpi-label { font-size:0.72rem; color:#8B949E; letter-spacing:0.08em; text-transform:uppercase; margin-top:6px; }
    .flow-step { background:#161B22; border:1px solid #30363D; border-radius:8px; padding:18px; text-align:center; position:relative; }
</style>
""", unsafe_allow_html=True)

st.markdown('<span style="color:#C41E3A;font-size:0.7rem;letter-spacing:0.15em;font-weight:700;">MODULE 06</span>', unsafe_allow_html=True)
st.markdown('<h1 style="color:#E6EDF3; font-size:1.6rem; font-weight:800; margin:0;">🚗 Luxury Goods Re-Routing Network</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#8B949E; font-size:0.9rem; margin:4px 0 24px 0;">Supply Chain Intelligence · G-Wagon Pipeline · Chinese Middleman Network · Parallel Import Analysis</p>', unsafe_allow_html=True)

col_a, col_b, col_c, col_d = st.columns(4)
kpis = [
    ("G-Wagon", "Icon of Financial Rebellion", "#C41E3A"),
    ("Austria", "Single Source Factory (Magna Steyr, Graz)", "#1F6FEB"),
    ("China", "Reclassification Gateway", "#D29922"),
    ("'Used Car'", "Legal Status After Reclassification", "#3FB950"),
]
for col, (val, label, color) in zip([col_a, col_b, col_c, col_d], kpis):
    with col:
        st.markdown(f"""<div class="kpi-card" style="border-top-color:{color}">
            <div class="kpi-value" style="font-size:1.3rem;">{val}</div>
            <div class="kpi-label">{label}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-header">LUXURY VEHICLE TRANSSHIPMENT FLOW — AUSTRIA → CHINA → RUSSIA</div>', unsafe_allow_html=True)

flow_steps = st.columns(7)
steps = [
    ("🏭", "STAGE 1", "Austria\n(Magna Steyr)", "Manufacturing: G-Wagon produced at single Graz factory. No other global production site.", "#1F6FEB"),
    ("→", "", "", "", "#30363D"),
    ("🇨🇳", "STAGE 2", "China\n'Asian Market'", "New vehicles sold to qualified buyers in China, classified as 'for local Asian markets'. Fully legal export.", "#D29922"),
    ("→", "", "", "", "#30363D"),
    ("🔄", "STAGE 3", "Chinese Border\nZone", "Vehicles reclassified as 'pre-owned/used cars' by Chinese customs. New factory vehicles become used personal vehicles.", "#D29922"),
    ("→", "", "", "", "#30363D"),
    ("🇷🇺", "STAGE 4", "Russia\nShowrooms", "Vehicles pass Eurasian border controls with zero compliance risk. Classified as used personal vehicles — not factory-made. VPN systems fool European brand servers into providing cloud updates.", "#C41E3A"),
]
for col, (icon, stage, loc, desc, color) in zip(flow_steps, steps):
    with col:
        if stage == "":
            st.markdown(f'<div style="display:flex; align-items:center; justify-content:center; height:160px; font-size:1.5rem; color:#30363D;">→</div>', unsafe_allow_html=True)
        else:
            st.markdown(f"""<div style="background:#161B22; border:1px solid #30363D; border-top:3px solid {color};
                 border-radius:8px; padding:14px 10px; text-align:center; height:160px;">
                <div style="font-size:1.5rem; margin-bottom:6px;">{icon}</div>
                <div style="color:{color}; font-size:0.62rem; font-weight:700; letter-spacing:0.1em; margin-bottom:4px;">{stage}</div>
                <div style="color:#E6EDF3; font-size:0.78rem; font-weight:600; margin-bottom:6px; white-space:pre-line;">{loc}</div>
                <div style="color:#8B949E; font-size:0.7rem; line-height:1.4;">{desc}</div>
            </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col_chart1, col_chart2 = st.columns(2)

with col_chart1:
    st.markdown('<div class="section-header">ASYMMETRIC VEHICLE TRANSSHIPMENT LOG (2022–2026)</div>', unsafe_allow_html=True)
    years = [2022, 2023, 2024, 2025, 2026]
    gwagon = [120, 890, 2100, 3400, 2800]
    porsche = [80, 540, 1200, 2100, 1900]
    bmw_x7 = [200, 1200, 2800, 4200, 3700]
    fig_veh = go.Figure()
    fig_veh.add_trace(go.Bar(name="Mercedes G-Wagon", x=years, y=gwagon,
                             marker_color="#C41E3A"))
    fig_veh.add_trace(go.Bar(name="Porsche 911/Cayenne", x=years, y=porsche,
                             marker_color="#D29922"))
    fig_veh.add_trace(go.Bar(name="BMW X7 / Audi EV", x=years, y=bmw_x7,
                             marker_color="#1F6FEB"))
    fig_veh.update_layout(
        plot_bgcolor="#0D1117", paper_bgcolor="#161B22",
        font=dict(color="#E6EDF3"), barmode="group",
        title=dict(text="Estimated Units Re-Routed via Chinese Middlemen", font=dict(size=11, color="#8B949E"), x=0),
        yaxis=dict(color="#8B949E", showgrid=True, gridcolor="#21262D", title="Units"),
        xaxis=dict(color="#8B949E"),
        legend=dict(font=dict(color="#8B949E", size=9), bgcolor="#161B22"),
        margin=dict(l=10, r=10, t=40, b=10), height=300,
    )
    st.plotly_chart(fig_veh, use_container_width=True)

with col_chart2:
    st.markdown('<div class="section-header">SUPPLY CHAIN NETWORK — SANKEY FLOW</div>', unsafe_allow_html=True)
    labels_lux = ["Austria (Magna Steyr)", "Germany (BMW/Porsche)", "China (Official Sale)", "Chinese Border Zone",
                  "Central Asian Transit", "Kazakhstan Transit", "Russia (Showrooms)", "Russia (Private Buyers)"]
    source_lux = [0, 1, 0, 1, 2, 2, 3, 3, 4, 5]
    target_lux = [2, 2, 2, 2, 3, 3, 6, 7, 6, 6]
    value_lux  = [40, 35, 40, 35, 45, 30, 35, 10, 25, 20]
    colors_lux = ["rgba(31,111,235,0.4)","rgba(31,111,235,0.4)","rgba(31,111,235,0.4)","rgba(31,111,235,0.4)",
                  "rgba(210,153,34,0.4)","rgba(210,153,34,0.4)",
                  "rgba(196,30,58,0.4)","rgba(196,30,58,0.4)","rgba(196,30,58,0.4)","rgba(196,30,58,0.4)"]
    fig_lux_sankey = go.Figure(go.Sankey(
        node=dict(
            pad=15, thickness=18,
            label=labels_lux,
            color=["#1F6FEB","#1F6FEB","#D29922","#D29922","#8B949E","#8B949E","#C41E3A","#C41E3A"],
            line=dict(color="#30363D", width=0.5),
            hovertemplate="%{label}<extra></extra>",
        ),
        link=dict(source=source_lux, target=target_lux, value=value_lux, color=colors_lux)
    ))
    fig_lux_sankey.update_layout(
        paper_bgcolor="#161B22",
        font=dict(color="#E6EDF3", size=10),
        margin=dict(l=10, r=10, t=10, b=10), height=300,
    )
    st.plotly_chart(fig_lux_sankey, use_container_width=True)

st.markdown("---")
st.markdown('<div class="section-header">THE VPN LOOPHOLE — DIGITAL SANCTIONS BYPASS</div>', unsafe_allow_html=True)
vpn_cols = st.columns(3)
vpn_info = [
    ("🔑", "The Problem", "#C41E3A",
     "European manufacturers (Mercedes-Benz, BMW, Porsche, Audi) encode geofencing into vehicle computer systems. Without European server cloud updates, modern luxury vehicles cannot function correctly in unauthorized markets."),
    ("🌐", "The Solution", "#D29922",
     "Russian tech networks rent VPN access from friendly cities — Dubai and Istanbul. Vehicle computers connect through these VPNs, fooling European central servers into treating Russian dealerships as authorized European service locations."),
    ("✅", "The Result", "#3FB950",
     "Cloud updates deploy normally. Warranty systems activate. Navigation, ADAS, and OTA updates function as if the vehicle is in Germany. The unilateral software blockade is completely neutralized by commercially available VPN infrastructure."),
]
for col, (icon, title, color, text) in zip(vpn_cols, vpn_info):
    with col:
        st.markdown(f"""<div style="background:#161B22; border:1px solid #30363D; border-top:3px solid {color};
             border-radius:8px; padding:20px; min-height:160px;">
            <div style="font-size:1.4rem; margin-bottom:8px;">{icon}</div>
            <div style="color:#E6EDF3; font-weight:700; font-size:0.9rem; margin-bottom:10px;">{title}</div>
            <div style="color:#8B949E; font-size:0.8rem; line-height:1.65;">{text}</div>
        </div>""", unsafe_allow_html=True)

st.markdown('<div style="text-align:center; color:#484F58; font-size:0.75rem; padding:20px 0 4px 0; border-top:1px solid #21262D; margin-top:32px;">Double-Headed Growth Intelligence Platform · Module 06 · Luxury Goods Re-Routing · Source: Eurostat, AUTOSTAT, Eurasian Customs Union (2022–2026)</div>', unsafe_allow_html=True)
