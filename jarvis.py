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
        print("Listining....")
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
    while True:
        query = takeCommand().lower()

        #Logic for executing task based on queries...
        if 'wikipedia' in query:
            speak("Searching in wikipedia....")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia..")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open whatsapp' in query:
            wpath = "C:\\Users\\ks282\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(wpath)

        elif 'open gmail' in query:
            webbrowser.open("gmail.com")

        elif 'open github' in query:
            webbrowser.open("github.com")

        elif 'the time' in query:
            strTime = datetime.now().strftime("%H:%M:%S")
            speak(f"The time is: {strTime}")

        elif 'open code' in query:
            codePath = "D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'play songs' in query:
            webbrowser.open("wynk.in/music")

