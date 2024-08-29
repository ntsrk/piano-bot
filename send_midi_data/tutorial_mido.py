# doing this tutorial: https://www.twilio.com/en-us/blog/working-with-midi-data-in-python-using-mido

from mido import MidiFile

mid = MidiFile('midi_files/VampireKillerCV1.mid', clip=True)
# print(mid)

for track in mid.tracks:
    print(track)


