import serial
import time
import os
import sys
import random
import threading
import numpy as np
import sounddevice as sd
import soundfile as sf

# =========================
# basic settings
# =========================
SERIAL_PORT = "COM5"
BAUD_RATE = 115200
MP3_FOLDER = "mp3"

# how often amplitude is sent to ESP32
AMP_INTERVAL = 0.05

# higher value = stronger beak movement
AMP_SCALE = 5.0

# =========================
# tarot intro / outro
# =========================
TAROT_INTRO_FILES = [
    "intro_1.mp3",
    "intro_2.mp3",
    "intro_3.mp3",
    "intro_4.mp3",
    "intro_5.mp3",
    "intro_6.mp3",
]

OUTRO_FILES = [
    "outro_1.mp3",
    "outro_2.mp3",
    "outro_3.mp3",
    "outro_4.mp3",
]

# =========================
# yes no maybe mode
# =========================
YESNO_INTRO_FILES = [
    "Question_1.mp3",
    "Question_2.mp3",
    "Question_3.mp3",
]

YESNO_MAP = {
    "YES": [
        "Yes_1.mp3",
        "Yes_2.mp3",
        "Yes_3.mp3",
        "Yes_4.mp3",
        "Yes_5.mp3",
        "Yes_6.mp3",
        "Yes_7.mp3",
        "Yes_8.mp3",
        "Yes_9.mp3",
        "Yes_10.mp3",
    ],
    "NO": [
        "No_1.mp3",
        "No_2.mp3",
        "No_3.mp3",
        "No_4.mp3",
        "No_5.mp3",
        "No_6.mp3",
        "No_7.mp3",
        "No_8.mp3",
        "No_9.mp3",
        "No_10.mp3",
    ],

}

# =========================
# tarot card audio
# =========================
CARD_MAP = {
    "8A9C5C10": ["TheFool_1.mp3", "TheFool_2.mp3", "TheFool_3.mp3", "TheFool_4.mp3"],
    "8223B55C": ["TheMagician_1.mp3", "TheMagician_2.mp3", "TheMagician_3.mp3", "TheMagician_4.mp3"],
    "2AA44C10": ["TheHermit_1.mp3", "TheHermit_2.mp3", "TheHermit_3.mp3", "TheHermit_4.mp3"],
    "6A557710": ["Death_1.mp3", "Death_2.mp3", "Death_3.mp3", "Death_4.mp3"],
    "B3C1666D": ["TheChariot_1.mp3", "TheChariot_2.mp3", "TheChariot_3.mp3", "TheChariot_4.mp3"],
    "AA725C10": ["TheLovers_1.mp3", "TheLovers_2.mp3", "TheLovers_3.mp3", "TheLovers_4.mp3", "TheLovers_5.mp3", "TheLovers_6.mp3"],
    "2AAC5910": ["TheDevil_1.mp3", "TheDevil_2.mp3", "TheDevil_3.mp3", "TheDevil_4.mp3"],
    "7418255D": ["TheEmpress_1.mp3", "TheEmpress_2.mp3", "TheEmpress_3.mp3", "TheEmpress_4.mp3"],
    "AA096110": ["TheHighPriestess_1.mp3", "TheHighPriestess_2.mp3", "TheHighPriestess_3.mp3", "TheHighPriestess_4.mp3"],
    "348E235D": ["TheWheelOfFortune_1.mp3", "TheWheelOfFortune_2.mp3", "TheWheelOfFortune_3.mp3", "TheWheelOfFortune_4.mp3", "TheWheelOfFortune_5.mp3"],
}

# =========================
# shared state
# =========================
current_amplitude = 0.0
playback_done = threading.Event()

