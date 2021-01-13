from control.controller import Thumbstick, Controller

if __name__ == '__main__':
	left_stick = Thumbstick(pin=13)
	right_stick = Thumbstick(pin=12)

	controller = Controller(left_thumbstick=left_stick, right_thumbstick=right_stick)
	controller.calibrate()
	
	# @@ todo: read from frame_detection ipc, determine action.