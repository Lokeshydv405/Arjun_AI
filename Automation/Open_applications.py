import os
import webbrowser
import random
from Basic_Utilization.Say import say
from databse.openapplications import app_opening_dialogues,website_opening_dialogues

# Define applications and their executable paths
applications = [
    ['WhatsApp', "start whatsapp:"],
    ['Excel', "C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE"],
    ['PowerPoint', "C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE"],
    ['Google Chrome', "C:/Program Files/Google/Chrome/Application/chrome.exe"],
    ['Camera', "start ms-camera:"],  # Default command for opening Camera
    ['Calendar', "start outlookcal:"],  # Default command for opening Calendar
    ['Canva', "https://www.canva.com/"]  # Web-based, so we use the URL
]

# Open Applications based on user query
def Open_Apps(query):
    for application in applications:
        if f"open {application[0].lower()}" in query.lower():
            app_name = application[0]
            if application[1].startswith("http"):  # Check if it's a URL
                webbrowser.open(application[1])
            else:
                os.system(f'"{application[1]}"')
            
            # Pick a random dialogue for the app
            to_say = random.choice(app_opening_dialogues[f'{application[0]}'])
            print(to_say,end='\n')
            say(to_say)
            return True
    
    return False

# Open Websites based on user query
def Open_websites(query):
    sites = [
        ['YouTube', 'https://www.youtube.com/'],
        ['Wikipedia', 'https://www.wikipedia.com/'],
        ['LMS', 'https://lms.iitmandi.ac.in/'],
        ['Google', 'https://www.google.com/']
    ]
    for site in sites:
        if f"open {site[0].lower()}" in query.lower():
            if 'chrome' in query.lower():
                return 
            else:
                webbrowser.open(site[1])
            
            # Pick a random dialogue for the website
            to_say = random.choice(website_opening_dialogues[f'{site[0]}'])
            print(to_say,end='\n')
            say(to_say)
            return True

    return False

# Example usage
if __name__ == "__main__":
    # Load dialogues from JSON
    # dialogues = load_dialogues()

    # Example queries
    app_query = "open Excel"
    site_query = "open YouTube"

    # Opening applications or websites based on user query
    response = Open_Apps(app_query)
    if not response:
        response = Open_websites(site_query)
    
    print(response)