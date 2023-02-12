import Parser
import sentience as senses
import locomotion as moveIt

TRIG = 17
ECHO = 27
trigger = senses.gpiozero.OutputDevice(TRIG,active_high=None)
echo = senses.gpiozero.DigitalInputDevice(ECHO,active_state=None)

class GUSrobot:
    def __init__(self, name, location):
        self.name = 'GUS'   
        self.location = (0,0)
    def __str__(self):
        return f"{self.name}({self.location})"
    def locate(self):
        yetanotherstupidTempVar=str(senses.Ping(TRIG, ECHO, trigger, echo))
        return(yetanotherstupidTempVar)
    def move(self):
        moveIt.movement()
         
GUS=GUSrobot

        
#  I prefer the while loop to be out here
if __name__ == '__main__':
    while(True):
	    Parser.Parse_query(GUS)
            