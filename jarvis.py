import datetime
import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition, pip install pipwin, pipwin install pyaudio
import wikipedia #pip install wikipedia
import webbrowser
import os
import random


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good morning!")

    elif hour>=12 and hour<18:
        speak("Good Aftenoon")

    else:
        speak("Good Evening")

    speak("I am jackson Sir Please tell me how may i help you")

def takecommand():
    #it takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listining...")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)

        print("say that again please...")
        return "None"
    return query   

if __name__== "__main__":
    wishMe()
    #while True:
    if 1:
        query = takecommand().lower()

        #logic for executing task based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query .replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        #elif 'hello jackson' in query:
         #   speak('hello sir')

        elif 'open youtube' in query:
            speak('opening youtube')
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak('i am great as compare to this ass')
            webbrowser.open("google.com")
        
        elif 'open github' in query:
            webbrowser.open("github.com")

        elif'open coursera' in query:
            webbrowser.open("coursera.org")

        elif 'music' in query:
            music_dir = 'C:\\Users\\mukun\\Music\\mukudab#'
            songs = os.listdir(music_dir)
            print (songs)
            os.startfile(os.path.join(music_dir, songs[random.randrange (1,137)]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")
        
        elif 'open code' in query:
            codepath = "C:\\Users\\mukun\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        
        elif 'quit' in query:
            engine = pyttsx3.init()
            engine.say("Good bye!")
            engine.runAndWait()
            exit()

        elif 'open netflix' in query:
            webbrowser.open("netflix.com")

        elif 'open prime' in query:
            webbrowser.open("primevideo.com")

        elif 'open brave' in query:
            path = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
            os.startfile(path)

        elif 'open eagle' in query:
            pat = "C:\\EAGLE 9.6.2\\eagle.exe"
            os.startfile(pat)
        
        #elif 'roll a dice' in query:
         #   dice = random.randrange(1,6)
          #  print(dice)
           # speak(dice)