import numpy as np

# [front_left, back_left, front_right, back_right]
motor_pins = np.array([9, 10, 11, 12])
motor_dirs = np.array([1, 1, 1, 1])

pwm_midpoint = 1500
pwm_range = 300
