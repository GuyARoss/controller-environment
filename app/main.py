#!/usr/bin/env python3.8
import cv2
import time
import asyncio

from enum import IntEnum
from typing import NoReturn 
from menu_prediction.menu_prediction import predict_frame, train_model
from control.gameplay import select_action
from driver import Controller, Thumbstick

def setup_cap() -> any:
    cap = cv2.VideoCapture(0)
    cap.set(3, 1080)
    cap.set(4,720)
    cap.set(5, 30)

    return cap

def setup_controller() -> any:
    left_thumb = Thumbstick(pin=13)
    right_thumb = Thumbstick(pin=12)

    return Controller(left_thumbstick=left_thumb, right_thumbstick=right_thumb)

class Action(IntEnum):
    NONE = 0
    GAMEPLAY = 1

async def gameplay_worker(action_queue, gameplay_queue, controller) -> NoReturn:
    last_gameplay_action = None
    action = await action_queue.get()

    while True:
        print(action)
        if action is Action.NONE:
            continue

        gameplay_action, gameplay_action_handler = select_action(last_gameplay_action)
        gameplay_action_handler(controller)
        last_gameplay_action = gameplay_action

        print('gameplay_action', gameplay_action)
        await gameplay_queue.put(gameplay_action)

async def main() -> NoReturn:
    # menu_detection_model = train_model()
    # cap = setup_cap()
    controller = setup_controller()

    predictions: List[str] = []

    gameplay_queue = asyncio.Queue()

    # @@todo: when we introuduce more action handlers to our pool
    # we will need to prob want to change this to a priority queue
    action_queue = asyncio.Queue()

    gameplay_task = asyncio.create_task(gameplay_worker(action_queue, gameplay_queue, controller))

    while True:
        frame = cap.read()[1]

        frame_prediction = predict_frame(menu_detection_model, frame, predictions=predictions, )
        if frame_prediction == "gameplay":
            action_queue.put_nowait(Action.GAMEPLAY)
        else:
            action_queue.put_nowait(Action.NONE)

        try:
            last_gameplay_action = gameplay_queue.get_nowait()
        except asyncio.QueueEmpty:
            last_gameplay_action = None

        frame = cv2.putText(frame, f'predicted_menu: {frame_prediction}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, f'last_action: {str(last_gameplay_action)}', (50, 72), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)

        if cv2.waitKey(1) == 27:
            break

        cv2.imshow('output', frame)
        
    cv2.destroyAllWindows()

    # gameplay_task.cancel()
    # await asyncio.gather(*[gameplay_task], return_exceptions=False)

if __name__ == '__main__':
    asyncio.run(main())
