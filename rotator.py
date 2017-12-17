import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pinA,GPIO.IN) #clck
GPIO.setup(pinB,GPIO.IN) #dt

encoderPosCount = 0
pinALast =0
aVal =0
bCW =0
pinA = 38
pinB = 36


#Read Pin A
#Whatever state it's in will reflect the last position
pinALast = GPIO.input(pinA)


#Serial.begin (9600);
#while True:
 # getRotation(38,36,10)
def getRotation(pinA, pinB, limit=100):
  global encoderPosCount
  global pinALast
  global aVal 
  global bCW
  aVal = GPIO.input(pinA)
  if aVal != pinALast: #Means the knob is rotating
    bVal = GPIO.input(pinB)
    if bVal != aVal:
      if encoderPosCount < limit:
        encoderPosCount +=1
      bCW = True
    else:
      bCW = False
      if encoderPosCount >0:
        encoderPosCount -=1
    print bCW
    print encoderPosCount
  pinALast = aVal
  return encoderPosCount
