# Copyright: (c) 2019, Michele Valsecchi <https://github.com/MicheleV>
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

import bottle
from bottle import route, response, static_file, run
import time
import led
import lcd


import lcddriver
import time
from pomodoro import pomodoro

import sys
from threading import Thread
import Adafruit_DHT

# Temperature and humidity sensor type
# https://github.com/adafruit/Adafruit_Python_DHT/blob/master/Adafruit_DHT/common.py#L34-L38
DHT_TYPE = 11

# Define sensors pins
DHT_SENSOR_PIN = 14

app = bottle.app()

# Credits: https://stackoverflow.com/a/17262900
def enable_cors(fn):
    def _enable_cors(*args, **kwargs):
        # set CORS headers
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, POST, PUT, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

        if bottle.request.method != 'OPTIONS':
            # actual request; reply with the actual response
            return fn(*args, **kwargs)

    return _enable_cors

@app.route('/red')
@enable_cors
def hello():
    led.light_led(led.RED)
    return "RED"

@app.route('/green')
@enable_cors
def hello():
    led.light_led(led.GREEN)
    return "GREEN"

@route('/greetings')
@enable_cors
def greetings():
    lcd.message_to_screen()

@route('/temperature')
@enable_cors
def temperature():
    display_to_lcd = True
    display = lcddriver.lcd()

    humidity, temperature = Adafruit_DHT.read_retry(DHT_TYPE, DHT_SENSOR_PIN)
    message = 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)

    lcd.long_string(message, 1)
    return 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)

# HACK: we're using a global variable!
# NOTE: Initialize timer so that '/status/ route won't throw errors
timer = Thread()

@route('/pomodoro')
def pomodoro_route():
    global timer
    print('inside pomodoro')
    if (timer.is_alive()):
        print('One pomodoro at the time, please')
        return 'BUSY'
    else:
        # TODO: get the length from post/get params
        timer = Thread(target=pomodoro, args=("Multithreaded timer 1", 3))
        timer.start()
        return 'POMODORO'

@route('/pomodoro/status')
def pomodoro_route():
    global timer
    print(timer.is_alive())
    print('inside status')
    return str(timer.is_alive())


@route('/<filename>')
def server_static(filename):
   return static_file(filename, root='./templates')

run(host='0.0.0.0', port=8080, debug=True)
