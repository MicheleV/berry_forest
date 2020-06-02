# Copyright: (c) 2020, Michele Valsecchi <https://github.com/MicheleV>
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
import json
import os
import time

import bottle
from bottle import static_file
from bottle import route
from bottle import run
from bottle import template
import led
import lcd
import sys

from temperature import get_external_temp
from temperature import get_pi_temperature
from utils import enable_cors

app = bottle.app()


@route('/')
def home():
    return template('templates/index.tpl')


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
    tmp_msg = 'Temp: {0:0.1f} C'.format(temp)
    hum_msg = 'Humidity: {0:0.1f} %'.format(hum)

    lcd.long_string(tmp_msg, num_line=1, clean_after=False, step=0, wait=0)
    lcd.long_string(hum_msg, num_line=2, step=0, wait=3)

    return json.dumps({"result": {"temperature": temp, "humidity": hum}})


@route('/temperature/internal')
@enable_cors
def temperature():
    message = get_pi_temperature()

    lcd.long_string(message, 1)
    return json.dumps({"result": message})


# @route('/<filename>')
# def server_static(filename):
#     return static_file(filename, root='./templates')


run(host='0.0.0.0', port=8080, debug=True)
