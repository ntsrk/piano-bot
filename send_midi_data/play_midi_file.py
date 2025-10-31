import mido
import time
import serial
import sys
from functions import play_midi_file

def send_all_notes_off(ser):
    """
    Sendet Note Off-Befehle für alle MIDI-Noten (0-127) auf allen 16 Kanälen
    über die serielle Verbindung zum Arduino.
    """
    try:
        for channel in range(16):  # Alle MIDI-Kanäle (0-15)
            for note in range(128):  # Alle MIDI-Noten (0-127)
                msg = mido.Message('note_off', channel=channel, note=note, velocity=0)
                ser.write(msg.bytes())
                time.sleep(0.001)  # 1ms, Kurze Pause, um Arduino-Verarbeitung zu ermöglichen
        print("Alle Note Off-Nachrichten gesendet.")
    except serial.SerialException as e:
        print(f"Fehler bei serieller Kommunikation: {e}")
    except Exception as e:
        print(f"Fehler: {e}")

def main():
    # Konfiguriere serielle Verbindung
    try:
        ser = serial.Serial(
            port='/dev/ttyACM0',
            baudrate=115200,
            parity=serial.PARITY_NONE,
            stopbits=serial.STOPBITS_ONE,
            bytesize=serial.EIGHTBITS,
            timeout=2
        )
        if not ser.is_open:
            ser.open()
        print(f"Serielle Verbindung geöffnet: {ser.name}")
        time.sleep(2)  # Warte, bis Arduino bereit ist
    except serial.SerialException as e:
        print(f"Fehler beim Öffnen des Ports: {e}")
        return

    # Flag, um doppelte Note Off-Nachrichten zu vermeiden
    notes_off_sent = False

    try:
        # MIDI-Datei abspielen
        if len(sys.argv) < 2:
            print("Bitte gib eine MIDI-Datei als Argument an.")
            return
        play_midi_file(mido.MidiFile(sys.argv[1]), ser)
        time.sleep(1)
    except KeyboardInterrupt:
        print("\nCtrl+C erkannt: Alle Noten deaktivieren.")
        send_all_notes_off(ser)
        notes_off_sent = True  # Markiere, dass Noten ausgeschaltet wurden
    except Exception as e:
        print(f"Fehler beim Abspielen der MIDI-Datei: {e}")
    finally:
        # Schließe seriellen Port
        try:
            if not notes_off_sent:  # Nur senden, wenn nicht schon bei Ctrl+C gesendet
                send_all_notes_off(ser)
            ser.close()
            print("Serielle Verbindung geschlossen.")
        except serial.SerialException as e:
            print(f"Fehler beim Schließen des Ports: {e}")

if __name__ == "__main__":
    main()
