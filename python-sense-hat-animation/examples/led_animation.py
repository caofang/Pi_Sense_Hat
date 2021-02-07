#!/usr/bin/python3
# Last update:        02/07/2021 by Fang
import argparse

from sense_hat import SenseHat
import time
import numpy as np
import time
# import ect
from random import randint
import sys
import signal

def line(image, point1, point2, color, timer):
    sense = SenseHat()
    image2 = image.reshape(8, 8, 3)

    x1 = point1[0]
    y1 = point1[1]
    x2 = point2[0]
    y2 = point2[1]
    dx = (x2 - x1)
    dy = (y2 - y1)

    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    Xincrement = dx / steps
    Yincrement = dy / steps
    x = x1
    y = y1

    for v in range(steps + 1):
        image2[int(y), int(x)] = color
        x = x + Xincrement
        y = y + Yincrement

    image3 = image2.reshape(64, 3)
    sense.set_pixels(image3)
    time.sleep(timer)
    return image3


def square(image, point1, point2, point3, point4, color, timer):
    sense = SenseHat()
    image2 = image.reshape(8, 8, 3)

    line(image2, point1, point2, color, 0)
    line(image2, point2, point3, color, 0)
    line(image2, point3, point4, color, 0)
    line(image2, point4, point1, color, 0)

    image3 = image2.reshape(64, 3)
    sense.set_pixels(image3)
    time.sleep(timer)

    return image3


def clear():
    sense = SenseHat()

    e = [0, 0, 0]

    image = np.array([
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e
    ])

    sense.set_pixels(image)


def handler_stop_signals(signalNumber, frame):
    print('Received:', signalNumber)
    clear()
    exit(0)


def registerSignals():
    # register the signals to be caught
    signal.signal(signal.SIGINT, handler_stop_signals)
    signal.signal(signal.SIGTERM, handler_stop_signals)


if __name__ == '__main__':
    print("===== start =====")
    
    registerSignals()

    w = [150, 150, 150]
    b = [0, 0, 255]
    e = [0, 0, 0]

    # create empty screen
    image = np.array([
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e,
        e, e, e, e, e, e, e, e
    ])

    print("LED square animation")
    while True:
        for x in range(5):
            square(image, [0, 0], [7, 0], [7, 7], [0, 7], [randint(0, 255), randint(0, 255), randint(0, 255)], .01)
            square(image, [1, 1], [6, 1], [6, 6], [1, 6], [randint(0, 255), randint(0, 255), randint(0, 255)], .01)
            square(image, [2, 2], [5, 2], [5, 5], [2, 5], [randint(0, 255), randint(0, 255), randint(0, 255)], .01)
