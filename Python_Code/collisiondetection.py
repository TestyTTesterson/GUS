import spankbank

broker = 'localhost'
port = 1883
topic = "GUSAvoision"
client_id = ''
client= spankbank.connect_mqtt()

def checkpath(GUS):
    GUS.avoision = True
    client.publish("GUSAvoision", "TRIGGERED")
    return(True)