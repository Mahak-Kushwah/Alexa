import speech_recognition as sr   #this module is for recognizing the voice of the user
import pyttsx3                    #text to speech version 3 module
import pywhatkit                  #this module is to search on youtube
import datetime                   #this module is to show date and time
import wikipedia                  #this module is to search from wikipedia
import pyjokes                    #this module is to show jokes

listener = sr.Recognizer()        #listener will listen to the voice and recognize the voice
engine = pyttsx3.init()           #engine variable will speak to user and initialize the engine
voices = engine.getProperty('voices')   #to get the voice of the female
engine.setProperty('voice', voices[1].id)  #to set the voice of the female

def talk(text):      #repeat the commands given by the user
    engine.say(text)
    engine.runAndWait()

def take_command():   #take commands from alexa and user want to do some work using the alexa
    try :
        with sr.Microphone() as source :    #source of our audio
            print("listening.......")
            voice = listener.listen(source)   #voice variable listen to the source of the audio
            #command variable will listen to the voice to the google api and google will return you the text
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace("alexa"," ")    #alexa will be removed from the string
                talk(command)
    except :     #does nothing
        pass
    return command

def run_alexa():    #take the command and run the alexa
    command = take_command()
    print(command)
    if 'play' in command:    #play a song
        song = command.replace("play"," ")   #play will be removed from the string
        talk("playing"+song)
        pywhatkit.playonyt(song)  #playonyt means play on youtube
    elif 'time' in command :
        time = datetime.datetime.now().strftime('%I:%M %p')   #shows the current time in AM or PM
        talk('Current time is :' + time)
        print(time)
    elif 'who is' in command:
        person = command.replace("who is"," ")    #who is will removed from the string
        info = wikipedia.summary(person,1)       #search from wikipedia
        print(info)
        talk(info)
    elif 'date' in command:
        talk('sorry,I have a headache')
    elif 'what is your name' in command:
        talk('My name is Alexa')
    elif 'are you single' in command:
        talk('I am in a relationship with WiFi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'who created you' in command:
        talk('i was created by Mahak Kushwah')
    elif 'how are you' in command:
        talk("I am fine,Thank you")
        talk('How are you')
    elif 'fine' in command:
        talk('Its is good to know that you are fine')
    elif 'exit' in command:
        talk('Thank for giving me the time')
        exit()
    else :
        talk("Please say the command again....")

while True:
    run_alexa()
