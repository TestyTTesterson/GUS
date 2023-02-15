
#  ! Importing sytem stuff
import datetime 
from prompt import GUSPrompt
from greeting import greeting
#import GUScontroller as GUSctrl
#PS4Ctrlr = GUSctrl.MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
#  Text to Speech
#  import pyttsx3
import communications
message = communications.Message

def brain(GUS):
    

    query = message.read(message)
    message.write(GUSPrompt(GUS))
	
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
        print("Eey ore!  You are such a good boy!")
    elif "hi" in query:
        greeting()

		#  Identify yourself
    elif "controller" in query:
        print('controllers are hard')
		#PS4Ctrlr.listen()
    elif "your name" in query:
        print("I'm GUS, your desktop assistant")

	#  End of the fun stuff

	# terminate the program
    elif "bye" in query:
        print("Buh Bye")
        exit()
		
	#  Catch all	
    else:
        print("No hablo whatever that was.")
	

#  MOTD   
#  Standard Greeting  moved to greeting.py
#  MAIN
# main method moved to GUS.py