import RPi.GPIO as GPIO

led_pin = 11
button_pin = 12
led_state = False

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def button_event(channel): # This will be executed when button is pressed
    global led_state
    print(f'button_event GPIO {channel}')
    led_state = not led_state
    if led_state:
        print('LED turned on >>>')
    else:
        print('LED turned off <<<')
    GPIO.output(led_pin, led_state) 

def loop():
    GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=button_event, bouncetime=300)
    while True:
        pass

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    print ('Program starting...')
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
