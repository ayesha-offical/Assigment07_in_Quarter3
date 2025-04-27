🧘‍♀️ Mental Wellness Routine Generator 🌟
Welcome to the Mental Wellness Routine Generator! This app is designed to help you create a personalized wellness routine based on your mood and stress level. Whether you're feeling happy, sad, anxious, or lazy, we’ve got you covered with simple, uplifting routines to boost your well-being! ✨💆‍♀️

🌈 Project Overview
The Mental Wellness Routine Generator is built using Streamlit, Python, and Matplotlib. It's your go-to tool for tracking moods, generating customized routines, receiving daily wellness tips, motivational quotes, and learning mindfulness exercises. It's like having a personal wellness coach, anytime you need it! 😌

Key Features:
🎨 Mood-based Routines: Personalized routines based on your current mood and stress level.

📊 Mood Tracking: Keep track of the moods you've selected over time for self-awareness.

🌻 Daily Wellness Tips: Get a wellness tip every time you open the app to improve your day.

💬 Motivational Quotes: Receive uplifting quotes to keep your spirits high.

🧘‍♀️ Mindfulness Exercises: Learn simple exercises to help you relax and de-stress.

🤖 AI Chatbot for Motivation: A chatbot that responds with a motivational message based on your mood.

🗂️ Files Overview
activities.py
This file contains the User class that manages the user's data (name, age, mood, and stress level) and the logic for generating a personalized wellness routine.

python
Copy
Edit
import random

class User:
    def __init__(self, name, age, mood, stress_level):
        self.name = name
        self.age = age
        self.mood = mood
        self.stress_level = stress_level

    def generate_routine(self):
        routines = {
            "Happy": ["Go for a walk", "Enjoy nature", "Call a friend", "Dance to your favorite song"],
            "Sad": ["Write down your feelings", "Take deep breaths", "Watch a comedy movie", "Talk to someone you trust"],
            "Anxious": ["Meditate for 10 minutes", "Drink herbal tea", "Take a break from work", "Practice gratitude"],
            "Lazy": ["Stretch for 5 minutes", "Take a cold shower", "Do one simple task", "Set a mini goal and achieve it"]
        }

        if self.stress_level == "High":
            routines["Anxious"].append("Take a 15-minute break and listen to calming music")
        routine = random.choice(routines.get(self.mood, ["Take care of yourself ❤️"]))
        return routine
app.py
This is the main file where the Streamlit app is built. It contains the user interface (UI), mood and stress level inputs, routine generation, mood tracking, daily wellness tips, motivational quotes, and mindfulness exercises.

python
Copy
Edit
import streamlit as st
from activities import User
import matplotlib.pyplot as plt  # for graph
import random

# --- Streamlit App UI ---

st.set_page_config(page_title="Mental Wellness Routine Generator", page_icon="🧘‍♀️", layout="centered")
st.title("🧘‍♀️ **Mental Wellness Routine Generator**")

st.write("Welcome! Customize your wellness routine based on your mood and stress level. 🌿💛")

# Input fields

name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=10, max_value=100)
mood = st.selectbox("How are you feeling today?", ["Happy", "Sad", "Anxious", "Lazy"])
stress_level = st.radio("How stressed are you?", ["Low", "Medium", "High"])

# --- Generate Routine ---
if st.button("Generate My Routine"):
    user = User(name, age, mood, stress_level)
    routine = user.generate_routine()
    st.success(f"Hello dear {name}! 🌸 Your personalized routine is: \n\n👉 {routine}")

    # Save mood to session state
    if "mood_tracking" not in st.session_state:
        st.session_state.mood_tracking = {"Happy": 0, "Sad": 0, "Anxious": 0, "Lazy": 0}

    st.session_state.mood_tracking[mood] += 1   # Increase mood count

# --- Wellness Dashboard ---

st.header("🌟 Your Wellness Dashboard")

