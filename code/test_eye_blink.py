from machine import Pin, PWM
import time

EYES_PIN = 27
EYES_CLOSED = 0
EYES_OPEN = 100

eyes_servo = PWM(Pin(EYES_PIN), freq=50)


def angle_to_duty(angle):
    min_duty = 26
    max_duty = 128
    return int(min_duty + (max_duty - min_duty) * angle / 180)


def set_eyes(angle):
    eyes_servo.duty(angle_to_duty(angle))


def open_eyes():
    set_eyes(EYES_OPEN)


def close_eyes():
    set_eyes(EYES_CLOSED)


def blink_once():
    close_eyes()
    time.sleep(0.25)
    open_eyes()
    time.sleep(0.25)


print("EYE BLINK TEST")
open_eyes()
time.sleep(1)

while True:
    blink_once()
    time.sleep(2)
