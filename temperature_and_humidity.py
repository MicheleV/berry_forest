# Derivative work of https://github.com/the-raspberry-pi-guy/lcd

# Standalone file to continuously display temperature & humidity on lcd display
# Creditis: natbett of the Raspberry Pi Forum, 2018 Feb 18th
# https://www.raspberrypi.org/forums/viewtopic.php?p=1314949&sid=385c6b728fc3ce85142749e13967cc54

import lcddriver
import time

import sys
import Adafruit_DHT


def long_string(display, text='', num_line=1, num_cols=16):
    """
    Parameters: (driver, string to print, number of line to print, number of
    columns of your display)
    Return: This function send to display your scrolling string.
    """
    if(len(text) > num_cols):
        display.lcd_display_string(text[:num_cols], num_line)
        time.sleep(1)
        for i in range(len(text) - num_cols + 1):
            text_to_print = text[i:i+num_cols]
            display.lcd_display_string(text_to_print, num_line)
            time.sleep(0.2)
        time.sleep(1)
    else:
        display.lcd_display_string(text, num_line)


if __name__ == '__main__':
    display_to_lcd = True
    display = lcddriver.lcd()
    while True:
        try:
            hum, tmp = Adafruit_DHT.read_retry(11, 14)
            message = 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(tmp, hum)
            if not display_to_lcd:
                print(message)
            else:
                long_string(display, message, 1)

        except KeyboardInterrupt:
            print("Cleaning up!")
            display.lcd_clear()
            break
