import RPi.GPIO as GPIO
import time
import random

pins = [11, 12, 13]

def setup():
    global red, green, blue
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(pins, GPIO.OUT, initial=True)
    red = GPIO.PWM(pins[0], 2000)
    green = GPIO.PWM(pins[1], 2000)
    blue = GPIO.PWM(pins[2], 2000)
    red.start(0)
    green.start(0)
    blue.start(0)

def setcolor(_r, _g, _b):
    red.ChangeDutyCycle(_r)
    green.ChangeDutyCycle(_g)
    blue.ChangeDutyCycle(_b)

def loop():
    r = 0
    g = 0
    b = 0
    r_targ = random.randint(0,100)
    g_targ = random.randint(0,100)
    b_targ = random.randint(0,100)
    while True:
        setcolor(r, g, b)
        print(f'{r} ({r_targ}), {g} ({g_targ}), {b} ({b_targ})')
        print
        if r == r_targ and g == g_targ and b == b_targ:
            r_targ = random.randint(0,100)
            g_targ = random.randint(0,100)
            b_targ = random.randint(0,100)
        else:
            if r < r_targ:
                r = r + 1
            elif r > r_targ:
                r = r - 1
            if g < g_targ:
                g = g + 1
            elif g > g_targ:
                g = g - 1
            if b < b_targ:
                b = b + 1
            elif b > b_targ:
                b = b - 1
        time.sleep(.01)

def destroy():
    red.stop()
    green.stop()
    blue.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    print('Program starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
