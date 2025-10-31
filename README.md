# Piano Bot

**A solenoid-powered piano-playing robot prototype** controlled by an **Arduino Uno**.  
**Python** sends MIDI data via **USB** to the Arduino, where a **C++ parser** translates note events into **PWM signals** on the correct pins — using **daisy-chained PCA9685 boards** for scalable output.

![Piano Bot Demo 1](demo/Pieczonka-Tarantella.mp4)
![Piano Bot Demo 2](demo/Stardew_Valley-The_Stardrop_Saloon.mp4)

*Click the videos above to watch the robot play in real time!*

**Pipeline:**
MIDI File → Python (USB) → Arduino Uno → Parser → PCA9685 Boards → Solenoids → Piano Keys

**Current specs:**
- **33 keys** (29 white + 4 black)
- **1.6 kHz** PWM frequency
- **24 V Solenoids** with **0.8 A peak current** per key

---

## Future Improvements

- **Increase PWM frequency to 25 kHz** — eliminate solenoid noise for silent operation  
- **Migrate to ESP32** — increase PWM Accuracy and Frequency Range  
- **Replace wiring with custom PCBs** — reduce clutter, improve reliability, and enable cleaner scaling  
- **Expand to full 88-key support** — complete the piano keyboard for professional-grade playback  
- **Add per-solenoid height adjustment** — enable dynamic key depth calibration (currently block-only)

