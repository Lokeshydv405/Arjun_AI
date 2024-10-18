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
    # elif "play" in command:
    #     play_music_on_youtube(command.replace("play", "").strip())
    if "play" in command and "video" in command:
        play_pause('play')
    elif "pause" in command and "video" in command:
        play_pause('pause')
    elif "mute" in command:
        mute_unmute()
    elif "stop" in command and "video" in command:
        stop_video()
    elif "next" in command and "video" in command:
        next_video()
    elif "previous" in command and "video" in command:
        previous_video()
    elif "seek" in command and "backward" in command and "bit" in command:
        seek_backward_5()
    elif "seek" in command and "forward" in command and "bit" in command:
        seek_forward_5()
    elif "seek" in command and "backward" in command:
        seek_backward_10()
    elif "seek" in command and "forward" in command:
        seek_forward_10()
    elif "increase" in command and "volume" in command:
        increase_volume()
    elif "decrease" in command and "volume" in command:
        decrease_volume()
    elif "fullscreen" in command:
        toggle_fullscreen()
    elif "toggle" in command and "captions" in command:
        toggle_captions()
    elif "miniplayer" in command:
        open_miniplayer()
    elif "skip" in command and "next" in command and "frame" in command:
        skip_next_frame()
    elif "skip" in command and "previous" in command and "frame" in command:
        skip_previous_frame()
    elif "increase" in command and "speed" in command:
        speed_up()
    elif "reduce" in command and "speed" in command:
        slow_down()
    elif "go" in command and "start" in command:
        seek_to_start()
    elif "go" in command and "end" in command:
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
