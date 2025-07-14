import RPi.GPIO as GPIO
import time

RED = 14
GREEN = 15
BLUE = 18
buttonPin = 17

buttonCnt = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

last_button_state = GPIO.HIGH

try:
	while True:
		button_state = GPIO.input(buttonPin)
		time.sleep(0.2)

		if (button_state == GPIO.LOW and last_button_state == GPIO.HIGH):
			buttonCnt += 1
			print(buttonCnt)
			time.sleep(0.2)

		if (buttonCnt == 1):
			GPIO.output(BLUE, GPIO.HIGH)
		elif (buttonCnt == 2):
			GPIO.output(RED, GPIO.LOW)
		elif (buttonCnt == 3):
			GPIO.output(RED, GPIO.HIGH)
			GPIO.output(GREEN, GPIO.LOW)
		elif (buttonCnt == 4):
			GPIO.output(GREEN, GPIO.HIGH)
			GPIO.output(BLUE, GPIO.LOW)
			buttonCnt = 0

		last_button_state = button_state
		time.sleep(0.2)
except KeyboardInterrupt:
	GPIO.cleanup()
