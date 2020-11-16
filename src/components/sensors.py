import time
import RPi.GPIO as GPIO
from libs.sensors.VL53L0X import VL53L0X

from config.distance_sensors import *


class Sensor:
    F_S_L, F_S_R, R_S_F, R_S_B, B_S_R, B_S_L, L_S_B, L_S_F = list(range(8))
    _ADDRESS = None
    _PIN = None
    _sensor_interface = None

    def __init__(self, sensor_position):
        self._ADDRESS = [SENSOR_F_S_L_ADDRESS, SENSOR_F_S_R_ADDRESS, SENSOR_R_S_F_ADDRESS, SENSOR_R_S_B_ADDRESS,
                         SENSOR_B_S_R_ADDRESS, SENSOR_B_S_L_ADDRESS, SENSOR_L_S_B_ADDRESS, SENSOR_L_S_F_ADDRESS] \
            [sensor_position]
        self._PIN = [SENSOR_F_S_L_PIN, SENSOR_F_S_R_PIN, SENSOR_R_S_F_PIN, SENSOR_R_S_B_PIN,
                     SENSOR_B_S_R_PIN, SENSOR_B_S_L_PIN, SENSOR_L_S_B_PIN, SENSOR_L_S_F_PIN][sensor_position]
        self._setup()

    def _setup(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._PIN, GPIO.OUT)
        GPIO.output(self._PIN, GPIO.LOW)
        self._sensor_interface = VL53L0X(address=self._ADDRESS)
        print(self._sensor_interface)
        time.sleep(0.5)
        GPIO.output(self._PIN, GPIO.HIGH)
        time.sleep(0.5)
        self._sensor_interface.start_ranging(4)
        time.sleep(0.5)
        timing = min(self._sensor_interface.get_timing(), 20000)
        print("timing %d ms" % (timing / 1000))

    def unplug(self):
        GPIO.output(self._PIN, GPIO.LOW)

    def get_distance(self):
        return max(0, min(1000, self._sensor_interface.get_distance()))
