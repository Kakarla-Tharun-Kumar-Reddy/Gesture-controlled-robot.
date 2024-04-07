'''import bluetooth
import time

def connect_to_device(device_name, pin):
    nearby_devices = bluetooth.discover_devices()
    for addr in nearby_devices:
        if device_name == bluetooth.lookup_name(addr):
            print(f"Found device: {device_name} with address {addr}")
            try:
                port = 1
                sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
                sock.connect((addr, port))
                print("Pairing...")
                sock.settimeout(10)
                sock.send(pin)
                print("Connected successfully!")
                return sock
            except Exception as e:
                print(f"Error connecting: {e}")
    print(f"Device {device_name} not found")
    return None

def main():
    device_name = "HC-05"  # Replace with your device's name
    pin = "1234"
    sock = connect_to_device(device_name, pin)
    if sock:
        try:
            while True:
                message = "hello frnd"
                print("Sending:", message)
                sock.send(message.encode())  # Send the message as bytes
                time.sleep(1)  # Wait for 1 second before sending the next message
        except KeyboardInterrupt:
            print("Closing connection...")
            sock.close()

if __name__ == "__main__":
    main()

------
import bluetooth

def print_available_devices():
    nearby_devices = bluetooth.discover_devices()
    if nearby_devices:
        print("Available Bluetooth devices:")
        for addr in nearby_devices:
            device_name = bluetooth.lookup_name(addr)
            print(f"  - {device_name} ({addr})")
    else:
        print("No Bluetooth devices found.")

def main():
    print_available_devices()

if __name__ == "__main__":
    main()

------
import bluetooth

def connect_to_hc05(address, name, pin):
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((address, 1))
        print("Pairing...")
        sock.settimeout(10)
        sock.send(pin)
        print("Connected successfully to HC-05!")
        return sock
    except Exception as e:
        print(f"Error connecting to HC-05: {e}")
        return None

def main():
    address = "00:00:13:10:4C:B0"  # Replace with the address of your HC-05 module
    name = "HC-05"  # Replace with the name of your HC-05 module
    pin = "1234"  # Replace with the PIN of your HC-05 module
    sock = connect_to_hc05(address, name, pin)
    if sock:
        try:
            while True:
                data = sock.recv(1024)
                print("Received:", data)
        except KeyboardInterrupt:
            print("Closing connection...")
            sock.close()

if __name__ == "__main__":
    main()

------
import bluetooth

def connect_to_hc05(address, name, pin):
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((address, 1))
        print("Pairing...")
        sock.settimeout(10)
        sock.send(pin)
        print("Connected successfully to HC-05!")
        return sock
    except Exception as e:
        print(f"Error connecting to HC-05: {e}")
        return None

def main():
    address = "00:00:13:10:4C:B0"  # Replace with the address of your HC-05 module
    name = "HC-05"  # Replace with the name of your HC-05 module
    pin = "1234"  # Replace with the PIN of your HC-05 module
    sock = connect_to_hc05(address, name, pin)
    if sock:
        try:
            message = "hello"
            print("Sending:", message)
            sock.send(message.encode())  # Send the message as bytes
            print("Message sent successfully!")
        except Exception as e:
            print(f"Error sending message: {e}")
        finally:
            print("Closing connection...")
            sock.close()

if __name__ == "__main__":
    main()
-----
import bluetooth
import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

def connect_to_hc05(address, name, pin):
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((address, 1))
        print("Pairing...")
        sock.settimeout(10)
        sock.send(pin)
        print("Connected successfully to HC-05!")
        return sock
    except Exception as e:
        print(f"Error connecting to HC-05: {e}")
        return None

def main():
    address = "00:00:13:10:4C:B0"  # Replace with the address of your HC-05 module
    name = "HC-05"  # Replace with the name of your HC-05 module
    pin = "1234"  # Replace with the PIN of your HC-05 module
    sock = connect_to_hc05(address, name, pin)
    if not sock:
        return

    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands=1, detectionCon=0.8)
    keyboard = Controller()

    while True:
        success, img = cap.read()
        hands, img = detector.findHands(img)

        if hands:
            hand = hands[0]
            fingers = detector.fingersUp(hand)

            # Check the hand gesture
            if fingers[0] == 1:  # Thumb open
                message = 1
            elif fingers[1] == 1 and fingers[0] == 1:  # Index and Thumb open
                message = 2
            elif fingers[1] == 1 and fingers[0] == 1 and fingers[2] == 1:  # Thumb, Index, and Middle open
                message = 3
            elif fingers[1] == 1 and fingers[0] == 1 and fingers[2] == 1 and fingers[3] == 1 :
            	message = 4
            elif fingers[1] == 1 and fingers[0] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1 :
            	message = 5
            else:  # Other gestures (not handled in this example)
                #message = "0"  # You can customize this based on your specific requirements
                pass

            # Send the message via Bluetooth
            try:
                sock.send(message.encode())  # Send the message as bytes
                print("Message sent successfully:", message)
            except Exception as e:
                print(f"Error sending message: {e}")

        cv2.imshow("Hand Tracking", img)
        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
'''

import bluetooth
import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller

def connect_to_hc05(address, name, pin):
    try:
        sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        sock.connect((address, 1))
        print("Pairing...")
        sock.settimeout(10)
        sock.send(pin)
        print("Connected successfully to HC-05!")
        return sock
    except Exception as e:
        print(f"Error connecting to HC-05: {e}")
        return None

def main():
    address = "00:00:13:10:4E:73"  # Replace with the address of your HC-05 module
    name = "HC-05"  # Replace with the name of your HC-05 module
    pin = "1234"  # Replace with the PIN of your HC-05 module
    sock = connect_to_hc05(address, name, pin)
    if not sock:
        return

    cap = cv2.VideoCapture(0)
    detector = HandDetector(maxHands=1, detectionCon=0.8)
    keyboard = Controller()
    bmsg=0

    while True:
        success, img = cap.read()
        hands, img = detector.findHands(img)

        if hands:
            hand = hands[0]
            fingers = detector.fingersUp(hand)
            

            # Check the hand gesture
            if fingers[1] == 1 and fingers[0] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
                message = 5
                print(message)
                cv2.putText(img, "STOP", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            elif fingers[1] == 1 and fingers[0] == 1 and fingers[2] == 1 and fingers[3] == 1:
                message = 4
                print(message)
                cv2.putText(img, "LEFT", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            elif fingers[1] == 1 and fingers[0] == 1 and fingers[2] == 1:
                message = 3
                print(message)
                cv2.putText(img, "RIGHT", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            elif fingers[1] == 1 and fingers[0] == 1:
                message = 2
                print(message)
                cv2.putText(img, "BACK", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            elif fingers[0] == 1:
                message = 1
                print(message)
                cv2.putText(img, "FRONT", (10, 110), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            else:
                #message = 0
                print("no open")
                
            # Send the message via Bluetooth
            try:
                if (bmsg != message):
                	sock.send(str(message).encode())  # Convert message to string and send as bytes
                	bmsg = message
                
                print("Message sent successfully:", message)
            except Exception as e:
                print(f"Error sending message: {e}")

        cv2.imshow("Hand Tracking", img)
        if cv2.waitKey(1) & 0xFF == 27:  # Press 'Esc' to exit
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

