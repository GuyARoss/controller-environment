#!/usr/bin/env python3.8
import cv2
from typing import NoReturn

from model import Model

def main() -> NoReturn:
    model = Model()
    model.train('../menu_dataset/training')
    print("training complete")

    cap = cv2.VideoCapture(0)
    cap.set(3, 1080)
    cap.set(4,720)
    cap.set(5, 30)

    while True:
        ret_val, frame = cap.read()
        
        frame_model_prediction = model.predict(frame)
        frame = cv2.putText(frame, frame_model_prediction, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        
        if cv2.waitKey(1) == 27:
            break

        cv2.imshow('output', frame)
        
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
