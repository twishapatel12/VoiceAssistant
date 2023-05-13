# voice assistant 

import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

# youtube_music = {"mehbooba":"https:\\music.youtube.com\\watch?v=weLIci9JtAw&feature=share","chup chup ke":"https:\\music.youtube.com\\watch?v=PMQfqWjwPis&feature=share"}
# print((type(youtube_music)))
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    speak("Hello I am Siri ! Please tell how may I help you?")
def takeCommand():

    '''
    It takes microphone input
    :return: string output
    '''

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-IN')
        print(f"User said:{query}\n")
    except Exception as e:
        #print(e)
        print("Say that again please....")
        return "None"   # here it specifies none string
    return query
    
if __name__ == '__main__':
    # speak("Hiii Twisha")
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()
        # logic for executing tasks based on query
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)
            speak(f"According to wikipedia{results}")

        elif 'open youtube' in query:
            webbrowser. get("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s")
            webbrowser.open("https:\\youtube.com")
            
        elif 'open google' in query:
            url ='https:\\google.com'
            webbrowser. get("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s")
            webbrowser.open(url)

        elif 'open stackoverflow' in query:
            webbrowser. get("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s")
            webbrowser.open("https:\\stackoverflow.com")

        elif 'play music' in query:
            music_dir='D:\\Songs'
            songs = os.listdir(music_dir)
            # print(songs)
            d = random.choice(songs)
            os.startfile(os.path.join(music_dir,d)) # for random songs
            # os.startfile(os.path.join(music_dir,songs[0])) //for songs to be in a list 0 is the index 
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\Twisha\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'thank you' in query:
            speak("Ok see you for the next time......Byeee")
            break
