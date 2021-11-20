import pyttsx3
from datetime import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import smtplib
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

print("Initializing Jarvis...")

#Speak function will pronounce the string which is passed to it.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
speak("Initializing Jarvis!!")


#This function will wish as per the current time
def wishMe():
    hour = int(datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon Sir!")
    else:
        speak("Good Evening Sir!")
    speak("I am Jarvis. How may I help you")


#This function will take command from microphone
def takeCommand():
    # Takes microphone input from user and convert it into string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listning....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recogninzing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Please say that again...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    takeCommand()
