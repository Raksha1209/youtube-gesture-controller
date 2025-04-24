import cv2
import mediapipe as mp

def draw_landmarks(img, hand_landmarks):
    mp.solutions.drawing_utils.draw_landmarks(
        img, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

def get_finger_states(landmarks):
    states = []
    if not landmarks or len(landmarks) < 21:
        return [False, False, False, False]
    # Index to Pinky tips: 8, 12, 16, 20. Check if tip is above PIP joint
    for tip_id in [8, 12, 16, 20]:
        states.append(landmarks[tip_id].y < landmarks[tip_id - 2].y)
    return states

