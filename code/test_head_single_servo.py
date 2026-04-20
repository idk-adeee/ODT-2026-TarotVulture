from machine import Pin, PWM
import time

HEAD_PIN = 25
HEAD_DOWN = 30
HEAD_UP = 100

servo = PWM(Pin(HEAD_PIN), freq=50)


def angle_to_duty(angle):
    min_duty = 26
    max_duty = 128
    return int(min_duty + (max_duty - min_duty) * angle / 180)


while True:
    servo.duty(angle_to_duty(HEAD_DOWN))
    print("DOWN")
    time.sleep(2)

    servo.duty(angle_to_duty(HEAD_UP))
    print("UP")
    time.sleep(2)
