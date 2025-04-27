# YouTube Gesture Controller

Control YouTube playback using hand gestures detected from webcam in real-time.

## Features

👋 Play / Pause by showing Open Palm or Fist.

👉✌️ Volume Control with two-finger gestures.

🤚🖐️ Skip Forward 10s with Pinky Only gesture.

✋🤏 Go Back 10s with All Fingers Except Pinky gesture.

🔊 Voice Feedback: System speaks recognized gestures.

🚀 Real-time performance with gesture smoothing and cooldown handling.

## Tech Stack

- Python
- OpenCV
- MediaPipe
- PyAutoGUI
- pyttsx3 (for text-to-speech)

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
