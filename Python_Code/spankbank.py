import cv2
import time
from paho.mqtt import client as mqtt_client
broker = '192.168.0.54'
port = 1883
topic = "GUSVision"
client_id = ''

delayGUSVision = 30

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

def publish(client):
    with open("Python_Code/Resources/GUSsend.jpg",'rb') as file:
        filecontent = file.read()
        byteArr = bytearray(filecontent)
        print(byteArr)
        result = client.publish(topic,byteArr,2)
    msg_status = result[0]
    if msg_status == 0:
        print(f"message sent to topic {topic}")
    else:
        print(f"Failed to send message to topic {topic}")
    

# Loop through frames from the webcam
def SpankBank():
    print("Background process started.")
    time.sleep(1)

    # Load the pre-trained Haar Cascade classifier for face detection
    face_cascade = cv2.CascadeClassifier('Python_Code/haarcascade_frontalface_default.xml')
    # Create a VideoCapture object to access the webcam
    cap = cv2.VideoCapture(0)
    # Check if the webcam is opened successfully
    if not cap.isOpened():
        print("Unable to access the webcam")
        exit()
    # Set the webcam to infrared mode Doesn't work
    #cap.set(cv2.CAP_PROP_CONVERT_RGB, 0.0)    
   # Read a frame from the webcam
    ret, frame = cap.read()

        # Check if the frame was read successfully
    if not ret:
        print("Unable to read frame from the webcam")
        return
    
        # Convert the frame to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the grayscale frame using the Haar Cascade classifier
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

        # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.putText(frame, "Alfred", (x, y+100), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)


        # Display the frame in a window
        #  cv2.imshow("GUS VISION", frame)

    cv2.imwrite("Python_Code/Resources/GUSsend.jpg", gray)
        # Wait for a key press to exit the loop
        #  if cv2.waitKey(1) == ord('q'):
        #    break

        # Release the VideoCapture object and close the window
    cap.release()
        #cv2.destroyAllWindows()
    client = connect_mqtt()
    client.loop_start()
    publish(client)
    #time.sleep(delayGUSVision)
    client.loop_stop()


#  SpankBank(face_cascade, cap)

