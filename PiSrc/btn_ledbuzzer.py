import RPi.GPIO as GPIO
import time

RED = 14
GREEN = 15
BLUE = 18

buttonPin = 17
piezoPin = 27

Melody = [500, 600, 700, 800, 900, 1000, 900, 800, 700, 600]

buttonCnt = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)
GPIO.setup(piezoPin, GPIO.OUT)

sound = GPIO.PWM(piezoPin, 440)
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
			GPIO.output(RED, GPIO.LOW)
			sound.start(50)
			for i in range(0, len(Melody)):
				sound.ChangeFrequency(Melody[i])
				time.sleep(0.1)
			sound.stop()
			GPIO.output(RED, GPIO.HIGH)
			print("Buzzer and LED ON!")
			
		elif (buttonCnt == 2):
			GPIO.output(RED, GPIO.HIGH)
			sound.stop()
		elif (buttonCnt == 3):
			buttonCnt = 1

		last_button_state = button_state
		time.sleep(0.2)

except KeyboardInterrupt:
	GPIO.cleanup()
