

# import RPi.# GPIO as # GPIO 
import gpiozero
from time import sleep

ledViolet = gpiozero.LED(23)
ledGreen = gpiozero.LED(24)
ledRed = gpiozero.LED(25)
ledYellow = gpiozero.LED(26)
# in1 = 24
# in2 = 23
en = 25
forgettabletempvarname=1
# rightWheel = gpiozero.LED(24)
# leftWheel = gpiozero.LED(23)
# GPIO.setmode(# GPIO.BCM)
# GPIO.setup(in1,# GPIO.OUT)
# GPIO.setup(in2,# GPIO.OUT)
# GPIO.setup(en,# GPIO.OUT)
# rightWheel.OFF
# leftWheel.OFF


# TODO Must figure out this part instead of using LED.ON/OFF
#p=# GPIO.PWM(en,1000)
#  myMotor=gpiozero.Motor(23, 24)
# if myMotor._check_open:
#p.start(25)

def movement(command):
    # moved this inside the method for obvi reasons
    # thankfully it wasn't still just named temp
    forgettabletempvarname=1
    motorSpeed=1


    if 's' in command:
        print("stop")
        ledRed.on()
        sleep(1)
        ledRed.off()
        #myMotor.stop
        

    elif 'f' in command:
        print("forward")
        #myMotor.forward()
        ledGreen.on()
        sleep(1)
        ledGreen.off()
        forgettabletempvarname=1
        

    elif 'b' in command:
        print("back")
        #myMotor.backward()
        ledYellow.on()
        sleep(1)
        ledYellow.off()
        forgettabletempvarname=0
        

    elif 'l' in command:
        print("low")
        #motorSpeed=0.25
        ledViolet.on()
        sleep(1)
        ledViolet.off()
        # p.ChangeDutyCycle(25)
       

    elif 'm' in command:
        print("medium")
        #motorSpeed=0.5
        ledYellow.on()
        sleep(1)
        ledYellow.off()
        # p.ChangeDutyCycle(50)
        

    elif 'h' in command:
        print("high")
        #motorSpeed=0.75
        # p.ChangeDutyCycle(75)
        ledRed.on()
        sleep(1)
        ledRed.off()

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