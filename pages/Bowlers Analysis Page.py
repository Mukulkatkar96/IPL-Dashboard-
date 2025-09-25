import streamlit as st
from PIL import Image
from app import get_base64

# ---- Page Config ----
logo = Image.open("assets/ipl_logo_favicon.ico")
st.set_page_config(page_title="Bowlers: Price vs Performance", page_icon=logo, layout="wide")

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
st.markdown("<h1 class='main-title'>Bowlers: Price vs Performance</h1>", unsafe_allow_html=True)

# ---- Intro Section ----
st.markdown("""
<div class="overlay">
<div class="section-title">📊 Overview</div>
<p>This dashboard explores the <b>relationship between auction price and wicket-taking performance</b> for IPL bowlers.  
It investigates whether the most expensive bowlers consistently deliver higher wicket counts.</p>
</div>
""", unsafe_allow_html=True)

# ---- Dashboard Image ----
st.image("assets/bowler_dashboard.png", caption="Dashboard: Auction Price vs Bowler Performance")

# ---- Button to Open Full Dashboard ----
st.markdown(
    """
    <div style="text-align:center; margin-top: 15px;">
        <a href="https://app.powerbi.com/links/WWckgOHNH8?ctid=779808ca-cf7a-433c-a7d8-c6d2419aafe0&pbi_source=linkShare"
           target="_blank"
           style="background-color:#3498db; color:white; padding:10px 18px;
                  text-decoration:none; border-radius:8px; font-weight:bold;">
           🔗 View Full Interactive Bowler Dashboard
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# ---- Insights ----
st.markdown("""
<div class="overlay">
<div class="section-title">🔍 Key Insights & Narrative</div>

<h5>🧠 1. Price vs Wickets (Scatter Plot)</h5>
<ul>
<li>The trendline slopes downward — suggesting that higher prices don’t guarantee more wickets.</li>
<li>Several low- and mid-priced bowlers are among the highest wicket-takers, offering excellent ROI.</li>
<li>Some elite bowlers appear in the low-wicket zone, indicating poor value for money.</li>
</ul>

<h5>💰 2. Top 5 Most Expensive Bowlers</h5>
<table class="table table-dark table-sm table-bordered">
<thead><tr><th>Player</th><th>Price (₹ Cr)</th><th>Wickets</th></tr></thead>
<tbody>
<tr><td>Mitchell Starc</td><td>25</td><td>34</td></tr>
<tr><td>Arshdeep Singh</td><td>18</td><td>30</td></tr>
<tr><td>Yuzvendra Chahal</td><td>18</td><td>139</td></tr>
<tr><td>Deepak Chahar</td><td>14</td><td>59</td></tr>
<tr><td>Jhye Richardson</td><td>14</td><td>3</td></tr>
</tbody></table>
<ul>
<li><b>Chahal</b> stands out with 139 wickets — strong ROI.</li>
<li><b>Mitchell Starc</b> and <b>Arshdeep</b> are expensive but with modest wicket returns.</li>
<li><b>Jhye Richardson</b> has only 3 wickets, making him one of the poorest value picks.</li>
</ul>

<h5>📈 3. Price Change by Season</h5>
<ul>
<li>Total spend on bowlers has grown dramatically since 2018, peaking at ₹297 Cr in 2025.</li>
<li>Despite higher spending, average wickets per player haven’t improved proportionally.</li>
</ul>

<h5>📊 4. Price by Player Category</h5>
<ul>
<li>Elite bowlers account for 51% of total spend, followed by High (24%), Mid (20%), and Low (5%).</li>
<li>Many of the most consistent wicket-takers belong to Mid and Low price categories, suggesting better value outside marquee buys.</li>
</ul>

<h5>📋 5. Player Table Insights</h5>
<ul>
<li><b>Chahal (₹18 Cr, 139 wickets)</b> and <b>Trent Boult (₹12.5 Cr, 76 wickets)</b> deliver exceptional ROI.</li>
<li><b>Jhye Richardson (₹14 Cr, 3 wickets)</b> and <b>Josh Hazlewood (₹12.5 Cr, 12 wickets)</b> are cost-inefficient.</li>
</ul>

<h5>🧠 Overall Conclusion</h5>
<p><i>"Big price tags don’t guarantee big wicket hauls."</i><br>
There is a clear disconnect between spending and bowling output.  
Franchises can improve by identifying undervalued bowlers and focusing on consistency and strike rates rather than reputation alone.</p>
</div>
""", unsafe_allow_html=True)
