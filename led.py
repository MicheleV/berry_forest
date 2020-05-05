import RPi.GPIO as GPIO
import time

GREEN = 18
RED = 17

def light_led(led):
        GPIO.setwarnings(True)
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(led, GPIO.OUT)
        GPIO.output(led, GPIO.HIGH)

        time.sleep(1)

        GPIO.output(led, GPIO.LOW)

        GPIO.cleanup()

