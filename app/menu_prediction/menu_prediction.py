#!/usr/bin/env python3.8
import cv2
from typing import NoReturn, List
from joblib import dump, load 

from menu_prediction.model import Model
from menu_prediction.utils import average_prediction

def predict_frame(in_model: any, frame: any, predictions: List[str] = []) -> str:
    current_frame_prediction = in_model.predict(frame)

    predictions.append(current_frame_prediction)
    if len(predictions) >= 20:
        predictions.pop(1)

    return average_prediction(predictions)

def train_model(train_path: str) -> Model:
    model = Model()
    model.train(train_path)

    return model
