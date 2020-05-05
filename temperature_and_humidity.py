#!/usr/bin/python
# Import necessary libraries for communication and display use
import lcddriver
import time

import sys
import Adafruit_DHT


def long_string(display, text = '', num_line = 1, num_cols = 16):
	""" 
	Parameters: (driver, string to print, number of line to print, number of columns of your display)
	Return: This function send to display your scrolling string.
	"""
	if(len(text) > num_cols):
		display.lcd_display_string(text[:num_cols],num_line)
		time.sleep(1)
		for i in range(len(text) - num_cols + 1):
			text_to_print = text[i:i+num_cols]
			display.lcd_display_string(text_to_print,num_line)
			time.sleep(0.2)
		time.sleep(1)
	else:
		display.lcd_display_string(text,num_line)

# Main body of code
def message_to_screen(display, message_to_screen, line):
    display.lcd_display_string(message_to_screen, line) # Write line of text to first line of display

def clean_screen():
    display.lcd_clear()                               # Clear the display of any data

display_to_lcd = True
display = lcddriver.lcd()
# Source: https://www.circuitbasics.com/how-to-set-up-the-dht11-humidity-sensor-on-the-raspberry-pi/
while True:
    try:
        humidity, temperature = Adafruit_DHT.read_retry(11, 14)

        if not display_to_lcd:
            print('Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity))
        else:
            # Load the driver and set it to "display"
            # If you use something from the driver library use the "display." prefix first
            message = 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)
            long_string(display, message, 1)

    except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
        print("Cleaning up!")
        display.lcd_clear()
        break
