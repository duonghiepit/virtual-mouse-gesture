import cv2
import mediapipe as mp

class HandTracker:
    def __init__(self, mode=False, max_hands=1, detection_confidence=0.7, tracking_confidence=0.7):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            static_image_mode=mode,
            model_complexity=1,
            min_detection_confidence=detection_confidence,
            min_tracking_confidence=tracking_confidence,
            max_num_hands=max_hands
        )
        self.draw = mp.solutions.drawing_utils

    def find_hand_landmarks(self, frame):
        """Process frame and return hand landmarks."""
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        processed = self.hands.process(frameRGB)
        
        landmarks_list = []
        if processed.multi_hand_landmarks:
            hand_landmarks = processed.multi_hand_landmarks[0]
            self.draw.draw_landmarks(frame, hand_landmarks, self.mpHands.HAND_CONNECTIONS)
            
            for lm in hand_landmarks.landmark:
                landmarks_list.append((lm.x, lm.y))
        
        return processed, landmarks_list
    
    def get_index_finger_tip(self, processed):
        """Extract index finger tip from landmarks."""
        if processed.multi_hand_landmarks:
            hand_landmarks = processed.multi_hand_landmarks[0]
            return hand_landmarks.landmark[self.mpHands.HandLandmark.INDEX_FINGER_TIP]
        return None