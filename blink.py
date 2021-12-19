import RPi.GPIO as GPIO
import time

led_pin = 11

def setup():
	GPIO.setmode(GPIO.BOARD) # use physical GPIO numbering
	GPIO.setup(led_pin, GPIO.OUT, initial=False) #Set the led_pin to output, initial level LOW 
	print(f'Using pin #{led_pin}.')

def loop():
	while True:
		GPIO.output(led_pin, True) # Turn on LED - True=1=GPIO.HIGH
		print('LED turned on')
		time.sleep(0.5)
		GPIO.output(led_pin, False) # Turn off LED - False=0=GPIO.LOW
		print('LED turned off')
		time.sleep(0.5)

def destroy():
	GPIO.cleanup() # Release all GPIO

if __name__ == '__main__':
	print ('Program starting...\n')
	setup()
	try:
		loop()
	except KeyboardInterrupt: # press ctrl+c to end the program
		destroy()
