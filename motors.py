import pigpio
import numpy as np
import params as p
import os
import time
import subprocess

class Motors:
	def __init__(self):
		# launch the pigpio daemon
		os.system('sudo pigpiod')

		# keep trying to connect to the daemon
		self.pi = pigpio.pi()
		while not self.pi.connected:
			time.sleep(0.001)
			self.pi = pigpio.pi()

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

		print(motor_pwms)
		# set the motors accordingly
		for pin, pwm in zip(p.motor_pins, motor_pwms):
			self.pi.set_servo_pulsewidth(pin, pwm)

	def stop(self):
		for pin in p.motor_pins:
			self.pi.set_servo_pulsewidth(pin, p.pwm_midpoint)

		self.pi.stop()
