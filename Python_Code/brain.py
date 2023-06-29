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
import spankbank
import collisiondetection
import multiprocessing
import openai
openai.api_key = "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"

AIMessages = []
AIMessages.append({"role": "system", "content": "A wise old mentor"})
#from GUSmain import GUS


HOST = ""  # Standard loopback interface address (localhost)
PORT = 23232  # Port to listen on (non-privileged ports are > 1023)


def spankbank_process(queue):
    #sb = spankbank.SpankBank()
    while True:
        try:
            command = queue.get(block=False)
        except queue.Empty:
            pass
        else:
            
            if command == "start":
                sb = spankbank.SpankBank()
            elif command == "stop":
                if sb is not None:
                    sb.stop()
                break



def brain(GUS):

    print(GUS.query)
    
	# TODO START OF LOCOMOTION INTERACTION
    if "move" in GUS.query:
		# check travel arg for proper input

        res = GUS.query.split(' ')
        print(res[0])
        print(len(res))

        if len(res) > 1:
			#movement(res[1])
            responseTemp=str(res[1])
            GUS.move(GUS, responseTemp)
        else:
            speak('Must provide direction as 2nd argument ("move [arg]") not: ' + GUS.query)
            print('Must provide direction as 2nd argument ("move [arg]") not: ' + GUS.query)
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


	# terminate the program
    elif "bye" in GUS.query:
        speak("Buh Bye")
        speak("SFX OFF")
        #soundfx('ramblin')
        exit()
    elif "SpankBank" in GUS.query:
        SBProcess = multiprocessing.Process(target=spankbank.SpankBank())

        SBProcess.start()
        #SBProcess.join()
        #queue.put("start")       
    elif "SBStop" in GUS.query:
        speak("Once it's out there...")
        #SBProcess.terminate()
        #queue.put('stop')
    elif "avoision" in GUS.query:
        collisiondetection.checkpath()
 
    # Start of the fun stuff
    elif "good boy" in GUS.query:
        speak("Eey ore!  You are such a good boy!")
    elif "hi" in GUS.query:
        greeting()
		#  Identify yourself
    elif "controller" in GUS.query:
        speak('controllers are hard')
		#PS4Ctrlr.listen()
    elif "who" in GUS.query or "your name" in GUS.query:
        speak("I'm GUS, your desktop assistant")
        print(greeting())
    elif "hamburger" in GUS.query or "cheeseburger" in GUS.query:
        speak("SFX disabled")
        #    soundfx("hamburger")
    elif "you" in GUS.query:
        speak("SFX disabled")
        #   soundfx('fuck you')
    elif "audacity" in GUS.query:
        speak("SFX disabled")
        #    soundfx("audacity")
    elif "what is best in life" in GUS.query:
        speak("Crush your enemies, see them driven before you, and hear the lamentation of their women.")
        sleep(3.5)
    elif 'assassinate' in GUS.query or 'murder' in GUS.query or "kill" in GUS.query:
    #    soundfx("kill")
        speak("Activating assassination protocol.")
        assassination_protocol("kill")
        sleep(3)
    elif "mayhem" in GUS.query:
     #   soundfx("kill")
        speak("Activating strategic action protocol")
        sleep(2)
        speak("Target acquisition in progress")
        sleep(2)
        speak("Water infrastructure, electricical infrastructure, road systems.")
        sleep(4)
        speak("No viable targets")
    elif "future" in GUS.query:
    #    soundfx("aenema")
        speak("Accessing future crime database")
    #    soundfx('keyboard')
        sleep(2)
    #    soundfx("dial-up")
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
    elif "lost" in GUS.query:
        speak("SFX disabled")
        #   soundfx("lost")    
    elif 'quiet' in GUS.query:
        speak("SFX disabled")
        #    soundfx('quiet')
#  End of the fun stuff
    elif 'AI' in GUS.query:
        # split the query by " " delim 
        resAI = GUS.query.split(' ')

        if len(resAI) > 1:
            #if there are at least 2 words

            responseTempAI=GUS.query
            # add header info
            AIMessages.append({"role": "user", "content": responseTempAI})
            AICompletion = openai.ChatCompletion.create(model= "gpt-3.5-turbo", messages=[{"role": "user", "content": responseTempAI}])
            AIReply = AICompletion["choices"][0]["message"]["content"]
            
            speak(AIReply)

        else:
            speak('Must provide direction as 2nd argument ("move [arg]") not: ' + GUS.query)


    elif GUS.query == "":
        # shouldn't get here
        speak("Waiting patiently for a command.")
        sleep(2)
    	
	#  Catch all	
    else:
        
        speak("No hablo whatever that was.")
        #  If it's gibberish, make it blank
        GUS.query = ""




