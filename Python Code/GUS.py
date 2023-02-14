import Parser
import gpiozero
import sentience as senses
import locomotion as moveIt

class GUSrobot:
    def __init__(self, name, location, stepdistance, avoision, leftMotor, rightMotor, TRIG, ECHO, trigger, echo):
        self.name = 'GUS 0.1.2'
        self.location = [0, 0, 0] # x, y, and yaw
        self.stepdistance = 1
        self.avoision = False
        self.leftMotor = 'Motor.Object.Left'
        self.rightMotor = 'Motor.Object.Right'
        self.TRIG = 17
        self.ECHO = 27
        self.trigger = gpiozero.OutputDevice(self.TRIG)
        self.echo = gpiozero.DigitalInputDevice(self.ECHO)
    def __str__(self):
        return f"{self.name}"
    def locate(self):
        yetanotherstupidTempVar=str(senses.Ping(self.TRIG, self.ECHO, self.trigger, self.echo))
        self.location[3] = float(yetanotherstupidTempVar)
        return(yetanotherstupidTempVar)
    def move(self):
        moveIt.movement()

GUS=GUSrobot

#  I prefer the while loop to be out here
if __name__ == '__main__':
    while(True):
	    Parser.Parse_query(GUS)
            