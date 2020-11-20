import sys
import os

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('.') + "/libs")

import click
from src.components.sensors import Sensor
from src.robbo_olympic import RobboOlympic


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
            vals = 'Values from : '
            for _ in range(10):
                vals += str(sensor.get_distance()) + ' ;'
            print(vals)
            print()
        except AttributeError:
            print('Sensor is not set')
        print('-' * 20)


@click.command(name='gd', help='Gear debug')
def gear_debug():
    ro = RobboOlympic(init_sensors=False)
    while True:
        try:
            c = int(input())
            if c == 0:
                ro.stop_moving()
            elif c == 1:
                ro.move_forward(600)
            elif c == 2:
                ro.move_backward(600)
            elif c == 3:
                ro.move_left(600)
            elif c == 4:
                ro.move_right(600)
            elif c == 5:
                ro.move_counterclockwise(600)
            elif c == 6:
                ro.move_clockwise(600)

        except ValueError:
            print('Try again')
            

cli.add_command(main)
cli.add_command(sensor_test)
cli.add_command(gear_debug)

if __name__ == "__main__":
    cli()
