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
    st.session_state.total_time = 600  # Default to 10 minutes

# Title
st.markdown("<h1 style='text-align: center; color: #333333;'>⏰ Productivity Timer</h1>", unsafe_allow_html=True)

# Timer Duration Selection
timer_option = st.radio(
    "Choose timer duration:",
    ["Custom time", "30 seconds", "1 minute", "5 minutes", "10 minutes", "15 minutes", "25 minutes (Pomodoro)"],
    horizontal=True
)

# Initialize variables
minutes = 0
seconds = 0

# Custom timer input for "Custom time"
if timer_option == "Custom time":
    col1, col2, col3 = st.columns([1, 1, 1])
    with col1:
        st.write("")  # Spacer
    with col2:
        minutes = st.number_input(
            "Minutes:",
            min_value=0,
            max_value=180,
            value=10,
            step=1,
            disabled=st.session_state.running
        )
        seconds = st.number_input(
            "Seconds:",
            min_value=0,
            max_value=59,
            value=0,
            step=1,
            disabled=st.session_state.running
        )
    with col3:
        st.write("")  # Spacer
else:
    # Set pre-set timer options
    if timer_option == "30 seconds":
        minutes = 0
        seconds = 30
    elif timer_option == "1 minute":
        minutes = 1
        seconds = 0
    elif timer_option == "5 minutes":
        minutes = 5
        seconds = 0
    elif timer_option == "10 minutes":
        minutes = 10
        seconds = 0
    elif timer_option == "15 minutes":
        minutes = 15
        seconds = 0
    elif timer_option == "25 minutes (Pomodoro)":
        minutes = 25
        seconds = 0

# Convert all time to seconds for consistency
total_seconds = (minutes * 60) + seconds

# Validation
if total_seconds == 0 and not st.session_state.running:
    st.warning("⚠️ Please set a time greater than 0 seconds")

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
    if st.button("▶️ Start", type="primary", disabled=st.session_state.running or total_seconds == 0, use_container_width=True):
        st.session_state.total_time = total_seconds
        st.session_state.time_left = total_seconds
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
        st.session_state.total_time = total_seconds
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
    
    # Play alarm sound using HTML5 audio with a public sound URL
    alarm_html = """
    <audio autoplay>
        <source src="mixkit-facility-alaram-sound-999.wav" type="audio/mpeg">
    </audio>
    """
    st.markdown(alarm_html, unsafe_allow_html=True)
    st.rerun()

# Instructions
with st.expander("ℹ️ How to use"):
    st.markdown("""
    1. **Choose a timer duration** (pre-set or custom)
    2. For custom time, set both **minutes and seconds**
    3. **Click Start** to begin the countdown
    4. **Click Stop** to pause the timer
    5. **Click Reset** to clear the timer
    6. An alarm will sound when time is up! 🔔
    
    Perfect for:
    - 🍅 Pomodoro technique (25 minutes)
    - 📚 Study sessions
    - 💪 Workout intervals
    - ☕ Break reminders
    - ⏱️ Cooking timers
    """)
