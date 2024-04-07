/*
const int irSensorPin = 2; // Pin connected to the digital IR sensor

void setup() {
  Serial.begin(9600); // Initialize serial communication
  pinMode(irSensorPin, INPUT); // Set IR sensor pin as input
}

void loop() {
  int sensorValue = digitalRead(irSensorPin); // Read digital value from IR sensor
  if (sensorValue == HIGH) {
    Serial.println("black"); // Print message if object is detected
  } else {
    Serial.println("white"); // Print message if no object is detected
  }
  delay(500); // Delay for 500 milliseconds
}

// Define the pin connected to the switch
// Define the pin connected to the switch
const int switchPin = 2;

void setup() {
  // Initialize serial communication
  Serial.begin(9600);
  
  // Set the switch pin as input
  pinMode(switchPin, INPUT);
}

void loop() {
  // Read the state of the switch
  int switchState = digitalRead(switchPin);

  // Print the state of the switch
  Serial.print("Switch state: ");
  Serial.println(switchState);

  // Add a short delay to avoid reading the switch too quickly
  delay(100);
}
*/
// Define the pin connected to the switch
#define bluetooth Serial 
const int switchPin = 2;
const int leftSensorPin = 7; // Left IR sensor pin
const int rightSensorPin = 8; // Right IR sensor pin
const int leftMotorForwardPin = 3; // Left motor forward pin
const int leftMotorBackwardPin = 4; // Left motor backward pin
const int rightMotorForwardPin = 5; // Right motor forward pin
const int rightMotorBackwardPin = 6; // Right motor backward pin
int switchState;
bool switchOn = false; // Variable to track switch state

void setup() {
  // Initialize motor pins
 bluetooth.begin(9600);  
  pinMode(leftMotorForwardPin, OUTPUT);
  pinMode(leftMotorBackwardPin, OUTPUT);
  pinMode(rightMotorForwardPin, OUTPUT);
  pinMode(rightMotorBackwardPin, OUTPUT);

  // Initialize sensor pins
  pinMode(leftSensorPin, INPUT);
  pinMode(rightSensorPin, INPUT);

  // Set the switch pin as input
  pinMode(switchPin, INPUT);
switchState = digitalRead(switchPin);
  // Begin serial communication
  Serial.begin(9600);
  if (switchState == HIGH) {
    switchOn = true; // Set switch status to ON
    Serial.println("Switch turned ON. Starting line follower robot...");
  }

}

void loop() {
  // Read the state of the switch
  

  // If switch is in HIGH state and the robot is not already started
  

  // If switch is in LOW state and the robot is started
 /* if (switchState == LOW && switchOn) {
    switchOn = false; // Set switch status to OFF
    stopMoving(); // Stop the robot
    Serial.println("Switch turned OFF. Stopping line follower robot.");
  }*/

  // If the switch is ON, execute line following logic
 /* if (switchOn) {
    // Read sensor values
    int leftSensorValue = digitalRead(leftSensorPin);
    int rightSensorValue = digitalRead(rightSensorPin);

    // Debugging: print sensor values
    Serial.print("Left Sensor: ");
    Serial.print(leftSensorValue);
    Serial.print(" - Right Sensor: ");
    Serial.println(rightSensorValue);

    // Your existing line-following logic here...

    // Example:
    // If both sensors detect the line, move forward
  if (leftSensorValue == LOW && rightSensorValue == LOW) {
      moveForward();
    }
    //If left sensor detects the line, turn right
    else if (leftSensorValue == LOW && rightSensorValue == HIGH) {
     turnRight();
     }
     // If right sensor detects the line, turn left
   else if (leftSensorValue == HIGH && rightSensorValue == LOW) {
      turnLeft();
   }
    // // If both sensors don't detect the line, stop
    else {
      stopMoving();
   }
  delay(100);
  }
*/

if (bluetooth.available()) { // Check if data is available from Bluetooth module
Serial.print("inloop");
    char command = bluetooth.read(); // Read the incoming byte
Serial.print(command);
    // Execute corresponding action based on the received command
    switch (command) {
      case '1': // Forward
        moveForward();
       
        break;
      case '2': // Backward
        moveBackward();
        
        break;
      case '3': // Right
        turnLeft();     
                 
        
        break;
      case '4': // Left
        turnRight();
        
        break;
      case '5': // Stop
        stopMoving();
        
        break;
      default:
        // Invalid command
        Serial.println("Invalid command received.");
    }
  }
 // Add a small delay for stability
}

// Function to move the robot forward
void moveForward() {
  digitalWrite(leftMotorForwardPin, LOW);
  digitalWrite(leftMotorBackwardPin, HIGH);
  digitalWrite(rightMotorForwardPin, LOW);
  digitalWrite(rightMotorBackwardPin, HIGH);
 
}

// Function to turn the robot left
void turnLeft() {
  digitalWrite(leftMotorForwardPin, LOW);
  digitalWrite(leftMotorBackwardPin, HIGH);
  digitalWrite(rightMotorForwardPin, HIGH);
  digitalWrite(rightMotorBackwardPin, LOW);

  }
void moveBackward() {
  digitalWrite(leftMotorForwardPin, HIGH);
  digitalWrite(leftMotorBackwardPin, LOW);
  digitalWrite(rightMotorForwardPin, HIGH);
  digitalWrite(rightMotorBackwardPin, LOW);
  Serial.println("Moving backward");
  

}
// Function to turn the robot right
void turnRight() {
  digitalWrite(leftMotorForwardPin, HIGH);
  digitalWrite(leftMotorBackwardPin, LOW);
  digitalWrite(rightMotorForwardPin, LOW);
  digitalWrite(rightMotorBackwardPin, HIGH);
 

}

// Function to stop the robot
void stopMoving() {
  digitalWrite(leftMotorForwardPin, LOW);
  digitalWrite(leftMotorBackwardPin, LOW);
  digitalWrite(rightMotorForwardPin, LOW);
  digitalWrite(rightMotorBackwardPin, LOW);
}
