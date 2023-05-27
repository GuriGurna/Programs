import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os 
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
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

    else:
        speak("Good Evening!")

    speak("I am siri. Please tell  me how may i help you")

def takecommand():
    #it takes microphone input from the user and returns string output 
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query =r.recognize_google(audio, language='en-us') 
        print(f"Used said: {query}\n")

    except Exception as e:
        print("say that again please...")
        return "None"
    return query

def sendEmail(to , content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('gurigurnajarvis@gmail.com','1234567890')
    server.sendmail('gurigurnajarvis@gmail.com',to , content)
    server.close()

if __name__ == "__main__":
    wishMe()                  
    while True:
        
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")        

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")  
            
        elif 'open whatsapp' in query:
            webbrowser.open("whatsapp.com")    

        elif 'open telegram' in query:
            webbrowser.open("telegram.com")

        elif 'open youtube ' in query:
            webbrowser.open("youtube.com")        

        elif 'the time ' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {strtime}")

        elif 'open code' in query:
            codepath = "C:\\Users\\DELL\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code\\Visual Studio Code.lnk"   
            os.startfile(codepath)

        elif 'send email to guri' in query:
            try:
                speak("what should i say?") 
                content = takecommand()
                to = "gurigurna327@gmail.com"
                sendEmail(to ,content)
                speak("email has been sent!")
            except Exception as e:
                print(e)
                speak("not able to send this email")    