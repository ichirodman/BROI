import subprocess
import json
import sys
import os

from broi.robbo_olympic import RobboOlympic


class SystemProcessesManager:
    __SHELL_STATE_FILE_PATH = 'shell_management/shell_state.json'

    @staticmethod
    def are_there_other_user_scripts() -> bool:
        _running_pid = SystemProcessesManager.__get_user_running_process_id()
        print('running pid : {}'.format(_running_pid))
        if _running_pid is not None:
            return True
        else:
            _pid = os.getpid()
            SystemProcessesManager.__update_user_running_process_id(_pid)
            print('pid set : {}'.format(_running_pid))
            return False

    @staticmethod
    def terminate_running_user_script() -> None:
        _pid = SystemProcessesManager.__get_user_running_process_id()
        print('terminating pid : {}'.format(_pid))
        SystemProcessesManager.__kill_process(_pid)
        SystemProcessesManager.__update_user_running_process_id(-1)
        SystemProcessesManager.__stop_robot_move()

    @staticmethod
    def __get_user_running_process_id() -> int:
        _shell_state = SystemProcessesManager.__get_shell_state()
        print('shell state : {}'.format(_shell_state))
        return _shell_state['user_running_pid']

    @staticmethod
    def __update_user_running_process_id(pid: int) -> None:
        _shell_state = SystemProcessesManager.__get_shell_state()
        _shell_state['user_running_pid'] = pid if SystemProcessesManager.__is_valid_pid(pid) else None
        SystemProcessesManager.__write_shell_state(_shell_state)

    @staticmethod
    def __get_shell_state() -> dict:
        with open(SystemProcessesManager.__SHELL_STATE_FILE_PATH, 'r') as _state_file:
            _state_file_content = ''.join(_state_file.readlines()).replace('\n', '')
            _state_file.close()
        _shell_state = json.loads(_state_file_content)
        return _shell_state

    @staticmethod
    def __write_shell_state(new_state: dict) -> None:
        _new_state_file_content = json.dumps(new_state)
        with open(SystemProcessesManager.__SHELL_STATE_FILE_PATH, 'w') as _state_file:
            _state_file.truncate()
            _state_file.seek(0)
            _state_file.write(_new_state_file_content)
            _state_file.seek(0)
            _state_file.close()

    @staticmethod
    def __stop_robot_move() -> None:
        RobboOlympic(init_sensors=False).stop_moving()

    @staticmethod
    def __kill_process(pid: int) -> None:
        if SystemProcessesManager.__is_valid_pid(pid):
            subprocess.Popen(['kill', str(pid)], stdout=sys.stdout, stderr=sys.stderr).wait(2)
        else:
            raise RuntimeError('All processes are killed already. No running process with pid \'{}\' found.'.format(pid))

    @staticmethod
    def __is_valid_pid(pid: int) -> bool:
        return pid and pid != -1 and pid is not None
