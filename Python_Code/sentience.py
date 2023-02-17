# ! Begin proximity sensor
import gps3
import time
import gpiozero
from gps3 import gps3
locale = gps3.GPSDSocket() 
the_fix = gps3.Fix()

TRIG = 17
ECHO = 27
trigger = gpiozero.OutputDevice(TRIG)
echo = gpiozero.DigitalInputDevice(ECHO)

def Ping():
    # args   TRIG, ECHO, trigger, echo
    pulse_start = time.time()
    pulse_end = time.time()

    trigger.on()
    time.sleep(0.00001)
    trigger.off()

    while echo.is_active == False:
        pulse_start = time.time()
        #print('echo off ')

    while echo.is_active == True:
        pulse_end = time.time()
        #print('echo on')

    pulse_duration = pulse_end - pulse_start
    distance = 34300 * (pulse_duration/2)
    round_distance = round(distance, 1)
    return(round_distance)

# TODO End of proximity sensor
# ! GPS
def getPositionData(gps3):
    try:
        for new_data in locale:
            if new_data:
                the_fix.refresh(new_data)
            if not isinstance(the_fix.TPV['lat'], str): # lat as determinate of when data is 'valid'
                speed = the_fix.TPV['speed']
                latitude = the_fix.TPV['lat']
                longitude = the_fix.TPV['lon']
                altitude  = the_fix.TPV['alt']  
    except KeyboardInterrupt:
        print("Caught keyboard interrupt, exiting")
    finally:
        locale.close()