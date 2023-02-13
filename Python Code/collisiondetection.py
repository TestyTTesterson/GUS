
def checkpath(GUS):
    if GUS.locate < 10:
        GUS.avoision = True
        return(True)
    else:
        GUS.avoision = False
        return(False)

