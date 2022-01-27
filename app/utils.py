import psutil
import speech_recognition as sr #convert speech to text
import datetime #for fetching date and time
import time
import wikipedia
import random
# import mixer fix mixer issue 
import webbrowser
import smtplib, ssl
import subprocess #shut down or restart
import playsound # to play saved mp3 file 
from gtts import gTTS # google text to speech 
import os # to save/open files 
# import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations
import pyjokes
import wolframalpha 
import pyaudio
from ecapture import ecapture as ec 
# from pygame import mixer #what version fixes this?
#playsound 1.2.2
def talk():
    input=sr.Recognizer()
    with sr.Microphone() as source:
        audio=input.listen(source)
        data=""
        try:
            data=input.recognize_google(audio)
            print("Your question is, " + data)
            
        except sr.UnknownValueError:
            print("Sorry I did not hear your question, Please repeat again.")
    return data

def respond(output):
    num=0
    print(output)
    num += 1
    response=gTTS(text=output, lang='en')
    file = str(num)+".mp3"
    response.save(file)
    
    playsound.playsound(file, True)  
    os.remove(file)
    # num = 0
# def playMusic(): 
#    music_folder = r'C:\Users\solar\Music' 
#    music = os.listdir(music_folder) 
#    random_music = music_folder + random.choice(music) 
#    mixer.init() 
#    mixer.music.load(random_music) 
#    mixer.music.play()
   
def find(name, path):
    for root, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

def sendEmail(to, content):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "solarinsarah3@gmail.com"  # Enter your address
    password = input("Type your password and press enter: ") 
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, to, content)


#resources
def battery_percent():

    return psutil.sensors_battery().percent

def network_info():
    stats = psutil.net_if_stats()

    return [
        {
            'network': key, 
            'up': "Up" if stats[key].isup else "Down", 
            'speed': stats[key].speed}
        for key in stats
    ]

def memory_info():
    # Fetch the memory information
    vm = psutil.virtual_memory()
    return {
        "total": vm.total,
        "used": vm.used,
        "available": vm.available,
        "percentage": vm.percent
    }

def process_info():

    processes = []

    for process in psutil.pids():
        # While fetching the processes, some of the subprocesses may exit
        # Hence we need to put this code in try-except block
        try:
            p = psutil.Process(process)
            processes.append({
                'pid': process,
                'name': p.name(),
                'status': p.status(),
                'cpu': str(p.cpu_percent())+"%",
                'num_threads': p.num_threads()
            })
        except psutil.NoSuchProcess:
            pass
        except psutil.AccessDenied:
            print("Warning: We just hit an Access Denied. Try running the app with admin/superuser priviledges")
            pass
        except Exception as e:
            raise e

    return processes

def main_channel():
    return {
        'battery': battery_percent(),
        'network': network_info(),
        'memory': memory_info(),
        'processor': process_info(),
        # 'voice': voice_cont()
    }
