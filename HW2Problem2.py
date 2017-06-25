import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

import time

pins = [4,17,18,27]
pause=0.2

while True:
    for i, pin in enumerate(pins):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin,1)
        time.sleep(pause)
        GPIO.output(pin,0)
        time.sleep(pause)
        print(pin)
    for i, pin in reversed(list(enumerate(pins))):
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin,1)
        time.sleep(pause)
        GPIO.output(pin,0)
        time.sleep(pause)
        print(pin)
GPIO.cleanup()
