import pigpio
import numpy as np
import params as p
import sys
import os

class Motors:
	def __init__(self):
		# launch the pigpio daemon
		os.system('sudo pigpiod')

		# connect to the daemon
		self.pi = pigpio.pi()
		if not self.pi.connected:
			print('Failed to connect to pigpio daemon.')
			sys.exit(1)

		# a mixing matrix to map from drive instructions to motor speed
		self.mix = np.array([[1,  1],
							 [1,  1],
							 [1, -1],
							 [1, -1]])

	def set(self, forward, turn):
		# calculate the pwm for each motor
		cmd = np.array([forward, turn], dtype=float)
		motor_speeds = (self.mix @ cmd) * p.motor_dirs
		motor_pwms = (motor_speeds * p.pwm_range + p.pwm_midpoint).astype(int)

		# set the motors accordingly
		for pin, pwm in zip(p.motor_pins, motor_pwms):
			self.pi.set_servo_pulsewidth(pin, pwm)

	def stop(self):
		for pin in p.motor_pins:
			self.pi.set_servo_pulsewidth(pin, p.pwm_midpoint)

		self.pi.stop()
