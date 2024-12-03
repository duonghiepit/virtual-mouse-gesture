import cv2
import pyautogui
import random
from pynput.mouse import Button, Controller
from utils import get_angle, get_distance

class GestureController:
    def __init__(self):
        self.mouse = Controller()
        self.screen_width, self.screen_height = pyautogui.size()

    def move_mouse(self, index_finger_tip):
        """Move mouse cursor based on finger tip position."""
        if index_finger_tip:
            x = int(index_finger_tip.x * self.screen_width)
            y = int(index_finger_tip.y * self.screen_height)
            pyautogui.moveTo(x, y)

    def detect_gestures(self, frame, landmarks_list, processed):
        """Detect and perform mouse gestures."""
        if len(landmarks_list) >= 21:
            index_finger_tip = processed.multi_hand_landmarks[0].landmark[8]
            thumb_index_dist = get_distance([landmarks_list[4], landmarks_list[5]])

            # Mouse movement
            if thumb_index_dist < 50 and get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) > 90:
                self.move_mouse(index_finger_tip)

            # Left Click
            elif self._is_left_click(landmarks_list, thumb_index_dist):
                self.mouse.press(Button.left)
                self.mouse.release(Button.left)
                cv2.putText(frame, "Left Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

            # Right Click
            elif self._is_right_click(landmarks_list, thumb_index_dist):
                self.mouse.press(Button.right)
                self.mouse.release(Button.right)
                cv2.putText(frame, "Right Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

            # Double Click
            elif self._is_double_click(landmarks_list, thumb_index_dist):
                pyautogui.doubleClick()
                cv2.putText(frame, "Double Click", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

            # Screenshot
            elif self._is_screenshot(landmarks_list, thumb_index_dist):
                img = pyautogui.screenshot()
                label = random.randint(1, 1000)
                img.save(f'screenshots/screenshot_{label}.png')
                cv2.putText(frame, "Screenshot", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

    def _is_left_click(self, landmarks_list, thumb_index_dist):
        return (get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) < 50 and 
                get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) > 90 and
                thumb_index_dist > 50)

    def _is_right_click(self, landmarks_list, thumb_index_dist):
        return (get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) > 90 and 
                get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) < 50 and
                thumb_index_dist > 50)

    def _is_double_click(self, landmarks_list, thumb_index_dist):
        return (get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) < 50 and 
                get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) < 50 and
                thumb_index_dist > 50)

    def _is_screenshot(self, landmarks_list, thumb_index_dist):
        return (get_angle(landmarks_list[5], landmarks_list[6], landmarks_list[8]) < 50 and 
                get_angle(landmarks_list[9], landmarks_list[10], landmarks_list[12]) < 50 and
                thumb_index_dist < 50)