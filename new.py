from math import sin, cos, pi
from lx16a import *
import time

LX16A.initialize("/dev/ttyUSB0")

try:
    servo1 = LX16A(5)
    servo2 = LX16A(6)
    servo3 = LX16A(7)
    servo4 = LX16A(8)
    servo5 = LX16A(9)
    servo6 = LX16A(10)

    servo1.set_angle_limits(0, 240)
    servo2.set_angle_limits(0, 240)
    servo3.set_angle_limits(0, 240)
    servo4.set_angle_limits(0, 240)
    servo5.set_angle_limits(0, 240)
    servo6.set_angle_limits(0, 240)

except ServoTimeoutError as e:
    print(f"Servo {e.id_} is not responding. Exiting...")
    quit()

t = 0
while True:
    servo1.move(sin(t) * 60 + 60)
    servo2.move(sin(t) * 60 + 60)
    servo3.move(sin(t) * 60 + 60)
    servo4.move(-sin(t) * 60 + 60)
    servo5.move(-sin(t) * 60 + 60)
    servo6.move(-sin(t) * 60 + 60)

    time.sleep(0.05)
    t += 0.1
