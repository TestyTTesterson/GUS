from greeting import greeting
from GUS import senses, TRIG, ECHO, trigger, echo   


def GUSPrompt():

	# TODO add a prompt instead of using the greeting
	# TODO The prompt should be here instead

    print(greeting())
    print('***BEFORE INPUT***')
    query = input()
    print('***AFTER***')
    stupidTempVar=str(senses.Ping(TRIG, ECHO, trigger, echo))
    print(stupidTempVar + "cm>'Position in Command Structure'>")
    return (query)