
def collisionavoision(GUS):

    avoisionTempvar = GUS.locate(GUS)

    print("distance: ",avoisionTempvar)

    if GUS.avoision:
        if avoisionTempvar < 10:
            GUS.move(GUS, "s")

            return("WHOA!!")
        elif avoisionTempvar < 30:
            GUS.move(GUS, 'b')
            return('back it up')
        elif avoisionTempvar < 90:
            GUS.move(GUS,'l')
            GUS.move(GUS,'f')
            GUS.move(GUS, 'r')
            return('move to the left')

        else:
            GUS.avoision = False

            return(False)