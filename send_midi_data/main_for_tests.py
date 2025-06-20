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

# play_repeating_note(repeat=5, sleeptime=1, note=101, velocity=80, ser=ser)

# play_repeating_note(repeat=10, sleeptime=0.05, note=101, velocity=80, ser=ser)
# play_repeating_note(repeat=10, sleeptime=0.1, note=101, velocity=80, ser=ser)
# play_repeating_note(repeat=10, sleeptime=0.2, note=101, velocity=80, ser=ser)
# play_repeating_note(repeat=10, sleeptime=0.4, note=101, velocity=80, ser=ser)

# play_repeating_note(repeat=1, sleeptime=1, note=101, velocity=80, ser=ser)
# play_repeating_note(repeat=10, sleeptime=0.25, note=101, velocity=80, ser=ser)


# midi_msg_on1 = mido.Message('note_on', channel=0, note=21, velocity=80)
# midi_msg_on2 = mido.Message('note_on', channel=0, note=22, velocity=80)
# midi_msg_on3 = mido.Message('note_on', channel=0, note=23, velocity=80)
# midi_msg_off1 = mido.Message('note_on', channel=0, note=21, velocity=0)
# midi_msg_off2 = mido.Message('note_on', channel=0, note=22, velocity=0)
# midi_msg_off3 = mido.Message('note_on', channel=0, note=23, velocity=0)

# for i in range(10): 
#     ser.write(midi_msg_on1.bytes())
#     ser.write(midi_msg_on2.bytes())
#     ser.write(midi_msg_on3.bytes())
#     time.sleep(0.5)
#     ser.write(midi_msg_off1.bytes())
#     ser.write(midi_msg_off2.bytes())
#     ser.write(midi_msg_off3.bytes())
#     time.sleep(0.5)

play_repeating_note(repeat=10, sleeptime=0.25, note=21, velocity=80, ser=ser)
# play_repeating_note(repeat=10, sleeptime=0.25, note=22, velocity=80, ser=ser)
# play_repeating_note(repeat=10, sleeptime=0.25, note=23, velocity=80, ser=ser)
# play_repeating_note(repeat=1, sleeptime=1, note=101, velocity=80, ser=ser)



#############################
########## AKKORDE ##########
#############################
# play_accord(note=21, velocity=80, ser=ser)
# time.sleep(1)
# play_accord(note=21, velocity=0, ser=ser)
# play_accord(note=22, velocity=80, ser=ser)
# time.sleep(1)
# play_accord(note=22, velocity=0, ser=ser)
# play_accord(note=23, velocity=80, ser=ser)
# time.sleep(1)
# play_accord(note=23, velocity=0, ser=ser)
# play_accord(note=24, velocity=80, ser=ser)
# time.sleep(1)
# play_accord(note=24, velocity=0, ser=ser)
# play_accord(note=25, velocity=80, ser=ser)
# time.sleep(1)
# play_accord(note=25, velocity=0, ser=ser)
# play_accord(note=26, velocity=80, ser=ser)
# time.sleep(1)
# play_accord(note=26, velocity=0, ser=ser)

#############################
########## ARPEGGIOS ##########
#############################
# for i in range(10):
#     play_notes_from_a_to_b(sleeptime=0.05, a=21, b=30, velocity=80, ser=ser)

# for i in range(10):
#     play_notes_from_b_to_a(sleeptime=0.05, a=21, b=30, velocity=80, ser=ser)

# play_notes_increment_a_to_b(a=21, b=30, velocity=80, sleeptime=0.1, ser=ser)
# play_notes_increment_b_to_a(b=30, a=21, velocity=80, sleeptime=0.1, ser=ser)



# play_accord(note=22, velocity=80, sleeptime=0.1, ser=ser)
# play_accord(note=23, velocity=80, sleeptime=0.1, ser=ser)
# play_accord(note=24, velocity=80, sleeptime=0.1, ser=ser)
# play_accord(note=25, velocity=80, sleeptime=0.1, ser=ser)
# play_accord(note=26, velocity=80, sleeptime=0.1, ser=ser)

