import os
import webbrowser
import datetime
from pytube import Search
from Chatting.Chat import chat
from Automation.Open_applications import Open_Apps, Open_websites
from Basic_Utilization.AI_Prompts import ai
from Basic_Utilization.Say import say        
from Basic_Utilization.On_Start import greet,Exit,handle_query_wt
from Basic_Utilization.TakeCommand import takecommand
from Automation.Search_Control import handle_query
from Automation.Youtube_automation import command_handler
from TodoList.Task_functions import ToDOmain
def main():
    print("Arjun is online now")
    greet()            
    youtube_mode = 0
    while True:
        query = takecommand()
        Exit_response = Exit(query)
        if Exit_response:
            break
        if query is None:
            continue
        if 'enter youtube' in query.lower():
            say("Entering YouTube mode")
            youtube_mode = 1
            continue
        
        if 'exit youtube' in query.lower():
            say("Exiting YouTube mode")
            youtube_mode = 0
            continue
        
        if youtube_mode:
            command_handler(query)
            continue

        # Check for application or website commands
        response = handle_query_wt(query)
        if response:
            continue
        
        response = Open_websites(query)
        if response:
            continue

        response = Open_Apps(query)
        if response:
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
        

        # ToDoList Related Commands
        ToDOList_ress = ToDOmain(query)
        print(ToDOList_ress)
        if ToDOList_ress:
            print("-"*30)
            continue
        
        # Default response
        response = chat(query)
        say(response)

if __name__ == '__main__':
    main()
