from machine import Pin
import time

# use this to verify GPIO 32 changes from 1 to 0
# when directly touched to GND
switch = Pin(32, Pin.IN, Pin.PULL_UP)

print("WIRE TEST STARTED")

while True:
    print("GPIO32 =", switch.value())
    time.sleep(0.2)
