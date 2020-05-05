# Copyright: (c) 2020, Michele Valsecchi <https://github.com/MicheleV>
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
import Adafruit_DHT
import bottle
from bottle import route, response, static_file, run
import led
import lcd
import sys
import time


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

# NOTE: this is POC and all the operation below are syncronous!!!
# Rewrite using threads https://bottlepy.org/docs/dev/async.html
# or refer to https://stackoverflow.com/a/37230303


@app.route('/red')
@enable_cors
def hello():
    led.light_led(led.RED)
    # TODO: return well-formed json
    return "RED"


@app.route('/green')
@enable_cors
def hello():
    led.light_led(led.GREEN)
    # TODO: return well-formed json
    return "GREEN"


@route('/greetings')
@enable_cors
def greetings():
    lcd.message_to_screen()


@route('/temperature')
@enable_cors
def temperature():

    humidity, temperature = Adafruit_DHT.read_retry(DHT_TYPE, DHT_SENSOR_PIN)
    message = 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temperature, humidity)

    lcd.long_string(message, 1)
    # TODO: return well-formed json
    return message


@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='./templates')


run(host='0.0.0.0', port=8080, debug=True)
