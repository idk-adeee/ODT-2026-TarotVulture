from machine import Pin, PWM
import time

SERVO_PIN = 27

servo = PWM(Pin(SERVO_PIN), freq=50)


def angle_to_duty(angle):
    min_duty = 26
    max_duty = 128
    return int(min_duty + (max_duty - min_duty) * angle / 180)


while True:
    servo.duty(angle_to_duty(20))
    print("20")
    time.sleep(2)

    servo.duty(angle_to_duty(90))
    print("90")
    time.sleep(2)

    servo.duty(angle_to_duty(160))
    print("160")
    time.sleep(2)
