#!/usr/bin/env python3.8
import cv2
import time

def main():
    cap = cv2.VideoCapture(0)
    cap.set(3, 1080)
    cap.set(4,720)
    cap.set(5, 30)

    while True:
        ret_val, img = cap.read()

        cv2.imshow('output', img)
        
        if cv2.waitKey(1) == 27: 
            break

        if cv2.waitKey(1) == ord('p'):
            cv2.imwrite(f"./snaps/snap_{time.time()}.png", img)


    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()