#!/usr/bin/env python3.8
import cv2
import time
import logging
import argparse

from typing import NoReturn 

from menu_prediction.menu_prediction import predict_frame, train_model
from menu_prediction.model import Model
from setup import setup_cap

from gameplay_action import Action

logging.basicConfig(filename="log.txt", level=logging.INFO)

def main(no_loop: bool) -> NoReturn:
    cap = setup_cap()

    while not no_loop:
        frame = cap.read()[1]
        # @@ save frame

        # @@ todo: read agent ipc context for data to display
        # frame = cv2.putText(frame, f'', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        if cv2.waitKey(1) == 27:
            break

        cv2.imshow('output', frame)
        
    cv2.destroyAllWindows()

if __name__ == '__main__':    
    parser = argparse.ArgumentParser()
    parser.add_argument('--noloop', '--noloop', help="set true if the main process loop should not be ran", type=bool, default=False)

    args = parser.parse_args()

    main(
        no_loop=args.noloop,
    )
