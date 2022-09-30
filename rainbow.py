#!/usr/bin/python3
from neopixel import *
import numpy as np
import time
import logging

LEDCOUNT = 44 # Number of LEDs
GPIOPIN = 18
FREQ = 800000
DMA = 5
INVERT = True # Invert required when using inverting buffer
BRIGHTNESS = 255
strip = Adafruit_NeoPixel(LEDCOUNT, GPIOPIN, FREQ, DMA, INVERT, BRIGHTNESS)
# Intialize the library (must be called once before other functions).
strip.begin()

class RgbColor:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue

    def __eq__(self, other):
        return self.red == other.red and self.green == other.green and self.blue == other.blue


def set_color(color, wait_ms=0):
        for i in range(strip.numPixels()):
            strip.setPixelColor(i, Color(color.green, color.red, color.blue))
            strip.show()
            time.sleep(wait_ms/1000.0)


while True:
    # First LED white
    set_color(RgbColor(list(np.random.choice(range(256), size=3))),50)

