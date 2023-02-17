#import communications
#  from playsound import playsound

from sentience import getPositionData
from mpyg321 import mpyg321

# from GUS import GUS
def GUSPrompt(GUS):

	# TODO add a prompt instead of using the greeting
	# TODO The prompt should be here instead

    
    tongue = mpyg321.MPyg321Player()
    tongue.play_song("/Python_Code/Resources/sonar.mp3")
    stupidTempVar=str(GUS.locate(GUS))
    stupidTempvar2 = getPositionData(gps3)
    print(stupidTempvar2 + "\n")
    query = input(stupidTempVar + "cm>'Position in Command Structure'>")
    #query = input()
    return (query)