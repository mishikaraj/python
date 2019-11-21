import os
import sys
import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import wikipedia
import webbrowser
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():   
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("good afternoon!")
    
    else:
        speak("Good evening")

    speak("I am jarvis Sir,please tell me how may I help you")

def takeCommand():
    #take microphone input from user and returns string output

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
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('abc@gmail.com', 'your-password')
    server.sendmail('abc@gmail.com', to, content)
    server.close()

    
if __name__ == "__main__":
    wishMe()
    while True:
    
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open whatsapp' in query:
            webbrowser.open("web.whatsapp.com")

        elif 'play music' in query:
            music_dir = r'D:\Mishika\music\@@music\faded'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open code' in query:
            codePath = r"C:\Users\Mishika\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(codePath)
        
        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "abc@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")

        elif 'exit' in query:
                exit()
