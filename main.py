import cv2
from hand_tracking import HandTracker
from gesture_controller import GestureController

def main():
    cap = cv2.VideoCapture(0)
    hand_tracker = HandTracker()
    gesture_controller = GestureController()

    try:
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame = cv2.flip(frame, 1)
            processed, landmarks_list = hand_tracker.find_hand_landmarks(frame)

            if processed.multi_hand_landmarks:
                gesture_controller.detect_gestures(frame, landmarks_list, processed)

            cv2.imshow('Virtual Mouse', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    finally:
        cap.release()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()