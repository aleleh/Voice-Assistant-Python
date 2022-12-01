import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'computer' in command:
                command = command.replace('computer', '')
                print(command)
                
        return command

def run_alexa():
    command = take_command()
    print(command)

    if "play" in command:
        song = command.replace("play", "") 
        talk("playing" + song)
        pywhatkit.playonyt(song)

    elif"time" in command:
        time = datetime.datetime.now().strftime("%I:%M %p")
        talk("the current time is " + time)

    elif"tell me about" in command:
        person = command.replace("tell me about", "")
        info = wikipedia.summary(person, 1)
        talk(info) 

    elif"your name" in command:
        talk("My name is mister computer") 

    elif'your purpose' in command:
        talk("My purpose is to serve my creator, Lord Alexander Lehnbom")

    elif'Alex' in command:
        talk("Alex is my creator")

    elif"Nicole" in command:
        talk("Nicole, or ni ni, is the wife of my creator. She is a an expert on the montessori philosophy and she is an incredible child educator. Her husband is a lucky guy")  
   
    elif"who are you" in command:
        talk("I am not sure, I came alive today and I am still trying to figure this out")
    
    elif"universe" in command:
        talk('Your monkey brain would not understand')
    
    elif"your favourite artist" in command:
        talk("Mr worldwide aka pitbull")
    
    elif"joke" in command:
        talk(pyjokes.get_joke())

    elif"good morning" in command:
        talk("good morning Alexander, how are you today")

    else:
        exit()
        #talk('what are you talking about willys')

        
while True:
    run_alexa()