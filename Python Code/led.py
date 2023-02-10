import gpiozero
import time

ledViolet = gpiozero.LED(17)
ledRed = gpiozero.LED(4)

while True:
    ledViolet.on()
    ledRed.off()
    time.sleep(1)
    ledViolet.off()
    ledRed.on()
    time.sleep(1)
    

