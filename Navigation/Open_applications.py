import os
import webbrowser

# Define applications and their executable paths
applications = [
    ['WhatsApp', "start whatsapp:"],
    ['Excel', "C:/Program Files/Microsoft Office/root/Office16/EXCEL.EXE"],
    ['PowerPoint', "C:/Program Files/Microsoft Office/root/Office16/POWERPNT.EXE"],
    ['Google Chrome', "C:/Program Files/Google/Chrome/Application/chrome.exe"],
    ['Camera', "start ms-camera:"],  # Default command for opening Camera
    ['Calendar', "start outlookcal:"],  # Default command for opening Calendar
    ['Canva', "https://www.canva.com/"],  # Web-based, so we use the URL
]

def Open_Apps(query):
    for application in applications:
        if f"open {application[0].lower()}" in query.lower():
            if application[1].startswith("http"):  # Check if it's a URL
                webbrowser.open(application[1])
            else:
                os.system(f'"{application[1]}"')
            return f"Opening {application[0]} for you"
    
    return False

def Open_websites(query):
    sites = [
        ['youtube', 'https://www.youtube.com/'],
        ['wikipedia', 'https://www.wikipedia.com/'],
        ['lms', 'https://lms.iitmandi.ac.in/'],
        ['google', 'https://www.google.com/']
    ]
    for site in sites:
        if f"open {site[0]}" in query.lower():
            webbrowser.open(site[1])
            return f"Opening {site[0]} for you"

    return False

# Example usage:
