import mido
import serial
import time

# =========================
# Arduino Serial Setup
# =========================
ser = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=115200,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

time.sleep(2)  # kurze Pause, damit Arduino bereit ist

# =========================
# MIDI Setup
# =========================
print("Verfügbare MIDI-Eingänge:")
for name in mido.get_input_names():
    print(f"  {name}")

midi_port_name = "VirMIDI 3-0"

print(f"\nÖffne MIDI-Eingang: {midi_port_name}")

# =========================
# Hauptloop
# =========================
try:
    with mido.open_input(midi_port_name) as inport:
        print("Empfange MIDI-Nachrichten... (Ctrl+C zum Beenden)")
        for msg in inport:
            print(msg)
            if msg.type in ['note_on', 'note_off']:
                # print(msg)  # Debug-Ausgabe

                # MIDI-Botschaft in Bytes umwandeln
                data = msg.bytes()

                # an Arduino weiterleiten
                ser.write(bytes(data))

except KeyboardInterrupt:
    print("\nAbbruch mit Ctrl+C erkannt.")
finally:
    ser.close()
    print("Serielle Verbindung geschlossen.")
