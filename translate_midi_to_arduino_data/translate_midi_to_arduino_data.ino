// load libraries
#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

// define PCA9685 boards with their I2C addresses
Adafruit_PWMServoDriver pwmBoards[6] = {
  Adafruit_PWMServoDriver(0x40), // Board 0: Key 81-88
  Adafruit_PWMServoDriver(0x41), // Board 1: Key 65-80
  Adafruit_PWMServoDriver(0x42), // Board 2: Key 49-64
  Adafruit_PWMServoDriver(0x43), // Board 3: Key 33-48
  Adafruit_PWMServoDriver(0x44), // Board 4: Key 17-32
  Adafruit_PWMServoDriver(0x45)  // Board 5: Key 1-16
};

const float DUTY_CYCLE_ACC = 40.96; // 4096 / 100

void setup() {
  Serial.begin(115200);
  for (int i = 0; i < 6; i++) {
    pwmBoards[i].begin();
    pwmBoards[i].setPWMFreq(1600);
  }
}

void loop() {
  static byte messageType = 0;
  static byte dataByte1 = 0;
  static byte dataByte2 = 0;
  static int state = 0;
  static int expectedDataBytes = 0;

  while (Serial.available()) {
    byte incomingByte = Serial.read();

    if (incomingByte & 0x80) {
      messageType = incomingByte;
      byte type = messageType & 0xF0;
      expectedDataBytes = (type == 0xC0 || type == 0xD0) ? 1 : 2;
      state = 0;
    } else {
      if (state == 0) {
        dataByte1 = incomingByte;
        state = 1;
        if (expectedDataBytes == 1) {
          // optional
        }
      } else if (state == 1) {
        dataByte2 = incomingByte;
        state = 0;

        if ((messageType & 0xF0) == 0x90 || (messageType & 0xF0) == 0x80) {
          byte pin = returnPin(dataByte1);
          int boardIndex = returnBoardIndex(dataByte1);

          if (boardIndex >= 0 && boardIndex < 6) {
            pwmBoards[boardIndex].setPWM(
              pin,
              calcDutyCycleOnTime(calcDutyCycleValue(dataByte2)),
              calcDutyCycleOffTime(calcDutyCycleValue(dataByte2))
            );
          }
        }
      }
    }
  }
}

byte returnBoardIndex(byte midiNoteValue) {
  if (midiNoteValue >= 101 && midiNoteValue <= 108) return 0;
  if (midiNoteValue >= 85 && midiNoteValue <= 100) return 1;
  if (midiNoteValue >= 69 && midiNoteValue <= 84)  return 2;
  if (midiNoteValue >= 53 && midiNoteValue <= 68)  return 3;
  if (midiNoteValue >= 37 && midiNoteValue <= 52)  return 4;
  if (midiNoteValue >= 21 && midiNoteValue <= 36)  return 5;
  return -1; // invalid note
}

byte returnPin(byte midiNoteValue) {
  return (midiNoteValue - 21) % 16; // note-to-pin mapping per board
}

byte calcDutyCycleValue(byte midiNoteVelocity) {
  if (midiNoteVelocity == 0) return 0;
  return 70 + (midiNoteVelocity - 16) * (30 / 110.0);
}

int calcDutyCycleOnTime(byte dutyCycleValue) {
  return (dutyCycleValue == 100) ? 4096 : 0;
}

int calcDutyCycleOffTime(byte dutyCycleValue) {
  if (dutyCycleValue == 100) return 0;
  if (dutyCycleValue == 0) return 4096;
  return dutyCycleValue * DUTY_CYCLE_ACC;
}
