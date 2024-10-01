import datetime
from config import WeatherAPI
from Basic_Utilization.Say import say
import requests
from Chatting.Chat import chat

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
    "Can you look at the clock for me"
]
weather_phrases = [
    "What's the weather like",
    "How's the weather today",
    "Can you tell me the weather",
    "What's the current weather",
    "What’s the weather forecast",
    "Do you know the weather",
    "Is it going to rain today",
    "Is it sunny outside",
    "How hot is it today",
    "Is it cold right now",
    "What's the temperature",
    "Can you check the weather for me",
    "Is it windy today",
    "Is there a storm coming",
    "Will it snow today",
    "Do I need an umbrella",
    "Is the weather good today",
    "What’s the weather right now",
    "What’s the weather outside",
    "How warm is it today"
]


def get_weather_info():
    base_url = f"http://api.openweathermap.org/data/2.5/forecast?id=1263862&exclude=hourly,daily&appid={WeatherAPI}&q=mandi"
    response = requests.get(base_url)
    weather_data = response.json()

    if weather_data['cod'] != '404':
        y = weather_data["list"][0]
        temp = y['main']
        current_temperature = round(temp["temp"] - 273.15, 1)  # Convert from Kelvin to Celsius
        weather_description = y["weather"][0]["description"].capitalize()

        return f"It's currently {current_temperature} degrees Celsius with {weather_description}."
    else:
        return "I'm having trouble fetching the current weather."

def get_time():
    current_time = datetime.datetime.now().strftime("%I:%M %p")  # 12-hour format with AM/PM
    return f"The time is {current_time}."

def greeting():
    current_hour = datetime.datetime.now().hour

    if 5 <= current_hour < 12:
        greeting_time = "Good morning!"
    elif 12 <= current_hour < 17:
        greeting_time = "Good afternoon!"
    elif 17 <= current_hour < 21:
        greeting_time = "Good evening!"
    else:
        greeting_time = "Hello there, night owl!"

    greet_message = f"{greeting_time} Master, Jarvis is here for you."
    print(greet_message)
    say(greet_message)

    # Ask how the assistant can help
    assistance_message = "What can I assist you with today?"
    print(assistance_message)
    say(assistance_message)

def handle_query_wt(query):
    for i in time_phrases:
        if i in query.lower():
            time_message = get_time()
            say(time_message)
            print(time_message)
            return True
        
    for i in weather_phrases:
        if i in query.lower():
            weather_info = get_weather_info()
            say(weather_info)
            print(weather_info)
            return True


def Exit(query):
    quit_phrases = [
        "Goodbye", "Bye", "See you later", "Talk to you later", "Catch you later", 
        "Take care", "I'm done", "That's all for now", "End conversation", 
        "Exit", "Stop", "Thanks, that's it", "Signing off", 
        "Shut down", "Quit", "Good night", "I'm leaving"
    ]
    for phrase in quit_phrases:
        if phrase.lower() in query.lower():
            return True
    return False
