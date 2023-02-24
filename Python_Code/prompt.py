#import communications

import os
#os.system("bluetoothctl connect FC:58:FA:9C:9C:08")

import serial
# serialPort = serial.Serial("/dev/serial0", 9600, timeout=0.5)
from voice import soundfx

# from GUS import GUS
def GUSPrompt(GUS):

	# TODO The prompt should be here instead
    GPSstring = "OFF OFF2 OFF3 OFF4 OFF5" #str(serialPort.readline())
    GPSlist = GPSstring.split(',')
    if len(GPSlist) >= 5:
        print(GPSlist[3] + " " + GPSlist[4] + " " + GPSlist[5] + " " + GPSlist[6] + "\n")
 
    stupidTempVar="OFF" #str(GUS.locate(GUS))

    query = input(stupidTempVar + "cm>'Position in Command Structure'>")
    soundfx('ping')
    return (query)