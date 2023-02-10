#  Text to Speech
import pyttsx3


import webbrowser 

import wikipedia

#  Importing sytem stuff
import datetime 



def Parse_query():

	while(True):
		
		query = takeCommand().lower()
		
		if "good boy" in query:
			print("Ee ore!  You are a good boy")
			
			continue
		elif "hi" in query:
			greeting()
			
		elif "google" in query:
			print("Opening Google ")
			webbrowser.open("www.google.ca")
			continue
		
		elif "wikipedia" in query:
			
			# from wikipedia
			print("Checking wikipedia ")
			query = query.replace("wikipedia", "")
			
			# summary of 4 lines from
			# wikipedia can be increased and decreased

			result = wikipedia.summary(query, sentences=4)
			print("According to wikipedia")
			print(result)
		
		elif "tell me your name" in query:
			print("I am Eegore. Your desktop Assistant")
		# terminate the program
		elif "bye" in query:
			print("Buh Bye")
			exit()
		else:
			print("no understando!")


#  Take command

def takeCommand():
	query = input("Enter your query: ")

	return (query)

    #    MOTD   

def greeting():
	# This function is for when the assistant
	# is called it will say greeting and then
	# take query
    print("Hi!  I'm your desktop assistant, Eegore. How can I help?")


if __name__ == '__main__':
     
    # main method for executing
    # the functions
    Parse_query()