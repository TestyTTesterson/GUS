
def checkpath(GUS):
    collisionTempvar = GUS.locate(GUS)
    if collisionTempvar < 10:
        GUS.avoision = True
        return(True)
    else:
        GUS.avoision = False
        return(False)

