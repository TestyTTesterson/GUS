from brain import brain
from greeting import greeting
#import gpiozero
import sentience as senses
import locomotion as moveIt
# import communications
from gps3 import gps3
the_connection = gps3.GPSDSocket() 
the_fix = gps3.Fix()

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
        for new_data in the_connection:
            if new_data:
                the_fix.refresh(new_data)
            if not isinstance(the_fix.TPV['lat'], str): # lat as determinate of when data is 'valid'
                speed = the_fix.TPV['speed']
                latitude = the_fix.TPV['lat']
                longitude = the_fix.TPV['lon']
                altitude  = the_fix.TPV['alt']
        print(speed + latitude + longitude + altitude)