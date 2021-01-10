#!/usr/bin/env python3.8
import cv2
from typing import NoReturn, List

from menu_prediction.model import Model
from menu_prediction.utils import average_prediction

def predict_frame(in_model: any, frame: any, predictions: List[str] = []) -> str:
    current_frame_prediction = in_model.predict(frame)

    predictions.append(current_frame_prediction)
    if len(predictions) >= 20:
        predictions.pop(1)

    return average_prediction(predictions)

def train_model() -> Model:
    model = Model()
    model.train('../menu_dataset/training')

    return model

def main() -> NoReturn:
    model = train_model()
    print("training complete")

    cap = cv2.VideoCapture(0)
    cap.set(3, 1080)
    cap.set(4,720)
    cap.set(5, 30)

    predictions: List[str] = []

    while True:
        ret_val, frame = cap.read()
        
        frame_prediction = predict_frame(model, frame, predictions=predictions)
        frame = cv2.putText(frame, frame_prediction, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        if cv2.waitKey(1) == 27:
            break

        cv2.imshow('output', frame)
        
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
