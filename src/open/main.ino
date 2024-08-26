#include <Wire.h>
#include "Adafruit_TCS34725.h"

// Pin Definitions
const int trigPin = 12;
const int echoPin = 11;
const int led = 13;

// Variables
long duration;
int distance;
byte gammatable[256];

// Initialize TCS34725 sensor
Adafruit_TCS34725 tcs = Adafruit_TCS34725(TCS34725_INTEGRATIONTIME_50MS, TCS34725_GAIN_4X);

void setup() {
  Serial.begin(115200); // Faster baud rate for quicker serial communication

  // Set pin modes
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  pinMode(led, OUTPUT);

  // Initialize TCS34725 sensor
  if (!tcs.begin()) {
    Serial.println("No TCS34725 found ... check your connections");
    while (1); // Halt if sensor not found
  }

  // Create gamma correction table
  for (int i = 0; i < 256; i++) {
    float x = i / 255.0;
    x = pow(x, 2.5) * 255;
    gammatable[i] = x; // Simplified for non-commonAnode case
  }
}

void loop() {
  digitalWrite(led, HIGH); // Turn on LED for TCS34725
  delay(10); // Shorter delay to speed up reading

  float red, green, blue;
  tcs.setInterrupt(false); // Turn on LED for color reading
  tcs.getRGB(&red, &green, &blue);
  tcs.setInterrupt(true); // Turn off LED

  // Process color data
  int r = int(red);
  int g = int(green);
  int b = int(blue);
  String result;
  
  if (r<100) {
    result = "b";
  } else if (r > g && (r - g) <= 55) {
    result = "w";
  } else {
    result = "r";
  }

  // Measure distance
  distance = measureDistance(trigPin, echoPin);

  // Output results
  Serial.print(distance);
  Serial.print(",");
  Serial.println(result);

  // Short delay for loop stability
  delay(100); // Adjust as needed for your application
}

// Function to measure distance
int measureDistance(int trigPin, int echoPin) {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  long duration = pulseIn(echoPin, HIGH);
  return duration * 0.034 / 2;
}
