import sys
import os

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('.') + "/libs")

import click
from src.components.sensors import Sensor


@click.group()
def cli():
    pass


@click.command(name='main')
def main():
    print("Run main")


@click.command(name='st', help='Sensors test')
def sensor_test():
    for sensor_position, position_name in zip([Sensor.F_S_L, Sensor.F_S_R, Sensor.R_S_F, Sensor.R_S_B,
                                               Sensor.B_S_R, Sensor.B_S_L, Sensor.L_S_B, Sensor.L_S_F],
                                              ["F_S_L", "F_S_R", "R_S_F", "R_S_B", "B_S_R", "B_S_L", "L_S_B", "L_S_F"]):
        print('Connecting to {}'.format(position_name))
        sensor = Sensor(sensor_position)
        try:
            sensor.get_distance()
            print('Values from : ', end='')
            for _ in range(10):
                print(sensor.get_distance(), end='; ')
        except AttributeError:
            print('Sensor is not set')
        print('-' * 20)


cli.add_command(main)
cli.add_command(sensor_test)

if __name__ == "__main__":
    cli()
