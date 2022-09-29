import RPi.GPIO as gpio
import sys
from time import sleep
gpio.setmode(gpio.BCM)
gpio.setup(2, gpio.OUT)
dac=[26, 19, 13, 6, 5, 11, 9, 10]
gpio.setup(dac, gpio.OUT)
try:
        p=gpio.PWM(2, 1000)
        p.start(100)
        input()
        p.stop()
            
finally:
    gpio.output(dac, 0)
    gpio.cleanup()   