if 'mood_tracking' in st.session_state:
    moods = list(st.session_state.mood_tracking.keys())
    counts = list(st.session_state.mood_tracking.values())

    fig, ax = plt.subplots()
    ax.bar(moods, counts, color='skyblue')
    ax.set_xlabel('Mood')
    ax.set_ylabel('Number of Times Selected')
    ax.set_title('Your Mood Tracking Progress 📊')
    st.pyplot(fig)

    st.success(f"Your Current Mood Stats: {st.session_state.mood_tracking}")
else:
    st.info("Generate your routine first to see your mood tracking dashboard! 🌱")

# --- Daily Wellness Tip ---

st.subheader("🌻 **Daily Wellness Tip**")
daily_tips = [
    "Drink at least 8 glasses of water today! 💧",
    "Take a 10-minute walk outside. 🌿",
    "Smile at yourself in the mirror. 🌟",
    "Write 3 things you are grateful for today. ✨"
]

st.info(random.choice(daily_tips))

# --- Motivational Quote ---

st.subheader("💬 **Motivational Quote**")
quotes = [
    "Believe you can and you're halfway there. 🌈",
    "You are stronger than you think. 💪",
    "Every day is a second chance. 🌻",
    "Your only limit is your mind. 🌟"
]
st.success(random.choice(quotes))

# --- Mindfulness Exercises Section ---

st.header("🧘‍♀️ **Mindfulness Exercises**")

st.write("1. **Breathing Exercise**: Breathe in for 4 seconds, hold for 7 seconds, exhale for 8 seconds. 🌬️")
st.write("2. **Meditation**: Sit quietly and focus on your breathing for 5 minutes. 🧘‍♀️")
st.write("3. **Stretching**: Stretch your arms, legs, and back lightly to relax your muscles. 🤸‍♀️")

# --- Simple AI Chatbot for Motivation ---

st.header("🤖 **Chat with Wellness AI Bot**")

if st.button("Chat Now"):
    bot_responses = {
        "Happy": f"🌻dear {name}! Let your laughter be loud, your heart be light, and your soul be free. 🌈💛 Happiness looks good on you!",
        "Sad": f"🕊️dear {name}! In the soft silence of sadness, new strength is born. 🌿 You are not broken — you are growing in ways your heart will understand soon.",
        "Anxious": f"🌼dear {name}! Even when your mind races, your soul knows how to rest. 🌙 Close your eyes, breathe slowly, and remember: you are bigger than any worry inside you.",
        "Lazy": f"🍃dear {name}! Rest is not a weakness. 🌼 Recharge your soul today, and when you're ready, even a tiny action can light up your path."
    }

    st.write(f"**Jimin Bot**: {bot_responses.get(mood, 'Stay positive and shine! ☀️')}")
🌟 How to Run the App
Install the required libraries: To run this app, install Streamlit, Matplotlib, and Random libraries by running:

nginx
Copy
Edit
pip install streamlit matplotlib
Run the Streamlit App: After installing the necessary libraries, open a terminal, navigate to the directory where your app.py file is located, and run:

arduino
Copy
Edit
streamlit run app.py
Open the App: Streamlit will automatically open the app in your browser. You can now interact with the app to generate your personalized wellness routine! 🌿

🔍 Test the App
You can test the app directly using the link below:

Test the Wellness App Here

🧑‍💻 Object-Oriented Programming (OOP) Concepts Used
This project leverages Object-Oriented Programming (OOP) concepts to organize the code efficiently. The key OOP principles used in this project are:

Classes and Objects: We created a User class to represent the user and store their data like name, age, mood, and stress level.

Encapsulation: The generate_routine method encapsulates the logic for generating a wellness routine based on the user's mood and stress level.

Abstraction: We abstracted the details of routine generation and user data into methods and properties within the User class.

Inheritance: Although not explicitly used in this project, you could easily extend the User class to include subclasses for more specific types of users (e.g., different routines for different age groups).

These concepts help keep the code clean, organized, and easy to scale or modify as new features are added.

Enjoy your journey toward a more mindful and balanced life! 💖✨
