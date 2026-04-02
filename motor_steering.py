
"""
Purpose:
Convert the steering value into left and right motor speeds.
"""
import numpy as np
from Motordriver import MotorRun, forward
<<<<<<< HEAD
from log_store import log_sto

=======
>>>>>>> ab2f61ab3dad8298b4646765e5853024ca61b109
def set_motor_speeds(steering_val, base_speed=90):

    left_speed = base_speed*(0.5+steering_val/100)
    right_speed = base_speed*(0.50-steering_val/100)

    left_speed = int(max(0, min(255, left_speed)))
    right_speed = int(max(0, min(255, right_speed)))

    print(f"L: {left_speed}, R: {right_speed}")
<<<<<<< HEAD
    log_sto(f"L: {left_speed}, R: {right_speed}")
=======
>>>>>>> ab2f61ab3dad8298b4646765e5853024ca61b109
    MotorRun(0, 'forward', left_speed)
    MotorRun(1, 'forward', right_speed)
