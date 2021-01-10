from __future__ import division
import time

import Adafruit_PCA9685 

pwm = Adafruit_PCA9685.PCA9685()

pwm.set_pwm_freq(60)

class Thumbstick:
	def __init__(self, pin: int):
		self.pin = pin



if __main__ == '__main__':
	while True:
		print('doing spin')
		pwm.set_pwm(12, 0, 120)
		time.sleep(1)
		pwm.set_pwm(12, 0, 500)
		time.sleep(1)
