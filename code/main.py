from machine import Pin, PWM
from mfrc522 import MFRC522
import time
import random
import sys
import uselect

# =========================
# pins
# =========================
HEAD_LEFT_PIN = 21
HEAD_RIGHT_PIN = 22
BEAK_PIN = 26
EYES_PIN = 27
LED_PIN = 33
SWITCH_PIN = 32

RFID_SCK = 18
RFID_MOSI = 23
RFID_MISO = 19
RFID_CS = 5
RFID_RST = 4

# =========================
# press timing
# =========================
LONG_PRESS_MS = 1500

# =========================
# options
# =========================
USE_BEAK = True
USE_EYES = True
USE_AUDIO_SYNC = True
USE_LED = True

# =========================
# angles
# =========================
HEAD_DOWN = 30
HEAD_UP = 100

BEAK_CLOSED = 38
BEAK_OPEN = 72

EYES_CLOSED = 0
EYES_OPEN = 100

# =========================
# setup
# =========================
switch = Pin(SWITCH_PIN, Pin.IN, Pin.PULL_UP)

if USE_LED:
    led = Pin(LED_PIN, Pin.OUT)

head_left_servo = PWM(Pin(HEAD_LEFT_PIN), freq=50)
head_right_servo = PWM(Pin(HEAD_RIGHT_PIN), freq=50)

if USE_EYES:
    eyes_servo = PWM(Pin(EYES_PIN), freq=50)

if USE_BEAK:
    beak_servo = PWM(Pin(BEAK_PIN), freq=50)

rfid = MFRC522(
    sck=RFID_SCK,
    mosi=RFID_MOSI,
    miso=RFID_MISO,
    cs=RFID_CS,
    rst=RFID_RST
)

KNOWN_CARDS = {
    "8A9C5C10": "The Fool",
    "8223B55C": "The Magician",
    "2AA44C10": "The Hermit",
    "6A557710": "Death",
    "B3C1666D": "The Chariot",
    "AA725C10": "The Lovers",
    "2AAC5910": "The Devil",
    "7418255D": "The Empress",
    "AA096110": "The High Priestess",
    "348E235D": "The Wheel of Fortune"
}

poller = uselect.poll()
poller.register(sys.stdin, uselect.POLLIN)

# =========================
# servo helpers
# =========================
def angle_to_duty(angle):
    min_duty = 26
    max_duty = 128
    return int(min_duty + (max_duty - min_duty) * angle / 180)

def set_servo(servo, angle):
    servo.duty(angle_to_duty(angle))

def set_head(angle):
    angle = max(0, min(180, int(angle)))
    mirror_angle = 180 - angle
    set_servo(head_left_servo, angle)
    set_servo(head_right_servo, mirror_angle)

def set_idle_pose():
    set_head(HEAD_DOWN)

    if USE_EYES:
        set_servo(eyes_servo, EYES_CLOSED)

    if USE_BEAK:
        set_servo(beak_servo, BEAK_CLOSED)

    if USE_LED:
        led.value(0)

def open_eyes():
    if USE_EYES:
        set_servo(eyes_servo, EYES_OPEN)

def close_eyes():
    if USE_EYES:
        set_servo(eyes_servo, EYES_CLOSED)

def close_beak():
    if USE_BEAK:
        set_servo(beak_servo, BEAK_CLOSED)

def set_beak_from_amp(amp):
    if not USE_BEAK:
        return

    amp = max(0.0, min(1.0, amp))
    angle = int(BEAK_CLOSED + (BEAK_OPEN - BEAK_CLOSED) * amp)
    set_servo(beak_servo, angle)

def move_head_up():
    for angle in range(HEAD_DOWN, HEAD_UP + 1, 2):
        set_head(angle)
        time.sleep(0.04)

def move_head_down():
    for angle in range(HEAD_UP, HEAD_DOWN - 1, -2):
        set_head(angle)
        time.sleep(0.04)

def blink_once():
    if not USE_EYES:
        return

    close_eyes()
    time.sleep(random.uniform(0.08, 0.22))
    open_eyes()
    time.sleep(random.uniform(0.05, 0.18))

# =========================
# serial helpers
# =========================
def send_command(command):
    print(command)

def read_serial_line():
    if poller.poll(0):
        return sys.stdin.readline().strip()
    return None

# =========================
# switch helpers
# =========================
def wait_for_press_and_release():
    while switch.value() == 1:
        time.sleep(0.01)

    start = time.ticks_ms()

    while switch.value() == 0:
        time.sleep(0.01)

    duration = time.ticks_diff(time.ticks_ms(), start)
    time.sleep(0.2)
    return duration

def wait_for_confirm_press():
    print("WAIT_CONFIRM")
    wait_for_press_and_release()
    print("CONFIRMED")

def tarot_reset_pressed():
    return switch.value() == 0

