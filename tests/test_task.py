import time

from broi.robbo_olympic import RobboOlympic

ro = RobboOlympic(init_sensors=False)

ro.move_forward(600)
time.sleep(1)
ro.stop_moving()

ro.move_right(600)
time.sleep(1)
ro.stop_moving()

ro.move_clockwise(600)
time.sleep(1)
ro.stop_moving()

print('That\'s all')
