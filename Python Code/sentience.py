# TODO Begin proximity sensor

import gpiozero
import time

def Ping():
    TRIG = 17
    ECHO = 27
    pulse_start = time.time()

    trigger = gpiozero.OutputDevice(TRIG)
    echo = gpiozero.DigitalInputDevice(ECHO)

    trigger.on()
    time.sleep(0.00001)
    trigger.off()

    while echo.is_active == False:
        pulse_start = time.time()

    while echo.is_active == True:
        pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start
    distance = 34300 * (pulse_duration/2)
    round_distance = round(distance, 1)
    return(round_distance)

while True:
    Ping()


# TODO End of proximity sensor