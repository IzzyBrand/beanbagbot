import numpy as np

# [front_left, back_left, front_right, back_right]
motor_pins = np.array([22, 23, 27, 17])
motor_dirs = np.array([1, -1, -1, 1])

# convert joystick commands to PWM
pwm_mid = 1500
pwm_min = 1000
pwm_max = 2000

forward_coeff = 300
turn_coeff = 100

# how much to scale the ADC by to calculate battery voltage
adc_channel = 0
adc_offset = 0.
adc_scale = 3.

# battery voltage thresholds
batt_warn_voltage = 11.5
batt_min_voltage = 11.2

# the server stops handling command requests if it hasn't received new control
motor_command_timeout = 1

# web params
flask_port = 5000
websocket_port = 5050