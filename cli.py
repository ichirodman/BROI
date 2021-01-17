import sys
import os

sys.path.insert(0, os.path.abspath('.'))
sys.path.insert(0, os.path.abspath('.') + "/libs")

import click
import json

from shell_management.task_manager import TaskManager
from shell_management.components_test_manager import ComponentsTestManager


@click.group()
def cli():
    pass


@click.command(name='showtasks', help='Show tasks\' info')
def show_tasks_info():
    _task_view_template = 'Name: {}\nExecutable: {}\nInclude module: {}\n\n'
    for task in TaskManager.get_tasks():
        print(_task_view_template.format(task['name'], task['executable'], task['include_module']))


@click.command(name='execute', help='Util for running python scripts without modules yet')
@click.argument('executable_file_path', type=click.Path())
def run_script(executable_file_path: str):
    TaskManager.run_script(executable_file_path)


@click.command(name='runtask', help='Util for running tasks recorded in tasks.json')
@click.argument('task_name', type=click.STRING)
def run_task(task_name: str):
    TaskManager.run_task(task_name)


@click.command(name='update_tasks', help='Updated tasks file')
@click.argument('tasks_to_add', type=click.STRING)
@click.argument('tasks_names_to_remove', type=click.STRING)
def update_tasks(tasks_to_add: str, tasks_names_to_remove: str):
    tasks_to_add = json.loads(tasks_to_add)
    tasks_names_to_remove = json.loads(tasks_names_to_remove)
    TaskManager.update_tasks(tasks_to_add, tasks_names_to_remove)


@click.command(name='ts', help='Test sensors')
def test_sensors():
    ComponentsTestManager.test_sensors()


@click.command(name='tg', help='Test gear')
def test_gear():
    ComponentsTestManager.test_gear()


cli.add_command(show_tasks_info)
cli.add_command(run_script)
cli.add_command(run_task)
cli.add_command(update_tasks)
cli.add_command(test_sensors)
cli.add_command(test_gear)

if __name__ == "__main__":
    cli()

'''
from pynput import keyboard
from pynput.keyboard import Key

def on_press(key):
    #handle pressed keys
    pass

def on_release(key):
    #handle released keys
    if(key==Key.enter):
        function_x()

with keyboard.Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
'''
