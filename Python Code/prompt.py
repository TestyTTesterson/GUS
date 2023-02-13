from greeting import greeting

def GUSPrompt(GUS):

	# TODO add a prompt instead of using the greeting
	# TODO The prompt should be here instead

    print(greeting())
    print('***BEFORE INPUT***')
    query = input()
    print('***AFTER***')
    stupidTempVar=GUS.locate()

    print(stupidTempVar + "cm>'Position in Command Structure'>")
    return (query)