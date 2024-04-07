# Gesture-controlled-robot.# CVControlRobot


This project enables controlling an Arduino-based device using hand gestures captured through a camera feed and transmitted via Bluetooth from a Python script.

## Overview 📝

The system consists of two main components:

1. **Python Script**: The Python script captures video from a camera, detects hand gestures using computer vision techniques, and sends corresponding commands over Bluetooth to the Arduino.

2. **Arduino Code**: The Arduino code receives commands via Bluetooth from the Python script and controls motors or servos based on the received commands.

## Requirements 🛠️

- Python 3.x
- OpenCV
- cvzone (for HandTrackingModule)
- pynput
- Arduino IDE
- HC-05 Bluetooth module
- Arduino-compatible board (e.g., Arduino Uno)
- Motors or servos for movement control

## Setup ⚙️

1. Connect the HC-05 Bluetooth module to the Arduino board.
2. Upload the provided Arduino code to your Arduino board.
3. Make sure the HC-05 module is paired with your computer.
4. Install the required Python libraries using pip: `pip install opencv-python cvzone pynput`.
5. Run the Python script on your computer. Make sure to modify the script to use the correct Bluetooth address of your HC-05 module.
6. Use hand gestures as specified in the Python script to control the Arduino device.

## Usage 🚀

- Run the Python script (`hand_gesture_control.py`) on your computer.
- Make appropriate hand gestures in front of the camera to control the Arduino device.
- Refer to the Arduino code (`bluetoothCar.ino`) for pin mappings and motor control logic.
- Press 'Esc' to exit the Python script.

## Contributing 🤝

Contributions are welcome! Feel free to submit issues, feature requests, or pull requests.

## License 📄

This project is licensed under the [MIT License](LICENSE).
## GitHub Repository 🌐

Find the project on [GitHub](https://github.com/GovardhanaRekam/CVControlRobot).
