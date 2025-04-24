# YouTube Gesture Controller

Control YouTube playback using hand gestures detected from webcam in real-time.

## Features

- Open Palm → Play
- Fist → Pause
- Index + Middle → Volume Up
- Ring + Pinky → Volume Down
- All Except Pinky → Previous Video
- Pinky Only → Next Video

## Tech Stack

- Python
- OpenCV
- MediaPipe
- PyAutoGUI

## How to Run

1. Clone the repo and navigate into it
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # or venv\Scripts\activate (Windows)
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the project:
   ```bash
   python main.py
   ```

## Next Steps

- Add swipe gesture recognition
- Custom gesture training module

main.py
Handles:

webcam input (OpenCV)

hand tracking (MediaPipe)

overlays (cv2.putText)

gesture detection calls

gestures.py
Handles:

detection of gesture based on hand landmark positions

returns which action to perform (play, pause, etc.)

utils.py
Handles:

checking finger states

implementing cooldown timers

config.py
Holds:

gesture cooldown settings

screen resolution constants, key mappings

requirements.txt
