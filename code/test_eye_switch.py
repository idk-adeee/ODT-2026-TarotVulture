from machine import Pin, PWM
import time

EYES_PIN = 27
SWITCH_PIN = 32

EYES_CLOSED = 0
EYES_OPEN = 100

switch = Pin(SWITCH_PIN, Pin.IN, Pin.PULL_UP)
eyes_servo = PWM(Pin(EYES_PIN), freq=50)

eyes_open_now = False


def angle_to_duty(angle):
    min_duty = 26
    max_duty = 128
    return int(min_duty + (max_duty - min_duty) * angle / 180)


def set_eyes(angle):
    eyes_servo.duty(angle_to_duty(angle))


def move_eyes_slow(start_angle, end_angle):
    step = -1 if start_angle > end_angle else 1

    for angle in range(start_angle, end_angle + step, step):
        set_eyes(angle)
        time.sleep(0.02)


print("EYE SWITCH TEST")

last_switch = 1

while True:
    current_switch = switch.value()

    if last_switch == 1 and current_switch == 0:
        if eyes_open_now:
            print("EYES CLOSED")
            move_eyes_slow(EYES_OPEN, EYES_CLOSED)
            eyes_open_now = False
        else:
            print("EYES OPEN")
            move_eyes_slow(EYES_CLOSED, EYES_OPEN)
            eyes_open_now = True

        time.sleep(0.3)

    last_switch = current_switch
    time.sleep(0.05)
