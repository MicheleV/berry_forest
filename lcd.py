# Derivative work of https://github.com/the-raspberry-pi-guy/lcd

# This is the driver library for the LCD display
# Creditis: natbett of the Raspberry Pi Forum, 2018 Feb 18th
# https://www.raspberrypi.org/forums/viewtopic.php?p=1314949&sid=385c6b728fc3ce85142749e13967cc54
from threading import Thread
from threading import Lock
import time

import lcddriver

display = lcddriver.lcd()
lock = Lock()


def _message_to_screen():
    try:
        lock.acquire()
        display.lcd_display_string("Hello world!", 1)
        display.lcd_display_string("Line 2 :)", 2)
        time.sleep(2)
        display.lcd_clear()
        display.lcd_display_string("New line 1", 1)
        display.lcd_display_string("... new line 2", 2)
        time.sleep(2)
        display.lcd_clear()
        time.sleep(2)

    except KeyboardInterrupt:
        print("Cleaning up!")
        display.lcd_clear()

    finally:
        lock.release()
        display.lcd_clear()


def _long_string(text='', num_line=1, num_cols=16, clean_after=True, step=1,
                wait=2):
    """
    This function display on a LED screen the given string
    Parameters:
      text: text to display on the screen
      num_line: row of the display to use
      num_cols: number ofcolumns of your display
      clean_after: whether to reset the display when done
      step: seconds to wait before before and after scrolling the text
      wait: seconds to wait after displaying the last char to the screen
    """
    try:
        lock.acquire()
        if(len(text) > num_cols):
            display.lcd_display_string(text[:num_cols], num_line)
            time.sleep(step)
            for i in range(len(text) - num_cols + 1):
                text_to_print = text[i:i+num_cols]
                display.lcd_display_string(text_to_print, num_line)
                time.sleep(0.2)
            time.sleep(step)
        else:
            display.lcd_display_string(text, num_line)
        time.sleep(wait)
        if clean_after:
            display.lcd_clear()

    finally:
        lock.release()


def long_string(text='', num_line=1, num_cols=16, clean_after=True, step=1,
                wait=2):
    """
    This function start a thread to display on a LED screen the given string
    Parameters:
      text: text to display on the screen
      num_line: row of the display to use
      num_cols: number ofcolumns of your display
      clean_after: whether to reset the display when done
      step: seconds to wait before before and after scrolling the text
      wait: seconds to wait after displaying the last char to the screen
    """
    light = Thread(target=_long_string, kwargs=locals()).start()


def message_to_screen():
    light = Thread(target=_message_to_screen).start()


if __name__ == "__main__":
    message_to_screen()
