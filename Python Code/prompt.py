#import communications
from playsound import playsound

# from GUS import GUS
def GUSPrompt(GUS):

	# TODO add a prompt instead of using the greeting
	# TODO The prompt should be here instead

    
    # print('GUSPrompt')
    
    playsound('/Resources/sonar-a-dry-98689.mp3')
    stupidTempVar=str(GUS.locate(GUS))
    
    query = input(stupidTempVar + "cm>'Position in Command Structure'>")
    #query = input()
    return (query)