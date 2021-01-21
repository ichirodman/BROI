import click
import json

from shell_management.task_manager import TaskManager
from shell_management.components_test_manager import ComponentsTestManager
from shell_management.system_processes_manager import SystemProcessesManager


@click.group()
def cli():
    pass


@click.command(name='execute', help='Util for running python scripts without modules yet')
@click.argument('executable_file_path', type=click.Path())
def run_script(executable_file_path: str):
    if not SystemProcessesManager.are_there_other_user_scripts():
        TaskManager.run_script(executable_file_path)


@click.command(name='showtasks', help='Show tasks\' info')
def show_tasks_info():
    _task_view_template = 'Name: {}\nExecutable: {}\nInclude module: {}\n\n'
    for task in TaskManager.get_tasks():
        print(_task_view_template.format(task['name'], task['executable'], task['include_module']))


@click.command(name='runtask', help='Util for running tasks recorded in tasks.json')
@click.argument('task_name', type=click.STRING)
def run_task(task_name: str):
    if not SystemProcessesManager.are_there_other_user_scripts():
        TaskManager.run_task(task_name)


@click.command(name='stoptasks', help='Stops running task mentioned in shell_state.json')
def stop_all_tasks():
    SystemProcessesManager.terminate_running_user_script()


@click.command(name='update_tasks', help='Update tasks file')
@click.argument('tasks_to_add', type=click.STRING)
@click.argument('tasks_names_to_remove', type=click.STRING)
def update_tasks(tasks_to_add: str, tasks_names_to_remove: str):
    tasks_to_add = json.loads(tasks_to_add)
    tasks_names_to_remove = json.loads(tasks_names_to_remove)
    TaskManager.update_tasks(tasks_to_add, tasks_names_to_remove)


@click.command(name='ts', help='Test sensors')
def test_sensors():
    if not SystemProcessesManager.are_there_other_user_scripts():
        ComponentsTestManager.test_sensors()


@click.command(name='tg', help='Test gear')
def test_gear():
    if not SystemProcessesManager.are_there_other_user_scripts():
        ComponentsTestManager.test_gear()


cli.add_command(show_tasks_info)
cli.add_command(run_script)
cli.add_command(run_task)
cli.add_command(stop_all_tasks)
cli.add_command(update_tasks)
cli.add_command(test_sensors)
cli.add_command(test_gear)

if __name__ == "__main__":
    cli()
