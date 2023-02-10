#  Importing stuff for the PINs
import gpiozero
#importing stuff for system tasks
import time
# for PS4Controller
from pyPS4Controller.controller import Controller

# define and assign 
# for leds
ledViolet = gpiozero.LED(17)
ledRed = gpiozero.LED(4)

# for controller
class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

    def on_x_press(self):
        ledViolet.on()
        return super().on_x_press()


    def on_x_release(self):
        ledViolet.off()
        return super().on_x_release()
    
    def on_triangle_press(self):
        ledRed.on()
        return super().on_triangle_press()
    
    def on_triangle_release(self):
        ledRed.off()
        return super().on_triangle_release()
    
PS4Ctrlr = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)

while True:
    
    PS4Ctrlr.listen()
    

