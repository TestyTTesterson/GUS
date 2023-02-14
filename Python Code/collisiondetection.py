
def checkpath(GUS):
    collisionTempvar = int(GUS.locate(GUS))
    if collisionTempvar < 10:
        GUS.avoision = True
        return(True)
    else:
        GUS.avoision = False
        return(False)

