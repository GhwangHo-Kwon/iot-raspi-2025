import RPi.GPIO as GPIO
import time

RED = 14
GREEN = 15
BLUE = 18

swPin = 17
swCnt = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(swPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

def printcallback(channel):
	global swCnt
	swCnt += 1
	time.sleep(0.2)
	if (swCnt == 1):
		GPIO.output(RED, GPIO.LOW)
		print("LED ON!")
	elif (swCnt >= 2):
		GPIO.output(RED, GPIO.HIGH)
		print("LED OFF!")
		swCnt = 0

GPIO.add_event_detect(swPin, GPIO.RISING, callback=printcallback)

try:
	while True:
		pass
except KeyboardInterrupt:
	GPIO.cleanup()
