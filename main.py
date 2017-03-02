# main.py
# 3-LED-NeoPixel Stripe
# Just a test drive.

import ntptime
import utime
import time
import math
import machine
from machine import Pin
from neopixel import NeoPixel

pin = Pin(0, Pin.OUT)
np = NeoPixel(pin, 3)

while True:
    h=utime.localtime()[3]
    m=utime.localtime()[4]
    s=utime.localtime()[5]

    np[0] = (math.floor(255/24*h), 20, 20)
    np[1] = (20, 20, math.floor(255/60*m))
    np[2] = (255-math.floor(255/60*s), math.floor(255/60*s), 0)

    np.write()
    if(s%10==0):
        print(utime.localtime())
    if(h%4==0):
        ntptime.settime()
    time.sleep(1)
