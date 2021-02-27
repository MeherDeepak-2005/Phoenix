
from gtts import gTTS
import speech_recognition as sr
import time
import random
import playsound
import webbrowser
import os
import subprocess
from Chatgui import chatbot_response

r = sr.Recognizer()



def speak(audio_string):
    tts = gTTS(text=audio_string,lang='en')
    r = random.randint(1,200)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)
    
    
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.RequestError:
            print('going offline')

        except sr.UnknownValueError:
            print('i did not get that')

        voice_data = voice_data.lower()
        return voice_data
        
time.sleep(1)
while 1:
    voice_data = record_audio()

    msg = voice_data.lower()
    res = chatbot_response(msg)
    speak(res)

