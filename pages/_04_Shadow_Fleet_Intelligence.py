import streamlit as st
import plotly.graph_objects as go
import pandas as pd

st.set_page_config(page_title="Shadow Fleet Intelligence | Intelligence Platform", page_icon="🏴‍☠️", layout="wide")

st.markdown("""
<style>
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0D1117 0%, #161B22 100%); border-right: 1px solid #30363D; }
    .section-header { color:#8B949E; font-size:0.7rem; letter-spacing:0.18em; text-transform:uppercase; border-bottom:1px solid #30363D; padding-bottom:6px; margin-bottom:16px; }
    .kpi-card { background:#161B22; border:1px solid #30363D; border-top:3px solid #C41E3A; border-radius:8px; padding:20px 16px; text-align:center; }
    .kpi-value { font-size:1.7rem; font-weight:800; color:#E6EDF3; }
    .kpi-label { font-size:0.72rem; color:#8B949E; letter-spacing:0.08em; text-transform:uppercase; margin-top:6px; }
</style>
""", unsafe_allow_html=True)

st.markdown('<span style="color:#C41E3A;font-size:0.7rem;letter-spacing:0.15em;font-weight:700;">MODULE 04</span>', unsafe_allow_html=True)
st.markdown('<h1 style="color:#E6EDF3; font-size:1.6rem; font-weight:800; margin:0;">🏴‍☠️ Shadow Fleet Intelligence Center</h1>', unsafe_allow_html=True)
st.markdown('<p style="color:#8B949E; font-size:0.9rem; margin:4px 0 24px 0;">Ghost Fleet Operations · Maritime Route Analysis · Energy Transit Intelligence · Refining Laundering Network</p>', unsafe_allow_html=True)

