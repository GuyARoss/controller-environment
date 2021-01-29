from abc import ABC

import time

class PWAControl(ABC):
	def __init__(self, pin: int):
		self.pin = pin

	def apply(self, on: int, off: int):
		pass

class PCA9685(PWAControl):
	def __init__(self, pin: int):
		self.pin = pin

		import Adafruit_PCA9685

		pwm = Adafruit_PCA9685.PCA9685()
		pwm.set_pwm_freq(60)

		self.pwm = pwm

	def apply(self, on: int, off: int):
		self.pwm.set_pwm(self.pin, on, off)

	
class Thumbstick:
	def __init__(self, pin: int, control_type:PWAControl= PCA9685):
		self.control = control_type(pin)

	def center(self):
		self.control.apply(0, 300)

	def linear_min(self):
		self.control.apply(0, 120)

	def linear_max(self):
		self.control.apply(0, 500)

class Controller:
	def __init__(self, left_thumbstick: Thumbstick, right_thumbstick: Thumbstick):
		self.left_thumbstick = left_thumbstick
		self.right_thumbstick = right_thumbstick

	def calibrate(self):
		# left pre
		self.left_thumbstick.center()
		time.sleep(1)
		self.left_thumbstick.linear_min()
		time.sleep(1)
		self.left_thumbstick.linear_max()
		time.sleep(1)
		self.left_thumbstick.center()
		time.sleep(1)

		# right pre
		self.right_thumbstick.center()
		time.sleep(1)
		self.right_thumbstick.linear_max()
		time.sleep(1)
		self.right_thumbstick.linear_min()
		time.sleep(1)
		self.right_thumbstick.center()
		time.sleep(1)