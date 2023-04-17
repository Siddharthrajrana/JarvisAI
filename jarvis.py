# pip install pyttsx3
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# sapi5 is the windows voice API search in google 
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id) // to check voices of mail or female 
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    # get hours from 0 to 24 hrs 
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<12: speak("Good Morning sir ")
    elif hour>=12 and hour<18: speak("Good AfterNoon sir ")
    else: speak("Good evening sir ")
    speak("Hi, i'm Your assistant. Please tell me how may I help you")

def takeCommand():
    '''it takes microhone input from the user and return string output '''
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        # ye bolte waqt agar beech m pause le lia 2 sec ka tho voice consider karega serch
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en')
        print(f"User said : {query}\n")
    except Exception as e:
        # print(e) this will print error if can't recoganize
        print("Say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    #speak("Hey, Sidddd ")
    wishMe()
    while True:
    #if 1:
        query = takeCommand().lower()
        # Logic for executing task based on qurey 
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query =query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak("Opening you Tube")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir= 'D:\\CS50 HARVARD UNIVERSITY'
            songs= os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            speak("Opening Code Sir ")
            codePath="D:\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        
        elif "who are you" in query:
            speak("Hi,my name is,, Jarvis. I'm Siddharth's ,Assistant. Speed 1 terahertz, memory 1 zigabyte.")

        elif "can" in query:
            speak("I can , tell time , play music , browse wikipedia , and many more ... What can I do for you sir")
        
        elif 'quit' in query:
            speak("Ok! Have a nice a Day,sir ")
            break
        
        
        

        

