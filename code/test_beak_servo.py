from machine import Pin, PWM
import time

BEAK_PIN = 26
BEAK_CLOSED = 38
BEAK_OPEN = 72

beak = PWM(Pin(BEAK_PIN), freq=50)


def angle_to_duty(angle):
    min_duty = 26
    max_duty = 128
    return int(min_duty + (max_duty - min_duty) * angle / 180)


while True:
    beak.duty(angle_to_duty(BEAK_CLOSED))
    print("BEAK CLOSED")
    time.sleep(2)

    beak.duty(angle_to_duty(BEAK_OPEN))
    print("BEAK OPEN")
    time.sleep(2)
