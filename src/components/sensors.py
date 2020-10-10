'''
import time
import RPi.GPIO as GPIO
import VL53L0X
'''

from config.distance_sensors import *


class Sensor:
    _ADDRESS = None
    _sensor_interface = None

    def __init__(self, sensor_address):
        self._ADDRESS = sensor_address
        print("Hello, sensor, {}".format(sensor_address))
        '''
        self._init()

    def _init(self):
        self._sensor_interface = VL53L0X.VL53L0X(address=0x2B)
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._ADDRESS, GPIO.OUT)
        GPIO.output(self._ADDRESS, GPIO.LOW)
        time.sleep(0.5)
        GPIO.output(self._ADDRESS, GPIO.HIGH)
        time.sleep(0.5)
        self._sensor_interface.start_ranging(4)
        time.sleep(0.5)
        timing = min(self._sensor_interface.get_timing(), 20000)
        print("timing %d ms" % (timing / 1000))
        '''

    def get_distance(self):
        pass
