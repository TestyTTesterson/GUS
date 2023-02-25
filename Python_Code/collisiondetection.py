

def checkpath(GUS):
    collisionTempvar = GUS.locate(GUS)
    if collisionTempvar > 0 and collisionTempvar < 300:
        if collisionTempvar < 90:
            GUS.avoision = True
            return(True)
        else:
            GUS.avoision = False
            return(False)

