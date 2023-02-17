from brain import brain
from greeting import greeting
#import gpiozero
import sentience as senses
import locomotion as moveIt
# import communications
import pigps
GUSgps = pigps.GPS()
import serial
import pynmea2
serialPort = serial.Serial("/dev/serial0", 9600, timeout=0.5)

while True:
    str = serialPort.readline()
    print(str)



class GUSrobot:
    def __init__(self, name, location, avoision):
        #  args    TRIG, ECHO, trigger, echo
        self.name = 'GUS 0.1.2'
        self.location = [0, 0, 0] # x, y, and yaw
        
        self.avoision = False
        #self.leftMotor = 'Motor.Object.Left'
        #self.rightMotor = 'Motor.Object.Right'
        #self.TRIG = 17
        #self.ECHO = 27
        #self.trigger = gpiozero.OutputDevice(self.TRIG)
        #self.echo = gpiozero.DigitalInputDevice(self.ECHO)
    def __str__(self):
        return f"{self.name}"
    def locate(self):
        yetanotherstupidTempVar=senses.Ping()
        #self.location[3] = float(yetanotherstupidTempVar)
        return(yetanotherstupidTempVar)
    def move(self, command):
        moveIt.movement(self, command)
    stepdistance = 0.5

GUS=GUSrobot

#  I prefer the while loop to be out here
if __name__ == '__main__':
    while(True):
        
        #print(greeting())
        #brain(GUS)
        print(GUSgps.lon)