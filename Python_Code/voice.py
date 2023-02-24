# from mpyg321 import MPyg321Player
from playsound import playsound
import os

import pyttsx3
#import speech_recognition as sr

def speak(phrase):
     
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[0].id)
     
    engine.say(phrase) 
    # Blocks while processing all the currently
    engine.runAndWait()

def soundfx(fx):

    if "hurt" in fx:
        playsound('/home/testyt/Desktop/GUS/Python_Code/Resources/hurt.mp3', False)
    elif "theme" in fx:
        playsound("/home/testyt/Desktop/GUS/Python_Code/Resources/lateralus.mp3", False)
    elif "ping" in fx:
        playsound('/home/testyt/Desktop/GUS/Python_Code/Resources/sonar.mp3', False)
    elif "hamburger" in fx:
        playsound('/home/testyt/Desktop/GUS/Python_Code/Resources/hamburger-cheeseburger.mp3', False)
    else:
        playsound('/home/testyt/Desktop/GUS/Python_Code/Resources/voodoo-child.mp3', False)

#speak("Yo mamma!")