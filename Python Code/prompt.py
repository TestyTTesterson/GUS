#import communications
#  from playsound import playsound
#import gps3
from sentience import getPositionData
from mpyg321 import mpyg321

# from GUS import GUS
def GUSPrompt(GUS):

	# TODO add a prompt instead of using the greeting
	# TODO The prompt should be here instead

    
    # print('GUSPrompt')
    
    mpyg321('/Resources/sonar-a-dry-98689.mp3')
    stupidTempVar=str(GUS.locate(GUS))
    stupidTempvar2 = getPositionData()
    print(stupidTempvar2 + "\n")
    query = input(stupidTempVar + "cm>'Position in Command Structure'>")
    #query = input()
    return (query)