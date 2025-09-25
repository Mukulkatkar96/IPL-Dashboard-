import streamlit as st
from PIL import Image
import base64

# ---- Page Config ----
logo = Image.open("assets/ipl_logo_favicon.ico")
st.set_page_config(page_title="IPL Data Storytelling", page_icon=logo, layout="wide")

# ---- Load Background ----
def get_base64(file_path):
    with open(file_path, "rb") as f:
        return base64.b64encode(f.read()).decode()

background_image = get_base64("assets/ipl_background_blur.jpg")

# ---- Bootstrap + Custom Styling ----
st.markdown("""
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
""", unsafe_allow_html=True)

st.markdown(
    f"""
    <h1 style='color:#808080; text-align:center;'>
       
    </h1>
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
        max-width: 850px;
        font-size: 1.15rem;
        line-height: 1.65;
    }}
    .main-title {{
        text-align: center;
        font-size: 2.5rem;
        font-weight: 700;
        color: #363534;
        margin-top: 1rem;
        margin-bottom: 1rem;
    }}
    .section-title {{
        font-size: 1.4rem;
        font-weight: 600;
        margin-bottom: 0.5rem;
    }}
    .card-grid {{
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
        gap: 1rem;
        margin-top: 1rem;
    }}
    .card {{
        background: rgba(255,255,255,0.05);
        border: 1px solid rgba(255,255,255,0.15);
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
        color: #ffffff;
        font-size: 1rem;
    }}
    .footer {{
        color: #363534;
        text-align: center;
        margin-top: 2rem;
        font-size: 0.85rem;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ---- Main Title ----
st.markdown("<h1 class='main-title'>Beyond the Price Tag: IPL’s Rise & the Myth of Expensive Players</h1>", unsafe_allow_html=True)

# ---- Objective ----
st.markdown(f"""
<div class="overlay">
<div class="section-title">🎯 Objective</div>
<p>
This project explores two key questions:
</p>
<ul>
<li>Do the most expensive IPL players consistently deliver?</li>
<li>How did IPL transform into a multi-billion-dollar global sports league?</li>
</ul>
<p>We combine auction data, player stats, business insights, and social media engagement to reveal the truth behind the numbers.</p>
</div>
""", unsafe_allow_html=True)

# ---- Navigation ----
st.markdown(f"""
<div class="overlay">
<div class="section-title">🧭 Explore</div>
<div class="card-grid">
    <div class="card">📊 <b>Batsmen Dashboard</b><br>Price vs Performance</div>
    <div class="card">🎯 <b>Bowler Dashboard</b><br>Wickets vs Price</div>
    <div class="card">📈 <b>IPL Growth</b><br>Media Rights & YouTube Earnings</div>
</div>
</div>
""", unsafe_allow_html=True)

# ---- Research Questions ----
st.markdown(f"""
<div class="overlay">
<div class="section-title">📌 Research Questions</div>
<ul>
<li>Is there a gap between auction hype and on-field performance?</li>
<li>Who are the best value-for-money players?</li>
<li>How do media rights and digital engagement drive IPL’s revenue growth?</li>
</ul>
</div>
""", unsafe_allow_html=True)

# ---- Tools ----
st.markdown(f"""
<div class="overlay">
<div class="section-title">🛠 Tools</div>
<p>Power BI • Python (Pandas, NumPy) • Streamlit • Excel</p>
</div>
""", unsafe_allow_html=True)

# ---- Feedback ----
st.markdown(f"""
<div class="overlay text-center">
<div class="section-title">💬 Feedback</div>
<a href="https://docs.google.com/forms/d/e/1FAIpQLScAQzzTGF2lQH-VYLV7Ee4hlrGm2xM34uFTmLNfbS7OXFdd7Q/viewform?usp=dialog" 
   class="btn btn-outline-light btn-sm" target="_blank">
   Submit Feedback
</a>
</div>
""", unsafe_allow_html=True)

# ---- Footer ----
st.markdown("""
<div class="footer">
© 2025 Mukul Katkar | MSc Data Science and AI | Oxford Brookes University
</div>
""", unsafe_allow_html=True)
