import time
import processing_parallel
from processing_parallel import process_frame
from motor_steering import set_motor_speeds
from Motordriver import stop_all,_send_command,turn_right

<<<<<<< HEAD
def avoid_obstacle():
    _send_command('forward')
    time.sleep(2.4)
    set_motor_speeds(25.0)
    time.sleep(1.0)
    _send_command('forward')
    time.sleep(3.3)
    set_motor_speeds(-30.0)
    time.sleep(2.0)
    _send_command('forward')
    time.sleep(2.8)
    set_motor_speeds(25.0)
    time.sleep(1.0)
=======
if find_obstacle:
    _send_command('backward')
    time.sleep(2)
    set_motor_speeds(30.0)
    time.sleep(1.2)
    _send_command('forward')
    time.sleep(3.0)
    set_motor_speeds(-30.0)
    time.sleep(1.2)
    _send_command('forward')
    time.sleep(8.0)
    set_motor_speeds(-30.0)
    time.sleep(1.2)
    _send_command('forward')
    time.sleep(3.0)
    set_motor_speeds(30.0)
    time.sleep(1.2)
>>>>>>> ab2f61ab3dad8298b4646765e5853024ca61b109

