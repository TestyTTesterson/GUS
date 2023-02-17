#import communications
#  from playsound import playsound

#from sentience import getPositionData
from mpyg321 import mpyg321
tongue = mpyg321.MPyg321Player()

import serial
serialPort = serial.Serial("/dev/serial0", 9600, timeout=0.5)


# from GUS import GUS
def GUSPrompt(GUS):

	# TODO The prompt should be here instead

    GPSstring = str(serialPort.readline())
    GPSlist = GPSstring.split(',')
    if len(GPSlist) >= 5:
        print(GPSlist[3] + GPSlist[4] + GPSlist[5] + GPSlist[6] + "\n")


    #tongue.play_song("/Python_Code/Resources/sonar.mp3")

    stupidTempVar=str(GUS.locate(GUS))

    query = input(stupidTempVar + "cm>'Position in Command Structure'>")
    return (query)