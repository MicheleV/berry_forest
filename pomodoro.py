from datetime import datetime
import time

import led


def pomodoro(timer_name, pom_length):
    ticks = 0
    while ticks < pom_length:
        # TODO: this should using threads as well...
        time.sleep(1)
        ticks += 1
    print("POMODORO was completed!")
    led.light_led(led.RED)
