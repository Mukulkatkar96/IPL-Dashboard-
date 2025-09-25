1. Project Title & Short Description

Start with a clear title and 1–2 line description.

 Beyond the Price Tag: IPL Auction Price vs Performance
📊 An interactive data storytelling project exploring whether expensive players in the Indian Premier League (IPL) deliver proportionate performance — built with Power BI, Python, and deployed via Streamlit.

2. Demo Link

If you’re deploying on Streamlit Cloud, add a direct link to your app.

🚀 **Live App:** [View the Dashboard](https://yourappname.streamlit.app)

3. Project Overview

Briefly explain what the project does and what problem it solves.

 📖 Overview
This project analyzes IPL auction data (2008–2024) to examine whether the most expensive players consistently justify their price tags.  
Using data storytelling techniques, the project provides:
- Player Price vs Performance Dashboards** (Batsmen & Bowlers)
- League Financial Growth Analysis** (Media rights, YouTube engagement)
- Interactive Visuals** for exploring trends across seasons, teams, and player categories.

4. Features

Highlight the interactive elements and storytelling aspects.

✨ Features
- 📈 Scatter Plots with Trendlines** – Compare auction price vs performance.
- 🏏 Top Players View – Quickly see the top 5 most expensive players.
- 🎨 Dynamic Filters – Select team, season, and price categories.
- 💻 Fully Interactive – Users can explore data in real-time.
- 🌐 Deployed on Streamlit – No installation required, runs in the browser.

5. Dataset Information

Explain where the data comes from and give links.
 📊 Data Sources
- [ESPN Cricinfo](https://www.espncricinfo.com/records/trophy/indian-premier-league-117) – Player stats & auction results  
- [Cricsheet](https://cricsheet.org/matches/) – Ball-by-ball match data  
- [Kaggle IPL Dataset](https://www.kaggle.com/datasets/patrickb1912/ipl-complete-dataset-20082020) – Initial schema design  
- [SocialBlade](https://socialblade.com/youtube/channel/UCl23mvQ3321L7zO6JyzhVmg) – YouTube analytics for franchises  
- [Economic Times](https://economictimes.indiatimes.com/news/sports/ipl-media-rights-sold-for-rs-48390-crore-for-a-five-year-period-bcci-secretary-jay-shah/articleshow/92208961.cms) – Media rights data  

6. Tech Stack

List all technologies used.

 🛠️ Tech Stack
- Frontend:** Streamlit
- Backend / Analysis:** Python (Pandas, NumPy, Matplotlib, Plotly)
- Visualization & Modelling: Power BI (DAX measures, star schema)
- Version Control:** Git & GitHub

7. Installation & Usage

Explain how someone can run it locally.

🏃‍♂️ Run Locally

1. Clone the repo:
bash
git clone https://github.com/yourusername/ipl-auction-performance.git
cd ipl-auction-performance


Install dependencies:

pip install -r requirements.txt


Run the app:

streamlit run app.py

8. Project Structure

Give a quick idea of folder layout.

📂 Project Structure

├── app.py                   # Main Streamlit app
├── data/                    # Cleaned datasets
├── scripts/                 # Preprocessing scripts
├── requirements.txt
└── README.md

