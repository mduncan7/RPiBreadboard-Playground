import RPi.GPIO as GPIO

led_pin = 11
button_pin = 12

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Set button_pin to PULL UP INPUT mode

def loop():
    while True:
        if GPIO.input(button_pin) == False:
            GPIO.output(led_pin, True)
        else:
            GPIO.output(led_pin, False)

def destroy():
    GPIO.cleanup

if __name__ == '__main__':
    print('Program is starting...\n')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()