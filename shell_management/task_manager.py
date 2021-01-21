import json
import subprocess
import sys
import typing


class TaskManager:
    __TASK_FILE_PATH = 'shell_management/tasks.json'

    @staticmethod
    def run_task(task_name: str):
        _task = TaskManager.get_task(task_name)
        if _task is None:
            print('There\'s no task with such name \'{}\''.format(task_name))
        else:
            TaskManager.run_script(_task['executable'], _task['include_module'])

    @staticmethod
    def run_script(executable_filepath: str, include_module: str = None):
        TaskManager.__load_include_directives(executable_filepath, include_module)

        _script = subprocess.Popen(['python3', executable_filepath], shell=False, stdout=sys.stdout, stderr=sys.stderr)

        try:
            _script.wait()
            _exit_code = _script.returncode
            if _exit_code:
                raise Exception(executable_filepath, _exit_code)
            else:
                print('Subprocess\'s finished. Bye.')
        except KeyboardInterrupt:
            _script.kill()
            print('Subprocess was interrupted. Bye.')

    @staticmethod
    def update_tasks(tasks_to_add: list, tasks_to_remove: list) -> None:
        TaskManager.__remove_tasks(tasks_to_remove)
        TaskManager.__add_tasks(tasks_to_add)

    @staticmethod
    def get_task(task_name: str) -> typing.Any:
        return None if not TaskManager.__has_task(task_name) else \
            list(filter(lambda task: task['name'] == task_name, TaskManager.get_tasks()))[0]

    @staticmethod
    def get_tasks() -> list:
        with open(TaskManager.__TASK_FILE_PATH, 'r') as _tasks_file:
            _tasks = json.loads(''.join(_tasks_file.readlines()))
            _tasks_file.close()
        for i in range(len(_tasks)):
            if 'include_module' not in _tasks[i].keys():
                _tasks[i]['include_module'] = None
        return _tasks

    @staticmethod
    def __has_task(task_name: str) -> bool:
        return len(list(filter(lambda task: task['name'] == task_name, TaskManager.get_tasks()))) > 0

    @staticmethod
    def __add_tasks(tasks_to_add: list) -> None:
        _tasks = TaskManager.get_tasks()
        _tasks_to_add_names = [task['name'] for task in tasks_to_add]
        _tasks_names_to_replace = [task['name'] for task in _tasks if task['name'] in _tasks_to_add_names]
        TaskManager.__remove_tasks(_tasks_names_to_replace)

        _tasks = TaskManager.get_tasks()
        for task_to_add in tasks_to_add:
            _new_task = {'name': task_to_add['name'], 'executable': task_to_add['executable'],
                         'include_module': task_to_add['include_module']}
            _tasks.append(_new_task)
        TaskManager.__load_tasks(_tasks)

    @staticmethod
    def __remove_tasks(tasks_names_to_remove: list) -> None:
        _tasks_to_load = [task for task in TaskManager.get_tasks() if task['name'] not in tasks_names_to_remove]
        TaskManager.__load_tasks(_tasks_to_load)

    @staticmethod
    def __load_tasks(tasks_to_load: list) -> None:
        with open(TaskManager.__TASK_FILE_PATH, 'w') as _tasks_file:
            _tasks = json.dumps(tasks_to_load)
            _tasks_file.truncate()
            _tasks_file.seek(0)
            _tasks_file.write(_tasks)
            _tasks_file.seek(0)
            _tasks_file.close()

    @staticmethod
    def __load_include_directives(relative_filepath: str, include_module_relative_path: str = None) -> None:
        with open(relative_filepath, 'r') as _file:
            _file_content = ''.join(_file.readlines())
            _file.close()

        with open(relative_filepath, 'w') as _file:
            _import_code = 'import sys\nimport os\n'
            if _import_code != _file_content[:len(_import_code)]:
                _file.write(_import_code)

            _include_code_template = "sys.path.insert(0, \'{}\')\n"

            for _include_path in ['.', './external_libs', include_module_relative_path]:
                _include_code = _include_code_template.format(_include_path)
                if _include_path is not None and _include_code not in _file_content:
                    _file.write(_include_code)

            _file.write(_file_content)
