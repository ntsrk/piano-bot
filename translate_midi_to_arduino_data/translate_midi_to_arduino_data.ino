// load libraries
#include <Wire.h> // library allowing to communicate with I2C devices
#include <Adafruit_PWMServoDriver.h> // library for PCA985 PWM-Controller-Board (16 channel, 12bit)

// define addresses for pwm boards
// middle C (60 / 40 / C4)=(midi note number / key Number / name of key)
Adafruit_PWMServoDriver pwmBoard5 = Adafruit_PWMServoDriver(0x45); // Key Number 1 to 16 / Midi Note Number 21 to 36 / Key Name A0 to C2 / I2C Bus 000 101
// Adafruit_PWMServoDriver pwmBoard4 = Adafruit_PWMServoDriver(0x44); // Key Number 17 to 32 / Midi Note Number 37 to 52 / Key Name C#2 to E3 / I2C Bus 000 100
// Adafruit_PWMServoDriver pwmBoard3 = Adafruit_PWMServoDriver(0x43); // Key Number 33 to 48 / Midi Note Number 53 to 68 / Key Name F3 to G#4 / I2C Bus 000 011
// Adafruit_PWMServoDriver pwmBoard2 = Adafruit_PWMServoDriver(0x42); // Key Number 49 to 64 / Midi Note Number 69 to 84 / Key Name A4 to C6 / I2C Bus 000 010
// Adafruit_PWMServoDriver pwmBoard1 = Adafruit_PWMServoDriver(0x41); // Key Number 65 to 80 / Midi Note Number 85 to 100 / Key Name C#6 to E7 / I2C Bus 000 001
// Adafruit_PWMServoDriver pwmBoard0 = Adafruit_PWMServoDriver(0x40); // Key Number 81 to 88 / Midi Note Number 101 to 108 / Key Name F7 to C8 / I2C Bus 000 000

// Ziel C4 bis E5 / nur pwmBoard5 zur Verfügung
// C4 = 60

// define constants and variables
// const byte INTERVAL_BETWEEN_NOTES = 25; // in ms (25ms works best at the moment)
const float DUTY_CYCLE_ACC = 40.96; // PWM Board Accuracy 12bit=2^12=4096
byte dutyCycleValue; // store value from calcDutyCyclveValue(midiNoteVelocity)
byte messageType;
byte midiNoteValue;
byte midiNoteVelocity;

void setup() {
  Serial.begin(115200); // open serial port with reading/sending speed (bit per second)
  // Serial.begin(9600); // open serial port with reading/sending speed (bit per second)
  // pwmBoard0.begin();
  // pwmBoard0.setPWMFreq(1600); // define frequency for all ports on the board
  // pwmBoard1.begin();
  // pwmBoard1.setPWMFreq(1600);
  // pwmBoard2.begin();
  // pwmBoard2.setPWMFreq(1600);
  // pwmBoard3.begin();
  // pwmBoard3.setPWMFreq(1600);
  // pwmBoard4.begin();
  // pwmBoard4.setPWMFreq(1600);
  pwmBoard5.begin();
  pwmBoard5.setPWMFreq(1600); 
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
      // Statusbyte erkannt
      messageType = incomingByte;

      // Bestimme erwartete Datenbytes
      byte type = messageType & 0xF0;
      if (type == 0xC0 || type == 0xD0) {
        expectedDataBytes = 1; // Program Change, Channel Pressure
      } else {
        expectedDataBytes = 2; // Note On/Off, CC, etc.
      }

      state = 0; // Start reading data bytes
    } else {
      // Datenbytes
      if (state == 0) {
        dataByte1 = incomingByte;
        state = 1;

        if (expectedDataBytes == 1) {
          // Nur ein Datenbyte erwartet – verarbeite sofort
          // OPTIONAL: Wenn du Program Changes verarbeiten willst
          // (Hier nichts machen, da irrelevant für PWM)
        }
      } else if (state == 1) {
        dataByte2 = incomingByte;
        state = 0;

        // Jetzt verarbeiten
        if ((messageType & 0xF0) == 0x90 || (messageType & 0xF0) == 0x80) {
          // delay(INTERVAL_BETWEEN_NOTES);
          pwmBoard5.setPWM(
            returnPin(dataByte1),
            calcDutyCycleOnTime(calcDutyCycleValue(dataByte2)),
            calcDutyCycleOffTime(calcDutyCycleValue(dataByte2))
          );
        }
      }
    }
  }
}



// methods (functions and procedures)
byte returnPin(byte midiNoteValue) { // returns value between 0 and 15 (on one board are 16 pins numbered from 0 to 15)
    switch (midiNoteValue) {
      case 60:
        return midiNoteValue = 15;
        break;
      case 62:
        return midiNoteValue = 14;
        break;
      case 64:
        return midiNoteValue = 13;
        break;
      case 65:
        return midiNoteValue = 12;
        break;
      case 67:
        return midiNoteValue = 11;
        break;
      case 69:
        return midiNoteValue = 10;
        break;
      case 71:
        return midiNoteValue = 9;
        break;
      case 72:
        return midiNoteValue = 8;
        break;
      case 74:
        return midiNoteValue = 7;
        break;
      case 76:
        return midiNoteValue = 6;
        break;
    }
}

byte calcDutyCycleValue(byte midiNoteVelocity) { // midiNoteVelocity between 0 and 127, dutyCycleValue between 0 and 100
  switch(midiNoteVelocity) {
    case 0: // note off
      return 0;
    default:
      return 70+(midiNoteVelocity-16)*(30/110); // see notes for explanation
  }
}  

int calcDutyCycleOnTime(byte dutyCycleValue) {
  if (dutyCycleValue == 100) return 4096;
  else return 0;
}

int calcDutyCycleOffTime(byte dutyCycleValue) {
  if (dutyCycleValue == 100) return 0;
  else if (dutyCycleValue == 0) return 4096;
  else return dutyCycleValue * DUTY_CYCLE_ACC;
}