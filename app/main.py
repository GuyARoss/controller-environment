import cv2

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

def main() -> NoReturn:
    menu_detection_model = train_model()
    cap = setup_cap()
    controller =setup_controller()

    predictions: List[str] = []
    last_gameplay_action = None

    while True:
        frame = cap.read()[1]

        frame_prediction = predict_frame(menu_detection_model, frame, predictions=predictions)
        if frame_prediction == "gameplay":
            gameplay_action, gameplay_action_handler = select_action(last_gameplay_action)
            last_gameplay_action = gameplay_action

            # gameplay_action_handler(controller)
        else:
            last_gameplay_action = None

        frame = cv2.putText(frame, f'predicted_menu: {frame_prediction}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
        frame = cv2.putText(frame, f'last_action: {str(last_gameplay_action)}', (50, 55), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

        if cv2.waitKey(1) == 27:
            break

        cv2.imshow('output', frame)
        
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
