from brain import brain
from greeting import greeting
#import gpiozero
import sentience as senses
import locomotion as moveIt
# import communications

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

def parseGPS(msg):

    #msg = pynmea2.parse(str)
    print ("Timestamp: %s -- Lat: %s %s -- Lon: %s %s -- Altitude: %s %s" % (msg.timestamp,msg.lat,msg.lat_dir,msg.lon,msg.lon_dir,msg.altitude,msg.altitude_units))

#  I prefer the while loop to be out here
if __name__ == '__main__':
    #while(True):
        
        print(greeting())
        brain(GUS)
    



