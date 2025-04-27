#input: list showing if each finger is up (True) or down (False).


def detect_gesture(finger_states):
    """
    Given the states of fingers, returns (gesture_name, action_key_for_pyautogui)
    """
    thumb, index, middle, ring, pinky = finger_states

    # ✋ Open Palm (All fingers up)
    if thumb and index and middle and ring and pinky:
        return ("Play", "k")  # Play
    # ✊ Fist (All fingers down)
    if not thumb and not index and not middle and not ring and not pinky:
        return ("Pause", "k")  # Pause
    # ✌️ Two fingers up
    if not thumb and index and middle and not ring and not pinky:
        return ("Volume Up", "up")
    # 🤞 Ring and pinky fingers up
    if not thumb and not index and not middle and ring and pinky:
        return ("Volume Down", "down")
    # 🤟 Only pinky up
    if not thumb and not index and not middle and not ring and pinky:
        return ("Next", "l")
    # 🤘 All except pinky
    if thumb and index and middle and ring and not pinky:
        return ("Previous", "j")
    # 👍 Thumbs Up
    if thumb and not index and not middle and not ring and not pinky:
        return ("Thumbs Up", None)  # No action, just say

    return (None, None)
