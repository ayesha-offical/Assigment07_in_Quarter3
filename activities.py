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
