import paho.mqtt.client as mqtt
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO

# create the MQTT client
client = mqtt.Client()

# connect to the MQTT server
client.connect("localhost")

# create the GUI
root = Tk()

# create the first listbox to display received messages
GUSmessage_listbox = Listbox(root)
GUSmessage_listbox.pack()

# create the input box and send button
GUSinput_box = Entry(root)
GUSinput_box.pack()
GUSinput_box.focus_set()

#create image boximage_label = Label(root)
GUSVisionImage_label = Label(root)
GUSVisionImage_label.pack(side=RIGHT)

def send_message():
    # get the message from the input box
    message = GUSinput_box.get()

    # post the message to the MQTT server with the topic "GUSCommands"
    client.publish("GUSCommands", message)

    # add the message to the second listbox
    GUSmessage_listbox.insert(END, message)

    # clear the input box
    GUSinput_box.delete(0, END)

send_button = Button(root, text="Send", command=send_message)
root.bind('<Return>', lambda event: send_button.invoke())
send_button.pack()

def update_LIST_box(client, userdata, message):
    # get the message payload
    payload = message.payload.decode()

    # update the LISTBOX box with the received message
    
    GUSmessage_listbox.insert(0, payload)

def update_IMAGEBOX(client, userdata, message):
    # load the image from the message payload
    image = Image.open(BytesIO(message.payload))

    # resize the image to fit the label
    width, height = image.size
    aspect_ratio = height / width
    new_width = 200
    new_height = int(new_width * aspect_ratio)
    image = image.resize((new_width, new_height))

    # update the image label
    photo = ImageTk.PhotoImage(image)
    GUSVisionImage_label.configure(image=photo)
    GUSVisionImage_label.image = photo


# set the callback function for the "GUSPrompt" topic
client.message_callback_add("GUSPrompt", update_LIST_box)
client.message_callback_add("GUSVision", update_IMAGEBOX)

# subscribe to the "GUSPrompt" topic
client.subscribe("GUSPrompt")
client.subscribe("GUSVision")

# start the MQTT loop in a separate thread
client.loop_start()

# start the GUI main loop
root.mainloop()