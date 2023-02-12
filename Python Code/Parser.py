#  {CONSTANTS}/

#  ! Pins for the proximity sensor
#TRIG = 17
#ECHO = 27
#trigger = gpiozero.OutputDevice(TRIG)
#echo = gpiozero.DigitalInputDevice(ECHO)

#  /{CONSTANTS}
#  {IMPORTS}/

#  Text to Speech
#  import pyttsx3

#  Actions
#import webbrowser 
#import wikipedia

#  Importing sytem stuff
import datetime 
#from locomotion import movement
#import GUScontroller as GUSctrl
#PS4Ctrlr = GUSctrl.MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
#import sentience as senses
from prompt import GUSPrompt
from greeting import greeting
from GUS import GUSrobot


#trigger = senses.gpiozero.OutputDevice(TRIG,active_high=None)
#echo = senses.gpiozero.DigitalInputDevice(ECHO,active_state=None)

#  /{IMPORTS}


#  {FUNCTIONS}/

#  Parser
#  TODO add commands

def Parse_query(GUS):
    from GUS import GUSrobot
    
    query = GUSPrompt()
	
		
    if "good boy" in query:
        print("Eey ore!  You are such a good boy!")
    
    elif "hi" in query:
        greeting()

		#  Identify yourself
    elif "controller" in query:
        print('controllers are hard')
		#PS4Ctrlr.listen()

    elif "your name" in query:
        print("I'm GUS, your desktop assistant")
	
	# TODO START OF LOCOMOTION INTERACTION
    elif "travel" in query:
		# check for travel arg
        
        res = query.split(' ')
        print(res[0])
        print(len(res))
        if len(res) > 1:
			#movement(res[1])
            GUS.move()
	
        else:
            print('Must provide direction as 2nd argument ("travel forward") not: ' + query)
		

	######  !  END OF LOCOMOTION INTERACTION

	# Kinda fun optional functionality

    elif "wikipedia" in query:
			
			# from wikipedia
        print("Checking wikipedia ")
        query = query.replace("wikipedia", "")
			
			# summary of 4 lines from
			# wikipedia can be increased and decreased

		# TODO I had to comment this out due to dep issues on GUS

		#result = wikipedia.summary(query, sentences=4)
        print("According to wikipedia")
        print("result")

    elif "google" in query:
        print("Opening Google ")

		# TODO I had to comment this out due to dep issues on GUS

		#webbrowser.open("www.google.ca")
		

	# ! End of the fun stuff

	# terminate the program
    elif "bye" in query:
        print("Buh Bye")
        exit()
		
	#  Catch all	
    else:
        print("No understando!")
	

#  MOTD   
#  Standard Greeting  moved to greeting.py
#  MAIN
# main method moved to GUS.py