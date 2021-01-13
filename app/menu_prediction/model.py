#!/usr/bin/env python3.8
import os
import glob
import cv2
import mahotas as mt
from joblib import dump, load

from typing import Callable, List, NoReturn
from sklearn.svm import LinearSVC

def normalize_image(image: any) -> any:
    grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    crop = grayscale[150:, 0:]
      
    return grayscale

def haralick_features(image) -> any:
    hara = mt.features.haralick(image)
    
    return hara.mean(axis=0)

class Model:
    normal_img_fn: Callable[[any], any]
    extract_features_fn: Callable[[any], any]
    svc: any
    file_path: str

    def __init__(
        self,
        normal_img_fn: Callable[[any], any] = normalize_image,
        extract_features_fn: Callable[[any], any] = haralick_features,
        file_path: str = "./menu-prediction.joblib"
    ) -> NoReturn:
        self.normal_img_fn = normal_img_fn
        self.extract_features_fn = extract_features_fn
        self.file_pth = file_path

    def save(self):
        dump(self.svc, self.file_path)

    def load(self):
        self.svc = load(self.file_path)

    def train(self, train_path: str, should_save: bool = True) -> NoReturn:
        assert train_path != None, "train path should not be empty"

        cates = os.listdir(train_path)
        
        feats = []
        lbls = []

        for cate in cates:
            for file in glob.glob(f"{train_path}/{cate}/*.png"):                
                img = cv2.imread(file)
                img = self.normal_img_fn(img)
                
                feat = self.extract_features_fn(img)
                
                feats.append(feat)
                lbls.append(cate)

        self.svc = LinearSVC(random_state=5, dual=False)
        self.svc.fit(feats, lbls)
        
        if should_save:
            self.save()

    def predict(self, img: any) -> str:
        normal_img = self.normal_img_fn(img)
        img_features = self.extract_features_fn(normal_img)

        return self.svc.predict(img_features.reshape(1, -1))[0]
