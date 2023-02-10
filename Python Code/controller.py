from pyPS4Controller.controller import Controller
from time import sleep

from os import system, name

class MyController(Controller):

    def __init__(self, **kwargs):
        Controller.__init__(self, **kwargs)

def clear():
 
    # for windows
    if name == 'nt':
        _ = system('cls')
 
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

PS4Ctrlr = MyController(interface="/dev/input/js0", connecting_using_ds4drv=False)
#clear = os.system('clr')

while True:
    #  print('Yo!')
    message=PS4Ctrlr.listen()
    print(str(message))
    #  print('Yo!')
    #  sleep(1)
    clear()


