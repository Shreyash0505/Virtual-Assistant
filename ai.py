from re import search
from time import sleep
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser as wb
import os
import sys
import pywhatkit as kit
import pyautogui as pg
import pyjokes as pj

#initializing engine(google)
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate',180)

#global variable for chorme path
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"

#define a main function which consists of in-out conditions or give test cases which will access a list
def main():
    wishme()
    take_command()
    while True:
        command = take_command().lower()

        # Logic for executing tasks based on query/ input given
        if 'on wikipedia' in command:
            wikipedia()
            
        
        elif "good morning" in command:
            speak("good morning sir. How are you!!!")

        
        elif "how are you"in command:
            speak("I am good sir, How may i help you!!")

       
        elif 'open youtube' in command:
            speak("ok sir")
            wb.get(chrome_path).open("youtube.com")
            
        
        elif 'search' in command:
            speak("sir what should i search")
            search =take_command().lower()
            wb.get(chrome_path).open_new_tab(search + ".com")
            print(search)

        
        elif 'open stackoverflow' in command:
            url = "https://www.stackoverflow.com/"
            wb.get(chrome_path).open(url)  

        
        elif 'play music' in command:
            music_dir = 'D:\\Non Critical\\songs\\Favorite Songs2'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        
        elif 'the time' in command:
            strTime = datetime.datetime.now()
            curr_time = strTime.strftime("%I:%M %p")    
            speak(f"Sir, the time is {curr_time}")

        
        elif 'open code' in command:
            speak('opening vs code')
            codePath = "E:\Microsoft VS Code\Code.exe"
            os.startfile(codePath)

        
        elif 'close code' in command:
            speak("ok sir, closing vs code")
            os.system('TASKKILL /F /IM Code.exe')
        
        
        elif 'open chrome' in command:
            get_chrome()
            speak("done sir")
        
        
        elif 'close chrome' in command:
            speak('ok sir')  
            os.system('TASKKILL /F /IM chrome.exe')

        
        elif 'send message' in command:
            speak('enter the no sir')
            ph_no = input()
            print(ph_no)
            msg = input()
            print(msg)
            speak('sending message sir')
            kit.sendwhatmsg_instantly(ph_no,msg,10)
        
        
        elif 'open whatsapp' in command:
            speak('opening sir please wait')
            wb.get(chrome_path).open("https://web.whatsapp.com")
            
            
        
        elif 'shutdown' in command:
            speak('shuttig down in 10 seconds')
            sleep(10)
            os.system('shutdown /s /t 1')
        
        
        elif 'open github' in command:
            speak('opening sir')
            get_github()

        
        elif 'task manager' in command:
            speak('please wait a second')
            pg.hotkey("ctrl","shift","esc")
        
        
        elif 'running task' in command:
            pg.hotkey('winleft','tab')

        
        elif 'screenshot' in command:
            speak('taking screenshot')
            pg.hotkey('winleft','prtscr')
            speak('done')

        
        elif 'close app' in command:
            speak('closing sir')
            pg.hotkey("alt","f4")
        
        
        elif 'play' in command:
            speak('what should i play sir')
            song = command.replace('play','')
            speak('playing ' + song)
            kit.playonyt(song)
        
        
        elif 'joke' in command:
            joke()
        
        
        elif 'quit now' in command:
            speak('ok sir, have a good day')
            sys.exit() 


def wikkipedia():
    speak('Searching Wikipedia...')
    query = query.replace("wikipedia", "")
    results = wikipedia.summary(query, sentences=3)
    speak("According to Wikipedia")
    speak(results)

def joke():
    speak(pj.get_joke())

def get_chrome():
    url = "https://www.google.co.in/"
    wb.get(chrome_path).open(url)

def get_github():
    speak('done sir')
    url = 'https://github.com/Shreyash0505/Bio' 
    wb.get(chrome_path).open(url)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():       
    hour = int(datetime.datetime.now().hour)
    if hour>= 0 and hour<=12:
        speak("Good Morning Sir. How are you")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon Sir. How are you")
    else:
        speak("Good Evening Sir. How are you")

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("evaluating..")
        user_input = r.recognize_google(audio, language = 'en-in')
        print(f"User said: {user_input} \n")

    except Exception as e:
        print(e)
        print("please speak again!!")
        speak('i was unable to get that sir, can you please repeat it again')
        return 'None'
    
    return user_input


if __name__ == '__main__':
    main()
    
