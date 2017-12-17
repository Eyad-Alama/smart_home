import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pin,GPIO.OUT) #signal

def laser_on(pin):
    GPIO.output(pin,100)

def laser_off(pin):
    GPIO.output(pin,0)

def laser_switch(pin, status):
    if status==True:
        laser_on(pin)
    else:
        laser_off(pin)

def laser_freq(pin,freq):



    GPIO.output(pin,100)
    time.sleep(freq)
    GPIO.output(pin,0)
    time.sleep(freq)