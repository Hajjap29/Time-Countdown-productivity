import streamlit as st
import time

# Page configuration
st.set_page_config(
    page_title="Productivity Timer",
    page_icon="⏰",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
    .big-timer {
        font-size: 72px;
        font-weight: bold;
        color: #ff6347;
        text-align: center;
        padding: 30px;
        background-color: #f7f7f7;
        border-radius: 15px;
        margin: 20px 0;
    }
    .stButton>button {
        width: 100%;
        height: 60px;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'time_left' not in st.session_state:
    st.session_state.time_left = 0
if 'running' not in st.session_state:
    st.session_state.running = False
if 'total_time' not in st.session_state:
    st.session_state.total_time = 600  # 10 minutes default

# Title
st.markdown("<h1 style='text-align: center; color: #333333;'>⏰ Productivity Timer</h1>", unsafe_allow_html=True)

# Time input
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    minutes = st.number_input(
        "Enter minutes:",
        min_value=1,
        max_value=180,
        value=10,
        step=1,
        disabled=st.session_state.running
    )

# Display countdown
if st.session_state.time_left > 0:
    minutes_left = st.session_state.time_left // 60
    seconds_left = st.session_state.time_left % 60
    timer_display = f"{minutes_left:02d}:{seconds_left:02d}"
else:
    timer_display = "00:00"

st.markdown(f"<div class='big-timer'>{timer_display}</div>", unsafe_allow_html=True)

# Progress bar
if st.session_state.total_time > 0:
    progress = max(0, st.session_state.time_left / st.session_state.total_time)
    st.progress(progress)

# Control buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("▶️ Start", type="primary", disabled=st.session_state.running, use_container_width=True):
        st.session_state.total_time = minutes * 60
        st.session_state.time_left = minutes * 60
        st.session_state.running = True
        st.rerun()

with col2:
    if st.button("⏹️ Stop", use_container_width=True):
        st.session_state.running = False
        st.rerun()

with col3:
    if st.button("🔄 Reset", use_container_width=True):
        st.session_state.running = False
        st.session_state.time_left = 0
        st.session_state.total_time = minutes * 60
        st.rerun()

# Timer logic
if st.session_state.running and st.session_state.time_left > 0:
    time.sleep(1)
    st.session_state.time_left -= 1
    st.rerun()
elif st.session_state.running and st.session_state.time_left <= 0:
    st.session_state.running = False
    st.balloons()
    st.success("⏰ Time's up! Great work!")
    
    # Play alarm sound when time's up (using HTML audio)
    st.markdown("""
    <audio autoplay>
        <source src="https://www.soundjay.com/button/beep-07.wav" type="audio/wav">
        Your browser does not support the audio element.
    </audio>
    """, unsafe_allow_html=True)
    
    st.rerun()

# Instructions
with st.expander("ℹ️ How to use"):
    st.markdown("""
    1. **Enter the time** in minutes (1-180 minutes)
    2. **Click Start** to begin the countdown
    3. **Click Stop** to pause the timer
    4. **Click Reset** to clear the timer
    
    Perfect for:
    - 🍅 Pomodoro technique (25 minutes)
    - 📚 Study sessions
    - 💪 Workout intervals
    - ☕ Break reminders
    """)

<audio autoplay>
    <source src="https://www.soundjay.com/button/beep-07.wav" type="audio/wav">
    Your browser does not support the audio element.
</audio>
