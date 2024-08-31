import mido # https://github.com/mido/mido
import time
import serial
import sys
from functions import *

# Configure serial connection
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,  # Arduino hat auch 9600 bit per second -> passt also zusammen
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=2  # Read timeout in seconds
)

# Ensure the serial port is open
if not ser.is_open:
    ser.open()

time.sleep(2) # benötigt etwas Zeit die Verbindung aufzubauen -> sonst verpasst der Arduino die ersten paar Bytes

play_repeating_note(repeat=5, sleeptime=1, note=101, velocity=80, ser=ser)
# play_repeating_note(repeat=1, sleeptime=1, note=101, velocity=80, ser=ser)

# play_repeating_note_getting_faster(startsleeptime=1, stopsleeptime=0.2, change=0.2, note=101, velocity=80, ser=ser)

# play_repeating_note_getting_slower(startsleeptime=0.2, stopsleeptime=1, change=0.2, note=101, velocity=80, ser=ser)

midi_file = mido.MidiFile('send_midi_data/midi_files/Test_Klavier.mid')
# midi_file = mido.MidiFile('send_midi_data/midi_files/Hungarian Rhapsody No. 2 - Franz Liszt [MIDICollection.net].mid')

# play_midi_file(midi_file, ser) # Open the MIDI file as static for tests

# play_midi_file_one_channel(midi_file, 0, ser) # plays only notes on channel 0 (think thats left hand)

# play_midi_file(mido.MidiFile(sys.argv[1]), ser) # Open MIDI file dynamic as param in terminal -> brauche ich vllt auch nicht, da das auswählen der Midi Files direkt im Python File schneller ist wie im Terminal

time.sleep(1) # nicht unbedingt nötig denke ich, aber schön wenn der nicht instant den Port schließt nach dem letzten Byte finde ich

# Close the serial port
ser.close()



