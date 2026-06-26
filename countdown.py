import streamlit as st

st.set_page_config(page_title="Countdown Timer", layout="centered")

# Inject CSS for background and styled boxes
st.markdown("""
    <style>
    .stApp {
        background-image: url("https://raw.githubusercontent.com/loozaB/countdown/images.jpg");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        color: white;
        text-align: center;
    }
    .countdown-title {
        font-size: 40px;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .countdown-container {
        display: flex;
        justify-content: center;
        gap: 20px;
    }
    .countdown-box {
        background: rgba(0, 0, 0, 0.5);
        padding: 20px;
        border-radius: 10px;
        font-size: 30px;
        font-weight: bold;
        min-width: 120px;
    }
    .countdown-label {
        font-size: 16px;
        margin-top: 5px;
        display: block;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="countdown-title">Countdown Timer</div>', unsafe_allow_html=True)

# Target date/time (adjust as needed)
target_datetime = "July 1, 2026 12:00:00"

# JavaScript countdown script
countdown_script = f"""
<script>
var target = new Date("{target_datetime}").getTime();
var x = setInterval(function() {{
  var now = new Date().getTime();
  var distance = target - now;

  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  document.getElementById("days").innerHTML = days;
  document.getElementById("hours").innerHTML = hours;
  document.getElementById("minutes").innerHTML = minutes;
  document.getElementById("seconds").innerHTML = seconds;

  if (distance < 0) {{
    clearInterval(x);
    document.getElementById("countdown").innerHTML = "🎉 Time's up!";
  }}
}}, 1000);
</script>

<div id="countdown" class="countdown-container">
    <div class="countdown-box"><span id="days"></span><span class="countdown-label">Days</span></div>
    <div class="countdown-box"><span id="hours"></span><span class="countdown-label">Hours</span></div>
    <div class="countdown-box"><span id="minutes"></span><span class="countdown-label">Minutes</span></div>
    <div class="countdown-box"><span id="seconds"></span><span class="countdown-label">Seconds</span></div>
</div>
"""

st.markdown(countdown_script, unsafe_allow_html=True)
