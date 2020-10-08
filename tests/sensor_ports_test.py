from src.modules.sensors import Sensor

for address in range(0x0, 0xFF):
    print("Checking port with address : {}. Stand By.".format(address))
    port = Sensor(address)
