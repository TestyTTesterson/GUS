import paho.mqtt.client as mqtt
from tkinter import *
from tkinter import ttk, Canvas
import tkinter as tk
from PIL import Image, ImageTk
from io import BytesIO

# create the MQTT client
client = mqtt.Client()

# connect to the MQTT server
client.connect("192.168.0.4")

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
# Create a Canvas widget
# Create a Canvas widget
canvas = tk.Canvas(GUSCon, width=200, height=200, borderwidth=0, highlightthickness=0)
canvas.pack(anchor='nw')

# Calculate the size of the oval
oval_size = 50

# Calculate the coordinates for aligning the oval to the top-left corner
x1 = canvas.winfo_x()
y1 = canvas.winfo_y()
x2 = x1 + oval_size
y2 = y1 + oval_size
# Draw a light as a circle
light = canvas.create_oval(x1, y1, x2, y2, fill="purple")

# Calculate the coordinates for placing the label
label_x = ((x1 + x2) / 2)+10
label_y = ((y1 + y2) / 2)+40

# Add the label to the canvas
label = canvas.create_text(label_x, label_y, text="Avoision", font=("Arial", 12))

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

def update_AVOISIONLIGHT(client, userdata, message):
    # get the message payload
    payload = message.payload.decode()
    # update the LISTBOX box with the received message
    if "TRIGGERED" in payload:   
        canvas.itemconfig(light, fill="green")
    else:
        canvas.itemconfig(light, fill="red")

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
client.message_callback_add("GUSAvoision", update_AVOISIONLIGHT)

# subscribe to the "GUSPrompt" topic
client.subscribe("GUSPrompt")
client.subscribe("GUSVision")
client.subscribe("GUSAvoision")
# start the MQTT loop in a separate thread
client.loop_start()

# start the GUI main loop
GUSCon.mainloop()