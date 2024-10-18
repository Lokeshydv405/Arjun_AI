import speech_recognition as sr
from Basic_Utilization.Say import say

from mtranslate import translate
 
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        query = translate_text(query)
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...",end='\n')
        say("Say that again please...")
        return None
    return query


def translate_text(text, to_lang='en'):
    engligh_text =  translate(text, to_lang)
    return engligh_text

if __name__ == "__main__":
    sample_text = "how was the day? aaj din kaisa raha?"
    translated_text = translate_text(sample_text, 'en')
    print(f"Original text: {sample_text}")
    print(f"Translated text: {translated_text}")