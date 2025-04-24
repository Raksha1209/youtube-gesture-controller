import cv2
import mediapipe as mp
import pyautogui
import time
from gestures import detect_gesture
from utils import draw_landmarks, get_finger_states
from config import COOLDOWN_TIME

# Initialize modules
cap = cv2.VideoCapture(0)
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=1, min_detection_confidence=0.7)

last_gesture_time = 0

def main():
    global last_gesture_time
    while True:
        success, img = cap.read()
        if not success:
            continue

        img = cv2.flip(img, 1)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                draw_landmarks(img, hand_landmarks)

                landmarks = [lm for lm in hand_landmarks.landmark]
                finger_states = get_finger_states(landmarks)

                current_time = time.time()
                if current_time - last_gesture_time >= COOLDOWN_TIME:
                    gesture, action = detect_gesture(finger_states)
                    if gesture:
                        if action in ['volumeup', 'volumedown']:
                            pyautogui.press(action)
                        else:
                            pyautogui.press(action)
                        last_gesture_time = current_time
                        cv2.putText(img, gesture, (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255, 0, 0), 3)

        cv2.imshow("YouTube Gesture Controller", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
