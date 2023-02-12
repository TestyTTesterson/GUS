# TODO Begin proximity sensor

import gpiozero
import time

#TRIG = 17
#ECHO = 27

#trigger = gpiozero.OutputDevice(TRIG)
#echo = gpiozero.DigitalInputDevice(ECHO)

def Ping(TRIG, ECHO):

    trigger = gpiozero.OutputDevice(TRIG,active_high=None)
    echo = gpiozero.DigitalInputDevice(ECHO,active_state=True)

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

#while True:
#    Ping()


# TODO End of proximity sensor