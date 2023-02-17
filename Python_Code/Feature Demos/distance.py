import gpiozero
import time

TRIG = 17
ECHO = 27
pulse_start = time.time()
trigger=gpiozero.OutputDevice(TRIG,active_high=True)
#trigger = gpiozero.OutputDevice(TRIG)
echo = gpiozero.DigitalInputDevice(ECHO,active_state=True)

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

print('Distance ', round_distance)
