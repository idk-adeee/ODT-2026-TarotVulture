from machine import Pin, PWM
import time

LEFT_HEAD_PIN = 21
RIGHT_HEAD_PIN = 22
SWITCH_PIN = 32

HEAD_DOWN = 30
HEAD_UP = 100

switch = Pin(SWITCH_PIN, Pin.IN, Pin.PULL_UP)

left_servo = PWM(Pin(LEFT_HEAD_PIN), freq=50)
right_servo = PWM(Pin(RIGHT_HEAD_PIN), freq=50)

head_is_up = False


def angle_to_duty(angle):
    min_duty = 26
    max_duty = 128
    return int(min_duty + (max_duty - min_duty) * angle / 180)


def set_servo(servo, angle):
    servo.duty(angle_to_duty(angle))


def set_head(angle):
    mirror_angle = 180 - angle
    set_servo(left_servo, angle)
    set_servo(right_servo, mirror_angle)


def move_head(start_angle, end_angle):
    step = 2 if end_angle > start_angle else -2
    for angle in range(start_angle, end_angle + step, step):
        set_head(angle)
        time.sleep(0.04)


print("FORCING HEAD DOWN")
set_head(HEAD_DOWN)
time.sleep(1)

print("READY")
last_switch = 1

while True:
    current_switch = switch.value()

    if last_switch == 1 and current_switch == 0:
        print("SWITCH PRESSED")

        if head_is_up:
            print("HEAD DOWN")
            move_head(HEAD_UP, HEAD_DOWN)
            head_is_up = False
        else:
            print("HEAD UP")
            move_head(HEAD_DOWN, HEAD_UP)
            head_is_up = True

        time.sleep(0.3)

    last_switch = current_switch
    time.sleep(0.05)