c1, c2, c3, c4, c5 = st.columns(5)
kpis = [
    ("1,500+", "Shadow Vessels", "#C41E3A"),
    ("9×", "Fleet Growth Since 2022", "#D29922"),
    ("€1.075T", "Total Energy Revenue", "#1F6FEB"),
    ("€231B", "EU Purchases (Despite Ban)", "#C41E3A"),
    ("€567M", "Feb 2026 Refinery Exports", "#D29922"),
]
for col, (val, label, color) in zip([c1,c2,c3,c4,c5], kpis):
    with col:
        st.markdown(f"""<div class="kpi-card" style="border-top-color:{color}">
            <div class="kpi-value">{val}</div>
            <div class="kpi-label">{label}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

col_map, col_info = st.columns([3, 2])

with col_map:
    st.markdown('<div class="section-header">GLOBAL SHADOW FLEET ROUTE NETWORK — INTERACTIVE MAP</div>', unsafe_allow_html=True)

    # Key locations
    locations = {
        "Russia (Primorsk)": (60.0, 28.5),
        "Russia (Novorossiysk)": (44.7, 37.8),
        "Turkey (Tupras)": (41.0, 29.0),
        "India (Jamnagar)": (22.5, 70.1),
        "China (Shanghai)": (31.2, 121.5),
        "EU (France)": (48.9, 2.3),
        "EU (Belgium)": (50.8, 4.4),
        "Hungary (Budapest)": (47.5, 19.0),
        "Serbia (Belgrade)": (44.8, 20.5),
        "Liberia (Flag)": (6.3, -10.8),
        "Panama (Flag)": (9.0, -79.5),
        "Marshall Islands (Flag)": (7.1, 171.2),
    }

    fig_map = go.Figure()

    # Shadow routes
    routes = [
        ("Russia (Novorossiysk)", "Turkey (Tupras)", "#C41E3A", 3, "Direct crude → Turkey refinery"),
        ("Turkey (Tupras)", "EU (France)", "#D29922", 2, "Refined 'Turkish' fuel to EU"),
        ("Turkey (Tupras)", "EU (Belgium)", "#D29922", 2, "Refined 'Turkish' fuel to EU"),
        ("Russia (Primorsk)", "India (Jamnagar)", "#C41E3A", 3, "Discounted crude to India"),
        ("India (Jamnagar)", "EU (France)", "#1F6FEB", 2, "'Indian' fuel sold back to EU"),
        ("Russia (Primorsk)", "China (Shanghai)", "#C41E3A", 2, "China crude supply"),
    ]

    for src, tgt, color, width, label in routes:
        lat0, lon0 = locations[src]
        lat1, lon1 = locations[tgt]
        fig_map.add_trace(go.Scattergeo(
            lat=[lat0, lat1], lon=[lon0, lon1],
            mode="lines",
            line=dict(width=width, color=color),
            hoverinfo="text",
            text=label,
            showlegend=False,
        ))

    # Nodes
    node_colors = {"Russia": "#C41E3A", "Turkey": "#D29922", "India": "#1F6FEB",
                   "EU": "#3FB950", "China": "#1F6FEB", "Hungary": "#D29922",
                   "Serbia": "#D29922", "Liberia": "#8B949E", "Panama": "#8B949E",
                   "Marshall": "#8B949E"}

    for name, (lat, lon) in locations.items():
        key = name.split(" ")[0]
        color = node_colors.get(key, "#8B949E")
        fig_map.add_trace(go.Scattergeo(
            lat=[lat], lon=[lon],
            mode="markers+text",
            marker=dict(size=10 if "Russia" in name else 8, color=color,
                        line=dict(width=1, color="#E6EDF3")),
            text=[name.split(" (")[0]],
            textposition="top right",
            textfont=dict(color="#E6EDF3", size=9),
            hovertemplate=f"<b>{name}</b><extra></extra>",
            showlegend=False,
        ))

    fig_map.update_layout(
        geo=dict(
            showland=True, landcolor="#161B22",
            showocean=True, oceancolor="#0D1117",
            showcoastlines=True, coastlinecolor="#30363D",
            showframe=False,
            projection_type="natural earth",
            bgcolor="#0D1117",
            showcountries=True, countrycolor="#21262D",
            showlakes=False,
        ),
        paper_bgcolor="#161B22",
        font=dict(color="#E6EDF3"),
        margin=dict(l=0, r=0, t=10, b=0),
        height=440,
    )
    st.plotly_chart(fig_map, use_container_width=True)

with col_info:
    st.markdown('<div class="section-header">GHOST FLEET OPERATION BRIEF</div>', unsafe_allow_html=True)
    facts = [
        ("#C41E3A", "The Fleet", "Russia invested billions acquiring 1,500+ shadow tankers — older oil vessels that cannot be easily tracked by Western compliance systems."),
        ("#D29922", "Registration Trick", "Tankers registered under 'Flags of Convenience' in Liberia, Panama, and the Marshall Islands — non-aligned nations with no Western compliance obligations."),
        ("#1F6FEB", "Refining Laundering", "Russian crude sent to Turkey and India. Refineries (Tupras, Jamnagar) convert it into diesel and jet fuel — which becomes legally 'Turkish' or 'Indian' fuel."),
        ("#3FB950", "The Loop", "EU nations buy back refined Russian energy at premium prices — the same energy they officially banned. France and Belgium are confirmed buyers."),
        ("#8B949E", "Hungary Exception", "93% of Hungary's oil imports from Russia in 2025 (up from 61% in 2021). Druzhba pipeline exemption made legally mandatory for EU sanctions."),
        ("#8B949E", "Serbia Pipeline", "Serbia receives Russian gas via TurkStream. Renewed supply agreement signed late 2025 through March 2026."),
    ]
    for color, title, desc in facts:
        st.markdown(f"""<div style="background:#161B22; border:1px solid #30363D; border-left:3px solid {color};
             border-radius:6px; padding:12px 14px; margin-bottom:8px;">
            <div style="color:{color}; font-size:0.72rem; font-weight:700; letter-spacing:0.06em; margin-bottom:4px;">{title}</div>
            <div style="color:#8B949E; font-size:0.78rem; line-height:1.5;">{desc}</div>
        </div>""", unsafe_allow_html=True)

st.markdown("---")
col_growth, col_buyers = st.columns(2)

with col_growth:
    st.markdown('<div class="section-header">SHADOW FLEET GROWTH TIMELINE</div>', unsafe_allow_html=True)
    years = [2021, 2022, 2023, 2024, 2025, 2026]
    fleet = [165, 400, 750, 1100, 1400, 1500]
    fig_fleet = go.Figure()
    fig_fleet.add_trace(go.Scatter(
        x=years, y=fleet,
        mode="lines+markers",
        line=dict(color="#C41E3A", width=3),
        marker=dict(color="#C41E3A", size=8, line=dict(color="#E6EDF3", width=1)),
        fill="tozeroy",
        fillcolor="rgba(196,30,58,0.1)",
        hovertemplate="<b>%{x}</b><br>%{y} vessels<extra></extra>",
        name="Shadow Vessels",
    ))
    fig_fleet.update_layout(
        plot_bgcolor="#0D1117", paper_bgcolor="#161B22",
        font=dict(color="#E6EDF3"),
        xaxis=dict(color="#8B949E", showgrid=False),
        yaxis=dict(color="#8B949E", showgrid=True, gridcolor="#21262D", title="Vessel Count"),
        margin=dict(l=10, r=10, t=10, b=10), height=260,
        showlegend=False,
    )
    st.plotly_chart(fig_fleet, use_container_width=True)

with col_buyers:
    st.markdown('<div class="section-header">EU ENERGY DEPENDENCY — KEY COUNTRIES (2025)</div>', unsafe_allow_html=True)
    countries = ["Hungary", "Serbia", "France", "Belgium", "Slovakia"]
    dependency = [93, 85, 35, 28, 70]
    pre_sanctions = [61, 78, 18, 15, 65]
    fig_dep = go.Figure()
    fig_dep.add_trace(go.Bar(name="Pre-Sanctions 2021", x=countries, y=pre_sanctions,
                             marker_color="#484F58", text=pre_sanctions, textposition="outside",
                             textfont=dict(color="#8B949E", size=9)))
    fig_dep.add_trace(go.Bar(name="Current 2025", x=countries, y=dependency,
                             marker_color="#C41E3A", text=dependency, textposition="outside",
                             textfont=dict(color="#E6EDF3", size=9)))
    fig_dep.update_layout(
        plot_bgcolor="#0D1117", paper_bgcolor="#161B22",
        font=dict(color="#E6EDF3"), barmode="group",
        yaxis=dict(color="#8B949E", showgrid=True, gridcolor="#21262D", ticksuffix="%", title="Russian Energy Dependency"),
        xaxis=dict(color="#8B949E"),
        legend=dict(font=dict(color="#8B949E", size=10), bgcolor="#161B22"),
        margin=dict(l=10, r=10, t=10, b=10), height=260,
    )
    st.plotly_chart(fig_dep, use_container_width=True)

st.markdown('<div style="text-align:center; color:#484F58; font-size:0.75rem; padding:20px 0 4px 0; border-top:1px solid #21262D; margin-top:32px;">Double-Headed Growth Intelligence Platform · Module 04 · Shadow Fleet Intelligence Center</div>', unsafe_allow_html=True)
