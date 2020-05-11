# Derived from https://github.com/the-raspberry-pi-guy/lcd

# This is the driver library for the LCD display
# Creditis: natbett of the Raspberry Pi Forum, 2018 Feb 18th
# https://www.raspberrypi.org/forums/viewtopic.php?p=1314949&sid=385c6b728fc3ce85142749e13967cc54

import lcddriver
import time

display = lcddriver.lcd()

def message_to_screen():
    try:
            display.lcd_display_string("Hello world!", 1)
            display.lcd_display_string("Line 2 :)", 2)
            # TODO: use threading
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

    display.lcd_clear()


def long_string(text = '', num_line = 1, num_cols = 16):
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
	time.sleep(2)
	display.lcd_clear()


if __name__ == "__main__":
        message_to_screen()
