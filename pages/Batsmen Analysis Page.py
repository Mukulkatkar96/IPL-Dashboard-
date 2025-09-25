import streamlit as st
from PIL import Image
from app import get_base64

# ---- Page Config ----
logo = Image.open("assets/ipl_logo_favicon.ico")
st.set_page_config(page_title="Batsmen: Price vs Performance", page_icon=logo, layout="wide")

# ---- Load Background ----
background_image = get_base64("assets/ipl_background_blur.jpg")

# ---- Bootstrap + Custom Styling ----
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpeg;base64,{background_image}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        backdrop-filter: blur(6px);
    }}
    .overlay {{
        background: rgba(0, 0, 0, 0.8);
        border-radius: 10px;
        padding: 1.5rem 2rem;
        margin: 1.2rem auto;
        color: #f5f5f5;
        max-width: 900px;
        font-size: 1.1rem;
        line-height: 1.65;
    }}
    .main-title {{
        text-align: center;
        font-size: 2.4rem;
        font-weight: 700;
        color: #808080;
        margin: 1rem 0;
    }}
    .section-title {{
        font-size: 1.3rem;
        font-weight: 600;
        margin-bottom: 0.7rem;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---- Page Title ----
st.markdown("<h1 class='main-title'>Batsmen: Price vs Performance</h1>", unsafe_allow_html=True)

# ---- Intro Section ----
st.markdown("""
<div class="overlay">
<div class="section-title">📊 Overview</div>
<p>This dashboard analyzes the <b>relationship between auction prices and batting performance</b> in the Indian Premier League (IPL) from 2008–2024.  
It challenges the assumption that the most expensive players are always the top performers.</p>
</div>
""", unsafe_allow_html=True)

# ---- Dashboard Image ----
st.image("assets/batsman_dashboard.png", caption="Dashboard: Auction Price vs Batsman Performance", use_column_width=True)

# ---- Button to Open Full Dashboard ----
st.markdown(
    """
    <div style="text-align:center; margin-top: 15px;">
        <a href="https://app.powerbi.com/links/WWckgOHNH8?ctid=779808ca-cf7a-433c-a7d8-c6d2419aafe0&pbi_source=linkShare"
           target="_blank"
           style="background-color:#f39c12; color:white; padding:10px 18px;
                  text-decoration:none; border-radius:8px; font-weight:bold;">
           🔗 View Full Interactive Dashboard
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# ---- Insights ----
st.markdown("""
<div class="overlay">
<div class="section-title">🔍 Key Insights & Narrative</div>

<h5>💰 Top 5 Most Expensive Batsmen</h5>
<ul>
<li><b>Rishabh Pant</b> & <b>Shreyas Iyer</b> are the costliest picks at ₹27 Cr each.</li>
<li><b>Nicholas Pooran (₹16 Cr)</b> stands out for low ROI with only ~606 runs.</li>
<li><b>Yuvraj Singh</b> & <b>Jos Buttler</b> justify their price better with strong run totals.</li>
<li><b>Takeaway:</b> Being expensive does not guarantee top-tier performance.</li>
</ul>

<h5>📉 Auction Price vs Runs (Scatter Plot)</h5>
<ul>
<li>Shows wide variation in runs at all price points.</li>
<li>Trendline slightly slopes downward — higher price often doesn’t mean higher run production.</li>
<li>Several mid- and low-priced players match or outperform elite players, providing better value-for-money.</li>
<li><b>Takeaway:</b> Teams can find high-ROI players without overspending.</li>
</ul>

<h5>📈 Price Change by Season</h5>
<ul>
<li>Spending has skyrocketed from 2018 onwards, peaking at ₹639 Cr in the latest season.</li>
<li>However, performance hasn’t scaled proportionally — questioning the efficiency of heavy spending.</li>
</ul>

<h5>📊 Price Distribution by Player Category</h5>
<ul>
<li>Elite + High players take up ~70% of total spend but don't always dominate run tallies.</li>
<li>Mid-tier players are frequently undervalued but still deliver competitive runs.</li>
<li><b>Takeaway:</b> Franchises might be over-relying on marquee names while missing mid-tier value.</li>
</ul>

<h5>📋 Player Table (Cost vs Runs)</h5>
<ul>
<li><b>Venkatesh Iyer (₹23.75 Cr, 370 runs)</b> & <b>Pat Cummins (₹20.5 Cr, 316 runs)</b> deliver very poor cost-per-run.</li>
<li><b>Jos Buttler (₹15.75 Cr, 1968 runs)</b> shows strong ROI with high runs at a lower price point.</li>
</ul>

<h5>🧠 Overall Conclusion</h5>
<p><i>"Expensive doesn’t always mean effective."</i>  
This analysis highlights a disconnect between auction price and batting output.  
Teams may be overspending on marquee players while undervaluing mid-tier talent that delivers comparable results.  
Smarter scouting and ROI-based bidding could improve squad efficiency.</p>
</div>
""", unsafe_allow_html=True)
