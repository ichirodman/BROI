from broi.components.sensors import Sensor

if __name__ == '__main__':
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
    exit()
