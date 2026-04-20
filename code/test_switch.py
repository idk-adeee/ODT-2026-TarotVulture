from machine import Pin
import time

switch = Pin(32, Pin.IN, Pin.PULL_UP)

while True:
    print(switch.value())
    time.sleep(0.2)
