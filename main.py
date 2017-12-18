# import RPi.GPIO as GPIO
import time
from rotator import getRotation
# rom active_buzzer import buzzer
# #from laser import laser_freq, laser_on, laser_off, laser_switch
import yeelight as yee


# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BOARD)

level_last = 0

# pinA = 38
# pinB = 36

# btn_status = False

yee.setup()

while True:

	# status = button_read(37)
	# if status >0:
	# 	if btn_status == False:	
	# 		btn_status = True
	# 	else:
	# 		btn_status = False
	# 	btn_switch(btn_status)
	#laser_freq(32,0.3)

	level = getRotation(38,36) %10
	if level==level_last:
		time.sleep(0.1)
	else:
		level_last = level
		yee.set_bright_all(level*10)
#	print level
	#buzzer(29,3)
