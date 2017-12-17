import RPi.GPIO as GPIO
import time



def buzzer(pin,freq):
	GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
	GPIO.setup(pin,GPIO.OUT) #signal
	sleep = freq/100
	if freq==0:
		GPIO.output(pin,0)
	else:	
    	GPIO.output(pin,100)
    	time.sleep(sleep)
	    GPIO.output(pin,0)
    	time.sleep(sleep)
