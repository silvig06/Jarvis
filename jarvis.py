
import pyttsx3  # For speak engine
import datetime
import speech_recognition as sr   # For speeh recognition
import wikipedia   # To search on wikipedia
import webbrowser   # To open website on Browser like youtube, LinkedIn, google etc.
#webbrowser.get('chrome')
import os
import random
import smtplib  # To send email.


engine = pyttsx3.init('sapi5')  # Creating engine to speak.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
print(voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am deepak sir. Please tell me how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:  # Getting from Microphone
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)   # Listening the input from Microphone
    try:
        print("Recognizing.....")
        query = r.recognize_google(audio, language="en-in")  
        # Jarvis is Recognizing what is said by User. 
        print(f"User said:\t {query} \n")
    except Exception as e :
        print("Say that again please.....")
        return "None"
    return query   


f = open('password.txt','r')
password = f.read()
f.close()	
fi = open('username.txt','r')
username = fi.read()
fi.close()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', port=587)
    server.ehlo()
    server.starttls()	
	
    server.login(username, password) # Read password from file.
    server.sendmail(username, to, content)
    server.close()


# MAIN BODY
if __name__=='__main__':
    #speak("Hello World")    
    wishMe()
    while True:
        query = takeCommand().lower()  
        # gettign a string here. Now we will perform our logics.
        # Our logics come here like wikipedia, time, music etc.
        # speak fucntion. 
        if "wikipedia" in query:
            try:
                speak("Searching wikipedia......")
                query = query.replace('wikipedia', "")
                results = wikipedia.summary(query, sentences=2)
                print(results)
                speak(results)
            except Exception as e:
                speak("Do not find any result. Search again.....")
        elif "open youtube" in query:
            webbrowser.open("youtube.com")
        elif "open google" in query:
            webbrowser.open("google.com")
        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")    
        elif "play music" in query:
            music_dir = "E:\\music"
            songs = os.listdir(music_dir)
            if songs:
                print(songs)
                play_song = random.choice(songs)
                os.startfile(os.path.join(music_dir, play_song )) # Use random module here to select random song.
            else:
                speak("Your Music Directory is empty...Add some songs in your Directory.")

        elif "the time" in query:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {time} ")
        elif "open slack" in query:
            try:
                path = "C:\\Users\\XYZ\\AppData\\Local\\slack\\slack.exe"
                os.startfile(path)
            except Exception as e:
                speak("Path of slack not found. Set it's path.")  

        elif "email to rahul" in query:
            # Make dictionary of name with thier email address.
            try:
                speak("what should I say? ")
                content = takeCommand()
				
                to = "sainihimanshi1998@gmail.com"
                sendEmail(to, content)
                speak("Sir, email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email.")    


        elif "quit" in query:
            break


