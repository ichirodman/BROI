import sys

sys.path.insert(0, '/home/pi/NROIS')

from src.components.sensors import Sensor


if __name__ == '__main__':
    for address in range(0x0, 0xFF):
        print("Checking port with address : {}. Stand By.".format(address))
        port = Sensor(address)
