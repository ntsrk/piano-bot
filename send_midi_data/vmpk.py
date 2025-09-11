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
# Hauptloop
# =========================
try:
    with mido.open_input() as inport:
        print("Empfange MIDI-Nachrichten... (Ctrl+C zum Beenden)")
        print("VMPK Output muss RtMidi In oder Midi Through sein um zu funktionieren!")
        for msg in inport:
            print(msg)
            if msg.type in ['note_on', 'note_off']:

                # MIDI-Botschaft in Bytes umwandeln
                data = msg.bytes()

                # an Arduino weiterleiten
                ser.write(bytes(data))

except KeyboardInterrupt:
    print("\nAbbruch mit Ctrl+C erkannt.")
finally:
    ser.close()
    print("Serielle Verbindung geschlossen.")
