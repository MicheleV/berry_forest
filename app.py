# Copyright: (c) 2020, Michele Valsecchi <https://github.com/MicheleV>
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
import os
import bottle
from bottle import route, response, static_file, run
import led
import lcd
import sys
import time
from temperature import get_external_temp
from temperature import get_pi_temperature
import json


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

# NOTE: this is a POC and all the operation below are syncronous!!!
# Rewrite using threads https://bottlepy.org/docs/dev/async.html
# or refer to https://stackoverflow.com/a/37230303


@app.route('/red')
@enable_cors
def hello():
    led.light_led(led.RED)
    return json.dumps({"result": {"led": "red"}})


@app.route('/green')
@enable_cors
def hello():
    led.light_led(led.GREEN)
    return json.dumps({"result": {"led": "green"}})


@route('/greetings')
@enable_cors
def greetings():
    lcd.message_to_screen()
    return json.dumps({"result": "success"})


@route('/temperature/external')
@enable_cors
def temperature():
    hum, temp = get_external_temp()
    message = 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temp, hum)

    lcd.long_string(message, 1)
    return json.dumps({"result": {"temperature": temp, "humidity": hum}})


@route('/temperature/internal')
@enable_cors
def temperature():
    message = get_pi_temperature()

    lcd.long_string(message, 1)
    return json.dumps({"result": message})


@route('/<filename>')
def server_static(filename):
    return static_file(filename, root='./templates')


run(host='0.0.0.0', port=8080, debug=True)
