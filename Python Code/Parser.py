#  {IMPORTS}/

#  Text to Speech
#  import pyttsx3

#  Actions
#import webbrowser 
#import wikipedia

#  Importing sytem stuff
import datetime 
from locomotion import movement
import GUScontroller as GUSctrl
PS4Ctrlr = GUSctrl.MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)

#  /{IMPORTS}

#  {FUNCTIONS}/

#  Parser
#  TODO add commands

def Parse_query():

		
	query = takeCommand().lower()
		
	if "good boy" in query:
		print("Eey ore!  You are such a good boy!")

	elif "hi" in query:
		greeting()

		#  Identify yourself
	elif "controller" in query:

		PS4Ctrlr.listen()

	elif "your name" in query:
		print("I'm GUS, your desktop assistant")
	
	# TODO START OF LOCOMOTION INTERACTION

	elif "travel" in query:
		res = query.split(' ')
		print(res[0])
		print(len(res))
		if len(res) > 1:
			movement(res[1])
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

		#result = wikipedia.summary(query, sentences=4)
		print("According to wikipedia")
		print("result")

	elif "google" in query:
		print("Opening Google ")
		#webbrowser.open("www.google.ca")
		


	# ! End of the fun stuff

	# terminate the program
	elif "bye" in query:
		print("Buh Bye")
		exit()
		
	#  Catch all	
	else:
		print("no understando!")
	


#  Take command

def takeCommand():

	# TODO add a prompt instead of using the greeting
	# TODO The prompt should be here instead
	query = input(str(greeting())+"'Position in the World'>'Position in Command Structure'>")

	return (query)


#    MOTD   
#  Standard Greeting 

def greeting():
	# This function is for when the assistant
	# is called it will say greeting and then
	# take query

	#  TODO I had to switch this to a return rather than a print
	#   TODO otherwise it was printing NONE to the console 
	# TODO but now it doesn't recognize the line break
    
	return("Hi!  I'm your desktop assistant, GUS. How can I help?/n")

#  /{FUNCTIONS}

#  MAIN

if __name__ == '__main__':
     
    # main method

	#  I prefer the while loop to be out here
	while(True):
		Parse_query()
	