import RPi.GPIO as GPIO
import time

# GPIO.setmode(GPIO.BCM)			# BCM mode 설정

RED = 14						# LED pin 설정
GREEN = 15
BLUE = 18

def set_led():
	time.sleep(1)
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(RED, GPIO.OUT)		# pin mode 설정
	GPIO.setup(GREEN, GPIO.OUT)
	GPIO.setup(BLUE, GPIO.OUT)

# VCC = GPIO.LOW, GROUND = GPIO.HIGH
# GPIO.output(RED, GPIO.LOW)			# 출력값 설정

while True:
	set_led()

	GPIO.output(RED, GPIO.LOW)
	time.sleep(1)
	GPIO.cleanup()
	set_led()

	GPIO.output(GREEN, GPIO.LOW)
	time.sleep(1)
	GPIO.cleanup()
	set_led()

	GPIO.output(BLUE, GPIO.LOW)
	time.sleep(1)
	GPIO.cleanup()
