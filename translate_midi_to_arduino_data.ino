// load libraries
#include <Wire.h> // library allowing to communicate with I2C devices
#include <Adafruit_PWMServoDriver.h> // library for PCA985 PWM-Controller-Board (16 channel, 12bit)

// define addresses for pwm boards
// middle C (60 / 40 / C4)=(midi note number / key Number / name of key)
Adafruit_PWMServoDriver pwmBoard5 = Adafruit_PWMServoDriver(0x45); // Key Number 1 to 16 / Midi Note Number 21 to 36 / Key Name A0 to C2 / I2C Bus 000 101
Adafruit_PWMServoDriver pwmBoard4 = Adafruit_PWMServoDriver(0x44); // Key Number 17 to 32 / Midi Note Number 37 to 52 / Key Name C#2 to E3 / I2C Bus 000 100
Adafruit_PWMServoDriver pwmBoard3 = Adafruit_PWMServoDriver(0x43); // Key Number 33 to 48 / Midi Note Number 53 to 68 / Key Name F3 to G#4 / I2C Bus 000 011
Adafruit_PWMServoDriver pwmBoard2 = Adafruit_PWMServoDriver(0x42); // Key Number 49 to 64 / Midi Note Number 69 to 84 / Key Name A4 to C6 / I2C Bus 000 010
Adafruit_PWMServoDriver pwmBoard1 = Adafruit_PWMServoDriver(0x41); // Key Number 65 to 80 / Midi Note Number 85 to 100 / Key Name C#6 to E7 / I2C Bus 000 001
Adafruit_PWMServoDriver pwmBoard0 = Adafruit_PWMServoDriver(0x40); // Key Number 81 to 88 / Midi Note Number 101 to 108 / Key Name F7 to C8 / I2C Bus 000 000

// define constants and variables
const byte INTERVAL_BETWEEN_NOTES = 25; // in ms (25ms works best at the moment)
const float DUTY_CYCLE_ACC = 40.96; // PWM Board Accuracy 12bit=2^12=4096
byte dutyCycleValue; // store value from calcDutyCyclveValue(midiNoteVelocity)
byte messageType;
byte midiNoteValue;
byte midiNoteVelocity;

void setup() {
  Serial.begin(9600); // open serial port with reading/sending speed (bit per second)
  pwmBoard0.begin();
  pwmBoard0.setPWMFreq(1600); // define frequency for all ports on the board
  pwmBoard1.begin();
  pwmBoard1.setPWMFreq(1600);
  pwmBoard2.begin();
  pwmBoard2.setPWMFreq(1600);
  pwmBoard3.begin();
  pwmBoard3.setPWMFreq(1600);
  pwmBoard4.begin();
  pwmBoard4.setPWMFreq(1600);
  pwmBoard5.begin();
  pwmBoard5.setPWMFreq(1600); 
}

void loop() {  
  while (Serial.available() > 2) {
    messageType = Serial.read();
    if (messageType != 144) return; // alle was keine Note On Messages sind sollen ignoriert werden (zu Beginn des Liedes gibt es manchmal noch andere Message die alles dann durcheinander bringen)
    else {
      midiNoteValue = Serial.read();
      midiNoteVelocity = Serial.read();
      // choose right pwm board and set the right pin with duty cycle
      if (midiNoteValue >= 101 && midiNoteValue <= 108) {
        delay(INTERVAL_BETWEEN_NOTES);
        pwmBoard0.setPWM(returnPin(midiNoteValue), calcDutyCycleOnTime(calcDutyCycleValue(midiNoteVelocity)), calcDutyCycleOffTime(calcDutyCycleValue(midiNoteVelocity)));  
      }
      if (midiNoteValue >= 85 && midiNoteValue <= 100) {
        delay(INTERVAL_BETWEEN_NOTES);
        pwmBoard1.setPWM(returnPin(midiNoteValue), calcDutyCycleOnTime(calcDutyCycleValue(midiNoteVelocity)), calcDutyCycleOffTime(calcDutyCycleValue(midiNoteVelocity)));
      }
      if (midiNoteValue >= 69 && midiNoteValue <= 84) {
        delay(INTERVAL_BETWEEN_NOTES);
        pwmBoard2.setPWM(returnPin(midiNoteValue), calcDutyCycleOnTime(calcDutyCycleValue(midiNoteVelocity)), calcDutyCycleOffTime(calcDutyCycleValue(midiNoteVelocity)));
      }
      if (midiNoteValue >= 53 && midiNoteValue <= 68) {
        delay(INTERVAL_BETWEEN_NOTES);
        pwmBoard3.setPWM(returnPin(midiNoteValue), calcDutyCycleOnTime(calcDutyCycleValue(midiNoteVelocity)), calcDutyCycleOffTime(calcDutyCycleValue(midiNoteVelocity)));
      }
      if (midiNoteValue >= 37 && midiNoteValue <= 52) {
        delay(INTERVAL_BETWEEN_NOTES);
        pwmBoard4.setPWM(returnPin(midiNoteValue), calcDutyCycleOnTime(calcDutyCycleValue(midiNoteVelocity)), calcDutyCycleOffTime(calcDutyCycleValue(midiNoteVelocity)));
      }
      if (midiNoteValue >= 21 && midiNoteValue <= 36) {
        delay(INTERVAL_BETWEEN_NOTES);
        pwmBoard5.setPWM(returnPin(midiNoteValue), calcDutyCycleOnTime(calcDutyCycleValue(midiNoteVelocity)), calcDutyCycleOffTime(calcDutyCycleValue(midiNoteVelocity)));
      }    
    }
  }
}

// methods (functions and procedures)
byte returnPin(byte midiNoteValue) { // returns value between 0 and 15 (on one board are 16 pins numbered from 0 to 15)
  if (midiNoteValue >= 21 && midiNoteValue <= 36) {
    return midiNoteValue - 21;
  }
  if (midiNoteValue >= 37 && midiNoteValue <= 52) {
    return midiNoteValue - 37;
  }
  if (midiNoteValue >= 53 && midiNoteValue <= 68) {
    return midiNoteValue - 53;
  }
  if (midiNoteValue >= 69 && midiNoteValue <= 84) {
    return midiNoteValue - 69;
  }
  if (midiNoteValue >= 85 && midiNoteValue <= 100) {
    return midiNoteValue - 85;
  }
  if (midiNoteValue >= 101 && midiNoteValue <= 108) {
    return midiNoteValue - 101;
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