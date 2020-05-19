# Copyright: (c) 2020, Michele Valsecchi <https://github.com/MicheleV>
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
import RPi.GPIO as GPIO
import os
from dotenv import load_dotenv

from threading import Thread
import time

load_dotenv(verbose=True)

GREEN = int(os.getenv("GREEN"))
RED = int(os.getenv("RED"))


def _light_led(led, seconds=1):
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


# FIXME: this will throw an Exception if called too fast
# TODO: implement a throttle mechanism... or fix the led driver to be async :)
def light_led(led, seconds=1):
    light = Thread(target=_light_led, args=(led, seconds)).start()
