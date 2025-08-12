import mido # https://github.com/mido/mido
import time
import serial
import sys
from functions import *

# Configure serial connection
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,  # Arduino hat auch 9600 bit per second -> passt also zusammen
    # baudrate=9600,  # Arduino hat auch 9600 bit per second -> passt also zusammen
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

# play_repeating_note(repeat=30, sleeptime=0.088, note=60, velocity=30, ser=ser)
# play_repeating_note(repeat=30, sleeptime=0.088, note=62, velocity=80, ser=ser)
# play_repeating_note(repeat=30, sleeptime=0.088, note=64, velocity=80, ser=ser)
# play_repeating_note(repeat=30, sleeptime=0.088, note=65, velocity=80, ser=ser)
# play_repeating_note(repeat=30, sleeptime=0.088, note=67, velocity=80, ser=ser)
# play_repeating_note(repeat=30, sleeptime=0.088, note=69, velocity=80, ser=ser)
# play_repeating_note(repeat=30, sleeptime=0.088, note=71, velocity=80, ser=ser)
# play_repeating_note(repeat=30, sleeptime=0.088, note=72, velocity=80, ser=ser)
# play_repeating_note(repeat=30, sleeptime=0.088, note=74, velocity=80, ser=ser)
# play_repeating_note(repeat=30, sleeptime=0.088, note=76, velocity=80, ser=ser)

# play_repeating_note_getting_faster(startsleeptime=1, stopsleeptime=0.02, change=0.02, note=60, velocity=80, ser=ser)
# play_repeating_note_getting_slower(startsleeptime=0.05, stopsleeptime=1, change=0.05, note=60, velocity=80, ser=ser)


#############################
########## AKKORDE ##########
############################
# ser.write(mido.Message('note_on', channel=0, note=60, velocity=80).bytes())
# ser.write(mido.Message('note_on', channel=0, note=64, velocity=80).bytes())
# ser.write(mido.Message('note_on', channel=0, note=67, velocity=80).bytes())
# time.sleep(1)
# ser.write(mido.Message('note_on', channel=0, note=60, velocity=0).bytes())
# ser.write(mido.Message('note_on', channel=0, note=64, velocity=0).bytes())
# ser.write(mido.Message('note_on', channel=0, note=67, velocity=0).bytes())
# time.sleep(1)
# ser.write(mido.Message('note_on', channel=0, note=62, velocity=80).bytes())
# ser.write(mido.Message('note_on', channel=0, note=65, velocity=80).bytes())
# ser.write(mido.Message('note_on', channel=0, note=69, velocity=80).bytes())
# time.sleep(1)
# ser.write(mido.Message('note_on', channel=0, note=62, velocity=0).bytes())
# ser.write(mido.Message('note_on', channel=0, note=65, velocity=0).bytes())
# ser.write(mido.Message('note_on', channel=0, note=69, velocity=0).bytes())
# time.sleep(1)
# ser.write(mido.Message('note_on', channel=0, note=64, velocity=80).bytes())
# ser.write(mido.Message('note_on', channel=0, note=67, velocity=80).bytes())
# ser.write(mido.Message('note_on', channel=0, note=71, velocity=80).bytes())
# time.sleep(1)
# ser.write(mido.Message('note_on', channel=0, note=64, velocity=0).bytes())
# ser.write(mido.Message('note_on', channel=0, note=67, velocity=0).bytes())
# ser.write(mido.Message('note_on', channel=0, note=71, velocity=0).bytes())
# time.sleep(1)
# ser.write(mido.Message('note_on', channel=0, note=65, velocity=80).bytes())
# ser.write(mido.Message('note_on', channel=0, note=69, velocity=80).bytes())
# ser.write(mido.Message('note_on', channel=0, note=72, velocity=80).bytes())
# time.sleep(1)
# ser.write(mido.Message('note_on', channel=0, note=65, velocity=0).bytes())
# ser.write(mido.Message('note_on', channel=0, note=69, velocity=0).bytes())
# ser.write(mido.Message('note_on', channel=0, note=72, velocity=0).bytes())
# time.sleep(1)
# ser.write(mido.Message('note_on', channel=0, note=67, velocity=80).bytes())
# ser.write(mido.Message('note_on', channel=0, note=71, velocity=80).bytes())
# ser.write(mido.Message('note_on', channel=0, note=74, velocity=80).bytes())
# time.sleep(1)
# ser.write(mido.Message('note_on', channel=0, note=67, velocity=0).bytes())
# ser.write(mido.Message('note_on', channel=0, note=71, velocity=0).bytes())
# ser.write(mido.Message('note_on', channel=0, note=74, velocity=0).bytes())
# time.sleep(1)
# ser.write(mido.Message('note_on', channel=0, note=69, velocity=80).bytes())
# ser.write(mido.Message('note_on', channel=0, note=72, velocity=80).bytes())
# ser.write(mido.Message('note_on', channel=0, note=76, velocity=80).bytes())
# time.sleep(1)
# ser.write(mido.Message('note_on', channel=0, note=69, velocity=0).bytes())
# ser.write(mido.Message('note_on', channel=0, note=72, velocity=0).bytes())
# ser.write(mido.Message('note_on', channel=0, note=76, velocity=0).bytes())

