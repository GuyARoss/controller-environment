#!/usr/bin/env python3.8
import cv2
import time
import logging
import argparse

from typing import NoReturn 

from menu_prediction.menu_prediction import predict_frame, train_model
from menu_prediction.model import Model

from control.gameplay import select_action
from driver import Controller, Thumbstick
from setup import setup_cap, setup_controller
from gameplay_action import Action

logging.basicConfig(filename="log.txt", level=logging.INFO)

def main(disable_menu_detection: bool, should_train: bool) -> NoReturn:
    menu_detection_model = Model()
    menu_detection_model.load() if not should_train else menu_detection_model.train()

    cap = setup_cap()
    controller = setup_controller()

    predictions: List[str] = []

    last_gameplay_action = None

    while True:
        frame = cap.read()[1]

        frame_prediction = "gameplay" if disable_menu_detection == True else predict_frame(menu_detection_model, frame, predictions=predictions)
        
        # write frame_prediction to named pipe
        # read named pipe for last_action

        frame = cv2.putText(frame, f'predicted_menu: {frame_prediction}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, f'last_action: {str(last_gameplay_action)}', (50, 72), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        if cv2.waitKey(1) == 27:
            break

        cv2.imshow('output', frame)
        
    cv2.destroyAllWindows()

if __name__ == '__main__':    
    parser = argparse.ArgumentParser()
    parser.add_argument('--nopredict', '--nopredict', help="set to true if menu prediction should be disabled", type=bool, default=False)
    parser.add_argument('--t', '--train', help="set true if the training process should be ran", type=bool, default=False)

    args = parser.parse_args()

    main(
        disable_menu_detection=args.nopredict,
        should_train=args.train,
    )
