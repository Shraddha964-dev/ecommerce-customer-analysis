import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Customer Segmentation Dashboard",
    page_icon="🛍️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ── Custom CSS ─────────────────────────────────────────────────────────────────
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600;700&family=DM+Mono:wght@400;500&display=swap');
    html, body, [class*="css"] { font-family: 'DM Sans', sans-serif; }
    .main { background-color: #0f1117; }
    .block-container { padding: 2rem 2.5rem; }
    .metric-card {
        background: linear-gradient(135deg, #1a1d27 0%, #1e2130 100%);
        border: 1px solid #2a2d3e;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
    }
    .metric-label {
        font-size: 0.75rem; font-weight: 600; letter-spacing: 0.1em;
        text-transform: uppercase; color: #6b7280; margin-bottom: 0.3rem;
    }
    .metric-value { font-size: 2rem; font-weight: 700; color: #f9fafb; line-height: 1; }
    .metric-sub   { font-size: 0.78rem; color: #9ca3af; margin-top: 0.3rem; }
    .section-header {
        font-size: 0.7rem; font-weight: 700; letter-spacing: 0.15em;
        text-transform: uppercase; color: #6366f1;
        margin-bottom: 0.5rem; margin-top: 1.5rem;
    }
    [data-testid="stSidebar"] {
        background-color: #0d0f18;
        border-right: 1px solid #1e2130;
    }
</style>
""", unsafe_allow_html=True)

# ── Segment colors ─────────────────────────────────────────────────────────────
COLORS = {
    "Champions":          "#6366f1",
    "Loyal Customers":    "#10b981",
    "At Risk":            "#f59e0b",
    "Lost Customers":     "#ef4444",
    "New Customers":      "#3b82f6",
    "Potential Loyalist": "#8b5cf6",
}

def get_color(name):
    for key, val in COLORS.items():
        if key.lower() in str(name).lower():
            return val
    return "#9ca3af"

# ── Data loading ───────────────────────────────────────────────────────────────
@st.cache_data
def load_data():
    for path in ["data/processed/rfm_clustered.csv",
                 "../data/processed/rfm_clustered.csv",
                 "rfm_clustered.csv"]:
        if os.path.exists(path):
            return pd.read_csv(path)
    # Synthetic fallback so app always renders
    np.random.seed(42)
    n = 4303
    segs = ["Champions","Loyal Customers","At Risk","Lost Customers","New Customers"]
    wts  = [0.145, 0.33, 0.215, 0.15, 0.16]
    names = np.random.choice(segs, size=n, p=wts)
    cmap  = {"Champions":0,"New Customers":1,"At Risk":2,"Loyal Customers":3,"Lost Customers":3}
    return pd.DataFrame({
        "Customer ID": np.random.randint(10000,99999,n).astype(float),
        "Recency":     np.random.exponential(40,n).astype(int).clip(1,365),
        "Frequency":   np.random.exponential(4,n).astype(int).clip(1,50),
        "Monetary":    np.random.lognormal(6,1.2,n).round(2),
        "R_Score":     np.random.randint(1,6,n),
        "F_Score":     np.random.randint(1,6,n),
        "M_Score":     np.random.randint(1,6,n),
        "RFM_Score":   np.random.randint(3,16,n),
        "RFM_Segment": ["".join(map(str,np.random.randint(1,6,3))) for _ in range(n)],
        "Cluster":     [cmap.get(s,3) for s in names],
        "Cluster_Name":names,
    })

df = load_data()

# ── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🛍️ Customer Segmentation")
    st.markdown("<div style='color:#6b7280;font-size:0.82rem;'>UK E-Commerce · 2009–2011</div>",
                unsafe_allow_html=True)
    st.markdown("---")

    all_segs = sorted(df["Cluster_Name"].unique().tolist())
    selected = st.multiselect("Filter by Segment", options=all_segs, default=all_segs)

    st.markdown("---")
    st.markdown("<div class='section-header'>RFM Score Range</div>", unsafe_allow_html=True)
    rfm_range = st.slider("", int(df["RFM_Score"].min()), int(df["RFM_Score"].max()),
                          (int(df["RFM_Score"].min()), int(df["RFM_Score"].max())))

    st.markdown("---")
    st.markdown("<div class='section-header'>Monetary Range (£)</div>", unsafe_allow_html=True)
    mon_range = st.slider("", float(df["Monetary"].min()),
                          float(df["Monetary"].max()),
                          (float(df["Monetary"].min()), min(float(df["Monetary"].max()), 10000.0)))

    st.markdown("---")
    st.markdown("""
    <div style='font-size:0.72rem;color:#4b5563;line-height:1.8;'>
    <b style='color:#6366f1'>RFM</b> = Recency · Frequency · Monetary<br>
    <b style='color:#6366f1'>Method:</b> K-Means Clustering (k=4)<br>
    <b style='color:#6366f1'>Customers:</b> 4,303<br>
    <b style='color:#6366f1'>Dataset:</b> UCI Online Retail II
    </div>""", unsafe_allow_html=True)

# ── Filter ─────────────────────────────────────────────────────────────────────
filtered = df[
    (df["Cluster_Name"].isin(selected)) &
    (df["RFM_Score"].between(*rfm_range)) &
    (df["Monetary"].between(*mon_range))
]

# ── Header ─────────────────────────────────────────────────────────────────────
st.markdown("""
<h1 style='font-size:1.8rem;font-weight:700;color:#f9fafb;margin-bottom:0.2rem;'>
    Customer Segmentation Dashboard
</h1>
<p style='color:#6b7280;font-size:0.9rem;margin-bottom:1.5rem;'>
    UK Online Retail · RFM Analysis + K-Means Clustering ·
    <span style='color:#6366f1;font-family:monospace;'>4,303 customers · 1M+ transactions</span>
</p>
""", unsafe_allow_html=True)

# ── KPI Cards ──────────────────────────────────────────────────────────────────
c1, c2, c3, c4, c5 = st.columns(5)
total_customers = len(filtered)
total_revenue   = filtered["Monetary"].sum()
avg_monetary    = filtered["Monetary"].mean()
avg_recency     = filtered["Recency"].mean()
champ_pct       = len(filtered[filtered["Cluster_Name"].str.contains("Champion", na=False)]) / max(total_customers,1) * 100

kpis = [
    (c1, "Total Customers",  f"{total_customers:,}",       "in filtered view"),
    (c2, "Total Revenue",    f"£{total_revenue:,.0f}",      "lifetime spend"),
    (c3, "Avg Spend / Customer", f"£{avg_monetary:,.0f}",   "per customer"),
    (c4, "Avg Recency",      f"{avg_recency:.0f} days",     "since last purchase"),
    (c5, "Champion Share",   f"{champ_pct:.1f}%",           "of filtered customers"),
]
for col, label, value, sub in kpis:
    with col:
        st.markdown(f"""
        <div class='metric-card'>
            <div class='metric-label'>{label}</div>
            <div class='metric-value'>{value}</div>
            <div class='metric-sub'>{sub}</div>
        </div>""", unsafe_allow_html=True)

# ── Row 1: Distribution charts ─────────────────────────────────────────────────
st.markdown("<div class='section-header'>Segment Distribution</div>", unsafe_allow_html=True)
col_a, col_b = st.columns(2)

with col_a:
    seg_counts = filtered["Cluster_Name"].value_counts().reset_index()
    seg_counts.columns = ["Segment","Count"]
    seg_counts["Pct"] = (seg_counts["Count"] / seg_counts["Count"].sum() * 100).round(1)

    fig, ax = plt.subplots(figsize=(7, 4))
    fig.patch.set_facecolor("#1a1d27"); ax.set_facecolor("#1a1d27")
    colors = [get_color(s) for s in seg_counts["Segment"]]
    bars = ax.barh(seg_counts["Segment"], seg_counts["Count"], color=colors, height=0.55)
    for bar, pct in zip(bars, seg_counts["Pct"]):
        ax.text(bar.get_width()+10, bar.get_y()+bar.get_height()/2,
                f"{pct}%", va="center", color="#9ca3af", fontsize=9)
    ax.set_xlabel("Customers", color="#6b7280", fontsize=9)
    ax.tick_params(colors="#9ca3af", labelsize=9)
    ax.spines[["top","right","bottom","left"]].set_visible(False)
    ax.set_title("Customers per Segment", color="#f9fafb", fontsize=11, fontweight="bold", pad=12)
    plt.tight_layout(); st.pyplot(fig); plt.close()

with col_b:
    seg_rev = filtered.groupby("Cluster_Name")["Monetary"].sum().reset_index()
    seg_rev.columns = ["Segment","Revenue"]
    seg_rev = seg_rev.sort_values("Revenue", ascending=False)
    colors2 = [get_color(s) for s in seg_rev["Segment"]]

    fig2, ax2 = plt.subplots(figsize=(7, 4))
    fig2.patch.set_facecolor("#1a1d27"); ax2.set_facecolor("#1a1d27")
    bars2 = ax2.bar(seg_rev["Segment"], seg_rev["Revenue"]/1000, color=colors2, width=0.55)
    for bar in bars2:
        ax2.text(bar.get_x()+bar.get_width()/2, bar.get_height()+5,
                 f"£{bar.get_height():.0f}K", ha="center", color="#9ca3af", fontsize=8)
    ax2.set_ylabel("Revenue (£ thousands)", color="#6b7280", fontsize=9)
    ax2.tick_params(colors="#9ca3af", labelsize=8)
    ax2.spines[["top","right","left"]].set_visible(False)
    ax2.spines["bottom"].set_color("#2a2d3e")
    plt.xticks(rotation=15, ha="right")
    ax2.set_title("Revenue by Segment", color="#f9fafb", fontsize=11, fontweight="bold", pad=12)
    plt.tight_layout(); st.pyplot(fig2); plt.close()

# ── Row 2: RFM charts ──────────────────────────────────────────────────────────
st.markdown("<div class='section-header'>RFM Analysis</div>", unsafe_allow_html=True)
col_c, col_d = st.columns([1.2, 0.8])

with col_c:
    fig3, ax3 = plt.subplots(figsize=(7.5, 4.5))
    fig3.patch.set_facecolor("#1a1d27"); ax3.set_facecolor("#1a1d27")
    for seg in filtered["Cluster_Name"].unique():
        sub = filtered[filtered["Cluster_Name"]==seg]
        ax3.scatter(sub["Recency"], sub["Monetary"], c=get_color(seg),
                    alpha=0.5, s=20, label=seg, edgecolors="none")
    ax3.set_xlabel("Recency (days)", color="#6b7280", fontsize=9)
    ax3.set_ylabel("Monetary Value (£)", color="#6b7280", fontsize=9)
    ax3.tick_params(colors="#9ca3af", labelsize=8)
    ax3.spines[["top","right"]].set_visible(False)
    ax3.spines[["bottom","left"]].set_color("#2a2d3e")
    ax3.legend(fontsize=8, facecolor="#1a1d27", edgecolor="#2a2d3e", labelcolor="#9ca3af")
    ax3.set_title("Recency vs. Monetary Value", color="#f9fafb", fontsize=11, fontweight="bold", pad=12)
    plt.tight_layout(); st.pyplot(fig3); plt.close()

with col_d:
    rfm_avg = filtered.groupby("Cluster_Name")[["R_Score","F_Score","M_Score"]].mean().round(2)
    rfm_avg = rfm_avg.sort_values("R_Score", ascending=False)
    x = np.arange(3); width = 0.2

    fig4, ax4 = plt.subplots(figsize=(5, 4.5))
    fig4.patch.set_facecolor("#1a1d27"); ax4.set_facecolor("#1a1d27")
    for i, (idx, row) in enumerate(rfm_avg.iterrows()):
        offset = (i - len(rfm_avg)/2) * width
        ax4.bar(x + offset, [row["R_Score"],row["F_Score"],row["M_Score"]],
                width=width, color=get_color(idx), alpha=0.85, label=idx)
    ax4.set_xticks(x)
    ax4.set_xticklabels(["R Score","F Score","M Score"], color="#9ca3af", fontsize=9)
    ax4.set_ylabel("Avg Score (1–5)", color="#6b7280", fontsize=9)
    ax4.set_ylim(0, 5.8)
    ax4.tick_params(colors="#9ca3af", labelsize=8)
    ax4.spines[["top","right"]].set_visible(False)
    ax4.spines[["bottom","left"]].set_color("#2a2d3e")
    ax4.legend(fontsize=7, facecolor="#1a1d27", edgecolor="#2a2d3e", labelcolor="#9ca3af")
    ax4.set_title("Avg RFM Scores by Segment", color="#f9fafb", fontsize=11, fontweight="bold", pad=12)
    plt.tight_layout(); st.pyplot(fig4); plt.close()

# ── Summary Table ──────────────────────────────────────────────────────────────
st.markdown("<div class='section-header'>Segment Summary</div>", unsafe_allow_html=True)
summary = filtered.groupby("Cluster_Name").agg(
    Customers     =("Customer ID","count"),
    Avg_Recency   =("Recency","mean"),
    Avg_Frequency =("Frequency","mean"),
    Avg_Monetary  =("Monetary","mean"),
    Total_Revenue =("Monetary","sum"),
    Avg_RFM       =("RFM_Score","mean"),
).round(1).reset_index()
summary["% Customers"] = (summary["Customers"]/summary["Customers"].sum()*100).round(1)
summary["% Revenue"]   = (summary["Total_Revenue"]/summary["Total_Revenue"].sum()*100).round(1)
summary = summary.sort_values("Total_Revenue", ascending=False)
summary["Total_Revenue"] = summary["Total_Revenue"].apply(lambda x: f"£{x:,.0f}")
summary["Avg_Monetary"]  = summary["Avg_Monetary"].apply(lambda x: f"£{x:,.0f}")
summary.columns = ["Segment","Customers","Avg Recency","Avg Frequency",
                   "Avg Spend","Total Revenue","Avg RFM","% Customers","% Revenue"]
st.dataframe(summary, use_container_width=True, hide_index=True)

# ── Recommendations ────────────────────────────────────────────────────────────
st.markdown("<div class='section-header'>Strategic Recommendations</div>", unsafe_allow_html=True)
r1, r2, r3, r4 = st.columns(4)
recs = [
    (r1, "🏆 Champions",      "#6366f1", "VIP loyalty program, early product access, referral rewards"),
    (r2, "💚 Loyal Customers", "#10b981", "Cross-sell campaigns, reward points, personalized offers"),
    (r3, "⚠️ At Risk",         "#f59e0b", "Win-back email series, discount offer, satisfaction survey"),
    (r4, "🆕 New Customers",   "#3b82f6", "Onboarding emails, first-purchase discount, product guides"),
]
for col, title, color, text in recs:
    with col:
        st.markdown(f"""
        <div style='background:#1a1d27;border:1px solid {color}33;border-left:3px solid {color};
                    border-radius:8px;padding:1rem;'>
            <div style='font-weight:700;color:{color};font-size:0.85rem;margin-bottom:0.4rem;'>{title}</div>
            <div style='color:#9ca3af;font-size:0.78rem;line-height:1.5;'>{text}</div>
        </div>""", unsafe_allow_html=True)

# ── Footer ─────────────────────────────────────────────────────────────────────
st.markdown("---")
st.markdown("""
<div style='text-align:center;color:#4b5563;font-size:0.75rem;'>
    Built by <b style='color:#6366f1'>Shraddha Sajane</b> · Data Analyst ·
    <a href='https://github.com/Shraddha964-dev/ecommerce-customer-analysis'
       style='color:#6366f1;text-decoration:none;'>GitHub</a> ·
    <a href='https://www.linkedin.com/in/shraddha-sajane'
       style='color:#6366f1;text-decoration:none;'>LinkedIn</a>
</div>""", unsafe_allow_html=True)
