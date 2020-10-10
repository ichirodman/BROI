import sys
import os

sys.path.insert(0, os.path.abspath('.'))


import click
from src.components.sensors import Sensor


@click.group()
def cli():
    pass


@click.command(name='main')
def main():
    print("Run main")


@click.command(name='sensortest')
def sensor_test():
    print('Run sensor test')
    for check_address in range(0x20, 0x50):
        port_check = Sensor(check_address)


cli.add_command(main)
cli.add_command(sensor_test)

if __name__ == "__main__":
    cli()
