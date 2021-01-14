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

class Button:
	def __init__(self, pin: int, control_type: PWAControl=PCA9685):
		self.control_type = control_type(pin)	

	def press(self):
		self.control_type.apply(5, 3500)
	
	def release(self):
		self.control_type.apply(0, 100)

class Thumbstick:
	def __init__(self, pin: int, control_type:PWAControl= PCA9685, offset: int=0):
		self.control = control_type(pin)
		self.offset = offset

	def center(self):
		self.control.apply(0, 510 + self.offset)

	def linear_min(self):
		self.control.apply(0, 390 + self.offset)
		pass

	def linear_max(self):
		self.control.apply(0, 600 + self.offset)

class Controller:
	def __init__(self, left_thumbstick: Thumbstick, right_thumbstick: Thumbstick, y_btn: Button):
		self.left_thumbstick = left_thumbstick
		self.right_thumbstick = right_thumbstick
		self.y_btn = y_btn

	def calibrate(self):
		# left pre
		self.left_thumbstick.center()
		time.sleep(1)
		self.left_thumbstick.linear_max()
		time.sleep(1)
		self.left_thumbstick.linear_min()
		time.sleep(1)
		self.left_thumbstick.center()
		time.sleep(1)

		# # right pre
		# self.right_thumbstick.center()
		# print('center')
		# time.sleep(1)
		# self.right_thumbstick.linear_max()
		# print('max')
		# time.sleep(1)
		# self.right_thumbstick.linear_min()
		# print('min')
		# time.sleep(1)
		# self.right_thumbstick.center()
		# print('center')
		# time.sleep(1)

		# # y button
		# self.y_btn.press()
		# time.sleep(1)
		# self.y_btn.release()
		# time.sleep(1)

if __name__ == '__main__':
	left_stick = Thumbstick(pin=13, offset=60)
	right_stick = Thumbstick(pin=12)
	y_btn = Button(pin=14)

	controller = Controller(left_thumbstick=left_stick, right_thumbstick=right_stick, y_btn=y_btn)
	controller.calibrate()
	

