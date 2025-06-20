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


####################################
########## EINZELNE NOTEN ##########
####################################
# play_note(sleeptime=0.5, note=60, velocity=80, ser=ser)

# play_repeating_note(repeat=10, sleeptime=0.25, note=60, velocity=80, ser=ser)

# play_repeating_note_getting_faster(startsleeptime=1, stopsleeptime=0.05, change=0.05, note=60, velocity=80, ser=ser)
# play_repeating_note_getting_slower(startsleeptime=0.05, stopsleeptime=1, change=0.05, note=60, velocity=80, ser=ser)


#############################
########## AKKORDE ##########
#############################
# play_accord(note=60, velocity=80, ser=ser)
# time.sleep(1)
# play_accord(note=60, velocity=0, ser=ser)
# play_accord(note=62, velocity=80, ser=ser)
# time.sleep(1)
# play_accord(note=62, velocity=0, ser=ser)
# play_accord(note=64, velocity=80, ser=ser)
# time.sleep(1)
# play_accord(note=64, velocity=0, ser=ser)
# play_accord(note=65, velocity=80, ser=ser)
# time.sleep(1)
# play_accord(note=65, velocity=0, ser=ser)
# play_accord(note=67, velocity=80, ser=ser)
# time.sleep(1)
# play_accord(note=67, velocity=0, ser=ser)
# play_accord(note=69, velocity=80, ser=ser)
# time.sleep(1)
# play_accord(note=69, velocity=0, ser=ser)


#############################
########## ARPEGGIOS ##########
#############################
# for i in range(10):
#     play_white_keys(a=60, b=76, ser=ser, velocity=80, sleeptime=0.05)

# for i in range(10):
#     play_white_keys_descending(b=76, a=60, ser=ser, velocity=80, sleeptime=0.05)

# play_white_keys_incremental(a=60, b=76, ser=ser, velocity=80, sleeptime=0.05)
# play_white_keys_incremental_desc(b=76, a=60, ser=ser, velocity=80, sleeptime=0.05)


###########################
########## SONGS ##########
###########################
midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/twinkle-twinkle-little-star.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/bleach-here-to-stay.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/bach_846.mid')
# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/bach_847.mid')
# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/bach_850.mid')

# midi_file = mido.MidiFile('piano_robot_project_software/send_midi_data/midi_files/Test_Klavier.mid')
# midi_file = mido.MidiFile('send_midi_data/midi_files/Hungarian Rhapsody No. 2 - Franz Liszt [MIDICollection.net].mid')

play_midi_file(midi_file, ser) # Open the MIDI file as static for tests

# play_midi_file_one_channel(midi_file, 0, ser) # plays only notes on channel 0 (think thats left hand)

# play_midi_file(mido.MidiFile(sys.argv[1]), ser) # Open MIDI file dynamic as param in terminal -> brauche ich vllt auch nicht, da das auswählen der Midi Files direkt im Python File schneller ist wie im Terminal

time.sleep(1) # nicht unbedingt nötig denke ich, aber schön wenn der nicht instant den Port schließt nach dem letzten Byte finde ich

# Close the serial port
ser.close()



