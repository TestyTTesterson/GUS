import spankbank

broker = 'localhost'
port = 1883
topic = "GUSAvoision"
client_id = ''
client= spankbank.connect_mqtt()

def checkpath(GUS):
    collisionTempvar = GUS.locate(GUS)
    if collisionTempvar > 0 and collisionTempvar < 300:
        if collisionTempvar < 90:
            GUS.avoision = True
            client.publish("GUSAvoision", "TRIGGERED")
            return(True)
        else:
            GUS.avoision = False
            client.publish("GUSAvoision", "PROBLYCLEAR")
            return(False)

