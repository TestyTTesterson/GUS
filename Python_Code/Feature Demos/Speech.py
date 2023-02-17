import pyttsx3
import speech_recognition as sr
import webbrowser 
import datetime 
import wikipedia

#  SPEECH Definition
def speak(audio):
     
    engine = pyttsx3.init()
    # getter method(gets the current value
    # of engine property)
    voices = engine.getProperty('voices')
     
    # setter method .[0]=male voice and
    # [1]=female voice in set Property.
    engine.setProperty('voice', voices[0].id)
     
    # Method for the speaking of the assistant
    engine.say(audio) 
     
    # Blocks while processing all the currently
    # queued commands
    engine.runAndWait()

#  TAKE QUERY

def Take_query():

	# calling the Hello function for
	# making it more interactive
	# Hello()
	
	# take our queries continuously until and unless
	# we do not say bye to exit or terminate
	# the program

	while(True):
		
		# taking the query and making it into
		# lower case so that most of the times
		# query matches and we get the proper
		# output
		query = takeCommand().lower()
		
		if "good boy" in query:
			speak("Ee ore!  You are a good boy")
			
			continue
		elif "hi" in query:
			Hello()
			
		elif "google" in query:
			speak("Opening Google ")
			webbrowser.open("www.google.ca")
			continue
		
		elif "wikipedia" in query:
			
			# from wikipedia
			speak("Checking wikipedia ")
			query = query.replace("wikipedia", "")
			
			# summary of 4 lines from
			# wikipedia can be increased and decreased

			result = wikipedia.summary(query, sentences=4)
			speak("According to wikipedia")
			speak(result)
		
		elif "tell me your name" in query:
			speak("I am Eegore. Your desktop Assistant")
		# terminate the program
		elif "bye" in query:
			speak("Buh Bye")
			exit()
		
		

    #    MOTD   

def Hello():
	# This function is for when the assistant
	# is called it will say hello and then
	# take query
	speak("Hi!  I'm your desktop assistant, Eegore. How can I help?")

#  Take command

# this method is for taking the commands
# and recognizing the command from the
# speech_Recognition module we will use
# the recongizer method for recognizing
def takeCommand():
	query = input("Enter your query ")

	return (query)

#  MAIN METHOD


if __name__ == '__main__':
     
    # main method for executing
    # the functions
    Take_query()

