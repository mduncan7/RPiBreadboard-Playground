import RPi.GPIO as GPIO
import time

led_pins = [11,12,13,15,16,18,22,3,5,24]

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pins, GPIO.OUT)
    GPIO.output(led_pins, True)

def loop():
    while True:
        for pin in led_pins:
            GPIO.output(pin, False)
            time.sleep(.1)
            GPIO.output(pin, True)
        for pin in led_pins[::-1]:
            GPIO.output(pin, False)
            time.sleep(.1)
            GPIO.output(pin, True)

def destroy():
    GPIO.cleanup

if __name__ == '__main__':
    print('Program is starting...\n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()