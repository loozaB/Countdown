import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="Countdown Timer", layout="centered")

# Background image from GitHub raw link
background_url = "https://raw.githubusercontent.com/loozaB/Countdown/refs/heads/main/IMG_20260627_131113.jpg"

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{background_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        #color: white;
        text-align: center;
    }}
    .stApp::before{{
        content: "";
        position: absolute;
        top: 0; left: 0; right: 0; bottom: 0;
        background-color: rgba(255, 255, 255, 0.2);
    }}
    .countdown-title {{
        font-size: 50px;
        font-weight: bold;
        margin-bottom: 60px;
        margin-top: 50px;
        color: black;
        padding-top: 25px;
        text-align: center;
    }}
    .countdown-container {{
        display: flex;
        justify-content: center;
        gap: 30px;
        flex-wrap: wrap;
    }}
    .countdown-box {{
        background: rgba(0, 0, 0, 0.3);
        padding: 25px;
        border-radius: 20px;
        font-size: 35px;
        font-weight: bold;
        min-width: 130px;
        box-sizing: content-box;
        text-align: center;
    }}
    .countdown-label {{
        font-size: 50px;
        margin-bottom: 5px;
        text-align: center;
        display: block;
        font-weight: bold;
        background: linear-gradient(to left, #00FEFF, #00FFFF);
        -webkit-background-clip: text; 
        -webkit-text-fill-color: transparent;   
    }}
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="countdown-title">12 Barse BungaDyo Jatra</div>', unsafe_allow_html=True)

# Fixed target date/time
target_datetime = datetime(2027, 5, 10, 16, 0, 0)

placeholder = st.empty()

# Loop for live countdown
while True:
    now = datetime.now()
    remaining = target_datetime - now

    if remaining.total_seconds() <= 0:
        placeholder.markdown("## 🎉 Time's up!")
        break
    else:
        days, seconds = divmod(int(remaining.total_seconds()), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        countdown_html = f"""
        <div class="countdown-container">
            <div class="countdown-box"><span class="countdown-label">{days}</span><span>Days</span></div>
            <div class="countdown-box"><span class="countdown-label">{hours}</span><span>Hours</span></div>
            <div class="countdown-box"><span class="countdown-label">{minutes}</span><span>Minutes</span></div>
            <div class="countdown-box"><span class="countdown-label">{seconds}</span><span>Seconds</span></div>
        </div>
        """
        placeholder.markdown(countdown_html, unsafe_allow_html=True)

        time.sleep(1)
