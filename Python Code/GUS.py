import Parser
import sentience as senses
import locomotion as moveIt

TRIG = 17
ECHO = 27

trigger = senses.gpiozero.OutputDevice(TRIG)
echo = senses.gpiozero.DigitalInputDevice(ECHO)

class GUSrobot:
    def __init__(self, name, location, stepdistance, avoision, leftMotor, rightMotor):
        self.name = 'GUS 0.1.2'
        self.location = [0, 0, 0] # x, y, and yaw
        self.stepdistance = 1
        self.avoision = False
        self.leftMotor = 'Motor.Object.Left'
        self.rightMotor = 'Motor.Object.Right'
    def __str__(self):
        return f"{self.name}"
    def locate(self):
        yetanotherstupidTempVar=str(senses.Ping(TRIG, ECHO, trigger, echo))
        self.location[3] = int(yetanotherstupidTempVar)
        return(yetanotherstupidTempVar)
    def move(self):
        moveIt.movement()

GUS=GUSrobot

#  I prefer the while loop to be out here
if __name__ == '__main__':
    while(True):
	    Parser.Parse_query(GUS)
            