from gtts import gTTS
import os
import platform

def speak(text):
    tts = gTTS(text=text, lang='en')
    file = "response.mp3"
    tts.save(file)
    os.system(f"start {file}")
