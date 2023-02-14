# ! Begin proximity sensor

import time
import gpiozero
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