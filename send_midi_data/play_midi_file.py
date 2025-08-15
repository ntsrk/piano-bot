import mido
import time
import serial
import sys
from functions import *

# Configure serial connection
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=2
)

if not ser.is_open:
    ser.open()

time.sleep(2)  # kurz warten, bis der Arduino bereit ist

try:
    # MIDI abspielen
    play_midi_file(mido.MidiFile(sys.argv[1]), ser)
    time.sleep(1)
except KeyboardInterrupt:
    print("\nCtrl+C erkannt: Alle Noten aus")
    for note in range(128):
        msg = mido.Message('note_on', channel=0, note=note, velocity=0)
        ser.write(msg.bytes())  # Alle Noten auf 0 setzen
finally:
    ser.close()  # Port sauber schließen
