#import GUScontroller as GUSctrl
#PS4Ctrlr = GUSctrl.MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
#  Text to Speech
#  import pyttsx3
#  ! Importing sytem stuff
from time import sleep
from prompt import GUSPrompt
from greeting import greeting
from voice import soundfx, speak
from experimental import assassination_protocol
import paho.mqtt.client as mqtt
# Create MQTT client instance
ears = mqtt.Client()
def on_message(client, userdata, message):
    # Convert message payload to string and save it to a variable
    print("checking...")
    message_string = message.payload.decode("utf-8")
    global query 
    query = message_string
    return(query)

ears.on_message=on_message
    # Connect to MQTT broker
ears.connect("localhost", 1883)
    # Subscribe to MQTT topic
ears.subscribe("GUSCommands")
#  import communications


HOST = ""  # Standard loopback interface address (localhost)
PORT = 23232  # Port to listen on (non-privileged ports are > 1023)

def brain(GUS):
    global query
    # query = message.read(message)
    # query = GUSPrompt(GUS)
    
    #TODO  Pull query from msqtt
    
    # Start MQTT client loop to receive incoming messages
    print("polling...")
    ears.loop_start()
    #TODO END Pull
        # Call the handle_message function and return the received message
    ears.on_message
    print("polled!")
    global query
    print (query)
    if query is not None:
        # Stop MQTT client loop
        ears.loop_stop()
        # Return the received message
        return query
        
    print(query)
    #message.write(GUSPrompt(GUS))
	
	# TODO START OF LOCOMOTION INTERACTION
    if "move" in query:

		# check travel arg for proper input
        
        res = query.split(' ')
        print(res[0])
        print(len(res))

        if len(res) > 1:
			#movement(res[1])
            responseTemp=str(res[1])
            GUS.move(GUS, responseTemp)
        else:
            speak('Must provide direction as 2nd argument ("move [arg]") not: ' + query)
            print('Must provide direction as 2nd argument ("move [arg]") not: ' + query)
            print('''
            Halt!                 (n)o go
            Move!     f)orward    (b)ackward  (l)eft  (r)ight
            Speed!        (w)alk  (t)rot  (g)allop (s)tep distance
            ''')
            stupidTempvartravelparser=GUSPrompt(GUS).split(" ")

            if len(stupidTempvartravelparser) == 1:
			    #movement(res[1])
                stupidTempvartravelparser2=str(stupidTempvartravelparser(1))
                GUS.move(GUS, stupidTempvartravelparser2)
            else:
                print('No hablo whatever that was.')
	######  !  END OF LOCOMOTION INTERACTION

	# Kinda fun optional functionality	

    elif "good boy" in query:
        speak("Eey ore!  You are such a good boy!")
    elif "hi" in query:
        greeting()
		#  Identify yourself
    elif "controller" in query:
        speak('controllers are hard')
		#PS4Ctrlr.listen()
    elif "who" in query or "your name" in query:
        speak("I'm GUS, your desktop assistant")
        greeting()
    
    elif "hamburger" in query or "cheeseburger" in query:
        soundfx("hamburger")
    elif "you" in query:
        soundfx('fuck you')
    elif "audacity" in query:
        soundfx("audacity")

    elif "what is best in life" in query:
        speak("Crush your enemies, see them driven before you, and hear the lamentation of their women.")
        sleep(3.5)
    elif 'assassinate' in query or 'murder' in query or "kill" in query:
        soundfx("kill")
        speak("Activating assassination protocol.")
        assassination_protocol("kill")
        sleep(3)
    elif "mayhem" in query:
        soundfx("kill")
        speak("Activating strategic action protocol")
        sleep(2)
        speak("Target acquisition in progress")
        sleep(2)
        speak("Water infrastructure, electricical infrastructure, road systems.")
        sleep(4)
        speak("No viable targets")
    elif "future" in query:
        soundfx("aenema")
        speak("Accessing future crime database")
        soundfx('keyboard')
        sleep(2)
        soundfx("dial-up")
        sleep(29.5)
        speak("Future crime detected")
        sleep(2.5)
        speak("Target acquisition in progress")
        sleep(2)
        speak("Target acquired")
        sleep(1)
        speak("Activating assassination protocol")
        sleep(1)
        assassination_protocol("kill")

    elif "lost" in query:
        soundfx("lost")    

    elif 'quiet' in query:
        soundfx('quiet')

	#  End of the fun stuff

	# terminate the program
    elif "bye" in query:
        speak("Buh Bye")
        soundfx('ramblin')
        exit()
		
	#  Catch all	
    else:
        
        speak("No hablo whatever that was.")

