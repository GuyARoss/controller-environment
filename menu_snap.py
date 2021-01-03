#!/usr/bin/env python3.8
import cv2

from datetime import datetime

date = datetime.now().strftime("%y-%m-%d")

def main():
    cam = cv2.VideoCapture(0)
    cam.set(3, 1080)     
    cam.set(4,720)     
    cam.set(5, 30)      

    while True:
        ret_val, img = cam.read()

        cv2.imshow('output', img)
        
        if cv2.waitKey(1) == 27: 
            break

        if cv2.waitKey(1) == ord('p'):
            cv2.imwrite(f"./menus/snap_{date}.png", img)


    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()