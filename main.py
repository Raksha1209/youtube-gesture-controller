import cv2
import mediapipe as mp
import pyautogui
import time
import pyttsx3
from gestures import detect_gesture
from utils import draw_landmarks, get_finger_states
from config import COOLDOWN_TIME

# Initialize modules
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)

# Voice Engine
engine = pyttsx3.init()

# Variables
last_gesture_time = 0
SMOOTHING_TIME = 0.5
last_detected_gesture = None
gesture_start_time = 0

def speak(text):
    engine.say(text)
    engine.runAndWait()

def main():
    global last_gesture_time, last_detected_gesture, gesture_start_time

    while True:
        success, img = cap.read()
        if not success:
            continue

        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        gesture = None
        action = None

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                draw_landmarks(img, hand_landmarks)

                landmarks = [lm for lm in hand_landmarks.landmark]
                finger_states = get_finger_states(landmarks)

                current_time = time.time()

                # Static Gesture Detection
                gesture, action = detect_gesture(finger_states)

                if gesture:
                    if gesture != last_detected_gesture:
                        last_detected_gesture = gesture
                        gesture_start_time = current_time
                    else:
                        hold_time = current_time - gesture_start_time
                        if hold_time > SMOOTHING_TIME:
                            if current_time - last_gesture_time >= COOLDOWN_TIME:
                                if action:
                                    pyautogui.press(action)
                                speak(gesture)
                                last_gesture_time = current_time
                                cv2.putText(img, f"{gesture} - Confirmed", (10, 150), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 255, 255), 3)

        cv2.imshow("YouTube Gesture Controller", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
