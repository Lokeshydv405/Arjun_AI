import subprocess
import webbrowser
import os
import time

def start_Server():
       server_process = subprocess.Popen(["python", "TodoList/TodoList_main.py"], shell=True)
       return server_process
   
def open_todo_list():
    # Start the Flask server
    # Assuming 'server.py' is the name of your server script
 
    
    # Wait a few seconds for the server to start
    time.sleep(3)
    
    # Path to the index.html file
    html_path = os.path.abspath("TodoList/index.html")
    # Open the index.html in the default web browser
    webbrowser.open(f"file://{html_path}")
    
    return  # Return the process in case you want to close it later

def stop_todo_list(server_process):
    server_process.terminate()
    print("To-Do List server stopped.")




# Example call
# This should be called based on Arjun's recognized prompt
# open_todo_list()
# time.sleep(10)
# stop_todo_list()