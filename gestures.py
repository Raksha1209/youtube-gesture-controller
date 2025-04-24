def detect_gesture(fingers):
    # fingers: [index, middle, ring, pinky] - True if finger is up
    if fingers == [True, True, True, True]:
        return "Play", 'k'
    elif fingers == [False, False, False, False]:
        return "Pause", 'k'
    elif fingers == [True, True, False, False]:
        return "Volume Up", 'volumeup'
    elif fingers == [False, False, True, True]:
        return "Volume Down", 'volumedown'
    elif fingers == [True, True, True, False]:
        return "Previous", 'j'
    elif fingers == [False, False, False, True]:
        return "Next", 'l'
    else:
        return None, None

