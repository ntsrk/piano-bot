import mido # https://github.com/mido/mido
import time

def play_function(midi_file, ser):
    for msg in midi_file.play():
        data = msg.bytes() # [144=status_byte->type of message and channel, 81=data_byte1->note, 52=data_byte2->velocity]    
        ser.write(data) # Send the bytes to the serial port
        # zum debuggen
        # print(msg)
        print(data)

def debug_repeat(repeat, sleeptime, note, velocity, ser):
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

def debug_faster(startsleeptime, stopsleeptime, change, note, velocity, ser):
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

def debug_slower(startsleeptime, stopsleeptime, change, note, velocity, ser):
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

# beispielsweise um nur die linke oder rechte Hand zu spielen
def play_one_channel(midi_file, channel, ser):
    for msg in midi_file.play():
        if msg.channel == channel:
            data = msg.bytes()  
            ser.write(data) # Send the bytes to the serial port
            # zum debuggen
            # print(msg)
            print(data)

# midi file schneller oder langsamer abspielen lassen