import webbrowser
import re
from youtubesearchpython import VideosSearch
from Basic_Utilization.Say import say
from Basic_Utilization.TakeCommand import takecommand

commands = {
    'music': 'Which music would you like to listen to today?',
    'video': 'Which video would you like to watch today?',
    'movie': 'Which movie would you like to watch today?',
    'podcast': 'Which podcast would you like to listen to today?',
}

media_keywords = {
    'music': ['listen to', 'play', 'music', 'song', 'track', 'album', 'genre'],
    'video': ['watch', 'play', 'video', 'clip'],
    'movie': ['watch', 'movie', 'film'],
    'podcast': ['listen to', 'play', 'podcast', 'episode'],
}

def extract_details(query):
    patterns = [
        r'listen to (?P<detail>.+)',
        r'play (?P<detail>.+)',
        r'watch (?P<detail>.+)',
        r'I want to listen to (?P<detail>.+)',
        r'I want to watch (?P<detail>.+)',
        r'I would like to listen to (?P<detail>.+)',
        r'I would like to watch (?P<detail>.+)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, query, re.IGNORECASE)
        if match:
            return match.group('detail').strip()
    return None

def play_media(media_type, name):
    say(f"Searching for {name} on YouTube...")
    search = VideosSearch(name, limit=1)
    search_results = search.result()
    if search_results['result']:
        first_result = search_results['result'][0]
        video_url = first_result['link']
        webbrowser.open(video_url)
        say(f"Playing {name} for you")
    else:
        say("Sorry, I couldn't find that on YouTube.")
    return True

def handle_query(query):
    query_lower = query.lower()

    for media_type, keywords in media_keywords.items():
        if any(keyword in query_lower for keyword in keywords):
            specific_detail = extract_details(query)
            
            if not specific_detail:
                say(commands[media_type])
                specific_detail = takecommand().lower()
            
            play_media(media_type, specific_detail)
            break
    else:
        return False
    return True

# # Example usage
if __name__ == "__main__":
    query = "I want to listen to music"  # This would come from the user's input
    handle_query(query)
