# Copyright: (c) 2020, Michele Valsecchi <https://github.com/MicheleV>
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
import os

from dotenv import load_dotenv
import Adafruit_DHT
from gpiozero import CPUTemperature

load_dotenv()

# Temperature and humidity sensor type
# https://github.com/adafruit/Adafruit_Python_DHT/blob/master/Adafruit_DHT/common.py#L34-L38
DHT_TYPE = int(os.getenv("DHT_TYPE"))
DHT_SENSOR_PIN = int(os.getenv("DHT_SENSOR_PIN"))


def get_external_temp():
    humidity, temperature = Adafruit_DHT.read_retry(DHT_TYPE, DHT_SENSOR_PIN)
    return humidity, temperature


def get_formatted_external_temp():
    hum, temp = get_external_temp()
    message = 'Temp: {0:0.1f} C  Humidity: {1:0.1f} %'.format(temp, hum)
    return message


def get_pi_temperature():
    """
    Return CPU temperature (floating, 3 decimals)
    """
    temp = str(CPUTemperature().temperature)
    return temp
