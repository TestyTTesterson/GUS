# from mpyg321 import MPyg321Player
from playsound import playsound
import os
from time import sleep
#import pyttsx3
#engine = pyttsx3.init()
#voices = engine.getProperty('voices')
import os
from paho.mqtt import client as mqtt_client
import spankbank

broker = '192.168.0.54'
port = 1883
topic = "GUSPrompt"
client_id = ''
client= spankbank.connect_mqtt()

def speak(phrase, GUS):

    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    #engine.setProperty('voice', 'zhy')
 #   engine.setProperty('voice', "english_wmids" + '-m7')
  #  engine.setProperty('rate', 235)
     
   # engine.say(phrase) 
    #engine.runAndWait()
    print(phrase)
    
    GUS.ears.publish("GUSPrompt", phrase)

def soundfx(fx):

    if "hurt" in fx:
        playsound('/home/testyt/Desktop/GUS/Python_Code/Resources/hurt.mp3', False)
    elif "keyboard" in fx:
        playsound("/home/testyt/Desktop/GUS/Python_Code/Resources/keyboard.mp3", False)
    elif "dial-up" in fx:
        playsound("/home/testyt/Desktop/GUS/Python_Code/Resources/dial-up.mp3", False)
    elif "ramblin" in fx:
        playsound("/home/testyt/Desktop/GUS/Python_Code/Resources/ramblin-man.mp3", False)
    elif "theme" in fx:
        playsound("/home/testyt/Desktop/GUS/Python_Code/Resources/lateralus.mp3", False)
    elif "ping" in fx:
        playsound('/home/testyt/Desktop/GUS/Python_Code/Resources/sonar.mp3', False)
    elif "hamburger" in fx:
        playsound('/home/testyt/Desktop/GUS/Python_Code/Resources/hamburger-cheeseburger.mp3', False)
    
    elif "fuck you" in fx:
        playsound('/home/testyt/Desktop/GUS/Python_Code/Resources/abcdefu.mp3', False)
    
    elif "audacity" in fx:
        playsound('/home/testyt/Desktop/GUS/Python_Code/Resources/audacity.mp3', False)
    
    elif "heart" in fx:
        playsound('/home/testyt/Desktop/GUS/Python_Code/Resources/jar-of-hearts.mp3', False)

    elif "kill" in fx:
        playsound('/home/testyt/Desktop/GUS/Python_Code/Resources/killing.mp3', False)
    
    elif "aenema" in fx:
        playsound('/home/testyt/Desktop/GUS/Python_Code/Resources/aenema.mp3', False)
    
    elif "lost" in fx:
        playsound('/home/testyt/Desktop/GUS/Python_Code/Resources/lost-boy.mp3', False)
    elif "quiet" in fx:
        print("Turn down for what?  Can't stop, won't stop.")
        os.system('pulseaudio -k')
    else:
        playsound('/home/testyt/Desktop/GUS/Python_Code/Resources/voodoo-child.mp3', False)

#speak("Yo mamma!")
'''
for voice in voices:
    print(voice, voice.id)
    engine.setProperty('voice', voice.id)
    engine.say("Hi, I'm Gus!")
    sleep(2)
    engine.runAndWait()
    engine.stop()
'''
