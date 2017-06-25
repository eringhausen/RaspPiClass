import RPi.GPIO as GPIO
import time

led_pin=22
GPIO.setmode(GPIO.BCM)
GPIO.setup(led_pin, GPIO.OUT)
pwm_led=GPIO.PWM(led_pin, 500)
duty=50
pwm_led.start(duty)

switch_pin1 = 23

GPIO.setup(switch_pin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

switch_pin2 = 24
GPIO.setup(switch_pin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

while True:
	pwm_led.ChangeDutyCycle(duty)
	if GPIO.input(switch_pin1)==True:
	   if duty<100:
		duty+=5
	   time.sleep(0.2)
	if GPIO.input(switch_pin2)==True:
	    if duty>10:
		duty-=5
	    time.sleep(0.2)
		
finally:
	print("Cleaning up")
	GPIO.cleanup()	
		 
