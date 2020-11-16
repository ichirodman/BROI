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
    for sensor_position in [Sensor.F_S_L, Sensor.F_S_R, Sensor.R_S_F, Sensor.R_S_B,
                            Sensor.B_S_R, Sensor.B_S_L, Sensor.L_S_B, Sensor.L_S_R]:
        Sensor(sensor_position)


cli.add_command(main)
cli.add_command(sensor_test)

if __name__ == "__main__":
    cli()
