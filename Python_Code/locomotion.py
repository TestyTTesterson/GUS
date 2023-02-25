
import gpiozero
from time import sleep
from collisiondetection import checkpath
from collisionavoision import collisionavoision
#  this is what we have to multiply the step distance by in order to get
#  the length of time to run the motor.
stepDistanceTimeconversion = 1
rotationMultiplier = 1
wheels=gpiozero.Robot(left=(5,6),right=(16,19))
def movement(GUS, command):
    
    if checkpath(GUS) == False:

        if 'n' in command:
            print("(n)o go")
            wheels.stop()
            # GUS.rightMotor = 'STOP!!!'

        elif 'f' in command:
            print("(f)orward")
            wheels.forward()
            sleep(GUS.stepdistance)
            wheels.stop()
            #GUS.leftMotor = 'Forward for for (stepMutltiplier * GUS.stepdistance) seconds'
            #GUS.rightMotor = 'Forward for (stepMultiplier * GUS.stepdistance) seconds'

        elif 'b' in command:
            print("(b)ack")
            wheels.backward()
            sleep(GUS.stepdistance)
            wheels.stop()
            #GUS.leftMotor = 'Reverse for for (stepMutltiplier * GUS.stepdistance) seconds'
            #GUS.rightMotor = 'Reverse for (stepMultiplier * GUS.stepdistance) seconds'

        elif 'l' in command:
            print('(l)eft')
            wheels.left()
            sleep(GUS.stepdistance)
            wheels.stop()
            #GUS.leftMotor = 'Reverse for for (rotationMutltiplier) seconds'
            #GUS.rightMotor = 'Forward for (rotationMultiplier) seconds'
            #GUS.leftMotor = 'STOP!!!'
            #GUS.rightMotor = 'STOP!!!'

        elif 'r' in command:
            print('(r)ight')
            wheels.right()
            sleep(GUS.stepdistance)
            wheels.stop()
            #GUS.rightMotor = 'Reverse for for (rotationMutltiplier) seconds'
            #GUS.leftMotor = 'Forward for (rotationMultiplier) seconds'
            #GUS.leftMotor = 'STOP!!!'
            #GUS.rightMotor = 'STOP!!!'

        elif 'w' in command:
            print("(w)alk")
            GUS.stepdistance = 0.25

        elif 't' in command:
            print("(t)rot")
            GUS.stepdistance = 0.5
        
        elif 'g' in command:
            print("(g)allop")
            GUS.stepdistance = 0.75
    
        else:
            print("<<<  wrong data  >>>")
            print("please enter the defined data to continue.....")
    else:
        return("Avoision required!")
        collisionavoision(GUS)
        



