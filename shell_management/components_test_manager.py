from broi.robbo_olympic import RobboOlympic
from broi.components.sensors import Sensor


class ComponentsTestManager:
    @staticmethod
    def test_sensors():
        _all_sensors = [Sensor.F_S_L, Sensor.F_S_R, Sensor.R_S_F, Sensor.R_S_B,
                        Sensor.B_S_R, Sensor.B_S_L, Sensor.L_S_B, Sensor.L_S_F]
        _sensors_positions = ["F_S_L", "F_S_R", "R_S_F", "R_S_B", "B_S_R", "B_S_L", "L_S_B", "L_S_F"]
        for sensor_position, position_name in zip(_all_sensors, _sensors_positions):
            print('Connecting to {}'.format(position_name))
            _sensor = Sensor(sensor_position)
            try:
                _sensor.get_distance()
                _values = 'Values from : '
                for _ in range(10):
                    _values += str(_sensor.get_distance()) + ' ;'
                print('{}\n'.format(_values))
            except AttributeError:
                print('Sensor is not set')
            print('-' * 20)

    @staticmethod
    def test_gear():
        _robot = RobboOlympic(init_sensors=False)
        _test_methods = [_robot.stop_moving, lambda: _robot.move_forward(600), lambda: _robot.move_backward(600),
                         lambda: _robot.move_left(600), lambda: _robot.move_right(600),
                         lambda: _robot.move_clockwise(600), lambda: _robot.move_counterclockwise(600)]
        while True:
            try:
                _code_num = int(input())
                _test_methods[_code_num]()
            except (ValueError, IndexError):
                print('Try again')
