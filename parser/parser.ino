#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwmBoard5 = Adafruit_PWMServoDriver(0x45);

const float DUTY_CYCLE_ACC = 40.96; // Umrechnung für PCA9685 (12 Bit = 4096 Schritte)
const byte HOLD_DUTY = 50;          // DutyCycle nach Kick-Phase
const byte MIN_NOTE_DELAY = 40;     // Minimaler Abstand in ms zwischen zwei gleichen Anschlägen (ansonsten hat die Taste nicht genug Zeit wieder nach oben zu kommen um erneut gespielt zu werden und ist dann einfach stumm)

struct NoteState {
  bool active = false;
  unsigned long kickStart = 0;
  unsigned long lastReleased = 0;
  byte pin = 0xFF;
  byte dutyCycleKick = 0;
};

NoteState noteStates[128]; // Zustände für alle MIDI-Noten

void setup() {
  Serial.begin(115200);
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

    if (incomingByte & 0x80) {  // Statusbyte
      messageType = incomingByte;
      byte type = messageType & 0xF0;
      expectedDataBytes = (type == 0xC0 || type == 0xD0) ? 1 : 2;
      state = 0;
    } else {
      if (state == 0) {
        dataByte1 = incomingByte;
        state = 1;
      } else if (state == 1) {
        dataByte2 = incomingByte;
        state = 0;

        byte pin = returnPin(dataByte1);
        if (pin == 0xFF) continue; // ungültige Note ignorieren

        unsigned long now = millis();

        if ((messageType & 0xF0) == 0x90 && dataByte2 > 0) {
          // NOTE ON
          unsigned long timeSinceRelease = now - noteStates[dataByte1].lastReleased;
          if (timeSinceRelease < MIN_NOTE_DELAY) {
            delay(MIN_NOTE_DELAY - timeSinceRelease); // Warten bis Taste bereit ist
          }

          byte kickDuty = calcDutyCycleValue(dataByte2);
          pwmBoard5.setPWM(pin, calcDutyCycleOnTime(kickDuty), calcDutyCycleOffTime(kickDuty));

          noteStates[dataByte1].active = true;
          noteStates[dataByte1].kickStart = millis();
          noteStates[dataByte1].pin = pin;
          noteStates[dataByte1].dutyCycleKick = kickDuty;

        } else if ((messageType & 0xF0) == 0x80 || dataByte2 == 0) {
          // NOTE OFF
          pwmBoard5.setPWM(pin, 0, 4096); // PWM auf 0 setzen
          noteStates[dataByte1].active = false;
          noteStates[dataByte1].lastReleased = now;
        }
      }
    }
  }

  // Nach 50 ms DutyCycle auf HOLD_DUTY reduzieren
  for (int i = 0; i < 128; i++) {
    if (noteStates[i].active && (millis() - noteStates[i].kickStart > 50)) {
      pwmBoard5.setPWM(
        noteStates[i].pin,
        calcDutyCycleOnTime(HOLD_DUTY),
        calcDutyCycleOffTime(HOLD_DUTY)
      );
      noteStates[i].active = false; // nur einmal reduzieren
    }
  }
}

// Nur weiße Tasten definieren (weil nur 10 weiße Tasten aktuell angeschlossen sind)
byte returnPin(byte midiNoteValue) {
  switch (midiNoteValue) {
    case 60: return 15; // C4
    case 62: return 14; // D4
    case 64: return 13; // E4
    case 65: return 12; // F4
    case 67: return 11; // G4
    case 69: return 10; // A4
    case 71: return 9;  // B4
    case 72: return 8;  // C5
    case 74: return 7;  // D5
    case 76: return 6;  // E5
    default: return 0xFF;
  }
}

byte calcDutyCycleValue(byte midiNoteVelocity) {
  if (midiNoteVelocity == 0) return 0;
  if (midiNoteVelocity < 16) midiNoteVelocity = 16;
  return 70 + ((midiNoteVelocity - 16) * 30 / 110); // 70–100 %
}

int calcDutyCycleOnTime(byte dutyCycleValue) {
  return (dutyCycleValue == 100) ? 4096 : 0;
}

int calcDutyCycleOffTime(byte dutyCycleValue) {
  if (dutyCycleValue == 100) return 0;
  if (dutyCycleValue == 0) return 4096;
  return dutyCycleValue * DUTY_CYCLE_ACC;
}
