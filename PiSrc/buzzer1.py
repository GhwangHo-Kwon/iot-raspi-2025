import RPi.GPIO as GPIO
import time

buzzerPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(buzzerPin, GPIO.OUT)

try:
	GPIO.output(buzzerPin, GPIO.HIGH)
	print("Buzzer ON")
	time.sleep(1)
	GPIO.output(buzzerPin, GPIO.LOW)
	print("Buzzer Off")

except KeyboardInterrupt:
	print("end...")
finally:
	GPIO.cleanup()