# =========================
# play audio with amplitude tracking
# =========================
def play_audio_with_amplitude(filename):
    global current_amplitude

    filepath = os.path.join(MP3_FOLDER, filename)

    if not os.path.exists(filepath):
        print("File not found:", filepath)
        return False

    print("Loading:", filepath)

    try:
        samples, samplerate = sf.read(filepath, dtype="float32")
    except Exception as e:
        print("Error loading audio:", e)
        return False

    if samples.ndim > 1:
        mono = samples.mean(axis=1)
        channels = samples.shape[1]
    else:
        mono = samples
        channels = 1

    position = [0]

    def callback(outdata, frames, time_info, status):
        global current_amplitude

        start = position[0]
        end = start + frames
        chunk = samples[start:end]

        if len(chunk) < frames:
            if len(chunk) > 0:
                if channels == 1:
                    outdata[:len(chunk), 0] = chunk
                else:
                    outdata[:len(chunk)] = chunk
            outdata[len(chunk):] = 0
            position[0] = len(samples)
            raise sd.CallbackStop()
        else:
            if channels == 1:
                outdata[:, 0] = chunk
            else:
                outdata[:] = chunk
            position[0] = end

        mono_chunk = mono[start:end]
        if len(mono_chunk) > 0:
            rms = float(np.sqrt(np.mean(mono_chunk ** 2)))
            current_amplitude = min(1.0, rms * AMP_SCALE)

    def finished():
        playback_done.set()

    print("Playing:", filename)

    with sd.OutputStream(
        samplerate=samplerate,
        channels=channels,
        callback=callback,
        finished_callback=finished
    ):
        playback_done.wait()

    current_amplitude = 0.0
    print("Playback finished")
    return True

# =========================
# send amp values while audio plays
# =========================
def amplitude_sender(ser):
    while not playback_done.is_set():
        try:
            ser.write(f"AMP:{current_amplitude:.2f}\n".encode())
        except Exception:
            break
        time.sleep(AMP_INTERVAL)

    try:
        ser.write(b"AMP:0.00\n")
    except Exception:
        pass

# =========================
# handle one playback event
# =========================
def handle_playback(ser, filename):
    global current_amplitude

    playback_done.clear()
    current_amplitude = 0.0

    sender_thread = threading.Thread(target=amplitude_sender, args=(ser,), daemon=True)
    sender_thread.start()

    success = play_audio_with_amplitude(filename)

    sender_thread.join(timeout=1)

    if success:
        ser.write(b"DONE\n")

# =========================
# main serial loop
# =========================
def main():
    print("Connecting to ESP32 on", SERIAL_PORT)

    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
    except serial.SerialException as e:
        print("Could not open serial port:", e)
        sys.exit(1)

    time.sleep(2)
    print("Connected. Waiting for commands...\n")

    while True:
        line = ser.readline().decode("utf-8", errors="ignore").strip()

        if not line:
            continue

        print("ESP32:", line)

        if line == "PLAY_INTRO_TAROT":
            filename = random.choice(TAROT_INTRO_FILES)
            print("Chosen tarot intro:", filename)
            handle_playback(ser, filename)

        elif line == "PLAY_INTRO_YESNO":
            filename = random.choice(YESNO_INTRO_FILES)
            print("Chosen yes/no intro:", filename)
            handle_playback(ser, filename)

        elif line.startswith("PLAY_FORTUNE:"):
            uid = line.split(":", 1)[1].strip()

            if uid in CARD_MAP:
                filename = random.choice(CARD_MAP[uid])
                print("Chosen fortune:", filename)
                handle_playback(ser, filename)
            else:
                print("Unknown UID:", uid)
                ser.write(b"DONE\n")

        elif line == "PLAY_YESNO":
            category = random.choice(list(YESNO_MAP.keys()))
            filename = random.choice(YESNO_MAP[category])
            print("Chosen answer type:", category)
            print("Chosen answer file:", filename)
            handle_playback(ser, filename)

        elif line == "PLAY_OUTRO":
            filename = random.choice(OUTRO_FILES)
            print("Chosen outro:", filename)
            handle_playback(ser, filename)

if __name__ == "__main__":
    main()
