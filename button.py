import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.IN) #signal

def button_read(pin):

	status = GPIO.input(pin)
	print status
	return status

	