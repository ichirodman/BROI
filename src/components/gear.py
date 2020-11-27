import serial


class Gear:
    _ABS_LIMIT_VALUE: int = 255
    _gear_f_s_l_power_value, _gear_f_s_r_power_value, _gear_b_s_l_power_value, _gear_b_s_r_power_value \
        = 0, 0, 0, 0
    _gear_driver = None

    def __init__(self):
        self._gear_driver = serial.Serial(
            port='/dev/ttyS0',
            baudrate=9600,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=0.1
        )

    def power(self, gear_f_s_l_val, gear_f_s_r_val, gear_b_s_l_val, gear_b_s_r_val):
        self._gear_f_s_l_power_value = Gear._cut_signal(gear_f_s_l_val)
        self._gear_f_s_r_power_value = Gear._cut_signal(gear_f_s_r_val)
        self._gear_b_s_l_power_value = Gear._cut_signal(gear_b_s_l_val)
        self._gear_b_s_r_power_value = Gear._cut_signal(gear_b_s_r_val)
        self._driver_write_gears_values()

    def _driver_write_gears_values(self):
        encoded_signal = "{}q{}w{}e{}r{}t{}y{}u{}i".format(
            self._down_cut_signal(self._gear_f_s_l_power_value), self._up_cut_signal(self._gear_f_s_l_power_value),
            self._down_cut_signal(self._gear_f_s_r_power_value), self._up_cut_signal(self._gear_f_s_r_power_value),
            self._down_cut_signal(self._gear_b_s_l_power_value), self._up_cut_signal(self._gear_b_s_l_power_value),
            self._down_cut_signal(self._gear_b_s_r_power_value), self._up_cut_signal(self._gear_b_s_r_power_value))
        self._gear_driver.write(encoded_signal)

    @staticmethod
    def _cut_signal(val: int):
        return min(Gear._ABS_LIMIT_VALUE, max(-Gear._ABS_LIMIT_VALUE, val))

    @staticmethod
    def _up_cut_signal(val: int):
        return -min(0, Gear._cut_signal(val))

    @staticmethod
    def _down_cut_signal(val: int):
        return max(0, Gear._cut_signal(val))
