import speech_recognition as sr
import webbrowser
import time
import os
import playsound
import random
from gtts import gTTS
from time import ctime


r = sr.Recognizer()

def recordAudio(ask = False) :
    with sr.Microphone() as source:
        if ask:
            IANARspeak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            IANARspeak("Sorry, I didn't understand")
        except sr.RequestError:
            IANARspeak('Sorry, my speech service is down')
        return voice_data

def IANARspeak(audioString):
    tts = gTTS(text = audioString, lang = 'en')
    r = random.randint(1, 10000000)
    audioFile = 'audio-' + str(r) + '.mp3'
    tts.save(audioFile)
    playsound.playsound(audioFile)
    print(audioString)
    os.remove(audioFile)

def respond(voice_data):
    if "what's your name" in voice_data or 'what is your name' in voice_data:
        IANARspeak('My name is IANAR.')
    if 'what time is it' in voice_data:
        IANARspeak(ctime())
    if 'search' in voice_data:
        search = recordAudio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        IANARspeak('Here is what I found for ' + search)
    if 'find location' in voice_data:
        location = recordAudio('What is the location?')
        url = 'https://google.nl/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        IANARspeak('Here is the location of ' + location)
    if 'Facebook password' in voice_data:
        IANARspeak('za1234')
    if 'thank you' in voice_data:
        IANARspeak('your welcome')
    if 'exit' in voice_data:
        IANARspeak('good luck')
        exit()

time.sleep(1)
IANARspeak('Hello New, how can I help you.')
print("example: What's your name")
print('         What time is it')
print('         search')

while 1:
    voice_data = recordAudio()
    print(voice_data)
    respond(voice_data)