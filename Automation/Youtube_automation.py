import pywhatkit as ktimpo
import pyautogui as ui
import time
import webbrowser
import pygetwindow as gw
global playing
playing = True
def is_youtube_active():
    try:
        # Get the title of the currently active window
        active_window = gw.getActiveWindow()
        return active_window and 'youtube' in active_window.title.lower()
    except Exception as e:
        print(f"Error checking active window: {e}")
        return False

def open_youtube_search(text):
    webbrowser.open('https://www.youtube.com/')
    time.sleep(2)
    ui.press('/')
    ui.write(text)
    time.sleep(1)
    ui.press('enter')

def youtube_search(text):
    time.sleep(2)
    ui.press('/')
    ui.write(text)
    time.sleep(1)
    ui.press('enter')

def play_music_on_youtube(text):
    ktimpo.playonyt(text)

def play_pause(command):    
    ui.press('space')

def mute_unmute():
    ui.press('m')

def stop_video():
    ui.press('spacebar')

def seek_backward_5():
    ui.press('left')

def seek_forward_5():
    ui.press('right')

def seek_backward_10():
    ui.press('j')

def seek_forward_10():
    ui.press('l')

def skip_next_frame():
    ui.press('.')

def skip_previous_frame():
    ui.press(',')

def speed_up():
    ui.hotkey('shift', '>')

def slow_down():
    ui.hotkey('shift', '<')

def seek_to_start():
    ui.press('0')

def seek_to_end():
    ui.press('end')

def increase_volume():
    ui.press('up')

def decrease_volume():
    ui.press('down')

def seek_by_percentage(percentage):
    if 0 <= percentage <= 9:
        ui.press(str(percentage))

def go_to_search():
    ui.press('/')

def toggle_fullscreen():
    ui.press('f')

def toggle_captions():
    ui.press('c')

def next_video():
    ui.hotkey('shift', 'n')

def previous_video():
    ui.hotkey('shift', 'p')

def open_miniplayer():
    ui.press('i')

# Command Handler
def command_handler(command):
    if 'open youtube' in command.lower():
        webbrowser.open('https://www.youtube.com/')
        command = command.replace('open youtube',"").strip()
        
    if not is_youtube_active():
        print("YouTube is not active.")
        return
    if "search" in command:
        search_text = command.replace("search", "").strip()
        youtube_search(search_text)
    elif "play" in command:
        play_music_on_youtube(command.replace("play", "").strip())
    elif command == "play video":
        play_pause('play')
    elif command == "pause video":
        play_pause('pause')
    elif command == "mute":
        mute_unmute()
    elif command == "stop video":
        stop_video()
    elif command == "next video":
        next_video()
    elif command == "previous video":
        previous_video()
    elif command == "seek backward a bit":
        seek_backward_5()
    elif command == "seek forward a bit":
        seek_forward_5()
    elif command == "seek backward":
        seek_backward_10()
    elif command == "seek forward":
        seek_forward_10()
    elif command == "increase volume":
        increase_volume()
    elif command == "decrease volume":
        decrease_volume()
    elif command == "fullscreen":
        toggle_fullscreen()
    elif command == "toggle captions":
        toggle_captions()
    elif command == "miniplayer":
        open_miniplayer()
    elif command == "skip next frame":
        skip_next_frame()
    elif command == "skip previous frame":
        skip_previous_frame()
    elif command == "increase speed":
        speed_up()
    elif command == "reduce speed":
        slow_down()
    elif command == "go to start":
        seek_to_start()
    elif command == "go to end":
        seek_to_end()
    else:
        print("Command not recognized.")

# Main Loop
if __name__ == "__main__":
    while True:
        user_input = input("Enter a command for YouTube (or 'exit' to quit): ").lower()
        if user_input == 'exit':
            break
        command_handler(user_input)
