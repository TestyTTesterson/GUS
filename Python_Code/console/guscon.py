import paho.mqtt.client as mqtt
from tkinter import *
from tkinter import ttk

from PIL import Image, ImageTk
from io import BytesIO

# create the MQTT client
client = mqtt.Client()

# connect to the MQTT server
client.connect("localhost")

# create the GUI
GUSCon = Tk()

# create the first listbox to display received messages
GUSmessage_listbox = Listbox(GUSCon, width = 60, height = 10, )
# Create a Scrollbar widget
scrollbar = Scrollbar(GUSCon, orient='vertical', command=GUSmessage_listbox.yview)
scrollbar.pack(side='left', fill='y')

GUSmessage_listbox.config(yscrollcommand=scrollbar.set)
GUSmessage_listbox.pack(side='bottom', fill='both', expand=True)
#create image boximage_label = Label(root)
GUSVisionImage_label = Label(GUSCon)
GUSVisionImage_label.pack(side="top")
# Create Combobox widget with custom values
previous_entries = ["who"]
GUSInput_box = ttk.Combobox(GUSCon, values=previous_entries)
GUSInput_box.pack()
GUSInput_box.focus_set()

def send_message():
    # get the message from the input box
    message = GUSInput_box.get()
    # post the message to the MQTT server with the topic "GUSCommands"
    client.publish("GUSCommands", message)
    # add the message to the second listbox
    # Add current value to previous entries list
    previous_entries.append(message)
    # Update values of Combobox
    GUSInput_box['values'] = previous_entries
    # clear the input box
    GUSInput_box.delete(0, END)

send_button = Button(GUSCon, text="Send", command=send_message)
GUSCon.bind('<Return>', lambda event: send_button.invoke())
send_button.pack()

def update_LIST_box(client, userdata, message):
    # get the message payload
    payload = message.payload.decode()
    # update the LISTBOX box with the received message
    GUSmessage_listbox.insert(END, payload)

def update_IMAGEBOX(client, userdata, message):
    # load the image from the message payload
    image = Image.open(BytesIO(message.payload))

    # resize the image to fit the label
    width, height = image.size
    aspect_ratio = height / width
    new_width = 600
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
GUSCon.mainloop()