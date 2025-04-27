import cv2
import mediapipe as mp

# draws the bones and joints of the detected hand on the image
def draw_landmarks(img, hand_landmarks):
    mp.solutions.drawing_utils.draw_landmarks(
        img, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)

# every hand has 21 landmarks -- this func checks if hand has all 21
def get_finger_states(landmarks):
    states = []
    if not landmarks or len(landmarks) < 21:
        return [False, False, False, False, False]  # 5 fingers

    # Thumb
    if landmarks[4].x < landmarks[3].x:  
        # Thumb tip is to the left of thumb joint (for right hand) → thumb open
        states.append(True)
    else:
        states.append(False)

    # Fingers: Index, Middle, Ring, Pinky
    for tip_id in [8, 12, 16, 20]:
        states.append(landmarks[tip_id].y < landmarks[tip_id - 2].y)
        # If tip's Y is LESS than joint's Y → finger is UP

    return states

# 

# ONE LINER:
# Checks if each finger (thumb, index, middle, ring, pinky) is open or closed based on positions!
