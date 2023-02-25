from voice import soundfx, speak
from time import sleep

def assassination_protocol(target):
    #soundfx('kill')
    sleep(1)
    speak("Murder")
    sleep(1.5)
    speak("death") 
    sleep(1)
    speak("kill " + target + "!")