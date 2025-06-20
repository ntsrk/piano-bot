import mido # https://github.com/mido/mido
import time

###############################
### functions for debugging ###
###############################
def play_notes_from_a_to_b(sleeptime, a, b, velocity, ser):
    while a<=b:
        note = a
        midi_msg_on = mido.Message('note_on', channel=0, note=note, velocity=velocity)
        midi_msg_off = mido.Message('note_on', channel=0, note=note, velocity=0)
        ser.write(midi_msg_on.bytes())
        print(midi_msg_on.bytes())
        time.sleep(sleeptime)
        ser.write(midi_msg_off.bytes())
        print(midi_msg_off.bytes())
        time.sleep(sleeptime)
        a = a + 1

def play_notes_from_b_to_a(sleeptime, a, b, velocity, ser):
    while b>=a:
        note = b
        midi_msg_on = mido.Message('note_on', channel=0, note=note, velocity=velocity)
        midi_msg_off = mido.Message('note_on', channel=0, note=note, velocity=0)
        ser.write(midi_msg_on.bytes())
        print(midi_msg_on.bytes())
        time.sleep(sleeptime)
        ser.write(midi_msg_off.bytes())
        print(midi_msg_off.bytes())
        time.sleep(sleeptime)
        b = b - 1

def play_notes_increment_a_to_b(a, b, velocity, sleeptime, ser):
    for end_note in range(a, b + 1):
        for note in range(a, end_note + 1):
            midi_msg_on = mido.Message('note_on', channel=0, note=note, velocity=velocity)
            ser.write(midi_msg_on.bytes())
            print(f"ON  {midi_msg_on.bytes()}")
            time.sleep(sleeptime)

            midi_msg_off = mido.Message('note_on', channel=0, note=note, velocity=0)
            ser.write(midi_msg_off.bytes())
            print(f"OFF {midi_msg_off.bytes()}")
            time.sleep(sleeptime)


def play_notes_increment_b_to_a(b, a, velocity, sleeptime, ser):
    for end_note in range(b, a - 1, -1):  # rückwärts von b bis a (inklusive)
        for note in range(b, end_note - 1, -1):  # spiele ab b bis aktuelle Grenze
            midi_msg_on = mido.Message('note_on', channel=0, note=note, velocity=velocity)
            ser.write(midi_msg_on.bytes())
            print(f"ON  {midi_msg_on.bytes()}")
            time.sleep(sleeptime)

            midi_msg_off = mido.Message('note_on', channel=0, note=note, velocity=0)
            ser.write(midi_msg_off.bytes())
            print(f"OFF {midi_msg_off.bytes()}")
            time.sleep(sleeptime)

def play_accord(note, velocity, ser):
    notes = [note, note + 2, note + 4]
    for note in notes:
        midi_msg = mido.Message('note_on', channel=0, note=note, velocity=velocity)
        ser.write(midi_msg.bytes())
        print(f"NOTE_ON {midi_msg.bytes()}")

def play_note(sleeptime, note, velocity, ser):
    midi_msg_on = mido.Message('note_on', channel=0, note=note, velocity=velocity)
    midi_msg_off = mido.Message('note_on', channel=0, note=note, velocity=0)
    ser.write(midi_msg_on.bytes())
    print(midi_msg_on.bytes())
    time.sleep(sleeptime)
    ser.write(midi_msg_off.bytes())
    print(midi_msg_off.bytes())
    time.sleep(sleeptime)

def play_repeating_note(repeat, sleeptime, note, velocity, ser):
    # Debug send only one key
    midi_msg_on = mido.Message('note_on', channel=0, note=note, velocity=velocity)
    midi_msg_off = mido.Message('note_on', channel=0, note=note, velocity=0)
    for i in range(repeat):
        ser.write(midi_msg_on.bytes())
        print(midi_msg_on.bytes())
        time.sleep(sleeptime)
        ser.write(midi_msg_off.bytes())
        print(midi_msg_off.bytes())
        time.sleep(sleeptime)

def play_repeating_note_getting_faster(startsleeptime, stopsleeptime, change, note, velocity, ser):
    # Debug send only one key
    midi_msg_on = mido.Message('note_on', channel=0, note=note, velocity=velocity)
    midi_msg_off = mido.Message('note_on', channel=0, note=note, velocity=0)
    while startsleeptime >= stopsleeptime:
        ser.write(midi_msg_on.bytes())
        print(midi_msg_on.bytes())
        time.sleep(startsleeptime)
        ser.write(midi_msg_off.bytes())
        print(midi_msg_off.bytes())
        time.sleep(startsleeptime)
        startsleeptime -= change

def play_repeating_note_getting_slower(startsleeptime, stopsleeptime, change, note, velocity, ser):
    # Debug send only one key
    midi_msg_on = mido.Message('note_on', channel=0, note=note, velocity=velocity)
    midi_msg_off = mido.Message('note_on', channel=0, note=note, velocity=0)
    while startsleeptime <= stopsleeptime:
        ser.write(midi_msg_on.bytes())
        print(midi_msg_on.bytes())
        time.sleep(startsleeptime)
        ser.write(midi_msg_off.bytes())
        print(midi_msg_off.bytes())
        time.sleep(startsleeptime)
        startsleeptime += change

################################
### functions for actual use ###
################################
def play_midi_file(midi_file, ser):
    for msg in midi_file.play():
        data = msg.bytes() # [144=status_byte->type of message and channel, 81=data_byte1->note, 52=data_byte2->velocity]    
        ser.write(data) # Send the bytes to the serial port
        # zum debuggen
        # print(msg)
        print(data)

# beispielsweise um nur die linke oder rechte Hand zu spielen
def play_midi_file_one_channel(midi_file, channel, ser):
    for msg in midi_file.play():
        if msg.channel == channel:
            data = msg.bytes()  
            ser.write(data) # Send the bytes to the serial port
            # zum debuggen
            # print(msg)
            print(data)

# midi file schneller oder langsamer abspielen lassen