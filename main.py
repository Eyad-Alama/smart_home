import RPi.GPIO as GPIO
import time
from rotator import getRotation
#from active_buzzer import buzzer
#from laser import laser_freq, laser_on, laser_off, laser_switch
from yeelight import set_bright_all, setup

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)



pinA = 38
pinB = 36

btn_status = False

setup

while True:

	# status = button_read(37)
	# if status >0:
	# 	if btn_status == False:	
	# 		btn_status = True
	# 	else:
	# 		btn_status = False
	# 	btn_switch(btn_status)
	#laser_freq(32,0.3)
	level = getRotation(38,36)
	set_bright_all(level)
#	print level
	#buzzer(29,3)
