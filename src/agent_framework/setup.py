import cv2
from driver import Controller, Thumbstick

def setup_cap() -> any:
    cap = cv2.VideoCapture(0)
    cap.set(3, 720)
    cap.set(4,480)
    cap.set(5, 30)

    return cap

def setup_controller() -> any:
    left_thumb = Thumbstick(pin=13)
    right_thumb = Thumbstick(pin=12)

    return Controller(left_thumbstick=left_thumb, right_thumbstick=right_thumb)
