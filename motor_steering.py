"""
Purpose:
Control the robot's automatic movement.

Pseudocode:
1. Check whether auto mode is running.
2. Check whether a stop line has already been detected.
3. Receive the newest camera frame from the server layer.
4. Process the frame using OpenCV.
5. Use the steering value to control motor speeds.
6. If the horizontal stop line is detected, wait a few seconds so the robot
   can pass over the line, then stop the robot.
7. Allow the GUI Play/Stop buttons to start and stop automation.
"""

import time
import processing_parallel
from processing_parallel import process_frame
from motor_steering import set_motor_speeds
#from martian_detection.py import detect_face
from Motordriver import stop_all,_send_command,turn_right

# Auto-mode state variables
auto_running = False
stop_line_seen = False
stop_time = None

# How long the robot should keep moving after it detects the horizontal tape
# before stopping. You can tune this later if needed.
STOP_DELAY_SECONDS = 2.0

def start_automation():
    """
    Turn on automatic line-following mode.
    """
    global auto_running, stop_line_seen, stop_time

    auto_running = True
    stop_line_seen = False
    stop_time = None


def stop_automation(pause=False):
    """
    Turn off automatic line-following mode and stop the robot.
    """
    global auto_running, stop_line_seen, stop_time

    auto_running = pause
    stop_line_seen = False
    stop_time = None
    stop_all()


def is_running():
    """
    Return whether automatic mode is currently active.
    """
    return auto_running
def searching(horizontal_line,l,r):
    if not horizontal_line:
        _send_command("forward")
    elif horizontal_line and l and not r:
        print('turn right initialized')
        _send_command('forward')
        time.sleep(3.0)
        #print("turn right initialized")
        set_motor_speeds(40)
        time.sleep(1.4)
        _send_command('forward')
        time.sleep(1)
    else:
        stop_automation()

def update_automation(frame):
    """
    Process one frame of video and update robot behavior.

    Parameters:
        frame: The newest camera frame.

    Returns:
        out: The processed overlay image.
    """
    global auto_running, stop_line_seen, stop_time

    # Always process the frame so the processed stream can still display overlays
    out, steering_value, stop_line_detected, center_line,left,right,det_face = process_frame(frame)

    if not auto_running:
        return out,det_face

"""
Purpose:
Convert the steering value into left and right motor speeds.
"""
import numpy as np
from Motordriver import MotorRun, forward
def set_motor_speeds(steering_val, base_speed=90):

    left_speed = base_speed*(0.5+steering_val/100)
    right_speed = base_speed*(0.50-steering_val/100)

    left_speed = int(max(0, min(255, left_speed)))
    right_speed = int(max(0, min(255, right_speed)))

    print(f"L: {left_speed}, R: {right_speed}")
    MotorRun(0, 'forward', left_speed)
    MotorRun(1, 'forward', right_speed)
