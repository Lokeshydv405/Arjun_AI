import random

def greeting(x):
    greetings_data = {
    "morning": [
        "Good morning! How may I assist you today?",
        "Morning sunshine! How can I help you?",
        "Hey, morning! Rise and shine! What can I do for you?",
        "Good morning! It's great to start the day with you! What do you need help with?",
        "Morning! Hope you're having a fantastic day so far! Is there anything on your mind?",
        "Rise and shine! Good morning! What can I help you with today?",
        "Good morning! We're glad you're up and running! What can I do for you?",
        "Morning! May I start your day off right by helping you with...?",
        "Good morning! It's a brand new day! What do you want to accomplish?",
        "Hey, morning! Let's make today amazing! What's on your agenda?"
    ],
    "afternoon": [
        "Afternoon! How's your day going so far? Need any help getting things done?",
        "Hey, afternoon! Hope you're having a fantastic day! What do you need assistance with?",
        "Good afternoon! We're here to help you tackle the rest of your day!",
        "Afternoon! May I help you power through the remaining tasks on your to-do list?",
        "Hey, afternoon! We're in the home stretch! What can I help you with to make the rest of your day easier?",
        "Good afternoon! Take a moment to relax; we've got you covered!",
        "Afternoon! It's not too late to get everything done today! What do you need help with?",
        "Hey, afternoon! What's on your mind? Need any help figuring things out?",
        "Good afternoon! Here to help you wrap up your tasks for the day!",
        "Afternoon! We're all ears! Need any help with anything today?"
    ],
    "evening": [
        "Good evening! Hope you're unwinding after a great day! What can I help you with?",
        "Hey, evening! It's been a busy day, but we're here to make the evening even more relaxing!",
        "Good evening! We're glad you made it through the day! Need any help with tomorrow's tasks?",
        "Evening! May I help you wrap up your day with a smile?",
        "Hey, evening! What do you need help with to make the evening amazing?",
        "Good evening! It's time to kick back and relax! What can I help you with?",
        "Evening! We're here to help you wind down and get ready for tomorrow!",
        "Hey, evening! Need any help finding something to do or watching streaming recommendations?",
        "Good evening! We're all set to help you with whatever you need tonight!",
        "Evening! It's been a pleasure helping you throughout the day! Is there anything else I can assist you with?"
    ],
    "good_night": [
        "Good night! Wishing you a peaceful rest. See you tomorrow!",
        "Night night! Let me know if you need help before heading off to bed!",
        "Good night! Sleep well and let me know how I can assist you tomorrow.",
        "Good night! I'll be here if you need me. Rest easy!",
        "Sweet dreams! I'll be ready to help when you wake up!"
    ],
    "night_working": [
        "Burning the midnight oil? I'm here to assist you!",
        "Late night work, huh? How can I help you power through?",
        "You're working hard! Let me know what you need during this late hour.",
        "Still working at night? I’m here to help with anything you need!",
        "Late night hustle! What can I assist you with to keep things moving?"
    ]
}
   
    return random.choice(greetings_data[x])

quit_phrases = [
    "Bye",
    "Goodbye",
    "Quit",
    "Stop",
    "Exit",
    "Leave",
    "Cancel",
    "Disconnect",
    "Disconnect from you",
    "End of session",
    "Time to go",
    "That's all",
    "I think I'll head out",
    "That's all for now",
    "I'm done here",
    "I'll be back later",
    "See you later",
    "Talk to you soon",
    "I'll catch you later",
    "I'm done with this conversation",
    "I've had enough",
    "I think I've had my fill",
    "I'm ready to wrap things up",
    "I've got what I need, thanks",
    "I'm satisfied with the information I've received",
    "I think we're all set",
    "That's all for me",
    "I'm good to go",
    "I'm ready to move on"
]
goodbye_greetings = [
    "It was nice chatting with you. Have a great day!",
    "Thanks for talking to me. Goodbye for now!",
    "It was a pleasure assisting you. Have a wonderful day!",
    "Thank you for using me. Goodbye and take care!",
    "I hope our chat was helpful. Goodbye and have a great day!",
    "I'll miss our conversation. Goodbye for now!",
    "It was my pleasure to help you. Have a fantastic day!",
    "Thanks for reaching out. Goodbye and take care!",
    "I hope you enjoyed our conversation. Goodbye and have a great day!",
    "It was a pleasure serving you. Have a wonderful day!"
]

time_phrases = [
    "What is the time",
    "What time is it",
    "Do you know the time",
    "Can you tell me the time",
    "What's the current time",
    "Could you check the time for me",
    "Do you have the time",
    "What’s the time now",
    "How late is it",
    "Can you give me the time",
    "Do you know what time it is",
    "Is it time already",
    "Can you tell me what time it is",
    "What time does your watch say",
    "How much time has passed",
    "What’s the hour",
    "Is it (X o'clock) yet",
    "Do you happen to have the time",
    "Can I get the time",
    "Is it time now",
    "Can you look at the clock for me",
    "Can you check the time",
]
weather_phrases = [
    "What is the weather like outside",
    "How is the weather today",
    "Can you tell me the weather right now",
    "What is the current weather outside",
    "What is the weather forecast for today",
    "Do you know the weather outside",
    "Is it going to rain today",
    "Is it sunny outside",
    "How hot is it today",
    "Is it cold right now",
    "What is the temperature",
    "Can you check the weather for me",
    "Is it windy today",
    "Is there a storm coming",
    "Will it snow today",
    "Do I need an umbrella",
    "Is the weather good today",
    "What is the weather right now",
    "What is the weather outside",
    "How warm is it today",
    "Tell me about the weather outside",
    "Give me weather updates",
    "What is the weather",
    "How is the weather",
]

if __name__ == "__main__":
    print(greeting('evening'))

