from random import random
import sys
import time
import pyttsx3
import datetime
import requests
import wikipedia
import webbrowser
import speech_recognition as sr
import os
import cv2 
import random
from requests import get
import pyjokes
import pyautogui
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
import smtplib
import instaloader
import ssl
import PyPDF2
import math
import psutil

from tkinter import *
import datetime
import time
import winsound
import subprocess
import datetime

from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisui import Ui_jarvisui


engine = pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def systemstats():
    cpu =str(psutil.cpu_percent())
    print(cpu)
    speak(f"you have used {cpu}of cpu.")
    ram = str(psutil.virtual_memory()[2])
    speak (f" you have used{ram} of ram")

def pdf_reader():
    book = open('example.pdf ', 'rb')
    pdfReader = PyPDF2.PdfFileReader(book) 
    pages = pdfReader.numPages
    speak(f"Total numbers of pages in this book {pages} ") 
    speak ("  sir please enter the page number i have to read")
    pg = int (input("Please enter the page number: "))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak (text)

def wish():
    hour = int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<12:
        speak(f"good morning sir and the time is{tt}")

    elif hour>=12 and hour<18:
        speak(f"good afternoon sir and the time is{tt}")

    else:
        speak(f"good evening and the time is{tt}")
    
    speak("i am yourassistant sir how may i help you sir")




