

# import RPi.# GPIO as # GPIO 
import gpiozero
from time import sleep

#ledViolet = gpiozero.#led(23)
#ledGreen = gpiozero.#led(24)
#ledRed = gpiozero.#led(25)
#ledYellow = gpiozero.#led(26)
# in1 = 24
# in2 = 23
en = 25

# TODO Must figure out this part instead of using #led.ON/OFF

def movement(command):
    # moved this inside the method for obvi reasons
    # thankfully it wasn't still just named temp
    forgettabletempvarname=1
    motorSpeed=1

    if 's' in command:
        print("stop")
        #ledRed.on()
        sleep(1)
        #ledRed.off()
        #myMotor.stop
        

    elif 'f' in command:
        print("forward")
        #myMotor.forward()
        #ledGreen.on()
        sleep(1)
        #ledGreen.off()
        forgettabletempvarname=1
        

    elif 'b' in command:
        print("back")
        #myMotor.backward()
        #ledYellow.on()
        sleep(1)
        #ledYellow.off()
        forgettabletempvarname=0
        

    elif 'l' in command:
        print("low")
        #motorSpeed=0.25
        #ledViolet.on()
        sleep(1)
        #ledViolet.off()
        # p.ChangeDutyCycle(25)
       

    elif 'm' in command:
        print("medium")
        #motorSpeed=0.5
        #ledYellow.on()
        sleep(1)
        #ledYellow.off()
        # p.ChangeDutyCycle(50)
        

    elif 'h' in command:
        print("high")
        #motorSpeed=0.75
        # p.ChangeDutyCycle(75)
        #ledRed.on()
        sleep(1)
        #ledRed.off()

    #  TODO add the turning function
    # I'm thinking just a 90 degree turn but not sure what that will look like until
    # I interact with the motor    
    elif 'e' in command:
        # GPIO.cleanup()

        exit()
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")


# print("\n")
# print("The default speed & direction of motor is LOW & Forward.....")
# print("r-run s-stop f-forward b-backward l-low m-medium h-high e-ecommandit")
# print("\n")