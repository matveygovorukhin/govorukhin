import RPi.GPIO as gpio
import sys
from time import sleep
gpio.setmode(gpio.BCM)
dac=[26, 19, 13, 6, 5, 11, 9, 10]
comp=4
troyka=17
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka,gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)

def perev(a):
    return [int (elem) for elem in bin(a)[2:].zfill(8)]

def adc():
    for i in range(256):
        daccc=perev(i)
        gpio.output(dac, daccc)
        compvalue=gpio.input(comp)
        sleep(0.005)
        if compvalue==0:
            return i

try:
    while True:
        i=adc()
        if i!=0:
            print(i, int(3.3*k/256*100)/100)
        
finally:
    gpio.output(dac, 0)
    gpio.cleanup()   