################### Velocity testen
# for i in range(5):
#     play_white_keys(a=36, b=84, ser=ser, velocity=30, sleeptime=0.025)
#     play_white_keys(a=36, b=84, ser=ser, velocity=50, sleeptime=0.025)
#     play_white_keys(a=36, b=84, ser=ser, velocity=70, sleeptime=0.025)
#     play_white_keys(a=36, b=84, ser=ser, velocity=90, sleeptime=0.025)
#     play_white_keys(a=36, b=84, ser=ser, velocity=110, sleeptime=0.025)
#     play_white_keys(a=36, b=84, ser=ser, velocity=127, sleeptime=0.025)


#############################
########## ARPEGGIOS ##########
############################
for i in range(2):
    play_white_keys(a=36, b=84, ser=ser, velocity=80, sleeptime=0.088, repeat=3)

# for i in range(5):
#     play_white_keys_descending(b=84, a=36, ser=ser, velocity=80, sleeptime=0.1)

# play_white_keys_incremental(a=36, b=84, ser=ser, velocity=80, sleeptime=0.025)
# play_white_keys_incremental_desc(b=84, a=36, ser=ser, velocity=80, sleeptime=0.025)

# for i in range(5):
    # play_white_keys(a=36, b=84, ser=ser, velocity=80, sleeptime=0.025)
    # play_white_keys_incremental(a=36, b=84, ser=ser, velocity=80, sleeptime=0.025)

###########################
########## SONGS ##########
###########################
# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/twinkle-twinkle-little-star.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/bleach-here-to-stay.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/bach_846.mid')
# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/bach_847.mid')
# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/bach_850.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/Pachelbel_Canon_in_C_Piano.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/Etude_Op.10_No.1_Waterfall_Chopin_in_C_Major.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/Mozart_Sonata_No._16_in_C_Major_Mvt_I_Allegro_1788.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/Invention_BWV_772_in_C_Major.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/Beethoven_-_Piano_Concerto_No._1_in_C_Major_Op._15_3rd_Movement_Transcribed_for_Piano.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/Toccata_Adagio_and_Fugue_in_C_major_BWV_564__Johann_Sebastian_Bach_Busoni_transcription_2nd._mov..mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/Waltz_in_A_MinorChopin.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/Concerto_in_A_minor_A_Vivaldi.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/Tarantella_in_A_minor.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/Pirates_Of_The_Caribbean__PinoPro.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/Liszt_Grandes_tudes_de_Paganini_in_A_Minor_Theme_and_Variations_S._141_No._6.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/Fantasia_in_D_Minor_K.397.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/W._A._Mozart_-_Dies_Irae_Piano_arr._by_Karl_Klindworth.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/Concerto_No._1_in_a_minor_-_Saint-Saens.mid')

# midi_file = mido.MidiFile('/home/mdlxxiii/piano/piano_robot_project/piano_robot_project_software/send_midi_data/midi_files/Adagio_from_Concerto_in_D_minor_BWV_974_by_A._Marcello-J.S._Bach_for_Violin_and_Piano.mid')

# midi_file = mido.MidiFile('piano_robot_project_software/send_midi_data/midi_files/Test_Klavier.mid')
# midi_file = mido.MidiFile('send_midi_data/midi_files/Hungarian Rhapsody No. 2 - Franz Liszt [MIDICollection.net].mid')

# play_midi_file(midi_file, ser) # Open the MIDI file as static for tests

# play_midi_file_one_channel(midi_file, 0, ser) # plays only notes on channel 0 (think thats left hand)

# play_midi_file(mido.MidiFile(sys.argv[1]), ser) # Open MIDI file dynamic as param in terminal -> brauche ich vllt auch nicht, da das auswählen der Midi Files direkt im Python File schneller ist wie im Terminal

time.sleep(1) # nicht unbedingt nötig denke ich, aber schön wenn der nicht instant den Port schließt nach dem letzten Byte finde ich

# Close the serial port
ser.close()