class MainThread (QThread):
    def __init__(self):
        super(MainThread,self).__init__()
    def run(self):
        speak("please say wakeup to continue")
        while True:
            self.query =self.takecommand()
            if "wake up" in self.query or "are you there" in self.query:
                self.TaskExecution() 
    def takecommand(self):

        r=sr.Recognizer()
        with sr.Microphone() as source:
            print("listening....")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("recognizing...")
            query = r.recognize_google(audio,language='en-in')
            print(f"user said:{query}\n")
        
        except Exception as e:
        # print(e)

            print("say that again please...")
            return "none"
        query = query.lower()
        return query
    
    def TaskExecution(self):
        wish()
        while True:
            self.query = self.takecommand().lower()

            if 'open notes' in self.query:
                 npath = "C:\\WINDOWS\\system32\\notepad.exe"
                 os.startfile(npath)


            elif ' command prompt' in self.query:
                 os.popen("start cmd")
            

            elif 'open camera' in self.query:
                cap = cv2.VideoCapture(0)
                while (True):
                    ret,img = cap.read()
                    cv2.imshow('webcam',img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break;
                cap.release()
                cv2.destroyAllWindows()

            elif 'play music' in self.query:
                    mpath = "D:\\music"
                    songs = os.listdir(mpath)
                    rd = random.choice(songs)
                    os.startfile(os.path.join(mpath,rd))
            
            elif "system info" in self.query or "systemdetails" in self.query:
                systemstats()


            elif "write down something" in self.query or "remember"in self.query: 
                speak("What should i write down sir")
                note = self.takecommand()
                remember = open("data.txt", 'w')

                remember.write(note)

                remember.close()

                speak("I have noted that" + note)

            elif "do you have anything" in self.query or "important" in self.query:

                remember = open('data.txt', 'r').read()
                speak ("You told me to remember that" + remember)



                    #online
            elif 'ip address' in self.query:
                    ip = get('https://api.ipify.org').text
                    speak(f"your IP addres is {ip}")

            elif 'open youtube' in self.query:
                    webbrowser.open("youtube.com")
                
            elif 'open google'in self.query:
                    speak("sir, what should i search on google")
                    cm = self.takecommand().lower()
                    webbrowser.open(f"{cm}")

            elif 'open facebook'in self.query:
                    webbrowser.open("www.facebook.com")

            elif 'open stackoverflow' in self.query:
                    webbrowser.open("stackoverflow.com/")
          

            elif "open insta" in self.query:
                webbrowser.open("instagram.com")

            elif 'wikipedia' in self.query:
                    speak('searching wikipedia...')
                    self.query =self.query.replace("wikipedia","")
                    results = wikipedia.summary(self.query,sentences=2)
                    speak("according to wikipedia")
                    #print(results)
                    speak(results)
                
            

                
            elif 'how is the weather'in self.query or'weather' in self.query:
                url = 'https://api.openweathermap.org/data/205/weatheer?appid=02ba5ef1db1237350b21a5bbdc426954a&q='#Open api link here
                res = requests.get(url)

                data = res.json()

                weather = data['weather'][0]['main'] 
                temp = data['main']['temp']
                wind_speed = data['wind']['speed']

                latitude = data['coord']['lat']
                longitude = data['coord']['lon']

                description = data['weather'][0]['description']
                speak('Temperature : {} degree celcius'.format(temp))
                print('Wind Speed : {} m/s'.format(wind_speed))
                print('Latitude : {}'.format(latitude))
                print('Longitude : {}'.format(longitude))
                print('Description : {}'.format(description))
                print('weather is: {} '.format(weather))
                speak('weather is : {} '.format(weather))


            

                    
            

                    #closing
                
            elif 'close notes' in  self.query:
                    speak("okay sir, closing notepad")
                    os.system("taskkill /f /im notepad.exe")

             


                        
                
            

                    #jokes
            elif 'joke' in self.query:
                    joke = pyjokes.get_joke()
                    speak(joke)

                    #about the power

            elif 'shutdown the laptop' in self.query:
                    os.system("shutdown /s /t 5")

            elif 'restart the laptop' in self.query:
                    os.system("shutdown /r /t 5")

            elif 'sleep the laptop' in self.query:
                    os.system("rundll32.exe Powrprof.dll,SetSuspendState 0,1,0")

            elif 'switch between windows'in self.query:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                    pyautogui.keyUp("alt")

            

                #mail
            elif " mail" in self.query:
                    speak("sir what should i say" )
                    if "send a file in "in self.query:
                        email = 'jarvis140300@gmail.com'
                        password = 'vishnu1435'
                        send_to_email = "vishnukoyyada01@gmail.com"           
                        
                        speak ("okay sir, what is the subject for this email")
                        self.query =self.takecommand().lower()
                        subject = self.query
                        # The Subject in the email
                        speak ("and sir, what is the message for this email")
                        self.query2 = self.takecommand().lower()
                        message = self.query2
                        speak("sir please enter the correct path of the file into the shell")
                        file_location = input ("please enter the path here")
                        speak("please wait , i am sending email now")
                        msg = MIMEMultipart()
                        msg['From'] = email
                        msg['To'] =  send_to_email 
                        msg['Subject'] = subject
                        msg.attach(MIMEText (message, 'plain'))
                        # Setup the attachment
                        filename = os. path.basename(file_location)
                        attachment = open(file_location, "rb")
                        part = email.MIMEBase('application','octet-stream')
                        part.set_payload (attachment.read())
                        email.encoders.encode_base64(part)
                        part.add_header('Content-Disposition', "attachment;  filename= %s"  % filename)
                        # Attach the attachment to the MIMEMultipart object
                        msg.attach(part)
                        server =smtplib.SMTP('smtp.gmail.com', 587)
                        server.starttls()
                        server.login(email, password)
                        text =msg.as_string()
                        server.sendmail(email, send_to_email, text)
                        server.quit()
                        speak ("email has been sent to user")
                    else:
                        email = 'jarvis140300@gmail.com' 
                        password = 'vishnu1435' 
                        send_to_email = 'vishnukoyyada01@gmail.com' 
                        message =self.query # The nessage in the email
                        server = smtplib.SMTP('smtp.gmail.com', 587)
                        #Connect to the server
                        server.starttls() # Use TLS
                        server.login(email, password) # Login to the email server
                        server.sendmail(email, send_to_email, message) #Send the email
                        server.quit() # Logout of the email server
                        speak ("email has been sent to user")

                    #location
            elif "where i am" in self.query or "where we are" in self.query : 
                    speak("wait sir, let me check")
                    try:
                        ipAdd = requests.get('https://api.ipify.org').text 
                        #print (ipAdd)
                        url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                        geo_requests = requests.get(url)
                        geo_data = geo_requests.json ()
                        # print (geo_data)
                        city = geo_data['city']
                        region = geo_data[ 'region']
                        country = geo_data["country"]
                        speak (f"sir i can't get exactly, but we are closely in region of {region} and {city} city of {country} country")
                    except Exception as e:
                        speak ("sorry sir, Due to network issue i am not able to find where we are.") 
                        pass

                # normal screen shot
            elif "take screenshot" in self.query or "take a screenshot" in self.query or "capture the screen" in self.query :
                speak("By what name do you want to save the screenshot?")
                name = self.takecommand().lower()
                speak("Alright sir, taking the screenshot")
                img = pyautogui.screenshot()
                name = f"{name}.png"
                img.save(name)
                speak("The screenshot has been succesfully captured")
                
             
                
                #read books or pdfs
            elif "read pdf"in self.query or "read books"in self.query:
                    pdf_reader()

                #hiding files
            elif "how much power left" in self.query or "how much power we have" in self.query or "battery" in self.query: 
                import psutil
                battery = psutil.sensors_battery()
                percentage  = battery.percent
                speak (f"sir our system have {percentage} percent battery")
                if percentage >= 75:
                    speak("we have enough power to continue our work")
                elif percentage>=40 and percentage<=75:
                    speak("we should connect our system to charging point to charge our battery")
                elif percentage<=15 and percentage<=30:
                    speak("we don't have enough power to work, please connect to charging")
                elif percentage<=15:
                    speak("we have very low power, please connect to charging the system will shutdown very soon")

            elif "internet speed" in self.query or "netspeed"in self.query:
                import speedtest
                try:
                    os.system('cmd /k "speedtest"')
                except:
                    speak("there is no internet connection")
            elif "send message" in self.query: 
                speak ("sir what should i say")
                msz =  self.takecommand()
                from twilio.rest import Client
                account_sid = 'ACe0ba96fc1a60f89e7957707cc8d8cf20'
                auth_token = '678d4cc62c0cb20a9409a57010fb8232'
                client = Client (account_sid, auth_token)
                message = client.messages \
                    .create(
                        body = msz,
                        from_= '+17163404265',
                        to ='+917702788542'
                )
                print (message.sid)

            elif "call " in self.query: 
                from twilio.rest import Client
                account_sid = 'ACe0ba96fc1a60f89e7957707cc8d8cf20'
                auth_token = '678d4cc62c0cb20a9409a57010fb8232'
                client = Client (account_sid, auth_token)
                message = client.calls \
                    .create(
                        twiml='<Response><Say> this is a simple call from jarvis that heis not working</Say></Response>',
                        from_ = '+17163404265',
                        to ='+917702788542'
                )
                print (message.sid)

            elif 'volume up' in self.query: 
                pyautogui.press("volumeup")
            elif 'volume down' in self.query: 
                pyautogui.press("volumedown")
            elif 'volume mute' in self.query or 'mute' in self.query:
                pyautogui.press ("volumemute")

           
        

            elif "hide all files" in self.query or "hide this folder" in self.query:
                    os.system("attrib +h /s /d")
                    speak("Sir, all the files in this folder are now hidden")

            elif "visible" in self.query or "make files visible" in self.query:
                    os.system("attrib -h /s /d")
                    speak("Sir, all the files in this folder are now visible to everyone. I hope you are taking this decision in your own peace")
            
            elif "instagram pic " in self.query or " downloadinsta" in self.query:
                    speak ("sir please enter the user name correctly.")
                    name = input("Enter username here:")
                    webbrowser.open(f" www.instagram.com/{name}")
                    speak(f" sir here is the profile of the user {name}")
                    time.sleep (5)
                    speak (" Sir would you like to download profile picture of this account.")
                    condition = self.takecommand().lower()
                    if "yes" in condition:
                        mod = instaloader.Instaloader() 
                        mod.download_profile(name, profile_pic_only=True)
                        speak("i am done sir, profile picture is saved in our main folder. now i am ready for your next command")
                    else:
                        pass
            
            

                


            


            

    
    
startExecution =MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisui()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    def startTask(self):
        self.ui.movie = QtGui.QMovie("../../Downloads/7LP8.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("F:/fall 21-22/tarp/Jarvis_Loading_Screen.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date= QDate.currentDate()
        label_time =current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser_2.setText(label_date)
        self.ui.textBrowser.setText(label_time)


app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
