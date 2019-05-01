
import numpy as np
import params as p
import os
import time
import sys

# We wrap the whole motors class in a try/except to handle the case
# when this script is being run on a computer without pigpio for testing
try:
	import pigpio

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
			# scale the commands by the coefficients specified in params
			cmd = np.array([forward * p.forward_coeff, turn * p.turn_coeff], dtype=float)
			# apply the mixing matrix to go from command to motor speeds
			motor_speeds = (self.mix @ cmd) * p.motor_dirs
			# add the pwm midpoint and restrict to the pwm range
			motor_pwms = np.clip(motor_speeds + p.pwm_mid, p.pwm_min, p.pwm_max).astype(int)

			print(motor_pwms)

			# set the motors accordingly
			for pin, pwm in zip(p.motor_pins, motor_pwms):
				self.pi.set_servo_pulsewidth(pin, pwm)

		def stop(self):
			for pin in p.motor_pins:
				self.pi.set_servo_pulsewidth(pin, p.pwm_mid)

			self.pi.stop()

except ImportError:
	print('pigpio library not found. Substituting blank motors class.')
	
	class Motors:
		def set(self, forward, turn):
			print('Forward: {}\tTurn: {}'.format(forward, turn))

		def stop(self):
			pass

if __name__ == '__main__':
	m = Motors()
	m.set(0,0)

	if len(sys.argv) > 1 and sys.argv[1] == 'test':
		for pin in p.motor_pins:
			m.pi.set_servo_pulsewidth(pin, 1600)
			time.sleep(2)
			m.pi.set_servo_pulsewidth(pin, 1500)