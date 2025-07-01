import mido # https://github.com/mido/mido
import time
import serial
import sys
from functions import *

# Configure serial connection
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,  # Arduino hat auch 9600 bit per second -> passt also zusammen
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=2  # Read timeout in seconds
)

# Ensure the serial port is open
if not ser.is_open:
    ser.open()

time.sleep(2) # benötigt etwas Zeit die Verbindung aufzubauen -> sonst verpasst der Arduino die ersten paar Bytes

play_midi_file(mido.MidiFile(sys.argv[1]), ser)

time.sleep(1) # nicht unbedingt nötig denke ich, aber schön wenn der nicht instant den Port schließt nach dem letzten Byte finde ich

# Close the serial port
ser.close()



