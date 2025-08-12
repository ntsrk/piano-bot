#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwmBoard0 = Adafruit_PWMServoDriver(0x40);
Adafruit_PWMServoDriver pwmBoard1 = Adafruit_PWMServoDriver(0x41);
Adafruit_PWMServoDriver pwmBoard2 = Adafruit_PWMServoDriver(0x42);
Adafruit_PWMServoDriver pwmBoard3 = Adafruit_PWMServoDriver(0x43);
Adafruit_PWMServoDriver pwmBoard4 = Adafruit_PWMServoDriver(0x44);
Adafruit_PWMServoDriver pwmBoard5 = Adafruit_PWMServoDriver(0x45);

const float DUTY_CYCLE_ACC = 40.96;
const unsigned long MIN_TIME_BETWEEN_NOTES = 50; // ms

struct PinBoard {
  Adafruit_PWMServoDriver* board;
  byte pin;
};

struct ScheduledNote {
  byte note;
  byte velocity;
  unsigned long playTime; // Zeitpunkt, wann Note gespielt werden soll
};

const int MAX_SCHEDULED_NOTES = 16;
ScheduledNote scheduledNotes[MAX_SCHEDULED_NOTES];
int scheduledCount = 0;

// nächstmöglicher Zeitpunkt für jede Note
unsigned long nextAvailableTime[109];

void setup() {
  Serial.begin(115200);
  pwmBoard0.begin(); pwmBoard0.setPWMFreq(1600);
  pwmBoard1.begin(); pwmBoard1.setPWMFreq(1600);
  pwmBoard2.begin(); pwmBoard2.setPWMFreq(1600);
  pwmBoard3.begin(); pwmBoard3.setPWMFreq(1600);
  pwmBoard4.begin(); pwmBoard4.setPWMFreq(1600);
  pwmBoard5.begin(); pwmBoard5.setPWMFreq(1600);

  for (int i = 0; i < 109; i++) {
    nextAvailableTime[i] = 0;
  }
  for (int i = 0; i < MAX_SCHEDULED_NOTES; i++) {
    scheduledNotes[i].playTime = 0;
  }
}

void loop() {
  processSerialMidi();

  // Prüfe, ob geplante Noten jetzt gespielt werden können
  unsigned long currentTime = millis();
  for (int i = 0; i < scheduledCount; ) {
    if (scheduledNotes[i].playTime <= currentTime) {
      playNoteNow(scheduledNotes[i].note, scheduledNotes[i].velocity);

      // Note aus Queue löschen, indem alle nachfolgenden eine Position nach vorne rücken
      for (int j = i; j < scheduledCount - 1; j++) {
        scheduledNotes[j] = scheduledNotes[j + 1];
      }
      scheduledCount--;
    } else {
      i++;
    }
  }
}

void processSerialMidi() {
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
        if (expectedDataBytes == 1) return;
      } else if (state == 1) {
        dataByte2 = incomingByte;
        state = 0;

        if ((messageType & 0xF0) == 0x90 || (messageType & 0xF0) == 0x80) {
          byte velocity = dataByte2;
          byte note = dataByte1;

          scheduleNoteWithDelay(note, velocity);
        }
      }
    }
  }
}

void scheduleNoteWithDelay(byte note, byte velocity) {
  if (note >= 109) return; // ungültige Note ignorieren

  unsigned long currentTime = millis();
  unsigned long playTime = max(currentTime, nextAvailableTime[note]);
  nextAvailableTime[note] = playTime + MIN_TIME_BETWEEN_NOTES;

  if (scheduledCount < MAX_SCHEDULED_NOTES) {
    scheduledNotes[scheduledCount++] = {note, velocity, playTime};
  } else {
    // Queue voll, einfach sofort spielen als Fallback
    playNoteNow(note, velocity);
  }
}

void playNoteNow(byte note, byte velocity) {
  PinBoard pb = getPinAndBoard(note);
  if (pb.board != nullptr && pb.pin < 16) {
    int onTime = calcDutyCycleOnTime(calcDutyCycleValue(velocity));
    int offTime = calcDutyCycleOffTime(calcDutyCycleValue(velocity));
    pb.board->setPWM(pb.pin, onTime, offTime);
  }
}

PinBoard getPinAndBoard(byte note) {
  if (note >= 21 && note <= 36) return { &pwmBoard5, 36 - note };
  if (note >= 37 && note <= 52) return { &pwmBoard4, 52 - note };
  if (note >= 53 && note <= 68) return { &pwmBoard3, 68 - note };
  if (note >= 69 && note <= 84) return { &pwmBoard2, 84 - note };
  if (note >= 85 && note <= 100) return { &pwmBoard1, 100 - note };
  if (note >= 101 && note <= 108) return { &pwmBoard0, 108 - note };
  return { nullptr, 0xFF };
}

byte calcDutyCycleValue(byte midiNoteVelocity) {
  if (midiNoteVelocity == 0) return 0;
  return 50 + (midiNoteVelocity - 16) * (30.0 / 110);
}

int calcDutyCycleOnTime(byte dutyCycleValue) {
  if (dutyCycleValue == 100) return 4096;
  return 0;
}

int calcDutyCycleOffTime(byte dutyCycleValue) {
  if (dutyCycleValue == 100) return 0;
  if (dutyCycleValue == 0) return 4096;
  return dutyCycleValue * DUTY_CYCLE_ACC;
}
