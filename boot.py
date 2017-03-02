# This file is executed on every boot (including wake-boot from deepsleep)
# It establishes a network connection and sets the time with NTP.

import gc
import webrepl
import ntptime
import utime
import machine

webrepl.start()
gc.collect()

def do_connect():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect('<SSID>', '<Your Password>')
        while not sta_if.isconnected():
            pass
    print('network config:', sta_if.ifconfig())

do_connect()
ntptime.settime()
