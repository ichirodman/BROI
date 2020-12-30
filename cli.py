import sys
import os

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('.') + "/libs")

import click
import subprocess

from broi.components.sensors import Sensor
from broi.robbo_olympic import RobboOlympic


@click.group()
def cli():
    pass


@click.command(name='main')
def main():
    print("Run main")


@click.command(name='runtask', help='Util for running scripts from user\'s device on the robot')
@click.argument('executable_file_path', type=click.Path())
def run_task(executable_file_path: str):
    executable_file_path = 'tests/{}'.format(executable_file_path)
    _root_path = os.path.abspath('.')

    file_beginning_import_code = 'import sys\nimport os\nsys.path.insert(0, \'{}\')\nsys.path.insert(0,\'{}/libs\')\n'.format(
        _root_path, _root_path)

    with open(executable_file_path, 'r') as src_file:
        src_file_content = '\n'.join(src_file.readlines())

    if file_beginning_import_code not in src_file_content:
        with open(executable_file_path, 'w') as src_file:
            src_file.write('{}\n{}'.format(file_beginning_import_code, src_file_content))

    _script = subprocess.Popen(['python3', executable_file_path], shell=False,
                               stdout=sys.stdout, stderr=sys.stderr)
    try:
        _script.wait()

        _exit_code = _script.returncode

        if _exit_code:
            raise Exception(executable_file_path, _exit_code)
        else:
            print('Subprocess\'s finished. Bye.')
    except KeyboardInterrupt:
        _script.kill()
        print('Was interrupted. Bye.')


@click.command(name='st', help='Sensors test')
def sensor_test():
    for sensor_position, position_name in zip([Sensor.F_S_L, Sensor.F_S_R, Sensor.R_S_F, Sensor.R_S_B,
                                               Sensor.B_S_R, Sensor.B_S_L, Sensor.L_S_B, Sensor.L_S_F],
                                              ["F_S_L", "F_S_R", "R_S_F", "R_S_B", "B_S_R", "B_S_L", "L_S_B", "L_S_F"]):
        print('Connecting to {}'.format(position_name))
        sensor = Sensor(sensor_position)
        try:
            sensor.get_distance()
            values = 'Values from : '
            for _ in range(10):
                values += str(sensor.get_distance()) + ' ;'
            print(values)
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
cli.add_command(run_task)
cli.add_command(sensor_test)
cli.add_command(gear_debug)

if __name__ == "__main__":
    cli()
