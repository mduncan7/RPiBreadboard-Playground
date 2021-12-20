import RPi.GPIO as GPIO
import time

led_pin = 12

def setup():
    global p
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin, GPIO.OUT, initial=False)

    p = GPIO.PWM(led_pin, 500)  # Set PWM Frequency to 500Hz
    p.start(0)

def loop():
    while True:
        for dc in range (0, 101, 1):    # Make LED brighter
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(1)
        for dc in range (100, -1, -1):  # Make LED dimmer
            p.ChangeDutyCycle(dc)
            time.sleep(0.01)
        time.sleep(1)

def destroy():
    p.stop()    # end PWM
    GPIO.cleanup()

if __name__ == '__main__':
    print('Program starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()