# =========================
# card reading
# =========================
def wait_for_card():
    print("PLACE_CARD")

    card_locked = False
    missing_count = 0
    remove_threshold = 5

    while True:
        if tarot_reset_pressed():
            wait_for_press_and_release()
            print("RESET_TRIGGERED")
            return None

        uid = rfid.read_card()

        if uid:
            uid_str = ''.join('{:02X}'.format(b) for b in bytearray(uid)).upper()
            missing_count = 0

            if not card_locked:
                print("UID:" + uid_str)
                card_locked = True
                return uid_str

        else:
            if card_locked:
                missing_count += 1
                if missing_count >= remove_threshold:
                    card_locked = False
                    missing_count = 0

        time.sleep_ms(200)

# =========================
# movement during audio
# returns True if finished normally
# returns False if reset was pressed
# =========================
def animate_while_waiting(allow_reset=False):
    last_blink = time.ticks_ms()
    last_head_move = time.ticks_ms()
    audio_start = time.ticks_ms()

    beak_delay_ms = 700
    head_rest = HEAD_UP
    head_nod = max(HEAD_DOWN, HEAD_UP - 5)

    while True:
        if allow_reset and tarot_reset_pressed():
            wait_for_press_and_release()
            print("RESET_TRIGGERED")
            close_beak()
            set_head(HEAD_UP)
            open_eyes()
            return False

        line = read_serial_line()

        if line:
            if line == "DONE":
                close_beak()
                set_head(HEAD_UP)
                open_eyes()
                return True

            if line.startswith("AMP:") and USE_AUDIO_SYNC:
                try:
                    amp = float(line.split(":", 1)[1])
                except:
                    amp = 0.0

                if time.ticks_diff(time.ticks_ms(), audio_start) >= beak_delay_ms:
                    set_beak_from_amp(amp)

        if USE_EYES and time.ticks_diff(time.ticks_ms(), last_blink) > random.randint(1500, 2500):
            blink_once()
            last_blink = time.ticks_ms()

        if time.ticks_diff(time.ticks_ms(), last_head_move) > random.randint(2200, 4200):
            set_head(head_nod)
            time.sleep(0.18)
            set_head(head_rest)
            last_head_move = time.ticks_ms()

        time.sleep(0.03)

# =========================
# audio steps
# =========================
def play_intro_tarot():
    print("INTRO_TAROT_START")
    send_command("PLAY_INTRO_TAROT")
    ok = animate_while_waiting(allow_reset=True)
    print("INTRO_TAROT_DONE")
    return ok

def play_intro_yesno():
    print("INTRO_YESNO_START")
    send_command("PLAY_INTRO_YESNO")
    ok = animate_while_waiting(allow_reset=False)
    print("INTRO_YESNO_DONE")
    return ok

def play_fortune(uid):
    print("FORTUNE_START")
    send_command("PLAY_FORTUNE:" + uid)
    ok = animate_while_waiting(allow_reset=True)
    print("FORTUNE_DONE")
    return ok

def play_yesno_answer():
    print("YESNO_START")
    send_command("PLAY_YESNO")
    ok = animate_while_waiting(allow_reset=False)
    print("YESNO_DONE")
    return ok

def play_outro():
    print("OUTRO_START")
    send_command("PLAY_OUTRO")
    ok = animate_while_waiting(allow_reset=True)
    print("OUTRO_DONE")
    return ok

# =========================
# main show flow
# =========================
def wake_up():
    if USE_LED:
        led.value(1)

    move_head_up()
    open_eyes()
    close_beak()
    time.sleep(0.6)

def go_idle():
    time.sleep(0.5)
    move_head_down()
    close_eyes()
    close_beak()

    if USE_LED:
        led.value(0)

def run_tarot_show():
    print("MODE:TAROT")

    wake_up()

    if not play_intro_tarot():
        go_idle()
        return

    time.sleep(0.4)
    uid = wait_for_card()

    if uid is None:
        go_idle()
        return

    if uid in KNOWN_CARDS:
        print("Card:" + KNOWN_CARDS[uid])
    else:
        print("Unknown:" + uid)

    time.sleep(0.4)
    if not play_fortune(uid):
        go_idle()
        return

    time.sleep(0.4)
    if not play_outro():
        go_idle()
        return

    go_idle()

def run_yesno_show():
    print("MODE:YESNO")

    wake_up()
    play_intro_yesno()

    wait_for_confirm_press()

    time.sleep(0.6)
    play_yesno_answer()

    go_idle()

# =========================
# start
# =========================
set_idle_pose()
print("READY")

while True:
    if switch.value() == 0:
        press_time = wait_for_press_and_release()

        if press_time >= LONG_PRESS_MS:
            print("SHOW_START")
            run_tarot_show()
            print("SHOW_END")
        else:
            print("SHOW_START")
            run_yesno_show()
            print("SHOW_END")

    time.sleep(0.05)
