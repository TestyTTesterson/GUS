import cv2
from paho.mqtt import client as mqtt_client
broker = 'localhost'
port = 1883
topic = "GUSVision"
client_id = ''


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Successfully connected to MQTT broker")
        else:
            print("Failed to connect, return code %d", rc)
    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        f = open('Python_Code/Resources/GUSreceive.jpg', 'wb')
        f.write(msg.payload)
        f.close()
        print('image received')
        img = cv2.imread("Python_Code/Resources/GUSreceive.jpg", cv2.IMREAD_ANYCOLOR)
        cv2.imshow("GUS VISION", img)

        cv2.waitKey(1) == ord('q')
        #    break

    cv2.destroyAllWindows()
        # cv2.imread("Python_Code/Resources/GUSreceive.jpg")
        
    client.subscribe(topic)
    client.on_message = on_message


#  cap = cv2.VideoCapture(0)


def main():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()







if __name__ == '__main__':
    main()
