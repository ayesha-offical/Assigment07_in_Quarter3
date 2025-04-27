import streamlit as st
from activities import User 
import matplotlib.pyplot as plt # for graph
import random

# --- Streamlit App UI ---

st.set_page_config(page_title="Mental Wellness Routine Generator", page_icon="🧘‍♀️", layout="centered")
st.title("🧘‍♀️ Mental Wellness Routine Generator")

st.write("Welcome! Customize your wellness routine based on your mood and stress level.")

# Input fields

name= st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=10, max_value=100)
mood= st.selectbox("How are you feeling today?", ["Happy", "Sad", "Anxious", "Lazy"])
stress_level= st.radio("How stressed are you?", ["Low", "Medium", "High"])

# --- Generate Routine ---
if st.button("Generate My routine"):
    user = User(name, age, mood, stress_level)
    routine = user.generate_routine()
    st.success(f"Hello dear {name}!🌸 Your personalized routine is: \n\n👉 {routine}")

    # Save mood to session state
    if "mood_tracking" not in st.session_state:
        st.session_state.mood_tracking = {"Happy": 0, "Sad": 0, "Anxious": 0, "Lazy": 0}

    st.session_state.mood_tracking [mood] +=1   # Increase mood count

# --- Wellness Dashboard ---
st.header("🌟 Your Wellness Dashboard")

if 'mood_tracking' in st.session_state:
    moods = list(st.session_state.mood_tracking.keys())
    counts = list(st.session_state.mood_tracking.values())

    fig, ax = plt.subplots()
    ax.bar(mood, counts, color='skyblue')
    ax.set_xlabel('Mood')
    ax.set_ylabel('Number of Times Selected')
    ax.set_title('Your Mood Tracking Progress')
    st.pyplot(fig)

    st.success(f"Your Current Mood Stats: {st.session_state.mood_tracking}")
else:
    st.info("Generate your routine first to see your mood tracking dashboard!")

# --- Daily Wellness Tip ---

st.subheader("🌻 Daily Wellness Tip")
daily_tips = [
    "Drink at least 8 glasses of water today!",
    "Take a 10-minute walk outside.",
    "Smile at yourself in the mirror. 🌟",
    "Write 3 things you are grateful for today."
]

st.info(random.choice(daily_tips))

# --- Motivational Quote ---
st.subheader("💬 Motivational Quote")
quotes =[
    "Believe you can and you're halfway there.",
    "You are stronger than you think.",
    "Every day is a second chance.",
    "Your only limit is your mind."
]
st.success(random.choice(quotes))

# --- Mindfulness Exercises Section ---
st.header("🧘‍♀️ Mindfulness Exercises")
          
st.write("1. **Breathing Exercise**: Breathe in for 4 seconds, hold for 7 seconds, exhale for 8 seconds.")
st.write("2. **Meditation**: Sit quietly and focus on your breathing for 5 minutes.")
st.write("3. **Stretching**: Stretch your arms, legs, and back lightly to relax your muscles.")

# --- Simple AI Chatbot for Motivation ---
st.header("🤖 Chat with Wellness AI Bot")

if st.button("Chat Now"):
    bot__responses = {
        "Happy": f"🌻dear {name}! Let your laughter be loud, your heart be light, and your soul be free. 🌈💛 Happiness looks good on you!",
        "Sad": f"🕊️dear {name}! In the soft silence of sadness, new strength is born. 🌿 You are not broken — you are growing in ways your heart will understand soon.",
        "Anxious":f"🌼dear {name}! Even when your mind races, your soul knows how to rest. 🌙 Close your eyes, breathe slowly, and remember: you are bigger than any worry inside you.",
        "Lazy": f"🍃dear {name}! Rest is not a weakness. 🌼 Recharge your soul today, and when you're ready, even a tiny action can light up your path."
    }

    st.write(f"Jimin bot: {bot__responses.get(mood, 'Stay positive and shine! ☀️')}")
