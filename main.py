import os
import webbrowser
import datetime
from pytube import Search
from Chatting.Chat import chat
from Navigation.Open_applications import Open_Apps, Open_websites
from Basic_Utilization.AI_Prompts import ai
from Basic_Utilization.Say import say        
from Basic_Utilization.On_Start import greeting,Exit,handle_query_wt
from Basic_Utilization.TakeCommand import takecommand
from Navigation.Music_Control import handle_query

def main():
    print("Jarvis is online now")
    greeting()            

    while True:
        query = takecommand()
        if query is None:
            continue

        # Check for application or website commands
        response = handle_query_wt(query)
        if response:
            continue
        
        response = Open_websites(query)
        if response:
            say(response)
            continue

        response = Open_Apps(query)
        if response:
            say(response)
            continue

        response = handle_query(query)
        if response:
            # say('It is playing')
            continue

        # Handle specific commands
        if "it's time to meet her" in query.lower():
            say("Wait is over sir, I am calling her")
            webbrowser.open("https://meet.google.com/")
            continue
        
        if 'write' in query.lower():
            ai(query)
            continue
        
        Exit_response = Exit(query)
        if Exit_response:
            say("Good Bye sir, It was my please to assist you ")
            break

        # Default response
        response = chat(query)
        say(response)

if __name__ == '__main__':
    main()
