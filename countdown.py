import streamlit as st
from datetime import datetime
import time, base64

st.set_page_config(page_title="Countdown Timer", layout="centered")

# Custom CSS for gradient background and styled timer boxes
st.markdown("""
    <style>
    .stApp {
        background-image: url("");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
    .countdown-title {
        font-size: 90px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .countdown-container {
        display: flex;
        justify-content: center;
        gap: 30px;
    }
    .countdown-box {
        background: rgba(255, 255, 255, 0.1);
        padding: 20px;
        border-radius: 10px;
        font-size: 35px;
        font-weight: bold;
        min-width: 120px;
    }
    .countdown-label {
        font-size: 25px;
        margin-top: 7px;
        display: block;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="countdown-title">Countdown Timer</div>', unsafe_allow_html=True)

# Fixed target date/time
target_datetime = datetime(2026, 7, 1, 12, 0, 0)

placeholder = st.empty()

while True:
    now = datetime.now()
    remaining = target_datetime - now

    if remaining.total_seconds() <= 0:
        placeholder.markdown(" 🎉 Time's up!")
        break
    else:
        days, seconds = divmod(int(remaining.total_seconds()), 86400)
        hours, seconds = divmod(seconds, 3600)
        minutes, seconds = divmod(seconds, 60)

        countdown_html = f"""
        <div class="countdown-container">
            <div class="countdown-box">{days}<span class="countdown-label">Days</span></div>
            <div class="countdown-box">{hours}<span class="countdown-label">Hours</span></div>
            <div class="countdown-box">{minutes}<span class="countdown-label">Minutes</span></div>
            <div class="countdown-box">{seconds}<span class="countdown-label">Seconds</span></div>
        </div>
        """
        placeholder.markdown(countdown_html, unsafe_allow_html=True)

        time.sleep(1)
