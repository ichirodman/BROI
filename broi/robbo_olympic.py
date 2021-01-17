from broi.components.gear import Gear
from broi.components.sensors import Sensor


class RobboOlympic:
    _gear = None
    _sensor_f_s_l, _sensor_f_s_r = None, None
    _sensor_r_s_f, _sensor_r_s_b = None, None
    _sensor_b_s_r, _sensor_b_s_l = None, None
    _sensor_l_s_b, _sensor_l_s_f = None, None

    def __init__(self, init_sensors = True):
        self._gear = Gear()
        if init_sensors:
            self._sensor_f_s_l = Sensor(Sensor.F_S_L)
            self._sensor_f_s_r = Sensor(Sensor.F_S_R)
            self._sensor_r_s_f = Sensor(Sensor.R_S_F)
            self._sensor_r_s_b = Sensor(Sensor.R_S_B)
            self._sensor_b_s_r = Sensor(Sensor.B_S_R)
            self._sensor_b_s_l = Sensor(Sensor.B_S_L)
            self._sensor_l_s_b = Sensor(Sensor.L_S_B)
            self._sensor_l_s_f = Sensor(Sensor.L_S_F)

    def move_forward(self, power_value):
        self._gear.power(power_value, power_value, power_value, power_value)

    def move_backward(self, power_value):
        self.move_forward(-power_value)

    def move_left(self, power_value):
        self._gear.power(-power_value, power_value, power_value, -power_value)

    def move_right(self, power_value):
        self.move_left(-power_value)

    def move_counterclockwise(self, power_value):
        self._gear.power(-power_value, power_value, -power_value, power_value)

    def move_clockwise(self, power_value):
        self.move_counterclockwise(-power_value)

    def stop_moving(self):
        self._gear.power(0, 0, 0, 0)

    def get_f_s_l_distance(self):
        return self._sensor_f_s_l.get_distance()

    def get_f_s_r_distance(self):
        return self._sensor_f_s_r.get_distance()

    def get_r_s_f_distance(self):
        return self._sensor_r_s_f.get_distance()

    def get_r_s_b_distance(self):
        return self._sensor_r_s_b.get_distance()

    def get_b_s_r_distance(self):
        return self._sensor_b_s_r.get_distance()

    def get_b_s_l_distance(self):
        return self._sensor_b_s_l.get_distance()

    def get_l_s_b_distance(self):
        return self._sensor_l_s_b.get_distance()

    def get_l_s_f_distance(self):
        return self._sensor_l_s_f.get_distance()

    def power_off(self):
        pass
