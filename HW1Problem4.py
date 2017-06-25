"Elizabeth Ringhausen"
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

number=input("Please enter a number between 1 and 3")
num=int(number)

pins = [17,18,27]

    GPIO.setup(pin, GPIO.OUT)
    if num==1:
        GPIO.output(pins1,(1))
    elif num==2:
        GPIO.output(pins1,(2))
    elif num==3:
        GPIO.output(pins1,(3))
    else:
        print("You did not enter a number between 1 and 3")
GPIO.cleanup()
