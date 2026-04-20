from mfrc522 import MFRC522
import time

rfid = MFRC522(
    sck=18,
    mosi=23,
    miso=19,
    cs=5,
    rst=4
)

print("RFID TEST STARTED")
print("Tap a card on the reader")

last_uid = None

while True:
    uid = rfid.read_card()

    if uid:
        uid_str = ''.join('{:02X}'.format(b) for b in bytearray(uid)).upper()

        if uid_str != last_uid:
            print("CARD DETECTED")
            print("UID:", uid_str)
            last_uid = uid_str

        time.sleep_ms(500)
    else:
        last_uid = None

    time.sleep_ms(100)
