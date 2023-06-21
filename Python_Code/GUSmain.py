
from brain import brain
from greeting import greeting
from voice import soundfx
#import gpiozero
#import sentience as senses
#import locomotion as moveIt
# import communications
import paho.mqtt.client as mqtt
# Create MQTT client instance
ears = mqtt.Client()

#Robot class holds all sorts of dodads
#constants, some functions have been 
# put here but that doesn't work
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
        yetanotherstupidTempVar="300" #senses.Ping()
        #self.location[3] = float(yetanotherstupidTempVar)
        return(yetanotherstupidTempVar)
    def move(self, command):
        return("OFF") #moveIt.movement(self, command)
    
    
    stepdistance = 0.5
    query = ''

#Instantiate the GUS Class as GUS
GUS=GUSrobot

#listener callback function for mqtt
def on_message(client, userdata, message):
   
    # Convert message payload to string and save it to a variable
        print("checking...")
        message_string = message.payload.decode("utf-8") 
        GUS.query = str(message_string)
        return(message_string)

ears.on_message=on_message
    # Connect to MQTT broker
ears.connect("localhost", 1883)
    # Subscribe to MQTT topic
ears.subscribe("GUSCommands")


if __name__ == '__main__':
    #soundfx('theme')
    print(greeting())
    while(True):
        
        #Pull GUS.query from msqtt
    
        # Start MQTT client loop to receive incoming 
        # messages
        #print("polling...")
        ears.loop_start()

        #I forget why this was in here during 
        # troubleshooting

        stupidTempquery = ears.on_message
        #print("polled!")
            #END Pull
        
        #  Switched to not "" instead of None
        if GUS.query != "":
            print(GUS.query)
            # Stop MQTT client loop
            ears.loop_stop()
            # Return the received message to the 
            # parser.  I had to use a variable on
            # the class so I could pass the value around
            brain(GUS)
            #clear the message buffer
            GUS.query = ""
        
    



