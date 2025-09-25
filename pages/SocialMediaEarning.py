import streamlit as st
from PIL import Image
from app import get_base64

# ---- Page Config ----
logo = Image.open("assets/ipl_logo_favicon.ico")
st.set_page_config(page_title="IPL Social Media Insights", page_icon=logo, layout="wide")

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
    blockquote {{
        font-style: italic;
        color: #e0e0e0;
        border-left: 3px solid #aaa;
        margin: 1rem 0;
        padding-left: 1rem;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---- Title ----
st.markdown("<h1 class='main-title'>IPL Teams on YouTube: Earnings & Engagement (Last 30 Days)</h1>", unsafe_allow_html=True)

# ---- Dashboard Image ----
st.image("assets/SocialMedia.png", caption="Dashboard: Team-wise YouTube Performance & Earnings (30 Days)")

# ---- Button to Open Full Dashboard ----
st.markdown(
    """
    <div style="text-align:center; margin-top: 15px;">
        <a href="https://app.powerbi.com/links/WWckgOHNH8?ctid=779808ca-cf7a-433c-a7d8-c6d2419aafe0&pbi_source=linkShare"
           target="_blank"
           style="background-color:#2ecc71; color:white; padding:10px 18px;
                  text-decoration:none; border-radius:8px; font-weight:bold;">
           🔗 View Full Interactive Social Media & IPL Growth Dashboard
        </a>
    </div>
    """,
    unsafe_allow_html=True
)

# ---- Insights ----
st.markdown("""
<div class="overlay">
<div class="section-title">📊 Key Insights & Narrative</div>

<h5>💰 1. Total Earnings & Monetization</h5>
<ul>
<li><b>GT</b> leads with $686 earnings in the last 30 days — far ahead of <b>SRH ($149)</b>.</li>
<li>This indicates GT’s content strategy is more monetization-friendly, either via higher CPM regions or more ad-optimized videos.</li>
</ul>

<h5>👀 2. Views & Engagement</h5>
<ul>
<li><b>GT</b> averages ~85K daily views — about 4.6× higher than SRH (18.5K).</li>
<li>Consistent posting and engaging content formats are likely driving this viewership gap.</li>
</ul>

<h5>🎥 3. Content Output</h5>
<ul>
<li>GT has published <b>2,441 total videos</b> vs SRH’s <b>2,263</b>.</li>
<li>Higher output → more impressions → more watch time → higher earnings.</li>
</ul>

<h5>📈 4. Subscribers vs Engagement</h5>
<ul>
<li>SRH actually has a <b>larger subscriber base (1.44M)</b> than GT (1.0M).</li>
<li>Yet GT still outperforms SRH — showing GT’s audience is more engaged and content is better surfaced by YouTube’s algorithm.</li>
</ul>

<h5>📊 5. Revenue Efficiency</h5>
<ul>
<li>GT’s ability to earn more with fewer subscribers indicates better <b>revenue per view</b> (CPM efficiency).</li>
<li>SRH could improve monetization with longer-form content, better posting times, and ad-friendly formats.</li>
</ul>

<h5>🎯 Strategic Takeaways</h5>
<blockquote>
"Engagement & consistency drive earnings, not just subscriber count."  
GT proves that frequent, engaging videos can outperform even bigger subscriber bases.  
SRH should focus on boosting daily views and optimizing monetization strategy.
</blockquote>
</div>
""", unsafe_allow_html=True)
