import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import requests
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon")

    else:
        speak("Good evening")
    speak("I am jarvis, how can i help you sir?")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...\n")
        return "None"

    return query

def Requestmodule():
    url = ('https://newsapi.org/v2/top-headlines?'
           'country=us&'
           'apiKey=5b60eb13cb5142e2ad201d95c3ef90de')
    response = requests.get(url)
    news = response.json()
    return news

def ReadNews():
    news = Requestmodule()
    info = dict(news).get('articles')
    print("Head lines....")
    i = 0
    while (i < 4):
        str = f"Headline: {i + 1}"
        print(str)
        speak(str)
        data = dict(info[i]).get('title')
        print(data)
        speak(data)
        i = i + 1
        print()

def searchWikipedia(query):
    speak("ok sir, Searching wikipedia")
    query = query.replace("wikipedia", " ")
    results = wikipedia.summary(query, sentences=2)
    speak("According to wikipedia,")
    print(results)
    speak(results)

def searchWeb(query):
    speak(f"ok sir, Opening {query}")
    webbrowser.open(f"{query}.com")

def playMusic():
    speak("ok sir, Playing music")
    music_dir = 'D:\\music'
    songs = os.listdir(music_dir)
    rnd = random.randint(0,len(songs))
    print(f"Now Playing, {songs[rnd]}")
    speak(f"Now Playing, {songs[rnd]}")
    os.startfile(os.path.join(music_dir, songs[rnd]))

def getTime():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    print(f"Its {strTime}")
    speak(f"Its {strTime}")

def openCode():
    speak("ok sir, Initializing visual studio code")
    codepath = "C:\\Users\\WINDOWS\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
    os.startfile(codepath)

def news():
    speak("Ok sir , Getting news")
    speak("Here are the today's headlines")
    ReadNews()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    f = open("password.txt", "r")
    pswd = f.read()
    server.login('youremail@address.com', pswd)
    server.sendmail('youremail@address.com', to, content)
    server.close()

def email():
    try:
        speak("what should i say, sir?")
        content = takeCommand()
        to = "youremail@address.com"
        sendEmail(to, content)
        speak("Email has been sent , sir")

    except Exception as e:
        print("Sorry sir ,I am not able to send this email")


def quitJarvis():
    speak("ok sir , Quitting application")
    speak("Thank you for your time sir, Have a nice day")
    exit()