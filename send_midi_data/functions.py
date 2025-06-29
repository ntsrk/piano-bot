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

def is_white_key(midi_note):
    # Schwarze Tasten sind: C#, D#, F#, G#, A# (entspricht 1, 3, 6, 8, 10 mod 12)
    return midi_note % 12 not in [1, 3, 6, 8, 10]

def get_white_keys(a, b):
    return [note for note in range(a, b + 1) if is_white_key(note)]

def get_white_keys_desc(a, b):
    # a < b, aber rückwärts sortieren
    return [note for note in range(b, a - 1, -1) if is_white_key(note)]

def play_white_keys_incremental_desc(b, a, ser, velocity=80, sleeptime=0.2):
    white_keys = get_white_keys_desc(a, b)
    for i in range(1, len(white_keys) + 1):
        for note in white_keys[:i]:
            midi_msg_on = mido.Message('note_on', channel=0, note=note, velocity=velocity)
            ser.write(midi_msg_on.bytes())
            print("ON:", midi_msg_on.bytes())
            time.sleep(sleeptime)
            midi_msg_off = mido.Message('note_on', channel=0, note=note, velocity=0)
            ser.write(midi_msg_off.bytes())
            print("OFF:", midi_msg_off.bytes())
            time.sleep(sleeptime)

def play_white_keys_incremental(a, b, ser, velocity=80, sleeptime=0.2):
    white_keys = get_white_keys(a, b)
    for i in range(1, len(white_keys) + 1):
        for note in white_keys[:i]:
            midi_msg_on = mido.Message('note_on', channel=0, note=note, velocity=velocity)
            ser.write(midi_msg_on.bytes())
            print("ON:", midi_msg_on.bytes())
            time.sleep(sleeptime)
            midi_msg_off = mido.Message('note_on', channel=0, note=note, velocity=0)
            ser.write(midi_msg_off.bytes())
            print("OFF:", midi_msg_off.bytes())
            time.sleep(sleeptime)

def play_white_keys(a, b, ser, velocity=80, sleeptime=0.2):
    for note in range(a, b + 1):
        if is_white_key(note):
            midi_msg_on = mido.Message('note_on', channel=0, note=note, velocity=velocity)
            ser.write(midi_msg_on.bytes())
            print("ON:", midi_msg_on.bytes())
            time.sleep(sleeptime)
            midi_msg_off = mido.Message('note_on', channel=0, note=note, velocity=0)
            ser.write(midi_msg_off.bytes())
            print("OFF:", midi_msg_off.bytes())
            time.sleep(sleeptime)

def play_white_keys_descending(b, a, ser, velocity=80, sleeptime=0.2):
    for note in range(b, a - 1, -1):
        if is_white_key(note):
            midi_msg_on = mido.Message('note_on', channel=0, note=note, velocity=velocity)
            ser.write(midi_msg_on.bytes())
            print("ON:", midi_msg_on.bytes())
            time.sleep(sleeptime)
            midi_msg_off = mido.Message('note_on', channel=0, note=note, velocity=0)
            ser.write(midi_msg_off.bytes())
            print("OFF:", midi_msg_off.bytes())
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
    notes = [note, note + 4, note + 7]
    for note in notes:
        midi_msg = mido.Message('note_on', channel=0, note=note, velocity=velocity)
        ser.write(midi_msg.bytes())
        print(f"NOTE_ON {midi_msg.bytes()}")

def play_white_key_chord(note, velocity, ser):
    # Weiße Tasten sind 0,2,4,5,7,9,11 relative zu C in einer Oktave
    # Wir spielen note, note + 2, note + 4 (jeweils nur weiße Tasten)
    notes = [note, note + 2, note + 4]

    for n in notes:
        if 0 <= n <= 127:  # MIDI-Gültigkeitsbereich
            midi_msg = mido.Message('note_on', channel=0, note=n, velocity=velocity)
            ser.write(midi_msg.bytes())
            print(f"NOTE_ON {midi_msg.bytes()}")
        else:
            print(f"Warnung: Note {n} außerhalb gültigem MIDI-Bereich")


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