import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import time
import os
import sys
import cv2
import pywhatkit as kit 
import smtplib
import pyautogui
import psutil
import PyPDF2

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio) 
    print(audio)
    engine.runAndWait()

def wishMe():   
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%H:%M:%S")

    if hour >= 0 and hour <= 12:
        speak(f"Good morning!!, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"Good afternoon!!, its {tt}")
    else:
        speak(f"Good evening!!, its {tt}")

    speak("I am online sir. Please tell me how may I help you")

#to send email
def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('gaikwadsakshi448@gmail.com', '9403498352')
    server.sendmail('gaikwadsakshi448@gmail.com', to, content)
    server.close() 

def  takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source,timeout=5,phrase_time_limit=8)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please...")
        return "none"
    return query

# To read PDF
def pdf_reader():
    book = open('py3.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book) #pip install PyPDF2
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages} ")
    speak("sir please enter the page number i have to read")
    pg = int(input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)
    # jarvis speaking speed should be controlled by user


if __name__ == "__main__": #main program
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif "hello" in query or "hey" in query:
                speak("hello sir, may i help you with something.")
            
        elif "how are you" in query:
                speak("i am fine sir, what about you.")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        if "open notepad" in query:
            npath = "C:\\Windows\\system32\\notepad.exe"
            os.startfile(npath)

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'play music' in query:
            music_dir = "D:\\SAKSHI MAIN\\My Songs\\fav songs"
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'open code' in query:
            codePath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam', img)
                k = cv2.waitKey(50)
                if k==27:
                    break;
            cap.release()
            cv2.destroyAllWindows()

        elif "song on youtube" in query:
            kit.playonyt("see you again")

        # elif "send message to mummy" in query:
        #     speak("What should i say..?")
        #     say = takeCommand()
        #     # time.sleep(120)
        #     # speak("Set the time to deliever the message!")
        #     kit.sendwhatmsg('+919623538026',13,33,f"{say}")
        #     speak("message sent!")

        elif "send whatsapp message" in query:
            kit.sendwhatmsg("+917263075543", "Hello.. Sakshi here.. How e u..?",15,48)
            time.sleep(120)
            speak("message has been sent")

        #To send text message
        elif "send message" in query:
            speak("Sir what should i say..?")
            msz = takeCommand()

            from twilio.rest import Client

            account_sid = 'AC72e13e968b053027178679d9c008428c'
            auth_token = 'f8c94f134e61608362035522dc3bc358'
            client = Client(account_sid, auth_token)

            message = client.messages \
                .create(
                    body= msz,
                    from_='+15625218760',
                    to='+917887419530'
                )

            print(message.sid)

        #to send mail
        elif "email to sakshi" in query:
            try:
                speak("what should i say?")
                content = takecommand().lower()
                to = "EMAIL OF THE OTHER PERSON"
                sendEmail(to,content)
                speak("Email has been sent to sakshi")
            except Exception as e:
                print(e)
                speak("sorry sir, i am not able to sent this mail to sakshi")

        #to close any application
        elif "close notepad" in query:
            speak("okay sir, closing notepad")
            os.system("taskkill /f /im notepad.exe")
        
        # To take screenshot 
        elif "take screenshot" in query or "take a screenshot" in query:
            speak("sir, please tell me the name for this screenshot file")
            name = takeCommand()
            speak("please sir hold the screen for few seconds, i am taking sreenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, the screenshot is saved in our main folder. now i am ready for next command")
        
        #To shutdown system
        elif "shutdown the system" in query:
            os.system("shutdown /s /t 5")

        elif "restart the system" in query:
            os.system("shutdown /r /t 5")

        elif "sleep the system" in query:
            os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

        #to set an alarm
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if nn==22: 
                music_dir = 'D:\\My music'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))
        
        #To check battery percentage 
        elif "how much power left" in query or "how much power we have" in query or "battery" in query:
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir our sysytem have {percentage} percent battery")
            if percentage>=75:
                speak("we have enough power to continue our work")
            elif percentage>=40 and percentage<=75:
                speak("we should connect our system to charging point to charge our battery")
            elif percentage<=15 and percentage>=30:
                speak("we dont have enough power to work, please connect to charging")
            elif percentage<=10:
                speak("we have very low power, please connect to charging the system will shutdown very soon")
        
        #To Read PDF file or book
        elif "read pdf" in query or "read book" in query:
                pdf_reader()


        elif "no thanks" in query:
            speak("thanks for using me sir, have a good day.")
            sys.exit()

        # speak("sir, do you have any other work")
       