import pyttsx3  
import speech_recognition as sr      
import datetime
import wikipedia 
import webbrowser
import random
import sys
import time
import os
import os.path
import requests
import cv2     
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices');
# print(voices[0].id)
engine.setProperty('voices', voices[0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

#to wish
def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")

    if hour >= 0 and hour <= 12:
        speak(f"good morning, its {tt}")
    elif hour >= 12 and hour <= 18:
        speak(f"good afternoon, its {tt}")
    else:
        speak(f"good evening, its {tt}")
    speak("i am online sir. please tell me how may i help you")


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def  takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            # r.pause_threshold = 1
            # r.adjust_for_ambient_noise(source)
            # audio = r.listen(source)
            audio = r.listen(source,timeout=4,phrase_time_limit=7)
            
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            speak("Say that again please...")
            return "none"
        query = query.lower()
        return query

    def run(self):
        self.TaskExecution()
        # speak("please say wakeup to continue")
        # while True:
        #     self.query = self.takecommand()
        #     if "wake up" in self.query or "are you there" in self.query or "hello" in self.query:
        #         self.TaskExecution()


    def TaskExecution(self):
        wish()
        while True:
            self.query = self.takecommand()

            if "open notepad" in self.query:
                npath = "C:\\Windows\\system32\\notepad.exe"
                os.startfile(npath)

            elif 'wikipedia' in self.query:      #if wikipedia found in the query then this block will be executed
                speak('Searching Wikipedia...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2) 
                speak("According to Wikipedia")
                # print(results)
                speak(results)

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")    
                speak(f"Sir, the time is {strTime}")

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif 'open google' in self.query:
                webbrowser.open("www.google.com")

            elif "open stackoverflow" in self.query:
                webbrowser.open("www.stackoverflow.com")

            elif "open adobe reader" in self.query:
                apath = "C:\\Program Files (x86)\\Adobe\\Reader 11.0\\Reader\\AcroRd32.exe"
                os.startfile(apath)

            elif "open command prompt" in self.query:
                os.system("start cmd")

            # elif 'play music' in query:
            #     music_dir = "D:\\SAKSHI MAIN\\My Songs\\fav songs"
            #     songs = os.listdir(music_dir)
            #     print(songs)    
            #     os.startfile(os.path.join(music_dir, songs[0]))

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif "you can sleep" in self.query or "sleep now" in self.query:
                speak("okay sir, i am going to sleep you can call me anytime.")
                # sys.exit()
                # gifThread.exit()
                break


startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("D:/Wallpaper/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("D:/Wallpaper/T8bahf.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)



app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())