# play_notes_from_b_to_a(sleeptime=0.088, a=21, b=29, velocity=80, ser=ser)
# play_notes_from_a_to_b(sleeptime=0.088, a=22, b=30, velocity=80, ser=ser)
# play_notes_from_b_to_a(sleeptime=0.088, a=21, b=29, velocity=80, ser=ser)
# play_notes_from_a_to_b(sleeptime=0.088, a=22, b=30, velocity=80, ser=ser)
# play_notes_from_a_to_b(sleeptime=0.088, a=21, b=30, velocity=80, ser=ser)
# play_notes_from_b_to_a(sleeptime=0.088, a=21, b=29, velocity=80, ser=ser)
# play_notes_from_a_to_b(sleeptime=0.088, a=22, b=30, velocity=80, ser=ser)
# play_notes_from_b_to_a(sleeptime=0.088, a=21, b=29, velocity=80, ser=ser)
# play_notes_from_a_to_b(sleeptime=0.088, a=22, b=30, velocity=80, ser=ser)
# play_notes_from_a_to_b(sleeptime=0.088, a=21, b=30, velocity=80, ser=ser)
# play_notes_from_b_to_a(sleeptime=0.088, a=21, b=29, velocity=80, ser=ser)
# play_notes_from_a_to_b(sleeptime=0.088, a=22, b=30, velocity=80, ser=ser)
# play_notes_from_b_to_a(sleeptime=0.088, a=21, b=29, velocity=80, ser=ser)
# play_notes_from_a_to_b(sleeptime=0.088, a=22, b=30, velocity=80, ser=ser)



# play_notes_from_a_to_b(sleeptime=1, a=27, b=36, velocity=80, ser=ser)
# play_notes_from_b_to_a(sleeptime=1, a=27, b=36, velocity=80, ser=ser)
# play_notes_from_a_to_b(sleeptime=0.125, a=27, b=36, velocity=80, ser=ser)
# play_notes_from_b_to_a(sleeptime=0.125, a=27, b=36, velocity=80, ser=ser)
# play_notes_from_a_to_b(sleeptime=0.0625, a=27, b=36, velocity=80, ser=ser)
# play_notes_from_b_to_a(sleeptime=0.0625, a=27, b=36, velocity=80, ser=ser)
# play_notes_from_a_to_b(sleeptime=0.03125, a=27, b=36, velocity=80, ser=ser)
# play_notes_from_b_to_a(sleeptime=0.03125, a=27, b=36, velocity=80, ser=ser)
# play_notes_from_a_to_b(sleeptime=0.015625, a=27, b=36, velocity=80, ser=ser)
# play_notes_from_b_to_a(sleeptime=0.015625, a=27, b=36, velocity=80, ser=ser)
# play_notes_from_a_to_b(sleeptime=0.03125, a=27, b=36, velocity=80, ser=ser)
# play_notes_from_b_to_a(sleeptime=0.03125, a=27, b=36, velocity=80, ser=ser)
# play_notes_from_a_to_b(sleeptime=0.015625, a=27, b=36, velocity=80, ser=ser)
# play_notes_from_b_to_a(sleeptime=0.015625, a=27, b=36, velocity=80, ser=ser)
# play_notes_from_a_to_b(sleeptime=0.01, a=27, b=36, velocity=80, ser=ser)
# play_notes_from_b_to_a(sleeptime=0.01, a=27, b=36, velocity=80, ser=ser)
# play_notes_from_a_to_b(sleeptime=0.01, a=27, b=36, velocity=80, ser=ser)
# play_notes_from_b_to_a(sleeptime=0.01, a=27, b=36, velocity=80, ser=ser)

# play_repeating_note_getting_faster(startsleeptime=1, stopsleeptime=0.2, change=0.2, note=101, velocity=80, ser=ser)
# play_repeating_note_getting_slower(startsleeptime=0.2, stopsleeptime=1, change=0.2, note=101, velocity=80, ser=ser)

# midi_file = mido.MidiFile('piano_robot_project_software/send_midi_data/midi_files/Test_Klavier.mid')
# midi_file = mido.MidiFile('send_midi_data/midi_files/Hungarian Rhapsody No. 2 - Franz Liszt [MIDICollection.net].mid')


# play_repeating_note_getting_faster(startsleeptime=0.25, stopsleeptime=0.05, note=27, velocity=80, ser=ser, change=0.05)

# play_midi_file(midi_file, ser) # Open the MIDI file as static for tests

# play_midi_file_one_channel(midi_file, 0, ser) # plays only notes on channel 0 (think thats left hand)

# play_midi_file(mido.MidiFile(sys.argv[1]), ser) # Open MIDI file dynamic as param in terminal -> brauche ich vllt auch nicht, da das auswählen der Midi Files direkt im Python File schneller ist wie im Terminal

time.sleep(1) # nicht unbedingt nötig denke ich, aber schön wenn der nicht instant den Port schließt nach dem letzten Byte finde ich

# Close the serial port
ser.close()



