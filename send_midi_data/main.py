import mido # https://github.com/mido/mido
import time
import serial
import sys
from functions import play_function, debug_repeat, debug_faster, debug_slower, play_one_channel

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

# debug_repeat(5, 1, 101, 80, ser)
# debug_repeat(1, 1, 101, 80, ser)

# debug_faster(1, 0.2, 0.2, 101, 80, ser)

# debug_slower(0.2, 1, 0.2, 101, 80, ser)

# play_function(mido.MidiFile(sys.argv[1]), ser) # Open MIDI file dynamic as param in terminal -> brauche ich vllt auch nicht, da das auswählen der Midi Files direkt im Python File schneller ist wie im Terminal
play_function(mido.MidiFile('midi_files/Test_Klavier.mid'), ser) # Open the MIDI file as static for tests
# play_function(mido.MidiFile('midi_files/Hungarian Rhapsody No. 2 - Franz Liszt [MIDICollection.net].mid'), ser)

# play_one_channel(mido.MidiFile('midi_files/Hungarian Rhapsody No. 2 - Franz Liszt [MIDICollection.net].mid'), 0, ser)

time.sleep(1) # nicht unbedingt nötig denke ich, aber schön wenn der nicht instant den Port schließt nach dem letzten Byte finde ich

# Close the serial port
ser.close()



