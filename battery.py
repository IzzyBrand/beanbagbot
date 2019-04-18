import Adafruit_ADS1x15
import numpy
import params as p

class Battery:
	def __init__(self):
		self.adc = Adafruit_ADS1x15.ADS1115()
		self.GAIN = 1

	def read(self):
		raw = self.adc.read_adc(p.adc_channel, self.GAIN)
		# this is a 16 bit adc, so we normalize by dividing by 2^16
		return float(raw)/(2**16) * p.adc_scale + p.adc_offset