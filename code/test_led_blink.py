from machine import Pin
import time

led = Pin(33, Pin.OUT)

while True:
    led.value(1)
    print("ON")
    time.sleep(1)

    led.value(0)
    print("OFF")
    time.sleep(1)
