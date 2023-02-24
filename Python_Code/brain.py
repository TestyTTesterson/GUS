#import GUScontroller as GUSctrl
#PS4Ctrlr = GUSctrl.MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
#  Text to Speech
#  import pyttsx3
#  ! Importing sytem stuff
import datetime 
from prompt import GUSPrompt
from greeting import greeting
from voice import soundfx, speak


#  import communications


HOST = ""  # Standard loopback interface address (localhost)
PORT = 23232  # Port to listen on (non-privileged ports are > 1023)

def brain(GUS):
    
    # query = message.read(message)
    query = GUSPrompt(GUS)

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
	

def accept_wrapper(plug):
        conn, addr = plug.accept()  # Should be ready to read
        print(f"Accepted connection from {addr}")
        conn.setblocking(False)
        GUSmessage = Message(chooser, conn, addr)
        chooser.register(conn, selectors.EVENT_READ, data=GUSmessage)