#  Importing stuff for the PINs
import gpiozero
#importing stuff for system tasks
import time

# for PS4Controller
from pyPS4Controller.controller import Controller

# for Parser comms
import Parser as parser

# for controller
class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        
        return super().on_x_press()


    def on_x_release(self):
        
        return super().on_x_release()
    
    def on_triangle_press(self):
        parser.PS4Ctrlr.stop()

        return super().on_triangle_press()
    
    def on_triangle_release(self):
        
        return super().on_triangle_release()


   
# PS4Ctrlr = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)

# PS4Ctrlr.listen()
    

