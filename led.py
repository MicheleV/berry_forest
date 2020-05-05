# Copyright: (c) 2020, Michele Valsecchi <https://github.com/MicheleV>
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
import RPi.GPIO as GPIO
import time

GREEN = 18
RED = 17


def light_led(led, seconds=1):
    """
    Lights up a led for a given amount of time
    """
    GPIO.setwarnings(True)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(led, GPIO.OUT)
    GPIO.output(led, GPIO.HIGH)

    time.sleep(seconds)

    GPIO.output(led, GPIO.LOW)

    GPIO.cleanup()
