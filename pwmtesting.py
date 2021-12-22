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
        _dc = input('Input 0-100: ')    # Input duty cycle for LED
        try:
            dc = int(_dc)
            try:
                p.ChangeDutyCycle(dc)
            except:
                print('Duty cycle must be between 0-100.')
        except ValueError:
            print('Input is not an integer.')

def destroy():
    p.stop()    # end PWM
    GPIO.cleanup()

if __name__ == '__main__':
    print('Program starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt or Exception:
        destroy()