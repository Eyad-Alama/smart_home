import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(37,GPIO.IN) #signal


while True:

    value = GPIO.input(37)
    print value
    print "----------\n"
    time.sleep(0.1)
    
    