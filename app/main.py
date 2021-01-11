#!/usr/bin/env python3.8
import cv2
import time
import logging

from enum import IntEnum
from typing import NoReturn 
from menu_prediction.menu_prediction import predict_frame, train_model
from control.gameplay import select_action
from driver import Controller, Thumbstick

logging.basicConfig(filename="log.txt", level=logging.INFO)

def setup_cap() -> any:
    cap = cv2.VideoCapture(0)
    cap.set(3, 720)
    cap.set(4,480)
    cap.set(5, 15)

    return cap

def setup_controller() -> any:
    left_thumb = Thumbstick(pin=13)
    right_thumb = Thumbstick(pin=12)

    return Controller(left_thumbstick=left_thumb, right_thumbstick=right_thumb)

class Action(IntEnum):
    NONE = 0
    GAMEPLAY = 1

def main() -> NoReturn:
    menu_detection_model = train_model()
    cap = setup_cap()
    controller = setup_controller()

    predictions: List[str] = []

    last_gameplay_action = None

    while True:
        frame = cap.read()[1]

        frame_prediction = predict_frame(menu_detection_model, frame, predictions=predictions, )

        if frame_prediction == "gameplay":
            gameplay_action, gameplay_action_handler = select_action(last_gameplay_action)
            if gameplay_action_handler is not None:
                # @@performance: this runs horrible and is blocking
                print(gameplay_action_handler)
                gameplay_action_handler(controller)

            last_gameplay_action = gameplay_action
        else:
            last_gameplay_action = None

        frame = cv2.putText(frame, f'predicted_menu: {frame_prediction}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, f'last_action: {str(last_gameplay_action)}', (50, 72), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        if cv2.waitKey(1) == 27:
            break

        cv2.imshow('output', frame)
        
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
