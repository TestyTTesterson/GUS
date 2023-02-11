

# import RPi.# GPIO as # GPIO 
from time import sleep

in1 = 24
in2 = 23
en = 25
forgettabletempvarname=1

# GPIO.setmode(# GPIO.BCM)
# GPIO.setup(in1,# GPIO.OUT)
# GPIO.setup(in2,# GPIO.OUT)
# GPIO.setup(en,# GPIO.OUT)
# GPIO.output(in1,# GPIO.LOW)
# GPIO.output(in2,# GPIO.LOW)

#p=# GPIO.PWM(en,1000)
#p.start(25)

def movement(command):

    if command=='r':
        print("run")
        if(forgettabletempvarname==1):
            # GPIO.output(in1,# GPIO.HIGH)
            # GPIO.output(in2,# GPIO.LOW)
            print("forward")
            
        else:
            # GPIO.output(in1,# GPIO.LOW)
            # GPIO.output(in2,# GPIO.HIGH)
            print("backward")
            


    elif command=='s':
        print("stop")
        # GPIO.output(in1,# GPIO.LOW)
        # GPIO.output(in2,# GPIO.LOW)
        

    elif command=='f':
        print("forward")
        # GPIO.output(in1,# GPIO.HIGH)
        # GPIO.output(in2,# GPIO.LOW)
        forgettabletempvarname=1
        

    elif command=='b':
        print("back")
        # GPIO.output(in1,# GPIO.LOW)
        # GPIO.output(in2,# GPIO.HIGH)
        forgettabletempvarname=0
        

    elif command=='l':
        print("low")
        # p.ChangeDutyCycle(25)
       

    elif command=='m':
        print("medium")
        # p.ChangeDutyCycle(50)
        

    elif command=='h':
        print("high")
        # p.ChangeDutyCycle(75)
        
    elif command=='e':
        # GPIO.cleanup()

        exit()
    
    else:
        print("<<<  wrong data  >>>")
        print("please enter the defined data to continue.....")


# print("\n")
# print("The default speed & direction of motor is LOW & Forward.....")
# print("r-run s-stop f-forward b-backward l-low m-medium h-high e-ecommandit")
# print("\n")  

    
